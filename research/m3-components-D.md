# M3 / M3 Expressive component digest — Group D (selection, input, pickers, indicators)

Scope: checkbox, radio button, switch, sliders, text fields, date pickers, time pickers, progress indicators, loading indicator.
Sources: m3.material.io pages (content API snapshot, page "Updated" dates noted per component) = **[m3 page]**; resolved token tables (dsdb 38.2.9) = **[tokens]**; material-components-android docs = **[mdc-android]**. "n/s" = not stated in any source. Colour roles are M3 system roles (`md.sys.color.*`); hex values omitted because they vary by scheme. Status/availability tables on the m3 pages are unresolved placeholders in the corpus, so per-platform availability is n/s unless stated.

---

## Cross-cutting findings

- **Expressive split.** Only sliders (May 2025), progress indicators (Aug 2024) and the new loading indicator (May 2025) carry an "M3 Expressive update" section [m3 page]. The Expressive launch post lists 14 new or updated components. That list includes Loading indicator (**new**), Progress indicators and Sliders. It does not include checkbox, radio, switch, text fields, date pickers or time pickers [m3 page: building-with-m3-expressive]. Those six components are baseline M3 and have only "Differences from M2" or "What's new" notes, mostly about colour and dynamic colour.
- **Shared selection-control geometry.** Checkbox, radio and switch all use a 40dp circular state layer and a 48dp target. State-layer opacities are hover 0.08, focus 0.10 and pressed 0.10 [tokens `md.sys.state.*`]. The foundations page adds drag +16% [m3 page: interaction states]. Disabled content uses 0.38 opacity and disabled tracks/containers use 0.12 (text-field container 0.04). The focus indicator is the `secondary` colour, 3dp thick, with a 2dp outer offset [tokens].
- **Inverted press ripple on checkbox and radio.** When an *unselected* control is pressed, its state layer uses `primary`. When a *selected* control is pressed, it uses `on-surface`. Hover and focus follow the current selection colour [tokens]. The switch does not invert: selected uses `primary` and unselected uses `on-surface`.
- **"Avoid applying density by default."** This wording repeats on checkbox, radio, switch and text fields. Density lowers targets below 48×48 CSS px, so offer it as a user choice, and keep the control that reverts it ≥48×48 [m3 page]. Date pickers say density harms accessibility. Time pickers say not to densify the dial and to switch to the input variant instead.
- **Slider size system (Expressive).** Five sizes with track thickness XS 16 / S 24 / M 40 / L 56 / XL 96dp and track corners 8/8/12/16/28dp. The handle is a 4dp vertical bar that narrows to 2dp on press, drag and focus. There is a 6dp gap between handle and track, 2dp inner corners, and 4dp stop dots. The inset icon is for M/L/XL standard sliders only. Vertical orientation is new. "Continuous" was renamed **standard**, and "discrete" became the **stops** configuration. Sizes S–XL ship as presets only on MDC-Android; other platforms swap tokens [m3 page].
- **Wavy progress plus configurable thickness (Expressive, Aug 2024).**
  - Default thickness is 4dp; 8dp is a "thick" sample value.
  - Linear wave: amplitude 3dp, wavelength 40dp (determinate) or 20dp (indeterminate). Container height becomes 10dp (14dp when thick).
  - Circular wave: amplitude 1.6dp, wavelength 15dp. Size becomes 48dp (flat is 40dp; thick is 52dp).
  - Older linear/circular token sets are "[Deprecated]" and "no longer recommended" [m3 page, tokens].
- **Choosing between "nothing", loading indicator and progress indicator.** The rule on both pages: under 200ms show no indicator; 200ms–5s use a **loading indicator**; over 5s use a **progress indicator** [m3 page]. The loading indicator is "recommended as a replacement for indeterminate circular progress indicators". It must never transition into a determinate progress indicator. If progress may become known, start with an indeterminate *progress* indicator instead.
- **Loading indicator.** A morph sequence through seven M3 shapes. The container is 48dp and the active shape 38dp. It can scale from 24 to 240dp. In the "contained" variant the container is `primary-container` and the shape `on-primary-container`. It is used for pull-to-refresh (Jetpack Compose only), and in that case the container is required [m3 page, tokens].
- **3:1 non-text-contrast "end stop" pattern.** Sliders and linear determinate progress both put a 4dp stop indicator at the track end. It may be removed only if the track itself has ≥3:1 contrast with the surrounding surfaces. Icons outside the slider can serve the same purpose. When an indicator sits inside a button, use the label/icon colour and remove the track [m3 page].
- **Pickers are dialogs on compact windows and docked/dropdown on medium+.** Containers use `surface-container-high` at elevation level 3 (6dp) with 28dp corners; the docked date picker uses 16dp corners. Pickers "don't scale responsively". Time pickers swap orientation or variant rather than scroll [m3 page, tokens].
- **Source discrepancies to resolve in your own system.**
  1. Switch selected-icon colour: [tokens] say `primary`; [m3 page] caption and [mdc-android] say `on-primary-container`.
  2. Slider M handle height: [m3 page] table says 52dp; [tokens] say 44dp.
  3. Slider inactive track: [tokens] `secondary-container`; [mdc-android] default `colorSurfaceContainerHighest`.
  4. Progress track: [tokens] `secondary-container`; [mdc-android] `colorPrimaryContainer`.
  5. Date range fill: [tokens] `secondary-container`; [mdc-android] `colorSurfaceVariant`.
  6. Outlined text-field focused outline: [tokens] 3dp; [mdc-android] 2dp.
  7. The checkbox keyboard table is copy-pasted from chips.
  8. The 24h time dial has two contradictory ring descriptions.
  9. [mdc-android] labels the loading indicator's "Default" as contained, which is the reverse of [m3 page].

---

## 1. Checkbox

**Status** — Baseline M3 with no Expressive update (page updated 2026-08-12) [m3 page]. Differences from M2: "New color mappings and compatibility with dynamic color", and "New indeterminate states as well as error states for unselected, selected, and indeterminate". [mdc-android] does not support shape theming ("only rounded square checkboxes").

**Purpose & when to use**
- Select one or more options from a list. Present sub-selections (parent/child). Turn an item on or off in a desktop environment. Visually group similar options [m3 page].
- Use checkboxes instead of switches when several related options can be selected. They imply the items are related and take less space [m3 page].
- Use radio buttons for single choice, and switches for standalone or verbose settings [m3 page].
- Selected items should be more prominent than unselected ones. Labels should be scannable.

**Variants / configurations** — One component with three values: unselected, selected and indeterminate. Each can also be shown in an error state. Interaction states: enabled, disabled, hovered, focused, pressed [m3 page]. There are no size variants.

**Anatomy** — 1. Container. 2. Icon (check or dash) [m3 page]. The colour diagram adds the state layer. The adjacent text label is a separate element.

**Measurements** [m3 page; tokens]

| Attribute | Value |
|---|---|
| Container size | 18×18dp |
| Container corner | 2dp |
| Icon size | 18dp, centred |
| Unselected outline width | 2dp (selected: 0dp) |
| State layer | 40dp, circular (`corner.full`) |
| Target | 48dp ([mdc-android] min size = `?attr/minTouchTargetSize`) |
| Focus indicator | 3dp thick, 2dp outer offset |

- Padding between control and label: n/s. [mdc-android] centres the icon when there is no text (`centerIfNoTextEnabled = true`).

**Typography** — The adjacent label is `on-surface` [m3 page]. Type role: n/s on m3; [mdc-android] uses Body Medium.

**Colour roles** [tokens]

| Element | Unselected | Selected / indeterminate | Error | Disabled |
|---|---|---|---|---|
| Container fill | none | `primary` | `error` (selected) | `on-surface` @0.38 (selected) |
| Outline (2dp) | `on-surface-variant`; `on-surface` on hover, focus, press | none | `error` (unselected) | `on-surface` @0.38 |
| Icon | — | `on-primary` | `on-error` | `surface` (on the 0.38 container) |
| Hover/focus state layer | `on-surface` | `primary` | `error` | none |
| Pressed state layer | `primary` | `on-surface` | `error` | none |
| Label | `on-surface`, unchanged by state or interaction [m3 page] | | | |

- Token oddity: `disabled.selected.icon.color = primary @0.38` sits alongside `selected.disabled.icon.color = surface`. Treat the "selected.disabled" set as authoritative.

**States** — Opacities: hover 0.08, focus 0.10, pressed 0.10. Error uses the same opacities in `error` colour [tokens]. Disabled controls take no hover, focus or press [m3 page: states].

**Behaviour & motion**
- Several checkboxes in a list can be selected [m3 page].
- Parent/child rules:
  - Checking the parent checks all children; unchecking it unchecks all.
  - If some (not all) children are checked, the parent becomes indeterminate.
  - Checking an indeterminate parent checks all children.
- If the checkbox turns something on or off, the action executes immediately [m3 page].
- Check-mark animation timing: n/s.
- [mdc-android] exposes `checkedState` (checked, unchecked, indeterminate), `errorShown`, and `errorAccessibilityLabel` (custom error announcement).

**Adaptive**
- Expanded windows: put checkboxes in a contained region such as a side sheet to group filters and controls [m3 page].
- Pointer input: when selection is the primary activity, checkboxes are always visible. When it is secondary, a checkbox appears on hover, or for all items once one is selected [m3 page: interaction/selection].

**Accessibility**
- Users can select either the label or the box. The screen reader reads the label, then the role. The a11y label is usually the adjacent text [m3 page].
- Keyboard: the published table is copied from chips ("Tab moves focus to chip…", "Backspace/Delete removes input chip"). The intended behaviour is Tab to focus and Space/Enter to toggle.
- Density: don't apply by default (48×48).
- Contrast: the outline uses `on-surface-variant`. A 3:1 non-text figure is not stated specifically for checkbox.

**Do / don't** [m3 page]
- Do use a parent checkbox for select-all/none.
- Don't use a list of switches for multi-select; use checkboxes.
- Do let the label toggle the control.
- Don't apply density by default.

---

## 2. Radio button

**Status** — Baseline M3 (page updated 2026-07-17). "What's new: Color: New color mappings and compatibility with dynamic color" [m3 page]. No Expressive update.

**Purpose & when to use** [m3 page]
- The recommended way to make a single selection from a list, while exposing all the options.
- Use when there are **five or fewer** options. When space matters, consider a drop-down menu, accepting that menus add clicks and cognitive effort.
- Don't nest radio buttons. Don't use them for multi-select (use checkboxes).
- Take effect immediately, unless the radio group is inside a dialog or page that needs saving.

**Variants** — None. Values: selected, unselected. States: enabled, hover, focus, pressed, disabled.

**Anatomy** — Guidelines: 1. Selected icon; 2. Adjacent label text; 3. Unselected icon. Specs: 1. Radio button icon [m3 page].

**Measurements** [m3 page; tokens]

| Attribute | Value |
|---|---|
| Icon size | 20dp |
| State layer | 40dp |
| Target | 48dp |
| Ring stroke / inner dot diameter | n/s |

**Typography** — Label colour `on-surface` [m3 page]; type role Body Medium [mdc-android].

**Colour roles** [tokens]

| Element | Unselected | Selected | Disabled |
|---|---|---|---|
| Icon | `on-surface-variant`; `on-surface` on hover, focus, press | `primary` in all states | `on-surface` @0.38 (both) |
| Hover/focus state layer | `on-surface` | `primary` | none |
| Pressed state layer | `primary` | `on-surface` | none |

- The caption lists only two roles: `primary` and `on-surface-variant`.
- No error state is defined.

**States** — 0.08 / 0.10 / 0.10; disabled 0.38 [tokens].

**Behaviour**
- Tapping the icon *or* the label selects. Selecting one deselects the others [m3 page].
- Once something is selected, the group can't be deselected. Offer a "Not applicable" or "No option" choice, or a separate "Clear selection".
- Pre-selection: the Guidelines tab says "should always have one option pre-selected". The Accessibility tab says a group "can start with one radio button selected, or none". Treat pre-selection as the default and "none" as allowed.
- Animation: n/s.

**Placement / adaptive** — Stack vertically. Avoid horizontal radio lists (marked "caution") [m3 page]. Window-class guidance: n/s.

**Accessibility** [m3 page]

| Key | Action |
|---|---|
| Tab | Into the group, onto the selected radio (or the first if none) |
| Shift+Tab | Onto the selected radio (or the last if none) |
| Arrows | Move focus **and select** previous/next; wraps from last to first |
| Space | Selects the focused radio; does nothing if already selected |

- The group role is **Radio group**, labelled by the group title. Each radio's label is its adjacent text.
- Density: avoid by default.

**Do / don't** [m3 page]
- Do always pair each radio with an inline label.
- Don't nest radios.
- Don't allow multiple selections.
- Prefer a drop-down for long lists or when space is tight.

---

## 3. Switch

**Status** — Baseline M3 (page updated 2026-07-17). Differences from M2 [m3 page]:
- More accessible visual presentation.
- New colour mappings meet non-text-contrast requirements.
- Optional icon in the handle.
- "Track is taller and wider".
- The handle was formerly called the "thumb".

[mdc-android]: `SwitchMaterial` is documented as "Switch (deprecated)"; use `MaterialSwitch`. No Expressive update.

**Purpose & when to use** [m3 page]
- Adjust settings and standalone options with a binary on/off (or true/false). Effects start immediately, with no save step.
- Don't use for opposing options such as List vs Map view; use a connected button group.
- Don't use to select multiple items that need saving; use checkboxes.
- A switch can't replace a call-to-action button.
- Use radio buttons when only one item from a list can be selected.

**Configurations** [m3 page]
1. No icons.
2. Icon on the selected switch only.
3. Icons on both selected and unselected switches.

**Anatomy** — 1. Track. 2. Handle. 3. Icon (optional) [m3 page].

**Measurements** [m3 page; tokens]

| Element | Attribute | Value |
|---|---|---|
| Track | W × H | 52 × 32dp |
| Track | Outline width | 2dp (unselected only) |
| Track | Shape | `corner.full` |
| Handle | Unselected, no icon | 16dp |
| Handle | Unselected with icon / selected | 24dp |
| Handle | Pressed (either state) | 28dp |
| Handle | Shape | full |
| Handle | Elevation token | level1 = 1dp (disabled: 0dp) |
| Icon | Size (both states) | 16dp |
| State layer | Size | 40dp, full |
| Target | Size | 48dp |
| Label gap | `switchPadding` | 16dp [mdc-android] |

- [tokens] also list a generic `handle.width/height = 20dp`. This is unused by the page table; treat it as legacy.

**Typography** — Label `on-surface`; supporting text may use `on-surface-variant` [m3 page]. Type role Body Medium [mdc-android].

**Colour roles** [tokens unless noted]

| Element | Unselected | Selected | Disabled |
|---|---|---|---|
| Track fill | `surface-container-highest` | `primary` | Unselected: `surface-container-highest`; selected: `on-surface`; track opacity 0.12 |
| Track outline | `outline` | none | `on-surface` (×0.12) |
| Handle | `outline`; `on-surface-variant` on hover, focus, press | `on-primary`; `primary-container` on hover, focus, press | Unselected: `on-surface` @0.38; selected: `surface` @1.0 |
| Icon | `surface-container-highest` | `primary` [tokens] vs `on-primary-container` [m3 page caption; mdc-android] | Unselected: `surface-container-highest` @0.38; selected: `on-surface` @0.38 |
| State layer | `on-surface` | `primary` | none |
| Focus indicator | `secondary`, 3dp, offset 2dp | | |

- The caption's role list (light and dark): surface container highest, outline, outline, primary, on primary, on primary container.

**States** — Enabled, hovered, focused, pressed, disabled. Opacities 0.08 / 0.10 / 0.10 [tokens].

**Behaviour & motion** [m3 page]
- A toggle succeeds when the handle slides to the other end of the track. The handle grows when switched on: "The **on** state … is indicated by a larger handle size".
- Touch: tap or drag grows the handle (to 28dp).
- Cursor: hover enlarges the hover area on/off; click grows the handle.
- Motion speed: the switch is the canonical "Fast" spatial example, and "color change of the switch handle" the Fast effects example [m3 page: m3-expressive-motion-theming]. Exact springs: n/s.

**Adaptive / modality** — Behaviour differs by touch vs cursor (above). Window-class guidance: n/s.

**Accessibility** [m3 page]
- Initial focus lands on the handle. Tab focuses; Space or Enter toggles.
- The label comes from the adjacent text, followed by the role.
- If the visible text is ambiguous, extend the a11y label. Example: "Photo album" becomes "Photo album access".
- Colours meet non-text contrast. Density: avoid by default.

**Do / don't** [m3 page]
- Do use icons that clearly mean on/off (✓ and ✕). Don't use ambiguous icons such as a moon or pencil.
- Don't put "On"/"Off" text inside the switch (too small to be accessible).
- Keep labels short; describe what the control does when on.
- Don't use a switch for opposing options or as a CTA.

---

## 4. Sliders (standard, centered, range)

**Status** — **M3 Expressive update, May 2025** (page updated 2026-07-17): "expressive configurations for orientation, shape sizes, and an inset icon". Updated on MDC-Android and Compose [m3 page].
- Renames: **continuous → standard**; "The **discrete** slider is now the **stops** configuration".
- New: horizontal/vertical orientation; optional inset icon (standard only); sizes XS (existing default), S, M, L, XL.
- Earlier "Visual refresh to improve non-text contrast", Dec 2023:
  - Added the centered configuration and range selection.
  - New track and handle shapes.
  - "Slider handle adjusts width upon selection".
  - "Slider tracks adjust in shape when sliding to the edge".
  - Refreshed colours, a stop indicator, and larger label text.
- Variant table [m3 page]:

| Variant | M3 | M3 Expressive |
|---|---|---|
| Standard | Available as "continuous" | Available |
| Centered | "Available (web only)" | Available |
| Range | Available | Available |
| Discrete | Available | Available as "stops" configuration |

- Sizes S–XL: "Available on Android Views (MDC-Android). Available as tokens on other platforms". To resize elsewhere, swap the `md.comp.slider.xsmall.*` tokens for the target size's tokens [m3 page].
- [mdc-android]: `Widget.Material3.Slider.Legacy` reverts to the pre-2023 look ("**not recommended**"). `app:tickVisible` is deprecated in favour of `tickVisibilityMode` (default `autoLimit`).

**Purpose & when to use** [m3 page]
- Select a value along a range: volume, brightness, image-filter intensity. Changes take effect immediately while dragging. Present the full range of values.
- **Standard**: one value, starting from zero or the beginning of a sequence.
- **Centered**: a value from a negative-to-positive range, where zero or the default sits in the middle.
- **Range**: two handles defining a min and a max. Avoid using it vertically (cognitive load).

**Configurations** [m3 page]
- Orientation: horizontal (default) or vertical; vertical puts zero at the bottom.
- Size: XS (default), S, M, L, XL.
- Stop indicators: on or off.
- Value indicator: on or off.
- Inset icon: on or off. Standard slider only, and only at M/L/XL (track ≥40dp). Not on centered or range sliders.

**Anatomy** [m3 page]
1. Value indicator (optional)
2. Stop indicators (optional)
3. Active track
4. Handle
5. Inactive track
6. Inset icon (optional)

- The active track runs from the minimum to the handle; on a range slider, between the two handles. Values increase left to right in LTR and are reversed in RTL.

**Measurements per size** [m3 page table; tokens]

| Attribute | XS | S | M | L | XL |
|---|---|---|---|---|---|
| Track thickness (active = inactive) | 16dp | 24dp | 40dp | 56dp | 96dp |
| Handle height | 44dp | 44dp | **52dp [m3 page] / 44dp [tokens]** | 68dp | 108dp |
| Handle width | 4dp | 4dp | 4dp | 4dp | 4dp |
| Track outer corner (leading/trailing shape) | 8dp | 8dp | 12dp | 16dp | 28dp |
| Inset icon size | — | — | 24dp | 24dp | 32dp |
| Inset icon padding [tokens] | — | — | 6dp | 6dp | 8dp |

Common measurements [tokens unless noted]:
- Handle width 4dp; **pressed and focused 2dp**; hover and disabled 4dp. Handle shape full. Handle elevation token level1 = 1dp ([mdc-android] `thumbElevation` default 2dp).
- Handle-to-track gap: `active.handle.leading-space` / `trailing-space` / `padding` = 6dp ([mdc-android] `thumbTrackGapSize` 6dp).
- Inner corners of the track next to the handle: 2dp (`active.track.inner-corner`; [mdc-android] `trackInsideCornerSize` 2dp). Outer corners are full on the XS common set.
- Stop indicator 4dp circle, with 4dp trailing space from the track end. Legacy tick marks (`with-tick-marks.container.size`) are 2dp.
- Value indicator (label) container: 44dp tall × 48dp wide [m3 page]. Bottom space between indicator and handle: 12dp (`value-indicator.active.bottom-space`). Legacy baseline `label.container.height` is 28dp.
- State layer 40dp [tokens]. Minimum thumb touch target 48dp [mdc-android].
- Range sliders: when handles overlap, the handle gets a 1dp `on-primary` outline (`with-overlap.handle.outline`). [mdc-android] `minSeparation` defaults to 0dp.

**Typography**
- Value indicator text: **Label Large** (14/20) [tokens]. Its tracking and weight tokens point at Body Large (0 / 400), which is a token-table inconsistency.
- Legacy label: Label Medium (12/16, 500).
- The Dec 2023 refresh mentions "larger label text" [m3 page].

**Colour roles** [tokens; m3 page caption order: inverse surface, inverse on surface, primary, on primary, primary, secondary container, on secondary container, on secondary container, on primary]

| Element | Enabled | Disabled |
|---|---|---|
| Active track | `primary` | `on-surface` @0.38 |
| Inactive track | `secondary-container` ([mdc-android] default `colorSurfaceContainerHighest`) | `on-surface` @0.12 |
| Handle | `primary` | `on-surface` @0.38 |
| Stop indicator on active track | `on-primary` | `inverse-on-surface` @0.38 |
| Stop indicator on inactive track | `on-secondary-container` | `on-surface` @0.38 |
| Value indicator container / text | `inverse-surface` / `inverse-on-surface` | — |
| Inset icon (active / inactive track) | `on-primary` / `on-secondary-container` (inferred from caption) | n/s |
| State layer | `primary` (0.08 hover, 0.10 focus, 0.10 pressed) | — |

**States** — Enabled, disabled, hovered, focused, pressed [m3 page]. Dragged: the foundations value is +16% [m3 page: states], but no slider-specific drag token. Hover leaves the handle at 4dp; focus and press narrow it to 2dp [tokens].

**Behaviour & motion** [m3 page]
- **Select & drag**: the standard slider drags smoothly. With stops, the handle snaps to the nearest stop.
- **Select jump**: tapping the track moves the handle there, or to the nearest stop.
- The handle "changes shape when it's being pressed or dragged" (width shrinks), and the value appears.
- Range sliders show only one value label at a time. If the value is shown elsewhere, the indicator isn't required.
- Optional external text field: keep it two-way synced and next in tab order after the slider.
- Inset icon:
  - It moves from the active track to the inactive track when there isn't room, for example at low values.
  - Consider swapping the icon at zero (volume → mute).
- The track adjusts its shape at the edges (Dec 2023). Exact timing: n/s.
- [mdc-android] `labelBehavior` default `floating`; `LabelFormatter` (for example 1.5K); `continuousModeTickCount`; `trackIconActiveStart/End` and `trackIconInactiveStart/End`.

**Adaptive / modality**
- Larger sizes increase targets and emphasis. Reserve **XL for "hero moments"** where the slider is the most important element on the page [m3 page].
- Window-class rules: n/s.
- Touch: tap or drag narrows the handle and shows the value. Cursor: the cursor changes on hover; click+drag narrows the handle and shows the value [m3 page].

**Accessibility** [m3 page]
- Initial focus goes to the handle.

| Key | Action |
|---|---|
| Tab | Focus the handle |
| Arrows | ±1 value or one stop |
| Space + arrows | ±a larger interval or one stop |
| Home / End | Minimum / maximum |

- Role is **slider**; the label matches the adjacent text. Stepper icon buttons outside the slider take the **button** role.
- The end of the inactive track needs ≥3:1 contrast with the background, via a stop indicator or icons. All sliders carry end stops unless the inactive track already meets 3:1.
- [mdc-android]: set `contentDescription`; use `labelFor` when an external TextView shows the value.

**Do / don't** [m3 page]
- Don't use inset icons on XS/S sliders ("track thicknesses under 40dp") or on centered/range sliders.
- Avoid vertical range sliders.
- Avoid too many stops; it crowds the track and makes the value hard to adjust.
- Keep active and inactive tracks the same thickness.
- Use plus/minus icons or text at the ends as an alternative to end stops.

---

## 5. Text fields (filled, outlined)

**Status** — Baseline M3 (page updated 2026-09-08). Differences from M2: colour only [m3 page]. No Expressive update. [mdc-android]: the `passwordToggle*` attributes are deprecated in favour of `endIconMode`. The token table also contains **Select** and **Autocomplete** sets (filled/outlined): menu container `surface-container`, elevation level2 (3dp), 4dp corners, 48dp list items, Label Large text, selected item `surface-container-highest`.

**Purpose & when to use** [m3 page]
- Enter text in forms and dialogs (contact details, payment, login).
- Both variants have identical functionality; choose by visual style, by the UI's goals, and by distinctness from buttons and surroundings.
- **Outlined** has less emphasis and simplifies forms with many fields. **Filled** has more emphasis.
- If both are used, separate them by region (for example, a dialog vs the page). Never mix them in one form.

**Variants / configurations** [m3 page]
- Variants: filled, outlined.
- Configurations: supporting text, leading icon, trailing icon, both icons, prefix, suffix, multi-line.
- Input display modes:
  - **Single-line**: text scrolls horizontally.
  - **Multi-line**: grows and pushes content down.
  - **Text area**: fixed height, scrolls vertically. Prefer it over multi-line on web, and make sure it fits mobile screens.
- Other configurations:
  - **Read-only**: styled like a normal field, clearly labelled read-only.
  - **Required**: asterisk on the label.
  - **Character/word counter**.
  - **Error** state.
- Trailing-slot types:
  1. Icon signifier, e.g. a calendar that opens a date picker
  2. Valid/error icon
  3. Clear icon (only when text is present)
  4. Voice input icon
  5. Dropdown icon
  6. Image, 24dp tall (e.g. a card brand)

**Anatomy** [m3 page]
- *Filled (10)*:
  1. Container
  2. Leading icon
  3. Label (empty)
  4. Label (populated)
  5. Trailing icon
  6. Focused active indicator
  7. Caret
  8. Input text
  9. Supporting text
  10. Enabled active indicator
- *Outlined (9)*:
  1. Enabled container outline
  2. Leading icon
  3. Label (empty)
  4. Label (populated)
  5. Trailing icon
  6. Focused outline
  7. Caret
  8. Input text
  9. Supporting text
- The guidelines tab swaps items 2 and 3 for outlined.

**Measurements** [m3 page; tokens]

| Attribute | Filled | Outlined |
|---|---|---|
| Container height | 56dp | 56dp |
| Container shape | 4dp top corners, square bottom (`corner.extra-small.top`) | 4dp all corners (`corner.extra-small`) |
| Top/bottom padding | 8dp | n/s (label vertically centred) |
| Left/right padding, no icons / with icons | 16dp / 12dp | 16dp / 12dp |
| Icon-to-text gap | 16dp | 16dp |
| Icon size | 24dp | 24dp |
| Populated-label side padding (outline notch) | — | 4dp |
| Supporting text/counter top padding | 4dp | 4dp |
| Supporting text ↔ counter gap | 16dp | 16dp |
| Target | 56dp | 56dp |
| Indicator / outline, enabled & hover | 1dp active indicator | 1dp outline |
| Indicator / outline, focused | **2dp** active indicator | **3dp** outline [tokens] ([mdc-android] `boxStrokeWidthFocused` 2dp) |
| Disabled | 1dp indicator | 1dp outline |

- [mdc-android] sizing: start/end icon minimum 48dp touch size; recommended default width 245dp; max width 488dp; min width 56dp without a label or 88dp with a label.
- Focus-indicator tokens: filled `focus.active-indicator.thickness` 3dp; outlined `focus.indicator.outline` in `secondary`, 3dp.

**Typography** [tokens]

| Element | Role |
|---|---|
| Input text | Body Large (16/24, 400) |
| Label, empty | Body Large (16/24) |
| Label, populated | Body Small (12/16) |
| Supporting text, counter, error text | Body Small (12/16) |
| Prefix/suffix | Inherit the input role per tokens; [mdc-android] defaults to Title Medium |

**Colour roles** [tokens]

| Element | Enabled | Hover | Focus | Error | Error hover | Disabled |
|---|---|---|---|---|---|---|
| Filled container | `surface-container-highest` | + `on-surface` 0.08 state layer | same | same | + state layer | `on-surface` @0.04 |
| Filled active indicator | `on-surface-variant` | `on-surface` | `primary` (2dp) | `error` | `on-error-container` | `on-surface` @0.38 |
| Outlined outline | `outline` | `on-surface` | `primary` (3dp) | `error` | `on-error-container` | `on-surface` @0.12 |
| Label | `on-surface-variant` | filled `on-surface-variant`; outlined `on-surface` | `primary` | `error` | `on-error-container` | `on-surface` @0.38 |
| Input text | `on-surface` | `on-surface` | `on-surface` | `on-surface` | `on-surface` | `on-surface` @0.38 |
| Caret | `primary` | — | `primary` | `error` | — | — |
| Leading icon | `on-surface-variant` | same | same | `on-surface-variant` (unchanged) | same | `on-surface` @0.38 |
| Trailing icon | `on-surface-variant` | same | same | `error` | `on-error-container` | `on-surface` @0.38 |
| Supporting text | `on-surface-variant` | same | same | `error` | `error` | `on-surface` @0.38 |
| Placeholder / prefix / suffix | `on-surface-variant` | | | | | |

**States** [m3 page]
- Enabled, hovered, focused and disabled, each shown empty and populated.
- Error states: enabled, focused and hovered, each empty and populated.
- Disabled has no hover.

**Behaviour & motion** [m3 page]
- On focus, the label moves from the middle of the field to the top; it must always remain visible. Don't truncate it or wrap it to two lines.
- Error text *replaces* supporting text, to avoid layout shift. Long errors may wrap, so leave enough spacing between fields.
- An error icon is strongly recommended as a second, non-colour cue.
- Leading and trailing icons swap sides in RTL.
- Label animation timing: n/s.

**Adaptive** [m3 page]
- Compact: fields can span the full width.
- Medium/expanded: bind fields with flexible margins or containers. Don't span the full width of large screens. Set min/max values for margins, padding and container sizes.
- Dense fields: allowed as an opt-in, not by default.

**Accessibility** [m3 page]
- Role **textbox**; the a11y label equals the field label. Tab focuses non-disabled fields.
- Interactive trailing icon: role Button, with a functional label ("Show password" / "Hide password"). A non-interactive error icon is labelled "Error".
- Errors: role **alert**. Order: supporting text first, then the error.
- Counter label: "Character count, 5/20".
- Prefix/suffix: give each its own ID-referenced label, e.g. "Euro", "At gmail dot com".
- Required fields: the a11y label includes the asterisk.
- The outline should reach ≥3:1 against the background.
- [mdc-android]: error text live region defaults to `POLITE`.

**Do / don't** [m3 page]
- Swap supporting text for error text; don't stack both.
- Don't truncate labels or make them multi-line.
- Show an asterisk on required fields and explain it, either in supporting text or in one note at the top of the form.
- Don't mix filled and outlined fields in one form.
- Don't use fixed margins that stretch fields across large screens.
- Use multi-line fields or text areas, not single-line fields, for long answers.

---

## 6. Date pickers (docked, modal, modal input)

**Status** — Baseline M3 (page updated 2026-07-27). Differences from M2 [m3 page]:
- "Titles and labels are larger and have increased spacing to accommodate 48dp target size".
- New colour mappings; no drop shadow.
- Variants renamed to be device-independent: desktop → **docked**; mobile → **modal**; date input → **modal date input**.

No Expressive update.

**Purpose & when to use** [m3 page]
- Select a date or a range, embedded either in dialogs (compact windows) or in text-field drop-downs (medium/expanded).
- **Docked**: a text field plus a drop-down calendar, for near *and* distant dates.
- **Modal**: a calendar dialog. "Don't use a modal date picker to prompt for dates in the distant past or future, such as a date of birth." Use modal input or docked instead.
- **Modal input**: keyboard entry in a dialog. Good as the default when no calendar is needed (e.g. a 1979 date). Alternatively, use a plain text field with hint text.
- Ranges suit booking flights and hotels.

**Variants / configurations** [m3 page]
- Docked: day, month or year selection.
- Modal: single date, date range, or year selection.
- Modal input: single date or range.
- **Full-screen** modal: recommended for compact windows.

**Anatomy** [m3 page specs]
- *Docked (11)*:
  1. Outlined text field
  2. Month menu button
  3. Year menu button
  4. Icon button
  5. Weekday labels
  6. Unselected date
  7. Today's date
  8. Outside-month date
  9. Text buttons
  10. Selected date
  11. Container
- *Docked menu open (8)*: text field; month menu button (pressed); year menu button (disabled); header; menu; selected list item; unselected item; container.
- *Modal (13)*:
  1. Headline
  2. Supporting text
  3. Header
  4. Container
  5. Icon button
  6. Icon buttons
  7. Weekdays
  8. Today
  9. Unselected date
  10. Text buttons
  11. Selected date
  12. Menu button
  13. Divider
- *Modal year view (10)*: headline, supporting text, header, container, icon button, unselected year, selected year, text buttons, divider, menu button.
- *Modal range (15)*: adds the in-range active indicator, in-range date and month subhead.
- *Modal input (8)*:
  1. Headline
  2. Supporting text
  3. Header
  4. Container
  5. Icon button
  6. Outlined text field
  7. Text buttons
  8. Divider
- *Full-screen (14)*: includes a close icon button and a Save text button.

**Measurements** [tokens; page diagrams are image-only]

| Element | Docked | Modal | Modal input |
|---|---|---|---|
| Container W × H | 360 × 456dp | 360 × 524dp | 328 × 512dp |
| Container corner | 16dp (`corner.large`) | 28dp (`corner.extra-large`) | 28dp |
| Elevation | level3 (6dp) | level3 (6dp) | level3 (6dp) |
| Header height | 64dp | 120dp (range: 128dp) | 120dp |
| Date cell container | 48 × 48dp, circular | 40 × 40dp, circular | — |
| Date state layer | 40 × 40dp, circular | 40 × 40dp | — |
| Today outline | 1dp `primary` | 1dp `primary` | — |
| Month/year menu button | 40dp tall, full radius, 18dp icon | — | — |
| Menu list item | 48dp; selected leading icon 24dp | — | — |
| Year chip | — | 72 × 36dp, full radius | — |
| Range active indicator | — | 40dp tall, full radius | — |
| Range (full-screen) container | — | corner none, elevation 0 | — |

- Targets: all interactive targets are 48×48dp [m3 page].

**Typography** [tokens]

| Element | Role |
|---|---|
| Modal headline (selected date) | Headline Large (32, Google Sans brand face) |
| Range headline | Title Large (22) |
| Header supporting text | Label Large (14) |
| Weekday labels, dates, years, docked menu items | Body Large (16, 400) |
| Docked menu button | Label Large (14, 500) |
| Range month subhead | Title Small (14, 500) |

**Colour roles** [tokens; m3 page captions]

| Element | Role |
|---|---|
| Container | `surface-container-high` |
| Headline / supporting text | `on-surface-variant` |
| Selected date or year | `primary` fill, `on-primary` text; state layer `on-primary` |
| Today | `primary` text and 1dp `primary` outline; state layer `primary` |
| Unselected date | `on-surface` text; state layer `on-surface-variant` |
| Outside-month date (docked) | `on-surface` @0.38 |
| Unselected year | `on-surface-variant` |
| Weekdays | `on-surface` |
| Menu button text/icon | `on-surface-variant`; disabled `on-surface` @0.38 |
| Docked menu selected item | `surface-variant` container |
| Range fill | `secondary-container` ([mdc-android] `rangeFillColor` = `colorSurfaceVariant`) |
| In-range text | `on-secondary-container`; state layer `on-primary-container` |
| Divider | `outline-variant` |
| Action text buttons | `primary` |

**States** — Date and year elements: enabled, disabled, hovered, focused, pressed (ripple). Opacities 0.08 / 0.10 / 0.10 [m3 page; tokens].

**Behaviour & motion** [m3 page]
- *Docked*:
  - Keyboard entry and calendar entry are both available immediately.
  - The calendar drops down just below the field and resizes dynamically to the month.
  - The year menu *replaces* the calendar view.
  - Month and year are navigable by arrows or drop-down menus.
- *Modal*:
  - Swipe horizontally between months.
  - Tap the year to open the year picker, then scroll vertically through years.
  - Range: tap the start and end dates; scroll vertically through months. Start/end are filled; dates between are "connected with a subtle highlight".
- Switch between modal picker and modal input with the edit (pencil) or calendar icon.
- Exit with OK (confirm) or Cancel, or tap outside. Until then the picker keeps focus. Full-screen adds a close (×) button and Save.
- Dialog enter/exit uses the standard dialog transition pattern; timing n/s.

**Adaptive** [m3 page]
- Compact: full-screen modal picker recommended, for readability and target size.
- Medium/expanded: docked works best.
- "The sizing of the docked and modal date picker components don't scale responsively". Don't enlarge them on big screens.

**Accessibility** [m3 page]
- Always allow manual text entry. The calendar icon is the *exclusive* entry point to the picker; each input is a separate tab stop.
- Format the date only after Enter or blur. No input masks while typing.
- Accept dashes, spaces, slashes, dots and leading zeros.
- Remove the optional **Clear** button if not needed, to cut tab stops.
- Show keyboard shortcuts in tooltips, e.g. Shift+Page Up for the previous year.
- Weekday headers are not focusable; their tooltip appears on pointer hover only.
- Dates need ≥**4.5:1** contrast.
- Keyboard:

| Key | Action |
|---|---|
| Enter | Close and save |
| Page Up/Down | Same date, previous/next month |
| Shift+Page Up/Down | Same date, previous/next year |
| Home/End | First day of the month (as published) |
| Shift+M | Month drop-down |
| Shift+Y | Year drop-down |

- Roles: prev/next and month/year drop-downs are Button; weekdays are Column header; the month grid is Grid.
- Field label states the purpose (e.g. "Event date"). Helper text gives the format; default "MM/DD/YYYY".
- Screen readers read the full date ("Monday, August 17").
- [mdc-android]: the dialog title is announced on launch; use a descriptive title.

**Do / don't** [m3 page]
- Don't use the modal calendar for birthdays; use input or docked.
- Do make input the default when the calendar adds nothing.
- Don't scale pickers up on large screens.
- Keep both entry methods available.

---

## 7. Time pickers (dial, input; vertical/horizontal)

**Status** — Baseline M3 (page updated 2026-07-17). Differences from M2: colour only [m3 page]. No Expressive update.

**Purpose & when to use** [m3 page]
- Modal pickers over a scrim, for entering hours, minutes or periods (setting alarms, scheduling meetings).
- Not for granular timing such as stopwatch milliseconds.
- Make sure time can be set easily by hand on mobile.
- **Input** variant: keyboard numbers. It should be reachable from any mobile time picker via the keyboard icon.

**Variants / configurations** [m3 page]
- Variants: dial, input.
- Layout: vertical (default on mobile) or horizontal/landscape.
- Clock: 12h or 24h for both dial and input. 24h is set outside the component, typically by system settings.
- 12h dial: all numbers on the outer ring.
- 24h dial: **inconsistent source.** The text says "even numbers appear in an inner ring, and odd numbers appear in an outer ring". An image caption says "Hours 0–11 use an outer dial, hours 12–23 use an inner dial". [mdc-android]: 12H = 1 ring, 24H = 2 rings.
- The AM/PM selector appears only for 12h.

**Anatomy** [m3 page specs]
- *Dial (14)*:
  1. Headline
  2. Time selector separator
  3. Container
  4. Period selector container
  5. Period selector label
  6. Clock dial selector centre
  7. Clock dial selector track
  8. Text button
  9. Icon button
  10. Clock dial selector container
  11. Clock dial label text
  12. Clock dial container
  13. Time selector label text
  14. Time selector container
- *Input (10)*:
  1. Headline
  2. Separator
  3. Container
  4. Period selector container
  5. Period selector label
  6. Text button
  7. Icon button
  8. Input field supporting text
  9. Input field label text
  10. Input field container
- The input selector differs from a normal text field: it has a highlight when selected, a larger shape/size/font, and its label sits *below* the field. Hours and minutes are separate inputs.

**Measurements** [m3 page; tokens]

| Element | Dial | Input |
|---|---|---|
| Container | dynamic W/H; 24dp padding all sides; headline left-aligned; corner 28dp; elevation level3 (6dp) | same |
| Time selector / input field | 96 × 80dp (24h vertical: 114dp wide); corner 8dp | 96 × 72dp; corner 8dp; focus outline 2dp `primary` |
| Period selector, vertical layout | 52 × 80dp | 52 × 72dp |
| Period selector, horizontal layout | 216 × 38dp | — |
| Period selector shape / outline | 8dp corner / 1dp `outline` | same |
| Clock dial | 256dp circle | — |
| Dial selector handle | 48dp | — |
| Dial selector centre | 8dp | — |
| Dial selector track | 2dp wide | — |
| Dial targets | 48×48dp [m3 page a11y] | — |

**Typography** [tokens]

| Element | Role |
|---|---|
| Headline | Label Medium (12, 500), `on-surface-variant` |
| Dial time selector digits and separator | Display Large (57, Google Sans brand, 400) |
| Input field digits | Display Medium (45); separator Display Large (57) |
| Input supporting text (labels below fields) | Body Small (12) |
| AM/PM | Title Medium (16, 500) |
| Dial numbers | Body Large (16) |

**Colour roles** [tokens]

| Element | Unselected | Selected / focused |
|---|---|---|
| Container | `surface-container-high` | — |
| Time selector / input field | `surface-container-highest` fill, `on-surface` text | `primary-container` fill, `on-primary-container` text; input focus adds a 2dp `primary` outline |
| Separator | `on-surface` | — |
| Period selector | `outline` border, `on-surface-variant` text | `tertiary-container` fill, `on-tertiary-container` text |
| Clock dial | `surface-container-highest`; numbers `on-surface` | Selected number `on-primary` |
| Dial handle, track, centre | `primary` | — |
| State layers | Use each element's content colour (`on-surface`, `on-surface-variant`, `on-primary-container`, `on-tertiary-container`) | — |
| Focus indicator (input) | `secondary`, 3dp, 2dp offset | — |

**States** — Enabled, hover, focus, pressed. Disabled: n/s [m3 page].

**Behaviour & motion** [m3 page]
- Two ways to set time: type into the hour/minute fields, or select a field and drag/tap the dial. The dial and the field update together.
- The keyboard icon (bottom-left) toggles between dial and input; the clock icon toggles back.
- Text buttons: Cancel and OK. Tapping outside also dismisses; otherwise the picker keeps focus.
- Dialog enter/exit transitions; timing n/s.
- Time pickers should not scroll and don't scroll with the background.
- [mdc-android]: default input mode is `INPUT_MODE_CLOCK` with 12H. With 24H it defaults to `INPUT_MODE_KEYBOARD`. Title default "Select Time".

**Adaptive** [m3 page]
- Swap orientation or variant based on device orientation and viewport. Use landscape on larger breakpoints or when height is limited, to avoid scrolling the dial. Fall back to the input picker when even landscape doesn't fit.
- Never let edges crop the picker or other elements obscure it.
- Don't apply density to the dial in constrained viewports; use the input picker.
- Android Views always shows the dial selector.

**Accessibility** [m3 page]
- Always allow manual entry. Consider input as the default when no dial is needed.
- Keyboard: Tab focuses a non-disabled time slot; Space or Enter activates it.
- Hour and minute fields: role **Text input**, labels "Hour" / "Minute".
- AM/PM: label "AM or PM". Role Radio button (in list) on Wiz/Compose; Checkbox (in list) on Android Views.
- Keyboard icon: "Toggle input picker" (Button). Clock icon: "Toggle dial picker". Cancel and OK are Buttons.
- Dial value: "{Value} Hours or minutes of {Total}", Button role, read as e.g. "Hour 7 of 12".
- [mdc-android]: the title is announced on open.

**Do / don't** [m3 page]
- Make input reachable from the dial (keyboard icon).
- Don't densify the dial; switch variant instead.
- Don't let the picker scroll or be cropped; change orientation.
- Hide AM/PM for 24h users.

---

## 8. Progress indicators (linear & circular)

**Status** [m3 page; tokens; mdc-android]
- **M3 Expressive update, Aug 2024** (page updated 2026-07-29): "configurations for height and wavy shape". Track height becomes configurable and a **Wavy** shape is added.
- **Dec 2023 Non-text contrast (NTC)**: added an end stop indicator; higher track/indicator contrast; "new motion behavior"; rounded corners.
- July 2022: added to M3 (colour, dynamic colour).
- "Baseline tokens: The circular and linear progress indicator had separate token sets. These are no longer recommended." These are the `[Deprecated] md.comp.linear-progress-indicator` and `md.comp.circular-progress-indicator` sets: square corners, `surface-container-highest` track, 48dp circular, four-colour brand variants.
- [mdc-android]: `.Legacy` styles revert NTC changes ("not recommended"). Wavy has no theme attribute; apply the `Widget.Material3Expressive.*ProgressIndicator.Wavy` styles directly.

**Purpose & when to use** [m3 page]
- Show the status of ongoing processes such as loading an app, submitting a form or saving. Use for expected waits **over 5s**; for 200ms–5s use a loading indicator.
- One indicator for a group of items, not one per item.
- **Linear**: best on the edge of a container. **Circular**: best centred in an element.
- Use the same variant for the same process throughout the product.
- **Determinate** when progress and time are known; it must accurately reflect progress. **Indeterminate** when unknown.
- Switch from indeterminate to determinate as information arrives.
- For very long waits, let people navigate away.

**Variants / configurations** [m3 page]

| Category | Options | Availability |
|---|---|---|
| Variant | Linear, circular | M3 and Expressive |
| Behaviour | Determinate (default), indeterminate | M3 and Expressive |
| Track thickness | Fixed 4dp (default); configurable | Configurable: Expressive only |
| Shape | Flat (default), wavy | Wavy: Expressive only |

- [mdc-android] circular style sizes: Medium, Small and ExtraSmall exist (dimensions n/s).

**Anatomy** — 1. Active indicator. 2. Track. 3. Stop indicator (linear determinate only) [m3 page].

**Measurements** [tokens unless noted]

| Attribute | Linear flat | Linear wavy | Linear thick (8dp) | Circular flat | Circular wavy | Circular thick |
|---|---|---|---|---|---|---|
| Active indicator thickness | 4dp | 4dp | 8dp | 4dp | 4dp | 8dp |
| Track thickness | 4dp | 4dp | 8dp | 4dp | 4dp | 8dp |
| Overall height / size | 4dp | **10dp** | 8dp (wavy 14dp) | **40dp** | **48dp** | **52dp** ([mdc-android]: thick flat 44dp, thick wavy 52dp) |
| Wave amplitude | — | **3dp** | n/s | — | **1.6dp** | n/s |
| Wavelength | — | **40dp** determinate; **20dp** indeterminate | n/s | — | **15dp** | n/s |
| Indicator–track gap | 4dp | 4dp | 4dp | 4dp | 4dp | 4dp |
| Stop indicator | 4dp circle, 0dp trailing space | same | 4dp, 2dp trailing space | none | none | none |
| Shape | full (rounded) | | | | | |

- Amplitude is measured from the centre of the resting position to the centre of a peak. Wavelength is the distance between adjacent peaks. "Height is the overall container height" [m3 page].
- Linear: inset ≥**4dp** from the screen or element edge (modifiable). Don't use inside elements under **40dp** wide [m3 page].
- Circular: flexible from **24dp to 240dp** [m3 page]. [mdc-android] `indicatorInset` 4dp.
- Thicker variants are "sample measurement for makers to adjust" [m3 page]. [mdc-android] recommends `trackThickness` 8dp with `trackCornerRadius` 4dp.

**Typography** — None.

**Colour roles** [tokens; m3 page]

| Element | Role |
|---|---|
| Active indicator | `primary` |
| Track | `secondary-container` ([mdc-android] defaults: linear `colorPrimaryContainer`; circular track transparent in M3, visible in Expressive indeterminate) |
| Stop indicator | `primary` |
| In a button | Indicator = the button's label/icon colour; remove the track |

**States** — Not interactive. No hover, focus or press tokens.

**Behaviour & motion** [m3 page; mdc-android]
- Determinate fills 0→100%. Linear animates leading→trailing; circular starts at the top and runs clockwise by default.
- At very low progress, the active indicator shows as a **dot**.
- Indeterminate "move[s] along a fixed track, growing and shrinking".
- Wavy increases container height; "The waveform should scale with the size so the proportions look the same across sizes". At very small sizes the wave is barely visible, so use flat in small buttons.
- [mdc-android] wave parameters:
  - `wavelengthDeterminate` / `wavelengthIndeterminate`, `waveAmplitude`, `waveSpeed`.
  - Amplitude ramp range: `waveAmplitudeRampProgressMin` 0.1, `waveAmplitudeRampProgressMax` 0.9.
  - `indeterminateAnimatorDurationScale` 1.
- [mdc-android] indeterminate animation types:
  - Linear: `disjoint` (default; two segments) or `contiguous` (three adjacent coloured segments; needs ≥3 colours).
  - Circular: `advance` (default).
- [mdc-android] show/hide behaviours: `none` (default), `outward`, `inward`, `escape` (linear only). Also `showDelay` and `minHideDelay` in ms (default 0). Indeterminate→determinate transitions smoothly via `setProgressCompat(p, true)`.
- Exact animation durations: n/s.

**Adaptive** [m3 page]
- Reserve very large circular indicators for **large and extra-large windows** (desktop).
- Linear spans the full width of its host element.
- Placement:
  - Top of the page for whole-page loads; on a card's edge for card loads; on the expanding edge when a container will grow.
  - Circular: centre it on the loading element, or in the empty space where new content will appear, without overlapping existing content.
- RTL: mirror linear indicators; never mirror circular ones.

**Accessibility** [m3 page]
- Role **progress bar**. The label names the process and the content, e.g. "Loading news article", "Refreshing page".
- The active indicator must have ≥3:1 contrast against the background, and against the host component when embedded.
- Linear: the stop indicator is **required** if the track has <3:1 contrast with its container or the surface behind.
- [mdc-android]: TalkBack can't draw a focus box for bounds ≤4dp; add vertical padding.

**Do / don't** [m3 page]
- Indicate overall progress for a group; don't show one per item.
- Don't add indicators to every button in a list.
- Use flat (not wavy) in very small buttons.
- Only remove the stop indicator with ≥3:1 contrast on all adjacent surfaces.
- Keep one variant per process across the product.

---

## 9. Loading indicator (default / contained; morphing shapes)

**Status** [m3 page; mdc-android]
- **New component, M3 Expressive, May 2025** (page updated 2026-07-29). "Recommended as a replacement for indeterminate circular progress indicators"; "should replace most uses of the indeterminate circular progress indicator". There is no M3 (baseline) version.
- Naming conflict: [m3 page] "1. Default 2. Contained" (default = uncontained), while [mdc-android] lists "1. Default (contained) 2. Uncontained". In [mdc-android] code the default style `Widget.Material3.LoadingIndicator` has a transparent container and `.Contained` adds it, which agrees with m3.

**Purpose & when to use** [m3 page]
- Short, indeterminate waits of **200ms–5s**, where progress isn't detectable or its length isn't worth showing. Uses motion to mitigate perceived latency.
- Always reflects an ongoing process; "never simply decorative".
- Used for pull-to-refresh.
- **Not** for processes that may become determinate. "Don't transition a loading indicator into a progress indicator"; start with an indeterminate progress indicator instead.
- Can sit inside buttons (validating a form, checking for updates) or replace a tab icon.

**Variants / configurations** — One variant. Containment: default (no container) or contained [m3 page].

**Anatomy** — 1. Active indicator: "a looping shape morph sequence composed of seven unique Material 3 shapes". The seven shapes are not named in the sources (n/s). 2. Container (optional): a circle [m3 page].

**Measurements** [m3 page; tokens; mdc-android]

| Attribute | Value |
|---|---|
| Default size (container) | 48 × 48dp, full radius |
| Active indicator (shape) | 38dp ("the size is 48dp while the shape container is 38dp") |
| Allowed size range | 24–240dp; the container : indicator ratio stays constant when resizing |

**Typography** — None.

**Colour roles** [tokens; m3 page]

| Configuration | Active indicator | Container |
|---|---|---|
| Default | `primary` | none (token `container.color` = `secondary-container` exists but isn't shown) |
| Contained | `on-primary-container` | `primary-container` |

- When the container is visible, the indicator changes from `primary` to `on-primary-container` [m3 page].
- [mdc-android]: if several indicator colours are given, the colour changes along the morph sequence.

**States** — Not interactive.

**Behaviour & motion** [m3 page]
- Loops through morphs between the seven shapes ("Capture attention through motion"). Morph timing and rotation: n/s.
- Shape morph is a platform-API feature of the Material shape library, shared with the standard button group [m3 page: shape].
- Pull-to-refresh:
  - Jetpack Compose only.
  - The gesture must pass a **threshold** before a refresh starts; reversing past the threshold cancels.
  - The indicator stays visible until the new content is visible or the user navigates away. Don't let it scroll off-screen.
  - It can sit on top of content or next to it.
  - The contained version should be used for pull-to-refresh.
- [mdc-android]: `showDelay` and `minHideDelay` (default 0ms).

**Adaptive** [m3 page]
- The 48dp default is ideal for compact windows. As panes and windows grow, scale the indicator so it stays proportional to the surrounding empty space, never above 240dp.
- Reserve very large indicators for large/extra-large windows (desktop).
- Placement: centre on the loading page or container, or in the empty space where new items will load.
- Use the container when the indicator sits over other content. It isn't needed on a plain surface.

**Accessibility** [m3 page]
- Role **progress bar**, with a purpose label ("Loading news article", "Refreshing page").
- The active indicator needs ≥3:1 against the background or host component; "the container does not". [mdc-android] adds that contained versions need 3:1 between indicator and container.
- Pull-to-refresh can't rely on swipe alone. Provide a single-pointer alternative, such as a refresh action in the app bar or a menu.
- Users must be able to navigate to the indicator and understand it.

**Do / don't** [m3 page]
- Keep the indicator in view until the refresh completes.
- Don't transition a loading indicator into a determinate progress indicator.
- Don't exceed 240dp or go below 24dp.
- Don't use it decoratively.
- Use the contained style over content and for pull-to-refresh.
- Prefer it over the indeterminate circular progress indicator for short waits.
