# M3 / M3 Expressive component digest — Group A (buttons family + toolbars)

Scope: buttons (+ "All buttons" overview), button groups, split button, FAB, extended FAB, FAB menu, icon buttons, segmented buttons (legacy), toolbars (+ bottom app bar legacy).
Sources: m3.material.io pages (content API, 2026-09-23 corpus; page "Updated" stamps Jul–Sep 2026) = **[m3 page]**; resolved m3 token tables (dsdb 38.2.9) = **[tokens]**; material-components-android docs = **[mdc-android]**. **[derived]** = arithmetic on token values (e.g. width = leading + icon + trailing), not stated in sources. "n/s" = not specified in sources. Colour hex values in tokens are the baseline light scheme; only role names are recorded here.

---

## Cross-cutting findings

1. **One size ladder for every button-like component** [tokens]: XS 32dp / S 40dp (default) / M 56dp / L 96dp / XL 136dp container height. Shared by buttons, icon buttons, toggle buttons, button groups (standard + connected) and split buttons. FAB family uses a separate ladder: FAB 56 / medium FAB 80 / large FAB 96 (extended FAB small 56 / medium 80 / large 96).
2. **Type role scales with size** [tokens]: XS & S = label-large (14/20, w500); M = title-medium (16/24, w500); L = headline-small (24/32, w400); XL = headline-large (32/40, w400). Extended FAB: S title-medium, M title-large (22/28), L headline-small. Baseline extended FAB used label-large.
3. **Round vs square shape system** [m3 page + tokens]: Round = fully rounded (corner.full) at every size. Square radius by size: XS 12, S 12, M 16, L 28, XL 28dp. Same values for buttons and icon buttons.
4. **Shape-morph rules** [m3 page + tokens]: (a) *Pressed*: round and square both morph to the same, squarer pressed radius — XS 8, S 8, M 12, L 16, XL 16dp — animated with the "fast spatial" spring (damping 0.6, stiffness 800). (b) *Selected (toggle)*: resting shape inverts — round→square (selected radius = that size's square radius), square→round (full). Button groups add width morph (pressed item width +15%, same spring) and connected groups morph inner corners.
5. **Colour styles became "configurations", not variants** [m3 page]: buttons = elevated, filled (default), tonal, outlined, text; icon buttons = filled (default), tonal, outlined, standard. Variants are now just *default* vs *toggle (selection)*. Text buttons have no toggle. FAB variants are by size, not colour.
6. **Universal state/disabled values** [tokens]: state layer hover 8%, focus 10%, pressed 10% (dragged 16% at system level); disabled container = on-surface @ 10%, disabled label/icon = on-surface @ 38%; focus ring = secondary, 3dp thick, 2dp outer offset. State-layer colour always equals the content (label/icon) colour.
7. **Deprecations / "no longer recommended" → replacements**:
   - Segmented button → **connected button group** [m3 page].
   - Bottom app bar → **docked toolbar** (plus new floating toolbar) [m3 page].
   - Speed dial / stacked small FABs → **FAB menu** [m3 page].
   - Small FAB (40dp) → use a larger FAB size; **medium FAB (80dp) is now the most recommended** [m3 page].
   - Baseline extended FAB (56dp, label-large) → **small extended FAB** (56dp, title-medium, reduced padding) [m3 page].
   - Surface-colour FABs/extended FABs and "branded" FAB tokens → not recommended [m3 page + tokens].
   - FAB colour renames: old primary/secondary/tertiary → primary/secondary/tertiary **container**; new true primary/secondary/tertiary styles added [m3 page].
   - Small-button 24dp horizontal padding → 16dp [m3 page]; neutral text button no longer recommended (M2→M3 note).
   - Old per-style token sets (md.comp.filled-button, md.comp.filled-icon-button, etc.) are [Deprecated]; build expressive buttons from a *size* set + a *colour* set (e.g. md.comp.button.large + md.comp.button.filled) [tokens].
8. **48×48dp minimum target is enforced by layout, not by visual size** [m3 page]: XS (32) and S (40) visuals rely on padding/target areas; standard button-group gaps (XS 18dp, S 12dp) exist specifically to keep 48dp targets; connected XS/S groups get 48dp min width.
9. **Emphasis hierarchy** [m3 page, All buttons]: High = FAB / extended FAB / FAB menu, filled button, split button, standard button group; Medium = tonal, elevated, outlined; Low = connected button group, text button, icon button. One high-emphasis action per screen.
10. **Toolbars = slot containers** [m3 page + tokens]: 64dp tall; docked (full-width, square corners, standard/vibrant, bottom only) and floating (pill, elevated level 3, horizontal or vertical, may pair with a FAB). Never show a toolbar together with a navigation bar. Vibrant = primary-container surface; standard = surface-container.
11. **Expressive motion vs standard motion**: shape/width morphs use spring tokens (fast spatial 0.6/800); the split button's chevron rotation deliberately uses the *standard* (not expressive) motion scheme [m3 page]. Web: use a modified motion curve for rapid repeated clicks to avoid resonant overlapping animations [m3 page].
12. **Platform deltas** [m3 page + mdc-android]: Compose has separate floating toolbar, supports floating-toolbar-with-FAB and collapse-to-FAB on scroll; other platforms compose these manually. FAB menu has no native Android Views implementation (Compose interop only). On web the FAB menu is rendered as FAB + standard menu (4dp gap); icon buttons/FABs show tooltips on hover/focus; toolbar container gets `role=toolbar`. mdc hide-on-scroll behaviours are disabled when TalkBack is on. No XR-specific guidance in any of these sources.

### Shared system values used below [tokens]
| Item | Value |
|---|---|
| Elevation levels | L0 0dp, L1 1dp, L2 3dp, L3 6dp, L4 8dp, L5 12dp |
| Corner scale | none 0, extra-small 4, small 8, medium 12, large 16, large-increased 20, extra-large 28, extra-large-increased 32, extra-extra-large 48, full |
| Spacing tokens | space25 2, space50 4, space75 6, space100 8, space125 10, space150 12, space175 14, space200 16, space250 20, space300 24, space400 32, space600 48, space800 64, space900 72 dp |
| Type roles | label-large 14/20 w500; title-medium 16/24 w500; title-large 22/28 w400; headline-small 24/32 w400; headline-large 32/40 w400 (plain face = Google Sans Text in Google's baseline) |
| State layers | hover 0.08, focus 0.10, pressed 0.10, dragged 0.16 |
| Focus indicator | thickness 3dp, outer offset 2dp, inner offset −3dp; colour secondary |
| Spring "fast spatial" | damping 0.6, stiffness 800 |

---

## 1. Buttons (common buttons) — incl. "All buttons"

### Status
- **M3 Expressive update (May 2025), updated component** [m3 page]: "Buttons now have a wider variety of shapes and sizes, toggle functionality, and can change shape when selected."
- Added: toggle (selection) variant; sizes XS, M, L, XL (S = existing default); square shape; shape morph on press and on select.
- Small-button padding: 16dp recommended; **24dp "no longer recommended"** [m3 page] ("deprecated" in [mdc-android]).
- Token set `Button (baseline)` md.comp.button: "no longer recommended… For expressive, make the button using a size (md.comp.button.large) and color (md.comp.button.filled) token set." Per-style sets md.comp.elevated-button / filled-button / filled-tonal-button / outlined-button / text-button are **[Deprecated]** [tokens].
- M2→M3: neutral text button no longer recommended; icons and labels share one colour; M2 36dp slightly-rounded → M3 40dp fully rounded [m3 page].

### Purpose & when to use / not use
- Communicate discrete actions; used in dialogs, modals, forms, cards, toolbars, and standard button groups [m3 page].
- Don't overuse: too many buttons break hierarchy; move low-priority actions to overflow menus, icon buttons, nav rail, chips or text links [m3 page].
- Toggle buttons: binary selections (Save, Favorite); can change colour, shape and label when selected [m3 page].
- "All buttons" taxonomy — 10 types: button, toggle button, icon button, toggle icon button, split button, standard button group, connected button group, FAB, extended FAB, FAB menu [m3 page].
- Style choice: filled = most impact after FAB, final/unblocking actions (Save, Join now, Confirm), ideally one per page, may use tertiary colours; tonal = secondary palette, lower priority needing more than an outline (e.g. "Next" in onboarding); elevated = tonal-like + shadow, only for separation from a patterned/prominent background; outlined = medium emphasis, alternative/secondary actions, "escape a flow"; text = lowest priority, dialogs/cards/snackbars [m3 page].

### Variants / configurations [m3 page]
- Variants: Default; Toggle (selection) — Expressive only.
- Colour configs: elevated, filled (default), tonal, outlined, text (toggle not available in text).
- Sizes: XS, S (default), M, L, XL.
- Shapes: round (default), square.
- Small button padding: 16dp (Expressive) vs 24dp (legacy, not recommended).
- Width: hugs label by default; can be responsive (stretch to grid) [m3 page].

### Anatomy [m3 page]
1. Container 2. Label text 3. Icon (optional, leading; mirrored to trailing side in RTL).

### Measurements [tokens unless noted]
| Size | Height | Leading = trailing padding | Icon | Icon–label gap | Label role | Outline width (outlined) | Square radius | Pressed radius | Selected radius: round→ / square→ |
|---|---|---|---|---|---|---|---|---|---|
| XS | 32 | 12 | 20 | 4 | label-large | 1 | 12 | 8 | 12 / full |
| S | 40 | 16 (legacy 24) | 20 | 8 | label-large | 1 | 12 | 8 | 12 / full |
| M | 56 | 24 | 24 | 8 | title-medium | 1 | 16 | 12 | 16 / full |
| L | 96 | 48 | 32 | 12 | headline-small | 2 | 28 | 16 | 28 / full |
| XL | 136 | 64 | 40 | 16 | headline-large | 3 | 28 | 16 | 28 / full |
- Round corner = full at every size; pressed radius is shared by round and square [m3 page + tokens].
- Pressed corner-size animation: spring damping 0.6, stiffness 800 at all sizes [tokens].
- Min touch target: 48×48dp for XS and S [m3 page].
- Container width: dynamic to label; never narrower than label; min width n/s.
- Elevation: elevated = L1 (1dp) rest, L2 (3dp) hover, L1 focus/pressed, L0 disabled; filled & tonal = L0 rest, L1 hover; outlined/text = none [tokens].
- Legacy (deprecated sets): height 40, label-large, icon **18dp**, filled dragged elevation L3 (6dp) [tokens]. M2→M3 text says standard icon size "is now 20dp" [m3 page].
- Spacing between adjacent buttons: n/s on button page (see button groups).

### Typography
- Per size table above. Sentence case, single line [m3 page].

### Colour roles [m3 page table; confirmed in tokens]
| Style | Default (container / label+icon) | Toggle unselected | Toggle selected |
|---|---|---|---|
| Elevated | surface-container-low / primary | surface-container-low / primary | primary / on-primary |
| Filled | primary / on-primary | surface-container / on-surface-variant | primary / on-primary |
| Tonal | secondary-container / on-secondary-container | secondary-container / on-secondary-container | secondary / on-secondary |
| Outlined | outline: outline-variant; label on-surface-variant | same | container inverse-surface / inverse-on-surface |
| Text | label primary (no container) | — | — |
- Page labels the outlined stroke "Outline variant (outline)"; tokens resolve md.comp.button.outlined.outline.color = outline-variant.
- Other roles allowed if container↔text contrast ≥ 3:1 (e.g. tertiary / on-tertiary) [m3 page].
- Shadow colour = shadow [tokens].

### States [tokens + m3 page]
- Enabled, disabled, hovered, focused, pressed for every style (toggle adds selected/unselected sets).
- State layer colour = label colour of that style/selection; opacities 8% hover / 10% focus / 10% pressed.
- Disabled: container on-surface @ 10% (text & outlined: container invisible; outlined disabled outline = outline-variant); label & icon on-surface @ 38%; elevated drops to L0.
- Outlined and text containers are invisible at rest but take state layers/opacity like the others [m3 page].
- Focus indicator: secondary, 3dp, 2dp offset [tokens baseline set].

### Behaviour & motion
- Press: morph toward square (pressed radius table) [m3 page].
- Toggle select: round→square by default; square-resting toggles become round when selected [m3 page].
- Toggle iconography: outlined icon unselected → filled icon selected; if no filled glyph, increase weight [m3 page].
- Label may change between states but keep similar character count [m3 page].
- Web: modified motion curve for rapid clicks [m3 page].
- Optical centering of content in asymmetric shapes: Android `setOpticalCenterEnabled(true)`, off by default; shift ∝ difference between left and right corner sizes [mdc-android].

### Adaptive behaviour [m3 page]
- Choose position by window size: compact → filled buttons end-aligned below content; large → start-aligned beside content.
- Icon + label stay grouped and centered as width grows; never anchor them to opposite edges.
- Width can change per breakpoint, but constrain it (or place beside other elements) to avoid "long, flat buttons".
- Keep element order identical across screen sizes (screen reader / keyboard consistency).
- Platform: Android 200% font scale — labels should fit within two lines; if truncated, offer one-tap access to full content.

### Accessibility [m3 page]
- Contrast 3:1 vs background — measured on the container for elevated/filled/tonal, on the label for outlined/text.
- Keyboard: Tab focus; Space or Enter activates.
- Accessible name = visible label (may add context). Toggle buttons should expose selected state (implied by toggle semantics; explicit role guidance n/s).
- 48×48dp target for XS/S.

### Notable do / don't [m3 page]
- Do: label 1–3 words, sentence case; never wrap or truncate.
- Do: higher-emphasis style for the more important of paired actions (filled+text, filled+outlined, outlined+text); a single filled button for one important action.
- Don't: stack a button below another when they fit side-by-side; don't use two icons or vertically stacked icon/label.
- Caution: outlined buttons look like chips; outlined/text buttons on images/video lose legibility (use filled or a contrasting fill).
- Don't underline text buttons (use hyperlinked body text); in dialogs, trailing-align text buttons.
- Use elevated sparingly ("avoid overusing shadows").

---

## 2. Button groups

### Status
- **New in M3 Expressive (May 2025)** [m3 page]: standard and connected groups. "Connected button groups replace the segmented button", which is "no longer recommended". [mdc-android] says segmented is "deprecated".

### Purpose & when to use / not use [m3 page]
- Invisible container that adds padding between buttons/icon buttons and modifies their shape; contains no buttons by default.
- **Standard**: groups related key actions and adds interaction between adjacent buttons (selected/pressed button changes width/shape; neighbours flex). Example: Back / Pause / Next (high emphasis).
- **Connected**: select options, switch views, sort content (e.g. Walk/Bike/Drive; My files/Shared/Computers) — low emphasis; must use toggle buttons (single- or multi-select); avoid if nothing toggles.
- Avoid standard icon buttons or text buttons inside groups (no container treatment).

### Variants / configurations [m3 page]
- Variants: standard; connected.
- Sizes: XS, S, M, L, XL (applies to all buttons inside).
- Default shape: round or square (applied to all buttons).
- Selection: single-select, multi-select, selection-required.
- Colour: none of its own; children use button/toggle styles — filled, tonal, outlined, elevated.
- Common layouts: label buttons; label + icon buttons; XS icon buttons; L icon buttons.
- Resizing: **fixed** (manually set width narrow→wide, size, padding per breakpoint) or **flexible** (buttons grow/shrink until all flexible buttons hit max width).

### Anatomy
1. Container (invisible; not focusable).

### Measurements
| Size | Height | Standard gap between buttons | Connected gap | Connected inner corner (rest) | Connected inner corner (pressed) | Connected inner corner (selected) |
|---|---|---|---|---|---|---|
| XS | 32 | 18 | 2 | 8 [tokens] / 4 [m3 page caption] | 4 | 50% |
| S | 40 | 12 | 2 | 8 | 4 | 50% |
| M | 56 | 8 | 2 | 8 | 4 | 50% |
| L | 96 | 8 | 2 | 16 | 12 | 50% |
| XL | 136 | 8 | 2 | 20 | 16 | 50% |
- Values [tokens]; standard gaps confirmed by page caption (18/12/8/8/8) chosen "to ensure a minimum accessible target size of 48dp".
- Connected outer corners: round group = full [tokens]; square group outer corners XS 4, S 8, M 8, L 16, XL 20dp [m3 page].
- Standard group pressed-item width multiplier **15%**, spring damping 0.6 / stiffness 800 [tokens] (mdc `childSizeChange` 15% when pressed).
- XS and S connected groups: 48dp target areas and 48dp minimum width per button [m3 page].
- Density: groups adapt to button density (shown at 0, −1, −2, −3) [m3 page].
- mdc defaults: spacing 12dp (standard); connected = 2dp spacing, 8dp inner corners, fully rounded outer corners [mdc-android].

### Typography
- Inherited from contained buttons' size (see §1).

### Colour roles
- Inherit button/toggle-button colour roles. **Don't mix colour styles in a connected group** [m3 page].

### States [m3 page]
- Standard: enabled, disabled, hovered, focused, pressed; pressing changes width/shape of that button and adjacent ones; a selected toggle switches round↔square and colour per button specs.
- Connected: unselected (enabled, disabled, hovered, focused, pressed) and selected (enabled, hovered, focused, pressed); only the acted-on button changes shape.

### Behaviour & motion [m3 page]
- Standard: selected/activated button changes width, shape and padding, briefly changing widths of neighbours ("bounces against its adjacent button").
- Connected: no inter-button interaction; selected inner corners become fully round (50%).
- Selected buttons should change shape (round→square or square→round).
- Overflow: trailing buttons may collapse into an overflow menu at smaller breakpoints, overflow control at trailing end; buttons outside the group are unaffected.
- [mdc-android] `overflowMode` = none (clip/wrap text) | menu (auto overflow icon button + popup; don't use for toggle groups) | wrap (wrap to new lines) — note m3 page says groups "shouldn't wrap to a second line".

### Adaptive behaviour [m3 page]
- Single line; never wrap; stack multiple groups vertically if needed (groups don't interact vertically).
- Compact: smaller, narrower buttons so all fit; large/XL: larger, wider buttons.
- Don't stretch icon buttons beyond the "wide" setting when sizing manually.
- Preserve hierarchy across breakpoints (primary action stays largest/widest/most prominent).
- Standard group hugs its buttons; connected group spans the width of its surface (buttons widen); add a max width in larger windows.
- [mdc-android] adaptive via LinearLayout `layout_width` (fixed) / `layout_weight` (flexible) / mixed.

### Accessibility [m3 page]
- Each button ≥ 48×48dp target; don't reduce XS/S padding.
- Container not focusable; initial focus on first button.
- Keyboard: Tab to group/between buttons; Arrow keys within the group; Space/Enter select/activate.
- Container unlabeled; label each button per button/icon-button guidance; selection state must be identifiable.

### Notable do / don't [m3 page]
- Do keep all buttons in a standard group the same size and shape; vary width/colour for emphasis.
- Only mix sizes for "hero moments"; only mix shapes for selection or meaning.
- Use connected groups only when buttons are toggleable; don't mix colour styles there.
- Don't let groups wrap; collapse trailing items into overflow instead.

---

## 3. Split button

### Status
- **New in M3 Expressive (May 2025)** [m3 page]: "separate menu button that spins and changes shape when activated." [mdc-android]: "a special type of connected button group"; trailing button is checkable with animated icon.

### Purpose & when to use / not use [m3 page]
- A main action plus a menu of related actions (reduces visual complexity). High emphasis per All buttons (e.g. Send, Add, Create).
- Works alone or alongside buttons/icon buttons/button groups; may be larger than neighbouring buttons.
- Typically opens a menu, can open other components (e.g. cards); don't restyle the menu in unusual shapes.

### Variants / configurations [m3 page]
- One variant. Sizes XS, S (default), M, L, XL. Colours: elevated, filled, tonal, outlined (no text style).
- Leading button content: label + icon, label only, or icon only. Trailing button: always the expand/collapse (chevron) menu icon.

### Anatomy
1. Leading button 2. Icon 3. Label text 4. Trailing button.

### Measurements [tokens]
| Size | Height | Gap between halves | Inner corner (rest) | Inner corner hovered/pressed (focus per page) | Leading btn padding L/T | Trailing btn padding L/T | Trailing icon | Trailing width [derived] | Menu icon offset (unselected) [m3 page] |
|---|---|---|---|---|---|---|---|---|---|
| XS | 32 | 2 | 4 | 8 | 12 / 10 | 13 / 13 | 22 | 48 | −1dp |
| S | 40 | 2 | 4 | 12 | 16 / 12 | 13 / 13 | 22 | 48 | −1dp |
| M | 56 | 2 | 4 | 12 | 24 / 24 | 15 / 15 | 26 | 56 | −2dp |
| L | 96 | 2 | 8 | 20 | 48 / 48 | 29 / 29 | 38 | 96 | −3dp |
| XL | 136 | 2 | 12 | 20 | 64 / 64 | 43 / 43 | 50 | 136 | −6dp |
- Outer corners fully round (XS token expressed as 50%) [tokens]. Page confirms inner corners 4/4/4/8/12 and that the gap "should always be 2dp".
- Trailing button selected: inner corners → 50% (fully round) and the icon becomes centered [tokens + m3 page]; when unselected the icon is optically offset from center (table).
- Leading button icon size / label role / icon-label gap: n/s in split-button tokens; component shares button sizes, so presumably button size tokens apply (inference).
- Target: each half ≥ 48×48dp; XS/S need ≥ 48dp-tall target areas [m3 page].
- Menu offset from split button: **4dp** [m3 page].
- [mdc-android] default spacing 2dp; `buttonSizeChange` 0%.

### Colour roles [m3 page + tokens]
- Same colour sets as buttons (md.comp.button.elevated/filled/tonal/outlined). Unlike toggle buttons, colour does **not** change when the trailing button is selected — only a state layer (video caption: 10% state layer) is applied.
- [mdc-android] styles pair filled leading + filled trailing, or tonal leading + tonal trailing.

### States [m3 page]
- Leading: enabled, disabled, hovered, focused, pressed (+pressed with focus) — inner corners change on hover/focus/press.
- Trailing: same plus selected / selected-with-focus — inner corners change; icon centers when selected.
- Colours & state layers per button / icon-button specs.

### Behaviour & motion [m3 page]
- Trailing chevron rotates inward 180° on open/close; uses the **standard motion scheme** (not expressive) for this rotation; applies shape morph.
- Menu alignment: preferably aligned to the trailing button; else to either side of the leading/trailing button; may open above/below (6 alternative alignments) depending on breakpoint/scroll; always align to a button edge.
- RTL: whole component mirrors.
- [mdc-android] chevron animated via AnimatedVectorDrawable (`m3_split_button_chevron_avd`).

### Adaptive behaviour [m3 page]
- Scale up in large breakpoints, or use a larger size in compact windows for hero emphasis.

### Accessibility [m3 page]
- Focus order: leading → trailing (mirrors in RTL; may depend on OS settings).
- Keyboard: Tab between buttons; Space/Enter activates.
- Leading button label = visible label. Trailing button needs an expanded/collapsed state and a label conveying "more options" related to the main action (e.g. "More watch options" for "Watch later"). Label the opened menu per menu guidance.

### Notable do / don't [m3 page]
- Keep leading label to 1–2 words with a matching icon.
- Never replace or modify the trailing chevron (it rotates).
- Align the menu to the trailing button; keep a 4dp gap.
- Don't heavily customise the menu shape.

---

## 4. Floating action button (FAB)

### Status
- **Updated in M3 Expressive (May 2025)** [m3 page]: "new sizes to match the extended FAB and more color options. The small FAB is no longer recommended."
- Added medium FAB; FAB and large FAB unchanged; variants are size-based, not colour-based.
- Colour: added primary / secondary / tertiary styles; renamed former primary/secondary/tertiary to **primary/secondary/tertiary container** (values unchanged); **surface FABs no longer recommended**.
- Tokens: md.comp.fab.small "Not used in expressive FABs"; md.comp.fab.surface and md.comp.fab.branded "Not recommended"; combined size+colour sets (e.g. md.comp.fab.primary.large) are [Deprecated] → use size set + colour set [tokens].
- M2→M3: circle with shadow → boxier rounded square, dynamic colour, large FAB added [m3 page].

### Purpose & when to use / not use [m3 page]
- The most common/important, constructive action on a screen (Create, Compose, Favorite, Share, Start a process); appears in front of all content and persists while content scrolls.
- Not every screen needs one; never more than one per screen; individual components (cards) shouldn't have their own FAB.
- Don't use for minor/destructive/unclear actions (archive, trash, alerts, cut text, volume/font-colour controls better suited to a toolbar).
- Use extended FAB when a label is needed; use FAB menu when many related actions exist.

### Variants / configurations
- Sizes: FAB (56), medium FAB (80, most recommended), large FAB (96); small FAB (40) legacy.
- Colour styles (6): primary container (default), secondary container, tertiary container, primary, secondary, tertiary; surface (legacy).
- Elevation mode: default and "lowered" token variants [tokens] (lowered usage n/s on page).

### Anatomy
1. Container 2. Icon.

### Measurements [tokens]
| Size | Container | Corner radius | Icon | Padding around icon [derived] |
|---|---|---|---|---|
| FAB | 56×56 | 16 (large) | 24 | 16 |
| Medium FAB | 80×80 | 20 (large-increased) | 28 | 26 |
| Large FAB | 96×96 | 28 (extra-large) | 36 | 30 |
| Small FAB (legacy) | 40×40 | 12 (medium) | 24 | 8 |
- Elevation: L3 (6dp) rest, focus, pressed; L4 (8dp) hover. "Lowered": L1 rest/focus/pressed, L2 hover [tokens]. Page states caption: "Hovered (8% state layer) - elevation 4".
- Screen margin: 16dp (from FAB menu / extended FAB pages; FAB page measurement images uncaptioned) [m3 page].
- No pressed/selected shape-morph values for FAB: n/s.
- [mdc-android] elevation 6dp, hovered/focused translationZ 2dp, pressed translationZ 6dp.

### Colour roles [m3 page + tokens]
| Style | Container | Icon / state layer |
|---|---|---|
| Primary container (default) | primary-container | on-primary-container |
| Secondary container | secondary-container | on-secondary-container |
| Tertiary container | tertiary-container | on-tertiary-container |
| Primary | primary | on-primary |
| Secondary | secondary | on-secondary |
| Tertiary | tertiary | on-tertiary |
| Surface (legacy) | surface-container-high (+ surface-tint layer; lowered = surface-container-low) | primary |
- Rule: state-layer colour must equal icon colour for non-default mappings [m3 page]. (Token quirk: md.comp.fab.primary.focus/hover.icon.color reference on-primary-container while .icon.color is on-primary — treat on-primary as canonical.)

### States [m3 page + tokens]
- Enabled; hovered (8% layer, elevation L4); focused (10%); pressed (10%). No disabled state — **don't disable a FAB; hide it if unavailable** [m3 page].
- Focus indicator: secondary, 3dp, 2dp offset [tokens].

### Behaviour & motion [m3 page]
- Appearing: expands outward from a central point; icon may animate. Moves independently of content.
- Screen transitions: disappears and reappears during layout change; only reappears if relevant, ideally same position.
- Expanding: container transform into any surface (part of app structure or full screen); can transform into FAB menu.
- Scrolling: FAB stays in place; (extended FAB may collapse to FAB).
- Tabs: briefly disappears then reappears with new content; don't slide it with body content.
- [mdc-android] show() grows+fades in, hide() shrinks+fades out; in CoordinatorLayout shifts above Snackbars and hides when covered by AppBarLayout/BottomSheet.

### Adaptive behaviour [m3 page]
- FAB size: smallest, for compact windows with other actions; medium: compact & medium windows (default choice; "Use a medium FAB for mobile layouts"); large: any size but best expanded and larger ("large FAB for tablets and large screens").
- Placement: compact/medium → lower right (bottom trailing); expanded → upper left, e.g. within the navigation rail. Can be left/center/right aligned, above or nested in the navigation bar.
- Can transform into extended FAB on larger screens or into FAB menu.

### Accessibility [m3 page]
- Icon ≥ 3:1 contrast against container; container must stand out from background.
- Prioritise FAB in focus order (e.g. app bar → nav bar → FAB, skipping content).
- Tooltip on hover/focus (web) showing the label.
- Don't fully obscure another element's focus indicator (partial overlap OK).
- Keyboard: Tab to focus; Space/Enter default action.
- Accessible name describes the action ("Compose a new message"); [mdc-android] set contentDescription.

### Notable do / don't [m3 page]
- Use clear, simple, filled icons; no badges/notifications on the container.
- One FAB per screen; none on cards.
- Don't use for destructive or minor actions.
- Don't keep the FAB on screen while swiping between tabs.

---

## 5. Extended FAB

### Status
- **Updated in M3 Expressive (May 2025)** [m3 page]: three sizes small 56 / medium 80 / large 96 with larger type; "The baseline extended FAB is no longer recommended and should be replaced with the small extended FAB"; surface extended FAB not recommended.
- Tokens: `Extended FAB - Size - Baseline` (md.comp.extended-fab) → use md.comp.extended-fab.small; surface and branded colour sets "Not recommended" [tokens].
- M2→M3: same height as FAB, boxier shape, simpler elevation (M2 was pill-shaped) [m3 page].

### Purpose & when to use / not use [m3 page]
- Primary action where a label aids understanding or extra emphasis is needed; long scrolling views needing persistent access (checkout, publish, new task).
- Only one per screen; not as an option within a set of actions (use filled buttons instead).
- Not paired with floating toolbars (FABs can be; extended FABs can't); never opens a FAB menu.

### Variants / configurations
- Sizes: small, medium, large (+ baseline legacy). Colour styles: same 6 as FAB (primary container default…tertiary); surface legacy. With or without icon (label always required).

### Anatomy
1. Container 2. Label text 3. Icon (optional; leading, mirrored in RTL).

### Measurements [tokens]
| Size | Height | Corner | Icon | Icon–label gap | Leading / trailing padding | Label role |
|---|---|---|---|---|---|---|
| Small | 56 | 16 | 24 | 8 | 16 / 16 | title-medium |
| Medium | 80 | 20 | 28 | 12 | 26 / 26 | title-large |
| Large | 96 | 28 | 36 | 16 | 28 / 28 | headline-small |
| Baseline (legacy) | 56 | 16 | 24 | 12 | 16 / 20 | label-large |
- Width: hugs content (grows with text); baseline min width 80dp [m3 page table]; expressive min width n/s.
- Screen margins: 16dp [m3 page].
- Elevation: L3 (6dp) rest/focus/pressed, L4 (8dp) hover; lowered L1 [tokens]; page: "Hovered - elevation 4".
- [mdc-android] icon 24dp, icon padding 12dp (baseline), elevation 6dp, `collapsedSize`, `extendStrategy` wrap_content.

### Colour roles [m3 page + tokens]
- Container / label+icon: primary-container / on-primary-container (default); secondary-container / on-secondary-container; tertiary-container / on-tertiary-container; primary / on-primary; secondary / on-secondary; tertiary / on-tertiary. State layer = icon colour.

### States
- Enabled, hovered (elevation 4), focused, pressed; 8/10/10% layers [m3 page + tokens]. Disabled: n/s (don't disable — FAB a11y rule implies hide instead).

### Behaviour & motion [m3 page]
- Appearing: surface expands using enter/exit transition pattern.
- Expanding: container transform to any shape/surface.
- Scroll: collapses into a FAB on scroll down, re-extends on scroll up (FAB page: re-expands on reaching bottom). FAB→extended transition: shape changes, icon moves left, label fades in.
- [mdc-android] `extend()` / `shrink()` animate label; show/hide grow/shrink+fade.

### Adaptive behaviour [m3 page]
- Compact & medium: bottom of screen, centered or trailing-aligned.
- Expanded+: bottom-right edge (in **both** LTR and RTL) or at the top of the expanded navigation rail.
- Size: compact with one prominent action → large can be appropriate; larger breakpoints → medium or large.
- Responsive: transforms to FAB when space is limited (collapsed rail uses FAB; expanded rail uses extended FAB).

### Accessibility [m3 page]
- Prioritise in focus order; icon+label = one focusable element; no tooltip needed (visible label).
- Keyboard: Tab, Space/Enter.
- Accessible label must start with the same first word as the visible label ("Create" → "Create a new invite").
- Place in upper-left region (expanded nav rail) on large web screens; lower right in small windows; don't overlap actionable elements.

### Notable do / don't [m3 page]
- Label 1–2 words, never wrap/truncate; plan for localisation width.
- Icon-only extended FAB not allowed; label-only allowed.
- Don't place on toolbars, in the upper half of mobile screens, or on cards/dialogs/containers.
- Don't show multiple extended FABs; don't pair with a floating toolbar.

---

## 6. FAB menu

### Status
- **New in M3 Expressive (May 2025)** [m3 page]: "should replace the speed dial and any usage of stacked small FABs." M2 speed dial used small round FABs.
- [mdc-android]: not available as a native Views component — use Compose `FloatingActionButtonMenu` via interop.

### Purpose & when to use / not use [m3 page]
- Opens from a FAB to show 2–6 closely related actions (e.g. under "Share") floating on screen; keeps UI clean.
- Always opens from a FAB, in the FAB's place; never from an extended FAB or any other component.
- Don't use with a single item; don't group unrelated actions.
- Don't use when the FAB is paired with a floating toolbar or navigation rail.

### Variants / configurations
- One variant/size for all FAB sizes. Colour sets: primary, secondary, tertiary — match the FAB style (primary set ↔ primary or primary-container FAB, etc.) [m3 page].
- Web: rendered as FAB + standard menu component [m3 page].

### Anatomy
1. Close button 2. Menu item (list item: icon + label). 2–6 items.

### Measurements [tokens + m3 page]
| Element | Value |
|---|---|
| Close button | 56×56dp (always), shape full, icon 20dp, elevation L3 (6dp) |
| Gap close button ↔ items | 8dp |
| Menu item | height 56dp, shape full, icon 24dp, icon–label gap 8dp, leading/trailing 24dp, label title-medium |
| Gap between items | 4dp |
| Item elevation | L0 rest token; L4 hover, L3 focus/pressed |
- Items "share the same measurements as the medium button specs" [m3 page].
- Anchor: menu animates from the FAB's top trailing corner; close button occupies the FAB's position.
- Bottom margins: from FAB 16dp; from medium FAB the menu sits higher (40dp to screen bottom); from large FAB 56dp [m3 page].
- Window margins 16dp, increase to 24dp in large and extra-large windows [m3 page].
- Web: gap between FAB and menu varies; 4dp recommended [m3 page].
- All elements ≥ 48dp targets by default [m3 page].

### Typography
- Item label: title-medium.

### Colour roles [tokens]
| Set | Close button (container / icon) | Items (container / label+icon) |
|---|---|---|
| Primary | primary / on-primary | primary-container / on-primary-container |
| Secondary | secondary / on-secondary | secondary-container / on-secondary-container |
| Tertiary | tertiary / on-tertiary | tertiary-container / on-tertiary-container |
- State layer = icon colour; 8/10/10% [tokens]. "Contrasting close button and item colors" [m3 page].

### States
- Close button and items: enabled, hovered, focused, pressed [m3 page]. Web variant: enabled, hovered, selected.

### Behaviour & motion [m3 page]
- FAB transforms into the close button; items appear with enter/exit transition, originating from a trailing corner of the FAB (preferably top).
- Short windows (e.g. landscape phone): items scroll **behind** the close button; close button must stay unobstructed.
- Any item can container-transform into another surface (e.g. full-screen dialog).
- Don't fully obscure focus indicators of underlying elements.

### Adaptive behaviour [m3 page]
- Works at any window size; pair with the FAB size suitable for the window (larger FABs for larger windows).
- Stays anchored to the same corner/edge; trailing-aligned (left-aligned and mirrored in RTL).
- Large/XL windows: margins 24dp. Web/desktop: use menu component.

### Accessibility [m3 page]
- Initial focus stays on the close button (replaces FAB), then moves through items top to bottom.
- Keyboard: Tab next element; Space/Enter activate.
- Android: close button label "Toggle menu", role Button, state Expanded/Collapsed; items labelled with their visible text, role Button.
- Web: follow FAB + menu guidance; FAB's label describes the menu it opens.

### Notable do / don't [m3 page]
- Items always have labels; keep icons (removing them is "caution").
- Items hug content — no equal/fixed widths, no truncation.
- Don't change shapes (all elements fully rounded).
- Don't open from an extended FAB; don't combine with a toolbar or nav rail.

---

## 7. Icon buttons

### Status
- **Updated in M3 Expressive (May 2025)** [m3 page]: "wider variety of shapes and sizes, changing shape when selected. When placed in button groups, icon buttons interact with each other when pressed."
- Added sizes XS, M, L, XL; widths narrow/wide; square shape; press & select morph. Colour styles now configurations.
- Tokens: `Icon button (baseline)` md.comp.icon-button "not recommended" → use size set + colour set; md.comp.filled-icon-button / filled-tonal-icon-button / outlined-icon-button [Deprecated] [tokens].
- M2→M3: M2 "toggle buttons" became icon buttons with default and toggle variants [m3 page].

### Purpose & when to use / not use [m3 page]
- Compact, subtle actions with a clear system icon (Bookmark, Star, Print); default variant can open menus/search; toggle variant for binary on/off (favorite, bookmark).
- Placed on backgrounds or in cards, app bars, toolbars, button groups.
- Emphasis order: filled (highest; use sparingly) > tonal (secondary actions, e.g. "Raise hand") > outlined (medium, e.g. carousel arrows) > standard (lowest; or on colourful surfaces).
- Don't use toggle icon buttons for actions with no selected state (e.g. overflow menu).

### Variants / configurations [m3 page]
- Variants: default; toggle.
- Sizes: XS 32, S 40 (default), M 56, L 96, XL 136.
- Widths: narrow, default, wide. Shapes: round (default), square. Colours: filled (default), tonal, outlined, standard.

### Anatomy
1. Icon 2. Container.

### Measurements [tokens]
| Size | Height | Icon | Padding narrow / default / wide (each side) | Width narrow / default / wide [derived] | Square radius | Pressed radius | Outline |
|---|---|---|---|---|---|---|---|
| XS | 32 | 20 | 4 / 6 / 10 | 28 / 32 / 40 | 12 | 8 | 1 |
| S | 40 | 24 | 4 / 8 / 14 | 32 / 40 / 52 | 12 | 8 | 1 |
| M | 56 | 24 | 12 / 16 / 24 | 48 / 56 / 72 | 16 | 12 | 1 |
| L | 96 | 32 | 16 / 32 / 48 | 64 / 96 / 128 | 28 | 16 | 2 |
| XL | 136 | 40 | 32 / 48 / 72 | 104 / 136 / 184 | 28 | 16 | 3 |
- Round = full; selected: round→square radius, square→full [tokens + m3 page]; page corner table identical to buttons (12/12/16/28/28; pressed 8/8/12/16/16).
- Pressed corner spring 0.6 / 800 [tokens].
- Targets: XS and S must have ≥ 48×48dp targets in all widths [m3 page].
- Baseline (legacy) set: 40dp, icon 24dp, 40dp state layer [tokens].

### Colour roles [m3 page table = tokens]
| Style | Default (container / icon) | Toggle unselected | Toggle selected |
|---|---|---|---|
| Filled | primary / on-primary | surface-container / on-surface-variant | primary / on-primary |
| Tonal | secondary-container / on-secondary-container | same | secondary / on-secondary |
| Outlined | outline-variant stroke / on-surface-variant | same | inverse-surface / inverse-on-surface |
| Standard | no container / on-surface-variant | on-surface-variant | primary |
- Other roles OK at ≥ 3:1 contrast (e.g. tertiary) [m3 page].

### States [m3 page + tokens]
- Enabled, disabled, hovered (8%), focused (10%), pressed (10%), for default and toggle (unselected/selected).
- Disabled: container on-surface @ 10%; icon on-surface @ 38%; outlined disabled stroke outline-variant; outlined selected-disabled container on-surface @ 10%.
- Standard container invisible at rest; visible only via state layer.

### Behaviour & motion [m3 page]
- Press morph toward square; select morph round↔square.
- In a standard button group, adjacent icon buttons respond to presses (width morph).
- Toggle iconography: outlined → filled on select; if no filled glyph, semibold (bold if needed) so selection uses ≥ 2 properties, not colour alone.
- Hover (web): tooltip describing the action, not the icon name.

### Adaptive behaviour
- Use size/width for hierarchy (e.g. play/pause larger); equal importance → equal size [m3 page]. Breakpoint-specific rules: n/s (see button groups/toolbars for width use: no wide buttons in vertical toolbars).

### Accessibility [m3 page]
- Icon ≥ 3:1 vs surface/background.
- Target ≥ 48dp even when nested in other components.
- Don't apply density by default; user-selectable density must keep 48×48 CSS px targets.
- Keyboard: Tab focuses non-disabled buttons; Space/Enter activates.
- Label = action ("Add to favorites"); web tooltip carries the accessibility label. [mdc-android] always set contentDescription; default dims give a 48dp touch target via insets.

### Notable do / don't [m3 page]
- Default icon buttons use filled icons; toggles outlined (off) / filled (on).
- Use contained styles (filled/tonal/outlined) when separation from background is needed.
- Use only a few icon buttons at once; group many in a toolbar or button group.
- Don't use toggle style without a real selected state.

---

## 8. Segmented buttons (legacy)

### Status
- **"No longer recommended in the Material 3 expressive update… use the connected button group instead, which has mostly the same functionality but with an updated visual design"** [m3 page]. Token set `Segmented button - Outlined`: "This component is not recommended. Use connected button groups instead." [tokens]. [mdc-android] `MaterialButtonToggleGroup` "being deprecated".

### Purpose & when to use / not use [m3 page]
- Select options, switch views, sort elements among 2–5 choices; >5 or complex choices → chips.
- Single-select (radio-like; page implies a selection is required — "Unlike single-select, selection is not required" for multi) or multi-select (0–all). [mdc-android] exposes `singleSelection` and `selectionRequired`.

### Variants / configurations
- Single-select, multi-select. Segment content: icon, label, or both (don't mix icon-only and text segments).

### Anatomy [m3 page]
1. Segment 2. Container 3. Icon (optional) 4. Label text (optional) 5. Selected icon (checkmark).

### Measurements [m3 page + tokens]
| Attribute | Value |
|---|---|
| Height | 40dp |
| Container width | dynamic based on labels |
| Segment width | container width / number of segments |
| Outline width | 1dp |
| Shape | full |
| Left/right padding | min 12dp |
| Padding between elements | 8dp |
| Icon | 18dp |
| Target | 48dp |
| Density | height only; each step −4dp |

### Typography
- label-large (14/20 w500) [tokens].

### Colour roles [tokens + m3 page]
- Outline: outline. Unselected label/icon/state layer: on-surface. Selected container: secondary-container; selected label/icon/state layer: on-secondary-container.
- Disabled: label/icon on-surface @ 38%; outline on-surface @ 12%.

### States
- Unselected: enabled, disabled, hovered, focused, pressed. Selected: selected, hovered, focused, pressed. Layers 8% hover, 10% focus, 10% pressed [tokens].

### Behaviour & motion [m3 page]
- With icon + label, the icon is replaced by a checkmark when selected.

### Adaptive behaviour [m3 page]
- Keep margins from viewport edge; on large screens cap segment padding — don't span full width of large screens/panes.
- Can sit on bottom sheets / full-screen dialogs.

### Accessibility [m3 page]
- Tab to the component, arrows between segments; Space/Enter select/unselect.
- Outline ≥ 3:1 vs surface; selection shown by checkmark + colour (not colour alone).
- Initial focus on first segment (leftmost in LTR, rightmost in RTL) regardless of selection.
- Roles: single-select = radio group; multi-select = checkbox. Labels = visible text, or described meaning for icon-only ("Inexpensive" for "$").

### Notable do / don't [m3 page]
- 2–5 segments only; never wrap segments to a new line.
- Short, consistent labels; don't mix icon-only and text segments.
- Migration: map to connected button group (2dp gaps, per-button shapes, toggle buttons, same selection modes).

---

## 9. Toolbars (docked, floating) + bottom app bar (legacy)

### Status
- **M3 Expressive** [m3 page]: "The bottom app bar is no longer recommended and should be replaced with the docked toolbar, which functions similarly, but is shorter and has more flexibility. The floating toolbar was created for more versatility…"
- Token set `Bottom app bar (baseline)` → "For expressive, use md.comp.toolbar.docked and md.comp.toolbar.standard" [tokens]. [mdc-android]: bottom app bar "being deprecated".
- Compose: floating toolbar is a separate component from docked toolbar/bottom app bar [m3 page].

### Purpose & when to use / not use [m3 page]
- Actions related to the current page; can scale to show more actions on larger windows; add a menu when actions don't fit.
- **Docked**: full-width, global actions consistent across pages. **Floating**: floats over content, contextual/page-specific actions; can act as local navigation (tabs between related subsequent pages).
- Don't show at the same time as a navigation bar: nav bar on primary pages, toolbar on subsequent pages.
- Standard colour = low emphasis (focus on content); vibrant = high emphasis or temporary mode change (e.g. edit mode).

### Variants / configurations [m3 page]
- Variants: docked, floating (bottom app bar legacy).
- Colour: standard (default), vibrant.
- Floating layout: horizontal (default), vertical.
- Floating + FAB (fully supported in Compose; other platforms compose separately).
- Slots: icon buttons, buttons, text fields, images, custom components.

### Anatomy
1. Container 2. Elements/placed components (slots).

### Measurements [tokens + m3 page]
| Property | Docked | Floating |
|---|---|---|
| Height | 64dp | 64dp (horizontal); vertical width 64dp |
| Shape | none (square corners) | full (pill) |
| Leading/trailing internal padding | 16dp | 8dp |
| Spacing between items | min 4dp, max/default 32dp | 4dp |
| External margin | — (full width) | horizontal ≥ 16dp; vertical ≥ 24dp |
| Elevation | n/s (none in tokens) | L3 (6dp) |
| Container colour | surface-container (standard) / primary-container (vibrant) | same |
- Page: "By default all toolbars are 64dp high, center-aligned, have equal padding between items, and have a minimum outside padding of 16dp"; docked "32dp padding between items is just the default"; example center-aligned with 8dp between items.
- All elements need ≥ 48×48dp targets [m3 page].
- Floating toolbar + FAB [tokens]: gap 8dp; FAB 56×56, radius 16, icon 24, elevation L1 (1dp); medium FAB 80×80, radius 20, icon 28, elevation L2 (3dp).
- Bottom app bar (legacy) [tokens]: height 80dp (72dp "with-fab" token), surface-container, elevation L2 (3dp) + surface-tint, square. [mdc-android]: min height 80dp, elevation 3dp, FAB cradle margin 6dp / radius 4dp / vertical offset 12dp, end margin 16dp.

### Typography
- n/s for container; contained buttons use their own size roles.

### Colour roles [tokens; page captions noted]
| Role | Standard | Vibrant |
|---|---|---|
| Container | surface-container | primary-container |
| Icon/label (unselected) | on-surface-variant | on-primary-container |
| Icon-button container | surface-container | primary-container |
| Selected button container / content | secondary-container / on-secondary-container | surface-container / on-surface |
| Paired FAB | secondary-container / on-secondary-container | tertiary-container / on-tertiary-container |
| Disabled icon/label | on-surface @ 38% | on-surface @ 38% |
- Page captions: standard = surface container + filled button (primary/on-primary) + toggle tonal (secondary-container/on-secondary-container) + standard button "(Primary)"; vibrant = primary container + filled button (primary/on-primary) + toggle tonal (surface container/on-surface) + standard button (on-primary-container). Note the standard-button colour conflict (page primary vs token on-surface-variant).
- Consider alternative colour roles for more/less emphasis [m3 page].

### States
- Toolbar itself has no interaction; elements carry hover/focus/press (8/10/10%) and ripple [m3 page + tokens].

### Behaviour & motion [m3 page]
- Docked: stays on screen or animates off-screen on scroll.
- Floating: stays, animates off-screen, or collapses to a single high-emphasis action on scroll (Compose: collapse to FAB/key action). Don't both collapse and scroll off.
- Overflow: actions that don't fit go into an overflow menu in the trailing slot; revealed as breakpoints grow.
- Floating elevation may be removed when content beneath is visually distinct.
- [mdc-android] hide-on-scroll via `HideViewOnScrollBehavior` in CoordinatorLayout; **disabled when TalkBack is on**; `OverflowLinearLayout` for automatic overflow; floating toolbar defaults to system-window-inset margins.

### Adaptive behaviour [m3 page]
- Docked: always 100% width, bottom of window only (not with other bottom elements like a nav bar). Compact → evenly spaced items; medium+ → center all items, or center a key action and push others to edges. Web/large screens: may be rounded, placed elsewhere, use dividers for many items; shrink height/use XS buttons only if vertical space is tight.
- Floating: container only as wide as its items before hitting the 16dp margin; width may be capped; more actions revealed at larger sizes. Vertical toolbars for larger breakpoints, placed on either side (opposite the navigation rail, which should use its centered configuration); not recommended in compact windows.
- Multiple toolbars only in larger windows (e.g. undo/redo vs editing tools on opposite edges, styled differently); never in compact.
- RTL: mirror items; flip action order when order matters (e.g. "Next" stays trailing).

### Accessibility [m3 page + mdc-android]
- Initial focus on first interactive element; Tab or Arrows navigate; Space/Enter activate.
- Web: container role `toolbar`; mobile: generic container; children follow own guidance.
- Maintain access to controls when content scrolls/collapses (mdc disables hide-on-scroll under TalkBack; use accessibilityTraversalBefore/After to order focus).

### Notable do / don't [m3 page]
- Don't round docked toolbar corners (on mobile); don't overload with controls.
- Floating toolbar must stay fully on screen; use overflow instead of overflowing the window.
- Emphasise only one action at a time (filled icon button *or* FAB, not both); don't mix too many control styles.
- No square icon buttons in floating toolbars (fine in docked); no wide icon buttons in vertical toolbars.
- Don't show a toolbar with navigation controls alongside a navigation bar.
- Pair floating toolbars with FABs, not extended FABs; not with FAB menus.

---

## Source discrepancies & gaps (flag for design-system decisions)
1. **Connected button group XS inner corner**: page caption 4dp vs token `connected.xsmall.inner-corner.corner-size` 8dp (S/M also 8dp). mdc generic default 8dp.
2. **Toolbar standard icon-button colour**: page caption "Standard button (Primary)" vs tokens `toolbar.standard.icon.color = on-surface-variant`.
3. **Button icon size**: page "Differences from M2" says 20dp standard; deprecated per-style tokens still 18dp; Expressive size tokens XS/S 20dp.
4. **Bottom app bar elevation**: page M3 note says "no elevation or shadow"; tokens L2 (3dp) + surface tint; mdc default 3dp.
5. **Outlined stroke role**: page "Outline variant (outline)"; button/icon-button tokens = outline-variant; legacy segmented button = outline.
6. **FAB-in-floating-toolbar elevation** tokens (L1/L2) differ from standalone FAB (L3); intentional reduction not explained.
7. **FAB menu item elevation**: rest token L0 but hover L4 / focus & pressed L3.
8. **Token naming quirks**: md.comp.fab.primary and md.comp.extended-fab.primary contain both `focus.*`/`hover.*` (on-primary-container) and `focused.*`/`hovered.*` (on-primary) keys — legacy duplicates; on-primary is correct for the primary style.
9. **Wrapping**: m3 says button groups never wrap; mdc ButtonGroup offers `overflowMode=wrap`.
10. **Not specified anywhere in sources**: button minimum widths (Expressive), FAB/extended FAB press shape morph, split-button leading label typography (assumed = button sizes), docked toolbar elevation, toolbar item sizes, any XR guidance, explicit motion durations (only spring parameters given).
