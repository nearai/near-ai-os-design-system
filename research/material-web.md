# Material Web (MWC), the M3 / M3 Expressive token system, and Material Color Utilities: findings for the NEAR AI parent design system

Research stream: `material-components/material-web` and the M3 token system it implements (plus `material-foundation/material-color-utilities` and the AndroidX Compose Material 3 token files used as an Expressive cross-check).
Prepared 2026-10-13. All sources were fetched read-only (shallow `git clone`, `curl`, GitHub REST API). Nothing from the downloaded material was built or executed. Token values below come from parsing the generated SCSS/Kotlin source as text with my own scripts.

**Sources analysed (pinned)**

| Source | Revision | Notes |
|---|---|---|
| github.com/material-components/material-web | `main` @ `e3471c0` (2026-10-12, "fix(labs): align snackbar container inline-end padding with GM3 spec") | npm `@material/web` latest = **2.5.0** (released 2026-07-14/15). 1,568 files. |
| material-web `tokens/versions/v0_192` | Design system "Google Material 3", **v0.192**, context Audience 3P / Platform Web / Scheme Dynamic | The token set the shipping `<md-*>` elements compile against. |
| material-web `tokens/versions/latest/sass` | Design system "Google Material 3", **Version 34.0.21**, context audience 3p / font static / platform web | Added in PR #5880 "fix(tokens): add expressive token versions" (merged 2026-01-08). This is the M3 Expressive token set. 194 modules. |
| material-web `labs/gb/**` | same commit | New CSS-first Expressive component suite (internal codename "gBreeze", tags `md-gb-*`). |
| GitHub API: repo, releases, commits, issues; discussions #5642 and #5805 (HTML) | fetched 2026-10-13 | Project status. |
| github.com/material-foundation/material-color-utilities | `main` @ `5b3618b` (2026-08-21); npm `@material/material-color-utilities` **0.4.0** | HCT, schemes, spec versions 2021/2025/2026. |
| androidx/androidx `compose/material3/material3/src/commonMain/kotlin/androidx/compose/material3/tokens/` | `androidx-main`, fetched 2026-10-13 (120 `.kt` files) | Expressive tokens as shipped in Compose (mixed token versions per file, v0_103 to 37.2.1). |

**Corpus** (text copies for other streams): `$SCRATCH/corpus/material-web/`

- `docs/**` (all 26 MWC `.md` docs), `README.md`, `CHANGELOG.md`, `labs-README.md`
- `tokens/token-tables.md` (10,005 lines): every token module resolved to concrete values, for both `latest` (34.0.21) and `v0_192`
- `tokens/mwc-component-custom-properties.md`: every `--md-<component>-*` custom property the shipping elements expose, with the resolved default and the system token it points to
- `tokens/latest.json`, `tokens/v0_192.json` (machine-readable resolved tokens), `tokens/scss-latest/`, `tokens/scss-v0_192/`, `tokens/scss-mwc-wrappers/` (raw source)
- `labs-gb-styles/` (gBreeze system stylesheets and every component `_*-tokens.scss`)
- `mwc-component-api-summary.md` (properties, methods and events for every `<md-*>` element)
- `androidx-compose-m3-tokens/*.kt` (all 120 Compose token files)
- `mcu/**` (MCU README, concepts and dev guides)
- `discussion-5642-maintenance-mode.txt` (text of the maintenance-mode announcement thread)

---

## 0. Executive summary

1. **MWC is officially still in maintenance mode, but the codebase is not dormant.** The README links the June 2024 announcement ("MWC is in maintenance mode pending new maintainers"), and `docs/roadmap.md` (freshness-reviewed 2026-07-31) still says "There is no current work planned for new features or components." Even so, Google engineers have pushed steadily to `main` through 2026. Release 2.5.0 (2026-07-14) shipped the full M3 Expressive token set (`tokens/versions/latest`, GM3 v34.0.21). Since then, labs work has added a CSS-first Expressive component suite (`labs/gb`, elements `md-gb-*`) covering button, icon button, FAB, split button, button group, toolbar, nav bar, app bar, tabs, slider, snackbar, menu, list, chip, card, switch, checkbox, radio, badge, divider and icon. On 2026-05-18 the maintainer described this as experimental ("We're experimenting with some new lab ideas that may or may not go anywhere"). The stable `<md-*>` elements remain on the 2023-era **v0.192** tokens and receive only bug and security fixes. As of 2025-05-19 the maintainer's position on Expressive was: "new Expressive features are not planned for MWC."
2. **What this means for us.** Do not build NEAR AI web on top of the stable `<md-*>` elements: they are pre-Expressive, shadow-DOM-encapsulated and have no motion or density tokens. Do adopt MWC's *architecture* and the *latest token data*: the three-tier ref → sys → comp model with CSS custom properties, and the 34.0.21 values. Watch `labs/gb` closely. Its design (class-contract "baseline DOM", `@layer md.*` cascade layers, `light-dark()` colours, `@property`-registered ripple, spring curves converted to CSS `linear()`, focusgroup and `:state()`) is almost exactly the approach a glass-styled hybrid system needs.
3. **The token system is mature and fully extracted here.** That covers 6 key tonal palettes plus 11 new hue palettes, 49 colour roles in light, dark, medium-contrast and high-contrast variants, 15 type styles plus 15 "emphasized" styles with variable-font axes, a 9-step corner scale (new: 20/32/48 px), 6 elevation levels, 5 state opacities (focus and pressed are now 0.10, down from 0.12), focus-indicator tokens (3 px thick, 2 px outer or −3 px inner offset), 16 durations, 10 easings, and 6 spring tokens. Compose additionally defines a second, bouncier **Expressive motion scheme**.
4. **Dynamic colour.** MCU 0.4.0 offers 10 variants (Monochrome, Neutral, TonalSpot, Vibrant, Expressive, Fidelity, Content, Rainbow, FruitSalad, and the new two-source CMF), a continuous `contrastLevel` from −1 to 1 (0 = standard, 0.5 = medium, 1 = high) and three spec versions. The **2025** spec retunes TonalSpot, Neutral, Vibrant and Expressive per platform (phone or watch). The **2026** spec applies only to CMF.

---

## 1. Project status and implications

### 1.1 Evidence

| Signal | Value |
|---|---|
| README banner | "**Note: MWC is in maintenance mode pending new maintainers** (discussion #5642)". README also says Angular users should use Angular Material instead. |
| Announcement (#5642, 2024-06-10, maintainer asyncliz) | "Material Design is focusing on support for Google's large-scale internal Wiz framework, and has reassigned the engineers working on Material Web Components … MWC is not deprecated or going away … New features and components are no longer planned. GitHub PRs will not be accepted by default." |
| Follow-ups in #5642 | 2025-05-19: "new Expressive features are not planned for MWC." 2025-05-20: generating new tokens is possible, but "updating MWC to use the new tokens is much more difficult … would require effort to update and migrate internal projects." 2025-07-07: "committed to continued maintenance." **2026-05-18 (LTS question):** "you can use MWC's current components as they are today … We will continue to provide critical bug fixes and security patches … If however, you need additional components or new features beyond what MWC provides, then it may not be a good fit." Same day, on the recent activity: "We're experimenting with some new lab ideas that may or may not go anywhere. If the result would mean a change for this project, then I will post a much more satisfying and detailed update." |
| #5805 (token update Q&A, 2025) | The maintainer raised the open question of whether `@material/web/tokens` is valuable *independently of the components*. That is the use case we have. |
| `docs/roadmap.md` (reviewed 2026-07-31) | "MWC is currently in maintenance mode … no current work planned for new features or components." The list of never-built components is still present: autocomplete, badge, banner, bottom app bar, bottom sheet, card, data table, date picker, navigation bar, drawer and rail, search, segmented button, snackbar, time picker, top app bar, tooltip. Never-delivered goals: "Expand tokens (shape and motion) for expressive", "Density and spacing tokens", "TSX components", "layouts". |
| Releases | v1.0.0 2023-09-26 → v2.0.0 2024-07-25 → 2.1/2.2 (2024) → 2.3.0 2025-03-27 → 2.4.0 2025-08-21 → 2.4.1 2025-10-27 → **2.5.0 2026-07-15** (latest on npm). |
| 2.5.0 contents | `custom-elements.json` manifest; **expressive token versions** (`tokens/versions/latest`); labs: expressive button, FAB, icon, list, menu, **split button**, card, checkbox, radio, switch, badge, divider and icon-button utility-class components; **"expressive system stylesheets"**; **"Material for Tailwind theme stylesheet"**; **spacing system stylesheet**; `sass/ext` helpers; and fixes (button touch target, select typeahead, slider, switch on Firefox 150). |
| Unreleased on `main` since 2.5.0 | labs: appbar and chip utilities (Jul), ARIA tab elements (Jul), ARIA menu elements (Aug), toolbar suite (Sep 21), tabs (Sep 24), **button group, navigation bar suite, slider** (Sep 29), ARIA menubar (Sep 29), **snackbar** (Oct 7). Hardening: all `href`s sanitised with `safevalues` (Sep 11), `rel`/`referrerpolicy` on link components (Sep 10), TypeScript 6 suppressions. |
| Repo metrics (API, 2026-10-13) | 11.3 k stars, 188 open issues, not archived, `pushed_at` 2026-10-13. |
| Community stance | Open issue #5888 (2026-02-13) asks for M3 Expressive support and has no maintainer reply. In #5642 the community points to third-party Expressive web libraries (M3E, MICL, "seele", AWC UI, Material Web Additions). None are Google-endorsed. |

### 1.2 Interpretation

- **Two tracks coexist.**
  - Track A, the stable `@material/web/<component>` `md-*` elements: frozen API, v0.192 tokens, M3 2023 baseline, bug and security fixes only.
  - Track B, `@material/web/labs/gb`: new, explicitly "not recommended for production", may break in minor versions (labs README). It implements Expressive (GM3 34–35; one source comment reads "Design override of GM3 v35"). Track B is being built by Google engineers (commits authored by `copybara-service[bot]` from internal piper changes such as `PiperOrigin-RevId`), probably mirrored from Google's internal web stack (Wiz). Nothing promises that it will graduate to stable.
- **Token data is the most durable asset.** `tokens/versions/latest` is generated from Google's internal "Carbon" token compiler (header: "go/carbon-service-code-gen-mwtc", source template `contextualtokenset.scss.tmpl`). It is the most complete public machine-readable dump of M3 Expressive web tokens available. It includes every component (app bars, flexible app bars, banners, button groups, split buttons, FAB menu, loading indicator, toolbars, nav bar and rail items, list expand/reorder/reveal, menus standard/vibrant, sliders XS–XL, drag handle, carousel, search, sheets, date and time pickers, tooltips…), not only those MWC implements. Caveat from `tokens/versions/README.md`: "**may introduce breaking changes at any point across minor and patch updates** … save the *exact version*." Pin exactly (`--save-exact`), or better, vendor the values into our own token source.
- **Risk assessment.** Track A is safe to use for internal tools and admin UIs that accept stock Material styling. It is a dead end for a branded, glass-styled, Expressive product UI. Track B is a high-value *reference implementation* but too unstable to take as a dependency. Fork-and-own, or reimplement, is the prudent path.

---

## 2. Architecture

### 2.1 Packaging and runtime (Track A)

- **Lit 2/3 web components** (`lit ^2.8 || ^3`, `tslib`, `@lit/context`), ES modules with bare specifiers, one import per element (`@material/web/button/filled-button.js`), plus `all.js` and `common.js` bundles. Bundle sizes (docs/size.md, 2025-08-20): `all.js` **72.1 kB gzip / 455.5 kB min (64 % CSS)**; button ≈ 7 kB gzip each; text field 11.5 kB; select 18.8 kB; menu 8.2 kB. CSS dominates because every element ships its own token-to-CSS mapping inside shadow DOM.
- **Browser support** (docs/support.md): Chrome and Edge 120+, Firefox 119+, Safari 16.4+ (older Safari only with an ElementInternals polyfill). MWC targets "latest two majors".
- **Custom-element manifest:** `custom-elements.json` is included from 2.5.0 for IDE and framework tooling. It is generated at build time and was not present in the source tree.
- **File layout per component:** `<component>/<variant>.ts` registers the element (`md-filled-button`). `<component>/internal/*.ts` holds the base class. `internal/_<variant>.scss` maps `tokens.md-comp-<x>-values()` onto private `--_token` properties on `:host`. `internal/_shared.scss` holds the layout. `*-styles.scss` is compiled to CSS-in-JS (`*-styles.js`).
- **Shared infrastructure** (`internal/`, "limited support"): `aria/aria.ts` and `aria/delegate.ts` (`mixinDelegatesAria`: ARIA attributes set on the host are forwarded to the inner native element); `controller/attachable-controller.ts` (focus ring and ripple attach to a control via `for`/`htmlFor` or `attach()`); `events/form-label-activation.ts`, `redispatch-event.ts`, `dispatch-hooks.ts`; `motion/animation.ts` (EASING constants); `directives/safe-href.ts`. `labs/behaviors/` adds mixins: `element-internals`, `form-associated`, `constraint-validation`, `custom-state-set` (`:state()` compatibility), `focusable`, `form-submitter`, `on-report-validity` and validators.

### 2.2 The three token tiers

```
md.ref.*      reference: concrete values (hex tones, typeface names, weights)
   ↓ (map.get / Sass var)
md.sys.*      system: semantic roles (color roles, typescale, shape, elevation, state, motion)
   ↓
md.comp.*     component: per-part, per-state design decisions (container-color, hover-state-layer-opacity…)
```

In Sass the tiers are generated modules. `versions/v0_192/_md-comp-filled-button.scss` exports `values($deps)`, which returns a map such as `'container-color': map.get($deps, 'md-sys-color', 'primary')`. In `versions/latest/sass` the tiers are plain Sass variables with doc comments, for example `$container-shape-round: md-sys-shape.$corner-full;`. Typography uses mixins (`@mixin label-text { @include md-sys-typescale.label-large; }`).

**Web runtime mapping (Track A).** The hand-written wrappers in `tokens/_md-*.scss` do four things:

1. **Whitelist** tokens (`$supported-tokens`, `$unsupported-tokens`). For example, buttons drop `label-text-tracking` and the `font` shorthand `label-text-type`, so MWC never applies letter-spacing from tokens.
2. **Add web-only tokens** that the design system lacks, as `$new-tokens` with hard-coded values. Examples: button `leading-space` 24 px, `with-leading-icon-leading-space` 16 px, list-item `top-space`/`bottom-space` 12 px, icon `font: 'Material Symbols Outlined'`, `size: 24px`; logical-corner tokens `container-shape-start-start|start-end|end-start|end-end`, each falling back to the shorthand `--md-<comp>-container-shape`.
3. **Rename** tokens (`with-icon-icon-color` → `icon-color`; list `list-item-*` → `*`).
4. **Wrap every value** in a custom property with a fallback chain:

```css
/* emitted inside md-filled-button's shadow root */
:host {
  --_container-color: var(--md-filled-button-container-color, var(--md-sys-color-primary, #6750a4));
  --_container-shape-start-start: var(--md-filled-button-container-shape-start-start,
                                   var(--md-filled-button-container-shape, var(--md-sys-shape-corner-full, 9999px)));
  --_hover-state-layer-opacity: var(--md-filled-button-hover-state-layer-opacity,
                                 var(--md-sys-state-hover-state-layer-opacity, 0.08));
}
```

The three override levels:

| Level | Custom property | Scope |
|---|---|---|
| Reference | `--md-ref-typeface-brand`, `--md-ref-typeface-plain` | Supported. `--md-ref-palette-*` is **not** supported. |
| System | `--md-sys-color-*` (49 roles), `--md-sys-typescale-<role>-<size>-{font,size,line-height,weight}` (+ `-weight-prominent` for labels), `--md-sys-shape-corner-{none,extra-small,small,medium,large,extra-large,full}` | **No** `--md-sys-motion-*`, no `--md-sys-elevation-*`, and no `--md-sys-state-*` custom properties: those values are compiled in. |
| Component | `--md-<component>-<token>` | No `comp` infix. For example, `--md-filled-button-container-shape: 0px`. |

Sub-elements are reachable with `::part()`; the part name is the inner tag minus `md-`, for example `md-checkbox::part(focus-ring)`.

**Elevation on web** is a *level number*, not dp. `tokens/_md-sys-elevation.scss` overrides levels 0–5 to `0..5` (b/261602454). `<md-elevation>` turns `--md-elevation-level` into two pseudo-element shadows with `clamp()` arithmetic, giving the exact M3 key and ambient shadows listed in §3.6.

### 2.3 Track B architecture (`labs/gb`, "gBreeze")

- **CSS first, JS optional.** Every component is a *class contract* on native elements, documented as "Baseline DOM". For example `<button class="btn btn-filled btn-md">`, `<div class="tabs" role="tablist" focusgroup="tablist inline">`, `<button class="tab focus-ring-inner ripple selected" role="tab" aria-selected="true">`. The optional custom elements (`md-gb-button` and others) render the same classes and expose them through a single `::part()` (`btn`, `icon-btn`, `fab`, `chip`, `card`, `menu`, `list-item`…).
- **Cascade layers:** `@layer md.sys.{color,typescale,shape,motion,elevation,space,icon}` and `@layer md.comp.<component>`. The Tailwind theme declares `@layer theme, base, md, components, utilities;` so app utilities always win.
- **System stylesheet** `labs/gb/styles/m3.scss` imports color, elevation, icon, motion easing, shape, space and typography tokens, all emitted on `:root`.
  - Colour uses **`light-dark()`** with `color-scheme: light dark`, so dark mode follows the user agent automatically. A full variant also emits `--md-ref-palette-*`.
  - Typography is emitted as **font shorthands**: `--md-sys-typescale-body-md` is `400 0.875rem/1.25rem <family>`, with separate `-tracking` and `-axes` (`font-variation-settings`, for example `"ROND" 100` for emphasized styles). Short size names: `sm`/`md`/`lg`.
  - Shape uses short names (`--md-sys-shape-corner-xs|sm|md|lg|lg-increased|xl|xl-increased|xxl|full`), and `full` = **`50cqmin`**, a container-query unit, so pills stay pills at any size.
  - Elevation is real box-shadows built with relative colour syntax (`hsl(from var(--md-sys-color-shadow) h s l / 0.3)`).
  - Space: `--md-sys-space-unit: 8px` with steps 0, 25, 50, 75, 100, 125, 150, 175, 200, 250, 300, 400, 450, 500, 600, 700, 800, 900 (multipliers ×0.25 … ×9).
  - Icon: `@property`-registered `--md-icon-{font,color,size,opsz,wght,fill,grad}` driving Material Symbols variable axes.
- **Component-local tokens** are *unprefixed* custom properties on the class (`--container-color`, `--container-height`, `--label-text`, `--icon-size`, `--outline-width`, `--state-layer-color`…) and are documented with `@cssprop` JSDoc. Selected and pressed state is expressed with selectors (`:where(.btn-selected, [aria-pressed='true'])`, `:is(:active, .active)`), plus `:state(selected)` for custom elements.
- **Interaction primitives in pure CSS:**
  - Ripple and state layer use a `background-image` of two radial gradients driven by `@property` percentages (`--ripple-hover-opacity` 8 %, `--ripple-press-opacity` 10 %, `--ripple-scale` animated 20 %→100 % over 450 ms `cubic-bezier(0.2,0,0,1)`, release 375 ms).
  - The focus ring is an animated `outline` (3 px solid `--md-sys-color-secondary`, grows to 8 px over 150 ms then shrinks back over 450 ms).
- **Springs on the web:** the button group defines `--motion-spring-fast-spatial: linear(0, 0.099, 0.317, 0.561, 0.775, 0.934, 1.034, 1.083, 1.095, 1.084, 1.063, 1.04, 1.02, 1.005, 0.996, 0.992, 0.991, 0.992, 0.994, 0.996, 1)` with a duration of **350 ms**. I simulated it: it is exactly the **Compose *Expressive* fast-spatial spring (stiffness 800, damping 0.6)** sampled at 21 points (max error 0.002, peak 1.095 at about 140 ms). It is *not* the 1400/0.9 "standard" value in the web sys tokens. Google's own web Expressive work therefore uses the expressive spring scheme. Button and icon-button shape morphs use `border-radius 350ms cubic-bezier(0.42, 1.67, 0.21, 0.9)`, an overshooting bezier approximation of the same spring.
- **Tailwind 4 theme** (`labs/gb/styles/tailwind.scss`):
  - Maps `--color-*` to M3 roles and turns off the Tailwind defaults (`--color-*: initial`).
  - Maps `--radius-xs…4xl` to the M3 shape scale (xl = lg-increased 20, 2xl = xl 28, 3xl = xl-increased 32, 4xl = xxl 48) and `--shadow-xs…xl` to elevation 1–5.
  - Sets `--spacing` to 4 px (half the M3 unit) and adds `s0…s900` spacing names.
  - Sets **breakpoints sm 600 (medium), md 840 (expanded), lg 1200 (large), xl 1600 (extra-large)**.
  - Adds a `typescale-*` utility that sets font, letter-spacing and font-variation-settings together.
- **Headless ARIA primitives** (`labs/aria`): `md-aria-toggle`, `md-aria-tablist`/`tab`/`tabpanel`, `md-aria-menulist`/`menuitem`/`fieldset`/`menubar`. These implement *proposed* built-ins (`<menulist>`, `<menuitem>`) and use the **`focusgroup`** attribute (an OpenUI proposal) for arrow-key roving focus.


---

## 3. Token tables

Unless marked otherwise, values are from `tokens/versions/latest` (**GM3 34.0.21**, the Expressive generation), resolved through every alias. The `v0_192` column shows what shipping MWC elements use. Exhaustive per-module tables for every component are in `corpus/material-web/tokens/token-tables.md`.

### 3.1 md.ref.palette: baseline key palettes (source colour #6750A4)

All shared keys are byte-identical between v0_192 and latest. Latest adds tone **98** to every key palette. v0_192 also carries tone 99 and `black`/`white`. The neutral palette has the extra "surface" tones 4, 6, 12, 17, 22, 24, 87, 92, 94 and 96 that the surface-container roles need.

| tone | primary | secondary | tertiary | error | neutral | neutral-variant |
|---|---|---|---|---|---|---|
| 0 | #000 | #000 | #000 | #000 | #000 | #000 |
| 4 |  |  |  |  | #0f0d13 |  |
| 6 |  |  |  |  | #141218 |  |
| 10 | #21005d | #1d192b | #31111d | #410e0b | #1d1b20 | #1d1a22 |
| 12 |  |  |  |  | #211f26 |  |
| 17 |  |  |  |  | #2b2930 |  |
| 20 | #381e72 | #332d41 | #492532 | #601410 | #322f35 | #322f37 |
| 22 |  |  |  |  | #36343b |  |
| 24 |  |  |  |  | #3b383e |  |
| 30 | #4f378b | #4a4458 | #633b48 | #8c1d18 | #48464c | #49454f |
| 40 | #6750a4 | #625b71 | #7d5260 | #b3261e | #605d64 | #605d66 |
| 50 | #7f67be | #7a7289 | #986977 | #dc362e | #79767d | #79747e |
| 60 | #9a82db | #958da5 | #b58392 | #e46962 | #938f96 | #938f99 |
| 70 | #b69df8 | #b0a7c0 | #d29dac | #ec928e | #aea9b1 | #aea9b4 |
| 80 | #d0bcff | #ccc2dc | #efb8c8 | #f2b8b5 | #cac5cd | #cac4d0 |
| 87 |  |  |  |  | #ded8e1 |  |
| 90 | #eaddff | #e8def8 | #ffd8e4 | #f9dedc | #e6e0e9 | #e7e0ec |
| 92 |  |  |  |  | #ece6f0 |  |
| 94 |  |  |  |  | #f3edf7 |  |
| 95 | #f6edff | #f6edff | #ffecf1 | #fceeee | #f5eff7 | #f5eefa |
| 96 |  |  |  |  | #f7f2fa |  |
| 98 | #fef7ff | #fef7ff | #fff8f8 | #fff8f7 | #fef7ff | #fdf7ff |
| 99 | #fffbfe | #fffbfe | #fffbfa | #fffbf9 | #fffbff | #fffbfe |
| 100 | #fff | #fff | #fff | #fff | #fff | #fff |

v0_192 also contains tone 99 for primary/secondary/tertiary/error/neutral/neutral-variant (#fffbfe/#fffbfe/#fffbfa/#fffbf9/#fffbff/#fffbfe) and `black`/`white`; latest adds tone 98 for each key palette.

**New in 34.x: hue-named reference palettes.** These are fixed, non-dynamic palettes (Google's product hues). They do not exist in v0_192 and no sys role uses them. They are useful as a curated categorical and data-visualisation palette that is tone-matched to M3:

| tone | blue | blue-variant | cyan | green | grey | grey-variant | orange | pink | purple | red | yellow |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | #000 | #000 | #000 | #000 | #000 | #000 | #000 | #000 | #000 | #000 | #000 |
| 10 | #001944 | #001f2d | #001f26 | #002110 | #1b1b1c | #191d1c | #321200 | #3d0023 | #280255 | #3a0907 | #2f1400 |
| 20 | #012c6f | #003549 | #003641 | #00381f | #303030 | #2d312f | #522302 | #620438 | #400b84 | #60150f | #4d2600 |
| 30 | #04409f | #004d68 | #004e5d | #00522c | #474747 | #444746 | #753403 | #8d0053 | #5629a4 | #8a1a16 | #6d3a01 |
| 40 | #1157ce | #006788 | #00687c | #006c35 | #5e5e5e | #5c5f5e | #9a4600 | #b60d6e | #7438d2 | #b3251e | #8f4e06 |
| 50 | #3271ea | #0081a8 | #00839b | #128937 | #777 | #747775 | #c05a01 | #dc258d | #9254ea | #db372d | #b16300 |
| 60 | #4e8ff8 | #009dc9 | #009ebb | #1aa64a | #919191 | #8e918f | #e86e00 | #f94aab | #ad72ff | #f55e57 | #d37b00 |
| 70 | #76acff | #00bbea | #00bbdf | #44c265 | #ababab | #a9acaa | #ff8d41 | #ff7dd2 | #c597ff | #ff8983 | #ef9800 |
| 80 | #a1c9ff | #67d4ff | #60d5f3 | #80da88 | #c7c7c7 | #c4c7c5 | #ffb683 | #ffaee4 | #d9bafd | #ffb3ae | #fcbd00 |
| 90 | #d0e4ff | #bde9ff | #acedff | #beefbb | #e3e3e3 | #e1e3e1 | #ffdcc3 | #ffd8ef | #eedcfe | #ffdadc | #ffe07c |
| 95 | #e7f2ff | #e0f4ff | #d8f6ff | #ddf8d8 | #f2f2f2 | #eff2ef | #ffede1 | #ffecf6 | #f7ecfe | #ffecee | #fff2b4 |
| 98 | #f5faff | #f4faff | #f0fbff | #f2fcef | #f9f9f9 | #f7faf7 | #fff8f4 | #fff7fc | #fdf8ff | #fff8f8 | #fffade |
| 100 | #fff | #fff | #fff | #fff | #fff | #fff | #fff | #fff | #fff | #fff | #fff |

### 3.2 md.sys.color: all roles, baseline scheme, six variants

Format: `hex (palette tone)`. "MC" means medium contrast and "HC" means high contrast. In latest these ship as separate token modules: `md-sys-color`, `__medium-contrast`, `__high-contrast`, `__dark`, `__dark__medium-contrast`, `__dark__high-contrast`.

| role | light | light MC | light HC | dark | dark MC | dark HC |
|---|---|---|---|---|---|---|
| background | #fef7ff (neutral98) | #fef7ff (neutral98) | #fef7ff (neutral98) | #141218 (neutral6) | #141218 (neutral6) | #141218 (neutral6) |
| error | #b3261e (error40) | #8c1d18 (error30) | #601410 (error20) | #f2b8b5 (error80) | #f9dedc (error90) | #fceeee (error95) |
| error-container | #f9dedc (error90) | #b3261e (error40) | #8c1d18 (error30) | #8c1d18 (error30) | #e46962 (error60) | #f2b8b5 (error80) |
| inverse-on-surface | #f5eff7 (neutral95) | #fff (neutral100) | #fff (neutral100) | #322f35 (neutral20) | #1d1b20 (neutral10) | #000 (neutral0) |
| inverse-primary | #d0bcff (primary80) | #d0bcff (primary80) | #d0bcff (primary80) | #6750a4 (primary40) | #4f378b (primary30) | #381e72 (primary20) |
| inverse-surface | #322f35 (neutral20) | #322f35 (neutral20) | #322f35 (neutral20) | #e6e0e9 (neutral90) | #e6e0e9 (neutral90) | #e6e0e9 (neutral90) |
| on-background | #1d1b20 (neutral10) | #000 (neutral0) | #000 (neutral0) | #e6e0e9 (neutral90) | #fff (neutral100) | #fff (neutral100) |
| on-error | #fff (error100) | #fff (error100) | #fff (error100) | #601410 (error20) | #410e0b (error10) | #000 (error0) |
| on-error-container | #8c1d18 (error30) | #fff (error100) | #fff (error100) | #f9dedc (error90) | #000 (error0) | #000 (error0) |
| on-primary | #fff (primary100) | #fff (primary100) | #fff (primary100) | #381e72 (primary20) | #21005d (primary10) | #000 (primary0) |
| on-primary-container | #4f378b (primary30) | #fff (primary100) | #fff (primary100) | #eaddff (primary90) | #000 (primary0) | #000 (primary0) |
| on-primary-fixed | #21005d (primary10) | #fff (primary100) | #fff (primary100) | #21005d (primary10) | #000 (primary0) | #000 (primary0) |
| on-primary-fixed-variant | #4f378b (primary30) | #fff (primary100) | #fff (primary100) | #4f378b (primary30) | #381e72 (primary20) | #000 (primary0) |
| on-secondary | #fff (secondary100) | #fff (secondary100) | #fff (secondary100) | #332d41 (secondary20) | #1d192b (secondary10) | #000 (secondary0) |
| on-secondary-container | #4a4458 (secondary30) | #fff (secondary100) | #fff (secondary100) | #e8def8 (secondary90) | #000 (secondary0) | #000 (secondary0) |
| on-secondary-fixed | #1d192b (secondary10) | #fff (secondary100) | #fff (secondary100) | #1d192b (secondary10) | #000 (secondary0) | #000 (secondary0) |
| on-secondary-fixed-variant | #4a4458 (secondary30) | #fff (secondary100) | #fff (secondary100) | #4a4458 (secondary30) | #332d41 (secondary20) | #000 (secondary0) |
| on-surface | #1d1b20 (neutral10) | #000 (neutral0) | #000 (neutral0) | #e6e0e9 (neutral90) | #fff (neutral100) | #fff (neutral100) |
| on-surface-variant | #49454f (neutral-variant30) | #322f37 (neutral-variant20) | #000 (neutral-variant0) | #cac4d0 (neutral-variant80) | #e7e0ec (neutral-variant90) | #fff (neutral-variant100) |
| on-tertiary | #fff (tertiary100) | #fff (tertiary100) | #fff (tertiary100) | #492532 (tertiary20) | #31111d (tertiary10) | #000 (tertiary0) |
| on-tertiary-container | #633b48 (tertiary30) | #fff (tertiary100) | #fff (tertiary100) | #ffd8e4 (tertiary90) | #000 (tertiary0) | #000 (tertiary0) |
| on-tertiary-fixed | #31111d (tertiary10) | #fff (tertiary100) | #fff (tertiary100) | #31111d (tertiary10) | #000 (tertiary0) | #000 (tertiary0) |
| on-tertiary-fixed-variant | #633b48 (tertiary30) | #fff (tertiary100) | #fff (tertiary100) | #633b48 (tertiary30) | #492532 (tertiary20) | #000 (tertiary0) |
| outline | #79747e (neutral-variant50) | #49454f (neutral-variant30) | #322f37 (neutral-variant20) | #938f99 (neutral-variant60) | #aea9b4 (neutral-variant70) | #f5eefa (neutral-variant95) |
| outline-variant | #cac4d0 (neutral-variant80) | #79747e (neutral-variant50) | #49454f (neutral-variant30) | #49454f (neutral-variant30) | #938f99 (neutral-variant60) | #cac4d0 (neutral-variant80) |
| primary | #6750a4 (primary40) | #4f378b (primary30) | #381e72 (primary20) | #d0bcff (primary80) | #eaddff (primary90) | #f6edff (primary95) |
| primary-container | #eaddff (primary90) | #6750a4 (primary40) | #4f378b (primary30) | #4f378b (primary30) | #9a82db (primary60) | #d0bcff (primary80) |
| primary-fixed | #eaddff (primary90) | #6750a4 (primary40) | #4f378b (primary30) | #eaddff (primary90) | #eaddff (primary90) | #eaddff (primary90) |
| primary-fixed-dim | #d0bcff (primary80) | #4f378b (primary30) | #381e72 (primary20) | #d0bcff (primary80) | #d0bcff (primary80) | #d0bcff (primary80) |
| scrim | #000 (neutral0) | #000 (neutral0) | #000 (neutral0) | #000 (neutral0) | #000 (neutral0) | #000 (neutral0) |
| secondary | #625b71 (secondary40) | #4a4458 (secondary30) | #332d41 (secondary20) | #ccc2dc (secondary80) | #e8def8 (secondary90) | #f6edff (secondary95) |
| secondary-container | #e8def8 (secondary90) | #625b71 (secondary40) | #4a4458 (secondary30) | #4a4458 (secondary30) | #958da5 (secondary60) | #ccc2dc (secondary80) |
| secondary-fixed | #e8def8 (secondary90) | #625b71 (secondary40) | #4a4458 (secondary30) | #e8def8 (secondary90) | #e8def8 (secondary90) | #e8def8 (secondary90) |
| secondary-fixed-dim | #ccc2dc (secondary80) | #4a4458 (secondary30) | #332d41 (secondary20) | #ccc2dc (secondary80) | #ccc2dc (secondary80) | #ccc2dc (secondary80) |
| shadow | #000 (neutral0) | #000 (neutral0) | #000 (neutral0) | #000 (neutral0) | #000 (neutral0) | #000 (neutral0) |
| surface | #fef7ff (neutral98) | #fef7ff (neutral98) | #fef7ff (neutral98) | #141218 (neutral6) | #141218 (neutral6) | #141218 (neutral6) |
| surface-bright | #fef7ff (neutral98) | #fef7ff (neutral98) | #fef7ff (neutral98) | #3b383e (neutral24) | #3b383e (neutral24) | #3b383e (neutral24) |
| surface-container | #f3edf7 (neutral94) | #f3edf7 (neutral94) | #f3edf7 (neutral94) | #211f26 (neutral12) | #211f26 (neutral12) | #211f26 (neutral12) |
| surface-container-high | #ece6f0 (neutral92) | #ece6f0 (neutral92) | #ece6f0 (neutral92) | #2b2930 (neutral17) | #2b2930 (neutral17) | #2b2930 (neutral17) |
| surface-container-highest | #e6e0e9 (neutral90) | #e6e0e9 (neutral90) | #e6e0e9 (neutral90) | #36343b (neutral22) | #36343b (neutral22) | #36343b (neutral22) |
| surface-container-low | #f7f2fa (neutral96) | #f7f2fa (neutral96) | #f7f2fa (neutral96) | #1d1b20 (neutral10) | #1d1b20 (neutral10) | #1d1b20 (neutral10) |
| surface-container-lowest | #fff (neutral100) | #fff (neutral100) | #fff (neutral100) | #0f0d13 (neutral4) | #0f0d13 (neutral4) | #0f0d13 (neutral4) |
| surface-dim | #ded8e1 (neutral87) | #ded8e1 (neutral87) | #ded8e1 (neutral87) | #141218 (neutral6) | #141218 (neutral6) | #141218 (neutral6) |
| surface-variant | #e7e0ec (neutral-variant90) | #e7e0ec (neutral-variant90) | #e7e0ec (neutral-variant90) | #49454f (neutral-variant30) | #49454f (neutral-variant30) | #49454f (neutral-variant30) |
| tertiary | #7d5260 (tertiary40) | #633b48 (tertiary30) | #492532 (tertiary20) | #efb8c8 (tertiary80) | #ffd8e4 (tertiary90) | #ffecf1 (tertiary95) |
| tertiary-container | #ffd8e4 (tertiary90) | #7d5260 (tertiary40) | #633b48 (tertiary30) | #633b48 (tertiary30) | #b58392 (tertiary60) | #efb8c8 (tertiary80) |
| tertiary-fixed | #ffd8e4 (tertiary90) | #7d5260 (tertiary40) | #633b48 (tertiary30) | #ffd8e4 (tertiary90) | #ffd8e4 (tertiary90) | #ffd8e4 (tertiary90) |
| tertiary-fixed-dim | #efb8c8 (tertiary80) | #633b48 (tertiary30) | #492532 (tertiary20) | #efb8c8 (tertiary80) | #efb8c8 (tertiary80) | #efb8c8 (tertiary80) |
| surface-tint | #6750a4 (md-sys-color.primary) | #4f378b (md-sys-color__medium-contrast.primary) | #381e72 (md-sys-color__high-contrast.primary) | #d0bcff (md-sys-color__dark.primary) | #eaddff (md-sys-color__dark__medium-contrast.primary) | #f6edff (md-sys-color__dark__high-contrast.primary) |
| surface-tint-color | #6750a4 (md-sys-color.primary) | #4f378b (md-sys-color__medium-contrast.primary) | #381e72 (md-sys-color__high-contrast.primary) | #d0bcff (md-sys-color__dark.primary) | #eaddff (md-sys-color__dark__medium-contrast.primary) | #f6edff (md-sys-color__dark__high-contrast.primary) |

Role semantics, quoted from the token doc comments:

- `background`/`on-background` are **legacy** ("recommended to use Surface instead").
- `surface-variant` is described as an "alternate surface color, can be used for active states". Surface-container roles have replaced it for containers.
- `surface-tint` and `surface-tint-color` are **@deprecated** ("replaced by the tonal surface colors"). Tonal elevation overlays are gone.
- `outline-variant` is used for borders "where 3:1 contrast ratio isn't required, a container, or a divider".
- The `*-fixed` and `*-fixed-dim` roles do not change between light and dark.
- `inverse-*` roles are for snackbars and tooltips.

**Shipping MWC (v0_192) vs latest.** Only the on-container roles moved, from tone 10 to tone 30 in light mode. This is the 2025 "softer on-container" change. Dark mode is unchanged:

| role | v0_192 light | latest light | v0_192 dark | latest dark |
|---|---|---|---|---|
| on-error-container | #410e0b (error10) | #8c1d18 (error30) | #f9dedc (error90) | #f9dedc (error90) |
| on-primary-container | #21005d (primary10) | #4f378b (primary30) | #eaddff (primary90) | #eaddff (primary90) |
| on-secondary-container | #1d192b (secondary10) | #4a4458 (secondary30) | #e8def8 (secondary90) | #e8def8 (secondary90) |
| on-tertiary-container | #31111d (tertiary10) | #633b48 (tertiary30) | #ffd8e4 (tertiary90) | #ffd8e4 (tertiary90) |
| surface-tint-color |  () | #6750a4 (md-sys-color.primary) |  () | #d0bcff (md-sys-color__dark.primary) |

Note that Compose's `ColorLightTokens` (VERSION v0_210, fetched 2026-10-13) *still* maps `OnPrimaryContainer` to `Primary10`. Platforms disagree on this pair, so we must pick one explicitly. Recommendation: tone 30, the newer value. It still passes 4.5:1 on tone 90 (tone 30 on tone 90 ≈ 7.2:1).

### 3.3 md.sys.typescale: 15 baseline styles and 15 emphasized

Font for all styles: `md.ref.typeface.brand` (display, headline, title-large) or `.plain` (the rest). Both default to **Roboto**. The gBreeze stylesheet overrides `plain` with `'Roboto Flex', 'Roboto', 'Noto Sans', system-ui, sans-serif` and sets `brand = var(--md-ref-typeface-plain)`. Weights: regular 400, medium 500, bold 700. Sizes are in rem with px in brackets.

| style | font | size | line-height | weight | tracking | opsz axis | emphasized weight |
|---|---|---|---|---|---|---|---|
| display-large | Roboto | 3.5625rem (57px) | 4rem (64px) | 400 | -0.015625rem (-0.25px) | 'opsz' 57 | 500 |
| display-medium | Roboto | 2.8125rem (45px) | 3.25rem (52px) | 400 | 0rem (0px) | 'opsz' 45 | 500 |
| display-small | Roboto | 2.25rem (36px) | 2.75rem (44px) | 400 | 0rem (0px) | 'opsz' 36 | 500 |
| headline-large | Roboto | 2rem (32px) | 2.5rem (40px) | 400 | 0rem (0px) | 'opsz' 32 | 500 |
| headline-medium | Roboto | 1.75rem (28px) | 2.25rem (36px) | 400 | 0rem (0px) | 'opsz' 28 | 500 |
| headline-small | Roboto | 1.5rem (24px) | 2rem (32px) | 400 | 0rem (0px) | 'opsz' 24 | 500 |
| title-large | Roboto | 1.375rem (22px) | 1.75rem (28px) | 400 | 0rem (0px) | 'opsz' 22 | 500 |
| title-medium | Roboto | 1rem (16px) | 1.5rem (24px) | 500 | 0.009375rem (0.15px) | 'opsz' 16 | 700 |
| title-small | Roboto | 0.875rem (14px) | 1.25rem (20px) | 500 | 0.00625rem (0.1px) | 'opsz' 14 | 700 |
| body-large | Roboto | 1rem (16px) | 1.5rem (24px) | 400 | 0.03125rem (0.5px) | 'opsz' 16 | 500 |
| body-medium | Roboto | 0.875rem (14px) | 1.25rem (20px) | 400 | 0.015625rem (0.25px) | 'opsz' 14 | 500 |
| body-small | Roboto | 0.75rem (12px) | 1rem (16px) | 400 | 0.025rem (0.4px) | 'opsz' 12 | 500 |
| label-large | Roboto | 0.875rem (14px) | 1.25rem (20px) | 500 | 0.00625rem (0.1px) | 'opsz' 14 | 700 |
| label-medium | Roboto | 0.75rem (12px) | 1rem (16px) | 500 | 0.03125rem (0.5px) | 'opsz' 12 | 700 |
| label-small | Roboto | 0.6875rem (11px) | 1rem (16px) | 500 | 0.03125rem (0.5px) | 'opsz' 11 | 700 |

- **Emphasized** styles keep size, line height and tracking and change only weight: 400 → 500 for display, headline, title-large and body; 500 → 700 for title-m/s and label. In 34.0.21 the emphasized tokens still carry `'ROND' 0`. gBreeze nevertheless *forces* `'ROND' 100` (rounded terminals. ROND is an axis of Google Sans Flex, so it has no visible effect unless a font that supports ROND is loaded; the default Roboto/Roboto Flex stack ignores it) on every emphasized style; its source comment reads "Remove this function once emphasized tokens are fixed to use 'ROND' 100". So the design intent is rounded emphasized text, and the tokens have not caught up yet.
- **Variable-font axis tokens** exist for every style in latest (`opsz` = size in px, `wght`, `wdth` 100, `GRAD` 0, `ROND` 0, `slnt` 0, `CRSV`, `FILL`, `HEXP`), and `label-medium` additionally has `text-transform: none`. gBreeze emits only non-default ROND and GRAD as `font-variation-settings`. `opsz` comes through `font-size`, `wdth` through `font-stretch`, and `wght` through `font-weight`.
- **v0_192 typescale is identical** in size, line height, weight and tracking. MWC's shipping elements simply never apply tracking.
- **Compose `TypeScaleTokens` (v0_103) differ slightly in tracking:** display-large −0.2 sp (web −0.25 px), body-medium 0.2 sp (web 0.25), title-medium 0.2 sp (web 0.15). Compose emphasized styles also change tracking: body-large-emph 0.15 sp, body-medium-emph 0.25 sp, title-medium-emph 0.15 sp, display-large-emph 0. Use web values for web and Compose values for Android, and record the deltas.
- MWC classes: `md-typescale-styles.js` provides `.md-typescale-<scale>-<size>` and `.md-typescale-<scale>-<size>-prominent` (tokens exist for `label-large`/`label-medium-weight-prominent` = 700). They set the `font` shorthand only.

### 3.4 md.sys.shape: corner scale

| token | latest | v0_192 | note |
|---|---|---|---|
| md.sys.shape.corner-value.extra-extra-large | 48px | — |  |
| md.sys.shape.corner-value.extra-large | 28px | — |  |
| md.sys.shape.corner-value.extra-large-increased | 32px | — |  |
| md.sys.shape.corner-value.extra-small | 4px | — |  |
| md.sys.shape.corner-value.large | 16px | — |  |
| md.sys.shape.corner-value.large-increased | 20px | — |  |
| md.sys.shape.corner-value.medium | 12px | — |  |
| md.sys.shape.corner-value.none | 0px | — |  |
| md.sys.shape.corner-value.small | 8px | — |  |
| md.sys.shape.corner.extra-extra-large | 48px | — |  |
| md.sys.shape.corner.extra-large | 28px | 28px |  |
| md.sys.shape.corner.extra-large-increased | 32px | — |  |
| md.sys.shape.corner.extra-large.top | 28px 28px 0px 0px | (28px 28px 0px 0px) |  |
| md.sys.shape.corner.extra-small | 4px | 4px |  |
| md.sys.shape.corner.extra-small.top | 4px 4px 0px 0px | (4px 4px 0px 0px) |  |
| md.sys.shape.corner.full | 9999px | 9999px | Use for: Badge, Buttons, Icon buttons, Sliders, Switches, Search bar |
| md.sys.shape.corner.large | 16px | 16px |  |
| md.sys.shape.corner.large-increased | 20px | — |  |
| md.sys.shape.corner.large.end | 0px 16px 16px 0px | (0px 16px 16px 0px) |  |
| md.sys.shape.corner.large.start | 16px 0px 0px 16px | (16px 0px 0px 16px) |  |
| md.sys.shape.corner.large.top | 16px 16px 0px 0px | (16px 16px 0px 0px) |  |
| md.sys.shape.corner.medium | 12px | 12px |  |
| md.sys.shape.corner.none | 0px | 0px |  |
| md.sys.shape.corner.small | 8px | 8px |  |

- Expressive additions: **large-increased 20**, **extra-large-increased 32**, **extra-extra-large 48**, plus `corner-value-*` (bare `CornerSize` values used for "inner corners" of connected groups and split buttons).
- MWC exposes only the seven single-value corners as custom properties. The directional ones (top, start, end) are Sass-only shorthands composed from them.
- Corner `full` = 9999 px on web. gBreeze uses `50cqmin`, and Compose uses `CircleShape` (50 %). M3 corners are circular arcs, not Apple's continuous "squircle" curve.

### 3.5 md.sys.state: interaction opacities and focus indicator

| token | latest (34.0.21) | v0_192 (shipping MWC) | Compose StateTokens (v0_210) |
|---|---|---|---|
| hover state-layer opacity | **0.08** | 0.08 | 0.08 |
| focus state-layer opacity | **0.10** | 0.12 | 0.10 |
| pressed state-layer opacity | **0.10** | 0.12 | 0.10 |
| dragged state-layer opacity | **0.16** | 0.16 | 0.16 |
| disabled state-layer opacity (new) | **0.38** | — | — |
| disabled content opacity (component tokens) | 0.38 | 0.38 | 0.38 |
| disabled container opacity (buttons, Expressive) | **0.10** | 0.12 | 0.1 |
| focus-indicator thickness | **3 px** | (MWC focus ring: 3 px) | — |
| focus-indicator outer offset | **2 px** | (MWC: 2 px) | — |
| focus-indicator inner offset | **−3 px** | (MWC inward: 0 px) | — |

MWC's `md-focus-ring` defaults are: colour `secondary`, width 3 px, active width 8 px (the "grow" pulse), outward offset 2 px, inward offset 0, shape `corner-full` (inherits the host shape), and a pulse duration of `duration-long4` 600 ms with `easing-emphasized`. In gBreeze the ring is a `secondary` outline that grows to 8 px over 150 ms and shrinks back over 450 ms.

### 3.6 md.sys.elevation

| level | dp (latest `md.sys.elevation.levelN`) | MWC `--md-elevation-level` | Key shadow (opacity 0.3) | Ambient shadow (opacity 0.15) | gBreeze `--md-sys-elevation-shadow-N` / Tailwind |
|---|---|---|---|---|---|
| 0 | 0 | 0 | none | none | `shadow-0` = none |
| 1 | 1 | 1 | `0 1px 2px 0` | `0 1px 3px 1px` | shadow-1 / `shadow-xs` |
| 2 | 3 | 2 | `0 1px 2px 0` | `0 2px 6px 2px` | shadow-2 / `shadow-sm` |
| 3 | 6 | 3 | `0 1px 3px 0` | `0 4px 8px 3px` | shadow-3 / `shadow-md` |
| 4 | 8 | 4 | `0 2px 3px 0` | `0 6px 10px 4px` | shadow-4 / `shadow-lg` |
| 5 | 12 | 5 | `0 4px 4px 0` | `0 8px 12px 6px` | shadow-5 / `shadow-xl` |

I derived the shadow pairs from the `clamp()` formulas in `elevation/internal/_elevation.scss`. They match gBreeze's literal values exactly. The shadow colour is `md.sys.color.shadow` (#000). `md.sys.elevation.surface-tint-color` is deprecated. M3 now conveys elevation with surface-container tones plus shadow, not with tint overlays.

Typical levels: elevated button and card 1 (hover 2); menu 2; nav bar 2; FAB 3 (hover 4; "lowered" 1, hover 2); dialog 3; search bar 3; floating toolbar 3; snackbar 3; slider handle 1; dragged list item and chip 4.

### 3.7 md.sys.motion: durations, easings, springs

| token | latest | v0_192 | note |
|---|---|---|---|
| md.sys.motion.duration.extra-long1 (Duration) | 700ms | 700ms |  |
| md.sys.motion.duration.extra-long2 (Duration) | 800ms | 800ms |  |
| md.sys.motion.duration.extra-long3 (Duration) | 900ms | 900ms |  |
| md.sys.motion.duration.extra-long4 (Duration) | 1000ms | 1000ms |  |
| md.sys.motion.duration.long1 (Duration) | 450ms | 450ms |  |
| md.sys.motion.duration.long2 (Duration) | 500ms | 500ms |  |
| md.sys.motion.duration.long3 (Duration) | 550ms | 550ms |  |
| md.sys.motion.duration.long4 (Duration) | 600ms | 600ms |  |
| md.sys.motion.duration.medium1 (Duration) | 250ms | 250ms |  |
| md.sys.motion.duration.medium2 (Duration) | 300ms | 300ms |  |
| md.sys.motion.duration.medium3 (Duration) | 350ms | 350ms |  |
| md.sys.motion.duration.medium4 (Duration) | 400ms | 400ms |  |
| md.sys.motion.duration.short1 (Duration) | 50ms | 50ms |  |
| md.sys.motion.duration.short2 (Duration) | 100ms | 100ms |  |
| md.sys.motion.duration.short3 (Duration) | 150ms | 150ms |  |
| md.sys.motion.duration.short4 (Duration) | 200ms | 200ms |  |
| md.sys.motion.easing.emphasized.accelerate (Easing) | cubic-bezier(0.3, 0, 0.8, 0.15) | cubic-bezier(0.3, 0, 0.8, 0.15) |  |
| md.sys.motion.easing.emphasized.decelerate (Easing) | cubic-bezier(0.05, 0.7, 0.1, 1) | cubic-bezier(0.05, 0.7, 0.1, 1) |  |
| md.sys.motion.easing.legacy (Easing) | cubic-bezier(0.4, 0, 0.2, 1) | cubic-bezier(0.4, 0, 0.2, 1) |  |
| md.sys.motion.easing.legacy.accelerate (Easing) | cubic-bezier(0.4, 0, 1, 1) | cubic-bezier(0.4, 0, 1, 1) |  |
| md.sys.motion.easing.legacy.decelerate (Easing) | cubic-bezier(0, 0, 0.2, 1) | cubic-bezier(0, 0, 0.2, 1) |  |
| md.sys.motion.easing.linear (Easing) | cubic-bezier(0, 0, 1, 1) | cubic-bezier(0, 0, 1, 1) |  |
| md.sys.motion.easing.standard (Easing) | cubic-bezier(0.2, 0, 0, 1) | cubic-bezier(0.2, 0, 0, 1) |  |
| md.sys.motion.easing.standard.accelerate (Easing) | cubic-bezier(0.3, 0, 1, 1) | cubic-bezier(0.3, 0, 1, 1) |  |
| md.sys.motion.easing.standard.decelerate (Easing) | cubic-bezier(0, 0, 0, 1) | cubic-bezier(0, 0, 0, 1) |  |
| md.sys.motion.spring.default.effects.damping (Spring) | 1 | — |  |
| md.sys.motion.spring.default.effects.stiffness (Spring) | 1600 | — |  |
| md.sys.motion.spring.default.spatial.damping (Spring) | 0.9 | — |  |
| md.sys.motion.spring.default.spatial.stiffness (Spring) | 700 | — |  |
| md.sys.motion.spring.fast.effects.damping (Spring) | 1 | — |  |
| md.sys.motion.spring.fast.effects.stiffness (Spring) | 3800 | — |  |
| md.sys.motion.spring.fast.spatial.damping (Spring) | 0.9 | — |  |
| md.sys.motion.spring.fast.spatial.stiffness (Spring) | 1400 | — |  |
| md.sys.motion.spring.slow.effects.damping (Spring) | 1 | — |  |
| md.sys.motion.spring.slow.effects.stiffness (Spring) | 800 | — |  |
| md.sys.motion.spring.slow.spatial.damping (Spring) | 0.9 | — |  |
| md.sys.motion.spring.slow.spatial.stiffness (Spring) | 300 | — |  |
| md.sys.motion.easing.emphasized (Easing) | cubic-bezier(0.2, 0, 0, 1) | cubic-bezier(0.2, 0, 0, 1) |  |

Notes (rows for the composite tokens `md.sys.motion.path` and `spring.*` (composite), which the generator cannot express, are omitted):

- **`easing-emphasized` changed meaning.** The real emphasized curve is a two-segment path that CSS cannot express, and the generator emits `"motion_path" is not supported`. Latest therefore aliases `easing-emphasized` to `easing-standard` (`cubic-bezier(0.2,0,0,1)`). MWC's `internal/motion/animation.ts` hard-codes `EMPHASIZED: cubic-bezier(.3,0,0,1)`. For a faithful web emphasized curve, use `linear()` sampled from the path, or keep the `.3,0,0,1` approximation.
- **Springs are the primary Expressive motion system.** In CSS they appear only as the sampled `linear()` in gBreeze's button group ("fast-spatial", 350 ms) and the overshooting bezier `cubic-bezier(0.42, 1.67, 0.21, 0.9)` (350 ms) used for button corner morphs. My numerical check: the `linear()` samples reproduce stiffness **800**, damping **0.6** (Compose *Expressive* fast-spatial; peak 1.095) to within 0.002. The web sys tokens' 1400/0.9 would barely overshoot (peak 1.002). Settle times (to within 0.1 %): 800/0.6 ≈ 0.41 s; 1400/0.9 ≈ 0.21 s; 700/0.9 ≈ 0.29 s; 380/0.8 ≈ 0.44 s.

**Compose motion schemes** (`MotionSchemeKeyTokens`: DefaultSpatial, FastSpatial, SlowSpatial, DefaultEffects, FastEffects, SlowEffects). The web `md.sys.motion.spring.*` values equal Compose **Standard**. Compose additionally ships an **Expressive** scheme. *Spatial* springs move position, size and shape and may bounce. *Effects* springs animate colour and opacity and never overshoot (damping 1).

| token | Standard: stiffness / damping ratio | Expressive: stiffness / damping ratio | ≈ SwiftUI `response` (2π/√k) | ≈ SwiftUI `bounce` (1 − ζ) |
|---|---|---|---|---|
| fast spatial | 1400 / 0.9 | **800 / 0.6** | 0.17 s / 0.22 s | 0.10 / 0.40 |
| default spatial | 700 / 0.9 | **380 / 0.8** | 0.24 s / 0.32 s | 0.10 / 0.20 |
| slow spatial | 300 / 0.9 | **200 / 0.8** | 0.36 s / 0.44 s | 0.10 / 0.20 |
| fast effects | 3800 / 1.0 | 3800 / 1.0 | 0.10 s | 0 |
| default effects | 1600 / 1.0 | 1600 / 1.0 | 0.16 s | 0 |
| slow effects | 800 / 1.0 | 800 / 1.0 | 0.22 s | 0 |

The conversion assumes unit mass, ω = √k and response = 2π/ω. A damping ratio ζ < 1 overshoots; SwiftUI's "bounce" ≈ 1 − ζ. **This table is the bridge between M3 Expressive springs and Apple springs for the parent system.** SwiftUI's presets (`.smooth` bounce 0, `.snappy` ≈ 0.15, `.bouncy` ≈ 0.3, all with a 0.5 s default duration) are slower and softer than M3's spatial springs, so express M3 springs explicitly with `Spring(response:dampingRatio:)` or `.spring(duration:bounce:)` using the values above. Component tokens reference these directly. For example, every Expressive button size uses `pressed-container-corner-size-motion-spring` = fast-spatial (1400/0.9 in the web tokens, but 800/0.6 in practice in gBreeze). Button groups use the same spring for `pressed-item-width` (pressed item grows by **15 %**, `pressed-item-width-multiplier` 15 %, or 1.15 in gBreeze).

### 3.8 Space, density and breakpoints

- **Spacing:** there is no `md.sys.space` in the generated tokens. gBreeze defines `--md-sys-space-unit: 8px` with named steps (§2.3), and Tailwind gets `--spacing: 4px` (half unit). Components hard-code paddings in their own tokens.
- **Density:** MWC has **none**. The roadmap lists "Density and spacing tokens" as unrealised. Expressive replaces density with *explicit size variants*: XS 32, S 40, M 56, L 96 and XL 136 for buttons, icon buttons, split buttons and button groups; XS–XL for sliders (track 16/24/40/56/96). The parent system must define its own density model for desktop (macOS regular, small and mini control sizes).
- **Window-size classes** (from the gBreeze Tailwind theme): compact < 600; **medium 600–839; expanded 840–1199; large 1200–1599; extra-large ≥ 1600**.
- **Touch target:** 48 × 48 px minimum. MWC buttons render an invisible `.touch` element (`height: max(48px, 100%)`), configurable with `touch-target="wrapper"` (adds margin) or `"none"`. `--md-switch-touch-target-size` is 48 px. Checkbox, radio and icon-button state layers are 40 px.


---

## 4. Component catalog: API and token values

Conventions:

- "MWC" means the stable `@material/web` element on v0_192 tokens.
- "Expressive" means the GM3 34.0.21 tokens and/or the `labs/gb` implementation.
- Every MWC component token is overridable as `--md-<component>-<token>`. The full lists with defaults are in `corpus/material-web/tokens/mwc-component-custom-properties.md`, about 1,970 rows across 49 property families.
- Shared base API for the form-associated controls (button, icon button, checkbox, radio, switch, slider, text field, select): `name`, `disabled`, `form` (read-only), `labels` (read-only). The value-bearing ones also have `required`, `validity`, `validationMessage`, `willValidate`, `checkValidity()`, `reportValidity()`, `setCustomValidity()`, `formResetCallback()` and `formStateRestoreCallback()`. All use `ElementInternals` with `static formAssociated = true`.

### 4.1 Common buttons

**MWC tags:** `md-elevated-button`, `md-filled-button`, `md-filled-tonal-button`, `md-outlined-button`, `md-text-button`.
**Properties and attributes:**

- `disabled`, `soft-disabled` (disabled but focusable, for toolbars)
- `href`, `target` (`_blank|_parent|_self|_top`), `download`; Sep 2026 added `rel` and `referrerpolicy`, and hrefs are sanitised with `safevalues`
- `trailing-icon`, `has-icon`
- `type` (`submit|reset|button`; default `submit`), `name`, `value`, `form`, `labels`

**Slots:** default (label) and `icon`. 2.4 added gradient container support and disabled links.
**Accessibility:** `aria-label` is forwarded to the inner `<button>` or `<a>` (`mixinDelegatesAria`, `delegatesFocus: true`).

| token (MWC, v0_192) | elevated | filled | filled tonal | outlined | text |
|---|---|---|---|---|---|
| container-color | surface-container-low | primary | secondary-container | — (transparent) | — |
| label/icon color | primary | on-primary | on-secondary-container | primary | primary |
| outline | — | — | — | outline, 1 px | — |
| container elevation (rest/hover) | 1 / 2 | 0 / 1 | 0 / 1 | — | — |
| container-height | 40 px | 40 | 40 | 40 | 40 |
| container-shape | corner-full | full | full | full | full |
| leading/trailing space | 24/24 (16/24 with leading icon; 24/16 with trailing icon) | same | same | same | 12/12 (12/16 with leading icon, 16/12 with trailing icon) |
| icon-size | 18 px | 18 | 18 | 18 | 18 |
| label typography | label-large 14/20, 500 | | | | |
| disabled | container on-surface @ 0.12; label on-surface @ 0.38 | | | | |
| min width | 64 px (`calc(64px - leading - trailing)` min content width) | | | | |

**Expressive buttons** (latest `md-comp-button-*` and gBreeze `.btn`; `md-gb-button` attributes `color=filled|elevated|tonal|outlined|text`, `size=xs|sm|md|lg|xl` (default `sm`), `square`, `selected`, `type=toggle`, `soft-disabled`, `href`, `target`, `download`, `rel`, `referrerpolicy`; slots default and `container`; part `btn`; events `input`/`change` on toggle):

| size | height | leading/trailing | icon | icon–label gap | outline | label type | shape round → selected | shape square → selected | pressed shape |
|---|---|---|---|---|---|---|---|---|---|
| XS | 32 | 12/12 | 20 | 8 | 1 | label-large | full → medium 12 | medium 12 → full | small 8 |
| S (default) | 40 | 16/16 | 20 | 8 | 1 | label-large | full → 12 | 12 → full | 8 |
| M | 56 | 24/24 | 24 | 8 | 1 | **title-medium** | full → large 16 | 16 → full | 12 |
| L | 96 | 48/48 | 32 | 12 | 2 | **headline-small** | full → xl 28 | 28 → full | 16 |
| XL | 136 | 64/64 | 40 | 16 | 3 | **headline-large** | full → 28 | 28 → full | 16 |

- **Toggle (selected/unselected) colours:**
  - Filled: unselected surface-container with on-surface-variant; selected primary with on-primary.
  - Tonal: selected secondary with on-secondary.
  - Outlined: selected **inverse-surface** with inverse-on-surface; outline colour is now **outline-variant**, no longer `outline`.
  - Elevated: selected primary.
- **Disabled container opacity** is 0.10 (MWC: 0.12).
- **Shape morph motion:** fast-spatial spring (web tokens 1400/0.9; gBreeze CSS `350ms cubic-bezier(0.42,1.67,0.21,0.9)`, an overshooting approximation closer to the expressive 800/0.6).
- **Icon fill:** `--md-icon-fill` is 1 when selected and 0 when unselected.
- **Compose divergence (ButtonXSmallTokens v0_11_0):** XS leading space 16 dp (web 34.0.21: 12 px), and selected-round shape stays full (web: corner-medium). The web tokens are newer.

### 4.2 Icon buttons

**MWC tags:** `md-icon-button` (standard), `md-filled-icon-button`, `md-filled-tonal-icon-button`, `md-outlined-icon-button`. **Properties:** `toggle`, `selected`, `aria-label-selected`, `flip-icon-in-rtl`, `href`, `target`, `download`, `soft-disabled`, plus the form button API. **Slots:** default (icon) and `selected` (icon shown when selected). **Events:** `input`, `change` (toggle).

- **Tokens:** container 40 × 40, state layer 40 (standard), icon 24, shape full. Outlined: 1 px `outline`; selected uses inverse-surface/inverse-on-surface.
- **Filled toggle:** unselected container **surface-container-highest** with icon primary; selected primary with on-primary.
- **Expressive** (`md-comp-icon-button-{xsmall…xlarge}`; `md-gb-icon-button`: `color=filled|tonal|outlined|standard`, `size=xs…xl` (default `sm`), `width=narrow|wide|''`, `square`, `selected`):

| size | height | icon | default lead/trail | narrow | wide | outline | shape (round / square) | selected (round / square) | pressed |
|---|---|---|---|---|---|---|---|---|---|
| XS | 32 | 20 | 6 | 4 | 10 | 1 | full / 12 | 12 / full | 8 |
| S | 40 | 24 | 8 | 4 | 14 | 1 | full / 12 | 12 / full | 8 |
| M | 56 | 24 | 16 | 12 | 24 | 1 | full / 16 | 16 / full | 12 |
| L | 96 | 32 | 32 | 16 | 48 | 2 | full / 28 | 28 / full | 16 |
| XL | 136 | 40 | 48 | 32 | 72 | 3 | full / 28 | 28 / full | 16 |

The width of an icon button = icon + leading + trailing. For example, S default = 24 + 8 + 8 = 40 (square), S wide = 52.

### 4.3 FAB and extended FAB

**MWC tags:** `md-fab` and `md-branded-fab`. **Properties:** `variant` (`surface` (default) | `primary` | `secondary` | `tertiary`), `size` (`small` | `medium` | `large`), `label` (non-empty means extended FAB), `lowered`. **Slot:** `icon`.

| token (MWC) | small | medium | large | branded | branded large |
|---|---|---|---|---|---|
| container | 40 × 40, corner 12 | 56 × 56, corner 16 | 96 × 96, corner 28 | 56, 16 | 96, 28 |
| icon | 24 | 24 | 36 | 36 | 48 |
| elevation (rest/hover; lowered rest/hover) | 3/4; 1/2 | | | | |
| colour by variant | surface: surface-container-high with primary icon; primary: primary-container with on-primary-container; secondary: secondary-container; tertiary: tertiary-container | | | branded container surface-container-high | |
| extended | height 56, label = label-large, leading/trailing 16, icon gap 12 | | | | |

**Expressive** (`md-comp-fab*`; `md-gb-fab`: `color=primary|primary-container (default)|secondary|secondary-container|tertiary|tertiary-container`, `size=default|md|lg`). The **surface variant is gone** and small is no longer offered in gBreeze.

| | baseline | medium (new) | large | small (token only) |
|---|---|---|---|---|
| FAB | 56, corner 16 (large), icon 24 | **80, corner 20 (large-increased), icon 28** | 96, corner 28, icon 36 (Compose 32) | 40, corner 12 |
| Extended FAB | 56, shape 16, icon 24, gap 8, padding 16, label **title-medium** | 80, shape 20, icon 28, gap 12 (Compose 16), padding 26, label **title-large** | 96, shape 28, icon 36 (Compose 32), gap 16 (Compose 20), padding 28, label **headline-small** | — |

**FAB menu** (Expressive, `md-comp-fab-menu*`): close button 56 × 56, full shape, icon 20, elevation 3 (hover 4), colour primary/on-primary. Items: height 56, pill (full), padding 24/24, icon 24, gap 8, label title-medium, between-space 4, colour primary-container/on-primary-container (or secondary/tertiary sets), item elevation 0 in web 34.0.21 (Compose: level 3).

### 4.4 Split button and button groups (Expressive only)

- **Split button** (`md-comp-split-button-{xs…xl}`; `md-gb-split-button`: `color=filled|elevated|tonal|outlined`, `size=xs…xl`, `selected`). Two buttons separated by a 2 px gap. Outer corners are full (50 %). Inner corners are small at rest, larger on hover and press, and become 50 % on the trailing button when the menu is open (selected).

| size | height | inner corner (rest → hover/press) | leading btn L/T | trailing btn L/T | trailing icon |
|---|---|---|---|---|---|
| XS | 32 | 4 → 8 | 12/10 | 13/13 | 22 |
| S | 40 | 4 → 12 | 16/12 | 13/13 | 22 |
| M | 56 | 4 → 12 | 24/24 | 15/15 | 26 |
| L | 96 | 8 → 20 | 48/48 | 29/29 | 38 |
| XL | 136 | 12 → 20 | 64/64 | 43/43 | 50 |

- **Button group** (`md-comp-button-group-{standard|connected}-{xs…xl}`; `md-gb-button-group`: variant `standard|connected`, selection `none|single|multiple`; events `input`/`change`).
  - *Standard* between-space: XS 18, S 12, M 8, L 8, XL 8. The pressed item widens by 15 % and neighbours compress, using fast-spatial springs.
  - *Connected* between-space: 2. Outer corners full. Inner corners: XS–M 8 (pressed 4), L 16 (12), XL 20 (16). Selected inner corner 50 %. gBreeze overrides XS inner corners to 4 ("Design override of GM3 v35").

### 4.5 Chips

**MWC tags:** `md-chip-set` (roving tabindex), `md-assist-chip`, `md-filter-chip`, `md-input-chip`, `md-suggestion-chip`.

- **Common properties:** `label`, `disabled`, `soft-disabled`, `always-focusable`, `has-icon`.
- **Assist and suggestion chips:** `elevated`, `href`, `target`, `download`.
- **Filter chip:** `selected`, `removable`, `elevated`, `has-selected-icon`, `aria-label-remove`.
- **Input chip:** `avatar`, `selected`, `remove-only`, `href`, `aria-label-remove`.
- **Events:** `remove` (filter/input chips), `update-focus` (all); filter chips also emit native `input`/`change`.
- **Slots:** `icon`, `selected-icon` (filter), `remove-trailing-icon`.
- **Tokens:** height 32, shape **small 8**, outline 1 px `outline` (Expressive: outline-variant), icon 18, padding 16 (8 next to an icon), label label-large.
  - Filter selected: secondary-container with on-secondary-container, outline 0.
  - Elevated chips: surface-container-low, level 1 (hover 2). Dragged: level 4.
  - Input chip avatar: 24, full.
- **Expressive** (`md-gb-chip`): `color=elevated|filled|outlined|tonal`, `type=action|filter|toggle|link`, `selected`, `removable`; slots default, `icon`, `remove-icon`.

### 4.6 Text fields and field

**MWC tags:** `md-filled-text-field`, `md-outlined-text-field`. The underlying `md-filled-field` and `md-outlined-field` are also usable on their own.

- **Properties:** `label`, `value`, `type` (`text|email|number|password|search|tel|url|textarea`; unsupported: color, date, datetime-local, file, month, time, week), `placeholder`, `prefix-text`, `suffix-text`, `supporting-text`, `error`, `error-text`, `required`, `no-asterisk`, `has-leading-icon`, `has-trailing-icon`, `text-direction`, `rows`/`cols` (textarea), `min`/`max`/`step`/`minLength`/`maxLength`/`pattern`/`multiple`/`readOnly`/`autocomplete`/`inputMode`, `no-spinner`; character counter via `maxlength`.
- **Methods:** `select()`, `setRangeText()`, `setSelectionRange()`, `showPicker()` (2.3), `stepUp()`/`stepDown()`, `reset()`.
- **Events:** native `input`, `change`, `select` (re-dispatched).
- **Slots:** `leading-icon`, `trailing-icon`, and `container` (2.2, custom background).

| token (MWC) | filled | outlined |
|---|---|---|
| container | **surface-container-highest**, corner extra-small-top (4 4 0 0) | transparent, corner extra-small 4 |
| indicator / outline | active indicator 1 px on-surface-variant (hover 1 px on-surface, focus **2 px primary**) | outline 1 px `outline` (hover on-surface, focus **2 px primary**) |
| height (implicit) | 56 (top/bottom space 16; with label 8/8) | 56 (16/16) |
| horizontal padding | 16 (12 next to icons) | 16 (12 next to icons); label notch padding 4 |
| icons | 24, on-surface-variant | same |
| input text | body-large 16/24, on-surface; caret primary | same |
| label | body-large → populated body-small 12/16; focused primary; error `error` | same |
| supporting text | body-small, on-surface-variant, top 4 | same |

**Expressive deltas (34.0.21):** the focused outline is **3 px** (`focus-outline-width` 3, focus-indicator thickness) for outlined fields, and the filled field's focused active-indicator thickness is 3. Container height is explicitly 56.

### 4.7 Select

**MWC tags:** `md-filled-select`, `md-outlined-select`, `md-select-option`.

- **Select properties:** `label`, `value`, `selected-index`, `required`, `error`, `error-text`, `supporting-text`, `no-asterisk`, `display-text`, `has-leading-icon`, `menu-positioning` (`absolute|fixed|popover`, **default `popover`**), `clamp-menu-width`, `menu-align` (`start|end`), `typeahead-delay`, `quick`.
- **Select methods:** `select(value)`, `selectIndex(i)`, `reset()`, `showPicker()`.
- **Select events:** `input`, `change`, `opening`, `opened`, `closing`, `closed`.
- **Option properties:** `value`, `selected`, `disabled`, `display-text`, `typeahead-text`. **Option slots:** `headline`, `supporting-text`, `overline`, `start`, `end`, `trailing-supporting-text`.
- **Tokens:** the text-field set prefixed `--md-filled-select-text-field-*`, plus `--md-filled-select-select-*` menu tokens.

### 4.8 Lists and items

**MWC tags:** `md-list` (role `list`; `activateNextItem()`/`activatePreviousItem()`) and `md-list-item`.

- **List item properties:** `type` (`text|button|link`), `href`, `target`, `disabled`.
- **List item slots:** `start`, `end`, `headline` (default), `supporting-text`, `overline`, `trailing-supporting-text`, `container`.
- **List item event:** `request-activation`.
- `labs/item` (`md-item`) is the reusable layout primitive.

| token (MWC) | value |
|---|---|
| one-line / two-line height | 56 / 72 (three-line 88 in tokens) |
| padding | leading 16, trailing 16, top/bottom 12 (Expressive 10/10) |
| label | body-large, on-surface |
| supporting text | body-medium, on-surface-variant |
| trailing supporting text | label-small, on-surface-variant |
| icons | 24 (Expressive: 20 "expressive size"), on-surface-variant |
| avatar, image, video | avatar 40 full; image 56 × 56; video 100 × 56 (large 114 × 64) |
| container | surface (list container colour `--md-list-container-color` = surface) |

**Expressive lists** (`md-comp-list`, `list-expand`, `list-reorder`, `list-reveal`; `md-gb-list`/`md-gb-list-item` with slots `avatar`, `leading`, `overline`, default, `supporting-text`, `trailing-text`, `trailing`; attribute `static` = non-interactive):

- "Segmented" lists: items are separate rounded tiles with a **2 px gap**. Container shape large 16. Item shape extra-small 4. It morphs on interaction: hovered 12, focused 16, dragged 16 at level 4.
- Inner focus indicator (−3 px offset).
- Item between-space 12, leading image corner 8.
- Reorder items: tertiary-container, shape 16.
- Reveal list: action button primary.

### 4.9 Menus

**MWC tags:** `md-menu`, `md-menu-item`, `md-sub-menu`.

- **Menu properties:** `anchor` (id) or `anchorElement`, `positioning` (`absolute|fixed|document|popover`), `open`, `quick`, `has-overflow`, `x-offset`, `y-offset`, `anchor-corner` (default `end-start`), `menu-corner` (default `start-start`), `no-horizontal-flip`, `no-vertical-flip`, `typeahead-delay` (200 ms), `stay-open-on-outside-click`, `stay-open-on-focusout`, `skip-restore-focus`, `default-focus` (`FIRST_ITEM` …), `no-navigation-wrap`.
- **Menu methods:** `show()`, `close()`, `reposition()`, `activateNextItem()`/`activatePreviousItem()`.
- **Menu events:** `opening`, `opened`, `closing`, `closed`.
- **Menu item:** `type` (`menuitem|option|button|link`), `href`, `target`, `keep-open`, `selected`, `disabled`, `typeahead-text`; slots as for list item; event `close-menu`.
- **Sub-menu:** `anchor-corner` `start-end`, `hover-open-delay` and `hover-close-delay` 400 ms.

| token (MWC) | value |
|---|---|
| container | surface-container, **corner extra-small 4**, elevation level 2, top/bottom padding 8 |
| item | height 56 (two-line 72), padding 16, label body-large on-surface (Expressive menus: label-large) |
| selected item | secondary-container with on-secondary-container |

**Expressive menus** (`md-comp-menus`, `menus-standard`, `menus-vibrant`, `md-gb-menu` `color=standard|vibrant`, `md-gb-menu-group`, `md-gb-menu-item` with `checkable=single|multiple` semantics):

| | Expressive value |
|---|---|
| container | **corner large 16**, elevation level 2; standard = surface-container-low, vibrant = **tertiary-container** |
| groups | gap 2, group padding 2 (Compose segmented: 4), group shape 8; inactive container 8; active container 16 |
| item | height **44**, padding 16/16, top/bottom 8, between 12, icons 20, label **label-large** (14/20, 500; Compose `SegmentedMenuTokens` 24.1.2 uses body-large), supporting body-small; item shape 4, first/last child 12 with 4 inner corner, selected 12 |
| selected | standard: tertiary-container with on-tertiary-container; vibrant: tertiary with on-tertiary |
| horizontal menus (menubar) | pill container (full), items 12/6 padding, selected item full shape |
| focus | inner indicator (−3 px) |

### 4.10 Dialog

**MWC tag:** `md-dialog`, built on the native `<dialog>` with `showModal()`.

- **Properties:** `open`, `quick`, `returnValue`, `type` (`alert` → role `alertdialog`), `no-focus-trap`, `getOpenAnimation`, `getCloseAnimation`.
- **Methods:** `show()`, `close(returnValue)`.
- **Events:** `open`, `opened`, `close`, `closed`, `cancel`.
- **Slots:** `headline`, `icon`, `content`, `actions`. Form `method="dialog"` integrates with `returnValue`.

| token | value |
|---|---|
| container | **surface-container-high**, corner **extra-large 28**, elevation 3 (Expressive tokens: level 3) |
| headline | headline-small 24/32, on-surface; icon 24 secondary |
| supporting text | body-medium, on-surface-variant |
| actions | label-large, primary |
| scrim | `md.sys.color.scrim` (#000) at 0.32 opacity (M3 scrim token) |
| full-screen dialog | corner 0, header 56 tall |

### 4.11 Tabs

**MWC tags:** `md-tabs` (`active-tab-index`, `auto-activate`, `scrollToTab()`, event `change`), `md-primary-tab` (`inline-icon`, `icon-only`, `has-icon`, `active`; slot `icon`), `md-secondary-tab`.

| token | primary | secondary |
|---|---|---|
| height | 48; 64 with icon and label (inline-icon 48) | 48 |
| active indicator | **3 px**, shape 3 3 0 0, primary; width hugs the content | **2 px**, full width, primary |
| active label/icon | primary | on-surface |
| inactive | on-surface-variant | on-surface-variant |
| label | title-small 14/20, 500 | title-small |
| divider | 1 px outline-variant | same |
| focus (Expressive) | inner focus indicator −3 px | |

The gBreeze `.tabs`/`.tab` classes use CSS anchor positioning for the indicator and `focusgroup="tablist inline"`. `md-gb-tabs` has `variant=primary|secondary`.

### 4.12 Selection controls

| component | MWC API | key tokens (MWC v0_192) | Expressive (34.0.21) |
|---|---|---|---|
| `md-checkbox` | `checked`, `indeterminate`, `required`, `value='on'`; events `input`, `change` | container 18 × 18, **corner 2**, outline 2 px on-surface-variant; selected primary with on-primary check; state layer 40 full; error uses `error` | same geometry; selected outline 0; focus indicator outer +2 |
| `md-radio` | `checked`, `required`, `value`, `name` (group via name); events `input`, `change` | icon 20, unselected on-surface-variant, selected primary, state layer 40 | same |
| `md-switch` | `selected`, `icons`, `show-only-selected-icon`, `required`, `value`; events `input` (composed), `change`; slots `on-icon`, `off-icon` | track **52 × 32**, outline 2 px `outline`; handle 16 (unselected), 24 (selected or with icon), 28 pressed; handle colours outline → on-primary; selected track primary; icon 16; state layer 40; touch target 48 | identical geometry; `md-gb-switch` |
| `md-slider` | `min=0`, `max=100`, `value`, `step=1`, `range`, `value-start`/`value-end`, `name-start`/`name-end`, `labeled`, `ticks`, `value-label(-start/-end)`, `aria-label-start/end`, `aria-valuetext-start/end` | track **4 px** (active primary, inactive surface-container-highest), handle **20 × 20 circle** at level 1, value label container 28 (primary with on-primary), tick 2 px | **completely redesigned:** active and inactive tracks 16 (XS), **handle 4 × 44 bar** (2 px when focused or pressed), 6 px gap each side of the handle, stop indicator 4 px; sizes XS 16, S 24, M 40, L 56 (handle 68), XL 96 (handle 108) with inline icons (M–XL 24/24/32); track colours primary / **secondary-container**; value indicator inverse-surface; `md-gb-slider` `size`, `orientation=horizontal|vertical`, `centered` |

### 4.13 Progress indicators

**MWC tags:** `md-linear-progress` (`value`, `max=1`, `buffer`, `indeterminate`, `four-color`) and `md-circular-progress` (`value`, `max`, `indeterminate`, `four-color`).

- **MWC tokens:** linear track 4 px, active primary, track surface-container-highest, shape 0. Circular 48 px, 4 px width. Four-colour mode cycles primary → primary-container → tertiary → tertiary-container.
- **Expressive** (`md-comp-progress-indicator*`, Compose `LinearProgressIndicatorTokens`, `CircularProgressIndicatorTokens`):
  - Rounded (full) track and indicator, with a **4 px gap** between active and track and a **4 px stop indicator** at the end.
  - Optional **wavy** active indicator: linear amplitude 3, wavelength 40 (indeterminate 20), total height 10 (thick variant: 8 px track, 14 px with wave). Circular size 40 (wavy 48), amplitude 1.6, wavelength 15, thick variant 8 px / 52.
- **Loading indicator** (new): 48 × 48 container, 38 px active shape morphing through M3 shapes. Colour primary on transparent, or *contained* on primary-container with on-primary-container.

### 4.14 Navigation (labs in MWC; Expressive tokens)

| component | MWC labs API | MWC v0_192 tokens | Expressive (34.0.21 / gBreeze / Compose) |
|---|---|---|---|
| Navigation bar | `md-navigation-bar` (`active-index`, `hide-inactive-labels`; event `navigation-bar-activated`) and `md-navigation-tab` (`label`, `active`, `badge-value`, `show-badge`, `hide-inactive-label`; slots `active-icon`, `inactive-icon`) | height **80**, surface-container, level 2; indicator **64 × 32** pill, secondary-container; active icon on-secondary-container, active label on-surface; label label-medium | height **64** ("flexible"; Compose `TallContainerHeight` 80 kept for legacy), level 2; vertical item: indicator **56 × 32**, icon 24, label label-medium, active label **secondary**; horizontal item (medium windows): indicator 40 tall, padding 16; `md-gb-nav-bar` `item-layout=vertical|horizontal`, `selected-index`; `md-gb-nav-bar-item` `label`, `badge`, `active`, `disabled` |
| Navigation rail | — (not implemented) | 80 wide (v0_192 token) | collapsed **96** wide (narrow 80), top space 44, item height 64 (short 56), vertical item indicator 56 × 32; **expanded rail 220–360** wide, horizontal item indicator 56 tall, label label-large; modal expanded: surface-container, corner 16, level 2; standard container `surface` |
| Navigation drawer | `md-navigation-drawer` and `md-navigation-drawer-modal` (`opened`, `pivot=start|end`; event `navigation-drawer-changed`) | width 360, standard: surface; modal: surface-container-low, level 1, corner large-end (0 16 16 0); indicator 336 × 56 pill, secondary-container | superseded by the expanded nav rail |
| Top app bar | — | small 64, medium 112, large 152 | `md-comp-app-bar*`: small 64 (title title-large, subtitle label-medium; search variant 56 pill), medium **flexible** 112 (136 with subtitle; title headline-medium), large flexible 120 (152 with subtitle; title **display-small**); on scroll: surface-container, level 2; `md-gb-app-bar` `size=sm|md|lg`, `variant=standard|search`, `scrolled`; slots `leading`, `trailing`, `search`, `subtitle`; event `scrollstatechange` |
| Toolbars | — | (bottom app bar 80) | **docked** 64 tall, surface-container, square, spacing clamp(4, 4vw, 32), padding 16; **floating** 64, pill, level 3, padding 8, gap 4, external margin 16 (vertical 64 wide, 24 margin); FAB beside a floating toolbar: 56 (medium 80); colour **standard** (surface-container; selected secondary-container) or **vibrant** (primary-container; selected surface-container); `md-gb-toolbar` `color`, `orientation`, `docked` |

### 4.15 Cards, segmented buttons, badge, divider, icon, elevation, ripple, focus ring

| component | API | tokens |
|---|---|---|
| Cards (labs) `md-elevated-card`, `md-filled-card`, `md-outlined-card` | slot default (2.5 adds `container` slot in the gb card) | corner **medium 12**. Elevated: surface-container-low, level 1 (hover 2). Filled: **surface-container-highest**, level 0. Outlined: surface, 1 px **outline-variant**. Dragged: level 3–4. gBreeze `md-gb-card`: `color=elevated|filled|outlined`, `interactive`, `disabled`, parts `card` and `card-btn`. |
| Segmented button (labs) `md-outlined-segmented-button-set` (`multiselect`; event `segmented-button-set-selection`) and `md-outlined-segmented-button` (`label`, `selected`, `disabled`, `no-checkmark`, `has-icon`; slot `icon`) | | height 40, outline 1 px `outline`, shape full, icon 18; selected secondary-container with on-secondary-container. **Expressive replaces it with the connected button group.** |
| Badge (labs) `md-badge` (`value`) | | small 6 px dot; large 16 tall, label-small 11/16, `error` with on-error, full |
| `md-divider` | `inset`, `inset-start`, `inset-end`; decorative unless `role="separator"` | 1 px, outline-variant |
| `md-icon` | default slot (ligature, codepoint or SVG) | `--md-icon-font` `'Material Symbols Outlined'`, `--md-icon-size` 24. gBreeze adds variable axes `opsz`, `wght`, `FILL`, `GRAD`. |
| `md-elevation` | placed inside a positioned parent; inherits `border-radius` and transitions | `--md-elevation-level` 0–5, `--md-elevation-shadow-color` |
| `md-ripple` | `for`/`htmlFor`, `control`, `attach()`, `detach()`, `disabled` | hover on-surface @ 0.08, pressed on-surface @ 0.12 (latest 0.10). Press grows from 20 % to full radius (hypotenuse + 10 px padding, soft edge max(35 % of the larger dimension, 75 px)) over **450 ms**; minimum press 225 ms; touch delay 150 ms; respects `forced-colors` |
| `md-focus-ring` | `visible`, `inward`, `for`/`htmlFor`, `control`, `attach()`, `detach()`; event `visibility-changed` | `:focus-visible`-driven; color secondary, width 3, active 8, outward 2, inward 0, duration 600 ms; `prefers-reduced-motion` disables the pulse |

### 4.16 Expressive-only components with tokens but no MWC implementation

The 34.0.21 token dump also covers these, useful as spec values: banners (basic and rich), bottom app bar, carousel item (corner 28), data table, date pickers (docked and modal), date input, drag handle (4 × 48 pill; pressed 12 × 52, corner 12), **search bar** (56 tall pill, level 3, avatar 30) and **search view** (docked corner 28; full-screen header 72), **bottom sheet** (corner 28 top, drag handle 32 × 4, level 1), side sheet (256 wide; modal corner large-start 16), **snackbar** (single line 48, two lines 68, corner 4, level 3, inverse-surface; `md-gb-snackbar`: `timeout-ms` 5000, `label-text`, `action-label`, `has-close-button`, `close-label`, `fixed`, `quick`; slots `action`, `dismiss`), plain tooltip (corner 4, body-small, inverse-surface), rich tooltip (corner 12, level 2), time picker and time input, autocomplete (filled and outlined), menu buttons, and the scrim.


---

## 5. Theming, dark mode, dynamic colour, contrast

### 5.1 How theming works in MWC (Track A)

- **Set system roles on any selector.** Custom properties inherit through shadow roots:

```css
:root { --md-sys-color-primary: #006A6A; --md-sys-color-on-primary: #fff; /* … */
        --md-ref-typeface-brand: 'Open Sans'; --md-ref-typeface-plain: system-ui;
        --md-sys-shape-corner-medium: 6px; }
md-filled-button.error { --md-sys-color-primary: var(--md-sys-color-error);
                         --md-sys-color-on-primary: var(--md-sys-color-on-error); }
```

- **Component overrides** use `--md-<comp>-<token>`. The docs recommend changing the *system* role a component maps to rather than every state token, because hover, focus and pressed colours derive from it.
- **Sass APIs:** `@use '@material/web/color/color'` → `color.light-theme`, `color.dark-theme` (both accept an `$md-ref-palette` map), `color.theme($tokens)`; `typography.theme`; per-component `theme($tokens)` mixins that validate against `$supported-tokens`.
- **Dark mode is not automatic.** From the FAQ: "It's up to the app to decide when and how dark mode is applied … the CSS size for automatically supporting it is much higher and not as flexible." The pattern is `:root { @include color.light-theme; @media (prefers-color-scheme: dark) { @include color.dark-theme; } }`, or toggle a class or attribute that swaps the 49 `--md-sys-color-*` values.
- **The catalog's runtime theming** (`catalog/src/utils/material-color-helpers.ts`) builds a `SchemeContent(Hct.fromInt(argbFromHex(color)), isDark, 0)` scheme. It reads 40+ `MaterialDynamicColors` roles into a `:root,:host{--md-sys-color-*}` string and applies it as an adopted stylesheet. This is the reference recipe for runtime dynamic colour on the web.

### 5.2 How theming works in gBreeze (Track B)

- `md-color-tokens.scss` emits each role once, as `--md-sys-color-<role>: light-dark(<light>, <dark>)` (or as a single value when light and dark are equal), and sets `:root { color-scheme: light dark }`. **Dark mode follows the OS by default.** Apps force a mode by setting `color-scheme: light` or `dark` on any subtree, which also handles mixed-mode regions.
- `md-color-tokens-full.scss` emits the roles as `var(--md-ref-palette-*)` references plus all palette tones. Swapping one palette (for example primary) then re-themes everything.
- Typography is emitted as `font` shorthands plus tracking and axes; shape uses short names; elevation uses real shadows; space uses an 8 px unit.

### 5.3 Contrast levels

- **Static token sets** (latest): the baseline ships *six* colour modules: light, light-MC, light-HC, dark, dark-MC, dark-HC (§3.2). In MC/HC, containers become strong tones (primary-container light-MC = tone 40, HC = tone 30), on-containers become white or black, outlines darken (outline light-HC = neutral-variant 20), and surfaces stay put. Map them to `@media (prefers-contrast: more)` (HC) and to an in-app "contrast" setting (MC).
- **Dynamic:** MCU's `contrastLevel` runs from −1 (reduced) through 0 (standard), 0.5 (medium) to 1 (high). Guarantees (MCU `concepts/contrast_for_accessibility.md`):

| level | guaranteed minimums | discretionary targets |
|---|---|---|
| Standard (0) | 4.5:1 text and icons; 3:1 *required* non-text | 7:1 high-emphasis text |
| Medium (0.5) | 4.5:1 text and icons; 3:1 *all* non-text | 7:1 text; 11:1 high-emphasis |
| High (1) | 7:1 text and icons; 4.5:1 non-text | 11:1 text; 21:1 high-emphasis |

- Tone-delta heuristics: ΔT 40 guarantees ≥ 3.0:1 and ΔT 50 guarantees ≥ 4.5:1. MCU contrast is computed as `(Y_light + 5)/(Y_dark + 5)` on CIE Y.

### 5.4 Dynamic colour with material-color-utilities (MCU 0.4.0)

- **HCT colour space:** Hue 0–360, Chroma 0 to about 120, Tone 0–100 (= L*). It is built on CAM16 plus L*, so tone differences predict contrast. A **tonal palette** is a fixed hue and chroma sampled at tones 0, 4, 6, 10, 12, 17, 20, 22, 24, 30, 40, 50, 60, 70, 80, 87, 90, 92, 94, 95, 96, 98, 99, 100 as needed.
- **Pipeline:** source colour (picked, or extracted from an image with `quantize` (Celebi = Wu + WSMeans) and ranked with `score`) → variant rules derive five key palettes (primary, secondary, tertiary, neutral, neutral-variant) plus error → `DynamicColor` role definitions pick tones per light or dark mode, apply contrast curves and tone-delta pairs, and run fidelity adjustments → `MaterialDynamicColors.<role>.getArgb(scheme)`.
- **`DynamicScheme` options:** `sourceColorHct` (or `sourceColorHcts[]`), `variant`, `isDark`, `contrastLevel`, `platform: 'phone' | 'watch'` (2025 spec only), `specVersion: '2021' | '2025' | '2026'` (default `'2021'`).
- **Spec versions:** 2025 applies only to Expressive, Vibrant, TonalSpot and Neutral; the other variants fall back to 2021. **2026 applies only to the new CMF variant**; for the four above, 2026 falls back to 2025.
- **Variants** (palette rules from `DynamicSchemePalettesDelegateImpl2021/2025`; h = source hue, c = source chroma):

| Variant | Intent | Primary | Secondary | Tertiary | Neutral / N-variant | 2025 changes |
|---|---|---|---|---|---|---|
| **TonalSpot** (Android default) | calm, low chroma | h, c 36 | h, 16 | h+60, 24 | h, 6 / 8 | primary c 32 (phone dark 26); secondary 16 |
| **Neutral** | near-greyscale | h, 12 | h, 8 | h, 16 | h, 2 / 2 | primary 8 (12 for blue hues), phone; secondary 4 (6 blue) |
| **Vibrant** | max colourfulness | h, 200 (max) | rotated hue, 24 | rotated, 32 | h, 10 / 12 | primary 74 (phone) / 56 (watch); secondary 56/36 on rotated hue |
| **Expressive** | playful, detached from source | h+240, 40 | rotated, 24 | rotated, 32 | h+15, 8 / 12 | primary on source hue, c 48 (phone light) / 36 (phone dark) / 40 (watch); secondary hue rotated by a 9-band table, c 24 (16 dark) |
| **Fidelity** | true to source | h, c | h, max(c−32, c/2) | complement (dislike-fixed) | h, c/8 / c/8+4 | — |
| **Content** | true to source, analogous tertiary | h, c | h, max(c−32, c/2) | analogous (dislike-fixed) | h, c/8 / c/8+4 | — |
| **Monochrome** | greyscale | c 0 | 0 | 0 | 0 / 0 | — |
| **Rainbow** | playful | h, 48 | h, 16 | h+60, 24 | h, 0 / 0 | — |
| **FruitSalad** | playful, source hue absent | h−50, 48 | h−50, 36 | h, 36 | h, 10 / 16 | — |
| **CMF** (new, 2026) | **two source colours** | h1, c1 | h1, c1 × 0.5 | h2, c2 (or h1, c1 × 0.75) | h1, c1 × 0.2 / c1 × 0.2 | error hue derived from both; error c ≥ 50 |

- **Fixed (non-dynamic) brand colours:** use `TonalPalette.fromHct(brand)` for custom roles. `blend.harmonize()` shifts semantic colours (success, warning) toward the primary hue, and `temperature` gives analogous and complementary colours.
- **Material Theme Builder** (Figma plugin and web tool) exports the same 49 roles plus MC/HC sets as CSS, Compose, Swift and DTCG-style JSON.

### 5.5 Recommendation for our token pipeline

Use a source-of-truth token file in DTCG JSON:

- ref palettes generated by MCU from a NEAR AI brand seed, with the variant fixed (probably **Content** or **Fidelity** to preserve brand hue, or **TonalSpot** for UI chrome) and `specVersion '2025'`
- sys roles for {light, dark} × {standard, medium, high}
- our own glass materials (§7.3)

Emit four outputs: CSS (`light-dark()` and `prefers-contrast`), Swift (SwiftUI `Color` assets with Any/Dark and Increased Contrast appearances), Kotlin (Compose `ColorScheme`), and a TS runtime that can regenerate the scheme from a user-chosen seed with MCU in the browser (the catalog recipe).

---

## 6. Accessibility features

| Area | MWC implementation | Notes for us |
|---|---|---|
| **Native semantics inside** | Buttons render a real `<button>` or `<a>`; text fields a real `<input>` or `<textarea>`; dialog a real `<dialog>` + `showModal()`; menus use the **Popover API** (`positioning="popover"`, the select's default) with `fixed` fallback. | Popover and `<dialog>` give top-layer rendering. Translucent backdrop-filter surfaces in the top layer work well. |
| **ARIA delegation** | `mixinDelegatesAria` reflects host `aria-*` and `role` (the full AOM list in `internal/aria/aria.ts`) onto the inner focusable element. `delegatesFocus: true` on shadow roots. | Needed because ARIA does not cross shadow boundaries. The class-contract approach (gBreeze) avoids the problem. |
| **ElementInternals and form association** | `static formAssociated = true`, `attachInternals()`. Value submission, `form`, `labels`, constraint validation (`checkValidity`, `reportValidity`, `setCustomValidity`, `validity`), `formResetCallback`, `formStateRestoreCallback`. `labs/behaviors` turns this into mixins: `mixinElementInternals`, `mixinFormAssociated`, `mixinConstraintValidation`, `mixinOnReportValidity`, `mixinFocusable`, `mixinFormSubmitter`, `mixinCustomStateSet` (`:state()` with a fallback). | A reusable pattern for our own controls. Safari 16.4+ is required for ElementInternals. |
| **Labels caveat** | Checkboxes and radios "are not automatically labelled by `<label>` elements and always need an `aria-label`" (b/294081528). | A known gap. Our implementation should support `<label for>` through ElementInternals `labels`. |
| **Focus visibility** | `md-focus-ring` reacts to `:focus-visible` (attached via `for`/`attach()`), so keyboard focus only. 3 px secondary ring, 2 px outer offset, an animated 8 px "pulse", inward variant for list items and tabs. Latest tokens add `md.sys.state.focus-indicator` (thickness 3, outer +2, inner −3). | Meets WCAG 2.2 focus-appearance intent (≥ 2 px, contrasting). On glass, the ring needs a contrasting halo; see §7. |
| **Disabled vs soft-disabled** | `disabled` removes the element from the tab order. `soft-disabled` keeps it focusable with `aria-disabled` (WAI-ARIA APG guidance for toolbars and menus). | Adopt: Apple's VoiceOver also benefits from discoverable disabled controls. |
| **Touch targets** | 48 px invisible touch area (`.touch`), `touch-target="wrapper|none"`. Switch touch target 48. | Apple's minimum is 44 pt. Use max(44, 48) = 48 on touch web, 44 on iOS native, and allow 28–32 px pointer targets on desktop with spacing. |
| **Keyboard models** | List/menu roving tabindex (`activateNextItem`, typeahead with a 200 ms buffer, Home/End, wrap control), sub-menu hover delays (400 ms), tabs (arrow keys, `auto-activate` optional), chip set roving focus, slider keys, dialog Esc → `cancel`, focus trap (`no-focus-trap` to opt out), select typeahead. labs/aria uses **`focusgroup`** for tablist and menulist. | — |
| **Screen readers** | Roadmap: "fully supported: VoiceOver, TalkBack, ChromeVox, JAWS, NVDA" (completed Q1 2024). Dividers are decorative unless `role="separator"`. Progress needs `aria-label`. Dialog is labelled by its headline; `type="alert"` → alertdialog. Icon buttons need `aria-label`; toggles use `aria-label-selected`. | — |
| **Forced colours** | 39 `forced-colors` media blocks: disabled colours become `GrayText`, outlines are added, ripple is hidden. | Glass must degrade to solid system colours in forced-colours mode. |
| **Reduced motion** | `prefers-reduced-motion` in the focus ring and slider (MWC); gBreeze tabs, button group, snackbar, slider. | Extend to every spring and glass refraction animation. |
| **RTL** | `flip-icon-in-rtl`, logical properties throughout (`padding-inline`, logical corner tokens start-start…). | — |
| **Colour contrast** | Role pairs designed for ≥ 3:1 (non-text) and ≥ 4.5:1 (text); MC/HC token sets; MCU contrast levels. | Glass surfaces break the guarantee, because the background behind them is unknown. See §7.3. |

---

## 7. Recommendations for the NEAR AI web implementation

### 7.1 Adopt as-is, wrap, or reimplement?

| Option | Verdict | Reasoning |
|---|---|---|
| **Adopt stable `<md-*>` elements as-is** | **No** for product surfaces. Acceptable only for internal tools where stock M3 Baseline is fine. | Maintenance mode with no new features. Pre-Expressive v0.192 tokens: corner scale lacks 20/32/48, no XS–XL sizes, old slider and progress, nav-bar 80. Missing components: nav rail, app bars, toolbars, sheets, snackbar, search, tooltips, date and time pickers, split button, button groups. Shadow-DOM-encapsulated rendering. No motion, density or spacing custom properties. Roboto default. Manual dark mode. |
| **Wrap `<md-*>` (subclass or restyle via `--md-*` and `::part`)** | **Limited.** At most for complex form plumbing (text field, select, menu) in a transitional period. | Glass styling needs `backdrop-filter`, layered gradients and specular borders on the *container* element inside the shadow root. Only `--md-<comp>-container-color` and the 2.2 `container` slot (text field and field) reach it. Corner morphs and springs cannot be added to the existing shape tokens. Every glass tweak becomes a fight with `--_` private tokens. |
| **Fork or vendor `labs/gb` (Track B)** | **Strong reference; selectively vendor.** | Same Google tokens (34.0.21) and an Expressive spec match. CSS-first class contracts ("baseline DOM") work in any framework and SSR. Cascade layers make overrides predictable. `light-dark()`, `@property` ripples, `linear()` springs, `focusgroup`, `:state()`. But: explicitly experimental, may disappear, breaking changes allowed in minors, and it depends on bleeding-edge CSS (relative colour syntax, `light-dark()`, container-query units, anchor positioning, `interpolate-size`, `@property`, `focusgroup` which is not yet shipped in all browsers). Vendor the patterns into our own package at a pinned commit (Apache-2.0, keep notices). |
| **Reimplement our own components on our own token pipeline** | **Yes (recommended).** | Lets glass, Apple-parity and M3E sizing live in one coherent API. Re-use Material's *token values*, *state model*, *a11y behaviours* and MCU, but not its runtime. |

**Concrete stack proposal**

1. **Tokens.**
   - DTCG JSON source with tiers `nai.ref.*` → `nai.sys.*` → `nai.comp.*`, mirroring M3 naming so M3 docs stay usable. Seed with the 34.0.21 values (§3).
   - Generate CSS custom properties in `@layer nai.sys.*`: `--nai-sys-color-*` using `light-dark()`, plus `[data-contrast=medium|high]` and `@media (prefers-contrast: more)` overrides.
   - Generate Swift and Kotlin from the same source.
   - Keep `--md-sys-*` aliases (`--md-sys-color-primary: var(--nai-sys-color-primary)`) so third-party M3 web components and the Material Tailwind theme can drop in.
2. **Components.** Use a CSS class contract (gBreeze-style baseline DOM on native elements) with optional thin Lit or framework wrappers. Native `<button>`, `<input>`, `<dialog>`, `popover`, `<select>` (customisable select where supported) under the hood. Form association via ElementInternals only where a custom element is unavoidable.
3. **Motion.** Express springs as `linear()` easings generated at build time from (stiffness, damping) for each of the six spring tokens × two schemes (standard, expressive), with matching durations (settle time to within 0.1 %). Example: expressive fast-spatial 800/0.6 sampled over 350 ms, exactly as gBreeze does; standard fast-spatial 1400/0.9 needs only about 200 ms. Fall back to `cubic-bezier(0.2,0,0,1)` (standard) when `linear()` is unsupported, and to opacity-only effects under `prefers-reduced-motion`. Use the Web Animations API with the same `linear()` strings for JS-driven morphs.
4. **Dynamic colour.** Bundle `@material/material-color-utilities` (Apache-2.0, tree-shakeable ES modules) only in the theming path. Run MCU at build time for brand themes, and at runtime only for user-seeded themes.
5. **Tailwind.** If the web app uses Tailwind 4, start from `labs/gb/styles/tailwind.scss`: colour roles, radius scale, shadow scale, 600/840/1200/1600 breakpoints, the `typescale-*` utility, and the `@layer theme, base, md, components, utilities` ordering. Add `nai` glass utilities.

### 7.2 What to take from Material (high value, low conflict)

- Colour **role architecture** (primary, secondary, tertiary, error, each with container / on / fixed; surface-container-lowest…highest; outline / outline-variant; inverse; scrim). Role names map well onto glass tints.
- **State-layer model** (hover 0.08, focus 0.10, pressed 0.10, dragged 0.16; disabled content 0.38, container 0.10), expressed as overlays of the on-colour. This works on glass if the overlay is drawn *above* the blur layer.
- **Focus indicator** spec (3 px, +2 / −3 offsets, secondary colour) and soft-disabled.
- **Expressive size ladder** (32 / 40 / 56 / 96 / 136) for buttons, icon buttons, split buttons and groups, plus **shape morphing** (round ↔ square on select and press) and connected button groups with 2 px gaps and inner corners. These are distinctive and pair well with glass "capsules".
- **Window-size classes** 600 / 840 / 1200 / 1600 and the navigation pattern per class: bar (compact) → collapsed rail 96 (medium) → expanded rail 220–360 or modal (expanded+).
- **Elevation shadow formulas** as the non-glass fallback for raised surfaces.
- **MCU** for seeded themes and the HCT tone math behind contrast guarantees.

### 7.3 Glass on top of M3 tokens: needed additions

M3 has no translucency or material tokens, so we must add a layer. Suggested `nai.sys.material.*` tokens:

| token | purpose | suggested web mapping |
|---|---|---|
| `glass.{thin,regular,thick,clear}.blur` | backdrop blur radius | `backdrop-filter: blur(var(--…))` (+ `saturate()`) |
| `glass.*.tint` | tint colour = an M3 surface-container role at an alpha (for example `surface-container` @ 0.55 light / 0.45 dark) | `background: hsl(from var(--nai-sys-color-surface-container) h s l / α)` (relative colour syntax, as gBreeze uses) |
| `glass.*.saturation` | vibrancy boost | `saturate(1.6–1.8)` |
| `glass.edge.highlight` / `glass.edge.shadow` | specular rim and inner shadow | `box-shadow: inset 0 1px 0 hsl(… / .5), inset 0 -1px 0 hsl(… / .1)`, plus a border gradient |
| `glass.*.elevation` | outer shadow | M3 elevation levels 1–3 at reduced opacity |
| `on-glass.*` | content colours on glass | on-surface / on-surface-variant at full strength, with a **minimum 4.5:1 checked against the tint's worst case**: a tint alpha high enough that contrast ≥ 4.5:1 against both pure black and pure white backdrops, or a dynamic scrim |
| `glass.fallback` | for `prefers-reduced-transparency`, `forced-colors`, no `backdrop-filter` support, or low-end devices | an opaque surface-container-* role |

State layers, ripples and focus rings render above the glass fill. On glass, use `secondary` focus rings with a 1 px contrasting outer halo (`outline` + `box-shadow`), because the backdrop varies.

### 7.4 Conflicts between M3 (MWC tokens) and Apple conventions (Liquid Glass / HIG)

| Topic | Material 3 / Expressive | Apple (iOS/iPadOS/macOS, Liquid Glass era) | Suggested resolution for the parent system |
|---|---|---|---|
| **Surface model** | Opaque tonal surfaces (surface-container ladder) plus shadows; tint overlays deprecated | Translucent, refractive glass for controls and navigation layers that float above content; content stays opaque | Content layer uses M3 surface roles. Floating chrome (tab bars, toolbars, sidebars, popovers, sheets) uses `nai.material.glass` tinted from M3 roles. |
| **Typeface and scale** | Roboto / Roboto Flex; body-large 16/24, label-large 14/20; explicit tracking tokens; variable axes (ROND, GRAD) for emphasis | SF Pro / SF Pro Rounded; Dynamic Type (body 17 pt / 22, callout 16, subheadline 15, footnote 13, caption 12/11; large title 34); tracking built into the font's optical sizes | Platform-native fonts per platform: SF on Apple, our brand or Roboto Flex on web and Android. Keep **role** names (display/headline/title/body/label) and map each to the nearest Apple text style. Never hard-code tracking on Apple. Map M3 "emphasized" to semibold/bold. |
| **Corner geometry** | Circular arcs; scale 0/4/8/12/16/20/28/32/48/full; shape morphing; "inner corners" in connected groups | Continuous (squircle) corners; **concentric** radii (child radius = parent radius − padding); capsules everywhere in Liquid Glass | Keep the M3 radius *values* as tokens, but render continuous corners on Apple. Add a `concentric` rule for nested glass. Use `corner-shape: squircle` on web where supported, with circular fallback. |
| **Touch target** | 48 × 48 | 44 × 44 pt | Platform-specific `nai.sys.target.min` (48 web touch / Android, 44 iOS, 28 macOS pointer). |
| **Control heights** | Button S 40, M 56; text field 56; list item 56/72; nav bar 64 (Expressive) | iOS buttons about 44–50 (Liquid Glass capsule); macOS regular controls 22–28 pt (dense); iOS tab bar about 49–56 plus floating glass; list rows 44 | Introduce a **density** axis (missing in MWC): `compact` (macOS) = M3 values × ~0.7 or Apple metrics, `standard` (web), `comfortable` (touch). Expressive XS (32) suits desktop toolbars. |
| **Navigation** | Bottom nav bar (indicator pill), nav rail, FAB, top app bar with left-aligned title, flexible large app bars | Tab bar (floating glass in iOS 26+), sidebar (iPad / macOS), toolbars; large title that collapses; **no FAB**; primary actions in toolbar or nav bar | Web follows the M3 window-size classes. Mobile web uses a glass bottom bar styled like iOS but with the M3 active-indicator semantics. Avoid the FAB on Apple platforms (use a toolbar or prominent button). Desktop uses the sidebar (≈ expanded rail 220–360). |
| **Feedback** | Ripple plus state layers (hover 8 %, press 10 %), focus pulse | Highlight / dim on press, scale and glass "lensing" response, hover lift on iPad pointer; no ripple | Drop the ripple. Keep state-layer opacity as a "highlight" overlay. Use a spring scale (0.97) on press across platforms; this fits Expressive "fast spatial" too. |
| **Motion** | Spring tokens (stiffness/damping), two schemes (standard 0.9, expressive 0.6–0.8); fixed duration and easing tokens for CSS | Springs by response/bounce (`.smooth`, `.snappy`, `.bouncy`); interruptible, velocity-preserving | Use one spring vocabulary. Store stiffness and damping and derive response/bounce for SwiftUI (table §3.7) and `linear()` for CSS. Default to the M3 **standard** scheme on desktop and web chrome, **expressive** for playful moments. |
| **Dialogs and alerts** | 28 px corner dialog, left-aligned headline, text-button actions at the bottom right | Centered alerts with stacked or side-by-side buttons; action sheets and confirmation dialogs; sheets with detents | Platform-native on Apple. On web, an M3 dialog with glass styling and Apple-like button order rules (destructive in red, cancel last on macOS / first on iOS). |
| **Menus** | Expressive menus: 16 corner, grouped segments with 2 px gaps, vibrant variant, 44 px items | Context menus and pull-down menus with glass, 6–10 pt corner on macOS, compact 22–28 pt rows | Desktop and web pointer: Apple-like density (28–32 px rows) with M3 grouping semantics. Touch: M3 44 px items. |
| **Switch** | 52 × 32 track, 16 → 24 → 28 handle, icons optional | 51 × 31 (iOS), glass-lensing knob in Liquid Glass | Nearly identical geometry. Use one metric (52 × 32) with platform styling. |
| **Slider** | Expressive: thick 16–96 px track, 4 px bar handle, stop indicators | Thin track, round glass knob | Conflict. On Apple use the native slider; on web pick per-surface (Expressive for media and volume, thin for settings). |
| **Colour** | Dynamic colour from a seed (HCT), tonal roles, MC/HC schemes | System colours (label, secondaryLabel, systemFill…), accent colour, vibrancy on materials; Increase Contrast and Reduce Transparency settings | Generate M3 roles from the NEAR AI seed and map Apple semantic colours onto them (`label` ← on-surface, `secondaryLabel` ← on-surface-variant, `separator` ← outline-variant, `tint` ← primary). Honour Increase Contrast → HC set, and Reduce Transparency → glass fallback. |
| **Dark mode** | MWC: manual; gBreeze: `light-dark()` follows OS | Automatic | Automatic everywhere with an explicit override, via the `color-scheme` property on web. |
| **Iconography** | Material Symbols (variable: FILL, wght, GRAD, opsz), fill toggles on selection | SF Symbols (weights and scales, hierarchical and palette rendering, variable values) | Use one semantic icon registry keyed by name, rendered with SF Symbols on Apple and Material Symbols (or our own set) on web and Android. Map "selected = filled" to SF `.fill` variants. |

### 7.5 Risks and open items

- **Token churn:** the latest tokens are already "34.0.21", gBreeze comments mention "GM3 v35", and Compose files mix versions (on-container tone 10 vs 30; XS button padding 16 vs 12). Snapshot the values into our own DTCG source and diff on each upgrade rather than depending on `@material/web/tokens/versions/latest`.
- **gBreeze CSS features** need modern engines. Fallbacks are required for `focusgroup` (polyfill with roving tabindex), CSS anchor positioning (tabs indicator), `light-dark()` (Safari 17.5+), relative colour syntax (recent engines only; verify against the support matrix), `interpolate-size` (Chromium only) and `corner-shape` (Chromium-only at time of writing, if used).
- **Licensing:** MWC, MCU and AndroidX are Apache-2.0. Vendored code must keep notices. Roboto and Roboto Flex are under the SIL OFL. Material Symbols are Apache-2.0.
- **What I could not access:** GitHub Discussions is not readable through the REST API without auth. I parsed the HTML of #5642 and #5805 instead, and other discussions were not reviewed. The `custom-elements.json` manifest only exists in the npm package, not the repo, and I did not download it because the docs API tables cover the same data. The m3.material.io guidance pages are out of scope for this stream.
