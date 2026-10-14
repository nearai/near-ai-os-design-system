# PromptComposer

The field where a person writes to an agent: multi-line text, context chips, attachments, a model picker and one Send action that becomes Stop while the agent answers.

## When to use

- At the foot of every agent thread and side panel, and as the inline reply under a `ToolCall` that asks a question.
- Use `TextArea` for plain multi-line form input and `SearchField` for search. A composer always sends to an agent.

## Anatomy

1. **Starters** (empty thread only): up to four product-curated pills on `control`, label type. Choosing one fills the field; it does not send.
2. **Box**: `field` fill, `radius-card`, padding 10 top, 8 trailing, 8 bottom, 14 leading. Keyboard focus in the text draws the ring on the box (2px `focus-ring`, offset 2).
3. **Context chips**: scope chips ("@near-agents") on `accent-tint` with `accent-text`; attachment chips on `neutral-tint` with `text-secondary`, a 10 file glyph and a mono name. Max width `size-popover-width`, then truncate. Each has a 16 remove button.
4. **Text**: transparent, `text-primary`, placeholder `text-placeholder`. Grows from one line to eight (`calc(1lh * 8)`, derived), then scrolls.
5. **Bar**: Attach (round, `--nr-h-control`, `text-secondary` glyph), the model picker (quiet pill, mono model name, 10 chevron), and a trailing group with the optional counter and Send. The chip row and bar sit 4 and 6 outside the text inset so glyphs line up with the text (derived).
6. **Send**: round, `--nr-h-control`, `accent` fill with a `text-on-accent` arrow. The one accent action on the surface. While the agent answers, the same slot is **Stop** (square glyph).
7. **Route note** (caption, `text-tertiary`, inset 14 to align with the text): where the message goes and what goes with it. An outside model turns it into a `critical` dot and `critical-text` words.
8. **Reason line** (caption, `text-secondary`, `caution` dot): why Send can't act, with one action link.

## Sizes by density

| | compact (macOS) | regular (web) | touch iOS | touch Android | dense |
|---|---|---|---|---|---|
| Text | `mac-body` 13 | `web-body` 14 | `ios-body` 17 | `android-body` 16 | `mac-label` 12 |
| Chips, starters | `mac-label` | `web-label` | `ios-label` | `android-label` | `mac-caption` |
| Model | `mac-mono` 11 | `web-mono` 12 | `ios-mono` 13 | `android-mono` 12 | `mac-mono` 11 |
| Send, Attach | 28 | 28 | 44 | 44, target 48 | 20 |
| Box radius | `radius-card` 16 | 16 | 16 | 16 | `radius-control` 11 |

## Variants

- **Thread composer**: starters, chips, picker, route note.
- **Inline reply**: no starters; the route note shows only when it differs from the thread's.
- **Edit mode**: replaces a user `Message`; Cancel leading, Save and resend trailing (NDS-19).
- **Side panel**: the picker collapses to its glyph with the model as its name and tooltip.

## States

| State | Send slot | Lines under the box |
|---|---|---|
| Empty | Send, `aria-disabled` (the empty field is its own reason) | starters above |
| Ready | Send; Return sends | route note |
| Generating | Stop (`aria-keyshortcuts="Escape Meta+Period"`); the field stays editable; Return does not send | route note |
| Blocked | Send, `aria-disabled`, still focusable | reason line + action |
| Near the limit | Send; counter "3,812 / 4,000" from 90%; at the limit the counter turns `critical-text` and Send is blocked | reason line |
| Outside model | Send | note in `critical-text` with a `critical` dot |
| Uploading | Send waits; the chip shows the product's progress words | route note |

Controls: hover `control-hover`, pressed `brightness(0.92)` (Send: `accent-pressed`), disabled `opacity-disabled`. Under `-hc` themes the box, chips, pills and Send take the 1px `edge-hc` edge. In forced colors the box draws a 1px CanvasText border.

## Behavior

- **Keys**: Return sends; Shift+Return adds a line; Mod+Return sends from anywhere. While an IME is composing, Return confirms the candidate and never sends. On touch keyboards Return adds a line and only Send sends. Esc closes the mention list first, then stops the answer; Mod+. stops (NDS-14).
- **Mentions**: typing @ opens a `Menu` on the floating layer listing folders, agents and files; Return or Tab inserts a chip. Backspace at the start of the field selects the last chip, a second Backspace removes it.
- **Paste and drop**: pasted text over the product's threshold becomes a chip ("Pasted text · 212 lines"); pasted or dropped files become chips. While a drop is over the box it fills with `accent-tint`.
- **Model picker**: a `Menu` of models, each with its `ProofTag`. Choosing an outside model is a consent step: the menu says what leaves and asks once, then the note stays while that model is chosen.
- **Focus**: stays in the field after Send and while the answer streams. Output never takes it.
- **Draft**: survives errors, sign-out and model changes. Up arrow in an empty field may reopen the last user turn for editing.
- **Motion**: fills change on `duration-fast` `ease-standard`; the field grows without animation.

## Accessibility

- The text area is named by the consumer ("Message near-agents") and described by the route note and reason line.
- Chips form a list; each remove button names its object ("Remove @near-agents").
- The mention list uses the combobox pattern: `aria-autocomplete="list"`, `aria-expanded`, `aria-activedescendant`.
- Send and Stop are one button whose name changes; announce "Stopped" politely.
- Blocked Send uses `aria-disabled`, so it stays in the tab order and reads its reason.
- Placeholder `text-placeholder` holds 4.5:1 on `field`. In `trace-dark` the purple `accent` fill is 1.09:1 against the pane (flagged in the contrast report); the white glyph and the name carry Send there, never the fill.
- Send, Attach, the picker and chip remove buttons reach `--nr-target` through invisible hit areas.
- The consumer supplies every word: placeholder, starters, chip labels, model names, the note, the reason and its action.

## Platforms

| | SwiftUI/AppKit (macOS) | SwiftUI/UIKit (iOS/iPadOS) | Jetpack Compose M3 | Web |
|---|---|---|---|---|
| Field | `TextField(axis: .vertical)`, `.lineLimit(1...8)` in the field well; `.onKeyPress(.return)` sends unless Shift | same in a bottom `safeAreaInset`; Return adds a line | `TextField(maxLines = 8)` with `imePadding()` | `textarea` with `field-sizing: content`; check `isComposing` |
| Chips | custom capsules | custom capsules | `InputChip` | buttons in a `role="list"` |
| Model | `Menu` (as `GlassPicker`) | `Menu` | `ExposedDropdownMenuBox` | menu button |
| Attach | `.fileImporter`, `.dropDestination` | `PhotosPicker`, `.fileImporter` | `rememberLauncherForActivityResult` | `input type="file"` + drag and drop |

Custom composite on every platform.

## Do and don't

- Do keep Send the only accent on the surface, and put Stop in the same place.
- Do say where the message goes and what goes with it, in words, under the box.
- Do keep the draft through every failure.
- Don't disable Send without a visible reason beside it. A tooltip alone is not enough.
- Don't send on Return during IME composition or from a touch keyboard.
- Don't send a starter on tap; let the person edit it first.
- Don't write "secure", "encrypted" or "private" in the note. Say a tool "sends its calls here" and this computer "answers" them.

## Source

Intentional addition: trace-commons has no composer. The well, placeholder token and focus treatment come from `GlassTextField` (Controls.swift) and `GlassTextArea` (Forms.swift), chips from `GlassChip` (Indicators.swift), Send from `GlassButtonStyle(.primary)`, and the route note from the Private AI banned-words rule (sends its calls here, answers). Anatomy and states follow Unity App UI `ThreadComposer` (max length with a counter, attachments, drop zone, paste handling, sending state, edit mode with Cancel and Save, mentions through `IMentionProvider` and `MentionPicker`). HIG Generative AI asks for curated starters and for saying what leaves the device; HIG keyboards map Esc and Cmd-. to cancel and forbid moving focus.
