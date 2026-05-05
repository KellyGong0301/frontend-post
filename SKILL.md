---
name: frontend-post
description: Convert text into beautiful Xiaohongshu (小红书 / RED) image carousels. Use when the user wants to make 小红书图片、RED notes、图文笔记、图片排版、九宫格、朋友圈/微博图片. Generates 1080×1440 (3:4) or 1080×1080 (1:1) cards as a single HTML preview plus an optional Playwright script that exports each card to PNG. Includes 12 curated styles tuned for Chinese typography (奶油拿铁、莫兰迪、多巴胺、校园手账、极简黑白、港风胶片、杂志大字、暗黑科技、国风水墨、日系治愈、复古杂志、咖啡店黑板).
---

# Frontend Post

**定位：排版工具，不是内容生成器。** 用户提供文案 + 风格偏好，AI 按规则把它排成 1080×1440 / 1080×1080 的图——内容你说了算，AI 只负责"听话执行"。

输出：单个自包含 HTML 文件预览 + 可选脚本批量导出 PNG。

**12 个风格预设**：奶油拿铁、莫兰迪、多巴胺、校园手账、极简黑白、港风胶片、杂志大字、暗黑科技、国风水墨、日系治愈、复古杂志、咖啡店黑板。完整配色 / 字体 / 装饰元素 → `references/STYLE_PRESETS.md`。

封面标题钩子公式 → `references/HOOK_PATTERNS.md`。

> **⚠️ 合规提示（仅当用户明确要发到小红书时提醒）**：避免外链引导（"评论区扣 1"、"私信发你"、"GitHub 搜 X"）、诱导互动（"关注 + 收藏"）、和敏感钩子词（HOOK_PATTERNS.md 的"警告型"是高危区）。skill 内部保留所有套路，但生成给用户发布的内容必须脱敏。

---

## Phase 0: Detect Mode

- **Mode A — 新内容**：用户给主题或大纲 → Phase 1
- **Mode B — 文案改造**：用户已有一段长文案，要求拆成卡片 → Phase 1（跳过主题询问）
- **Mode C — 微调现有 HTML**：直接读文件改样式（始终保持像素固定 + 卡片不溢出）

---

## CRITICAL: 不可破坏的硬约束

### 1. 像素固定，不响应式

每张卡片是**固定像素**，不是 viewport：

```css
.card {
    width: 1080px;
    height: 1440px;       /* 3:4 默认。1:1 写 1080px。 */
    position: relative;
    overflow: hidden;     /* 内容溢出 = 你拆页 */
    box-sizing: border-box;
}
```

预览页用 `transform: scale()` 把卡片缩到屏幕能看见的大小，但 **生成的 PNG 必须是 1080px 宽**，否则上传到小红书会糊。

### 2. 内容密度上限（超量必拆页）

| 卡片类型 | 最大内容 |
|---|---|
| 封面 cover | 1 主标题（≤14 字）+ 1 副标题（≤20 字）+ 可选标签 1–2 个 |
| 干货列表 tip-list | 1 标题 + 3–5 条要点（每条 ≤16 字） |
| 知识卡 knowledge | 1 标题 + 1 段说明（≤80 字） |
| 对比卡 compare | 1 标题 + 2 列 ×（短标 + 3 条要点） |
| 步骤卡 steps | 1 标题 + 3–5 步骤（每步 ≤20 字） |
| 数据卡 data | 1 大数字 + 1 短说明（≤30 字） |
| 引言卡 quote | 1 金句（≤30 字）+ 出处 |
| 总结卡 summary | 1 标题 + 3–5 takeaway |
| 行动卡 cta | 1 呼吁（≤14 字）+ 1 引导动作 |

**规则**：超过上限 → 拆成多张。**绝对不要把字塞到 overflow: hidden 救命。**

### 3. 必须避开的 "AI 通用感"

**禁止**：
- 紫色渐变 + 白底（最廉价的 AI 配色）
- 默认 Inter / Roboto / 苹方系统字（中文一定要换成 Noto Serif SC、LXGW WenKai、Ma Shan Zheng、ZCOOL XiaoWei 等）
- 通用蓝色主色 (#3B82F6 / #2563EB)
- 浮夸的 emoji 堆叠（每张卡 emoji ≤ 3 个）
- 平均分布的对称排版（小红书要的是**有节奏的不平衡**）

**强制**：
- 配色严格 2–3 色（一主色 + 一辅色 + 一强调色）
- 标题字号至少 64–96px（封面甚至 120–180px）
- 留白 ≥ 卡片面积 30%
- 每个 preset 自带的"装饰元素"必须出现（贴纸、手绘箭头、圆角标签、网格线等）

### 4. 中文排版细节

```css
.card {
    font-family: "Noto Serif SC", "ZCOOL XiaoWei", "LXGW WenKai", serif;
    /* 中文换行 */
    word-break: break-all;
    /* 标点压缩 */
    text-spacing-trim: trim-start;
    /* 字间距，标题加 0.05em，正文不加 */
}

h1 { letter-spacing: 0.05em; line-height: 1.2; }
p  { line-height: 1.7; }
```

**字号节奏**：封面主标题 96–180px、副标题 32–48px、内页标题 64–96px、正文 28–40px、注释 22–26px。**别用 16px**，手机上看不见。

---

## Phase 1: Content Discovery

一次性问完：

1. **主题** / 已有文案？
2. **目标读者**（学生 / 职场新人 / 宝妈 / 程序员 / 生活博主受众…）
3. **卡片张数**：3（短）/ 5–7（标准）/ 9（深度）
4. **比例**：3:4（更长，能塞更多）还是 1:1（九宫格友好）
5. **是否要导出 PNG**（要 → 见 Phase 3 末尾的两种渲染方式）

如果用户给了大段文案，先把它**结构化**成：
- 1 个封面钩子（用 `references/HOOK_PATTERNS.md` 的公式之一）
- N 个内页（每页一个核心点）
- 1 个总结/CTA

把结构化结果先发给用户确认，再进入 Phase 2。

---

## Phase 2: Style Discovery

### Option A — 直接选

| Preset | 感觉 | 适合 |
|---|---|---|
| 奶油拿铁 Cream Latte | 温柔治愈 | 早餐/咖啡/读书笔记 |
| 莫兰迪 Morandi | 高级灰调 | 穿搭/家居/方法论 |
| 多巴胺 Dopamine | 鲜亮活泼 | 情绪 / 周末 / 学习打卡 |
| 校园手账 Campus Notebook | 学生手写 | 笔记 / 干货 / 考试 |
| 极简黑白 Minimal Mono | 高级商务 | 职场 / 干货 / 摄影 |
| 港风胶片 HK Film | 复古时尚 | 穿搭 / 旅游 / 城市 |
| 杂志大字 Magazine Display | 编辑感 | 观点 / 金句 / 文案 |
| 暗黑科技 Dark Tech | 科技博主 | AI / 编程 / 工具评测 |
| 国风水墨 Chinoiserie | 国风文艺 | 诗词 / 茶 / 节气 |
| 日系治愈 Japan Healing | 治愈安静 | 早安晚安 / 心情 |
| 复古杂志 Vintage Editorial | 文艺杂志 | 书影音 / 慢生活 |
| 咖啡店黑板 Cafe Chalkboard | 手写黑板 | 食谱 / 探店 / 课表 |

### Option B — 视觉发现（用户犹豫时默认走这条）

问："**你想让观众有什么感受？**"
- 治愈/温暖 → 奶油拿铁、日系治愈、咖啡店黑板
- 高级/冷静 → 莫兰迪、极简黑白、暗黑科技
- 兴奋/活泼 → 多巴胺、港风胶片、校园手账
- 文艺/思考 → 杂志大字、国风水墨、复古杂志

然后在 `.tmp-poster-previews/` 下生成 **3 个独立 HTML 预览文件**（每个只渲染一张封面 + 一张内页样张），告诉用户路径让 ta 选。

完整配色 / 字体 / 装饰元素清单 → 读 `references/STYLE_PRESETS.md`。

---

## Phase 3: Generate Output

### 文件结构

```
output/
├── index.html        # 单文件预览（所有卡片纵向排列，scale 缩放）
├── render.py         # （可选）批量 PNG 导出
└── images/           # （可选）用户提供的素材
```

### HTML 骨架

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>笔记标题</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;700;900&family=ZCOOL+XiaoWei&family=Ma+Shan+Zheng&family=Long+Cang&family=ZCOOL+KuaiLe&family=LXGW+WenKai&display=swap" rel="stylesheet">
<style>
  /* 1) 主题变量（每个 preset 一组） */
  :root {
    --bg: #F5EFE6;
    --ink: #4A3520;
    --accent: #D97757;
    --font-display: "ZCOOL XiaoWei", serif;
    --font-body: "Noto Serif SC", serif;
  }

  /* 2) 预览容器：把 1080px 卡片缩到 360px 显示 */
  body { background: #ECECEC; padding: 40px 0; }
  .deck { display: flex; flex-direction: column; align-items: center; gap: 32px; }
  .card-wrap {
    width: 360px; height: 480px;       /* 3:4 */
    /* width: 360px; height: 360px;    /* 1:1 时切换 */
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(0,0,0,.12);
    border-radius: 12px;
  }
  .card {
    width: 1080px; height: 1440px;     /* 真实尺寸 */
    transform: scale(0.3333);
    transform-origin: top left;
    background: var(--bg);
    color: var(--ink);
    font-family: var(--font-body);
    position: relative;
    overflow: hidden;
    padding: 96px 80px;
    box-sizing: border-box;
  }

  /* 3) 类型化字号 */
  .cover-title  { font-family: var(--font-display); font-size: 144px; line-height: 1.15; letter-spacing: 0.04em; font-weight: 900; }
  .cover-sub    { font-size: 40px; line-height: 1.6; opacity: .75; margin-top: 32px; }
  .page-title   { font-family: var(--font-display); font-size: 88px; line-height: 1.2; font-weight: 700; }
  .body         { font-size: 36px; line-height: 1.75; }
  .number-big   { font-size: 240px; font-weight: 900; line-height: 1; color: var(--accent); }
  .tag          { display: inline-block; padding: 8px 24px; border-radius: 999px; font-size: 28px; background: var(--accent); color: white; }

  /* 4) preset 的标志性装饰（举例：奶油拿铁的右上角圆点） */
  .deco-dot { position: absolute; top: 80px; right: 80px; width: 64px; height: 64px; border-radius: 50%; background: var(--accent); }

  /* 5) 打印 / 截图模式：去掉缩放和阴影 */
  @media print, (min-resolution: 200dpi) {
    body { background: white; padding: 0; }
    .card-wrap { width: 1080px; height: 1440px; box-shadow: none; border-radius: 0; }
    .card { transform: none; }
  }
</style>
</head>
<body>
<div class="deck">
  <!-- Cover -->
  <div class="card-wrap"><section class="card" id="card-1">
    <span class="tag">干货分享</span>
    <h1 class="cover-title">5 个让<br>笔记爆款<br>的标题公式</h1>
    <p class="cover-sub">90% 的博主都不知道</p>
    <div class="deco-dot"></div>
  </section></div>

  <!-- Knowledge / List / Quote / Steps / CTA cards... -->
</div>
</body>
</html>
```

### 导出 PNG —— 两种方式（按用户环境选）

**方式 A：Node + puppeteer-core（推荐，复用系统 Chrome，零下载）**

`scripts/render.js` 已打包在 skill 里。前置：用户系统装了 Node 和 Google Chrome（macOS 默认路径 `/Applications/Google Chrome.app/...`）。

```bash
cd output
npm init -y && npm install puppeteer-core
node ../scripts/render.js index.html png_output
```

**方式 B：Python + Playwright（跨平台稳定，但要下载 Chromium 约 200MB）**

`scripts/render.py` 也已打包。前置：Python 3.10–3.13（3.14 上 playwright 可能装不上）。

```bash
pip install playwright && playwright install chromium
python scripts/render.py output/index.html output/png
```

**输出**：`png_output/card_01.png` … `card_NN.png`，每张 2160×2880（retina 2x），上传小红书不糊。

---

## Phase 4: 质量自检（生成完必做）

逐张检查：

1. **封面钩子**：是不是 `references/HOOK_PATTERNS.md` 里的某个模式？还是干巴巴的标题？
2. **字数**：每张卡都在密度上限内？
3. **配色**：是不是只有 2–3 色？有没有混进 AI 通用紫蓝？
4. **字体**：中文字体是不是真的换了（不是默认苹方）？
5. **装饰元素**：preset 的标志性元素是不是出现了？
6. **节奏**：通读 N 张，有没有大字 / 小字 / 留白的轻重对比？
7. **像素**：`.card` 是不是严格 1080×1440 / 1080×1080？

任何一项不过 → 改。**不要交付平庸的 PNG。**

---

## Phase 5: Delivery

1. 删除 `.tmp-poster-previews/`（如果创建过）
2. 给用户：
   - `output/index.html`（直接浏览器打开预览）
   - 要 PNG → 跑 Phase 3 末尾两种渲染方式之一
3. 强调 **用户控制权**：
   - "改 `:root` 里的 `--bg / --ink / --accent` 换配色"
   - "改 `--font-display / --font-body` 换字体"
   - "或者直接告诉我'换成 XX 风格' / '字大一点' / '加贴纸'，我来改"
4. 问：风格、文案、配色、字体哪里还想调？

---

## 风格 → 感觉 速查

| 想要的感觉 | 默认配方 |
|---|---|
| 治愈温暖 | 米白 / 雾粉底 + 手写体 + 1 个暖色装饰，留白多 |
| 高级冷静 | 黑白灰为主 + 1 抹强对比色（荧光黄 / 朱红） |
| 活泼鲜亮 | 大色块对撞（粉+黄、蓝+橙）+ 圆角标签 + ZCOOL KuaiLe |
| 文艺思考 | 衬线大字 + 大量留白 + 浅色细线分割 |
| 国风 | 米白底 + 墨黑标题 + 朱红印章 + Ma Shan Zheng 题字 |
| 科技博主 | 深色底 + 单色荧光（青/绿）+ 等宽英文穿插 + 网格线 |

---

## 常见错误

- ❌ 用 viewport units（vw/vh）写卡片尺寸 → PNG 导出会变形
- ❌ 用系统默认字体 → 中文必出"AI 写文档"感
- ❌ emoji 堆 5 个以上 → 显得廉价
- ❌ 渐变背景 + 白字 → 99% 失败
- ❌ 一张卡塞 8 个要点 → 拆！
- ❌ 封面只写"干货分享" → 必须有钩子（数字 / 反差 / 提问 / 自爆）
