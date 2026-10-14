# Tooltip

A short label that appears beside a control on pointer hover or keyboard focus to name it, give its shortcut, show text that was cut off, or say why the control is unavailable.

## When to use

- Name every icon-only control on pointer platforms (`IconButton`), with its shortcut when it has one.
- Show the full value of truncated text.
- Say why a control is unavailable ("Resume watching to contribute.").
- Don't put information people need to finish a task in a tooltip; show it as text, an `InlineAlert` or an info `Popover`.
- Don't put links or buttons in a tooltip; use a `Popover`.
- Don't rely on tooltips on touch: iOS has none, and Android shows one only on long press.

## Anatomy

1. Container: `popover` fill over `blur-floating`, `radius-tile`, `shadow-float`, padding `space-4` by `space-8`. Width fits the text up to `size-popover-width` (260); dense tools allow 300 (`size-popover-width` + `space-40`).
2. Text: caption type in `text-primary`. The full label comes first; a description, when there is one, follows on the next line as a complete sentence. At most three lines and about 200 characters.
3. Shortcut (optional): `text-tertiary`, `space-6` after the label.
4. Offset: `space-8` below the target, centred (`.nr-tooltip-anchor`); above (`--above`) when the target sits in a bottom bar or near the window's bottom edge.

## Sizes by density

| | compact (macOS) | regular (web) | touch iOS | touch Android | dense |
|---|---|---|---|---|---|
| Type | `mac-caption` | `web-caption` | none; iPad pointer shows `.help` text | `android-caption` (plain tooltip) | `web-caption` |
| Max width | 260 | 260 | | 260 | 300 |
| Trigger | hover, focus | hover, focus | pointer hover on iPad | long press | hover, focus |

## Variants

- **Name**: the control's name ("Show inspector").
- **Name and shortcut**: "Show inspector ⌥⌘I" on Apple, "Show inspector Ctrl+Alt+I" elsewhere, rendered from the command registry (NDS-14).
- **Reason**: why a control is disabled, as a sentence.
- **Label and detail**: "Refresh balance", then "Last checked 2 minutes ago." on the next line.

M3 rich tooltips (title, text, actions) map to `Popover`.

## States

- Hidden, then shown after the delay; shown at once on keyboard focus.
- Increased contrast: a 1px `edge-hc` inset edge. Reduced transparency: `pane-opaque` with no blur, so text never sits on a see-through ground (Unity).

## Behavior

- Shows after 0.4 s of hover (Unity Editor). Moving straight to another control with a tooltip shows the next one at once.
- Stays while the pointer is over the target or the tooltip itself, so people can move onto it to read (WCAG 1.4.13).
- Hides when the pointer leaves, on Esc, on press, when a drag starts, and when focus moves. On Android it hides 1.5 s after the finger lifts (M3).
- One tooltip at a time; a new one replaces the old.
- It appears without movement, a fade on `duration-fast` with `ease-standard`; under Reduce Motion it appears at once.

## Accessibility

- Role `tooltip`, linked from the target with `aria-describedby`. When the tooltip repeats an icon button's `aria-label`, keep the name on the button and hide the duplicate from assistive tech.
- Esc dismisses it without moving focus.
- Disabled controls that explain themselves use `aria-disabled="true"`, not `disabled`, so they still take focus and hover.
- Text uses `text-primary` on `popover`, which holds 4.5:1 over the worst ground (7:1 in the `-hc` themes).
- The consumer supplies the text from the product's copy; a component never writes its own tooltip.

## Platforms

| | SwiftUI/AppKit (macOS) | SwiftUI/UIKit (iOS/iPadOS) | Jetpack Compose M3 | Web |
|---|---|---|---|---|
| Control | `.help(label)`: the system tooltip, system delay | `.help(label)` on iPad with a pointer; nothing on iPhone | `TooltipBox` with `PlainTooltip` | `.nr-tooltip` with `role="tooltip"`, shown by script after the delay |

## Do and don't

- Do describe the action ("Show inspector"), not the glyph ("Rectangle with line").
- Do read shortcuts from the command registry; never type them into copy.
- Do write the reason for a disabled control as a sentence that says how to make it available.
- Don't show tooltips on controls that already have a visible label.
- Don't put essential or interactive content in a tooltip.

## Source

Intentional addition. trace-commons names every icon-only control with the system `.help(label)` (`GlassRoundButton`, `GlassToolbarButton`, `GlassKebab` in `Controls.swift`) and keeps longer text in `GlassInfoButton`; it draws no tooltip of its own. Web and the Windows and Linux shells need one, so this follows Unity Editor Foundations (0.4 s delay, 300 px maximum, three lines, label then description, tooltips for unlabelled icons and disabled UI), M3 plain tooltips (placement, 1.5 s touch hide, one at a time) and WCAG 1.4.13.
