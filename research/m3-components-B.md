# M3 / M3 Expressive component digest, group B (navigation, app bars, search, overlays)

Sources: m3.material.io pages (content API version 2026-09-23; page "Updated" stamps July 2026) = [m3 page]; resolved token tables (dsdb 38.2.9) = [tokens]; material-components-android docs = [mdc-android]; layout foundation pages = [m3 breakpoints] / [m3 scaffold]. "n/s" = not stated in any source. Many measurement diagrams on the m3 pages are images whose numbers are NOT in the alt text; where only a token gives the number, it is tagged [tokens]. Hex values in tokens resolve to a mixed Google baseline palette (e.g. primary #6750A4 in some tables, #0B57D0 in Tabs); design against the colour ROLE, not the hex.

System-wide values used below [tokens, SYSTEM]: state-layer opacity hover 0.08, focus 0.10, pressed 0.10, dragged 0.16; disabled content opacity 0.38; focus indicator thickness 3dp, inner offset -3dp, outer offset +2dp, colour usually `secondary`. Elevation level0 0dp, level1 1dp, level2 3dp, level3 6dp.

---

## Cross-cutting findings

- **Navigation model by window size class.** [m3 breakpoints] table: Compact (<600dp): navigation bar or modal expanded nav rail. Medium (600-839): navigation bar or modal expanded nav rail (component pages also allow the collapsed rail; single-pane → rail, two-pane → nav bar). Expanded (840-1199), Large (1200-1599), Extra-large (≥1600): modal or standard expanded nav rail (collapsed rail also allowed; "Use a navigation rail, either collapsed or expanded"); "An expanded navigation rail is best suited for extra-large windows". Swappable-component table: Compact nav bar → Medium collapsed rail → Expanded collapsed rail; Compact/Medium modal expanded rail → Expanded standard expanded rail. Never show a nav bar and rail at the same time [m3 page nav-rail].
- **Nav bar item orientation by class.** Vertical items (icon over label) in compact; horizontal items (icon beside label inside the pill) in medium [m3 page nav-bar]. mdc-android switches at ≥600dp [mdc-android]. Nav bar is "not intended for desktop".
- **Deprecations / "no longer recommended" in M3 Expressive (May 2025 unless noted).** The m3 pages say "no longer recommended"; mdc-android says "being deprecated"; old top-app-bar token sets are literally labelled "[Deprecated]".
  - Navigation drawer → use **expanded navigation rail** ("The navigation drawer is no longer recommended in the Material 3 Expressive update").
  - Baseline navigation rail → **collapsed navigation rail**; expanded rail "is meant to replace the navigation drawer".
  - Baseline navigation bar → **flexible navigation bar** (shorter, 64dp vs 80dp).
  - Medium and large app bars → **medium flexible / large flexible**; center-aligned app bar "Merged into small"; component renamed "top app bar" → "app bar".
  - Bottom app bar → **docked toolbar** ("The bottom app bar is no longer recommended and should be replaced with the docked toolbar") [m3 page toolbars].
  - Search "divided" style → **contained** style ("Not recommended. Use contained.") (Feb 2025).
  - Baseline menu is NOT deprecated: "still available", but **vertical menus** (Nov 2025) are "recommended for new designs".
  - Tabs, badges, tooltips, snackbar: no M3 Expressive update listed; still the M3 baseline specs.
- **Unified navigation colour model (Expressive).** Bar and rail share: active indicator `secondary-container` (full/pill shape), active icon `on-secondary-container`, active label `secondary` (changed from `on-surface-variant` in Expressive), inactive icon+label `on-surface-variant`, state layers `on-secondary-container` [tokens]. Horizontal (expanded-rail) items put the label inside the indicator, so the active label there is `on-secondary-container` [m3 page nav-rail].
- **Bold active label conflict.** mdc-android Expressive: "Label text is no longer bolded when selected" (nav bar and rail); Expressive tokens have no prominent-weight token. But the nav-bar Accessibility tab still says "Use a filled icon with a bold label for selected destinations". Baseline tokens use weight 700 for active labels. Decide explicitly.
- **App bars in Expressive.** Four variants (search app bar, small, medium flexible, large flexible); 1 action, 2 max; extra actions go in a **toolbar**, "Avoid placing an overflow menu in the app bar when possible"; optional single filled/tonal trailing icon button; subtitle and centered text on all; images/logos. On scroll: flat `surface` → `surface-container` fill (no drop shadow); medium/large flexible compress into small; optional transparent-on-scroll with filled icon buttons; app bar can hide on scroll.
- **Search in Expressive.** "Search bar and search view are now collectively named search". Contained style (persistent filled bar that stays visible inside focused search), bar widens on focus (side margins 24dp → 12dp), fast spatial spring (damping 0.6, stiffness 800). Focused-search layout: full-screen (compact default) vs docked (medium/expanded). New **search app bar** variant hosts it globally; opening it opens focused search.
- **Toolbars absorb actions.** App bars, search app bars and menus all redirect persistent or numerous actions to toolbars ("To show actions on screen at all times, use a toolbar instead").
- **Elevation tokens vs prose.** Prose says separation by tonal fill, not shadow (app bar on scroll, nav bar "No shadow" vs M2), yet tokens keep elevation values: app-bar on-scroll level2 (3dp), nav-bar container level2 (3dp), search bar level3 (6dp, while search page says "no shadow by default"). Treat elevation as tonal/stacking order; shadows only where prose asks (snackbar "solid background color with a shadow", menus, rich tooltip, modal expanded rail).
- **Text scaling.** Nav bar and nav rail must show full labels at up to 2x text size, growing vertically (wrap allowed, truncation only beyond 2x).
- **Timings stated.** Tooltips linger 1.5s after leaving target; snackbar auto-dismiss 4-10s (platform dependent), actionable snackbars never auto-dismiss; tab indicator animation 250ms "elastic" [mdc-android]; most other motion is described as named patterns (top-level transition, enter/exit) with no durations.
- **Predictive back (Android).** Applies to modal expanded nav rail and full-screen search; nav rail spec says it applies only to the modal expanded rail.
- **Touch targets.** 48x48dp is the stated floor (tabs: 48x48 CSS px, "avoid applying density by default"; menu slots 48x48dp; search avatar target 48dp; nav drawer items 48dp [mdc-android]); nav rail target spans the full rail width even when the indicator hugs content.

---

## 1. App bars (search app bar, small, medium flexible, large flexible)

### Status
- M3 Expressive update May 2025 [m3 page]: "Renamed component from top app bar to app bar"; "Added search app bar"; "Medium and large app bars are no longer recommended"; added medium flexible and large flexible with "Reduced overall height, Larger title text, Subtitle, Left- and center-aligned text options, Text wrapping, More flexible elements for imagery and filled buttons". Small gains subtitle, centered text, image and filled-button slots.
- Variant table [m3 page]: Search app bar (Expressive only); Small (both); Center-aligned: "Merged into small. Use centered-text configuration"; Medium (baseline) / Large (baseline): "Not recommended".
- Token sets "[Deprecated] Top app bar - Small / Medium / Large / Small, Center-aligned" → use `md.comp.app-bar` + size sets [tokens]. mdc-android: implemented as `MaterialToolbar` (search, small = "regular") and `CollapsingToolbarLayout` (medium/large flexible = "collapsing"); in `Material3Expressive` themes the existing medium/large styles are re-used with the flexible behaviour.
- Related: bottom app bar no longer recommended → docked toolbar [m3 page toolbars] (baseline bottom app bar 80dp, 72dp with FAB; docked toolbar 64dp [tokens Toolbars]).

### Purpose & when to use / not
- Describe the current page and provide 1-2 essential actions plus navigation (Back or Menu). "App bars should only have one action, two if necessary"; primary action alters/exits the page (Send, Save, Edit).
- Many actions → toolbar; avoid overflow menu in the app bar.
- Search app bar: "Use on home pages when search is key to the product". Small: "dense layouts or when a page is scrolled". Medium flexible: larger headline, collapses to small. Large flexible: emphasize the headline.
- Contextual action bar mode for selection exists on Android [mdc-android] (close button, contextual title, contextual actions, optional overflow).

### Variants / configurations
- Variants: search app bar, small, medium flexible, large flexible.
- Text alignment: leading edge (default) or centered (Expressive) for headline and subtitle.
- Optional: image/logo (replaces headline in small; sits above text in others), subtitle, single filled/tonal trailing icon button (default or wide size).
- Search app bar trailing layouts: (1) leading + one trailing outside search; (2) leading + trailing inside search + trailing outside; (3) leading + two trailing outside.

### Anatomy
- Small/flexible: 1 Container, 2 Leading button, 3 Trailing elements, 4 Headline, 5 Subtitle.
- Search app bar: 1 Container, 2 Leading icon button, 3 Hinted search text, 4 Trailing icon or avatar, 5 Search container.

### Measurements
| Variant | Container height | Headline type | Subtitle type | Source |
|---|---|---|---|---|
| Search app bar | 64dp (small set); search container 56dp, full (pill) shape | Body large (search label) | – | [tokens] |
| Small | 64dp | Title large (22/28) | Label medium (12/16) | [tokens] |
| Medium flexible | 112dp; 136dp with subtitle | Headline medium (28/36) | Label large (14/20) | [tokens] |
| Large flexible | 120dp; 152dp with subtitle | Display small (36/44) | Title medium (16/24) | [tokens] |
| Medium (baseline, not rec.) | 112dp | Headline small (24/32) | Label large | [tokens] |
| Large (baseline, not rec.) | 152dp | Headline medium (28/36) | Title medium | [tokens] |
- Flexible bars "hug the text contents, so they are taller when a subtitle is visible"; headline can wrap to two lines max in medium/large flexible [m3 page]. Exact heights for a wrapped two-line headline: n/s.
- Common [tokens]: icon 24dp; avatar 32dp; leading-space 4dp; trailing-space 4dp; icon-button-space 0dp; search leading-space 8dp, trailing-space 8dp; container shape corner none; elevation level0 flat, level2 (3dp) on scroll.
- Search container width: fills 100% of the space between leading and trailing elements until 312dp, then grows to fill only 50% of that space [m3 page].
- Trailing actions: max 2 icon buttons (+ avatar on search app bar) on mobile; up to 4 trailing icons on larger screens [m3 page].
- Padding diagrams: image-only; side margins/title insets n/s on m3. mdc-android: collapsing expanded-title margin 16dp; title-subtitle padding 0dp.
- Container must be full window width, square corners, never shorter than default height.

### Typography
- See table. Search label Body large [m3 page, tokens]. mdc-android `MaterialToolbar` subtitle default is `textAppearanceTitleMedium` and collapsed title `TitleLarge` (implementation defaults; prefer tokens).

### Colour roles
| Element | Role |
|---|---|
| Container (flat) | surface |
| Container (on scroll) | surface-container |
| Headline | on-surface |
| Subtitle | on-surface-variant |
| Leading icon | on-surface |
| Trailing icons | on-surface-variant |
| Search container (search app bar) | surface-container; on scroll surface-container-highest |
| Search label/hint | on-surface-variant |
- Source [tokens, m3 page]. On darker backgrounds the search container may use surface-bright; any custom pairing needs ≥3:1 between search text and container [m3 page]. Note: the Search component page specifies surface-container-high for a standalone search bar; the app-bar token uses surface-container.

### States
- Icon buttons follow icon-button states; touch ripple on tap; hover state on cursor; focus ring on keyboard focus [m3 page]. No disabled/dragged guidance specific to app bars (n/s).

### Behaviour & motion
- Scroll: starts same colour as background, fills with surface-container on scroll ("No drop shadow, instead a color fill") [m3 page]. Can stay pinned, or hide on scroll and reappear on reverse scroll.
- Medium/large flexible "can transform into small app bars" via the compress effect; "remain small until the page is scrolled back to the top". "Don't transform app bars into a search app bar."
- Transparent-on-scroll option: container stays transparent and actions become filled icon buttons; consider narrow icon buttons (e.g. Back).
- Search app bar: selecting the search bar opens search view / focused search.
- Can animate on/off together with another bar of controls (e.g. a row of chips).
- Resizing: trailing actions collapse into overflow at smaller widths and reappear at larger ones.
- mdc-android: `liftOnScroll` default true, lift colour `?attr/colorSurfaceContainer`; scroll flags `scroll|enterAlways|snap` for hide/reveal; `layout_scrollEffect="compress"`; collapsing bars use `scroll|exitUntilCollapsed|snap`. Durations n/s.

### Adaptive behaviour
- Always spans 100% of window width; RTL mirrors layout [m3 page].
- Search app bar: up to 2 trailing icons (+avatar) on mobile, up to 4 on large screens; search container sizing rule above.
- Scaffold: app bar occupies the top bar region (web/desktop) [m3 scaffold].

### Accessibility
- Initial focus: leading button. Keys: Tab = next interactive element; Space/Enter = activate.
- Title label = visible title text, add context if needed; role "Title". Icon buttons labelled per icon-button guidance; role "Button".
- Search bar/label ≥3:1 contrast.
- mdc-android: set `navigationContentDescription`, content descriptions on menu items and collapsing-bar images.

### Do / don't
- Do use one filled or tonal button for the key action; don't use multiple filled/tonal buttons.
- Don't round the container corners ("implies that the container can expand").
- Don't shrink below default height; don't wrap or truncate headlines in small bars (use medium/large flexible, max 2 lines).
- Search app bar text always includes "Search" (e.g. "Search inbox"); no more than two trailing icons with an avatar.
- Don't use a logo to open an expanded navigation rail.
- Place most-used action closest to the leading edge of the trailing group.

---

## 2. Navigation bar (flexible)

### Status
- May 2025 [m3 page]: "A new flexible navigation bar was introduced to replace the baseline navigation bar. It's shorter and supports horizontal navigation items in medium windows." Baseline: "Not recommended. Use flexible navigation bar." Colour: "Active label changed from on-surface-variant to secondary".
- Formerly "bottom navigation"; Android class remains `BottomNavigationView` [mdc-android].
- mdc-android Expressive deltas: height 80 → 64dp; top item padding 12 → 6dp; bottom 16 → 6dp; active indicator 64 → 56dp wide; label no longer bold when selected; horizontal items at ≥600dp (icon to start, content-based width with a max, item gravity centered).

### Purpose & when to use / not
- 3-5 top-level destinations of equal importance; mobile or tablet only; destinations consistent across screens; one destination always active.
- >5 destinations: don't use; use tabs within a page or a modal expanded nav rail behind a menu icon.
- <3 destinations: use tabs. Not for single tasks (e.g. viewing one email). Not for desktop (use rail or tabs).

### Variants / configurations
- Flexible navigation bar (only recommended variant). Item layout: vertical (default; compact) or horizontal (Expressive; medium).
- Baseline configurations: 3, 4 or 5 destinations.

### Anatomy
- 1 Container, 2 Icon, 3 Label text, 4 Active indicator, 5 Small badge (optional), 6 Large badge (optional), 7 Large badge label.

### Measurements
| Attribute | Flexible (Expressive) | Baseline | Source |
|---|---|---|---|
| Container height | 64dp | 80dp | [tokens] |
| Container shape / elevation | corner none / level2 (3dp) | none / level2 (3dp) | [tokens] |
| Icon | 24dp | 24dp | [tokens] |
| Vertical item active indicator | 56 x 32dp, full radius | 64 x 32dp, full | [tokens] |
| Vertical item icon-label space | 4dp | n/s (mdc 4dp) | [tokens] |
| Vertical item top/bottom padding | 6dp (token `item.vertical.container.between-space`; mdc top and bottom 6dp) | 12dp top / 16dp bottom (mdc) | [tokens], [mdc-android] |
| Horizontal item active indicator height | 40dp | – | [tokens] |
| Horizontal indicator leading/trailing padding | 16dp each | – | [tokens] |
| Horizontal icon-label space | 4dp | – | [tokens] |
| Space between items | 0dp | – | [tokens] |
| Badges | see Badges section | small 6dp, large 16dp | [tokens] |
- Width: 100% of window. Vertical items flex to equal widths; horizontal items have fixed (content) width, "extra space is added to the ends of the navigation bar instead"; horizontal items stay centred with the same spacing across medium/expanded, only outer padding changes [m3 page]. Exact horizontal item max width: n/s (mdc: "based on content with a max width").
- mdc-android: indicator horizontal margin 4dp; label padding 4dp; expanded (horizontal) indicator height 56dp, horizontal margin 20dp, start/end padding 16dp. (Token says 40dp horizontal indicator height; mdc 56dp is the rail-shared default. Prefer tokens.)

### Typography
- Label: Label medium (12pt/16, weight 500, tracking 0.1) for both vertical and horizontal items [tokens]. Baseline active label weight 700 ("label-medium.weight.prominent") [tokens]. Expressive: not bold (mdc) vs page a11y "bold label" (conflict, see cross-cutting).

### Colour roles
| Element | Flexible | Baseline |
|---|---|---|
| Container | surface-container | surface-container (page caption says surface) |
| Active indicator | secondary-container | secondary-container |
| Active icon | on-secondary-container | on-secondary-container |
| Active label | secondary | on-surface |
| Inactive icon / label | on-surface-variant | on-surface-variant |
| State layers (active and inactive) | on-secondary-container | on-surface |
| Badges | error / on-error | error |
- Source [tokens, m3 page]. Icons (active and inactive) need ≥3:1 vs container; don't use multiple or low-contrast colours.

### States
- Enabled, hovered (8% state layer), focused (10%), pressed (10%) [m3 page]. Baseline focus indicator: secondary, 3dp, inner offset -3dp [tokens].
- Hover (cursor): "active indicator appears in a reduced state". Tap: indicator appears in place, ripple passes through it, icon switches outlined → filled and changes colour.
- Disabled/dragged: n/s.

### Behaviour & motion
- Selecting an unselected item: top-level transition pattern; choose preserve-state (scroll, tab, in-line search) or reset-state per product.
- Re-selecting the active destination scrolls to top.
- No swiping between destinations.
- Scroll: can hide on scroll down, reveal on scroll up; don't hide when a screen reader is active.
- Selection animation: icon fills, indicator expands from the icon centre, "only apply on one axis". Durations n/s.
- Can be temporarily covered by dialogs, sheets, drawers, keyboard; never permanently obstructed. FAB sits above the bar, right-aligned; never overlaps it.
- Transition to rail on resize (video: horizontal items, then rail).

### Adaptive behaviour
- Compact: nav bar (vertical items) or modal (expanded) nav rail. Medium: nav bar (horizontal items) or nav rail; decide whether horizontal or vertical space matters more. Expanded and extra-large: use a navigation rail instead [m3 page]. Medium two-pane layouts: use nav bar so panes use full width [m3 breakpoints].

### Accessibility
- Initial focus: first nav item. Tab moves between items; Space/Enter selects.
- Label = destination name; more descriptive a11y label where ambiguous ("Library" → "Music library"). "On Android Views (MDC-Android), a more descriptive accessibility label is not available and the role is not announced."
- Text scaling: grow vertically, keep padding; full label visible up to 2x; may wrap; truncate beyond 2x.
- Selected cue: filled icon (or semibold weight if no filled version) + indicator + colour.
- mdc `labelVisibilityMode` AUTO hides inactive labels at ≥4 items; the m3 page says don't remove labels.

### Do / don't
- Don't exceed 5 or go below 3 destinations; don't remove labels; labels 1-2 words, never wrap/truncate/shrink.
- Use the active indicator only on the active destination.
- Don't use horizontal items in compact windows (they overflow); don't scroll or reorder destinations.
- Don't combine with another primary navigation component (rail, drawer).
- Badges overlap the icon in both vertical and horizontal items.

---

## 3. Navigation drawer (no longer recommended)

### Status
- Every tab carries: "The navigation drawer is no longer recommended in the Material 3 Expressive update. For those who have updated, use an expanded navigation rail, which has mostly the same functionality of the navigation drawer and adapts better across breakpoints." [m3 page]. Token set "Navigation drawers (baseline)": "For expressive, use the expanded nav rail instead `md.comp.nav-rail.expanded`" [tokens]. mdc-android: "being deprecated".
- Spec retained for legacy; the expanded nav rail's modal/standard configurations are the replacement for modal/standard drawers.

### Purpose & when to use / not (legacy guidance)
- 5+ top-level destinations; 2+ levels of hierarchy; quick navigation between unrelated destinations; replacing rail/bar on large screens.
- Don't pair with another primary navigation component (e.g. nav bar).

### Variants / configurations
- Standard (beside content; permanently visible or dismissible via menu icon) and Modal (scrim, opened by an outside action). Bottom drawer shape token exists (top corners 16dp) [tokens].

### Anatomy
- Specs: 1 Container, 2 Headline, 3 Label text, 4 Active indicator, 5 Badge label text, 6 Scrim, 7 Icon. Guidelines add: Sheet, Divider, Section label (optional). "Essentially a list contained within a side sheet."

### Measurements
| Attribute | Value | Source |
|---|---|---|
| Container height | 100% | [m3 page, tokens] |
| Container width | 360dp | [m3 page, tokens] (mdc `maxWidth` default 280dp) |
| Container shape | 0,16,16,0dp (large-end corners) | [m3 page, tokens] |
| Icon | 24dp | [m3 page] |
| Active indicator | 336 x 56dp, 28dp radius (full) | [m3 page, tokens] |
| Left/right padding | 28dp | [m3 page] |
| Active indicator padding | 12dp | [m3 page] |
| Padding between elements | 0dp | [m3 page] |
| Elevation | standard level0; modal level1 (1dp) | [tokens] |
| Scrim | neutral-variant20 @ 0.4 opacity | [tokens] |
- mdc-android: item shape insets 12dp; item horizontal padding 28dp; item vertical padding 4dp; icon padding 12dp; subheader insets 28dp; drawer corner 16dp; touch targets 48dp.

### Typography
- Label: Label large (14/20, weight 500); active label weight 700; headline/section label: Title small (14/20, 500); large badge label: Label large [tokens].

### Colour roles
- Container: standard surface; modal surface-container-low [tokens]. Active indicator secondary-container; active icon/label on-secondary-container; inactive icon/label on-surface-variant; headline on-surface-variant; divider outline; inactive hover/focus content on-surface; scrim (see above) [tokens, m3 page].

### States
- Enabled, hovered, focused, pressed; state layers on-secondary-container (active) / on-surface (inactive hover/focus), opacities 0.08/0.10/0.10; focus indicator secondary 3dp [tokens].

### Behaviour & motion
- Drawer contents scroll independently. Dismissible standard (menu icon toggles) vs permanently visible standard. Modal dismissed by selecting an item, tapping scrim, or swiping toward anchoring edge. Enter/exit transition pattern; predictive back [mdc-android]. Durations n/s.
- Rail → drawer transformation when switching portrait → landscape (legacy guidance).

### Adaptive behaviour (legacy)
- Standard: expanded, large, extra-large. Modal: any, mainly compact/medium. Web <320 CSS px: swap drawer for nav bar. Large/XL web: standard drawer or rail that transitions into a modal drawer.

### Accessibility
- Initial focus first item; Tab lands on first destination; Arrow keys move between destinations; Space/Enter selects and moves focus to opened section. Scrim selectable to close. Role shown as "tab" in examples; Android Views can't set descriptive labels or announce role.

### Do / don't
- Full-width dividers between groups only; icons for all or none; truncate rather than wrap or shrink labels; filled icon for selected.

---

## 4. Navigation rail (collapsed, expanded: standard / modal / hide-when-collapsed)

### Status
- May 2025 [m3 page]: "A collapsed and expanded navigation rail have been introduced to replace the baseline nav rail. The expanded nav rail is meant to replace the navigation drawer." Baseline rail: "Not recommended. Use collapsed navigation rail." Active label on vertical items changed on-surface-variant → secondary.
- mdc-android Expressive deltas: width 80 → 96dp; item min height 60 → 64dp; item spacing 0 → 4dp; elevation 0 → 3dp (tokens say level0 for collapsed/standard; level2 only for modal expanded); top item padding 4 → 6dp; bottom item padding 12 → 4dp; content top margin 8 → 44dp; header-to-items padding 8 → 40dp; label no longer bold. mdc-android lists only the non-modal expanded configuration.

### Purpose & when to use / not
- Medium, expanded, large, extra-large windows; 3-7 destinations plus optional FAB; same place on every screen.
- Collapsed: leading edge, 3-7 items, "should not be hidden". In medium windows with few destinations consider a nav bar; "Compact windows should always use a navigation bar" (the modal expanded rail is the compact overflow option).
- Expanded: always opened from a menu icon; can show secondary destinations. Standard = beside content (larger windows). Modal = overlaps content (dense layouts, many items). Can be hidden entirely in immersive experiences (expanded only).

### Variants / configurations
| Category | Configuration |
|---|---|
| Variant | Collapsed; Expanded |
| Expanded layout | Standard (default, non-modal); Modal |
| Expanded behaviour | Transition to collapsed rail; Hide when collapsed |
| Item alignment | Top or centre group (centre recommended on tablets); menu and FAB always top-aligned |
| Common layouts | items only; + menu; + FAB; + menu + FAB |

### Anatomy
- Specs: 1 Container, 2 Menu (optional), 3 FAB or Extended FAB (optional), 4 Icon, 5 Active indicator, 6 Label text, 7 Large badge (optional), 8 Large badge label (optional), 9 Small badge (optional). Guidelines list active/inactive icon and label separately; optional divider.

### Measurements
| Attribute | Collapsed | Expanded | Source |
|---|---|---|---|
| Container width | 96dp (narrow option 80dp) | min 220dp, max 360dp | [tokens] |
| Container colour / elevation / shape | surface / level0 / none | standard: surface / level0 / none; modal: surface-container / level2 (3dp) / 16dp (corner large) | [tokens] |
| Top space (to first element) | 44dp | 44dp | [tokens] |
| Item container height | 64dp (short 56dp) | 64dp (short 56dp) | [tokens] |
| Item layout | vertical (icon over label) | horizontal (icon beside label) | [tokens] |
| Active indicator | 56 x 32dp, full | height 56dp, hugs content; 16dp leading/trailing padding | [tokens] |
| Icon-label space | 4dp | 8dp | [tokens] |
| Space between items | 4dp (collapsed item vertical space) | 0dp | [tokens] |
| Item vertical padding | 6dp (token `item.container.vertical-space`); mdc: top 6dp, bottom 4dp | n/s | [tokens], [mdc-android] |
| Vertical item leading/trailing | 16dp | – | [tokens] |
| Expanded vertical trailing space | – | 20dp | [tokens] |
| Header to items (minimum) | 40dp | 40dp | [tokens] |
| Icon | 24dp | 24dp | [tokens] |
| Baseline (not rec.) | 80dp wide; indicator 56 x 32dp; no-label indicator 56dp tall; badge 6dp / large 16dp | – | [tokens] |
- Target area spans full rail width even when the item container/indicator hugs content [m3 page]. Optional override: stretch indicator to fill width to resemble the old drawer.
- FAB in rail rests at elevation level0; FAB → extended FAB when the rail expands.

### Typography
- Vertical (collapsed) labels: Label medium (12/16, 500). Horizontal (expanded) labels: Label large (14/20, 500) [tokens]. Baseline: Label medium, active weight 700. Section headers in expanded rail: n/s.

### Colour roles
| Element | Role |
|---|---|
| Container | surface (fill optional; if removed keep ≥3:1 item contrast); modal expanded surface-container |
| Active indicator | secondary-container |
| Active icon | on-secondary-container |
| Active label | secondary (vertical); on-secondary-container (horizontal) |
| Inactive icon, label | on-surface-variant |
| State layers | on-secondary-container |
| Badges | error / on-error |
| Menu icon (baseline tokens) | on-surface-variant; on-surface on hover/focus/press |
- Source [tokens, m3 page]. "Don't use more than two colors for destinations."

### States
- Enabled, hovered, focused, pressed; hover 0.08, focus 0.10, pressed 0.10 [tokens]. Disabled/dragged n/s.

### Behaviour & motion
- Menu button toggles collapsed ↔ expanded; the menu icon changes to signal "collapse" when expanded. Content beside a standard rail resizes automatically; the FAB morphs into an extended FAB; extra destinations can appear.
- mdc-android: `expand()`/`collapse()`; collapsed shows only non-submenu items up to 7; expanded shows all (submenus); animated with a ChangeBounds transition that also shrinks adjacent content. Durations n/s.
- Scrolling: destinations stay fixed on vertical scroll. With horizontal scrolling content the rail may scroll off or stay fixed; distinguish with a divider or elevation level1.
- Selection: top-level transition; icon fills; indicator expands from icon centre.
- Predictive back: only the modal expanded rail; rail "pops off the edge of the window".
- Hidden expanded rail: body fills the space as long as the menu icon stays accessible.

### Adaptive behaviour
- Compact: no standard (collapsed) rail; nav bar; modal expanded rail for overflow. Medium: rail (esp. when persistent vertical nav matters more than vertical space), or nav bar; more than 5 destinations → modal expanded rail. Expanded-XL: rail, not nav bar; standard vs modal by horizontal space and destination count [m3 page].
- Breakpoints page: rail collapsed by default on mobile; can be open by default on expanded+; "An expanded navigation rail is best suited for extra-large windows"; collapse when space is needed or deeper in hierarchy; rail can be hidden on secondary destinations if Back reaches the primary. In split-pane layouts nav + first pane = 50% of window. Extra-large with a third (side-sheet) pane: the expanded rail can stay, collapse, or hide [m3 breakpoints].
- Placement: outside panes, always on the leading edge (left LTR, right RTL); never horizontal; tabs may be used alongside for an extra level. XR: rail can float as an orbiter [m3 scaffold].

### Accessibility
- Initial focus: first interactive item (menu, FAB, or first nav item). From FAB/menu, Tab reaches items; Tab or Arrows move between items; Space/Enter selects.
- Label = adjacent text; more descriptive if ambiguous ("Recent" → "Recent images"); Android Views can't.
- Text scaling to 2x: items grow vertically; wrap allowed.
- Filled icon for selected (semibold if none); sufficient contrast for both states.

### Do / don't
- Top-align the FAB (not below items); don't use a logo as the expand button or one that looks like an action.
- One-word labels; break long phrases onto two lines or hyphenate; never truncate or shrink type.
- Active indicator on one item only; don't make the rail horizontal; never show rail and nav bar together.
- Badges: on icon's upper-right in collapsed rail; next to the label in expanded rail.

---

## 5. Tabs (primary, secondary)

### Status
- Baseline M3; no Expressive update on the page. M2 → M3: new colour mapping; icons and labels vertically centred.

### Purpose & when to use / not
- Organise related content at the same hierarchy level; peers side by side; can scroll horizontally for many tabs.
- Primary tabs: top of content pane under an app bar, main content destinations. Secondary: within a content area, for a second level (always below primary).
- Not for sequential content (chapters). Not as primary app navigation (nav bar page: fewer than 3 destinations → use tabs; for distinct pages use navigation, tabs for related content within a page).

### Variants / configurations
- Primary; Secondary. Fixed vs scrollable. Label only; icon + label (stacked or inline); with badges.

### Anatomy
- Primary: 1 Container, 2 Badge (optional), 3 Icon (optional), 4 Label, 5 Divider, 6 Active indicator. Secondary: same minus icon in the spec image (tokens include optional icon).

### Measurements
| Attribute | Value | Source |
|---|---|---|
| Container height, label only | 48dp | [m3 page, tokens] |
| Container height, icon + label | 64dp | [m3 page, tokens] (mdc: 72dp for stacked icon+text) |
| Icon | 24dp | [m3 page] |
| Divider height | 1dp (inside container height) | [m3 page] |
| Primary indicator height | 3dp | [m3 page] |
| Secondary indicator height | 2dp | [m3 page] |
| Indicator shape | 3, 3, 0, 0 (top corners rounded) | [m3 page, tokens] |
| Primary indicator | inset 2dp each side, min length 24dp | [m3 page] |
| Inline icon-text gap | 8dp | [m3 page] |
| Inline text-badge gap | 4dp | [m3 page] |
| Badge overlap on stacked icon | 6dp | [m3 page] |
| Scrollable: first tab offset | 52dp from leading edge | [m3 page] |
| Elevation | level0 | [tokens] |
- Fixed tabs: equal sections; max tab width = widest tab; group uses fluid margin, aligned to centre or leading edge; avoid more than 4 fixed tabs. Scrollable tab width = label length, consistent padding.
- mdc-android: tab padding 12dp start/end; min width 72dp (scrollable); max width 264dp; indicator 2dp default height.

### Typography
- Label: Title small (14/20, weight 500) for both variants [tokens].

### Colour roles
| Element | Primary | Secondary |
|---|---|---|
| Container | surface | surface |
| Active label / icon | primary | on-surface |
| Active indicator | primary | primary |
| Inactive label / icon | on-surface-variant | on-surface-variant |
| Hover/focus/pressed content (inactive) | on-surface | on-surface |
| State layer | active: primary; inactive hover/focus: on-surface; inactive pressed: primary | on-surface |
| Divider | outline-variant (page) / surface-variant (token) | same |
| Focus indicator | secondary, 3dp, inner offset -3dp | same |
- Source [m3 page, tokens].

### States
- Enabled, hover (0.08), focused (0.10), pressed (0.10) for active and inactive tabs [tokens]. Disabled/dragged n/s.

### Behaviour & motion
- Fixed tabs: tap or swipe content left/right. Scrollable: swipe the tab row. Indicator "shifts into position" on selection; mdc-android: elastic animation mode, 250ms.
- Vertical scroll: tabs stay pinned or scroll off and return on scroll up; when attached to an app bar they move as one unit (don't scroll tabs behind the app bar).
- Avoid other swipeable content (maps, swipe-to-delete lists) in the tab content area.

### Adaptive behaviour
- Container spans full window width; fixed tabs grow with width; >4 tabs gets cramped → scrollable. On expanded+ windows, tabs used inside panes for sorting/filtering/secondary navigation [m3 breakpoints].

### Accessibility
- Arrow keys move focus between tabs (Tab also mentioned); Space/Enter activates; "Don't use Space/Enter for navigating tabs".
- Don't loop scrollable tabs infinitely (traps screen-reader users).
- Targets ≥48x48 CSS px; don't apply density by default.
- Icon-only tabs need descriptive labels ("Video format media content").

### Do / don't
- Icons and labels on all tabs or none; don't truncate unless required; labels may use a second line with truncation; badges max 4 characters incl. "+", cleared once viewed.
- Use globally recognised icons for icon-only tabs.

---

## 6. Search (search bar + focused search / search view)

### Status
- Expressive update (Feb 2025) [m3 page]: renamed (search bar + search view = "search"); styles contained (recommended) or divided (baseline, "Not recommended. Use contained."); gaps can group results; "The search bar grows wider when focused". Supported platform listed: Jetpack Compose. I/O 2026 page: expressive search available for Compose.
- mdc-android Expressive: centered text attribute, max width, lift-on-scroll colour, padding updates; contained SearchView where the bar "persists visually"; "bouncy" animation only with Expressive themes, otherwise linear. Recommended to host `SearchBar` inside `AppBarLayout` (AppBarWithSearch overlay, centred text default).

### Purpose & when to use / not
- Products with many items (files, messages). Entry points: search bar (search a specific view), search app bar (search is primary/global), search icon button (secondary action).
- Focused search can be a standalone destination from a nav bar item.

### Variants / configurations
| Category | Configuration |
|---|---|
| Style | Contained (Expressive, recommended); Divided (baseline, divider between bar and results) |
| Focused layout | Full-screen; Docked |
| Trailing elements | avatar; 1 icon button; 2 icon buttons; icon button + avatar |
| Text | start-aligned (spec); centered (mdc-android Expressive style) |
| Results | lists; gaps to group; category labels, avatars rows, filter chips |

### Anatomy
- 1 Search bar container, 2 Leading icon, 3 Supporting (hinted) text, 4 Trailing icon and avatar (optional), 5 Input text, 6 Container for suggestions/results (empty by default; use lists). Divided style adds a divider.

### Measurements
Search bar (unfocused):
| Attribute | Value | Source |
|---|---|---|
| Width | min 360dp, max 720dp | [m3 page] |
| Height | 56dp | [m3 page, tokens] |
| Shape | full (pill) | [tokens] |
| Outer margins | unfocused 24dp, focused 12dp | [m3 page, tokens] |
| Leading icon to label (from tap target) | 4dp | [m3 page, tokens] |
| Label to trailing icon (from tap target) | 4dp | [m3 page] |
| Avatar | 30dp, circular; target 48dp | [m3 page, tokens] |
| Icons | 24dp | [tokens] |
| Inner leading/trailing space (contained, with actions) | 4dp; no actions 16dp | [tokens] |
| Trailing actions gap | 0dp | [tokens] |
| Elevation | level3 (6dp) in token; page says "Lower elevation and no shadow by default" | [tokens], [m3 page] |

Focused search, contained style:
| Attribute | Value | Source |
|---|---|---|
| Full-screen container | full width x full height | [m3 page] |
| Docked container | width min 360 / max 720dp; height min 240dp, max 2/3 of screen height | [m3 page] |
| Search bar in view | 56dp tall, pill | [m3 page, tokens] |
| Leading / trailing padding | 16dp (page); contained margins 12dp (tokens) | [m3 page, tokens] |
| Docked bar-to-results gap | 2dp | [tokens] |
| Docked results shape | 12dp (corner medium) | [tokens] |
Divided/baseline view [tokens]: full-screen header 72dp, docked header 56dp, docked container 28dp radius (extra-large), full-screen corner none, leading/trailing 16dp, icon-label 16dp, divider outline.

### Typography
- Hint (supporting) text and input text: Body large (16/24) [tokens].

### Colour roles
| Element | Role |
|---|---|
| Search bar container | surface-container-high |
| Full-screen focused background | surface-container-low (contained) |
| Docked results container | surface-container-high |
| Leading icon, input text | on-surface |
| Hint text, trailing icons | on-surface-variant |
| Lift-on-scroll colour | surface-container-highest [mdc-android] |
| Divider (divided) | outline |
| Focus indicator | secondary, 3dp, outer offset 2dp |
- Source [m3 page, tokens]. Don't put surface-container-high on a surface-container background; keep container roles more than one step apart.

### States
- Bar: enabled, hovered (on-surface 0.08), focused, pressed (ripple, on-surface 0.10). Results use list-item states. In focused search each element keeps its own states.

### Behaviour & motion
- Selecting the entry point opens focused search; may show history before typing, live suggestions while typing, or wait for a query. Back icon releases focus, dismisses results, restores the bar. Optional clear (x) icon.
- Contained style: bar keeps the same shape focused/unfocused; widens (margins 24 → 12dp); motion spring `fast.spatial` = damping 0.6, stiffness 800 (Expressive), 0.9/1400 (standard) [tokens].
- Results scroll beneath the bar; executed query text stays visible but unfocused.
- Scroll: bar scrolls away and returns on scroll up, or stays fixed; mdc-android adds lift-on-scroll mode.
- Predictive back: search detaches from the screen edge, previous screen previewed.
- mdc-android: sibling icon buttons animate off-screen as the bar expands; standalone view uses slide up/down; recommended `windowSoftInputMode=adjustNothing`; keyboard auto-shows by default.

### Adaptive behaviour
- Full-screen layout default for compact; docked best for medium and expanded; swap automatically on resize. Bar stays in its pane, scales width, internal elements anchor left/right.

### Accessibility
- Hint text = accessibility label; role Text field (Android) / Search field (iOS).
- Initial focus: leading icon button, else the text field. Tab/Shift+Tab between elements; Space/Enter activates the field; Arrows move through results.
- Announce suggestions/results when they appear; focused search needs a status indicator ("Results", search icon). Results are lists (announced as lists).
- mdc-android `SearchView` makes siblings unimportant for accessibility while shown.

### Do / don't
- Max two trailing icons; avatar + at most one other icon.
- Leading side: navigational icon button or non-functional search icon.
- Hint text short and specific ("Search your messages").
- Use gaps (not dividers) in contained style to group results.

---

## 7. Badges (small, large)

### Status
- Baseline M3; no Expressive update. M2 → M3: new colour mappings only.

### Purpose & when to use / not
- Notification, count or status on a navigation destination or icon; used in nav bar, nav rail, app bars, tabs (also menu items).
- Small badge = unread/new indicator (shape only); large badge = count/status label.
- In nav bars, hide the badge once the destination is selected (unread case).

### Variants / configurations
- Small; Large (1-4 characters incl. "+", e.g. "999+"). Configurations shown on active/inactive items with and without labels, nav bar vs rail.

### Anatomy
- 1 Small badge, 2 Large badge container, 3 Large badge label (+ max-character container/label).

### Measurements
| Attribute | Value | Source |
|---|---|---|
| Small badge | 6 x 6dp, 3dp radius (full) | [m3 page, tokens] |
| Large badge, one digit | 16 x 16dp, 8dp radius (full) | [m3 page, tokens] |
| Large badge, max characters | 16 x 34dp | [m3 page] |
| Small: icon top-trailing corner → badge bottom-leading corner | 6 x 6dp | [m3 page] |
| Large: same offset | 14 x 12dp (H x W) | [m3 page] |
| Large: horizontal label padding | 4dp | [m3 page] |
- Anchored inside the icon bounding box at the upper trailing edge; width grows with count, placement stays. Mirror for RTL.

### Typography
- Large badge label: Label small (11pt/16, weight 500, tracking 0.1) [tokens].

### Colour roles
- Container error; label on-error [tokens, m3 page]. Custom roles need ≥3:1.

### States
- No interactive states (badge is non-interactive). Hidden after selection when indicating unread.

### Behaviour & motion
- Disappears on selection (video); count updates dynamically. Durations n/s.

### Adaptive behaviour
- Rail: large badge fine (no collisions); expanded rail puts badge next to the label. App bars: prefer small badges (tight space, won't hit screen edge). Tabs/inline: put a large badge at the trailing edge, not over icon+text.

### Accessibility
- Read after its destination; numbers read out; non-count badges announce "New notification". mdc-android: content-description setters for text, quantity plurals, exceeds-max and numberless.

### Do / don't
- Use default colours; don't move badges arbitrarily or place over the icon; truncate counts with "+" rather than letting the badge clip or collide; max 4 characters.

---

## 8. Menus (vertical menus, baseline menu)

### Status
- November 2025 [m3 page]: "Vertical menus were introduced with new shapes, color styles, selection states, and refined submenu motion. Gaps can be used for a more flexible layout on Android." Vertical menus "recommended for new designs"; "Baseline menu is still available" (not deprecated, but lacks new shapes/colours/selection/motion). I/O 2026: "Expressive lists and menus" on Android. mdc-android doc still documents only baseline dropdown/exposed dropdown/popup/context menus.
- Platform gaps: "Gaps are not currently available on web"; "Submenus are not currently available on Jetpack Compose".
- Tokens also define `md.comp.menus.horizontal.*` (pill container, 12dp-radius focused items, icon-only items) that the page does not document.

### Purpose & when to use / not
- Temporary set of actions/choices opened from icon buttons, split buttons, text fields, filter chips, selected text, right-click/long-press (context menus). Overflow, dropdown/select, context menus.
- Persistent actions → toolbar. Takes less space than radio buttons or chips. On compact, consider bottom sheets instead.

### Variants / configurations
| Category | Options |
|---|---|
| Variant | Vertical menu (Expressive); Menu (baseline) |
| Colour | Standard (surface-based, utilitarian); Vibrant (tertiary-based, use sparingly) |
| Layout | Standard; Grouped (gap or divider) |
| Selection | single-select; multi-select (stays open until dismissed) |
| Extras | submenus, filtering text field (autocomplete), custom slots (images, progress, swatches), scrolling |

### Anatomy (vertical)
- 1 Menu item, 2 Leading icon (opt.), 3 Menu item text, 4 Trailing icon (opt.), 5 Badge (opt.), 6 Trailing text (opt., e.g. keyboard shortcut), 7 Container, 8 Supporting text (opt.), 9 Label text / section label (opt.), 10 Gap (opt.), 11 Divider (opt.).
- Baseline: List item, leading icon, trailing icon, container, trailing text, divider.

### Measurements
| Attribute | Vertical (Expressive) [tokens] | Baseline [m3 page/tokens] |
|---|---|---|
| Container shape | 16dp (corner large); inactive (unfocused submenu) 8dp | 4dp |
| Container elevation | level2 (3dp) | level2 (3dp) |
| Container width | n/s | min 112dp, max 280dp |
| Item height | 44dp | 48dp |
| Item shape | 4dp; first/last child 12dp outer with 4dp inner corners; selected 12dp | n/s |
| Item leading / trailing padding | 16dp / 16dp | 12dp / 12dp |
| Item top / bottom padding | 8dp / 8dp | n/s |
| Space between item elements | 12dp | 12dp |
| Leading / trailing icon | 20dp | 24dp |
| Gap between groups | 2dp; group padding 2dp; group shape 8dp | – |
| Divider | n/s | 1dp, 8dp top/bottom padding, dynamic width |
| Submenu indicator icon | n/s | 24dp (cascading-menu-indicator) |
- Slots: keep item padding; targets ≥48x48dp.

### Typography
- Item label: Label large (14pt); supporting text: Body small (12pt); trailing supporting text: Label large [tokens]. Section label typography n/s. Baseline item label: Label large.

### Colour roles
| Element | Standard | Vibrant | Baseline |
|---|---|---|---|
| Container / item | surface-container-low | tertiary-container | surface-container |
| Label text | on-surface | on-tertiary-container | on-surface |
| Leading/trailing icons, supporting & trailing text | on-surface-variant | on-tertiary-container (icons turn tertiary on hover/focus/press) | on-surface-variant |
| Section label | on-surface-variant | on-tertiary-container | – |
| Selected item container | tertiary-container | tertiary | secondary-container |
| Selected content | on-tertiary-container | on-tertiary | on-secondary-container |
| State layer | on-surface (selected: on-tertiary-container) | on-tertiary-container (selected: on-tertiary) | on-surface |
| Disabled content | on-surface @ 0.38 | on-tertiary-container @ 0.38 | on-surface @ 0.38 |
| Divider | n/s | n/s | outline-variant (page) / surface-variant (token) |
- Source [tokens, m3 page]. Selected vs unselected default contrast 3:1.

### States
- Enabled, disabled, hovered (0.08), focused (0.10; focus indicator secondary 3dp, inset -3dp), pressed (0.10), active (parent item while submenu open; active state layer 0.08) [m3 page, tokens].
- Shape morphing: focused submenu corners become more rounded (16dp), unfocused submenu less rounded (8dp).
- Disabled items stay visible (don't remove) and can receive focus but not be selected; dividers/gaps never focusable.

### Behaviour & motion
- Positioned relative to window edge; appears below/next to/in front of trigger; repositions left/right/above to avoid clipping; opening at top expands downward, at bottom upward.
- Enter/exit transition tied to trigger; trigger shows pressed state while open and does not change its icon; ripple on item selection. Dense desktop menus may open instantly (no motion). Filtering: items "ease into their new position". Durations n/s.
- Scrolling menus show a persistent scrollbar; no gaps in scrolling menus (use dividers).
- Submenus open beside the parent item without covering it; best on large screens.
- Single-select auto-unselects previous; multi-select stays open.
- Web density 0 to -3 reduces top/bottom padding.

### Adaptive behaviour
- Compact: consider bottom sheets; medium/expanded: menus in context, can show more items and submenus [m3 page]. Breakpoint table: compact action surface = bottom sheet; medium+ = menu [m3 breakpoints].

### Accessibility
- On open, focus first item. Exit: select, Escape, tap outside, system back; post-close focus is app-defined.
- Keys: Tab = focus menu; Space/Enter = open menu/submenu or select; Up/Down = open closed menu / move focus; Left/Right = open/close submenu; Letters = jump to next item starting with letter; Escape = close.
- Label = item text; roles: web "Menu item", Android Views and Compose "Generic actionable element"; icons beside text are decorative.
- Selection uses colour + shape; add a checkmark as additional cue.
- No nested buttons/switches inside items (one action per item).

### Do / don't
- Limit gaps to one or two; don't resize gaps; dividers for scrolling menus and text-field dropdowns; dividers on web.
- Use vibrant sparingly.
- Don't add multiple actions inside a slot.
- Keep submenus beside, not over, the parent.

---

## 9. Tooltips (plain, rich)

### Status
- Baseline M3; no Expressive update. M2 → M3: colour mappings; rich tooltips more rounded. mdc-android: Tooltip component "is yet to be completed" (no Views implementation documented).

### Purpose & when to use / not
- Plain: brief label for elements without text (icon-only buttons, fields). Not needed when the element already has a label.
- Rich: longer context (definitions, feature explanations), optional subhead, link, up to 2 text buttons.
- Never hide critical information in tooltips (use a dialog). Don't use persistent rich tooltips on icon buttons.

### Variants / configurations
- Plain. Rich: subhead + text + 2 buttons; subhead + text + 1 button; subhead + text; text + 1 button; text + 2 buttons. Rich can be transient or persistent.

### Anatomy
- Plain: 1 Container, 2 Supporting text. Rich: 1 Subhead (opt.), 2 Container, 3 Supporting text, 4 Text button (opt.).

### Measurements
| Attribute | Plain | Rich | Source |
|---|---|---|---|
| Height | 24dp container | content-driven | [m3 page] |
| Padding | 8dp | top 12dp, bottom 8dp, left/right 16dp | [m3 page] |
| Shape | 4dp (extra-small) | 12dp (medium) | [tokens] |
| Elevation | n/s | level2 (3dp) | [tokens] |
| Distance from target | 4dp if target has a visual boundary, 8dp if not (e.g. text) | n/s | [m3 page] |
| Max width | n/s | n/s | – |
- Plain placement: above the target by default; below when the target is in an app bar. Rich: bottom-right of target, repositions in 8dp increments to stay on screen; never covers the parent; desktop may centre below target.

### Typography
- Plain text: Body small (12pt). Rich subhead: Title small (14pt); supporting text: Body medium (14pt); action: Label large (14pt) [tokens].

### Colour roles
- Plain: container inverse-surface; text inverse-on-surface. Rich: container surface-container; subhead and text on-surface-variant; action primary (state layers primary) [tokens, m3 page].

### States
- Rich action button: hover 0.08, focus 0.10, pressed 0.10 on primary [tokens]. Tooltip container itself has no states.

### Behaviour & motion
- Show on hover (desktop) or touch-and-hold (mobile); also on keyboard focus. Persistent rich tooltips open on click/tap or page load (new-feature education); not triggered by hover; dismissed when the user interacts with another element.
- "Both plain and rich tooltips disappear 1.5 seconds after navigating away from the target region." Only one tooltip at a time; a new tooltip closes the previous. Show-delay and animation duration: n/s.

### Adaptive behaviour
- Desktop placement variant (centred below, stays visible while pointer is within target region). Otherwise n/s.

### Accessibility
- Role "Tooltip" (or similar); label inner elements per their own guidance.
- Rich focus order top to bottom: parent element → inline link → text button; don't trap focus; keyboard Tab lands on the button; Space/Enter activates.
- Keep on screen long enough to read; tooltips must not hide crucial information.

### Do / don't
- Plain text short, avoid multi-line; rich subhead one line; keep buttons short and side by side (avoid stacking); one tooltip at a time.

---

## 10. Snackbar

### Status
- Baseline M3; no Expressive update. M2 → M3: colour mappings; clarified dismissive (auto) vs non-dismissive (persists until action). "Material Web doesn't yet include the snackbar component."

### Purpose & when to use / not
- Low-priority, non-interruptive feedback about a process the app performed/will perform; optional single action (e.g. Undo). Dialogs for high-priority messages requiring action.
- Not the only path to a core task; no icons (use another component); no stylised text or inline links.

### Variants / configurations
- Single line; single line + action; two lines; two lines + action; two lines + longer action (action on its own third line). Optional close icon.

### Anatomy
- 1 Container, 2 Supporting text, 3 Action (optional), 4 Close button / icon (optional).

### Measurements
| Attribute | Value | Source |
|---|---|---|
| Height, single line | 48dp | [tokens, m3 page] |
| Height, two lines | 68dp (token) / "expand vertically from 48dp to 64dp" (page) | [tokens] vs [m3 page] |
| Shape | 4dp (extra-small) | [tokens] |
| Elevation | level3 (6dp) | [tokens, mdc-android] |
| Close icon | 24dp | [tokens] |
| Margin from screen edges | fixed on compact (value n/s on m3); mdc-android 8dp | [mdc-android] |
| Max width / internal padding | n/s (padding diagram is image-only) | – |
- Medium/expanded: scale horizontally for longer text (ideal line 40-60 characters), single line + optional button, flexible trailing distance; left- or centre-aligned consistently; never flush to an edge.

### Typography
- Supporting text: Body medium (14pt); action: Label large (14pt) [tokens].

### Colour roles
- Container inverse-surface; text inverse-on-surface; action inverse-primary; close icon inverse-on-surface [tokens, m3 page]. Container opaque (slight transparency allowed if legible). Action text must differ in colour from the label.

### States
- Action: hover 0.08 / focus 0.10 / pressed 0.10 on inverse-primary; close icon states on inverse-on-surface [tokens].

### Behaviour & motion
- Appear at bottom, in front of content; nudge above FABs/docked toolbars; never in front of navigation or FABs; full-width only when there is no persistent navigation (app bar or nav bar), and may then push FABs up.
- Auto-dismiss (no action): 4-10 seconds depending on platform. With action: stay until acted on or dismissed. One at a time; consecutive snackbars sequential; an updated snackbar may immediately replace an outdated one. Don't stack; don't animate other components (e.g. FAB) with the snackbar animation.
- mdc-android: `LENGTH_SHORT` / `LENGTH_LONG` / `LENGTH_INDEFINITE` presets (ms values n/s), default animation mode `fade`, swipe-to-dismiss in CoordinatorLayout, `setAnchorView(fab)`.

### Adaptive behaviour
- Compact: up to two lines, fixed side/bottom distances, 48 → 64/68dp tall. Medium/expanded: wider, single line preferred, left- or centre-aligned.

### Accessibility
- Announce politely (live region, polite/queued) without moving focus; iOS 17+ polite by default; announced after page title at app launch.
- Don't trap focus; on web provide a documented shortcut (e.g. Alt+G) to reach actionable snackbars; Tab moves between elements; Esc dismisses when focused.
- On exit, focus returns to the triggering element or next logical element (Compose: nearest visible or first actionable).
- Web: auto-dismissing snackbars also need inline feedback (e.g. "Save" → "Saved"), or make the snackbar actionable (then it doesn't auto-dismiss).
- Don't let it fully cover focused elements.

### Do / don't
- Keep to one line when possible; don't use filled/elevated buttons for the action; Undo is a good action, Dismiss is unnecessary; don't significantly alter the container shape; snackbar above the FAB, not in front of or behind it.

---

## Appendix: source conflicts to resolve in the new system
- Nav bar/rail selected label weight: Expressive "no longer bolded" (mdc-android) vs nav-bar a11y "bold label" (m3 page); baseline tokens 700.
- Nav rail collapsed elevation: token level0 vs mdc-android Expressive "0dp to 3dp".
- Nav bar elevation: token level2 (3dp) vs page "No shadow".
- Search bar elevation: token level3 (6dp) vs page "no shadow by default".
- Search container colour: search page surface-container-high vs app-bar search token surface-container.
- Tabs/menu divider: page outline-variant vs token surface-variant.
- Tabs icon+label height: 64dp (page, tokens) vs 72dp (mdc-android).
- Snackbar two-line height: 64dp (page) vs 68dp (token).
- Nav drawer width: 360dp (page, tokens) vs mdc-android `maxWidth` 280dp.
- Nav bar horizontal indicator height: 40dp (token) vs 56dp expanded-indicator default (mdc-android).
- Medium flexible height (112dp) equals baseline medium (112dp); "reduced overall height" is only true for large flexible (120dp vs 152dp) and the with-subtitle cases.
