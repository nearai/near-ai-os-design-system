# Switch

A track and knob that turns a setting on or off the moment it is pressed, for features and settings that need no Save, such as Private AI or the edge rail.

## When to use

- Use it for a standalone setting that takes effect at once.
- On iOS, switches belong in list rows. Outside lists, use a toggle-style button.
- On macOS, use a switch for a setting that turns a feature on or controls a group. Ordinary settings use a `Checkbox`.
- Use a `Checkbox` for options applied on submit and whenever the value can be mixed; a switch is never mixed. Use a `SegmentedControl` or `RadioGroup` for opposing choices. A switch is never a call to action.

## Anatomy

1. **Track**: 40 x 24 (`size-toggle-width`, `size-toggle-height`), `radius-pill`. Off: `toggle-off`. On: `accent`.
2. **Knob**: 18 (`size-toggle-height` − `space-6`), inset 3 (`space-6` / 2), round, no ring. On: `text-on-accent`. Off: the theme's light ink, which is `text-on-accent` in the light and Trace themes and `text-primary` in dark and dark-hc, where `text-on-accent` is navy.
3. **Label**: leading, the label step at regular weight, `text-primary`, `space-12` before the track.
4. **Sub-line** (optional): caption, `text-tertiary`, saying what changes when it is on.

In a settings row the words lead and wrap and the switch sits on the trailing edge, so a column of switches lines up.

## Sizes by density

| | Compact (macOS) | Regular (web) | Touch iOS | Touch Android | Dense |
|---|---|---|---|---|---|
| Track | 40 x 24 | 40 x 24 | system `Toggle` | 52 x 32 (M3) | use `Checkbox` |
| Target | 28 | 28 | 44 (row) | 48 (row) | none |
| Row height | 40 `size-list-row` | 40 | 44 | 48 | none |
| Label | `mac-label` regular | `web-label` regular | `ios-body` | `android-body` | none |

## Variants

- **Inline**: the label, then the switch.
- **Row** (`.nr-switch--row`): settings rows, switch trailing.
- **Label hidden**: the switch alone in a row that already names it; the label stays as its accessible name.

## States

| State | Look | Tokens |
|---|---|---|
| Off | Gray track, knob leading | `toggle-off` |
| On | Accent track, knob trailing | `accent`, `text-on-accent` |
| Pressed | Off darkens; on takes the pressed accent | brightness 0.92, `accent-pressed` |
| Focus | 2px ring round the track | `focus-ring` |
| Disabled | Track and title dimmed; the sub-line that says why stays readable | `opacity-disabled` |
| Unconfirmed | Until the system confirms the state, the row shows the product's word or a `Spinner` with words, never "on" | none |
| Increased contrast | 1px edge on the off track | `edge-hc` |

## Behavior

- A click or tap on the row toggles it; Space toggles; on touch the knob can be dragged.
- It acts at once. A change with consequences offers Undo in a `Toast`. When turning on takes time, keep the knob where the person put it, show progress in words, and put it back with an `InlineAlert` if it fails.
- Motion: the knob slides on `spring-spatial-fast` (`duration-spring-spatial-fast`, 224ms); the track color changes on `duration-fast`. Under Reduce Motion the knob moves without travel.

## Accessibility

- `<input type="checkbox" role="switch">` on the web; a native `Toggle` representation on Apple platforms; `Modifier.toggleable(role = Role.Switch)` on the row in Compose.
- The label names it; the platform speaks on and off. Never write On or Off inside the track.
- State is the knob's position plus the track color. The `accent` track holds 3:1 on the pane in every theme except Trace dark (1.09:1, flagged), where the white knob on purple carries the state.
- The consumer supplies the label and sub-line. When the visible label is ambiguous, the consumer extends the accessible name ("Private AI for tools on this Mac").

## Platforms

| SwiftUI/AppKit (macOS) | SwiftUI/UIKit (iOS/iPadOS) | Jetpack Compose M3 | Web |
|---|---|---|---|
| `Toggle` with `GlassToggleStyle(.standard)` or `(.settings)` for trailing settings rows | Native `Toggle` tinted with `accent`, in list rows | `Switch` with `checkedTrackColor = accent`, `uncheckedTrackColor = toggle-off`, thumb colors as above | `<label class="nr-switch">` (type class here) with `.nr-switch__text` and `<input class="nr-switch__track" role="switch">` |

## Do and don't

- Do describe what turns on, in the label and sub-line.
- Do line switches up on the trailing edge in settings.
- Don't use a switch for a choice between two named things.
- Don't show a switch as on before the system confirms it.

## Source

`GlassToggleStyle` in Controls.swift: a 40 x 24 track, an 18pt knob inset 3, every switch on the accent (owner, 2026-10-08), Settings switches on the trailing edge with the label wrapping on the left (2026-10-09), and a native `Toggle` for assistive tech. The source's 38 x 22 watch switch folds into the one size. The knob is plain white in the source; the parent darkens it on the dark theme's light-blue track. Platform rules follow HIG toggles and M3 switch.
