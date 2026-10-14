# Sheet

A surface that rises over part of the screen for a scoped task tied to what is behind it: a bottom sheet with detents on phones and tablets, and a side sheet at the trailing edge of wide web windows.

## When to use

- Use a bottom sheet on phones and tablets for a short task in context: run settings, choosing a model, sharing a trace.
- Use the medium detent when people should still see what is behind the sheet; use the large detent for a task that needs the screen.
- Use a side sheet on web windows at `bp-expanded` and wider for details or filters that sit beside the content.
- On macOS, use `Modal` (the app's replacement for the system sheet) or an inspector pane.
- Don't use a sheet for a long multi-step flow (use a full-screen view), for a critical confirmation (use `Modal` or the system alert), or on top of another sheet.

## Anatomy

1. Layer: `scrim` behind a modal sheet, at `z-scrim`. A standard (nonmodal) sheet has none and the content behind stays usable.
2. Container: `pane-base` with `pane-fill`, `shadow-modal`. Bottom sheets round their top corners with `radius-sheet` (28), span the width up to `size-readable-width`, and pad `space-16` at the sides and bottom; parts sit `space-12` apart.
3. Grabber: a button `space-32` × 2 wide (64) and `target-touch-android` (48) tall, with a `space-32` × `space-4` mark in `neutral`, `radius-pill`.
4. Header: Cancel leading and Done trailing, with the title and optional subtitle centred between them (iOS, HIG 2026). On Android the title is start-aligned (`__header--start`) and actions sit in the footer.
5. Body: scrolls on its own once taller than the detent.
6. Footer (optional): an `ActionBar`.

Side sheet: `size-panel-width` (380) wide, inset `pane-gap` from the window edges, all corners `radius-pane`, a start-aligned header with a close button that is always present, an `ActionBar` at the bottom.

## Sizes by density

| | compact (macOS) | regular (web) | touch iOS | touch Android | dense |
|---|---|---|---|---|---|
| Form | use `Modal` | side sheet, 380 | bottom sheet, detents | bottom sheet; side sheet from 600 | use an inspector |
| Header actions | | 30 small CTA or 26 close | 44 round glass | 48 targets | |
| Title type | | `web-title` | `ios-body-strong` | `android-title` | |

## Variants

| Detent | Height | Use |
|---|---|---|
| Peek | the header and grabber | a standard sheet that waits (a player, a run in progress) |
| Medium | about half the screen; M3 caps a modal sheet's first height at 50% | progressive disclosure, the default |
| Large | full height; on iOS the glass turns opaque and meets the screen edges | tasks that need the screen |

- **Modal** sheets block the content behind; **standard** sheets leave it usable.
- **Side** (`--side`): a detached trailing sheet on wide windows; it mirrors to the leading edge in right-to-left layouts.

## States

- Dragging follows the finger with no easing; release settles to the nearest detent on `spring-spatial` (`duration-spring-spatial`, 317 ms).
- Unsaved changes: swiping down or tapping the scrim asks first ("Discard changes?").
- Busy: like `Modal`, the scrim, swipe and Cancel are inert until the work answers.
- Increased contrast: a 1px `edge-hc` inset edge on the container.

## Behavior

- A bottom sheet rises from the bottom edge on `spring-spatial`; a side sheet slides in from the trailing edge. Leaving uses `ease-exit` on web and Android. Under Reduce Motion the sheet appears and leaves without moving.
- The grabber resizes by drag, and a tap or Space or Return cycles the detents. Swipe down, the scrim, Cancel, Esc (web) and system Back (Android, with predictive back) close a modal sheet.
- One sheet at a time. Back steps through a multi-step sheet; it never closes it.
- A modal sheet traps focus like `Modal` and returns it to the opener; a standard sheet does not trap focus.

## Accessibility

- A modal sheet is a `dialog` with `aria-modal="true"`, labelled by its title.
- The grabber is a button named by the product ("Resize sheet") whose value is the current detent ("Half height"). It gives a single-pointer alternative to dragging (WCAG 2.5.7).
- Every sheet has a visible way to close it: Cancel, a close button, or Done.
- The grabber mark uses `neutral`, which holds 3:1 on `pane-opaque`. Header actions meet 44pt (Apple) and 48dp (Android).
- The consumer supplies the title, subtitle, action names and the grabber's name and values.

## Platforms

| | SwiftUI/AppKit (macOS) | SwiftUI/UIKit (iOS/iPadOS) | Jetpack Compose M3 | Web |
|---|---|---|---|---|
| Bottom | not used: `GlassModal` | `.sheet` with `.presentationDetents([.medium, .large])` and `.presentationDragIndicator(.visible)`; keep the system glass background | `ModalBottomSheet` with its drag handle, or `BottomSheetScaffold` for a standard sheet | `.nr-sheet` in `.nr-sheet-layer` |
| Side | inspector pane | `.inspector` on iPad | custom `Surface` (M3 Compose has no side sheet) | `.nr-sheet--side` in `.nr-sheet-layer--side` |

## Do and don't

- Do keep the first height at half the screen or less so the top actions stay in reach.
- Do pair Done with Cancel or Back, never all three (HIG).
- Do keep content supplementary to what is behind the sheet.
- Don't put a modal bottom sheet on a desktop window; use a side sheet, `Menu` or `Modal`.
- Don't inset a side sheet more than `pane-gap`.

## Source

Intentional addition. trace-commons' `GlassSheet` in `Surfaces.swift` is a padded column inside a pane or modal, not a presentation, and the macOS app presents scoped tasks as `GlassModal`. Phones, tablets and the web need edge-anchored sheets, so this follows HIG Sheets (detents, grabber, the 2026 Cancel and Done placement), Liquid Glass sheets (inset partial sheets that turn opaque at full height), M3 bottom and side sheets (a 32 × 4 handle in a 48 band, 28 top corners, 50% first height, 400 side maximum) and Unity App UI's Tray (bottom, left or right, with a drag handle).
