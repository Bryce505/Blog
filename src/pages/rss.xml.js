import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

import { BASE } from '../../site.config.mjs';

// context.site 是不带 base 的站点根（https://bryce505.github.io），
// 直接拿来拼 /posts/<slug> 会得到一条条 404 的链接 —— 站点实际在 /Blog/ 下。
const base = BASE.replace(/\/$/, '');

export async function GET(context) {
  const posts = (await getCollection('posts')).sort((a, b) => b.data.date - a.data.date);
  return rss({
    title: '表征笔记',
    description: '生物医药 CMC 与分析方法的工作笔记',
    site: new URL(`${base}/`, context.site),
    items: posts.map((p) => ({
      title: p.data.title,
      description: p.data.description,
      pubDate: p.data.date,
      categories: p.data.tags,
      link: `${base}/posts/${p.id}/`,
    })),
    customData: '<language>zh-cn</language>',
  });
}
