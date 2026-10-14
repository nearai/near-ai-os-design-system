# Color

Color does four jobs here: it separates layers (scene, glass, paint), carries text, marks the one action and the current selection, and states status. It never decorates, and it never carries meaning alone.

## Neutrals

The neutrals are trace-commons' flat glass values: a navy-black dark appearance and a cool grey light one. Both lean blue, so the NEAR blue accent sits in the same family.

| Role | Light | Dark | Use |
|---|---|---|---|
| `scene` | #e6eaf1 | #070a1a | Behind windows on web; behind first run |
| `scene-warm` | #f6f7fa | #11152b | Center of the scene gradient |
| `glass-veil` | #e3e6ec at 66% | #070a1a at 68% | Over every pane's material |
| `pane-fill` | #f4f6f9 at 8% | white at 4% | Over the veil |
| `pane-base` | #f4f5f8 at 96% | #0d1124 at 96% | Panes without a material |
| `pane-opaque` | #f2f3f6 | #0d1124 | Reduce Transparency, charts, status reference |
| `card` | white at 35% | #0d1124 at 35% | Cards |
| `card-quiet` | white at 29% | #0d1124 at 28% | Quiet cards, inspector sections |
| `card-on-opaque` | #ffffff | #171c33 | Cards on an opaque ground: phone and tablet screens, Reduce Transparency, opaque content panes |
| `card-quiet-on-opaque` | #f8f9fb | #13182d | Quiet cards on an opaque ground |
| `control` | white at 44% | black at 30% | Neutral buttons, pickers, toolbar groups |
| `well` | #8a93a5 at 43% | black at 30% | Segment tracks, legend cells, unchecked boxes |
| `field` | #f4f6f9 at 60% | black at 30% | Inputs |
| `popover` / `menu` | #f7f7f9 at 84% / 80% | #0b0f22 at 82% | Floating layer |

Dark cards on glass are darker than the pane (pane navy laid over it), not lighter; light cards are whiter. On an opaque ground the glass card fill would match the pane exactly, so cards there take `card-on-opaque` and `card-quiet-on-opaque`, one tonal step lighter (1.11:1), the way Material's surface containers step. Cards and controls are told apart by fill alone; they carry no rims or borders. This is the flat theme's rule (owner, 2026-10-10).

## Text

| Role | Light | Dark | Worst-case contrast (light / dark) |
|---|---|---|---|
| `text-primary` | #1d1d1f | #f2f3f8 | 7.66 / 5.70 |
| `text-secondary` | #3c3c43 | #f2f3f8 at 88% | 4.98 / 4.84 |
| `text-tertiary` | #3d3d43 | #f2f3f8 at 84% | 4.91 / 4.58 |
| `text-placeholder` | black at 64% | white at 80% | 4.79 / 4.75 |
| `accent-text` | #024175 | #c6e1ff | 4.74 / 4.70 |

Worst case means the lowest ratio across the pane, card, quiet card, field, control, popover, menu and opaque pane, each over the worst desktop the glass can show (white under dark glass, #333333 under light glass). The secondary and tertiary inks sit close together in light because that ground is dark; hierarchy comes from type weight and size as much as from ink. Never use `neutral` or a status mark color for words.

## Accent

The parent accent is NEAR AI blue. `brand-blue` #0091fd, the "AI" of the wordmark, is 2.9:1 on a light opaque pane and 3.3:1 under white text, so the roles step it in lightness at the same hue (OKLCH 251):

| Role | Light | Dark | Rule |
|---|---|---|---|
| `accent` | #035ca3 | #7ebcff | 3:1 against every ground (3.12 / 3.17) |
| `accent-pressed` | #00488f | #6aa8eb | 8% darker |
| `text-on-accent` | #ffffff | #071a2e | 6.85 / 8.80 on `accent` |
| `accent-text` | #024175 | #c6e1ff | 4.5:1 on every ground |
| `accent-soft` | #0070c6 | #0091fd | 3:1 on `pane-opaque` |
| `accent-tint` | #0070c6 at 14% | #0091fd at 22% | Ground behind accent content |
| `focus-ring` | #035ca3 | #7ebcff | 3:1 against every ground |

The dark accent is a light blue with dark text, the way Material's dark primary works: a saturated mid blue cannot hold 3:1 against dark glass over a white desktop. Use `accent` for:
- the one primary action on a surface (`Button` primary);
- selected states: a segment, a list or table row, a navigation item, a filter chip;
- controls that are on: a switch track, a checked checkbox, a chosen radio;
- the focus ring.

Use `accent-text` for links and accent eyebrows, and `accent-soft` for non-text accent marks: step-progress nodes, the tab ember, a lone series. Do not use accent for headings, icons that are not selected, borders, or decoration. Brand expression belongs to content and marks (Logo, hero type, illustration), not to every control.

## Status

Status never follows the product theme. Each status has a mark color (dots, glyphs; 3:1 on `pane-opaque`), a text color (4.5:1 on every ground and on its own tint) and a tint.

| Status | Means | Mark (L / D) | Text (L / D) | Tint |
|---|---|---|---|---|
| `positive` | On, watching, automatic, verified, contributed | #1a8f4c / #30d158 | #0b4628 / #acedbc | 14% / 18% |
| `caution` | Ask me, pending, worth a second look | #a8690f / #ffc75c | #573403 / #ffd585 | 14% / 18% |
| `critical` | Failed, leaves for an outside model, no proof | #d0342c / #ff6b6b | #771814 / #ffd3d3 | 12% / 18% |
| `neutral` | Off, never, not used | #8a8a90 / #a9a9b0 | (never text) | black 6% / white 10% |

- Show status as a dot plus words (`StatusLabel`), a tag (`Tag`, tint ground with text ink) or a notice title with a dot (`Notice`). Never as a fill on a card, and never by color alone.
- `destructive-text` (#791313 / #ffd0d0) labels destructive buttons and menu items; it is not a status.
- `badge-fill` with `text-on-status` is the one badge: decisions owed. Light #e04a42 with a dark count (4.86:1), dark #ff6b6b (7.04:1).
- Green and red differ in lightness as well as hue, and every status carries words, so the set is safe for color-vision deficiency.

## Data

Charts plot on `surface-chart` (light #f7f8fa, dark #0d1124), never directly on glass, and use `data-1` to `data-8` in this order, never cycled:

| Slot | Light | Dark |
|---|---|---|
| `data-1` | #2a78d6 | #0091fd |
| `data-2` | #cf5320 | #d95926 |
| `data-3` | #14906a | #199e70 |
| `data-4` | #a97200 | #c98500 |
| `data-5` | #c94a7c | #d55181 |
| `data-6` | #2f8a1f | #008300 |
| `data-7` | #5a48b8 | #9085e9 |
| `data-8` | #d33c3c | #e66767 |

Both sets pass the six palette checks: OKLCH lightness band, chroma floor, adjacent-pair separation under protanopia and deuteranopia (worst ΔE 9.2 light, 8.4 dark), the normal-vision floor (worst ΔE 17.2 light, 19.3 dark) and 3:1 against `surface-chart`. Scatter plots, maps and small multiples can tell apart only the first three slots; fold anything beyond into "Other" or facet. Gridlines are `chart-grid`; labels and values are text roles, never the series color. Status colors are reserved for series that mean good or bad (an error rate), and then they carry an icon and a label. Trace replaces the first three slots with its own series: shared, kept and inference.

## Increased contrast

The `-hc` themes deepen the veil to 90%, raise card, field and control fills, and solve every text role to 7:1 on every ground. Every painted surface gains a 1px `edge-hc` edge and hairlines rise to 40-45%, so surfaces read apart by edges, not by shade. The accent darkens to #01599f in light; in dark the accent already clears 7:1 under its dark text. The light badge becomes deep red #b01218 with a white count (7:1).

## The Trace theme

`trace-light` and `trace-dark` are trace-commons' flat themes, unchanged. Dark selection and the primary action are the brand purple #6d14f3 with white text (6.9:1); light uses the blue #15608a, adopted on 2026-10-12 because purple read muddy on the cool grey. Accent text is #e1d5ff in dark and #0c3f5c in light. Three Trace values miss the parent floors and stay exact, flagged in their token notes, until the Trace team fixes them:

| Theme | Pair | Ratio | Floor |
|---|---|---|---|
| `trace-dark` | `accent` (selected fill #6d14f3) on the pane over a white desktop | 1.09:1 | 3:1 |
| `trace-dark` | `toolbar-glyph-off` #83838c on a control | 2.63:1 | 3:1 |
| `trace-light` | `toolbar-glyph-off` #8a8a90 on a control | 2.27:1 | 3:1 |

The parent `light` and `dark` themes solve the toolbar glyph to #75757b and #8d8d97.

## Mapping to platform color systems

| Parent role | Material 3 role | Apple semantic |
|---|---|---|
| `accent` | primary | tint / accent color |
| `text-on-accent` | onPrimary | white or label on tint |
| `accent-tint` | primaryContainer (as a translucent ground) | tinted fill |
| `text-primary` | onSurface | label |
| `text-secondary` | onSurfaceVariant | secondaryLabel |
| `text-tertiary` | onSurfaceVariant (reduced) | tertiaryLabel |
| `pane-opaque`, `pane-base` | surface, surfaceContainer | systemBackground, secondarySystemBackground |
| `card`, `card-quiet` | surfaceContainerLow, surfaceContainerLowest (translucent) | secondarySystemFill, tertiarySystemFill |
| `hairline` | outlineVariant | separator |
| `critical` / `critical-text` | error / onErrorContainer | systemRed (stepped) |
| `positive`, `caution` | (custom: M3 has no success or warning role) | systemGreen, systemOrange (stepped) |

Apple's default system colors are tuned for opaque backgrounds and mostly miss 4.5:1 as text on light glass; use the parent text roles, not raw system colors, for words. Material's dynamic (wallpaper) color is opt-in on Android for personal surfaces only; NEAR products use the static scheme so the accent stays theirs.
