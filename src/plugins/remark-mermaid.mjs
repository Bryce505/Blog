import { visit } from 'unist-util-visit';

const ESC = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' };

/**
 * ```mermaid 代码块 → `<pre class="mermaid">`，交给浏览器端渲染成图。
 *
 * 必须在 remark 这一步拦掉：Shiki 认识 mermaid 语法，会把它当代码高亮，
 * 读者看到的就是一段带颜色的源码而不是流程图（实测待发布组里有 10 处，
 * 分布在 6 组）。换成 <pre class="mermaid"> 之后 Shiki 不再经手，
 * Post.astro 里的脚本按需加载 mermaid 把它渲染掉。
 */
export default function remarkMermaid() {
  return (tree) => {
    visit(tree, 'code', (node, index, parent) => {
      if (node.lang !== 'mermaid' || !parent || index === null) return;
      const src = node.value.replace(/[&<>"]/g, (c) => ESC[c]);
      parent.children[index] = {
        type: 'html',
        value: `<pre class="mermaid">${src}</pre>`,
      };
    });
  };
}
