# M3 component digest, group C: cards, carousel, lists, dialogs, bottom sheets, side sheets, divider, chips

Sources: m3.material.io content API snapshot (corpus version 2026-09-23; per-page "Updated" dates are given in each section), resolved token tables (dsdb 38.2.9), and material-components-android docs. Source tags: **[m3 page]** = the component's m3.material.io page (including image captions); **[tokens]** = the resolved token table; **[mdc-android]** = the MDC-Android doc; **[m3 foundations]** = another m3.material.io page (breakpoints, canonical layouts, gestures, layout overview). "n/s" means the sources don't specify it. Hex values are omitted on purpose: the token tables mix 1P (Google) and 3P (baseline purple) palettes, so only the colour **roles** carry over.

**Shared system values used below [tokens]**
- Elevation: level0 = 0dp, level1 = 1dp, level2 = 3dp, level3 = 6dp, level4 = 8dp.
- State-layer opacities: hover 0.08, focus 0.10, pressed 0.10, dragged 0.16. Disabled content is 0.38. Disabled outlines and containers are usually 0.12.
- Focus indicator: colour `secondary`, thickness 3dp, outer offset 2dp. Lists are the exception: they use an *inner* offset of −3dp.
- Shape scale: none 0, extra-small 4dp, small 8dp, medium 12dp, large 16dp, extra-large 28dp, full = circular.
- Typescale (1P font is Google Sans / Google Sans Text; 3P is Roboto; variable builds use Google Sans Flex or Roboto Flex). Values are size/line-height and weight:
  - body-large 16/24, w400
  - body-medium 14/20, w400
  - label-large 14/20, w500
  - label-small 11/16, w500, tracking 0.1pt (0.5pt in 3P)
  - title-medium 16/24, w500
  - title-large 22/28, w400
  - headline-small 24/32, w400
- No token set for any group-C component is marked "[Deprecated]" or "(baseline)" in the corpus. The only legacy flag is on lists, and it comes from the page, not the tokens: "List (baseline)" is "Not recommended. Use expressive lists instead."
- The "Availability & resources" status tables are unresolved placeholders in the corpus (`RESOURCE STATUS_TABLE`), so per-platform availability is n/s.

---

## Cross-cutting findings

1. **Lists are the only group-C component with an explicit M3 Expressive update [m3 page].** The Expressive list (Dec 2025) adds a segmented style, highlighted selection, slots, shape morphing, reorder tokens and swipe-to-reveal tokens. The baseline list is "Not recommended". Other group-C changes in the corpus:
   - Carousel added a new layout in Nov 2025 (uncontained multi-aspect ratio).
   - Chips softened their stroke colour in Aug 2024 (`outline` → `outline-variant`).
   - Cards, dialogs, bottom sheets, side sheets and dividers carry only "Differences from M2" notes, with no Expressive changes in the corpus.
2. **Containment model.** For cards, bottom sheets and side sheets the container is the *only* required element, and size is driven by content. Lists require container + label text. Expressive lists replace dividers with **gaps** ("Use gaps for contained lists… Limit dividers to uncontained or complex lists"). The segmented gap is 2dp [tokens]. Dividers are guided toward grouping, not item-by-item separation.
3. **Surface-container ladder [tokens]:**

   | Role | Used by |
   |---|---|
   | `surface` | outlined card, carousel item, list item (standard and segmented), standard side sheet, full-screen dialog container and header (token; the page diagram says surface container high) |
   | `surface-container-low` | elevated card, bottom sheet (standard and modal), modal side sheet, elevated chips, list reorder drop zone |
   | `surface-container` | full-screen dialog header on-scroll, expanded list chevron container |
   | `surface-container-high` | basic dialog |
   | `surface-container-highest` | filled card |

   Shadows are minimal: sheets 1dp, elevated card and elevated chips 1dp, dialog 6dp.
4. **Selection colour is unified.** Selected list items, selected filter chips and selected input chips all use `secondary-container` / `on-secondary-container`. Expressive list *reorder* uses `tertiary-container` / `on-tertiary-container` to distinguish the dragged item [tokens].
5. **Corner-radius map:**
   - Chips: 8dp (small)
   - Cards: 12dp (medium)
   - Lists: 16dp at the group's outer corners, 4dp at inner corners; selected, pressed, focused and dragged items 16dp; hovered items 12dp (Expressive)
   - Side sheets: 16dp when modal (inner corners only) or detached (all corners)
   - Carousel items, basic dialog, bottom-sheet top corners: 28dp (extra-large)
   - Full-screen dialog and standard side sheet: 0dp
6. **Modal vs standard pairs.** Modal versions sit above a scrim, block the app and are dismissed by scrim tap, swipe, close affordance, Back or Escape. Standard versions coexist with content. Modal bottom sheets are "used in mobile apps only". Modal side sheets are preferred at compact sizes; standard side sheets are mostly for medium to expanded [m3 page].
7. **Adaptive swaps:**
   - Full-screen dialog (compact only) → basic dialog at medium and above.
   - Bottom sheet (compact and medium) → side sheet on expanded/desktop.
   - Bottom sheet (compact) → menu (medium and expanded) for "supplemental selection" [m3 foundations].
   - Modal side sheet → standard side sheet at larger sizes.
   - Cards ↔ lists (compact may swap cards for lists). Lists → cards, carousel or list-detail at larger sizes.
   - Extra-large (≥1600): a standard side sheet can act as the 3rd pane. Its 400dp max width compares with 412dp fixed panes [m3 foundations].
   - Large (1200–1599) and extra-large rules are otherwise largely n/s per component. The breakpoints page lists "Simple dialog" and "Menu" for those sizes.
8. **Width constraints:**
   - Basic dialog: 280–560dp, with custom placement inside a 56dp margin.
   - Full-screen dialog: max 560dp.
   - Bottom sheet: max 640dp; beyond a 640dp window it gets a 56dp top margin and 56dp side margins.
   - Side sheet: max 400dp (the docked token is 256dp), with 16dp margins when detached.
   - Carousel small item: 40–56dp.
   - Chips: 32dp tall, with an 88dp minimum width when two actions need 48dp targets.
9. **Predictive back (Android)** applies to bottom sheets and side sheets. The sheet detaches from the screen edges and the previous screen previews underneath. Side-sheet content also scales in the direction of the gesture. Dialogs are not in the predictive-back component list [m3 foundations].
10. **Accessibility patterns:**
    - Every drag or swipe needs a single-pointer alternative: card menus, list "more" buttons, a bottom-sheet drag handle that cycles heights.
    - Targets are 48dp: drag-handle region, chip remove icon, list slots, carousel header arrow.
    - Dialogs trap Tab (focus cycles first ↔ last) and close on Escape.
    - Carousel focus starts on the first item, never on the container.
    - List arrow navigation wraps at the ends.
    - Roles: dialog = "alert dialog" (web); side sheet = "Dialog"; drag handle = "button"; carousel container = "container"; directly actionable card = button or link; selectable list items use listbox/option (web) or radio/checkbox (Android).
11. **Spec vs token conflicts to resolve in your system:**
    - Full-screen dialog container: page says surface-container-high, token says `surface`.
    - List divider: page diagram says outline-variant, list token says `outline`; the standalone divider token is outline-variant.
    - Baseline list trailing padding and divider inset: 24dp on the page vs 16dp in tokens.
    - Side sheet width: max 400dp on the page vs 256dp docked width in the token.
    - Side-sheet divider: page says outline-variant, token says `outline`.
    - Chip outline: assist and suggestion diagrams say `outline`, tokens say `outline-variant` (the Aug 2024 change).
    - Input chip: generic `outline` token vs `outline-variant` for the unselected state.
    - Card dragged elevation: mdc-android says 8dp (outlined/filled) and 2dp (elevated); tokens say 6/6/8dp.
    - List segmented container: token `surface` vs mdc-android `colorSurfaceBright`.

---

## 1. Cards (elevated, filled, outlined)
Page updated 2026-07-24.

**Status**
- Baseline M3. There is no Expressive update on the page and nothing is deprecated [m3 page].
- Differences from M2: "New color mappings and compatibility with dynamic color"; "Lower elevation and no shadow by default"; "Three official card variants" [m3 page].

**Purpose & when to use / not use**
- Show content and actions on a single topic. Cards should be easy to scan, with a clear hierarchy, and can be entry points to deeper detail (an album, a trip) [m3 page].
- Display cards together in a grid, a vertical list or a carousel [m3 page].
- Don't: "force content into cards when spacing, headlines, or dividers would create a simpler visual hierarchy" [m3 page].
- At compact sizes, consider swapping cards for lists [m3 page].

**Variants / configurations**
- Elevated, filled and outlined: "Each provides the same legibility and functionality, so the variant you use depends on style alone" [m3 page].
- Emphasis: filled has the least separation; elevated has more than filled but less than outlined; outlined has the greatest emphasis [m3 page].
- Interaction model: a card is **either** a non-actionable container holding buttons and links, **or** directly actionable with no inner buttons [m3 page].
- Collections: grid (customisable to staggered or mosaic), vertical list, carousel. Collections are coplanar (shared resting elevation) [m3 page].
- mdc-android adds a checkable state (checked icon plus foreground change) and a dragged state. Neither is on by default [mdc-android].

**Anatomy [m3 page]**
1. Container (the only required element)
2. Image
3. Button
4. Supporting text
5. Subhead
6. Headline

Other optional content:
- Outline (outlined variant)
- Thumbnail (avatar or logo) and video
- Full-width or inset dividers
- Icon buttons
- Selection controls (chips, sliders, checkboxes)
- Linked text
- Overflow menu, top-right or bottom-right

**Measurements**

| | Elevated | Filled | Outlined |
|---|---|---|---|
| Corner radius | 12dp | 12dp | 12dp |
| Resting elevation | 1dp | 0dp | 0dp |
| Hover elevation | 3dp | 1dp | 1dp |
| Focus / pressed elevation | 1dp | 0dp | 0dp |
| Dragged elevation | 8dp | 6dp | 6dp |
| Outline width | – | – | 1dp |
| Icon size | 24dp | 24dp | 24dp |

The corner radius is the `corner.medium` token [tokens]. Elevation and icon sizes are also [tokens].

- Page spec table: shape 12dp; left/right padding 16dp; padding between cards "8dp max"; label text start-aligned [m3 page].
- Width and height are flexible and content-driven. A "maximum card height" is mentioned but its value is n/s. A minimum touch target for the card itself is n/s [m3 page].
- mdc-android:
  - 8dp margins recommended on mobile.
  - Checked icon 24dp, margin 8dp, gravity TOP_END.
  - Stroke 1dp (outlined) or 0dp.
  - Its prose says the dragged elevation is 8dp for outlined/filled and 2dp for elevated, which conflicts with the tokens [mdc-android].

**Typography**
- n/s in the page and tokens.
- The mdc-android sample uses title = `titleMedium` and secondary/supporting text = `bodyMedium`, with a 194dp media height and 16dp content padding. Treat these as sample values only [mdc-android].

**Colour roles [tokens] unless noted**
- Elevated: container `surface-container-low`, shadow `shadow`, disabled container `surface` at 0.38 opacity.
- Filled: container `surface-container-highest`. The disabled container token is `on-surface` at 0.38.
- Outlined: container `surface`; outline `outline-variant` 1dp (also on hover, pressed and dragged); focus outline `on-surface`; disabled outline `outline` at 0.12.
- All variants: icon `primary`; state layer `on-surface`; focus ring `secondary`.
- mdc-android uses different roles: stroke `colorOutline` unchecked and `colorSecondary` checked; ripple `colorOnSurfaceVariant` at 20%; checked-icon tint `colorSecondary` [mdc-android].

**States**
- Hovered, focused, pressed, dragged and disabled exist for every variant [m3 page].
- Hover raises elevation by one level. Dragged raises elevation and applies a 0.16 state layer [tokens].
- Non-actionable cards have no hover state and no ripple [m3 page].
- A picked-up card sits "in front of all elements, except app bars and navigation" [m3 page].

**Behaviour & motion [m3 page]**
- Expand with a container transform. Reserve it "for hero moments that are meant to be expressive"; for ordinary navigation use the simpler forward/backward transition.
- Swipe: one swipe action per card, performed anywhere on the card, to dismiss or change state (flag, archive). No swipeable content inside cards (image carousels, pagination), and swipes must not detach parts of a card.
- Pick-up-and-move: drag to reorder within a collection.
- Scrolling on mobile: card content never scrolls internally. Overflow is truncated and revealed by expanding the card's height. An expanded card can exceed the screen and scroll with the page.
- Scrolling on desktop: content may expand and scroll *within* the card.
- mdc-android supports swipe-to-dismiss via `SwipeDismissBehavior` [mdc-android].

**Adaptive behaviour**
- Position and alignment (left, right, centre) change by breakpoint [m3 page].
- Compact: cards stretch full width; consider swapping to lists while keeping their controls and actions [m3 page].
- Expanded: use multiple columns. Rearrange related cards into horizontal rows or carousels rather than stretching them [m3 page].
- A horizontal card at compact can become a larger, vertical card at expanded [m3 page].
- Breakpoints page: "Be careful when changing between list items and cards" [m3 foundations].
- Medium, large and extra-large specifics: n/s.

**Accessibility [m3 page]**
- Never put an action on an actionable surface (no buttons inside a clickable card).
- Directly actionable card: a tab stop with role **button** or **link**; it ripples and shows hover. Non-actionable card: not a tab stop and needs no role. Every actionable element inside it is a tab stop, and all are visited before focus moves to the next card.
- Keys: Tab moves to the next card or element. Space/Enter activates or opens a secondary menu. Arrows move within that menu, Space/Enter selects, Tab exits.
- Reading-order example: heading, image, body, primary button, secondary button. Hide decorative images from screen readers.
- Drag and swipe need a single-pointer alternative. Example: tap or long-press opens a menu with move and delete actions.
- Text or icons on images need a scrim or bounding shape to meet contrast.
- On Android, expose drag actions via an `AccessibilityDelegate` with custom actions [mdc-android].

**Do / Don't [m3 page]**
- Don't force content into cards when spacing or dividers suffice.
- Don't scroll inside a card on mobile ("could cause two scroll bars to be displayed"); expand instead.
- Assign only one swipe action per card.
- Raise a moved card above the others; don't let it bump them.
- Place filter and sort controls outside the card collection.
- Avoid text on images; if unavoidable, add a scrim or bounding shape.

---

## 2. Carousel (multi-browse, uncontained, uncontained multi-aspect ratio, hero, center-aligned hero, full-screen)
Page updated 2026-08-18.

**Status**
- "This component is new in Material 3" [m3 page].
- Updates: **November 2025** added the "Uncontained multi-aspect ratio" layout. **2023** added uncontained, full-screen, centred carousels, hero and multi-browse [m3 page].
- No Expressive label and nothing deprecated.
- Differences from M2: dynamic items change shape when scrolled; parallax; snap-into-place [m3 page].

**Purpose & when to use / not use**
- A scrollable collection of visual items (images, video) with optional brief text that adapts to item size [m3 page].
- Layout guide [m3 page]:
  - Multi-browse: browsing many visuals at once.
  - Uncontained: highly customised or text-heavy content, or "traditional carousel behavior".
  - Hero: spotlighting large visuals such as movies or featured apps.
  - Center-aligned hero: centred large visuals.
  - Full-screen: vertically scrolling immersive feeds.
- Avoid multi-browse when items need a lot of text or have complicated imagery. For text-heavy items use uncontained, or a series of cards [m3 page].
- Research (200+ participants): a previewed or squished item strongly signals more content, and people expect around 10 items in a multi-scroll carousel [m3 page].

**Variants / configurations**
- Overview lists six layouts; Guidelines lists four "layouts" (multi-browse, uncontained, hero, full-screen). Center-aligned hero is the common centred form ("All of these layouts can be centered") [m3 page].
- Alignment: start or center [m3 page]. mdc-android `carouselAlignment` defaults to start [mdc-android].
- Scrolling modes:
  - Default (free) scrolling: only for uncontained.
  - Snap-scrolling: for multi-browse, hero and full-screen. Full-screen *must* snap [m3 page].
- Orientation: horizontal; full-screen scrolls vertically [m3 page].
- mdc-android strategies [mdc-android]:
  - `MultiBrowseCarouselStrategy` (the default)
  - `UncontainedCarouselStrategy`
  - `HeroCarouselStrategy` (start- or center-aligned)
  - `FullScreenCarouselStrategy` (vertical orientation recommended)
  - `CarouselSnapHelper` is recommended for multi-browse, hero and full-screen.
- An optional "with-outline" item style exists [tokens].

**Anatomy [m3 page]**
1. Container (a rectangle; the number of visible items varies by layout and breakpoint)
2. Large item
3. Medium item
4. Small item
5. Optional item text

**Measurements [m3 page]**

| Layout | Items shown | Leading / trailing padding | Top / bottom padding | Gap | Large item | Medium item | Small item | Item radius |
|---|---|---|---|---|---|---|---|---|
| Multi-browse | ≥1 large, 1 medium, 1 small | 16 / 16dp | 8dp | 8dp | dynamic or user-set | dynamic | 40–56dp | 28dp |
| Uncontained | same-size items bleeding past the edge | 16dp leading only | 8dp | 8dp | single size | – | – | 28dp |
| Uncontained multi-aspect | widths from 9:16 (min) to 16:9 (max) | 16dp leading only | 8dp | 8dp | per item | – | – | 28dp |
| Hero | ≥1 large + 1 small | 16 / 16dp | 8dp | 8dp | dynamic | – | 40–56dp | 28dp |
| Center-aligned hero | ≥1 large + 2 small | 16 / 16dp | 8dp | 8dp | dynamic | – | 40–56dp | 28dp |
| Full-screen | 1 edge-to-edge item | 0dp | 0dp | 16dp | full | – | – | n/s |

- Alignment is "vertically centered"; full-screen is "Centered" [m3 page].
- Large items have a customisable max width that drives how every item fits. Small items have a min of 40dp and a max of 56dp [m3 page].
- Tokens [tokens]:
  - Item shape `corner.extra-large` (28dp).
  - Elevation 0dp, 1dp on hover.
  - The with-outline style adds a 1dp outline.
- mdc-android [mdc-android]:
  - In a horizontal hero, the large item's width is at most 2× its height; more large items are added once that maximum is reached.
  - Item size comes from the first item's `MaskableFrameLayout` width, which must be fixed (not `wrap_content`).
  - The small-item range is adjustable via `setSmallItemSizeMin/Max`.
  - Use `shapeAppearanceExtraLarge`.
- Accessibility affordances: "Show all" button padding 4dp; header arrow icon button 48dp [m3 page].
- Item heights are n/s. Container height is set by the app (on Android, the RecyclerView height) [mdc-android].

**Typography**
- n/s (no type tokens).
- Text should be brief. Avoid more than two lines at compact sizes unless the background is simple [m3 page].
- Adapt text by item size: large items show full title + label, medium items hide the title, small items abbreviate the label [m3 page].

**Colour roles**
- Item container `surface` [tokens]. The page diagram names "Container" and "Surface" [m3 page].
- State layer `on-surface`; focus ring `secondary`; disabled container 0.38 opacity [tokens].
- With-outline style: `outline`; `on-surface` when focused; `outline` at 0.12 when disabled [tokens].

**States**
- Enabled, hovered (1dp elevation + 0.08 layer), focused, pressed and disabled [m3 page, tokens].
- Tapping an item "changes the shape slightly" and ripples. Hover and click ripples work on both active and inactive items [m3 page].

**Behaviour & motion [m3 page]**
- Item visuals parallax (they move at a different speed than their container), and items change size as they move through the layout.
- Snap-scrolling realigns items to the layout grid on release:
  - Hero moves one item at a time.
  - Multi-browse moves many at once.
  - Full-screen must snap to the container edges (never stop halfway).
- mdc-android masks items from 0–100% of their width (`MaskableFrameLayout`). `onMaskChangedListener` lets text pin or fade as the mask changes. Uncontained fits as many full-size items as possible, then one cut-off item [mdc-android].
- **Reduced motion** [m3 page]:
  - Remove parallax and the expand-on-entry effect; all items become the same size.
  - Items must reach the window edges to avoid clipping.
  - A hero shows its small item only partially.

**Adaptive behaviour [m3 page]**
- Compact (<600): "comfortably show up to three carousel items". With text, show at most three. A hero at compact shows one large + one small item.
- Larger sizes add more items and scale them: multi-browse shows more large and medium items; hero shows more large items. The example is 8 items on a landscape tablet.
- Full-screen always shows one item and "only works in portrait orientation in compact and medium breakpoints. Don't use this layout in landscape orientation".
- Medium, expanded, large and extra-large thresholds per layout: n/s beyond "more items".
- The lists page notes a list may become a carousel at larger sizes; the cards page suggests carousels for related cards on large screens.

**Accessibility [m3 page]**
- Use cases: navigate to the carousel, move between items, activate an item, skip the carousel.
- On vertically scrolling pages, provide a way to view every item without horizontal scrolling (not needed for full-screen):
  - A **Show all** button below the carousel (4dp padding) opens a vertical page of all items.
  - If the carousel has a header, use a 48dp arrow icon button next to it instead, and repeat the header on the all-items page.
- Don't put arrows or other buttons inside, beside or over the carousel.
- Focus: Tab puts initial focus on the **first item**, not the container. Tab or arrows move between items, and Up/Down arrows leave the carousel. Space/Enter activates.
- Labels: the container has the **container** role. Each item label announces the current position and the total item count.

**Do / Don't [m3 page]**
- Size large items so images and text stay recognisable. Avoid slivers so thin the image can't be recognised.
- Use snap-scrolling for multi-browse, hero and full-screen; use default scrolling only for uncontained.
- Use multi-aspect only if items genuinely vary in width.
- Don't cover the carousel with buttons or put arrows beside it.
- Keep item text to two lines or fewer at compact sizes.

---

## 3. Lists (Expressive list: standard and segmented; baseline list)
Page updated 2026-08-06.

**Status**
- "M3 Expressive update: Lists have a new segmented visual style, improved selection treatment, and support for slots" [m3 page].
- **December 2025** added the **expressive** list ("Recommended for new designs"); "List (baseline) is still available" [m3 page].
- Variant table: the baseline list under M3 Expressive is "Not recommended. Use expressive lists instead." [m3 page].
- Expressive lists are supported on MDC-Android and Jetpack Compose. On web, "expressive lists are built on top of baseline lists" [m3 page].
- Token sets [tokens]:
  - List – Common: baseline plus expressive shapes and sizes.
  - List – Expand.
  - List – Reorder ("Only use for Expressive lists").
  - List – Reveal ("Only use for expressive lists").
- Differences from M2 to baseline M3: standard heights of 56, 72 and 88dp; middle-aligned content, top-aligned when the item is 88dp or taller or has 3+ lines [m3 page].

**Purpose & when to use / not use [m3 page]**
- Help people find a specific item and act on it. Lists are vertical groups "optimized for reading comprehension"; use them to communicate or select discrete items (for example, choosing from a set of colours).
- Order items logically (alphabetical, numerical), keep them short and scannable, and keep element positions consistent from item to item.
- Non-interactive lists organise information for scanning only.
- At larger sizes, consider swapping to cards or a carousel to use the space. On compact, a list can replace cards.

**Variants / configurations**
- Variants: Expressive vs baseline.
- Styles: **standard** or **segmented**. This is a visual choice only and doesn't change behaviour. Segmented is Expressive-only [m3 page].
- Selection modes: one per list at a time [m3 page].
  - Single-action
  - Multi-action (primary action + secondary actions)
  - Single-select
  - Multi-select
  - Non-interactive
- Interactions: expand/collapse, and swipe-to-reveal. "Swipe-to-reveal interactions are only available on Android Views" [m3 page].
- Sizes: one-line, two-line and three-line [m3 page, mdc-android].
- Baseline configurations [m3 page]:
  - Leading avatar, image/thumbnail, video or icon, or text-only, each with or without a trailing checkbox.
  - Leading checkbox or radio, with or without trailing text.
  - Trailing switch, with or without a leading icon.
- Slots (Figma kit): leading, content and trailing.
  - Leading: visuals, selection controls, a badge or a larger image.
  - Content: label and supporting text plus a badge, icon, inline label or more text. It must be the widest slot.
  - Trailing: icon, icon button, trailing text or selection control.
  - "Slots require custom code implementation" and are "not accessible by default" [m3 page].

**Anatomy**
- Specs version [m3 page]:
  1. Container
  2. Overline
  3. Label text
  4. Trailing text
  5. Supporting text
  6. Trailing icon
  7. Divider
  8. Leading avatar
  9. Leading icon
  10. Leading media (image or video)
- Container and label text are required [m3 page].
- The Guidelines version also lists a trailing selection control (checkbox, radio, switch) and the leading avatar container and text [m3 page].

**Measurements**
- Item heights: one-line 56dp, two-line 72dp, three-line 88dp. The tallest element determines the height [tokens, m3 page].
- Item padding: leading 16dp, trailing 16dp, top 10dp, bottom 10dp, 12dp between elements [tokens].
- Baseline layout table [m3 page]:
  - Label left padding 16dp; leading element left padding 16dp.
  - Leading icon top padding 8dp (12dp when the item is 88dp or taller).
  - Trailing element left padding 16dp, right padding **24dp**.
  - Divider inset 16dp left / **24dp** right; 0dp above and below.
  - Targets 48dp.
  - Elements centre-aligned, top-aligned at 88dp or taller.
  - Conflict: tokens give trailing space 16dp and divider trailing space 16dp.
- Element sizes [tokens]:

  | Element | Baseline | Expressive |
  |---|---|---|
  | Leading icon | 24dp | 20dp |
  | Trailing icon | 24dp | 20dp |
  | Leading avatar | 40dp circle | 40dp circle |
  | Leading image | 56×56dp, square corners | 56×56dp, 8dp radius |
  | Leading video (small) | 100×56dp, 8dp radius | same |
  | Leading video (large) | 114×64dp, 8dp radius | same |

  The icon-button height is dynamic and fills the item height [m3 page].
- **Shape morphing (Expressive)** [m3 page]:
  - Unselected: "4dp inner, 16dp outer".
  - Selected: "16dp" on all corners.
  - Tokens [tokens]:
    - Group container 16dp (`large`).
    - Item at rest 4dp (`extra-small`); hovered 12dp (`medium`).
    - Focused, pressed, dragged and selected (in every state) 16dp.
    - Baseline item 0dp (`none`); the baseline selected container is 16dp.
- Segmented gap 2dp [tokens].
- mdc-android applies position states `state_first`/`middle`/`last`/`single` with matching `listItemShapeAppearanceFirst/Middle/Last/Single`, plus `…Checked/Pressed/Hovered`. Multi-section lists compute position per section [mdc-android].
- Elevation: 0dp at rest, 8dp (level4) when dragged [tokens].
- Divider: 1dp, inset 16dp leading and 16dp trailing, 0dp top and bottom [tokens].
- Focus ring: 3dp `secondary` at an *inner* offset of −3dp [tokens].
- Reveal: action shapes 16dp; secondary icon buttons circular [tokens]. The mdc-android sample uses 64dp-wide icon buttons with 2dp side margins; `minRevealedChildWidth` is 6dp [mdc-android].

**Typography [tokens]**
- Label text: body-large (16/24, w400)
- Supporting text: body-medium (14/20, w400)
- Overline: label-small (11/16, w500)
- Trailing supporting text: label-small
- Avatar letter: title-medium (16/24, w500)

**Colour roles [tokens]**
- Default:
  - Container `surface` (standard and segmented tokens alike). mdc-android differs: standard is transparent, segmented is `colorSurfaceBright`, selected is `colorSecondaryContainer` [mdc-android].
  - Label `on-surface`.
  - Supporting text, overline, leading and trailing icons, trailing text: `on-surface-variant`.
  - Avatar `primary-container` with an `on-primary-container` letter.
  - Divider `outline` (the page diagram says outline variant).
- Selected:
  - Container `secondary-container`.
  - Label, supporting text, overline, icons and trailing text `on-secondary-container`.
  - In selected hover, focus and pressed states the leading and trailing icons switch to `on-surface`.
- Disabled: content `on-surface` at 0.38; the selected-disabled container is `on-surface` at 0.38.
- State layers: `on-surface` at 0.08 / 0.10 / 0.10 / 0.16.
- Reorder (Expressive):
  - Item container `tertiary-container`; all content and the state layer `on-tertiary-container` (0.10).
  - Drop zone `surface-container-low`; shape 16dp; uses the shadow colour.
- Reveal (Expressive):
  - Primary action icon button: `primary` container, `on-primary` icon and state layers.
  - Other icon buttons: `secondary-container` container, `on-secondary-container` icon, circular.
  - Revealed item container `surface`.
- Expand: trailing chevron container is circular, `surface` when collapsed and `surface-container` when expanded; chevron icon `on-surface`; expand container shape 16dp.
- For items with images, consider a content-based colour scheme for the container, either at rest or on interaction [m3 page].

**States [m3 page]**
- Both default and selected items have enabled, disabled, hovered, focused, pressed and dragged states.
- The selected state applies to the *whole* item (item and checkbox both show selected).
- Expressive items morph shape on hover (12dp) and press/focus (16dp) [tokens].

**Behaviour & motion [m3 page]**
- Selection-mode rules:
  - Single-select: no multi-actions, no nested actions, no checkboxes; use radio buttons.
  - Multi-select: checkboxes or switches, no nested actions, no radios.
  - Single-action: no nested actions; can't be toggled into a persistent selected state.
  - Multi-action: the primary action fills the leading and content area; supplementary actions sit at the trailing end.
- Expand/collapse is folder-like and uses a container transform (parent-child transition).
- Swipe (Android):
  - Reveals buttons, using a mix of button styles.
  - The primary action is the final end-aligned option, and a full swipe triggers it, clearing the item off-screen.
  - Always provide an alternative such as a "more" icon.
- mdc-android swipe details [mdc-android]:
  - `primaryActionSwipeMode` can be disabled (default), `direct` or `indirect`.
  - Never leave an item fully swiped (revealed children shrink below the minimum touch size); reset or dismiss it.
  - The triggered action must match the element that grows during the swipe.
- Reorder uses a drag handle or an accessible alternative [tokens].

**Adaptive behaviour [m3 page]**
- Compact (<600): edge-to-edge; selecting an item opens a details page.
- Medium (600–839) and expanded (840–1199): list-detail side-by-side. A list can also become a carousel or cards, reveal supporting text, use larger imagery, or go multi-column.
- Line length: ideally 40–60 characters; large screens can take up to 120 (raise the line height near 120). Adjust margins instead of stretching.
- Large and extra-large: n/s beyond the canonical list-detail layout. The canonical layouts page gives 1 pane at compact and 2 panes at medium/expanded for list-detail [m3 foundations].

**Accessibility [m3 page]**
- Indicate selection with more than colour (checkbox or radio, an icon, or a non-colour style).
- Targets at least 48×48dp. Slots must keep the list structure and standard padding.
- Single-action lists:
  - Tab focuses the first item, or the selected item if there is one.
  - Up/Down arrows move between items and wrap at the ends.
  - Space/Enter activates.
- Multi-action lists:
  - Tab focuses the first element.
  - Arrow keys move between *all* focusable elements, crossing item boundaries.
  - Space/Enter activates.
- Label = label text + supporting text.
- Roles:

  | | Web | MDC-Android | Compose |
  |---|---|---|---|
  | Container | **listbox**, labelled with the selection type | – | – |
  | Item | **option** (selected / not selected) | radio button or checkbox, on the control | whole item gets radio or checkbox (checked / not checked) |

  A non-selectable list is read without a role (Compose).
- Swipe alternatives: single tap, double tap, long press, or a "more" button.
- mdc-android [mdc-android]:
  - Mark decorative elements not focusable.
  - Use the `Widget.Material3.Checkbox/RadioButton/Switch.ListItem` styles for decorative synced controls.
  - Expandable items must announce collapsed or expanded state (`ACTION_EXPAND` / `ACTION_COLLAPSE`).

**Do / Don't [m3 page]**
- Use segmented gaps with filled items for groups. Limit dividers to uncontained lists.
- Keep visuals and primary text in the same position in every item. Don't put visuals mid-row.
- Use only one selection interaction per item (not a checkmark *and* a bookmark).
- Limit supporting text to 1–3 lines and truncate by screen size.
- Use circular or expressive-shape avatars for people or entities; use square images for products or videos.
- Leading and trailing slots must be narrower than the content slot.

---

## 4. Dialogs (basic, full-screen)
Page updated 2026-07-28.

**Status**
- Baseline M3; no Expressive update or deprecation [m3 page].
- Differences from M2: new colour mapping; "Greater padding…"; custom positioning; "Increased corner-radius"; "Larger and darker headline" [m3 page].

**Purpose & when to use / not use [m3 page]**
- A modal window for critical information or a decision. It blocks the app until confirmed, dismissed or acted on. Common use: confirming high-risk actions.
- Use sparingly. For low or medium priority, use a snackbar; for options, a dropdown menu is less disruptive. Present non-critical information inline.
- Basic dialogs suit alerts, quick selection, confirmation, and date or time pickers. Full-screen dialogs suit multi-step tasks such as creating a calendar event.

**Variants / configurations**
- Basic: icon optional; with an icon content is centre-aligned, without one it is start-aligned; optional divider; optional scrollable list content; custom position on large screens [m3 page].
- Full-screen: header/app bar with a close "X", optional headline, confirm text button, optional divider, optional bottom action bar [m3 page].
- mdc-android overlays: default (start-aligned icon and title) and Centered. There is no dedicated full-screen dialog component; use a `DialogFragment` [mdc-android].

**Anatomy [m3 page]**
- Basic:
  1. Container
  2. Icon (optional)
  3. Headline (optional)
  4. Supporting text
  5. Divider (optional)
  6. Button label text
  7. Scrim
- Full-screen:
  1. Container
  2. Header
  3. Icon (close affordance)
  4. Headline (optional)
  5. Text button
  6. Divider (optional)

**Measurements [m3 page] + [tokens]**

| Attribute | Basic | Full-screen |
|---|---|---|
| Corner radius | 28dp (extra-large) | 0dp |
| Width | min 280dp, max 560dp | container width, max 560dp |
| Height | dynamic | dynamic |
| Padding | 24dp top, left, right and bottom | 24dp top, left and right |
| Spacing | 8dp between buttons; 16dp title→body; 16dp icon→title; 24dp body→actions | 8dp between elements |
| Header / action bar | – | header 56dp; bottom action bar 56dp |
| Icon | 24dp | close icon 24dp |
| Divider | 1dp | 1dp |
| Elevation | 6dp (level3) | 0dp; header and action bar rise to 3dp (level2) on scroll |

- Custom placement on large screens respects "a 56dp margin from the edges of the screen" [m3 page].
- mdc-android: background insets 24dp start/end and 80dp top/bottom; scrim dim amount 32% [mdc-android].

**Typography [tokens]**
- Basic: headline headline-small (24/32, w400; a "subhead" token uses the same); supporting text body-medium (14/20); action labels label-large (14/20, w500).
- Full-screen: header headline title-large (22/28, w400); action labels label-large.
- mdc-android list items use bodyMedium, and single/multi-choice items use bodyLarge [mdc-android].

**Colour roles**
- Basic [tokens; the m3 page diagram agrees]:
  - Container `surface-container-high`
  - Icon `secondary`
  - Headline `on-surface`
  - Supporting text `on-surface-variant`
  - Action labels and their state layers `primary`
  - Divider `outline`
  - Scrim: role `scrim`
- Full-screen [tokens]:
  - Container and header `surface` (the page diagram says surface container high).
  - Header on-scroll `surface-container` + 3dp.
  - Headline and close icon `on-surface`.
  - Actions `primary`.
  - Divider `surface-variant`.

**States**
- Action buttons follow the text-button states: hover 0.08, focus 0.10, pressed 0.10, all in `primary` [tokens].
- Confirm can be disabled until a required choice is made. "Dismissive actions are never disabled" [m3 page].
- Exception: in full-screen dialogs, "Don't disable the confirmation button" [m3 page].

**Behaviour & motion [m3 page]**
- Enter/exit transition (fade). A FAB transforms into a full-screen dialog via container transform.
- Focus is held until the dialog is dismissed. A dialog is never partly off-screen or obscured, except that dialogs can sit above full-screen dialogs ("the only dialogs over which other dialogs can appear"; launching one "resets the app's perceived elevation").
- Scrolling: avoid it. If needed, the title is pinned at the top and the buttons at the bottom, and dialog content never scrolls with the background.
- Actions: at most 2. A single action must be an acknowledgement. With two, the confirm action is closest to the trailing edge and the dismiss action sits to its left; this mirrors in RTL. Stacked buttons are allowed for long labels, with confirm above dismiss.
- Avoid a third action such as "Learn more"; use inline expansion instead.
- Full-screen dialogs:
  - Save with **Save** or a specific verb (Send, Create). Avoid Done, OK or Close.
  - The close "X" is the only navigation in the app bar.
  - Closing with unsaved changes shows a basic "discard?" dialog.
  - Don't show a confirmation dialog after confirming. Show a basic dialog only if the action fails.
  - Field errors appear inline, all at once. General errors (such as network) appear in a basic dialog.

**Adaptive behaviour [m3 page] + [m3 foundations]**
- Compact (<600): basic or full-screen. "Full-screen dialogs are for compact breakpoints only… For medium and expanded breakpoints, use a basic dialog."
- Medium (600–839): basic dialog, centred by default, with optional custom position (for example, the right side).
- Expanded (840–1199): a modal window above a scrim; can be custom-positioned anywhere within the 56dp margin.
- Large and extra-large: "Simple dialog" per the breakpoints table [m3 foundations]. Other specifics n/s.

**Accessibility [m3 page]**
- Initial focus lands on the first interactive element.
- Focus trap: Tab and Shift+Tab cycle through elements inside the dialog and wrap. Space/Enter commits. **Escape closes.**
- The label is the headline. The web role is **alert dialog** for basic dialogs. Inner components follow their own labelling guidance.
- At 200% text size, Android headlines should fit within 4 lines. If truncated, provide a one-tap path to the full text.
- Screen readers must be able to scroll all content and complete inputs.
- mdc-android: give the title icon a `contentDescription` [mdc-android].

**Do / Don't [m3 page]**
- Headlines are brief questions or statements ("Use location service?"). Avoid "Are you sure?", apologies and alarms.
- Don't place dismissive actions to the right of confirming actions.
- Don't offer "Cancel" when no action is proposed. Use a single acknowledgement instead.
- Keep long or variable-length headlines out of the full-screen app bar; put them in the content area.
- Don't use dialogs for low-priority information (use a snackbar).

---

## 5. Bottom sheets (standard, modal)
Page updated 2026-07-28.

**Status**
- Baseline M3; no Expressive update or deprecation [m3 page].
- Differences from M2: new colour mappings; "28dp top corner radius"; "New max-width of 640dp and an optional drag handle with an accessible 48dp hit target" [m3 page].

**Purpose & when to use / not use [m3 page]**
- "Use bottom sheets in compact and medium breakpoints." Content should be supplementary, not the app's main content.
- Standard: complements the primary content and stays interactive alongside it, for example a music player or location info over a map.
- Modal: an alternative to inline menus or simple dialogs on mobile, especially for long action lists or items needing descriptions and icons. "Modal bottom sheets are used in mobile apps only."
- For complex tasks on larger screens, consider a non-transient surface. On desktop, swap to a side sheet.

**Variants / configurations**
- Standard: no scrim, coexists with content, preset heights from full-screen down to preview. At full height it shows a collapse icon in an app bar [m3 page].
- Modal: above a scrim and blocking [m3 page].
- The token table names the container "docked" and includes a "minimized" state with square corners [tokens].
- mdc-android states [mdc-android]:
  - `STATE_COLLAPSED` (peek)
  - `STATE_EXPANDED`
  - `STATE_HALF_EXPANDED` (only when `fitToContents=false`)
  - `STATE_HIDDEN`
  - `STATE_DRAGGING`
  - `STATE_SETTLING`

**Anatomy [m3 page]**
1. Container (the only required element)
2. Drag handle (optional)
3. Scrim (modal only)
4. Optional content: list items, dividers, media (thumbnail, image, video)

**Measurements**
- Width: full window width up to a **640dp max** [m3 page; mdc-android `maxWidth` 640dp].
- Margins [m3 page]:
  - Top margin 72dp.
  - When the window is wider than 640dp: top margin 56dp and start/end margins 56dp.
  - Height is variable.
- Corner radius: 28dp, top corners only (`corner.extra-large.top`); 0dp when minimized [tokens].
- Elevation: 1dp (level1) for both standard and modal [tokens, mdc-android].
- **Drag handle:** 32×4dp, centred, with 22dp padding above and below [tokens, m3 page]. That gives 22 + 4 + 22 = 48dp, so "the top 48dp portion of the bottom sheet is interactive" [m3 page]. `BottomSheetDragHandleView` has a min size of 48×48dp [mdc-android].
- Modal initial position is capped at **50% of the screen height**. Taller content can then be pulled to full screen and scrolled [m3 page].
- mdc-android behaviour defaults [mdc-android]:

  | Behaviour | Default |
  |---|---|
  | `peekHeight` | auto |
  | `hideable` | false (standard), true (modal) |
  | `skipCollapsed` | false |
  | `fitToContents` | true |
  | `draggable` | true |
  | `halfExpandedRatio` | 0.5 |
  | `expandedOffset` | 0dp |
  | `significantVelocityThreshold` | 500 px/s |

**Typography**
- n/s; the content uses each inner component's own type.

**Colour roles**
- Container `surface-container-low` [tokens, m3 page].
- Drag handle `on-surface-variant` at 0.4 opacity [tokens].
- Scrim: role `scrim`. "On Android platforms, the scrim color and opacity is automatically handled by the system UI" [m3 page].
- Focus ring `secondary` (3dp, 2dp offset) [tokens].
- mdc-android gradient protection uses `colorSurfaceContainerLow` [mdc-android].

**States**
- The drag handle is focusable and shows a focus ring [m3 page, tokens].
- Sheet states: collapsed, expanded, half-expanded, hidden, dragging and settling [mdc-android].

**Behaviour & motion**
- An expansion option toggles between collapsed and fully raised [m3 page].
- Dragging or selecting the drag handle cycles through preset heights or closes the sheet. Selecting the scrim always closes it [m3 page].
- "Sheets should be able to cycle through preset heights and close completely without dragging" [m3 page].
- Modal dismissal [m3 page]:
  - Tap an item or action in the sheet.
  - Tap the scrim.
  - Swipe the sheet down.
  - Use the app-bar close affordance (required when the sheet is full-screen).
- Content scrolls once it exceeds the visible height. The page also says bottom sheets "can be horizontally scrolled, independent of the rest of the screen's content" [m3 page].
- **Predictive back**: the sheet detaches from the left and right edges and the previous screen previews. Release or fling commits; cancel restores [m3 page].
  - Modal `BottomSheetDialog` supports it automatically.
  - Standard sheets need a back callback that forwards events to `BottomSheetBehavior` [mdc-android].
- mdc-android drag handle: tap cycles expanded/collapsed and double-tap hides. Edge-to-edge insets are handled, and the dialog pads the top under the status bar [mdc-android].

**Adaptive behaviour**
- Compact (<600): full screen width, elevated above the content [m3 page].
- Medium (600–839) and expanded (840–1199): the default 640dp max width (overridable) applies, with 56dp margins once the window exceeds 640dp [m3 page].
- Expanded/desktop: "a bottom sheet can be swapped for a side sheet" [m3 page].
- Breakpoints page, supplemental selection: bottom sheet at compact → menu at medium and expanded [m3 foundations]. In the supporting-pane layout at compact, a bottom sheet holds the supporting content [m3 foundations].
- Large and extra-large: n/s.

**Accessibility [m3 page]**
- People must be able to resize the sheet without touch gestures. Provide a single-pointer alternative for any drag. If there is no drag handle, add a button that cycles the heights.
- Keyboard: Tab lands on the drag handle; Space/Enter toggles between available heights.
- Label only the drag handle, with role **button**.
- `BottomSheetDragHandleView` handles TalkBack, Voice Access and Switch Access expand/collapse automatically [mdc-android].
- Modal focus-trap behaviour: n/s on this page (modal sheets "like dialogs" block the app).

**Do / Don't [m3 page]**
- Keep the modal's initial height at 50% or less so top actions are reachable.
- Show a close affordance in full-screen modal sheets.
- Keep content supplementary, not the main content.
- Don't use a modal bottom sheet outside mobile. Use a side sheet, menu or dialog at larger sizes.
- Reserve the top 48dp for the resize interaction when a drag handle is present.

---

## 6. Side sheets (standard, modal; docked or detached)
Page updated 2026-07-28.

**Status**
- Baseline M3; no Expressive update or deprecation [m3 page].
- Differences from M2: RTL support with a left-edge side sheet; new colour mappings; "Modal side sheets have a 16dp corner radius" [m3 page].
- Introduced in MDC-Android 1.8.0 [mdc-android].

**Purpose & when to use / not use [m3 page]**
- Optional content and actions that don't interrupt the main content, such as filters or supplemental details and features. A sheet can navigate to another region within itself (back icon).
- Standard: "used mostly in medium to expanded breakpoints". It stays visible while people use the primary content.
- Modal: "preferred in compact breakpoints"; it must be dismissed before the underlying content can be used.
- Fixed width, typically spanning the screen height. Use a side sheet to organise many filter chips [m3 page, chips].

**Variants / configurations**
- Standard vs modal [m3 page].
- Docked (to the edge) vs **detached**: inset 16dp, with all corners rounded [m3 page, tokens].
- Edge: right by default, or left for RTL. The mdc-android sheet edge defaults to `end`, with start/end following the layout direction [m3 page, mdc-android].
- **Coplanar** (mdc-android): a standard sheet that "squashes" a sibling view instead of overlapping it. "Not recommended for narrow screens" [mdc-android].
- The m3 page describes the standard sheet as shrinking the body area ("the body area shrinks to accommodate the sheet's width while maintaining a margin on the body's trailing edge") [m3 page].

**Anatomy [m3 page]**
- Standard:
  1. Divider (optional)
  2. Headline
  3. Container
  4. Close icon button
- Modal:
  1. Back icon button (optional)
  2. Headline
  3. Container
  4. Close icon button
  5. Divider (optional)
  6. Action buttons (optional)
  7. Scrim
- The container is the only required element.

**Measurements**

| Attribute | Standard | Modal |
|---|---|---|
| Start/end padding | 24dp | 24dp (16dp start padding with a back icon) |
| Padding between top elements | 12dp | 12dp |
| Bottom actions | 72dp tall; 16dp top padding, 24dp bottom padding; left-aligned | same |
| Max width | 400dp | 400dp |
| Margins when detached | 16dp | 16dp |
| Corner radius | 0dp docked | 16dp on the inner corners (`corner.large.start`: top-left and bottom-left) |
| Detached corner radius | 16dp all corners | 16dp all corners |
| Elevation | 0dp | 1dp (level1) |
| Height | 100% | 100% |

Padding, bottom actions, max width and margins are [m3 page]. Corner radii, elevation and height are [tokens].

- Default docked width token is **256dp**, vs the page's 400dp max [tokens].
- Breakpoints page: "side sheets have a default maximum width of 400dp", compared with 412dp fixed panes at extra-large [m3 foundations].
- mdc-android: shape `shapeAppearanceCornerLarge`; elevation attribute 0dp; maxWidth not set [mdc-android].

**Typography**
- Headline: title-large (22/28, w400) [tokens].
- Action labels follow the button roles [tokens].

**Colour roles**
- Standard: container `surface`; headline `on-surface-variant`; icons `on-surface-variant`; divider `outline` per token (the page diagram's item 1 is "Outline variant") [tokens, m3 page].
- Modal: container `surface-container-low`; headline and icons `on-surface-variant` [tokens, m3 page].
- Actions: `primary` label and state layer [tokens].
- Focus ring: `secondary` [tokens].
- Scrim colour and opacity: n/s.

**States**
- Action state layers in `primary` (0.08 / 0.10 / 0.10) [tokens].
- Sheet states: expanded, hidden, dragging, settling [mdc-android].

**Behaviour & motion**
- Scrolls vertically and independently of the page; scroll positions persist. "Side sheets cannot scroll horizontally" [m3 page].
- Modal dismissal: tap the scrim, swipe the sheet off-screen horizontally, or use close or Back [mdc-android, m3 page].
- **Predictive back** [m3 page]:
  - The sheet detaches from the top and bottom edges.
  - The previous screen previews.
  - The sheet and its content scale in the direction of the gesture.
  - Modal `SideSheetDialog` supports it automatically; standard and coplanar sheets need a back callback [mdc-android].
- A standard sheet's entrance and exit animate the body area resizing [m3 page].

**Adaptive behaviour**
- Compact (<600): modal preferred [m3 page].
- Medium (600–839) and expanded (840–1199): standard sheets are the main use. "Modal side sheets on smaller screens can transition to standard side sheets at larger screen sizes" [m3 page].
- Bottom sheets swap to side sheets on desktop [bottom-sheets page].
- Extra-large (≥1600): a standard side sheet may serve as the **third pane**. The navigation rail may stay, collapse or hide. No more than 3 panes [m3 foundations].
- RTL: the sheet appears on the left edge with all elements reversed [m3 page].
- Large (1200–1599): n/s.

**Accessibility [m3 page]**
- "Material requires that a close affordance, such as a close icon button, is always present within a side sheet."
- People must be able to dismiss the sheet with assistive technology.
- Focus order example: headline → close → cancel → save.
- Keys: Tab moves to non-disabled icon buttons; Space/Enter activates them.
- Role: **Dialog**.
- Focus trap: n/s on this page.

**Do / Don't [m3 page]**
- Place sheets on the screen edge, usually the right, to avoid conflicting with left navigation. An inset of up to 16dp is fine; don't inset further.
- Always include a close icon button.
- Don't allow or imply horizontal scrolling.
- Use dividers to separate action buttons from content, or user-generated content from system-generated content.
- Use elevation, fill and tone to emphasise key actions.

---

## 7. Divider (full-width, inset, middle-inset; horizontal and vertical)
Page updated 2026-07-17.

**Status**
- Baseline M3; no Expressive update or deprecation [m3 page].
- Differences from M2: new colour mapping; "Ability to have vertical dividers" [m3 page].
- Expressive list guidance moves list separation toward gaps; dividers are for "uncontained or complex lists" [lists page].

**Purpose & when to use / not use [m3 page]**
- "Make dividers visible but not bold." "Only use dividers if items can't be grouped with open space." "Use dividers to group things, not separate individual items."
- Full-width dividers separate larger sections of unrelated content, or interactive from non-interactive areas (for example, a card body vs its "Read more" link).
- Inset dividers separate related content within a section, anchored by icons or avatars and aligned to the leading edge.
- Lists with repetitive formats may need only margins, no dividers.

**Variants / configurations**
- Full-width, inset and middle-inset (both sides) [m3 page].
- Vertical, for large screens (for example, text vs media) [m3 page].
- mdc-android adds a "heavy" 8dp divider for major section breaks, and `MaterialDividerItemDecoration` for RecyclerView with an option to skip the last item [mdc-android].

**Anatomy**
1. Divider: a simple line [m3 page].

**Measurements**
- Thickness 1dp [tokens].
- Page table [m3 page]:
  - Full-width: 100%.
  - Inset: 16dp left, 0dp right.
  - Middle-inset: 16dp left, 16dp right.
  - 4dp between the divider and supporting text.
  - "Divider right margin" 8dp and "Divider bottom margin" 8dp (context unstated).
- Within lists: list tokens give 16dp leading and trailing space and 0dp above and below [tokens]. The baseline list table gives a 16dp left and 24dp right inset [lists page].
- mdc-android: insets default to 0dp (full-bleed); heavy divider 8dp; `lastItemDecorated` true [mdc-android].

**Typography**
- n/a.

**Colour roles**
- `outline-variant` [tokens, m3 page, mdc-android].
- Exceptions inside other components [tokens]: list divider `outline`; dialog divider `outline`; full-screen dialog divider `surface-variant`; side sheet divider `outline`.

**States**
- None; dividers are non-interactive.

**Behaviour & motion**
- None.
- Cards: use full-width dividers for expandable content and inset dividers for related content [cards page].

**Adaptive behaviour**
- Vertical dividers on larger screens [m3 page].
- Per-size rules otherwise n/s.

**Accessibility**
- "Dividers are decorative elements, which have no contrast minimums" [m3 page].
- No special handling is needed [mdc-android].

**Do / Don't [m3 page]**
- When both kinds are on one screen, use full-width dividers for different kinds of content and inset dividers for nested items, so they reinforce the hierarchy.
- Use full-width dividers sparingly; too many clutter the UI.
- Use inset dividers with anchoring elements such as icons or avatars.
- Prefer open space and margins when items repeat a format.

---

## 8. Chips (assist, filter, input, suggestion; flat or elevated)
Page updated 2026-07-17.

**Status**
- Baseline M3; no Expressive update or deprecation [m3 page].
- **Aug 2024**: "Updated stroke color from **outline** to **outline variant**", softened "to improve visual hierarchy between chips and buttons" [m3 page].
- Differences from M2: new colours; a "Rounded rectangle" shape; M2 action chips split into assist and suggestion chips; "Choice chips are now a subset of filter chips" [m3 page].
- No size variants (single 32dp height). Density is opt-in only (see Accessibility) [m3 page].

**Purpose & when to use / not use [m3 page]**
- Help people enter information, make selections, filter content or trigger actions in context. "Chips aren't buttons": chips are dynamic forking options, buttons are persistent linear steps.
- Don't use chips for major or progressive actions (Save, Cancel, "Save task"). Don't show a single chip alone; chips come in sets.
- Choose by purpose and author:

  | Variant | Purpose | Example |
  |---|---|---|
  | Assist | smart or automated actions, possibly across apps | "Add to calendar" |
  | Filter | filters for a collection | multi- or single-select platform filters |
  | Input | user-entered information | a Gmail contact in "To" |
  | Suggestion | product-generated suggestions | a quick reply |

**Variants / configurations**
- Every variant comes flat (outlined) or elevated. Elevated is only for chips over images or dynamic backgrounds [m3 page, tokens]. mdc-android has explicit Elevated styles for assist, filter and suggestion [mdc-android].
- Selection: filter and input chips have selected and unselected states. Filter sets are multi-select or single-select; don't mix behaviours on one page [m3 page].
- Trailing icon: required on input chips (remove). Optional on filter chips (remove or open a menu, at medium/expanded sizes) [m3 page].
- Leading element: an icon, logo or circular image. Input chips can lead with a 24dp avatar [m3 page].
- Layout: chip sets scroll horizontally on one row or wrap to more rows. If filter chips need more than 2 rows, consider horizontal scroll [m3 page]. mdc-android `ChipGroup` offers `singleLine`, `singleSelection` and `selectionRequired` [mdc-android].

**Anatomy [m3 page]**
1. Container
2. Label text
3. Leading icon or image (optional)
4. Trailing icon (required for input, optional for filter)

By variant:
- Assist: container, label, leading icon.
- Filter: container, label, leading icon, trailing icon.
- Input: container, label, trailing icon, leading icon or avatar.
- Suggestion: container, label (plus an optional leading icon in the tokens).

**Measurements [m3 page] + [tokens]**

| Attribute | Assist | Filter | Input | Suggestion |
|---|---|---|---|---|
| Height | 32dp | 32dp | 32dp | 32dp |
| Corner radius | 8dp (small) | 8dp | 8dp | 8dp |
| Icon size | 18dp | 18dp | 18dp (leading and trailing) | 18dp |
| Avatar | – | – | 24dp, circular (page: "12dp corner radius") | – |
| L/R padding, no icon | 16dp | 16dp | – | 16dp |
| L/R padding with icon | 8dp | 8dp | 8dp | 8dp |
| Avatar padding | – | – | 4dp left, 8dp right | – |
| Gap between elements | 8dp | 8dp | 8dp | 8dp |
| Outline (flat) | 1dp | 1dp unselected, 0dp selected | 1dp unselected, 0dp selected | 1dp |
| Elevation | flat 0dp, elevated 1dp, elevated hover 3dp, dragged 8dp | same | 0dp, dragged 8dp | same as assist |

- Labels are vertically centred and start-aligned [m3 page].
- Spacing between chips: at least 8dp [m3 page]; `ChipGroup` `chipSpacing` 8dp [mdc-android].
- Target size: at least 48dp regardless of density; the target may extend beyond the visible chip. The input-chip close-icon target is at least 48dp [m3 page].
- Two actions (for example, edit/drag plus remove) need two 48×48dp targets: give the chip a **min width of 88dp** or the label a min width of **42dp** [m3 page].
- mdc-android [mdc-android]:
  - min height 32dp; chip padding 4dp start / 6dp end; text padding 8dp start / 6dp end.
  - chip and close icons 18dp; close-icon end padding 4dp (input).
  - min touch target 48dp, with `ensureMinTouchTargetSize` true via an `InsetDrawable`.

**Typography [tokens]**
- Labels: label-large (14/20, w500) for all variants, "the same typography style as buttons" [m3 page].
- Keep labels to 20 characters or fewer [m3 page].

**Colour roles [tokens]**
- Assist:
  - Label `on-surface`; icon `primary` (customisable to `on-surface-variant` for less emphasis [m3 page]).
  - Flat outline `outline-variant`; focus outline `on-surface`.
  - Elevated container `surface-container-low`.
  - State layer `on-surface`.
- Filter, unselected:
  - Label `on-surface-variant`.
  - Leading icon: `primary` in the "with-leading-icon" token, `on-surface-variant` in the "with-icon" token.
  - Trailing icon `on-surface-variant`.
  - Outline `outline-variant`; focus outline `on-surface-variant`.
  - Elevated container `surface-container-low`.
- Filter, selected:
  - Container `secondary-container`, outline 0dp.
  - Label and icons `on-secondary-container`.
  - Flat selected chips rise to 1dp on hover.
  - State layers: selected pressed uses `on-surface-variant`; unselected pressed uses `on-secondary-container`. The tokens are swapped as listed.
- Input, unselected:
  - Label `on-surface-variant`; leading icon `on-surface-variant` (`primary` on hover, focus and press); trailing icon `on-surface-variant`.
  - Outline `outline-variant` (a generic `outline` token also exists); focus outline `on-surface-variant`.
- Input, selected:
  - Container `secondary-container`, outline 0dp.
  - Label and trailing icon `on-secondary-container`; leading icon `primary`.
- Suggestion:
  - Label `on-surface-variant`; leading icon `primary`.
  - Flat outline `outline-variant` (the page diagram still says "Outline"); focus outline `on-surface-variant`.
  - Elevated container `surface-container-low`.
- Disabled (all variants): label and icons `on-surface` at 0.38; flat outline `on-surface` at 0.12; elevated or selected container `on-surface` at 0.12; avatar at 0.38.
- Focus ring: `secondary` (3dp, 2dp offset).
- mdc-android: text `colorOnSurfaceVariant`; ripple `colorOnSecondaryContainer` at 12%; stroke 1dp [mdc-android].

**States**
- Every variant documents enabled, disabled, hovered, focused, pressed and dragged states, in selected and unselected forms where they apply [m3 page].
- Dragged chips rise to 8dp [tokens].
- Don't use elevation to show the pressed state; use the ripple [m3 page].
- Filter chips add a leading checkmark when selected [m3 page].

**Behaviour & motion [m3 page]**
- Assist chips can turn into modals or full-screen views, or expand results inline. They can show progress and confirmation, with labels updating (Save → Saved).
- Filter chips toggle. Single-select sets auto-deselect the others. A filter chip can open a menu; at compact sizes the *whole chip* should open it. Filter chip suggestions can change dynamically.
- Input chips:
  - Convert typed text into chips; editing reverts a chip to text.
  - Backspace before a chip selects it, and a second Backspace deletes it.
  - Can be reordered or moved between fields.
  - Can expand via container transform.
  - Overflowing chips behave like text: an unfocused field shows the start, and focusing jumps to the end.
- Suggestion chips sit inline in rows, never stacked vertically. Overflow wraps, or scrolls horizontally if the field is one row high. Labels truncate when wrapped or wider than the window.

**Adaptive behaviour [m3 page]**
- Medium (600–839) and expanded (840–1199): filter chips may carry a trailing remove or menu icon.
- Compact (<600): the trailing icon target is too small on its own, so make the whole chip perform the action.
- Large numbers of filter chips can live in a side sheet.
- Breakpoints page: "Don't swap a button for a chip" [m3 foundations].
- Large and extra-large: n/s.

**Accessibility [m3 page]**
- The chip label needs at least 3:1 contrast with the background.
- An action chip exposes button semantics.
- Show interactivity with a secondary cue (required). Options:
  - A group label such as "Select type".
  - Page context such as "Filter results".
  - The `outline` role instead of `outline-variant`, for a 3:1 boundary.
  - An action-verb label or a leading icon.
- Horizontal overflow: provide a way to see everything without scrolling.
  - Reflow: a leading "Show all" filter chip pushes the content below down.
  - Menu: a leading button lists all options. Not for chips with a second action.
- Don't apply density by default; offer it as a user choice, and keep the density toggle's targets at 48×48dp or more.
- Keys:
  - Tab moves to a chip or chip group.
  - Space/Enter activates, selects or deselects.
  - Backspace/Delete removes the focused input chip.
  - Arrows move between chips.
- Roles:

  | Chip type | Web | MDC-Android | Compose |
  |---|---|---|---|
  | Basic chip (one action) | gridcell | button | button |
  | Selectable chip | gridcell | radio button | checkbox |
  | Chip with two actions | button or checkbox | button or checkbox | button or checkbox |

  Label = the chip text. Remove is labelled "Remove {chip content}". Hide decorative images.
- Focus: a chip with only a remove action is one focusable element. With a second action (select), the chip and the remove icon are two separate focus stops.
- On mobile, if remove is the only action, the icon can be omitted; select the chip and press Delete.

**Do / Don't [m3 page]**
- Don't elevate chips placed directly on the page; elevate only over images.
- Keep labels short (20 characters or fewer) and skip articles. Write filter chips as inclusive nouns (not "Exclude images"). Assist chips start with a verb.
- Use buttons, not chips, for the final step of a task.
- Never show a single chip, or a filter group with only one option.
- Keep at least 8dp between chips and 48dp targets.
- Don't mix single-select and multi-select chip sets on one page.
