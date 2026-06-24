"""Additional HTML & CSS interview topics — expands htmlcss section to 50 total."""

from data.interview_content import InterviewItem

MARKET_ITEMS: dict[tuple[str, str], list[InterviewItem]] = {
    ("htmlcss", "foundation"): [
        InterviewItem(
            "css-display-property",
            "Explain the CSS display property and common values.",
            "Controls layout mode: block, inline, inline-block, flex, grid, none, and contents.",
            "",
            "css",
        ),
        InterviewItem(
            "css-position-values",
            "Explain CSS position: static, relative, absolute, fixed, and sticky.",
            "Positioning removes elements from normal flow or anchors them to a containing block or viewport.",
            "",
            "css",
        ),
        InterviewItem(
            "css-overflow",
            "What does CSS overflow control and when do you use it?",
            "Clips or scrolls content that exceeds an element's box — visible, hidden, scroll, auto, clip.",
            "",
            "css",
        ),
        InterviewItem(
            "html-data-attributes",
            "What are HTML data attributes and how are they used?",
            "Custom `data-*` attributes store metadata for JS, CSS, and testing without non-standard attributes.",
            "",
            "html",
        ),
        InterviewItem(
            "css-calc-clamp-min-max",
            "Explain CSS calc(), clamp(), min(), and max() functions.",
            "Dynamic sizing that mixes units and constrains values between bounds for fluid responsive layouts.",
            "",
            "css",
        ),
        InterviewItem(
            "css-aspect-ratio",
            "What is the CSS aspect-ratio property?",
            "Reserves proportional width-to-height space to prevent layout shift for media and cards.",
            "",
            "css",
        ),
        InterviewItem(
            "html-meta-tags-seo",
            "Which HTML meta tags matter for SEO?",
            "Title, description, canonical, robots, and structured data influence indexing and click-through.",
            "",
            "html",
        ),
    ],
    ("htmlcss", "intermediate"): [
        InterviewItem(
            "css-float-clearfix",
            "How do CSS float and clearfix work?",
            "Float pulls elements sideways; clearfix contains floated children so the parent expands correctly.",
            "",
            "css",
        ),
        InterviewItem(
            "css-object-fit",
            "What is CSS object-fit and object-position?",
            "Controls how replaced content (img, video) fills its box — cover, contain, fill, none, scale-down.",
            "",
            "css",
        ),
        InterviewItem(
            "html-canvas-basics",
            "What is the HTML canvas element used for?",
            "A bitmap drawing surface for charts, games, and image manipulation via the 2D or WebGL API.",
            "",
            "html",
        ),
        InterviewItem(
            "html-video-audio",
            "How do HTML video and audio elements work?",
            "Native media playback with controls, multiple sources, captions, and responsive embedding patterns.",
            "",
            "html",
        ),
        InterviewItem(
            "css-scroll-snap",
            "What is CSS scroll-snap?",
            "Snaps scroll positions to defined points for carousels and full-page sections.",
            "",
            "css",
        ),
        InterviewItem(
            "css-transforms",
            "Explain CSS transforms: translate, rotate, scale, and skew.",
            "GPU-accelerated visual transforms without triggering layout reflow.",
            "",
            "css",
        ),
        InterviewItem(
            "css-import-vs-link",
            "Compare CSS @import vs the HTML link element.",
            "@import is render-blocking and serial; link loads in parallel and is preferred for performance.",
            "",
            "css",
        ),
    ],
    ("htmlcss", "advanced"): [
        InterviewItem(
            "css-filter-backdrop-filter",
            "What are CSS filter and backdrop-filter?",
            "filter applies visual effects to an element; backdrop-filter blurs or tints content behind it.",
            "",
            "css",
        ),
        InterviewItem(
            "css-supports-at-rule",
            "What is the CSS @supports at-rule?",
            "Feature queries apply styles only when the browser supports a property-value pair.",
            "",
            "css",
        ),
        InterviewItem(
            "html-open-graph",
            "What are Open Graph meta tags?",
            "og:title, og:image, and og:description control link previews on social platforms.",
            "",
            "html",
        ),
        InterviewItem(
            "css-logical-properties",
            "What are CSS logical properties?",
            "Flow-relative properties (inline-start, block-size) adapt to writing mode and direction.",
            "",
            "css",
        ),
        InterviewItem(
            "html-dialog-element",
            "How does the native HTML dialog element work?",
            "Built-in modal with showModal(), ::backdrop, and focus trapping without a JS library.",
            "",
            "html",
        ),
        InterviewItem(
            "css-has-selector",
            "What is the CSS :has() selector?",
            "Parent/ancestor selector that matches elements containing a descendant that satisfies a condition.",
            "",
            "css",
        ),
    ],
}

for _items in MARKET_ITEMS.values():
    for item in _items:
        if not item.code.strip():
            item.code = "/* See detailed code example below */"

MARKET_DETAILED: dict[str, dict] = {
    "css-display-property": {
        "explanation": (
            "The **display** property defines how an element participates in layout and whether it generates "
            "a box at all. **block** elements stack vertically and stretch to full width; **inline** elements "
            "flow with text and ignore width/height. **inline-block** combines inline flow with block sizing. "
            "**flex** and **grid** enable one- and two-dimensional layout respectively. **none** removes the "
            "element from layout entirely (unlike visibility: hidden). **contents** makes the element's box "
            "disappear while its children remain — useful for semantic wrappers without affecting grid/flex. "
            "In interviews, connect display values to document flow and when you'd choose flex vs grid."
        ),
        "code": """/* Block vs inline */
nav { display: block; }          /* stacks, full width */
span.badge { display: inline; }  /* flows with text */

/* Inline-block — sized inline element */
.chip {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  border-radius: 999px;
}

/* Flex toolbar */
.toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
}

/* Grid dashboard */
.dashboard {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}

/* Hide from layout but keep in DOM for toggling */
.drawer--closed { display: none; }

/* Semantic wrapper that doesn't affect grid children */
.card-grid > .semantic-wrapper { display: contents; }""",
        "language": "css",
        "key_points": [
            "block stacks; inline flows with text",
            "flex = 1D layout; grid = 2D layout",
            "display: none removes from layout and accessibility tree",
            "inline-block allows width/height in text flow",
            "display: contents for semantic-only wrappers",
        ],
    },
    "css-position-values": {
        "explanation": (
            "The **position** property controls how an element is placed relative to the normal document flow. "
            "**static** is the default — no offset properties apply. **relative** keeps the element in flow but "
            "offsets it visually; it also establishes a containing block for absolutely positioned descendants. "
            "**absolute** removes the element from flow and positions it relative to the nearest positioned "
            "ancestor (not static). **fixed** anchors to the viewport — common for sticky headers and FAB buttons. "
            "**sticky** toggles between relative and fixed based on scroll threshold within its scroll container. "
            "Interview tip: always mention containing blocks and that fixed/sticky create stacking contexts."
        ),
        "code": """.card { position: relative; }

/* Badge anchored to card corner */
.card__badge {
  position: absolute;
  top: -8px;
  right: -8px;
}

/* Fixed site header */
.site-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
}

/* Sticky table header inside scrollable container */
.table-wrap { overflow: auto; max-height: 400px; }
.table-wrap thead th {
  position: sticky;
  top: 0;
  background: #fff;
  z-index: 1;
}

/* Relative nudge without leaving flow */
.icon--offset { position: relative; top: 2px; }""",
        "language": "css",
        "key_points": [
            "static — default, offsets ignored",
            "relative — in flow, offsets visually, contains absolute children",
            "absolute — out of flow, nearest positioned ancestor",
            "fixed — relative to viewport",
            "sticky — relative until scroll threshold, then fixed",
        ],
    },
    "css-overflow": {
        "explanation": (
            "**overflow** determines what happens when content exceeds an element's padding box. "
            "**visible** (default) lets content spill outside — can break layouts. **hidden** clips "
            "overflowing content with no scrollbars. **scroll** always shows scrollbars (or scroll "
            "containers). **auto** shows scrollbars only when needed. **overflow-x** and **overflow-y** "
            "control each axis independently. Modern **overflow: clip** clips without creating a scroll "
            "container. Overflow hidden/auto/scroll creates a **block formatting context** and is essential "
            "for containing floats, enabling scroll areas, and pairing with position: sticky."
        ),
        "code": """/* Scrollable sidebar */
.sidebar {
  overflow-y: auto;
  max-height: calc(100vh - 64px);
}

/* Truncate single-line text */
.truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/* Multi-line clamp (with line-clamp) */
.excerpt {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* Horizontal scroll for code blocks */
.code-block { overflow-x: auto; }

/* Clip without scroll container (modern) */
.avatar-ring { overflow: clip; border-radius: 50%; }""",
        "language": "css",
        "key_points": [
            "visible spills; hidden clips; auto/scroll enable scrolling",
            "overflow-x/y for axis-specific control",
            "overflow: auto creates scroll container for sticky",
            "Pair with text-overflow: ellipsis for truncation",
            "overflow: clip clips without scroll container",
        ],
    },
    "html-data-attributes": {
        "explanation": (
            "HTML **data attributes** (`data-*`) store custom metadata on elements in a valid, standards-compliant "
            "way. Any attribute starting with `data-` is accessible via **`element.dataset`** in JavaScript "
            "(camelCase: `data-order-id` → `dataset.orderId`). CSS can target them with attribute selectors "
            "like `[data-state=\"open\"]`. They are ideal for hooks used by JS frameworks, analytics, and "
            "testing (`data-testid`) without misusing non-standard attributes or classes meant for styling. "
            "Data attributes are not indexed for SEO and should not replace semantic HTML for accessibility."
        ),
        "code": """<!-- Store state and IDs for JS -->
<button
  data-action="delete"
  data-order-id="1042"
  aria-label="Delete order 1042">
  Delete
</button>

<!-- Toggle panel via data attribute -->
<div data-panel="shipping" data-expanded="false">...</div>

<!-- CSS hook -->
.tab[data-active="true"] {
  border-bottom: 2px solid var(--color-primary);
}

<!-- JS access -->
<script>
  const btn = document.querySelector('[data-action="delete"]');
  const orderId = btn.dataset.orderId; // "1042"
  btn.addEventListener('click', () => deleteOrder(orderId));
</script>""",
        "language": "html",
        "key_points": [
            "Any data-* name is valid HTML5",
            "dataset converts kebab-case to camelCase",
            "Use for JS hooks, not primary styling",
            "CSS attribute selectors can read data values",
            "Prefer semantic elements over data-only meaning",
        ],
    },
    "css-calc-clamp-min-max": {
        "explanation": (
            "CSS math functions enable **dynamic sizing** that responds to viewport and parent constraints. "
            "**calc()** adds, subtracts, multiplies, or divides mixed units — e.g. `calc(100% - 2rem)`. "
            "**min()** picks the smallest value; **max()** picks the largest. **clamp(min, preferred, max)** "
            "is the most interview-relevant: it clamps a preferred value between bounds — perfect for "
            "fluid typography and spacing without media queries. Always include spaces around `+` and `-` "
            "operators in calc(). These functions work inside any property that accepts a length or number."
        ),
        "code": """/* Sidebar width minus gutter */
.layout-main {
  width: calc(100% - 280px);
}

/* Fluid typography — 16px min, scales with viewport, 24px max */
h1 {
  font-size: clamp(1rem, 2.5vw + 0.5rem, 1.5rem);
}

/* Responsive card padding */
.card {
  padding: clamp(1rem, 3vw, 2rem);
}

/* min/max for flexible columns */
.hero {
  width: min(1200px, 100% - 2rem);
  margin-inline: auto;
}

/* calc with custom properties */
.modal {
  max-height: calc(100vh - var(--header-height, 64px));
}""",
        "language": "css",
        "key_points": [
            "calc() mixes units — spaces required around +/-",
            "clamp(min, preferred, max) for fluid sizing",
            "min()/max() pick smallest/largest argument",
            "Reduces need for many media query breakpoints",
            "Works with CSS custom properties",
        ],
    },
    "css-aspect-ratio": {
        "explanation": (
            "The **aspect-ratio** property sets a preferred width-to-height ratio before content loads, "
            "preventing **Cumulative Layout Shift (CLS)** — a Core Web Vital. Common values: `16 / 9`, "
            "`4 / 3`, or `1` for squares. It works on any element, not just replaced content. Combine "
            "with `width: 100%` and `object-fit: cover` on images inside a ratio box. Before aspect-ratio, "
            "developers used the padding-top percentage hack. In responsive layouts, aspect-ratio preserves "
            "proportions while width adapts to the container."
        ),
        "code": """/* 16:9 video embed */
.video-wrap {
  aspect-ratio: 16 / 9;
  width: 100%;
  background: #000;
}
.video-wrap iframe,
.video-wrap video {
  width: 100%;
  height: 100%;
}

/* Square product thumbnail */
.product-thumb {
  aspect-ratio: 1;
  object-fit: cover;
  width: 100%;
}

/* Card media area */
.card__media {
  aspect-ratio: 4 / 3;
  overflow: hidden;
}
.card__media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}""",
        "language": "css",
        "key_points": [
            "Prevents layout shift (CLS) for media",
            "Syntax: aspect-ratio: width / height",
            "Pair with object-fit: cover for images",
            "Replaces padding-top percentage hack",
            "Works on containers and replaced elements",
        ],
    },
    "html-meta-tags-seo": {
        "explanation": (
            "HTML **meta tags** in `<head>` provide metadata that search engines and browsers consume. "
            "The **title** tag is the strongest on-page SEO signal — unique per page, under ~60 characters. "
            "**meta description** influences snippet text in search results (not a ranking factor but affects "
            "click-through). **link rel=\"canonical\"** prevents duplicate-content issues when the same "
            "content has multiple URLs. **meta name=\"robots\"** controls indexing (`noindex`, `nofollow`). "
            "Use **hreflang** for multilingual sites. While meta keywords are ignored by Google, structured "
            "data (JSON-LD) complements meta tags for rich results."
        ),
        "code": """<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Order Management Dashboard | Acme Corp</title>
  <meta name="description"
        content="Track, fulfill, and report on customer orders in real time.">
  <link rel="canonical" href="https://app.acme.com/orders">
  <meta name="robots" content="index, follow">
  <!-- Multilingual -->
  <link rel="alternate" hreflang="en" href="https://app.acme.com/en/orders">
  <link rel="alternate" hreflang="es" href="https://app.acme.com/es/orders">
  <!-- Structured data -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Acme Order Dashboard"
  }
  </script>
</head>""",
        "language": "html",
        "key_points": [
            "Unique, descriptive title per page",
            "meta description affects snippet, not ranking",
            "canonical URL prevents duplicate content",
            "robots meta controls indexing",
            "JSON-LD structured data for rich results",
        ],
    },
    "css-float-clearfix": {
        "explanation": (
            "Before flexbox and grid, **float** was the primary tool for multi-column layouts and wrapping "
            "text around images. `float: left` or `float: right` pulls an element to one side; inline content "
            "wraps around it. Floated elements are removed from normal block flow, causing the **parent to "
            "collapse** if it has no in-flow content. **clear** (`clear: both`) forces an element below floats. "
            "The **clearfix hack** (often `::after { content: ''; display: table; clear: both; }`) makes the "
            "parent contain floats. Today prefer flex/grid, but float/clearfix still appears in legacy codebases "
            "and interviews testing CSS fundamentals."
        ),
        "code": """/* Float image with wrapping text */
.article img.float-left {
  float: left;
  margin: 0 1rem 1rem 0;
  max-width: 40%;
}

/* Clearfix on parent */
.article::after {
  content: '';
  display: table;
  clear: both;
}

/* Modern alternative — flow-root contains floats */
.article { display: flow-root; }

/* Clear footer below floated columns */
.footer { clear: both; }

/* Legacy two-column (prefer grid today) */
.sidebar { float: left; width: 240px; }
.main   { margin-left: 260px; }""",
        "language": "css",
        "key_points": [
            "Float removes element from block flow",
            "Parent collapses without clearfix or flow-root",
            "clear: both pushes element below floats",
            "display: flow-root is modern clearfix",
            "Prefer flex/grid for new layouts",
        ],
    },
    "css-object-fit": {
        "explanation": (
            "**object-fit** defines how replaced content (`<img>`, `<video>`, `<svg>`) fills its content box "
            "when aspect ratios differ. **cover** scales to fill, cropping edges — ideal for thumbnails. "
            "**contain** scales to fit entirely, possibly leaving letterboxing. **fill** stretches to fill "
            "(may distort). **none** and **scale-down** preserve intrinsic size. **object-position** "
            "(default `50% 50%`) controls which part is visible when cropped — e.g. `object-position: top` "
            "for portrait headshots. Pair with fixed dimensions or aspect-ratio for consistent card grids."
        ),
        "code": """/* Cover — fills box, crops overflow */
.avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  object-fit: cover;
  object-position: center;
}

/* Product grid — uniform tiles */
.product-grid img {
  width: 100%;
  aspect-ratio: 1;
  object-fit: cover;
  object-position: top;
}

/* Contain — full image visible */
.logo {
  width: 120px;
  height: 40px;
  object-fit: contain;
}

/* Hero background-style img */
.hero-img {
  width: 100%;
  height: 400px;
  object-fit: cover;
  object-position: center 20%;
}""",
        "language": "css",
        "key_points": [
            "cover fills and crops; contain fits entirely",
            "object-position controls crop focal point",
            "Works on img, video, svg",
            "Pair with aspect-ratio for responsive grids",
            "fill may distort — avoid for photos",
        ],
    },
    "html-canvas-basics": {
        "explanation": (
            "The **`<canvas>`** element provides a bitmap drawing surface manipulated via JavaScript — "
            "not with CSS or HTML markup inside. Get a **2D rendering context** with `canvas.getContext('2d')` "
            "or **WebGL** with `'webgl2'` for 3D. Common uses: charts (Chart.js), image filters, signatures, "
            "games, and PDF previews. Canvas resolution is controlled by `width`/`height` attributes (not CSS "
            "alone) — CSS scaling can blur if attribute size differs from display size. Canvas content is "
            "not accessible by default; provide text alternatives or use SVG for semantic graphics."
        ),
        "code": """<canvas id="chart" width="600" height="300"
          role="img" aria-label="Monthly revenue bar chart">
</canvas>

<script>
  const canvas = document.getElementById('chart');
  const ctx = canvas.getContext('2d');

  // Draw axes
  ctx.strokeStyle = '#ccc';
  ctx.beginPath();
  ctx.moveTo(40, 260); ctx.lineTo(580, 260);
  ctx.moveTo(40, 20);  ctx.lineTo(40, 260);
  ctx.stroke();

  // Draw bars
  const data = [120, 180, 95, 210, 160];
  data.forEach((val, i) => {
    const x = 60 + i * 100;
    const h = val;
    ctx.fillStyle = '#512BD4';
    ctx.fillRect(x, 260 - h, 60, h);
  });
</script>""",
        "language": "html",
        "key_points": [
            "Drawing is JavaScript-only — no DOM inside canvas",
            "Set width/height attributes for resolution",
            "2D context for charts; WebGL for 3D",
            "Not accessible — add aria-label or fallback",
            "SVG better for scalable, semantic graphics",
        ],
    },
    "html-video-audio": {
        "explanation": (
            "HTML5 **`<video>`** and **`<audio>`** provide native media playback without plugins. Use "
            "multiple **`<source>`** children with different formats (MP4/H.264, WebM/VP9, MP3) so browsers "
            "pick the first supported type. The **controls** attribute adds play/pause/volume UI. "
            "**poster** sets a thumbnail for video. **preload** hints loading behavior (`none`, `metadata`, "
            "auto). For accessibility, include **`<track kind=\"captions\">`** for subtitles. "
            "**playsinline** prevents fullscreen on iOS. Always provide fallback text inside the element."
        ),
        "code": """<!-- Responsive video with captions -->
<video controls playsinline poster="hero-poster.jpg"
       width="800" height="450" preload="metadata">
  <source src="demo.webm" type="video/webm">
  <source src="demo.mp4"  type="video/mp4">
  <track kind="captions" src="demo.vtt" srclang="en" label="English"
         default>
  Your browser does not support HTML5 video.
</video>

<!-- Background-style muted autoplay loop -->
<video autoplay muted loop playsinline aria-hidden="true">
  <source src="bg-loop.mp4" type="video/mp4">
</video>

<!-- Audio podcast episode -->
<audio controls preload="metadata">
  <source src="episode-42.mp3"  type="audio/mpeg">
  <source src="episode-42.ogg"  type="audio/ogg">
  Download the <a href="episode-42.mp3">MP3</a>.
</audio>""",
        "language": "html",
        "key_points": [
            "Multiple source elements for format fallback",
            "track kind=captions for accessibility",
            "poster for video thumbnail",
            "playsinline required for iOS inline playback",
            "autoplay needs muted for browser policy",
        ],
    },
    "css-scroll-snap": {
        "explanation": (
            "**CSS scroll snap** makes scroll containers land on defined points — ideal for carousels, "
            "image galleries, and full-page sections. On the **scroll container**, set `scroll-snap-type: "
            "x mandatory` (or `y`, `both`) and `overflow: auto/scroll`. On **children**, set "
            "`scroll-snap-align: start | center | end` and optionally `scroll-snap-stop: always` to "
            "prevent skipping slides. **scroll-padding** offsets snap points for fixed headers. "
            "Unlike JS carousels, scroll snap is native, accessible (keyboard scroll works), and "
            "performant. Combine with `scroll-behavior: smooth` for animated snapping."
        ),
        "code": """/* Horizontal carousel */
.carousel {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  gap: 1rem;
  -webkit-overflow-scrolling: touch;
}
.carousel__slide {
  flex: 0 0 100%;
  scroll-snap-align: start;
  scroll-snap-stop: always;
}

/* Full-page vertical sections */
.page-scroll {
  height: 100vh;
  overflow-y: scroll;
  scroll-snap-type: y mandatory;
  scroll-padding-top: 64px; /* fixed header offset */
}
.page-scroll section {
  min-height: 100vh;
  scroll-snap-align: start;
}""",
        "language": "css",
        "key_points": [
            "scroll-snap-type on scroll container",
            "scroll-snap-align on snap targets",
            "scroll-padding offsets for fixed headers",
            "Native, accessible alternative to JS carousels",
            "mandatory vs proximity snap strictness",
        ],
    },
    "css-transforms": {
        "explanation": (
            "CSS **transforms** visually modify elements with **translate**, **rotate**, **scale**, and "
            "**skew** without changing document flow — so they don't trigger layout reflow (good for "
            "performance). Use **transform-origin** to change the pivot point (default: center). "
            "Combine functions: `transform: translate(-50%, -50%) rotate(45deg) scale(1.1)`. "
            "3D transforms (`translateZ`, `rotateX/Y`) enable perspective effects. Transforms create a "
            "**stacking context** and promote layers for GPU compositing. Prefer transforms over "
            "top/left for animations — pair with transitions for smooth hover effects."
        ),
        "code": """/* Center overlay absolutely */
.modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

/* Hover lift effect */
.card {
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.card:hover {
  transform: translateY(-4px) scale(1.02);
  box-shadow: 0 8px 24px rgba(0,0,0,0.12);
}

/* Rotate chevron when open */
.accordion__icon { transition: transform 0.2s; }
.accordion[open] .accordion__icon {
  transform: rotate(180deg);
}

/* 3D flip card */
.flip-card__inner {
  transition: transform 0.6s;
  transform-style: preserve-3d;
}
.flip-card:hover .flip-card__inner {
  transform: rotateY(180deg);
}""",
        "language": "css",
        "key_points": [
            "Transforms don't affect layout flow",
            "translate/rotate/scale/skew combine in one property",
            "transform-origin sets pivot point",
            "GPU-composited — good for animations",
            "Creates stacking context — affects z-index",
        ],
    },
    "css-import-vs-link": {
        "explanation": (
            "There are two ways to load external CSS: the HTML **`<link rel=\"stylesheet\">`** and the CSS "
            "**@import** at-rule. **link** is preferred: the browser discovers it early in HTML parsing, "
            "downloads stylesheets **in parallel**, and applies them as soon as ready. **@import** must wait "
            "until the containing stylesheet is downloaded and parsed, creating a **serial waterfall** that "
            "blocks rendering longer. @import also fails silently in older IE and cannot load CSS conditionally "
            "from HTML (media attribute on link handles that). Use @import only inside CSS for splitting "
            "large internal stylesheets — never in production critical path from HTML."
        ),
        "code": """<!-- ✅ Preferred — parallel, non-blocking discovery -->
<head>
  <link rel="stylesheet" href="/css/reset.css">
  <link rel="stylesheet" href="/css/main.css">
  <link rel="stylesheet" href="/css/print.css" media="print">
  <!-- Preload critical CSS -->
  <link rel="preload" href="/css/critical.css" as="style"
        onload="this.onload=null;this.rel='stylesheet'">
</head>

/* ❌ Avoid in HTML-loaded CSS — serial waterfall */
/* main.css */
@import url('reset.css');
@import url('components.css');
@import url('utilities.css');

/* ✅ Acceptable — internal split within one bundled file */
@layer reset, base, components;""",
        "language": "css",
        "key_points": [
            "link loads in parallel from HTML",
            "@import creates serial download waterfall",
            "link supports media attribute for conditional CSS",
            "Preload + onload for non-critical stylesheets",
            "Never chain @import in production critical path",
        ],
    },
    "css-filter-backdrop-filter": {
        "explanation": (
            "The CSS **filter** property applies graphical effects to an entire element — blur, brightness, "
            "contrast, grayscale, drop-shadow, and more. Filters affect the element and all its children as "
            "a flattened group. **backdrop-filter** applies the same effects to the **area behind** the "
            "element — the classic frosted-glass modal overlay. Both create a stacking context and can "
            "impact performance on large areas. **drop-shadow** follows the alpha shape of content (unlike "
            "box-shadow). Check browser support for backdrop-filter and provide a solid-color fallback "
            "for older browsers."
        ),
        "code": """/* Image hover desaturate */
.photo {
  filter: grayscale(0);
  transition: filter 0.3s;
}
.photo:hover { filter: grayscale(100%); }

/* Drop shadow on PNG icon (follows alpha) */
.icon { filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3)); }

/* Frosted glass modal backdrop */
.modal-backdrop {
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(12px) saturate(150%);
  -webkit-backdrop-filter: blur(12px) saturate(150%);
}

/* Fallback when backdrop-filter unsupported */
@supports not (backdrop-filter: blur(1px)) {
  .modal-backdrop { background: rgba(255, 255, 255, 0.92); }
}""",
        "language": "css",
        "key_points": [
            "filter affects element and children",
            "backdrop-filter blurs content behind element",
            "drop-shadow follows alpha unlike box-shadow",
            "Both create stacking contexts",
            "Provide fallback for unsupported browsers",
        ],
    },
    "css-supports-at-rule": {
        "explanation": (
            "The CSS **@supports** at-rule (feature queries) applies a block of CSS only when the browser "
            "supports a given property-value pair. Syntax: `@supports (display: grid) { ... }`. Combine "
            "conditions with **and**, **or**, and **not**. This enables **progressive enhancement** — "
            "deliver baseline styles everywhere, enhanced styles where supported. Unlike media queries "
            "(which test viewport/device), @supports tests **CSS capability**. Common uses: container queries, "
            "backdrop-filter, subgrid, :has(), and anchor positioning fallbacks."
        ),
        "code": """/* Baseline layout */
.layout { display: block; }

/* Enhanced when grid is supported */
@supports (display: grid) {
  .layout {
    display: grid;
    grid-template-columns: 240px 1fr;
    gap: 1.5rem;
  }
}

/* backdrop-filter with fallback */
.card-overlay { background: rgba(0,0,0,0.6); }
@supports (backdrop-filter: blur(8px)) {
  .card-overlay {
    background: rgba(0,0,0,0.3);
    backdrop-filter: blur(8px);
  }
}

/* :has() progressive enhancement */
@supports selector(:has(*)) {
  .form-group:has(input:invalid) {
    border-color: #dc3545;
  }
}""",
        "language": "css",
        "key_points": [
            "Feature queries test CSS support, not viewport",
            "Syntax: @supports (property: value)",
            "Combine with and / or / not",
            "Enables progressive enhancement",
            "Use for modern features with solid fallbacks",
        ],
    },
    "html-open-graph": {
        "explanation": (
            "**Open Graph** meta tags control how URLs appear when shared on social platforms (LinkedIn, "
            "Facebook, Slack, iMessage). They live in `<head>` with the **`property`** attribute (not `name`). "
            "Core tags: **og:title**, **og:description**, **og:image**, **og:url**, and **og:type**. "
            "Image should be at least 1200×630px for best previews. **Twitter Cards** use similar "
            "`twitter:card`, `twitter:title` tags. Without OG tags, platforms scrape random page content "
            "for previews. For SPAs (Angular), set OG tags server-side or via prerendering — client-only "
            "JS meta updates are often missed by crawlers."
        ),
        "code": """<head>
  <title>Q2 Revenue Report | Acme Corp</title>
  <meta name="description" content="Revenue up 12% to $4.2M in Q2.">

  <!-- Open Graph -->
  <meta property="og:type"        content="website">
  <meta property="og:url"         content="https://app.acme.com/reports/q2">
  <meta property="og:title"       content="Q2 Revenue Report | Acme Corp">
  <meta property="og:description" content="Revenue up 12% to $4.2M in Q2.">
  <meta property="og:image"       content="https://app.acme.com/og/q2-chart.png">
  <meta property="og:image:width"  content="1200">
  <meta property="og:image:height" content="630">

  <!-- Twitter Card -->
  <meta name="twitter:card"        content="summary_large_image">
  <meta name="twitter:title"       content="Q2 Revenue Report">
  <meta name="twitter:description" content="Revenue up 12% to $4.2M in Q2.">
  <meta name="twitter:image"       content="https://app.acme.com/og/q2-chart.png">
</head>""",
        "language": "html",
        "key_points": [
            "Use property= not name= for og: tags",
            "og:image minimum ~1200×630 for rich previews",
            "og:url should be canonical share URL",
            "Twitter Cards complement Open Graph",
            "SPAs need SSR/prerender for crawler-visible OG tags",
        ],
    },
    "css-logical-properties": {
        "explanation": (
            "**Logical properties** map physical directions (left, top, width, height) to **writing-mode-aware** "
            "concepts: **inline** (text flow direction) and **block** (perpendicular to text flow). "
            "`margin-inline-start` replaces `margin-left` in LTR and becomes `margin-right` in RTL automatically. "
            "`block-size` replaces `height` in horizontal writing modes. This simplifies **internationalization** "
            "— one stylesheet works for LTR, RTL, and vertical writing modes without duplicate rules. "
            "Modern shorthand: `margin-inline`, `padding-block`, `inset-inline-start`. Prefer logical "
            "properties in new codebases targeting global audiences."
        ),
        "code": """/* Physical — breaks in RTL */
.card-old {
  margin-left: 1rem;
  padding-right: 1.5rem;
  border-left: 3px solid #512BD4;
}

/* Logical — adapts to writing mode */
.card {
  margin-inline-start: 1rem;
  padding-inline-end: 1.5rem;
  border-inline-start: 3px solid #512BD4;
  block-size: 100%;
  inline-size: 100%;
}

/* Center with logical inset */
.dialog {
  position: fixed;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  transform: translate(-50%, -50%);
}

/* RTL document — logical props flip automatically */
html[dir="rtl"] .card { /* no override needed */ }""",
        "language": "css",
        "key_points": [
            "inline = text flow axis; block = perpendicular",
            "margin-inline-start replaces margin-left in LTR",
            "Automatic RTL support without duplicate rules",
            "block-size/inline-size replace height/width",
            "Prefer logical properties in i18n-ready apps",
        ],
    },
    "html-dialog-element": {
        "explanation": (
            "The native **`<dialog>`** element provides accessible modal semantics without a JavaScript library. "
            "Call **`dialog.showModal()`** to open as a modal (top layer, inert background, focus trap). "
            "**`dialog.show()`** opens non-modally. **`dialog.close(returnValue)`** dismisses it. The "
            "**`::backdrop`** pseudo-element styles the overlay behind the modal. Built-in **Escape key** "
            "closes the dialog. The **`closedby`** attribute (modern) controls dismiss behavior. "
            "For Angular/React, wrap dialog in a component but prefer the native element over div-based "
            "modals for accessibility and top-layer stacking without z-index wars."
        ),
        "code": """<button id="open-settings">Settings</button>

<dialog id="settings-dialog" aria-labelledby="settings-title">
  <header>
    <h2 id="settings-title">Settings</h2>
    <button type="button" id="close-dialog" aria-label="Close">✕</button>
  </header>
  <form method="dialog">
    <label>
      Theme
      <select name="theme">
        <option value="light">Light</option>
        <option value="dark">Dark</option>
      </select>
    </label>
    <menu>
      <button value="cancel">Cancel</button>
      <button value="save">Save</button>
    </menu>
  </form>
</dialog>

<style>
  dialog::backdrop { background: rgba(0,0,0,0.5); }
  dialog { border: none; border-radius: 8px; padding: 1.5rem; }
</style>

<script>
  const dlg = document.getElementById('settings-dialog');
  document.getElementById('open-settings').onclick = () => dlg.showModal();
  document.getElementById('close-dialog').onclick = () => dlg.close();
  dlg.addEventListener('close', () => console.log('Result:', dlg.returnValue));
</script>""",
        "language": "html",
        "key_points": [
            "showModal() for modal with backdrop and focus trap",
            "show() for non-modal dialog",
            "::backdrop styles the overlay",
            "Escape closes modal by default",
            "Prefer over div+role=dialog for accessibility",
        ],
    },
    "css-has-selector": {
        "explanation": (
            "The **:has()** pseudo-class is a **parent selector** — it matches an element if it contains "
            "a descendant (or subsequent sibling with `:has(+ ...)`) satisfying the inner selector. "
            "Example: `.card:has(img)` styles cards that contain an image. `.form-group:has(input:invalid)` "
            "highlights groups with invalid inputs — previously impossible in pure CSS. "
            "`:has()` enables conditional styling without JavaScript class toggling. It is supported in "
            "all modern browsers (2024+). Performance note: complex :has() on large DOM trees can be costly — "
            "keep selectors specific. Combine with @supports selector(:has(*)) for fallbacks."
        ),
        "code": """/* Style cards that contain an image */
.card:has(img) {
  display: grid;
  grid-template-columns: 120px 1fr;
}

/* Highlight form group with invalid input */
.form-group:has(input:invalid) {
  border-color: #dc3545;
}
.form-group:has(input:invalid) label {
  color: #dc3545;
}

/* Style heading that is followed by a paragraph */
h2:has(+ p) {
  margin-bottom: 0.5rem;
}

/* Empty state — hide list when no items */
.order-list:not(:has(.order-item)) .empty-state {
  display: block;
}

/* Progressive enhancement fallback */
@supports not selector(:has(*)) {
  .form-group.is-invalid { border-color: #dc3545; }
}""",
        "language": "css",
        "key_points": [
            "Parent/ancestor selector — 'if contains' logic",
            "Replaces many JS class-toggle patterns",
            "Supported in all modern browsers",
            "Keep selectors specific for performance",
            "Use @supports selector(:has(*)) for fallback",
        ],
    },
}
