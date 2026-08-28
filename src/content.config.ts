import { defineCollection, z } from 'astro:content';
import { file, glob } from 'astro/loaders';
import { slug as githubSlug } from 'github-slugger';

// schema 要同时容得下两条通道的产出：自动通道（main.assemble_frontmatter）
// 和手动通道（drafts.fill_defaults）。手写稿只有 title 是必填的，
// 所以除 title/date 外一律给默认值。
const posts = defineCollection({
  loader: glob({
    pattern: '**/*.md',
    base: './src/content/posts',
    // 文章按年月分了子目录（src/content/posts/YYYY-MM/），但 id 必须继续
    // 只取文件名——[...slug].astro 直接拿 entry.id 当 URL，series.json 按
    // entry.id 匹配文章，两处都不该因为挪了目录就变。Astro 默认的
    // generateId 会把目录路径也编进 id，这里显式只取最后一段文件名。
    //
    // 只取文件名还不够：Astro 对没有目录前缀的单段路径，默认也会先过一遍
    // github-slugger 再当 id，不是原样用文件名（实测 17 篇现有文章里
    // HCP鉴定与定量.md 会被转成小写 hcp鉴定与定量）。这里必须复刻同一步，
    // 否则这一篇的 URL 会因为这次迁移悄悄变掉。
    generateId: ({ entry }) => githubSlug(entry.split('/').pop().replace(/\.md$/, '')),
  }),
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
    // 没过校验的文章跟正式文章同住 posts/，只靠这一行区分。放行 = 删掉这一行。
    // 过滤在 src/lib/posts.ts 的 listPosts() 里一处完成，别处不许裸调 getCollection。
    draft: z.boolean().nullable().default(false).transform((v) => v ?? false),
    // 没过哪几项。用 YAML 而不是 HTML 注释：GitHub 的 markdown 预览会把
    // <!-- --> 整段吃掉，人打开文件根本看不见问题清单（实测踩过）。
    reviewNotes: z.array(z.string()).nullable().default([]).transform((v) => v ?? []),
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
