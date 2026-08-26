"""校验未通过时的记录与通知。

三条出口，各自独立失败不影响其他两条：

1. 日志：写进 logs/verify-YYYY-MM.md，随产出一起提交，翻历史不用翻
   Actions 的日志页
2. GitHub Issue：零配置（用 Actions 自带的 GITHUB_TOKEN），手机上
   GitHub App 会推送，能直接在 issue 里追问和记录处理结果
3. 邮件：配了 SMTP 的 secret 才发，没配就跳过

通知本身失败绝不能让整条流水线失败 —— 文章已经写好落盘了，通知发不出去
是次要问题，抛异常反而会把产出一起丢掉。
"""
import datetime as dt
import os
import smtplib
from email.message import EmailMessage
from pathlib import Path


def log_path(blog_root, today=None):
    d = today or dt.date.today()
    return Path(blog_root) / 'logs' / f'verify-{d:%Y-%m}.md'


def write_log(blog_root, results, today=None):
    """把本次运行的校验结果按天追加进月度日志。返回日志路径。"""
    d = today or dt.date.today()
    p = log_path(blog_root, d)
    p.parent.mkdir(parents=True, exist_ok=True)
    lines = [] if p.exists() else [f'# 校验日志 {d:%Y-%m}', '',
                                   '每次发布运行的校验结果。未通过的文章带 `draft: true` 躺在 '
                                   '`src/content/posts/` 里等人工放行。', '']
    lines.append(f'## {d:%Y-%m-%d} {dt.datetime.now():%H:%M}')
    lines.append('')
    for r in results:
        if r.get('status') == 'error':
            lines.append(f'- **运行出错**：{r.get("reason")}')
            continue
        head = (f'- **{r.get("title") or r.get("slug")}**（{r.get("slug")}）'
                f'　{"通过" if r.get("ok") else "未通过"}')
        meta = []
        if r.get('mode'):
            meta.append(f'{"减法" if r["mode"] == "shrink" else "加法"}模式')
        if r.get('seedChars'):
            meta.append(f'{r["seedChars"]:,} → {r.get("articleChars", 0):,} 字符')
        if r.get('seed'):
            meta.append(f'引子：`{r["seed"]}`')
        if meta:
            head += '　' + '，'.join(meta)
        lines.append(head)
        for f in r.get('failures', []):
            lines.append(f'  - {f}')
    lines.append('')
    with p.open('a', encoding='utf-8') as fh:
        fh.write('\n'.join(lines) + '\n')
    return p


def _failed(results):
    return [r for r in results if r.get('status') == 'error' or not r.get('ok', True)]


def format_report(results):
    """通知正文：只讲未通过的那些，以及去哪儿处理。"""
    bad = _failed(results)
    out = [f'本次运行有 {len(bad)} 篇文章没通过校验，已带 draft 标落在 '
           f'src/content/posts/ 里，不会上线。', '']
    for r in bad:
        if r.get('status') == 'error':
            out += [f'■ 运行出错：{r.get("reason")}', '']
            continue
        out.append(f'■ {r.get("title") or r.get("slug")}')
        out.append(f'  文件：{r.get("file")}')
        if r.get('seed'):
            out.append(f'  引子笔记：{r["seed"]}')
        if r.get('mode'):
            out.append(f'  模式：{"减法" if r["mode"] == "shrink" else "加法"}　'
                       f'{r.get("seedChars", 0):,} → {r.get("articleChars", 0):,} 字符')
        out.append('  未通过的检查：')
        out += [f'    - {f}' for f in r.get('failures', [])]
        out.append('')
    out.append('处理方式：打开上面的文件，按问题逐条修改，确认没问题后'
               '删掉 frontmatter 里 `draft: true` 那一行即可发布。'
               '不想要就直接删掉整个文件，下次运行会自动销账、那篇笔记重新入列。')
    return '\n'.join(out)


def github_issue(title, body, _post=None):
    """在仓库里开一个 issue。缺环境变量就跳过，返回 None。"""
    import requests
    token = os.environ.get('GITHUB_TOKEN')
    repo = os.environ.get('GITHUB_REPOSITORY')
    if not token or not repo:
        return None
    post = _post or requests.post
    try:
        r = post(f'https://api.github.com/repos/{repo}/issues',
                 headers={'Authorization': f'Bearer {token}',
                          'Accept': 'application/vnd.github+json'},
                 json={'title': title, 'body': body, 'labels': ['校验未通过']},
                 timeout=30)
        return r.json().get('html_url') if r.status_code < 300 else f'失败 HTTP {r.status_code}'
    except Exception as e:
        return f'失败 {type(e).__name__}'


def send_mail(subject, body, _smtp=None):
    """SMTP 发信。没配 MAIL_* 环境变量就跳过，返回 None。

    QQ 邮箱要用「授权码」而不是登录密码，在邮箱设置 → 账号 → POP3/SMTP
    服务里生成。
    """
    host = os.environ.get('MAIL_HOST', 'smtp.qq.com')
    user = os.environ.get('MAIL_USER')
    password = os.environ.get('MAIL_PASSWORD')
    to = os.environ.get('MAIL_TO')
    if not (user and password and to):
        return None
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = user
    msg['To'] = to
    msg.set_content(body)
    try:
        smtp = _smtp or (lambda: smtplib.SMTP_SSL(host, 465, timeout=30))
        with smtp() as s:
            s.login(user, password)
            s.send_message(msg)
        return to
    except Exception as e:
        return f'失败 {type(e).__name__}'


def notify(blog_root, results, today=None):
    """写日志；有未通过的就开 issue、发邮件。返回各出口的结果。"""
    out = {'log': str(write_log(blog_root, results, today))}
    bad = _failed(results)
    if not bad:
        return out
    subject = f'[表征笔记] {len(bad)} 篇文章校验未通过 {dt.date.today():%Y-%m-%d}'
    report = format_report(results)
    out['issue'] = github_issue(subject, report)
    out['mail'] = send_mail(subject, report)
    return out
