import { visit } from 'unist-util-visit';

const RE = /^\[!(\w+)\]([+-])?\s*(.*)$/;

/**
 * Obsidian callout：`> [!abstract] 标题` → `<aside class="callout callout-abstract">`
 *
 * 放在 Astro 构建期而不是 Python 流水线里：这是纯格式变换，一个插件处理
 * 全站，不必逐篇跑。实测源笔记里有 545 处。
 */
export default function remarkCallout() {
  return (tree) => {
    visit(tree, 'blockquote', (node) => {
      const first = node.children?.[0];
      if (first?.type !== 'paragraph') return;
      const text = first.children?.[0];
      if (text?.type !== 'text') return;

      const lines = text.value.split('\n');
      const m = RE.exec(lines[0]);
      if (!m) return;

      const [, kind, , label] = m;
      const rest = lines.slice(1).join('\n');
      if (rest) {
        text.value = rest;
      } else {
        first.children.shift();
        if (first.children.length === 0) node.children.shift();
      }

      node.data = {
        hName: 'aside',
        hProperties: { className: ['callout', `callout-${kind.toLowerCase()}`] },
      };
      node.children.unshift({
        type: 'paragraph',
        data: { hName: 'div', hProperties: { className: ['callout-title'] } },
        children: [{ type: 'text', value: label || kind }],
      });
    });
  };
}
