import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

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

export const collections = { posts };
