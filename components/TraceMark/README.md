# TraceMark

The Trace product mark: a live trace across a three-by-three lattice, for Trace surfaces only.

## When to use
Use it to identify Trace inside NEAR AI surfaces: the edge-rail app tile, the about window, onboarding, the product switcher, the Trace section of a NEAR AI site. The NEAR AI `Logo` stays the master brand; the Trace mark never replaces it outside Trace.

## Anatomy
1. Visited nodes and the necked joins between them, filled with the live gradient (`trace-live-start`, `trace-live-mid`, `trace-live-end`, from point 68,68 to 134,134 of a 200-unit box).
2. The current step: the last visited node, with a soft `trace-live-end` glow (radius 30, 55% at 0.3 falling to 0).
3. Unvisited nodes (the possible next steps) in `trace-purple`.
Node radius is 10 units in the 200-unit box.

## Sizes by density
| Context | Size | File |
|---|---|---|
| Edge-rail app tile (compact) | 30px in a 44px tile | ink |
| Menu-bar and toolbar glyph | 16 to 20px | ink |
| About window, onboarding (compact, regular) | 64 to 96px | live |
| Product switcher (touch) | 28px in a 44pt target | ink, live from 30px |

## Variants
- `live`: the gradient mark, dark grounds only, 30px and up.
- `ink`: one ink at full strength; white on dark grounds, black on light (`trace-mark-ink-white`, `trace-mark-ink-black`).

## States
None. When it links (the edge-rail tile), the tile owns hover, selection (`accent` with `text-on-accent` glyph) and focus.

## Behavior
Static. The live trace may draw in once on first run as a hero moment (one per product, `spring-expressive`), and holds still under Reduce Motion.

## Accessibility
Decorative next to the word "Trace" (`alt=""`, `accessibilityHidden`). Alone in a control, the control's label carries the name ("Open Trace").

## Platforms
| macOS (SwiftUI/AppKit) | iOS/iPadOS | Android (Compose) | Web |
|---|---|---|---|
| `GlassTraceMark()` and `GlassTraceMark(ink:)` drawn in a `Canvas` | The same view, or the SVG in an asset catalog | Vector drawable from `trace-mark-live.svg` / `-ink-*.svg` | `<img>` of the uploaded asset |

## Do and don't
- Do use the ink mark below 30px and on light grounds.
- Don't put the gradient mark on a light ground or inside a colored button.
- Don't recolor the gradient with a product accent or the NEAR AI blue.
- Don't redraw or simplify the lattice.

## Source
`GlassTraceMark` in `macos/Sources/TCDesign/Logos/GlassTraceMark.swift` ("1c Live trace", owner 2026-10-12), transcribed point for point into the uploaded SVGs. The Turn (`assets/mark/`) is the Trace packaging mark; see the Trace asset group.
