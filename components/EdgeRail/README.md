# EdgeRail

The edge rail is an optional macOS surface on the screen's right edge: hovering a thin zone opens a column of section tiles with a peek of each section's state, and anything beyond a glance opens the app.

## When to use

- A glance at the product's state from any app or Space without switching windows (Home status, Private AI totals, Traces folders), on macOS only.
- Off by default; the person turns it on in Settings > General.
- Not for decisions, consent or anything that sends data. Its one write is Pause or Resume watching. Everything else opens the app at that section.
- Not on iOS, iPadOS, Android, web or Windows/Linux, which have no screen-edge surfaces; use widgets, Live Activities, notifications or a tray menu there.

## Anatomy

1. **Hover zone** `.nr-edge-rail__zone`, closed: 4 by 240 (`space-4` by 5 × `space-48`) on the screen's right edge, centered vertically.
2. **Handle** `.nr-edge-rail__handle`: 3 by 72 (`space-2` + 1 by `space-64` + `space-8`), a `neutral` pill at the edge.
3. **Panel** `.nr-edge-rail`, open: the peek, 16 apart (`space-16`), then the rail, 12 from the screen edge (`space-12`); at most 680 tall; 484 wide with 20 of room for the peek's shadow.
4. **Rail** `.nr-edge-rail__rail` on a `.nr-pane`: 56 wide (44 + 2 × 6), 6 padding, 2 between tiles.
5. **Tile** `.nr-edge-rail__tile`: 44 square (`size-control-touch`), radius `radius-card-quiet` (concentric: the pane's 20 minus its 6 padding), glyph 20, or a product mark at 30 (44 − `space-14`).
6. **Rule** `.nr-edge-rail__rule`: 28 by 1 (`size-control-large`) of `rule` between the section tiles and the tile that opens the app.
7. **Peek** `.nr-edge-rail__peek` on a `.nr-pane`: 380 wide (`size-panel-width`), 12 padding, 10 between parts: a heading, the glance (cards, rows, a small graph), then an "Open Traces →" link (`accent-text`) beside the product's nothing-sent sentence.

## Sizes by density

| | compact (macOS) | regular, touch, dense |
|---|---|---|
| Zone | 4 × 240 | not used |
| Handle | 3 × 72 | |
| Rail | 56 wide, 44 tiles | |
| Peek | 380 wide, `mac-heading` title, `mac-body` and `mac-caption` content | |
| Panel | at most 680 tall | |

## Variants

- **Closed**: the zone and the handle only.
- **Open**: the rail and the peek of the hovered or selected tile (Home, Private AI, Traces).
- **Fixed** (`--fixed`): pins the panel to the viewport's right edge, for documentation pages that show it live.

## States

| State | Treatment |
|---|---|
| Tile default | no fill, glyph `text-primary` |
| Tile hover | `control-hover`; the tile's peek shows |
| Tile pressed | `filter: brightness(0.92)` |
| Tile selected (`aria-current="true"`) | `selection` fill, glyph `text-on-accent` |
| Selected, pressed | `accent-pressed` |
| Focus | 2px `focus-ring`, 2px outside (NDS-5) |
| Peek values | unknown values show a dash; a value never reads "on" until the product confirms it |

## Behavior

- **Pointer**: entering the zone opens the rail. Leaving the panel starts a 300 ms grace (`duration-slow`) before it closes. Hovering a tile switches the peek; clicking a tile opens the app at that section.
- **Keyboard**: the handle exposes an Open action to assistive tech. When open, Tab moves through tiles and the peek; Escape closes. The panel never takes focus from the app the person is using.
- **Motion**: the panel slides in on `duration-slide` with `ease-standard`. Under Reduce Motion it fades only.
- **Writes**: Pause and Resume watching only, applied at once and reversible.

## Accessibility

- Tiles are buttons with names and tooltips from the product ("Traces"); the selected tile has `aria-current`.
- The peek is a region labelled by its heading.
- Tile glyphs are icon-only controls: `text-primary` and `text-on-accent` hold 3:1 on their grounds. The handle uses `neutral`, 3:1 on `pane-opaque`; the desktop behind it varies.
- Tiles are 44 square, well above the 28 pointer target.
- **The product supplies**: the sections, their glyphs and names, each peek's content and the Open link's words.

## Platforms

| SwiftUI/AppKit (macOS) | SwiftUI/UIKit (iOS/iPadOS) | Jetpack Compose M3 | Web |
|---|---|---|---|
| A borderless, non-activating `NSPanel` at the status-bar level that joins all Spaces, hosting SwiftUI (`GlassRailTile`, `GlassRailHandle`, `GlassRailRule`) | Not available: widgets and Live Activities | Not available: widgets and notifications | Not available; Windows/Linux shells use a tray menu |

## Do and don't

- Do keep it off by default and keep each peek to facts that fit at a glance.
- Do open the app for anything that needs a decision.
- Don't put Contribute, consent or any send in the peek.
- Don't animate or pulse the handle to draw attention.
- Don't add tiles beyond the product's top-level sections (three in Trace) and the one tile that opens the app.

## Source

`EdgeRailGeometry`, `GlassRailTile`, `GlassRailHandle` and `GlassRailRule` in `macos/Sources/TCDesign/Components/EdgeRail.swift` (`size.edgeRail*` and `space.edgeRail*` tokens: zone 4 × 240, handle 3 × 72, rail 56, tile 44, rule 28, peek 380, open height 680, gap 16, inset 12); behavior in `Views/EdgeRail/EdgeRailController.swift` and `EdgeRailView.swift` (300 ms grace, slide, opacity only under Reduce Motion; #1381). Tile radius: tokens.json lists edge-rail tiles under `radius-control`, but the source uses the quiet-card radius and the concentric rule gives 14, so this spec uses `radius-card-quiet`.
