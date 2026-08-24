import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import remarkCallout from './src/plugins/remark-callout.mjs';

export default defineConfig({
  site: 'https://bryce505.github.io',
  base: '/blog',
  integrations: [sitemap()],
  markdown: {
    remarkPlugins: [remarkCallout],
    shikiConfig: {
      themes: { light: 'github-light', dark: 'github-dark' },
      wrap: false,
    },
  },
});
