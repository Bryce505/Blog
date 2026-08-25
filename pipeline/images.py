"""从 Google Drive 取图，转成站点自托管的 WebP。

Drive 只当取图来源，不当图床：它的图片直链有限流、会失效，拿来给公开
博客当 CDN 迟早出事。取下来转 WebP 提交进仓库，由 Pages 托管。

原图约 494 MB（1235 张），限宽 1200px 转 WebP 后约 74 MB，且随发布进度
逐步增长，git 仓库扛得住。
"""
import io
import json
import time
from pathlib import Path

from PIL import Image

import config


def drive_service(sa_json_str):
    """用服务账号建 Drive 只读客户端。

    别忘了把 image&attachment 文件夹共享给服务账号邮箱 —— 漏掉这步
    是取图全失败最常见的原因，且报错信息不直观。
    """
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    creds = service_account.Credentials.from_service_account_info(
        json.loads(sa_json_str),
        scopes=['https://www.googleapis.com/auth/drive.readonly'])
    return build('drive', 'v3', credentials=creds, cache_discovery=False)


def build_drive_index(service, folder_id):
    """递归遍历文件夹，建 文件名 → fileId 映射。"""
    index, stack = {}, [folder_id]
    while stack:
        fid = stack.pop()
        token = None
        while True:
            resp = service.files().list(
                q=f"'{fid}' in parents and trashed = false",
                fields='nextPageToken, files(id, name, mimeType)',
                pageSize=1000, pageToken=token).execute()
            for f in resp.get('files', []):
                if f['mimeType'] == 'application/vnd.google-apps.folder':
                    stack.append(f['id'])
                else:
                    index[f['name']] = f['id']
            token = resp.get('nextPageToken')
            if not token:
                break
    return index


def load_index(cache_path, factory, max_age_days=7):
    """索引缓存提交进仓库，避免每晚重新遍历整个 Drive 文件夹。

    缓存损坏或过期就重建，不让一个坏文件卡死流水线。
    """
    cache_path = Path(cache_path)
    if cache_path.exists():
        try:
            data = json.loads(cache_path.read_text(encoding='utf-8'))
            if time.time() - data.get('built_at', 0) < max_age_days * 86400:
                return data['index']
        except (json.JSONDecodeError, KeyError, OSError):
            pass
    index = factory()
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(
        json.dumps({'built_at': time.time(), 'index': index}, ensure_ascii=False),
        encoding='utf-8')
    return index


def to_webp(src_bytes, dest: Path):
    """限宽 1200px（等比，不放大），转 WebP。

    实测真实 vault 图片压缩到原大小的 10%：494 MB → 约 49 MB。

    ponytail: 只处理 Pillow 能打开的位图。Drive 上有 SVG，但实测待发布
    的 1273 张引用图全是 PNG/JPG，零 SVG，所以不加 SVG 直通路径。将来
    若笔记开始引用 SVG，在这里加一句「后缀是 .svg 就原样拷贝」即可。
    """
    img = Image.open(io.BytesIO(src_bytes))
    # 调色板图和带透明通道的截图直接存 WebP 会报错，先归一化
    if img.mode == 'P':
        img = img.convert('RGBA' if 'transparency' in img.info else 'RGB')
    elif img.mode not in ('RGB', 'RGBA'):
        img = img.convert('RGB')
    if img.width > config.IMAGE_MAX_WIDTH:
        h = round(img.height * config.IMAGE_MAX_WIDTH / img.width)
        img = img.resize((config.IMAGE_MAX_WIDTH, h), Image.LANCZOS)
    dest.parent.mkdir(parents=True, exist_ok=True)
    img.save(dest, 'WEBP', quality=config.WEBP_QUALITY)


def _download(service, fid):
    from googleapiclient.http import MediaIoBaseDownload
    buf = io.BytesIO()
    dl = MediaIoBaseDownload(buf, service.files().get_media(fileId=fid))
    done = False
    while not done:
        _, done = dl.next_chunk()
    return buf.getvalue()


def url_safe(name):
    """转义会撑破 markdown `![](...)` 语法的字符。

    Obsidian 的图片名大量带空格（Pasted image 2026...png、文献标题当文件名），
    裸空格会让整条图片语法当成纯文本印在页面上 —— 实测线上那篇质谱文章的
    「2011-Global quantification of mammalian gene expression control.webp」
    就是这么废掉的。

    中文不转义：浏览器和 Astro 都处理得了，转义了只会让 md 源文没法读。
    """
    return (name.replace('%', '%25').replace(' ', '%20')
                .replace('(', '%28').replace(')', '%29'))


def resolve(name, index):
    """文件名 → fileId。直接命中优先，落空再查 config.IMAGE_ALIASES。

    落盘仍用笔记里的引用名，不用 Drive 上的实际名：正文引用、占位标记、
    已下载文件三者对得上，重跑才幂等。
    """
    return index.get(name) or index.get(config.IMAGE_ALIASES.get(name, ''))


def copy_local(names, src_dir, out_dir, url_prefix):
    """本地目录里的图搬进 public/images/<slug>/ 并转 WebP。

    人工投稿用：随稿上传的图片放在 drafts/images/<稿件名>/ 下，按文件名
    对上就地转换，对不上的留给 Drive 那条路继续找。
    """
    src_dir, out_dir = Path(src_dir), Path(out_dir)
    mapping, missing = {}, []
    for name in names:
        dest = out_dir / (Path(name).stem + '.webp')
        if dest.exists():
            mapping[name] = f'{url_prefix}/{url_safe(dest.name)}'
            continue
        src = src_dir / name
        if not src.exists():
            missing.append(name)
            continue
        try:
            to_webp(src.read_bytes(), dest)
        except Exception:
            missing.append(name)
            continue
        mapping[name] = f'{url_prefix}/{url_safe(dest.name)}'
    return mapping, missing


def fetch_images(names, index, service, out_dir, url_prefix, _download=None):
    """返回 (文件名 → 站内路径, 找不到的文件名列表)。

    已存在的跳过，重跑幂等。找不到或转换失败的图记入 missing，由 render
    换成文字说明，不留破图。
    """
    download = _download or globals()['_download']
    mapping, missing = {}, []
    out_dir = Path(out_dir)
    for name in names:
        dest = out_dir / (Path(name).stem + '.webp')
        if dest.exists():
            mapping[name] = f'{url_prefix}/{url_safe(dest.name)}'
            continue
        fid = resolve(name, index)
        if not fid:
            missing.append(name)
            continue
        try:
            to_webp(download(service, fid), dest)
        except Exception:
            missing.append(name)
            continue
        mapping[name] = f'{url_prefix}/{url_safe(dest.name)}'
    return mapping, missing
