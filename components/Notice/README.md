# Notice

A quiet card that tells people about the state of a whole section or window, with its tone carried by the title's dot, an optional fix and an acknowledge link; use it when a state needs a sentence and possibly an action.

## When to use

- Health banners: the watcher stopped, a source is down, sign-in is needed, a grant expired.
- A section that failed to load, with Retry.
- A one-time explanation people must see before they act (a folder's rule changed).
- Pick the tier by scope:

| Scope | Component | Unity Foundations tier |
|---|---|---|
| One control or one request | `InlineAlert` | Help box |
| A section, pane or window | `Notice` | Help box (section) |
| The result of an action you can undo | `Toast` | Window banner |
| A decision that cannot be undone, or consent | `Modal` confirmation | Dialog |
| A record of operations | Activity log in `AgentRun` | Console |
| Anything while the app is in the background | System notification | |

## Anatomy

1. **Card.** `card-quiet`, `radius-card-quiet`, padding `space-10` x `space-12`. The card is never tinted by the tone.
2. **Title.** A strong `StatusLabel`: the tone's dot and a full sentence in `text-secondary`, label step, semibold. The title states the problem.
3. **Body.** Label step at regular weight in `text-secondary`. Cause, then the fix, in one to three sentences (about 200 characters). An optional short list.
4. **Actions** (optional). One `Button` (glass; primary only when the notice is the surface's one action), then an acknowledge link (Dismiss, Not now). `space-8` apart, `space-4` more above them.
5. **InlineAlert** (optional). A failed fix's line, under the actions.

Parts stack with `space-6`. In a **stack**, notices sit `card-gap` apart, most severe first, with a Dismiss all link at the head once two or more can be acknowledged. Cap the stack's height (the Mac app uses 320pt) and let it scroll.

## Sizes by density

| | compact (macOS) | regular (web) | touch iOS | touch Android | dense |
|---|---|---|---|---|---|
| Padding | 10 x 12 | 10 x 12 | 12 x 16 | 12 x 16 | 8 x 10 |
| Radius | `radius-card-quiet` | `radius-card-quiet` | `radius-card-quiet` | `radius-card-quiet` | `radius-control` |
| Title, body | `mac-label` | `web-label` | `ios-label` | `android-label` | `mac-caption` |
| Buttons | 28 inline | 28 inline | 44 | 40 in a 48 target | 20 |
| Width | The pane's column | Up to `size-readable-width` | Full width minus `margin-compact` | Full width minus `margin-compact` | The panel's column |

## Variants

| Tone | Dot | Use | Example title |
|---|---|---|---|
| Caution | `caution` | Something needs a look | The watcher isn't running. |
| Critical | `critical` | Something failed or was refused | History couldn't be read. |
| Neutral | `neutral` | Off, paused, informational | Watching is paused until 9:00. |
| Positive | `positive` | A recovery worth saying, sparingly | Proofs are back for every call. |

- **Health banner.** No actions. It goes away when the condition clears.
- **Dismissible.** Has an acknowledge link.
- **Gate.** No dismiss: the work behind it cannot continue until the person acts (sign in, choose Ask first).

## States

- **Shown.** Appears in place and pushes the content below it down. No motion.
- **Acting.** The fix's `Button` shows its busy state ("Restarting…"); the notice stays.
- **Fix failed.** An `InlineAlert` under the actions with the new reason.
- **Resolved.** The notice disappears when the product reports the condition gone. Never on a timer.
- **Increased contrast.** The card gets the 1px `edge-hc` inset edge.

## Behavior

- Never auto-dismiss. A notice leaves when its condition clears or the person acknowledges it.
- Keep each notice to one condition. Merge repeats ("3 folders need a look") instead of stacking copies.
- Keyboard: the notice is a region in reading order; Tab reaches its actions. Escape does nothing because a notice is not a popup. After Dismiss, focus moves to the next notice, or to the section heading when none remain.
- Never present a notice as an alert at launch. Show the held data with the notice above it.

## Accessibility

- Mark it up as a region named by its title (`<section aria-labelledby>`). When it appears while the person is on the page, announce it once in a polite live region; use `role="alert"` only for a gate that stops the work in front of them.
- The title's words carry the tone ("isn't running", "couldn't be read"). The dot is supplementary and hidden from assistive tech.
- The consumer supplies the title, body and action words from the product's copy.
- Contrast: `text-secondary` on `card-quiet` holds 4.5:1 over the worst ground behind glass (7:1 in the `-hc` themes).
- Action targets follow the density's floor.

## Platforms

| | SwiftUI/AppKit (macOS) | SwiftUI/UIKit (iOS/iPadOS) | Jetpack Compose M3 | Web |
|---|---|---|---|---|
| Build | Custom `GlassNotice`: quiet `GlassCard`, `GlassStatusLabel` title, content in text colors | Custom card at the top of the scroll view or as a `List` section | Custom `Card` with a dot `Row` title (M3 has no banner) | `<section class="nr-notice">` |
| Announce | `AccessibilityNotification.Announcement` | `UIAccessibility.post(.announcement)` | `liveRegion = LiveRegionMode.Polite` | `role="status"` region |
| Native? | No | No; never `.alert` for status | No | No |

## Do and don't

- Do write the title as the problem in a sentence, then the cause, then what to do (Problem, cause, solution).
- Do state what happened to the person's data ("nothing was sent", "sessions stay on this Mac").
- Do offer the fix in place when the product can do it.
- Don't prefix "Error" or "Warning"; the dot already says it.
- Don't tint the card, color the body or add a colored left border.
- Don't use a modal for a status that needs no decision.

## Source

`GlassNotice` in `Components/Containers.swift` (the title carries the tone as a status dot, the body stays in text colors, and "Tone never tints the card"); the shell notice stack in `Views/ShellNotices.swift` (320pt scroll, Dismiss all at two or more, gates without dismiss); notice, health banner and inline alert in the trace-commons cross-screen patterns 8, 10 and 12. The scope tiers and the Problem, cause, solution formula come from Unity Foundations' errors and messaging; alerts only for decisions, never at launch, from the HIG alerts and feedback pages.
