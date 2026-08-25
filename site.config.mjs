/** 站点根路径。astro.config 与 remark 插件共用一个来源 —— 分开写必然漂移，
 *  而漂移的后果是正文里的图片和站内链接全部 404（实测踩过）。 */
export const SITE = 'https://bryce505.github.io';
export const BASE = '/Blog';
