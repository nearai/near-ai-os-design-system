# Glass and materials

Glass is a role, not an effect. It marks the layer people navigate with: panes, bars, sidebars, toolbars, menus and popovers. Content inside that layer is painted. The baseline is trace-commons' flat glass: a frosted material, a veil that keeps text legible over any desktop, a flat fill, no rims, and one soft shadow on anything that floats.

## The layers

| Order | Layer | Fill | Edge and shadow | Radius |
|---|---|---|---|---|
| 0 | Scene | The desktop (native); `.nr-scene` gradient of `scene`, `scene-warm`, `scene-glow-1` to `-3` (web) | none | none |
| 1 | Pane: navigation layer | Native material or `blur-pane`, then `glass-veil`, then `pane-fill`; `inactive-dim` when the window is not key | `shadow-float` | `radius-pane` 20 |
| 2 | Card, quiet card | `card`, `card-quiet` (painted, never blurred) | none | `radius-card` 16, `radius-card-quiet` 14 |
| 2- | Well, field | `well`, `field` (recessed) | none | capsule, `radius-control` 11 |
| 3 | Control | `control`; selected `accent` | none | capsule |
| 4 | Floating: popover, menu, node card, tooltip, floating toolbar | `popover` or `menu` over `blur-floating` | `shadow-float` | `radius-card` 16, menus `radius-card-quiet` 14 |
| 5 | Modal | `pane-base` + `pane-fill` over `scrim-modal` and `blur-scrim` | `shadow-modal` | `radius-pane` 20 |

Rules:
- **Never glass on glass.** Anything drawn on a pane is painted. A control floating over content (map tabs, a zoom toolbar) takes the floating layer, not a second pane.
- **Group neighbors.** Glass shapes that sit close together render as one group (`GlassEffectContainer` on Apple, trace-commons' `GlassFloatingGroup`, one shared backdrop element on web) so they sample the same backdrop and can merge. The parent sets the group's merge spacing to `space-12`.
- **Remove glass by clearing it.** Animate a glass surface in and out with scale and opacity of its content; never fade the blur radius.
- **Never use glass for content.** Cards, list rows, table cells, chart grounds, documents, chat messages and code blocks are painted. Never use glass as a modal scrim, behind status text or as decoration.

## Flat and Classic

Flat is the baseline (decision NDS-2): flat fills, no specular rims, bigger radii (pane 20, card 16, quiet card 14, control 11), cards that are pane-navy in dark and white in light, and one soft shadow for floating things only. The checkbox keeps a 1px inset ring (`shadow-check`), the one rim flat glass draws.

Classic is the optional expressive treatment from trace-commons' first glass theme: a 160° gradient pane fill, gradient card and control fills, a 1pt top highlight and bottom shade on every painted tier (`edge-classic-pane`, `edge-classic-control`), and a glow under the primary button (`edge-classic-cta`). Use it only where a product wants one heightened moment (a promotion card, a launch screen); keep tools and dense surfaces flat. Classic radii are smaller (16, 14, 12, 8).

## Per platform

| Platform | Navigation layer | Floating layer | Fallback |
|---|---|---|---|
| macOS 26+ (lead) | `NSGlassEffectView` style `.regular`, tinted with 25% of the veil's alpha, then `glass-veil` and `pane-fill` painted over it | Painted `popover`/`menu` over an `NSVisualEffectView` `.hudWindow` blending within the window | `pane-opaque` |
| macOS 14-25 | `NSVisualEffectView` `.hudWindow` behind the window, veil and fill painted over | Same as 26 | `pane-opaque` |
| iOS / iPadOS 26+ | System tab bars, toolbars and sheets keep their own Liquid Glass. Panes the app draws follow the macOS recipe (`.glassEffect(.regular)` + painted veil and fill) | System menus and popovers; app popovers painted over a blur | `pane-base` / `pane-opaque` |
| Android 12+ (API 31) | Floating bars and rails: `RenderEffect` blur (`blur-bar`) under `glass-veil`; screens are opaque `pane-base` | `popover` over `blur-floating` | Below API 31, when the system disables cross-window blur, or in power saving: `pane-base` |
| Web | `backdrop-filter: var(--blur-pane)` (with the `-webkit-` prefix) under `glass-veil` and `pane-fill` | `.nr-floating`: `blur-floating` | No `backdrop-filter` support: `pane-base`; `prefers-reduced-transparency`, `forced-colors`, Save-Data or a slow device: `pane-opaque` |
| Windows (Tauri shell) | Mica for the window and sidebar (the large, opaque glass); our veil and fill painted inside | Acrylic for menus, flyouts and tooltips | `pane-opaque` with the High Contrast system brushes |
| Linux (Tauri, GTK) | Opaque `pane-base`; blur only where the compositor provides it | Opaque `popover` | `pane-opaque` |

On Apple platforms the parent keeps Trace's painted glass over the native material (decision NDS-7) rather than system-only glass. Two consequences follow, both accepted: painted surfaces do not follow the person's Clear-to-Tinted glass setting, and on macOS 27 the system draws its own darker edge and brighter highlight on glass, so the Classic painted edges must not be used on surfaces that also take system glass. Flat panes paint no edge and avoid the doubling.

Never use Apple's clear glass variant for panes. trace-commons tried it and rejected it (owner, 2026-10-09) because it showed the desktop unblurred behind a focused window. Clear glass is for controls over media only, with a 35% black dimming layer under bright content.

## Phones and tablets

A phone or tablet screen has no desktop behind it, so the screen itself is an opaque pane (`pane-base`, or `pane-opaque` under Reduce Transparency; `.nr-opaque` on the web). Cards on it take `card-on-opaque` and `card-quiet-on-opaque`; the glass card fills would match the opaque ground and vanish. The same swap happens wherever a pane turns opaque: Reduce Transparency, no backdrop support, an opaque content pane. Only the chrome floats in glass: the tab bar or navigation bar, the top bar once content scrolls under it, floating toolbars, sheets' chrome, menus and popovers. Bars take a scroll-edge treatment instead of a painted background: on Apple, the system scroll edge effect (soft under floating bars, hard under dense text bars, one per pane); on Android and web, `blur-bar` with the veil appears only once content passes under the bar.

## Legibility on glass

- Text always sits on a ground built from the veil up; never put text straight on a backdrop blur without `glass-veil`.
- Every text role holds 4.5:1 over the worst desktop (see Color). If a product's surface fails, raise the veil's alpha; never lower the floor.
- Small glass flips between light and dark with the content behind it on Apple; large glass gets more opaque but does not flip. Supply light and dark values for every role even in a single-appearance product.
- Tint glass only for the one primary action; tint the background, not the glyph. One prominent item per bar, one or two per view.

## Accessibility settings

| Setting | What changes |
|---|---|
| Reduce Transparency / `prefers-reduced-transparency` | Every pane and floating surface becomes `pane-opaque`; blur is removed |
| Increase Contrast / `prefers-contrast: more` | The `-hc` themes: veil 90%, fills raised, text 7:1, a 1px `edge-hc` on every painted surface |
| Forced colors (Windows High Contrast) | Surfaces become `Canvas` with a 1px `CanvasText` border; accent and status use system colors |
| Reduce Motion | No morphing, no elastic response, blur never animates; surfaces appear in place |
| Clear / Tinted glass (Apple, 26.1+; a continuous setting on 27) | System glass follows it; painted panes keep the parent veil (NDS-7) |

## Performance

- At most four backdrop-filtered surfaces visible at once on the web, and one large one (a sidebar or a pane).
- Never put `backdrop-filter` on scrolling content items.
- Never animate blur radius; animate opacity and transform only.
- Keep compositor cost under 2ms a frame on mid-range hardware; drop to `pane-opaque` on devices with four cores or fewer, with Save-Data, or when frame time degrades.
- Lensing (SVG displacement in `backdrop-filter`) renders only in Chromium; Firefox accepts the syntax and draws nothing. Never depend on it; frosted blur is the baseline everywhere.

## Window-tier values for shells without a native material

| Token | Value | Use |
|---|---|---|
| `blur-pane` | blur(30px) saturate(180%) | Panes |
| `blur-floating` | blur(24px) saturate(170%) | Popovers, menus, node cards |
| `blur-bar` | blur(20px) saturate(160%) | Floating bars over scrolling content |
| `blur-scrim` | blur(8px) | Window content behind a modal |
| `radius-window` | 22 | A window the app draws itself (web, Windows, Linux) |
| `scene-glow-1` to `-3` | #3f6a8a, #6a3f7a, #2f6b5a (dark); #c4d7f2, #dcd3ee, #cde6dc (light) | Radial glows in the web scene |

`blur-pane`, `blur-floating`, `blur-scrim`, `radius-window` and the dark glows are the original web shell's window-tier values (#1146), restored because the web, Windows, Linux and Android shells have no native material to supply them. `blur-bar` and the light glows are new parent values.
