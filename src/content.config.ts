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
    tags: z.array(z.string()).default([]),
    description: z.string().default(''),
    references: z.array(z.string()).default([]),
    sourceNotes: z.array(z.string()).default([]),
  }),
});

export const collections = { posts };
