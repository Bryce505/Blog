import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import { unified } from '@astrojs/markdown-remark';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import remarkCallout from './src/plugins/remark-callout.mjs';

export default defineConfig({
  site: 'https://bryce505.github.io',
  base: '/blog',
  integrations: [sitemap()],
  markdown: {
    // Astro 7 起默认处理器换成了 Sätteri；remark 插件要走 unified() 显式挂载
    // 实测待发布内容含 648 处 LaTeX（块级 160 + 行内 488），分布在 22/32 个
    // 分组里。不渲染的话七成文章会显示成一堆反斜杠。
    processor: unified({
      remarkPlugins: [remarkCallout, remarkMath],
      rehypePlugins: [[rehypeKatex, { throwOnError: false, strict: false }]],
    }),
    shikiConfig: {
      themes: { light: 'github-light', dark: 'github-dark' },
      wrap: false,
    },
  },
});
