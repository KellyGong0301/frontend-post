# frontend-post

> Convert text into beautiful Xiaohongshu (小红书) image carousels. A **Claude Code skill** that lets you direct an LLM to lay out your content into 1080×1440 / 1080×1080 cards — you keep full control over style, color, font, and layout.

🇨🇳 **中文用户直接往下看，全文中文。**

---

## ✨ 这是什么

一个 **Claude Code Skill**——把文字变成小红书风格的图片排版。

**核心定位：排版工具，不是内容生成器。**
- 你提供文案 + 风格偏好 → AI 按规则把它排成图
- 内容你说了算，AI 只负责"听话执行"
- 配色 / 字体 / 装饰 / 留白 / 比例 全部可定制

**不是什么**：不是又一个 AI 自动产出口水文的工具。

## 🎨 12 套精选风格

不撞款，每套都有自己的脾气：

| 风格 | 调性 | 适合 |
|---|---|---|
| 奶油拿铁 | 温柔治愈 | 早餐 / 咖啡 / 读书笔记 |
| 莫兰迪 | 高级灰调 | 穿搭 / 家居 / 方法论 |
| 多巴胺 | 鲜亮活泼 | 情绪 / 周末 / 学习打卡 |
| 校园手账 | 学生手写 | 笔记 / 干货 / 考试 |
| 极简黑白 | 高级商务 | 职场 / 干货 / 摄影 |
| 港风胶片 | 复古时尚 | 穿搭 / 旅游 / 城市 |
| 杂志大字 | 编辑感 | 观点 / 金句 / 文案 |
| 暗黑科技 | 科技博主 | AI / 编程 / 工具评测 |
| 国风水墨 | 国风文艺 | 诗词 / 茶 / 节气 |
| 日系治愈 | 治愈安静 | 早安晚安 / 心情 |
| 复古杂志 | 文艺杂志 | 书影音 / 慢生活 |
| 咖啡店黑板 | 手写黑板 | 食谱 / 探店 / 课表 |

完整规范（配色 / 字体 / 装饰）见 [`references/STYLE_PRESETS.md`](references/STYLE_PRESETS.md)。

## 🚀 快速开始

### 1. 安装 skill

```bash
# 克隆到 Claude Code 的 skills 目录
git clone https://github.com/KellyGong0301/frontend-post.git ~/.claude/skills/frontend-post
```

或者直接把 `frontend-post/` 整个目录拷到 `~/.claude/skills/` 下。

### 2. 让 Claude Code 用它

在 Claude Code 里直接说：

> "帮我做一组小红书图，主题是 XXX，风格用奶油拿铁"

skill 会自动触发，问你内容、张数、比例，然后生成 `index.html` 预览。

### 3. 在浏览器里改

预览 HTML 里 `:root` 有所有可调变量：

```css
:root {
  --bg: #F5EFE6;          /* 背景色 */
  --ink: #4A3520;         /* 文字色 */
  --accent: #D97757;      /* 强调色 */
  --font-display: "ZCOOL XiaoWei", serif;  /* 标题字体 */
  --font-body: "Noto Serif SC", serif;     /* 正文字体 */
}
```

改这 5 个变量就能换整套风格。或者直接跟 Claude 说"换深色背景 / 字大一点 / 加贴纸"，它会改 HTML。

### 4. 导出 PNG

**方式 A — Node（推荐）**：复用系统 Chrome，零额外下载

```bash
cd output
npm init -y && npm install puppeteer-core
node ~/.claude/skills/frontend-post/scripts/render.js index.html png_output
```

**方式 B — Python**：跨平台稳定，但要下载 Chromium ~200MB

```bash
pip install playwright && playwright install chromium
python ~/.claude/skills/frontend-post/scripts/render.py output/index.html output/png
```

输出：`png_output/card_01.png … card_NN.png`，每张 2160×2880（retina 2x，传小红书不糊）。

## 📂 目录结构

```
frontend-post/
├── SKILL.md                          # 主流程（Claude 读这个）
├── README.md                         # 你正在看的这份
├── LICENSE                           # MIT
├── references/
│   ├── STYLE_PRESETS.md              # 12 套风格的 CSS / 字体 / 装饰规范
│   └── HOOK_PATTERNS.md              # 9 种封面标题钩子公式
└── scripts/
    ├── render.js                     # Node + puppeteer-core（推荐）
    └── render.py                     # Python + Playwright（跨平台）
```

## 🛡️ 小红书发布合规提示

如果产出图准备发到小红书，**避免以下高危区**（容易被判违规 / 限流）：

- ❌ "评论区扣 1 / 私信发你 / GitHub 搜 X" 等外链引导
- ❌ "关注 + 收藏 + 点赞" 等诱导互动
- ❌ HOOK_PATTERNS.md 里的 **警告型** 钩子（"千万别 X！"）容易被审
- ❌ 任何具体产品名 / 价格 / 联系方式

skill 内部所有套路都保留（让 AI 知道有这些手段），但**生成给你发布的内容会自动脱敏**。如果 Claude 没脱敏，跟它说一句"按合规版重写一下"。

## 💡 设计哲学

参考自 [openclaw-slides](https://github.com/zarazhangrui/openclaw-slides) 的方法论：

1. **强约束 > 自由发挥**：每张卡片字数硬上限，超量必拆，不让 LLM 把字塞到 overflow: hidden
2. **精选模板 > 通用风格**：12 套人格化预设，明确禁用 AI 通用紫蓝渐变 / 默认系统字
3. **用户控制 > AI 自动**：所有风格变量暴露在 `:root`，用户随时改
4. **像素固定 > 响应式**：1080×1440 严格像素，保证 PNG 不变形

## 📜 License

MIT — 自由使用、修改、分发。

## 🙏 致谢

- 灵感来自 [openclaw-slides](https://github.com/zarazhangrui/openclaw-slides)（Zara Zhang）的 skill 设计哲学
- 中文字体：[Google Fonts CJK](https://fonts.google.com/?subset=chinese-simplified)、[LXGW WenKai](https://github.com/lxgw/LxgwWenKai)
- 渲染引擎：[Puppeteer](https://pptr.dev/) / [Playwright](https://playwright.dev/)

---

**做的图发出去爆了不要忘了我** 🌟（开个玩笑，star 个仓库就行）
