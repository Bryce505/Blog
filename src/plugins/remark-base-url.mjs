import { visit } from 'unist-util-visit';

import { BASE } from '../../site.config.mjs';

/**
 * 给正文里的根路径补上站点 base。
 *
 * 站点部署在 `/Blog/` 下，但流水线写进 markdown 的是 `/images/<slug>/x.webp`
 * 和 `/posts/<slug>`。Astro 只对**相对路径**的图片做资源处理，根路径原样
 * 输出 —— 于是浏览器去请求 `bryce505.github.io/images/...`，全站图片 404。
 * 布局组件那边没事，它们用的是 import.meta.env.BASE_URL。
 *
 * 在这里补而不是让流水线写死 `/Blog/`：markdown 里不该出现部署路径，
 * 换仓库名或换域名时只动 site.config.mjs 一处。
 */
export default function remarkBaseUrl({ base = BASE } = {}) {
  const prefix = base.replace(/\/$/, '');
  const fix = (url) =>
    prefix && typeof url === 'string' && url.startsWith('/')
      && !url.startsWith('//') && !url.startsWith(`${prefix}/`)
      ? prefix + url
      : url;

  return (tree) => {
    visit(tree, ['image', 'link', 'definition'], (node) => {
      node.url = fix(node.url);
    });
  };
}
