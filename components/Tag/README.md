# Tag

A small tinted pill holding a one- or two-word verdict about an item (Verified, Pending, External, Contributed); use it for an outcome that is settled, beside the item it describes.

## When to use

- Proof results on model calls, contribution outcomes in history, review states, draft markers.
- At the trailing end of a `ListRow`, a `DataTable` cell or a card head.
- Use `StatusLabel` for a live state that changes while you watch (Watching, Paused). Use `Chip` for anything a person can press, filter or remove. Use `ProofTag` when the verdict opens its proof.
- A tag is never interactive.

## Anatomy

1. **Container.** A capsule (`radius-pill`), height `size-control-dense` (20px), horizontal padding `space-8`, filled with the tone's `-tint` ground.
2. **Words.** The micro step in the tone's `-text` ink. Sentence case, one or two words.
3. **Outline** (failed only). 1px in the words' ink, inside the capsule; 2px under the `-hc` themes.

No dot, no icon. The words carry the verdict; the tint supports them.

## Sizes by density

| | compact (macOS) | regular (web) | touch iOS | touch Android | dense |
|---|---|---|---|---|---|
| Height | 20 | 20 | 20 | 20 | 20 |
| Padding | 0 x 8 | 0 x 8 | 0 x 8 | 0 x 8 | 0 x 8 |
| Words | `mac-micro` | `web-micro` | `ios-micro` | `android-micro` | `mac-micro` |
| Radius | `radius-pill` | `radius-pill` | `radius-pill` | `radius-pill` | `radius-pill` |

Tags are not targets, so touch floors do not apply. On touch, keep the row they sit in at its own target height.

## Variants

| Tone | Ground | Ink | Examples |
|---|---|---|---|
| Neutral | `neutral-tint` | `text-secondary` | Taken back, Not offered, No proof, Not recorded |
| Positive | `positive-tint` | `positive-text` | Verified, Contributed |
| Caution | `caution-tint` | `caution-text` | Pending, Under review, Gateway only |
| Critical | `critical-tint` | `critical-text` | External (left for an outside model) |
| Failed | `critical-tint` + 1px outline | `critical-text` | Check failed |
| Accent | `accent-tint` | `accent-text` | Drafts, New |

- **Failed** is a check that ran and did not pass. The outline keeps it apart from critical (a fact about routing or proof) and means it never relies on color alone.
- **Accent** marks product emphasis (a draft, a new item). It never carries status.

## States

- **Static.** No hover, pressed, focus or disabled state.
- **Unknown.** Draw no tag. A missing verdict is a dash in its column, never a positive tag and never "Pending" invented by the client.
- **Increased contrast.** Every tag except failed gets the 1px `edge-hc` inset edge; failed's outline grows to 2px.
- **Forced colors.** A 1px `CanvasText` border; words in system text color.

## Behavior

- A tag changes only when the product reports a new verdict; it swaps at once, with no motion.
- Never truncate a tag. Keep the words short (about 16 characters at most) and let the row wrap.
- At most two tags on one row. A third verdict belongs in the item's detail view.
- When a verdict needs explaining (why a proof failed), put an info `IconButton` or the row's detail behind it. The tag itself takes no focus.

## Accessibility

- The words are read as part of the row: "qwen3-32b, Check failed". Order the row so the item's name comes first.
- The consumer supplies the words from the product's copy. The component authors none.
- Contrast: each `-text` ink holds 4.5:1 on its `-tint` and on the worst ground behind glass (7:1 in the `-hc` themes). `text-secondary` on `neutral-tint` holds the same floor.
- Do not rely on the tint to separate verdicts in a list; the words must differ.

## Platforms

| | SwiftUI/AppKit (macOS) | SwiftUI/UIKit (iOS/iPadOS) | Jetpack Compose M3 | Web |
|---|---|---|---|---|
| Build | Custom `GlassTag`: `Text` on a filled `Capsule`, `strokeBorder` for failed | The same custom view | Custom `Surface(shape = CircleShape, color = tint)` with `Text`; not `AssistChip`, which is interactive | `<span class="nr-tag nr-tag--positive">` |
| Type | `mac-micro` | `ios-micro` | `android-micro` | `web-micro` |
| Native control? | No | No | No | No |

## Do and don't

- Do use the past or settled form: "Contributed", "Verified", "Taken back".
- Do keep one vocabulary per product so the same outcome always reads the same.
- Don't use uppercase or eyebrow tracking in a tag.
- Don't put a dot or a glyph inside a tag.
- Don't make a tag a button or a filter.
- Don't use critical for emphasis; reserve it for failures and data that leaves the device.

## Source

`GlassTag` in `Components/Indicators.swift` (tones neutral, on, ask, outside, failed, accent; micro type on a tint with text-safe ink; failed is outlined so it never matches the outside pill and never relies on color alone). Proof tags in `Views/Monitor/InferenceViews.swift` map verified to on, pending and gateway-only to ask, failed to failed, outside to outside, and no proof, unavailable and not recorded to neutral. The parent renames on, ask and outside to positive, caution and critical.
