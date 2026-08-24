import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context) {
  const posts = (await getCollection('posts')).sort((a, b) => b.data.date - a.data.date);
  return rss({
    title: '表征笔记',
    description: '生物医药 CMC 与分析方法的工作笔记',
    site: context.site,
    items: posts.map((p) => ({
      title: p.data.title,
      description: p.data.description,
      pubDate: p.data.date,
      categories: p.data.tags,
      link: `/posts/${p.id}/`,
    })),
    customData: '<language>zh-cn</language>',
  });
}
