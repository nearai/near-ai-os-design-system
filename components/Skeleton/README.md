# Skeleton

Faint rounded bars that hold the shape of a list or a result while it loads, breathing slowly, always next to a status line that says what is loading.

## When to use

- First load of a list or result whose shape is known: history rows, search results, a list of agent runs, model cards.
- Waits longer than about 200 ms.
- Never for a single value: a value still loading is a dash ("—"), never a bar and never zero.
- Never for a status (no dot until the product answers), and never for streamed text, where the first tokens are the placeholder.
- Never over data already on screen. A reload keeps the held rows and shows a `Spinner` line instead.

## Anatomy

1. **Line.** `neutral-tint`, 12px tall (`space-12`), `radius-control` (a capsule at this height). Widths vary between about 55% and 90% so the block reads as text.
2. **Heading line.** 16px tall (`space-16`).
3. **Tile or circle.** `size-tool-tile` (22px) square at `radius-tile`, or round, for a row's leading tile or avatar.
4. **Row.** A block as tall as the density's row (`--nr-h-row`).
5. **Group.** Lines and tiles stack `space-8` apart, laid out like the content that will replace them.
6. **Status line** (outside the skeleton). A `Spinner` with words ("Reading history…").

## Sizes by density

| | compact (macOS) | regular (web) | touch iOS | touch Android | dense |
|---|---|---|---|---|---|
| Line | 12 | 12 | 12 | 12 | 12 |
| Tile | `size-tool-tile` (22) | 22 | The row's own leading tile | The row's own leading tile | `size-glyph` (16) |
| Row | 40 (`size-list-row`) | 40 | 44 | 48 | 20 |
| Gap | `space-8` | `space-8` | `space-8` | `space-8` | `space-2` |

## Variants

- **Line, heading, tile, circle, row.** Building blocks.
- **Group.** The placeholder for one row or one result card.

## States

- **Breathing.** Opacity eases from 1 to `opacity-skeleton` (0.5) and back over `duration-pulse` (1.6 s) on `ease-standard`.
- **Still.** Under Reduce Motion the bars hold at full opacity.
- **Replaced.** Real rows replace skeleton rows as they arrive, one by one, at the same size, so nothing jumps.
- **Failed.** The skeleton goes. A `Notice` (critical) with Try again takes its place, or the held data stays with the notice above it.
- **Increased contrast.** Bars get the 1px `edge-hc` inset edge.

## Behavior

- Show it after 200 ms. Show about as many rows as will arrive, or three when unknown.
- No shimmer or sweeping highlight. The slow breath is the only motion.
- Keep the layout of the skeleton identical to the loaded content: same paddings, tiles and row heights.
- A skeleton never takes focus and never accepts input.

## Accessibility

- Hide every skeleton from assistive tech (`aria-hidden="true"`) and set `aria-busy="true"` on the region while it loads.
- Say what is loading in the status line, in a polite live region ("Reading history…"), and announce nothing per row.
- The consumer supplies the status words from the product's copy.
- Skeleton bars are decorative and carry no contrast requirement; the status line meets the text floor.

## Platforms

| | SwiftUI/AppKit (macOS) | SwiftUI/UIKit (iOS/iPadOS) | Jetpack Compose M3 | Web |
|---|---|---|---|---|
| Build | Custom `GlassSkeleton` (rounded bar, pulse on the token curve, hidden from accessibility) | `.redacted(reason: .placeholder)` on the real row views (native), with the pulse removed under Reduce Motion | Custom `Box` with `neutral-tint` and an `InfiniteTransition` alpha; no shimmer | `.nr-skeleton` blocks inside `.nr-skeleton-group` |
| Native? | No | Native redaction | No | No |

## Do and don't

- Do mirror the real layout so the swap is quiet.
- Do pair the skeleton with words that say what is loading.
- Do keep held data on reload.
- Don't use a skeleton for numbers, statuses or a single line of text.
- Don't add a shimmer, gradient sweep or color.
- Don't keep a skeleton up when the read failed.

## Source

`GlassSkeleton` in `Components/Feedback.swift` (an 8% ink bar at the control radius, 12pt tall, breathing to `opacity.skeletonDim` 0.5 over `motion.pulse` 1.6 s on the one curve, still under Reduce Motion, hidden from assistive tech). The Mac app never uses it: loading there is a text line or a spinner and a line, and values load as a dash (trace-commons cross-screen pattern 12). The parent keeps it for lists on web and touch, where the HIG loading page asks for placeholders and, for AI products, skeletons for history and results. Line widths follow Unity App UI's list item loading state (title 90%, subtitle 65%).
