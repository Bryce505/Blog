# 随稿上传的图片

一篇稿子一个目录，目录名 = 稿件文件名去掉 `.md`：

```
drafts/我的稿子.md
drafts/images/我的稿子/图一.png
drafts/images/我的稿子/流程图.jpg
```

正文里按**文件名**引用，不写路径：`![](图一.png)`

流水线会就地转成 WebP（限宽 1200px）存进 `public/images/<slug>/`。
找不到的图会退到 Google Drive 按文件名找，还找不到就在正文里留「图片暂缺」
占位并计入校验失败。
