import { defineCollection, z } from 'astro:content';
import { file, glob } from 'astro/loaders';

// schema 要同时容得下两条通道的产出：自动通道（main.assemble_frontmatter）
// 和手动通道（drafts.fill_defaults）。手写稿只有 title 是必填的，
// 所以除 title/date 外一律给默认值。
const posts = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/posts' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    category: z.string().default('杂记'),
    primaryTag: z.string().optional(),
    // 空列表在 YAML 里是 null（`references:` 后面直接跟下一个键），
    // 手写稿同样会这样写，所以一律 nullable 后再兜默认值
    tags: z.array(z.string()).nullable().default([]).transform((v) => v ?? []),
    description: z.string().nullable().default('').transform((v) => v ?? ''),
    references: z.array(z.string()).nullable().default([]).transform((v) => v ?? []),
    sourceNotes: z.array(z.string()).nullable().default([]).transform((v) => v ?? []),
  }),
});

// 系列的归属与顺序只存在这一个文件里：写进每篇文章的 frontmatter 的话，
// 调一次顺序要改 N 个文件，且两篇写了同一个序号没有任何东西会拦。
const series = defineCollection({
  loader: file('src/content/series.json'),
  schema: z.object({
    title: z.string(),
    description: z.string().default(''),
    // 每条 entry 恰好有 post 或 planned 之一。两者都写或都不写一律构建失败——
    // 手写 JSON 最容易把文章 id 打错，而打错的 id 绝不能静默退化成
    // 一条看不出错的「待发布」幽灵条目。
    entries: z.array(
      z.object({
        post: z.string().optional(),
        planned: z.string().optional(),
      }).refine((e) => !!e.post !== !!e.planned, {
        message: 'entry 必须恰好有 post 或 planned 之一',
      }),
    ).default([]),
  }),
});

export const collections = { posts, series };
