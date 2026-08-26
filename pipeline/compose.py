"""调 DeepSeek 把一组笔记结构重组成一篇文章。

这是流水线里唯一不确定的部件 —— LLM 会犯错。所以它的输出必须过
verify.py 的机械校验才能发布，校验不过就带 draft 标等人工看。

系统提示固定不变且放在最前面，多篇文章复用同一段前缀，便于 prompt
caching 省下重复计费的 token。
"""
from pathlib import Path

import requests

import config

SYSTEM_PROMPT = (Path(__file__).parent / 'prompt.md').read_text(encoding='utf-8')
# 引子通道用另一套提示词：多篇重组要求「只重排不新增」，单篇扩写要求
# 「补原理与脉络、但一个新数字都不许出现」，两者的红线不同，不能共用。
SEED_PROMPT = (Path(__file__).parent / 'prompt_seed.md').read_text(encoding='utf-8')


class ComposeError(RuntimeError):
    """API 返回了非预期结构。余额不足、鉴权失败、模型名写错都会走这里。"""


def build_user_message(group):
    parts = [f'以下是 {len(group.notes)} 篇关于「{group.tag}」的笔记，'
             f'请打散重组成一篇文章。\n']
    for i, n in enumerate(group.notes, 1):
        meta = ' | '.join(x for x in (
            f'出处：《{n.book}》' if n.book else '',
            f'论文：{n.paper}' if n.paper else '',
            f'摘要：{n.description}' if n.description else '',
        ) if x)
        parts.append(f'\n### 笔记 {i}：{n.title}\n{meta}\n\n{n.body.strip()}\n')
    return ''.join(parts)


def build_seed_message(note):
    meta = ' | '.join(x for x in (
        f'出处：《{note.book}》' if note.book else '',
        f'论文：{note.paper}' if note.paper else '',
        f'摘要：{note.description}' if note.description else '',
    ) if x)
    return (f'以下这篇笔记是引子，请围绕它的主题写成一篇完整的文章。\n\n'
            f'### 笔记：{note.title}\n{meta}\n\n{note.body.strip()}\n')


def _post(url, headers, payload):
    r = requests.post(url, headers=headers, json=payload, timeout=600)
    r.raise_for_status()
    return r.json()


def _chat(system, user, api_key, model=None, _post=None):
    post = _post or globals()['_post']
    payload = {
        'model': model or config.DEEPSEEK_MODEL,
        'messages': [
            {'role': 'system', 'content': system},
            {'role': 'user', 'content': user},
        ],
        'temperature': config.DEEPSEEK_TEMPERATURE,
        'max_tokens': config.DEEPSEEK_MAX_TOKENS,
    }
    resp = post(config.DEEPSEEK_API_URL,
                {'Authorization': f'Bearer {api_key}',
                 'Content-Type': 'application/json'},
                payload)
    try:
        return resp['choices'][0]['message']['content'].strip()
    except (KeyError, IndexError, TypeError, AttributeError) as e:
        # 静默返回空文章会让下游校验报「正文过短」，掩盖真正的原因
        raise ComposeError(f'DeepSeek 响应缺少 choices: {resp}') from e


def compose(group, api_key, model=None, _post=None):
    """多篇笔记打散重组（自动通道）。"""
    return _chat(SYSTEM_PROMPT, build_user_message(group), api_key, model, _post)


def compose_seed(note, api_key, model=None, _post=None):
    """单篇笔记当引子（引子通道）。"""
    return _chat(SEED_PROMPT, build_seed_message(note), api_key, model, _post)


def compose_seed_message(user_message, api_key, model=None, _post=None):
    """引子通道：user message 由 seed.py 拼好（含加减法模式与相关片段）。"""
    return _chat(SEED_PROMPT, user_message, api_key, model, _post)
