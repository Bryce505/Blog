import { getCollection } from 'astro:content';

/**
 * 站点唯一的文章入口：草稿（`draft: true`）一律不参与构建。
 *
 * 没过校验的文章和正式文章同住 `src/content/posts/`，只靠 frontmatter 里的
 * 一行 draft 区分 —— 这样人工放行就只是「删掉那一行」，不用改名、移文件、
 * 补 published.json。代价是全站每一处文章列表都必须过滤，而全站有 10 处
 * `getCollection('posts')`，逐处加过滤迟早漏一处，漏一处就是未审内容上线。
 *
 * 所以收敛到这一个函数，并由 `pipeline/test_pipeline.py` 的
 * `test_site_never_reads_posts_collection_directly` 守住「别处不许裸调」。
 */
export async function listPosts() {
  return getCollection('posts', ({ data }) => !data.draft);
}
