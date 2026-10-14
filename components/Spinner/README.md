# Spinner

A small ring whose quarter arc turns, for short work that has no measure, always next to words that say exactly what is happening.

## When to use

- Waits of about 200 ms to 5 s with no measure: reading a queue, checking a connection, checking proofs.
- Show nothing for waits under 200 ms.
- Use `ProgressBar` once the work can be counted or will take longer than about 5 s.
- Inside a `Button`, use the button's busy state. For lists of known shape, use `Skeleton` with a spinner line. For streamed AI text, the stream is the indicator (`Message`, `AgentRun`).

## Anatomy

1. **Track.** The full ring in `toggle-off` (the 16 to 18% ink).
2. **Arc.** A quarter of the ring in `text-secondary`, or `currentColor` in the inherit variant.
3. **Stroke.** Size ÷ 8: 1.5px at 12, 2px at 16, 4px at 32.
4. **Status words.** A separate element after the spinner, `inline-gap` (6px) away: caption or label step in `text-secondary`. The words belong to the status line, not to the spinner.

## Sizes by density

| | compact (macOS) | regular (web) | touch iOS | touch Android | dense |
|---|---|---|---|---|---|
| Inline | 12 (`space-12`) | 12 | 16 (`size-glyph`) | 16 | 12 |
| Centered in a pane | 32 (`space-32`) | 32 | 32, or the native large `ProgressView` | 48 `LoadingIndicator` | 16 |
| Words | `mac-caption` | `web-caption` | `ios-caption` | `android-caption` | `mac-caption` |

## Variants

- **Inline.** Spinner and words on one line ("Reading local queue…").
- **Standalone.** No visible words, for a value that is still being read in a settings row. It needs an accessible label.
- **Centered.** The large size with words under it, in the middle of the region that will fill (`nr-spinner-status--center`).
- **Inherit.** The arc takes `currentColor`, for use inside other components.

## States

- **Turning.** One turn per `duration-spin` (800 ms) on `ease-linear`.
- **Still.** Under Reduce Motion the arc stands still at its starting angle; the words carry the state.
- **Stalled.** When nothing has changed for a while, the words change to say why ("Still waiting for the watcher to answer."). A spinner never turns forever without new words.
- **Done.** The result replaces the spinner and its words. No checkmark flourish.

## Behavior

- Start after a 200 ms delay so quick answers never flash a spinner; once shown, keep it at least `duration-slow` (300 ms).
- One spinner per region, for the group of things loading, never one per row.
- Keep its position fixed for the same kind of wait across the product.
- People keep working while it turns. A spinner never blocks input; work that blocks belongs in a `Modal` with Cancel.

## Accessibility

- A spinner beside its words is hidden (`aria-hidden`), and the words sit in a polite live region (`role="status"`), so they are read once.
- A standalone spinner is `role="progressbar"` with an `aria-label` from the product's copy and no `aria-valuenow`. On macOS, represent it as a native indeterminate `ProgressView` named by the label.
- Words are specific: "Reading local queue…", "Checking proofs for 12 calls…". Never "Loading…" or "Thinking…".
- The consumer supplies every word; the component authors none.
- Contrast: the arc in `text-secondary` holds 3:1 as a mark; the track is decorative.
- Forced colors: the ring draws in system colors and still turns.

## Platforms

| | SwiftUI/AppKit (macOS) | SwiftUI/UIKit (iOS/iPadOS) | Jetpack Compose M3 | Web |
|---|---|---|---|---|
| Build | Custom `GlassSpinner`: `TimelineView` paused under Reduce Motion, `accessibilityRepresentation` as `ProgressView` | `ProgressView()` (native circular), tinted `text-secondary` | `CircularProgressIndicator()` inline; `LoadingIndicator()` (M3 Expressive) for pane waits of 200 ms to 5 s | `<span class="nr-spinner">` |
| Native? | Custom, to match the glass inks | Native | Native | Custom |

## Do and don't

- Do say what is being read, checked or sent, with counts when known.
- Do let the rest of the window stay usable.
- Do switch to a `ProgressBar` as soon as the work can be measured.
- Don't use a spinner for a single value; a value still loading is a dash.
- Don't label the ring itself or put text inside it.
- Don't keep a spinner for minutes without new words.

## Source

`GlassSpinner` in `Components/Feedback.swift` (12pt ring, 1.5pt stroke on an 18% ink track, a quarter arc in `textSecondary` turning once per `motion.spin` 0.8 s, still under Reduce Motion, a native indeterminate `ProgressView` to assistive tech, hidden when unlabelled unless `standalone`). trace-commons loading is a text line or a spinner and a line ("Reading local queue…"), and settings rows awaiting an answer show a standalone spinner (cross-screen pattern 12, `Views/Settings/SettingsStateRow.swift`). The 200 ms to 5 s window follows the M3 loading indicator; specific status words and "keep it moving" follow the HIG progress indicators and loading pages.
