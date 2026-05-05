# Style Presets — 详细规范

每个 preset 包含：**配色变量、字体配对、标志性装饰元素、不该做的事**。生成时直接把"主题变量"段拷到 `:root`，再叠加"装饰元素"片段。

---

## 1. 奶油拿铁 Cream Latte

**感觉**：温柔、治愈、咖啡馆早晨光线
**适合**：早餐 / 咖啡 / 读书笔记 / 日常分享

```css
:root {
  --bg: #F5EFE6;          /* 米色 */
  --bg-alt: #EBE0CC;
  --ink: #4A3520;         /* 深棕 */
  --ink-soft: #8B6F47;
  --accent: #D97757;      /* 焦糖橙 */
  --font-display: "ZCOOL XiaoWei", "Noto Serif SC", serif;
  --font-body: "Noto Serif SC", serif;
}
```

**装饰**：
- 右上角实心圆点（焦糖色，64px）
- 副标题前加细横线（80px × 2px）
- 卡片底部偶尔出现"☕"或手绘咖啡杯 SVG（最多 1 个）
- 段落间加米色细线 (`border-bottom: 1px solid var(--bg-alt)`)

**禁止**：高饱和度、霓虹色、硬阴影、纯白底。

---

## 2. 莫兰迪 Morandi

**感觉**：高级灰、克制、画廊感
**适合**：穿搭 / 家居 / 方法论 / 商业观点

```css
:root {
  --bg: #DDD5CB;          /* 灰米 */
  --bg-alt: #C8BFB3;
  --ink: #3E3A36;         /* 灰咖 */
  --ink-soft: #6B6560;
  --accent: #9CA39C;      /* 灰绿 */
  --accent2: #B8A89A;     /* 灰粉 */
  --font-display: "Noto Serif SC", "Cormorant Garamond", serif;
  --font-body: "Noto Sans SC", sans-serif;
}
```

**装饰**：
- 大色块分屏（左 1/3 灰绿，右 2/3 灰米）
- 标题旁竖排小字注释
- 极细 1px 分割线
- 数字用 Cormorant Garamond 斜体大写

**禁止**：圆角、emoji、手写体、粗描边。一切都要"安静"。

---

## 3. 多巴胺 Dopamine

**感觉**：鲜亮、活泼、上头
**适合**：周末 / 心情 / 学习打卡 / 美食

```css
:root {
  --bg: #FFE066;          /* 蛋黄 */
  --bg-alt: #FF6B9D;      /* 热粉 */
  --bg-alt2: #4DABF7;     /* 电蓝 */
  --ink: #1A1A1A;
  --accent: #FF6B35;      /* 橙红 */
  --font-display: "ZCOOL KuaiLe", "Noto Sans SC", sans-serif;
  --font-body: "Noto Sans SC", sans-serif;
}
```

**装饰**：
- 大色块对撞（同卡内出现 2 种亮色）
- 圆角标签 (`border-radius: 999px`)，描黑 3px 边
- 手绘风波浪线下划线（用 SVG）
- 数字裹彩色圆形背景

**禁止**：低饱和度、衬线体、深色背景、白底。

---

## 4. 校园手账 Campus Notebook

**感觉**：学生、手写、贴纸
**适合**：笔记 / 干货 / 考试 / 学习方法

```css
:root {
  --bg: #FDFBF5;          /* 米黄纸 */
  --bg-grid: #E8DFC9;
  --ink: #2C2826;
  --ink-pen: #2A4D8F;     /* 钢笔蓝 */
  --highlight: #FFE066;   /* 荧光黄 */
  --accent: #E84855;      /* 红笔 */
  --font-display: "LXGW WenKai", serif;
  --font-body: "LXGW WenKai", serif;
  --font-hand: "Long Cang", "Liu Jian Mao Cao", cursive;
}
```

**装饰**：
- 整卡背景细横线 (`background: linear-gradient(transparent 95%, var(--bg-grid) 95%); background-size: 100% 56px;`)
- 关键词加荧光笔背景 (`background: linear-gradient(transparent 60%, var(--highlight) 60%);`)
- 红笔批注用 `--font-hand`，倾斜 `transform: rotate(-3deg)`
- 贴纸：右上角带胶带感的小色块（几何形）
- 复选框 `□` 列表

**禁止**：渐变、霓虹、过度精致的设计。要"像真的本子"。

---

## 5. 极简黑白 Minimal Mono

**感觉**：高级、克制、商务
**适合**：职场 / 干货 / 摄影 / 思考

```css
:root {
  --bg: #FFFFFF;
  --ink: #0A0A0A;
  --ink-soft: #6E6E6E;
  --accent: #FF3D00;      /* 唯一一抹荧光（橙红 / 荧光黄 / 电青三选一） */
  --font-display: "Noto Sans SC", "Inter", sans-serif;
  --font-body: "Noto Sans SC", sans-serif;
}
```

**装饰**：
- 超大序号（240px+，黑色）作主视觉
- 左对齐 + 大量右侧留白
- 1px 分割线
- 标题加重点圆点 (`••`) 而不是 emoji
- 全卡只允许 1 处使用 `--accent`

**禁止**：装饰元素 ≥ 2 个、emoji、圆角 > 8px、手写体、渐变。

---

## 6. 港风胶片 HK Film

**感觉**：复古、霓虹、王家卫
**适合**：穿搭 / 旅游 / 城市 / 夜景

```css
:root {
  --bg: #1A0F1F;          /* 深紫黑 */
  --bg-alt: #2D1B3D;
  --ink: #F5E6D3;         /* 旧报纸黄 */
  --neon-pink: #FF2E92;
  --neon-cyan: #00F0FF;
  --accent: #FFB627;      /* 钨丝灯黄 */
  --font-display: "ZCOOL XiaoWei", "Bebas Neue", serif;
  --font-body: "Noto Serif SC", serif;
}
```

**装饰**：
- 卡片整体加颗粒噪点（CSS noise filter 或 SVG turbulence）
- 标题霓虹发光 (`text-shadow: 0 0 20px var(--neon-pink)`)
- 中英文混排（中文标题 + 英文小字）
- 边角 `border: 2px solid var(--accent)` 模仿胶片边框
- 时间戳样式数字（仿胶片日期）

**禁止**：纯净背景、扁平设计、亮色底。一定要有"做旧"质感。

---

## 7. 杂志大字 Magazine Display

**感觉**：编辑感、大字、强对比
**适合**：观点 / 金句 / 文案 / 读后感

```css
:root {
  --bg: #F8F5F0;
  --ink: #111111;
  --ink-soft: #555555;
  --accent: #C8102E;      /* 深红 */
  --font-display: "Cormorant Garamond", "Noto Serif SC", serif;
  --font-body: "Noto Serif SC", serif;
}
```

**装饰**：
- 巨型标题（180px+），可裁切出血
- 网格分栏（参考杂志 3 栏 / 6 栏）
- 章节号 `01 / 09` 角落小字
- 引文加左侧粗竖线 (`border-left: 6px solid var(--accent)`)
- 关键词用 `font-style: italic`

**禁止**：圆角、emoji、亮色、卡通元素。要严肃。

---

## 8. 暗黑科技 Dark Tech

**感觉**：科技博主、AI 工具评测
**适合**：AI / 编程 / 工具 / 数据

```css
:root {
  --bg: #0A0E1A;
  --bg-alt: #131829;
  --ink: #E8ECF1;
  --ink-soft: #8B95A7;
  --accent: #00FF94;      /* 荧光绿 */
  --accent2: #00D9FF;     /* 电青 */
  --font-display: "Noto Sans SC", sans-serif;
  --font-body: "Noto Sans SC", sans-serif;
  --font-mono: "JetBrains Mono", "Fira Code", monospace;
}
```

**装饰**：
- 背景细网格 (`background-image: linear-gradient(...)` 4% 不透明度)
- 数字、英文、版本号用 mono 字体
- 标题左侧带 `>` 终端提示符
- 进度条 / 数据条样式装饰
- 关键词加 `[ ]` 方括号

**禁止**：暖色调、衬线体、手写、卡通。

---

## 9. 国风水墨 Chinoiserie

**感觉**：东方、文人、节气
**适合**：诗词 / 茶 / 节气 / 传统文化

```css
:root {
  --bg: #F2EBDC;          /* 宣纸色 */
  --ink: #1A1A1A;         /* 墨黑 */
  --ink-soft: #5C5346;
  --accent: #B91C1C;      /* 朱砂 */
  --accent-gold: #B8860B;
  --font-display: "Ma Shan Zheng", "ZCOOL XiaoWei", serif;
  --font-body: "Noto Serif SC", serif;
}
```

**装饰**：
- 标题用毛笔字 `Ma Shan Zheng`，可竖排 (`writing-mode: vertical-rl`)
- 朱红印章方块（盖在右下角，旋转 -8°）
- 水墨晕染背景纹理（PNG 或 SVG 滤镜）
- 留白超过 50%
- 装饰用古典纹样（云纹 / 回字纹）极少量

**禁止**：现代字体作主标题、亮色块、emoji、圆角。

---

## 10. 日系治愈 Japan Healing

**感觉**：安静、柔软、晨光
**适合**：早安晚安 / 心情 / 散步

```css
:root {
  --bg: #FBF7F2;
  --bg-alt: #F0E5DC;
  --ink: #4A4034;
  --ink-soft: #8C7E6E;
  --accent: #C9A99C;      /* 雾粉 */
  --accent2: #A3B5A0;     /* 苔绿 */
  --font-display: "Noto Serif JP", "LXGW WenKai", serif;
  --font-body: "LXGW WenKai", serif;
}
```

**装饰**：
- 圆形或椭圆色块作背景图替代
- 极细圆角（4–8px）
- 标题旁加日文假名小字（如 "あさ / morning"）
- 底部短虚线 `border-bottom: 1px dashed`
- 手绘小图标（叶子 / 杯子，SVG，描边 1.5px）

**禁止**：高对比、霓虹、粗黑字、强烈情绪化文案。

---

## 11. 复古杂志 Vintage Editorial

**感觉**：70 年代杂志、文艺、慢生活
**适合**：书影音 / 慢生活 / 个人表达

```css
:root {
  --bg: #E8DCC4;          /* 米黄 */
  --ink: #2D2418;
  --accent: #8B2635;      /* 酒红 */
  --accent2: #2F4F2F;     /* 深绿 */
  --accent3: #C9A961;     /* 旧金 */
  --font-display: "Cormorant Garamond", "ZCOOL XiaoWei", serif;
  --font-body: "Noto Serif SC", serif;
}
```

**装饰**：
- 多色印刷错位感（标题加 `text-shadow: 2px 2px 0 var(--accent2)`）
- 页码、章节标记
- 装饰性圆角矩形边框
- 中英文标题对照
- 旧报纸网点纹理底纹

**禁止**：亮色、扁平极简、Sans-Serif 标题。

---

## 12. 咖啡店黑板 Cafe Chalkboard

**感觉**：手写黑板、温暖、生活
**适合**：食谱 / 探店 / 课表 / 待办

```css
:root {
  --bg: #2C2825;          /* 黑板深色 */
  --bg-noise: #3A3633;    /* 粉笔残留 */
  --ink: #F5F1E8;         /* 粉笔白 */
  --accent: #FFD93D;      /* 粉笔黄 */
  --accent2: #FF8E72;     /* 粉笔橘 */
  --accent3: #95E1D3;     /* 粉笔薄荷 */
  --font-display: "Long Cang", "Caveat", cursive;
  --font-body: "LXGW WenKai", serif;
}
```

**装饰**：
- 粉笔颗粒感 `text-shadow: 1px 1px 0 rgba(255,255,255,0.15)` + 微 blur
- 手绘箭头、波浪线、星星、圆圈强调（SVG，描边带不规则感）
- 重点项加白色虚线方框
- 角落画 ★ 或 ♥ 装饰
- 排版略微倾斜（每段 -1° 到 +1° 随机）

**禁止**：完美对齐的 grid、Sans-Serif、明亮背景。

---

## 字体加载

Google Fonts 一行（按需精简）：

```html
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;700;900&family=Noto+Sans+SC:wght@400;700;900&family=ZCOOL+XiaoWei&family=ZCOOL+KuaiLe&family=Ma+Shan+Zheng&family=LXGW+WenKai:wght@400;700&family=Long+Cang&family=Liu+Jian+Mao+Cao&family=Cormorant+Garamond:ital,wght@0,400;0,700;1,400&family=Noto+Serif+JP:wght@400;700&family=JetBrains+Mono:wght@400;700&family=Bebas+Neue&family=Caveat&display=swap" rel="stylesheet">
```

**注意**：LXGW WenKai 和 Long Cang 在 Google Fonts 上有，但加载略慢。如果用户在国内网络，建议下载 woff2 本地引用。

---

## 颜色组合速查（避免相邻色冲突）

主色 + 强调色绝对不能撞：

| 主色 | 安全强调色 | 危险（不要） |
|---|---|---|
| 米色系 | 焦糖、酒红、深绿 | 紫、电蓝 |
| 灰色系 | 朱红、荧光黄、深绿 | 浅粉、薄荷 |
| 亮色 | 白 / 黑 | 另一个亮色 |
| 深色底 | 单一荧光 | 多种荧光叠加 |
| 白底 | 黑 + 1 抹强色 | 多种中等饱和度色 |
