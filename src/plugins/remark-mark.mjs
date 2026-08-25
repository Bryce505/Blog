import { visit, SKIP } from 'unist-util-visit';

const RE = /==(?=[^\s=])([\s\S]*?[^\s=])==/g;

/**
 * Obsidian 高亮 `==文字==` → `<mark>`。
 *
 * 源笔记里高亮的是术语定义和关键结论（实测质谱那篇正文就有十几处），
 * 不处理的话等号会原样印在页面上。GFM 不含这条语法，remark 也没内置。
 *
 * 只遍历 text 节点：行内代码是 inlineCode 节点，代码块是 code 节点，
 * 都不会被误伤；数学公式在 remark-math 那步已经变成 math 节点。
 */
export default function remarkMark() {
  return (tree) => {
    visit(tree, 'text', (node, index, parent) => {
      if (!parent || index === null || !node.value.includes('==')) return;

      const out = [];
      let last = 0;
      for (const m of node.value.matchAll(RE)) {
        if (m.index > last) out.push({ type: 'text', value: node.value.slice(last, m.index) });
        out.push({
          type: 'emphasis',
          data: { hName: 'mark' },
          children: [{ type: 'text', value: m[1] }],
        });
        last = m.index + m[0].length;
      }
      if (!out.length) return;
      if (last < node.value.length) out.push({ type: 'text', value: node.value.slice(last) });

      parent.children.splice(index, 1, ...out);
      return [SKIP, index + out.length];
    });
  };
}
