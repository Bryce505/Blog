import { getCollection } from 'astro:content';

import { listPosts } from './posts';

export interface SeriesItem {
  /** 已发布的文章条目；待发布条目为 null */
  post: any | null;
  title: string;
  /** 从 1 起的序号，含待发布条目 */
  no: number;
}

export interface ResolvedSeries {
  id: string;
  title: string;
  description: string;
  items: SeriesItem[];
  publishedCount: number;
}

export interface SeriesContext {
  series: ResolvedSeries;
  no: number;
  total: number;
  prev: SeriesItem | undefined;
  next: SeriesItem | undefined;
}

/** 把 series.json 的 entries 解析成文章对象，并做两项构建期硬校验。 */
export async function loadSeries(): Promise<ResolvedSeries[]> {
  const [seriesEntries, posts] = await Promise.all([
    getCollection('series'),
    listPosts(),
  ]);
  const byId = new Map(posts.map((p) => [p.id, p]));
  // 文章 id -> 已归属的系列 id，用于拦「一篇进了两个系列」
  const owner = new Map<string, string>();

  return seriesEntries.map((s) => {
    const items: SeriesItem[] = s.data.entries.map((e: any, i: number) => {
      const no = i + 1;
      if (!e.post) return { post: null, title: e.planned, no };

      const post = byId.get(e.post);
      // 打错的 id 必须让构建炸掉。若容许「找不到就当作待发布」，
      // 一个拼写错误会变成页面上一条看不出错的灰条目。
      if (!post) {
        throw new Error(
          `series.json：系列「${s.id}」的第 ${no} 条引用了不存在的文章 id「${e.post}」`,
        );
      }
      // 文章页的系列归属提示只有一处，属于两个系列时显示哪个都是错的。
      const prev = owner.get(e.post);
      if (prev) {
        throw new Error(
          `series.json：文章「${e.post}」同时属于系列「${prev}」和「${s.id}」`,
        );
      }
      owner.set(e.post, s.id);
      return { post, title: post.data.title, no };
    });

    return {
      id: s.id,
      title: s.data.title,
      description: s.data.description,
      items,
      publishedCount: items.filter((i) => i.post).length,
    };
  });
}

/** 找出某篇文章所属的系列及其上下篇；不属于任何系列返回 null。 */
export async function seriesContextOf(postId: string): Promise<SeriesContext | null> {
  for (const s of await loadSeries()) {
    const idx = s.items.findIndex((i) => i.post?.id === postId);
    if (idx === -1) continue;
    // 上下篇跳过待发布条目：它们没有页面可链
    const prev = [...s.items.slice(0, idx)].reverse().find((i) => i.post);
    const next = s.items.slice(idx + 1).find((i) => i.post);
    return { series: s, no: s.items[idx].no, total: s.items.length, prev, next };
  }
  return null;
}
