import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import { unified } from '@astrojs/markdown-remark';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import remarkCallout from './src/plugins/remark-callout.mjs';
import remarkMark from './src/plugins/remark-mark.mjs';
import remarkBaseUrl from './src/plugins/remark-base-url.mjs';
import { SITE, BASE } from './site.config.mjs';

export default defineConfig({
  site: SITE,
  base: BASE,
  integrations: [sitemap()],
  markdown: {
    // Astro 7 起默认处理器换成了 Sätteri；remark 插件要走 unified() 显式挂载
    // 实测待发布内容含 648 处 LaTeX（块级 160 + 行内 488），分布在 22/32 个
    // 分组里。不渲染的话七成文章会显示成一堆反斜杠。
    processor: unified({
      // remarkBaseUrl 必须排在最后：前面的插件可能新增链接节点
      remarkPlugins: [remarkCallout, remarkMath, remarkMark, remarkBaseUrl],
      rehypePlugins: [[rehypeKatex, { throwOnError: false, strict: false }]],
    }),
    shikiConfig: {
      themes: { light: 'github-light', dark: 'github-dark' },
      wrap: false,
    },
  },
});
