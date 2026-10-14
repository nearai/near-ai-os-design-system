# Unity web sources: Editor Foundations and App UI 3.0

Research stream: Unity web sources, as the benchmark for the NEAR AI parent design system (Desktop / Web / Mobile; parent of the trace-commons macOS "glass" language).
Collected 2026-10-13. Every page was fetched raw with curl/urllib and parsed with local Python. WebFetch summaries were not used. Downloaded content was treated as data only.

---

## 0. Scope, coverage and method

### 0.1 Sources covered

**A. Unity Editor Foundations (www.foundations.unity.com).** Webflow site, last published 2026-10-02. It has no sitemap: `/sitemap.xml` returns the Webflow 404 page. I crawled the site breadth-first from `/` across the nav and every in-site link, and found **47 unique pages**. All 47 are in the corpus.

| Area | Pages (path under https://www.foundations.unity.com) |
|---|---|
| Hub | `/`, `/getting-started`, `/changelog`, `/feedback`, `/resources`, `/fundamentals`, `/patterns`, `/components` |
| Fundamentals (7) | `/fundamentals/accessibility`, `/color-palette`, `/iconography`, `/interactions`, `/typography`, `/ui-copy-style` (titled "UI Writing Guide"), `/ux-essentials` |
| Patterns (10) | `/patterns/authoring-flows`, `/content-organization`, `/contextual-tooling`, `/empty-states`, `/errors-and-messaging`, `/inheritance`, `/overlays`, `/project-settings-preferences`, `/selection-history-navigation`, `/windowing` (`/patterns/windows` 301-redirects here) |
| Components (22) | `/components/button`, `color-field`, `dropdown`, `foldout`, `help-box`, `label`, `list-view`, `multi-column-views`, `numeric-field`, `object-field`, `progress-bar`, `radio-button`, `reorderable-list`, `scroll-view`, `search-field`, `slider`, `tab`, `text-field`, `toggle`, `toolbar`, `tooltip`, `tree-view` |

Broken in-site links (404 on the live site): `/fundamentals/ui-writing-guide`, `/tree-view`, `/patterns/menus`. The Interactions page links "Patterns > Menus" for context-menu guidance, but that page does not exist.
I also probed 33 plausible unlisted slugs, including `components/menu`, `components/dialog`, `fundamentals/layout`, `fundamentals/spacing`, `fundamentals/motion` and `fundamentals/density`. All returned 404.
**There is no dedicated layout/grid, spacing, motion, density, dialog or menu page.** That guidance is scattered across Content Organization, Windowing, Errors & Messaging, component pages and the Project Settings pattern, and it is consolidated in §1.9 below.
Most pages are labelled "LTS 2022.3". Help Box is labelled "6.5" and Tab "2023.2". Content is written for both of Unity's frameworks: UI Toolkit (UITK, web-like, recommended) and IMGUI (legacy, code-driven).

**B. App UI 3.0 manual.** https://docs.unity3d.com/Packages/com.unity.dt.app-ui@3.0/manual/. The DocFX TOC (`toc.html`) lists **39 pages**, and all 39 were crawled. `toc.json` returns 404.
App UI 3.0 has no per-component manual pages, and neither do 1.0–2.1 (their TOCs list the same ~36 conceptual pages). Component documentation lives in the **API reference**. I therefore also fetched **434 API pages**: every type in `Unity.AppUI.UI`, `Core`, `Navigation`, `MVVM`, `Redux` and `Undo`, taken from `api/toc.html`, which lists 569 entries. I compacted them to summary, remarks, variants, USS class constants and properties.

**C. App UI 3.0 package source (tokens).** Registry: `https://packages.unity.com/com.unity.dt.app-ui`. dist-tag `latest` = 2.1.14. The 3.x line is **3.0.0-pre.1** (2026-07-31, minimum Unity 6000.3, sha1 `ed9cc22016b8fe20e68a0b57166d16b2bb20c679`).
I downloaded the 36 MB tarball into its own directory and extracted **only** `.uss/.tss/.md` and `package.json` (199 files). No code was executed. I wrote a resolver that computes every custom property for each **theme × scale** combination (4 × 3), plus resolved dimensions for all 84 component stylesheets.

### 0.2 Corpus locations (scratchpad)

- `corpus/unity-web/foundations/*.txt`: 47 page texts (structured markdown-ish, image alt text kept)
- `corpus/unity-web/foundations_unity_color_vars.txt`: 106 `--unity-*` variables with light/dark values
- `corpus/unity-web/appui-manual/*.txt`: 39 manual pages
- `corpus/unity-web/appui-api/appui_api_compact.txt`: 434 API types, compacted (~58k words)
- `corpus/unity-web/appui-tokens/`: `appui_tokens_semantic_by_theme.txt`, `appui_tokens_by_scale.txt` and `appui_components_resolved.txt` (all 84 component USS files resolved per scale and theme)
- Raw HTML: `downloads/unity-web/foundations/html/`, `downloads/unity-web/appui/{manual,api}/`. Extracted package: `downloads/unity-web/appui-pkg/extract/`

### 0.3 What could not be accessed or does not exist
- Foundations sitemap: none (404). The crawl via nav replaced it.
- Three Foundations pages are linked but 404 (listed above). Several numeric specs exist only inside diagram images. I checked the key diagrams for buttons, the text field and foldout indentation, and the text already carries the same numbers.
- Expandable "UX essentials" cards hide their body inside Webflow `<nav class="w-dropdown-list">`. The extractor was fixed to include them, so the standard texts (US-0171, US-0205, US-0212/0213/0216–0219) are captured.
- "See standard on GitHub" links point to an internal Unity host (`github.cds.internal.unity3d.com`). That host is not public and was not accessed.
- App UI 3.0 is **pre-release** and the manual flags App UI as "experimental… provided as is". The API pages for 3.0 are complete.
- Figma toolkits linked from Foundations are out of scope; the other stream covers them.

---

## 1. Editor Foundations: principles and fundamentals

### 1.1 Purpose and principles
Source: https://www.foundations.unity.com/getting-started

- **Audience:** "technical and non technical creators, engineers, designers, product managers". Goals: define best practices, give design rationale, keep docs current for the latest LTS, and create a feedback loop.
- **Three usability principles:**
  1. **Users first**: research-informed; creator goals at the heart of every decision; a consistent foundation that accelerates creativity.
  2. **Driving alignment**: a common designer/engineer language; "balance ideal design best practices with how the Editor realistically works"; unified look and behaviour.
  3. **Authentically Unity**: evolve with creators; prioritise bold enhancements.
- **Framework stance:** UITK is recommended for new work. IMGUI is still documented because most of the Editor uses it. Every component page carries parallel "UI Toolkit / IMGUI" API references and a UI Builder availability badge. This dual-implementation documentation model applies to us too: SwiftUI (trace-commons) versus web.
- **UX Essentials** (https://www.foundations.unity.com/fundamentals/ux-essentials) are numbered, testable standards ("Unity Standard US-0xxx") surfaced on every relevant page as checklist cards:
  - US-0171: UI does not use colour as the only interaction indicator.
  - US-0205: Windows with no content use empty states.
  - US-0212: Action-oriented menu and button labels use verbs, no longer than three words.
  - US-0213: Labels do not end with punctuation (no colons, full stops or question marks).
  - US-0216: All UI uses Inter (fallbacks: Verdana on Windows and Linux, Lucida Grande on macOS).
  - US-0217: Use the default 12 px font size wherever possible.
  - US-0218: Padding exists between text and other UI elements.
  - US-0219: Text is left-aligned in windows, dialogs, tabs, dropdowns and menus. Only button labels are centred (plus empty-state content).
  - US-0201: UI localization accounts for text expansion.
  - Unnumbered essentials:
    - Disable versus hide (see §1.6).
    - Blue links only for leaving the Editor.
    - In Inspector-like windows, every input has a label and a tooltip.
    - Tooltips are complete sentences.
    - Dockable windows include a tab and a window menu.
    - Windows persist through restarts.
    - Support min/max window sizes, with **no horizontal scrolling at the Inspector's minimum width of 275 px**.
    - Overlay shortcuts: `` ` `` opens the overlay menu at the cursor, Ctrl+`` ` `` toggles all overlays, and right-clicking an overlay header opens its options.
  - *Benchmark value:* standards are atomic, numbered and checkable. This is a good model for our own lint/QA checklist.

### 1.2 Colour system
Source: https://www.foundations.unity.com/fundamentals/color-palette

**Philosophy**
- Colour supports information architecture and signals priority.
- "Limit colour usage in the Editor to a **subtly nuanced palette** to avoid overwhelming the user interface with an excess of overly bright colours."
- Two themes, **light and dark**, chosen by personal preference: "users spend many hours in the Editor… reduce eye strain".
- **Never hard-code colours**; always use variables. New variables can be created as needed.

**Variable naming grammar** (an exact, reusable pattern):
`--unity-{group}-{role_and_control}-{sub_element}-{pseudo_state_sequence}`
- Parts are separated by hyphens, and words within a part by underscores. Example: `--unity-colors-toolbar_button-text-hover`.
- **Multiple pseudo-states are listed in alphabetical order, joined by underscores.** Example: `--unity-colors-toolbar_button-text-focus_selected`.
- Pseudo-state vocabulary:

| State | Meaning |
|---|---|
| (none) | normal / idle |
| `checked` | a toggle-type control is on (checkbox, tab, toolbar button) |
| `disabled` | the control is disabled |
| `focus` | the control has focus |
| `hover` | the pointer is over the control |
| `inactive` | a selected control does not have focus |
| `pressed` | the control is pressed and active (buttons) |
| `selected` / `highlighted` | selected items (tree/list rows, text selection) |

**Depth model: "flat design" with three base layers (no shadows)**
- "Avoid using shadows excessively to add depth. Instead use **accented borders and base layers**."
- **Accented borders**: inset borders for input fields (a darker top/accent border) and outset borders for click controls. Example: the text field "is inset and has a different top border colour". Each control has `-border` and `-border_accent` variables.
- **Base layers**, "like sheets of paper on a desk", go dark to light:
  - **Base 1**: application bar and controls
  - **Base 2**: components and windows
  - **Base 3**: toolbars and toolbar controls
- Content Organization adds a rule that **backgrounds get darker as content gets more detailed**: selected-object header and component headers are lighter, and controls and sub-controls are darker.

**Exact Editor colour variables (light / dark).** 98 colour variables were extracted from Color Palette and the component pages. Values are as published; Unity omits the `#` on several values.

| `--unity-colors-…` | Light | Dark |
|---|---|---|
| `alternated_rows-background` | #CACACA | #3F3F3F |
| `app_toolbar-background` | #8A8A8A | #191919 |
| `app_toolbar_button-background` | #C8C8C8 | #383838 |
| `app_toolbar_button-background-checked` | #656565 | #6A6A6A |
| `app_toolbar_button-background-hover` | #BBBBBB | #424242 |
| `app_toolbar_button-background-pressed` | #656565 | #6A6A6A |
| `app_toolbar_button-border` | #6B6B6B | #191919 |
| `app_toolbar_button-border_accent` | #6B6B6B | #222222 |
| `button-background` | #E4E4E4 | #585858 |
| `button-background-focus` | #BEBEBE | #6E6E6E |
| `button-background-hover` | #ECECEC | #676767 |
| `button-background-hover_pressed` | #B0D2FC | #4F657F |
| `button-background-pressed` | #96C3FB | #46607C |
| `button-border` | #B2B2B2 | #303030 |
| `button-border-pressed` | #707070 | #0D0D0D |
| `button-border_accent` | #939393 | #242424 |
| `button-border_accent-focus` | #018CFF | #7BAEFA |
| `button-text` | #090909 | #EEEEEE |
| `default-background` | #A5A5A5 | #282828 |
| `default-border` | #999999 | #232323 |
| `default-text` | #090909 | #D2D2D2 |
| `default-text-hover` | #090909 | #BDBDBD |
| `dropdown-background` | #DFDFDF | #515151 |
| `dropdown-background-hover` | #E4E4E4 | #585858 |
| `dropdown-border` | #B2B2B2 | #303030 |
| `dropdown-border_accent` | #939393 | #242424 |
| `dropdown-text` | #090909 | #E4E4E4 |
| `error-text` | #5A0000 | #D32222 |
| `headerbar-background` | #CBCBCB | #3C3C3C |
| `headerbar_column-background` | #CBCBCB | #3C3C3C |
| `headerbar_column-background-hover` | #C1C1C1 | #464646 |
| `headerbar_column-background-pressed` | #EFEFEF | #505050 |
| `helpbox-background` | rgba(235, 235, 235, 0.20) | rgba(96, 96, 96, 0.20) |
| `helpbox-border` | #A9A9A9 | #232323 |
| `helpbox-text` | #161616 | #BDBDBD |
| `highlight-background` | #3A72B0 | #2C5D87 |
| `highlight-background-hover` | rgba(0, 0, 0, 0.06) | rgba(256, 256, 256, 0.06) |
| `highlight-background-hover-lighter` | #9A9A9A | #5F5F5F |
| `highlight-background-inactive` | #AEAEAE | #4D4D4D |
| `highlight-text` | #0032E6 | #4C7EFF |
| `highlight-text-inactive` | #FFFFFF | #FFFFFF |
| `input_field-background` | #F0F0F0 | #2A2A2A |
| `input_field-border` | #B7B7B7 | #212121 |
| `input_field-border-focus` | #1D5087 | #3A79BB |
| `input_field-border-hover` | #6C6C6C | #656565 |
| `input_field-border_accent` | #A0A0A0 | #0D0D0D |
| `inspector_titlebar-background` | #CBCBCB | #3E3E3E |
| `inspector_titlebar-background-hover` | #D6D6D6 | #474747 |
| `inspector_titlebar-border` | #7F7F7F | #1A1A1A |
| `inspector_titlebar-border_accent` | #BABABA | #303030 |
| `label-text` | #090909 | #C4C4C4 |
| `label-text-focus` | #003C88 | #81B4FF |
| `link-text` | #4C7EFF | #4C7EFF |
| `object_field-background` | #EDEDED | #282828 |
| `object_field-border` | #B0B0B0 | #202020 |
| `object_field-border-focus` | #1D5087 | #3A79BB |
| `object_field-border-hover` | #6C6C6C | #656565 |
| `object_field_button-background` | #DEDEDE | #373737 |
| `object_field_button-background-hover` | #CCCCCC | #4C4C4C |
| `preview_overlay-text` | #FFFFFF | #DEDEDE |
| `scrollbar_button-background` | rgba(0, 0, 0, 0.05) | rgba(0, 0, 0, 0.05) |
| `scrollbar_button-background-hover` | #A7A7A7 | #494949 |
| `scrollbar_groove-background` | rgba(0, 0, 0, 0.05) | rgba(0, 0, 0, 0.05) |
| `scrollbar_groove-border` | rgba(0, 0, 0, 0.10) | rgba(0, 0, 0, 0.10) |
| `scrollbar_thumb-background` | #9A9A9A | #5F5F5F |
| `scrollbar_thumb-background-hover` | #8E8E8E | #686868 |
| `scrollbar_thumb-border` | #B9B9B9 | #323232 |
| `scrollbar_thumb-border-hover` | #8E8E8E | #686868 |
| `slider_groove-background` | #8F8F8F | #5E5E5E |
| `slider_groove-background-disabled` | #A4A4A4 | #575757 |
| `slider_thumb-background` | #616161 | #999999 |
| `slider_thumb-background-disabled` | #9B9B9B | #666666 |
| `slider_thumb-background-hover` | #4F4F4F | #EAEAEA |
| `slider_thumb-border` | #616161 | #999999 |
| `slider_thumb-border-disabled` | #666666 | #666666 |
| `slider_thumb_halo-background` | rgba(12, 108, 203, 0.50) | rgba(16, 111, 205, 0.50) |
| `tab-background` | #B6B6B6 | #353535 |
| `tab-background-checked` | #CBCBCB | #3C3C3C |
| `tab-background-hover` | #B0B0B0 | #303030 |
| `tab-text` | #090909 | #BDBDBD |
| `toolbar-background` | #CBCBCB | #3C3C3C |
| `toolbar-border` | #999999 | #232323 |
| `toolbar_button-background` | #CBCBCB | #3C3C3C |
| `toolbar_button-background-checked` | #EFEFEF | #505050 |
| `toolbar_button-background-focus` | #C1C1C1 | #464646 |
| `toolbar_button-background-hover` | #C1C1C1 | #464646 |
| `toolbar_button-border` | #999999 | #232323 |
| `toolbar_button-text` | #090909 | #C4C4C4 |
| `toolbar_button-text-checked` | #090909 | #C4C4C4 |
| `toolbar_button-text-hover` | #090909 | #BDBDBD |
| `tooltip-background` | #DEDEDE | #373737 |
| `tooltip-border` | #8A8A8A | #191919 |
| `visited_link-text` | #AA00AA | #FF00FF |
| `warning-text` | #333308 | #F4BC02 |
| `window-background` | #C8C8C8 | #383838 |
| `window-border` | #939393 | #242424 |
| `window-text` | #090909 | #BDBDBD |

Notes on the table:
- **Text metrics**:
  - `default-text` #090909 / #D2D2D2
  - `label-text` #090909 / #C4C4C4
  - `label-text-focus` #003C88 / #81B4FF (focused labels turn blue)
  - `highlight-text-inactive` #FFFFFF
  - `link-text` #4C7EFF in both themes
  - `visited_link-text` #AA00AA / #FF00FF
  - `warning-text` #333308 / #F4BC02
  - `error-text` #5A0000 / #D32222
- **Selection**: `highlight-background` #3A72B0 / #2C5D87; inactive selection #AEAEAE / #4D4D4D; row hover is rgba(0,0,0,.06) / rgba(255,255,255,.06). Note: Unity wrote `256,256,256`.
- **Primary blue states**: button pressed #96C3FB / #46607C, focus accent border #018CFF / #7BAEFA, input focus border #1D5087 / #3A79BB, slider thumb halo rgba(12,108,203,.5) / rgba(16,111,205,.5).
- **Override bar** (Inheritance pattern): Prefab override `.unity-binding__prefab-override-bar` rgb(50,163,225) light / rgb(5,147,224) dark; the not-applicable state is the same at 35% alpha. Other override bars (e.g. Materials) use #090909 / #C4C4C4.
- **Overlay container** (Overlays pattern): #B6B6B6 at 90% (light), #000000 at 80% (dark). Drop zones are #00AAEF at 25%, or 50% on hover.

**Contrast audit.** I computed WCAG 2.x ratios (§4.6 discusses them):
- Dark label #C4C4C4 on window #383838 = 6.72:1; default text #D2D2D2 on #383838 = 7.76:1; input text on field #2A2A2A = 9.49:1. All pass.
- **Dark error text #D32222 on #383838 = 2.25:1 (fails)**. Dark link #4C7EFF on #383838 = 3.20:1 (fails AA for body text). Focus border #3A79BB on field #2A2A2A = 3.17:1, which passes the 3:1 non-text rule.
- Dark button border #303030 on window #383838 = 1.13:1. This confirms the button is distinguished by fill (#585858), not by its border.

### 1.3 Typography
Source: https://www.foundations.unity.com/fundamentals/typography

**Font stack**
- **Inter** on every OS: "a font family designed to accommodate dense interfaces".
- Fallbacks: Windows/Linux use Verdana; macOS uses Lucida Grande.
- Secondary fonts use a type scale 1 px smaller "to account for these fonts appearing larger in the same size".

**Type scale (USS variables).** It is deliberately tiny: "The Unity Editor is a dense desktop software application and limiting the choice of font and styling options helps keep the interface cohesive."

| Variable | Inter | Verdana / Lucida Grande | Usage |
|---|---|---|---|
| `--unity-metrics-default-font_tiny_size` | **9 px** | 8 px | Only when absolutely necessary (the accessibility minimum) |
| `…font_small_size` | **10 px** | 9 px | Sparingly; labels inside grids, Timeline/Profiler tracks, help-box text |
| `…font_semi_small_size` | **11 px** | 10 px | Search fields inside toolbars |
| `…font_normal_size` | **12 px** | 11 px | **Default for most text** (US-0217) |
| `…font_big_size` | **14 px** | 12 px | Sparingly; list labels (Profiler) |
| `…font_very_big_size` | **19 px** | 16 px | Sparingly; window titles (Project Settings) |

**Line height = control height** (these are the dense-UI row metrics):

| Variable | Value | Use |
|---|---|---|
| `--unity-metrics-single_line_small-height` | **16 px** | mini toggle, mini text field |
| `--unity-metrics-single_line-height` | **18 px** | standard one-line control |
| `--unity-metrics-single_line_large-height` | **20 px** | large control, e.g. Inspector title bar label |

**Style rules**
- Left-aligned everywhere except button labels and empty-state content, which are centred.
- In compound fields, sub-labels (X/Y/Z) sit directly left of their boxes and the category label stays left-aligned.
- **Indentation conveys nesting**: hierarchy, Inspector and first-tier menus. Submenus have the same indentation as the initial menu.
- Bold is reserved for component headers, nesting headers and main folder labels. **Do not bold to group fields** (Content Organization).
- Italics: avoid, or limit to one or two words (Accessibility).
- All caps: avoid except acronyms (CPU, GPU, HDRP).
- Truncation (Label page):
  - End-truncate sentence-like labels.
  - **Middle-truncate object, stylesheet and path names** where the end matters.
  - Always expose the full string via tooltip (`TextElement.displayTooltipWhenElided`).

### 1.4 Iconography
Source: https://www.foundations.unity.com/fundamentals/iconography

**Sizes and artboard**
- Standard sizes: **16, 32, 64, 128, 256 px** (examples go to 512).
- **Artboard 16×16 with a 1 px margin, so the effective live area is 14×14.** "Do not use borders to create negative space."

**Three icon types**
1. **Single-size** (most tool and function icons): one size plus a @2x retina file.
2. **MIP-level** (anything shown in the Project window): all five sizes, suffixed `@16 … @256`. Never `@2x`.
3. **Gizmo** (scene) icons: `Name Gizmo_MIP[0-4].png`. They are exported with a 1%-opacity black layer to avoid white fringes.

**Naming:** Capitalised words. The `d_` prefix marks the dark-theme variant; an icon without `d_` is used for both themes. The `" On"` suffix marks the selected state (e.g. `d_WhiteBox On@32.png`).

**Format:** Transparent PNG only. SVG is not supported because of IMGUI; an "ongoing initiative" will change this.

**Icon-only colour palette** (not for brand use). Light / dark values:

*Primary*
- Gray #555555 / #C4C4C4 (the default for all non-coded icons)

*Secondary*, by product area:
- Blue #0C6CCB / #80D8FF: Graphics
- Charcoal/White #F0F0F0 / #2F2F2F: Unity logo
- Coral #B73C15 / #FF6E40: Navigation
- Cyan #0F7686 / #80FFE6: Animation
- Green 1 #2E7D32 / #B2FF59: Physics
- Magenta #CD237F / #E78DDC: Network/Constraints
- Purple #673AB7 / #AF91F4: 2D
- Yellow #C99700 / #FFC107: Lights

*Feedback*
- 50% Gray: rgba(85,85,85,.5) / rgba(196,196,196,.5)
- Cobalt #0F49BD / #57AEFF: active / on
- Gray #C4C4C4 / #555555: neutral
- Green 2 #008126 / #14D368: success
- Scarlet #B10C0C / #FF534A: error
- White #F0F0F0: selected-state icons
- Yellow #C99700 / #FFC107: warning

*Accent*, for tool-mode semantics:
- Antique Red #B25553 / #FD8678: **remove**
- Iris #6D66CC / #A1A3FF: **modify**
- Orange #B76106 / #FFBA6B: **select**
- Sea Green #00876A / #69E39F: **add**
- Steel Blue #4B88AC: generic, on white shapes

*Verb-coded accent colours (add, modify, select, remove) are a useful idea for dense toolbars.*

**Usage rules**
- Every icon gets a label or name, and icons without labels must have tooltips that include the name ("Print tool: Print this page").
- Most buttons should be **text-only**: "Reserve the use of icons within button labels for when your function requires it" (Label page).
- Tab icons sit left of the label with a 4 px margin (Windowing).

### 1.5 Interactions and states
Source: https://www.foundations.unity.com/fundamentals/interactions

**State hierarchy:** "Pressed states should be dominant in interaction state hierarchy as they denote continuous active states."

- **Hover**: lighter fill on action controls, lighter border on input controls. It can combine with focus, checked, pressed or selected.
- **Focus**: "In most cases focused elements are highlighted in blue. **The use of blue in the Unity Editor is reserved for controls that can be focused, pressed or selected.**" Focused controls receive keyboard input.
- **Disabled**: "In most cases, disabled elements have a **40% alpha** value, including their contents such as labels and icons." IMGUI defaults to 40% opacity. Use help boxes or tooltips to explain why a control is disabled.
- **Checked**: only for on/off inputs. Use *pressed* to show that a control is active.
- **Pressed**: blue highlight fill, optionally with a border. "Only elements that perform binary actions require a pressed state, such as toggle buttons."
- **Highlighted (selected)**: list, tree and text selection. More than one item can be highlighted at a time, and highlighted items are often draggable.
- **Visual cues**:
  - Drag-and-drop targets show **blue lines** in list views and **blue background highlights** in folder views.
  - Highlight applicable drop zones.
  - Tree-view drop lines start with a **blue circle** indicating the target depth.
- **Rounded corners hint at interactivity.** "Rounded corners should be used sparingly, and be reserved for interactive elements, **instead of paneling or containers**." (Flagged as a conflict with glass surfaces in §5.)
- **Containers hint at interactivity**: "Do not place static elements, such as status tags or read-only elements, in containers."
- **Underline**: links are underlined on hover only, never at idle.
- **Hide versus disable** (one of the clearest rules on the site):
  - **Disable** when the value is relevant but not editable (e.g. auto-determined), or when the control is normally available but temporarily isn't. Add a tooltip explaining why.
  - **Hide** when the control is active only in rare circumstances, or when an input's value is currently irrelevant.
  - **Buttons should never be hidden** ("expectation of persistence").
  - Controls hidden by another control's value go **below the trigger, ideally on the next line**.
- **Invalid entry:** numeric and text inputs **disallow invalid values and revert to the last valid value**, which is shown again when the field is unfocused.
- **Interaction methods:**
  - Mouse, keyboard and screen readers.
  - **Right-click is reserved for context menus.** Runtime Scene and Game views do not support right-click.
  - Drag and drop for add (copy cursor), duplicate (Alt+drag), move or reorder tree items (vertical = reorder, horizontal = re-parent), and assign objects to object fields.
  - Overlay docking with target and ghost drop zones.
  - All default windows are resizable, with resize cursors.
  - **Use system cursors**; no custom cursors unless required.
- **Interactive labels:** slider and numeric values **scrub by dragging the label** left or right, and the cursor changes to a scrub glyph. A standalone toggle flips when its label is clicked.

### 1.6 Accessibility
Source: https://www.foundations.unity.com/fundamentals/accessibility

**Colour**
- Semantic colours: Red = error / failure / wrong; Green = confirm / success / correct / safe; Yellow = alert / caution / warning.
- Colour is never the sole differentiator: 1 in 12 men and 1 in 20 women are colour-blind. The Profiler's Colorblind Mode is cited.

**Contrast**
- WCAG 2.1: **4.5:1 for normal text** (1.4.3) and **3:1 for non-text and form controls** (1.4.11).
- Test with hex values; do not colour-pick rendered text.
- Exempt: inactive UI, decorative text, invisible text, text inside pictures.
- Foundations claims the USS colour variables "automatically meet these criteria". The audit in §1.2 shows they do not always.
- Text over translucent backgrounds must meet contrast against every possible backdrop. Avoid "overly transparent" backgrounds. *This is directly relevant to glass.*
- Disabled text: grayed-out text should still meet contrast, and grayed-out areas must not be interactive.

**Size**
- Font sizes: minimum 9 px "only when absolutely necessary"; base 12 px.
- **Click target:** WCAG 2.5.5 recommends **44 × 44 px** (≈9 mm at 120 dpi). When the target can't be that large, make the hit area as large as possible using the space behind the element. Example: a 16 px toolbar icon gets a click target filling the whole toolbar button; a picker box is clickable over its full area even when empty. Failing that, provide an equivalent larger control nearby.

**Focus styling**
- Focus is distinct from hover, with ≥3:1 contrast (WCAG 2.4.11).
- **1 px blue outline** around the focused field or control.
- Selected list items show a **blue highlight with white text**.
- **The label of a focused field also turns blue.**
- When there is no clear input boundary, draw a 1 px blue box around the larger area.

**Keyboarding.** Every area must be reachable with no keyboard traps and a logical order, plus a full hotkey list for experts.

| Key | Behaviour |
|---|---|
| Tab | Moves top-left to bottom-right |
| Shift+Tab | Reverses the Tab order |
| Ctrl+Tab | Moves to the first open tab in each window group |
| Space | Expands dropdowns, activates buttons, toggles checkboxes, performs "click and hold"; scrolls a page down |
| Shift+Space | Scrolls a list up one screen |
| Arrows | Cycle through dropdown items; scroll pages |
| Esc | Reverts an input (numeric or search) or dismisses a dialog or menu |
| Enter / Return | Activates a link or button, or selects an autocomplete option |

**Writing and alt text**
- Alt text describes; it is not a call to action.
- No images containing text; no "Picture of…".
- Toggle copy should say "enabled".
- Descriptive link text: no "Click here", no raw URLs; same text for the same destination.

**Tooltips (accessibility view):** appear next to the element after a prolonged hover or focus, have a "**default duration for 1.5 seconds**", stay on while hovered, disappear quickly on exit, are concise, have good contrast and no transparent background. (This 1.5 s conflicts with the 0.4 s delay on the Tooltip page; see §5.)

**Loaders:** use a determinate indicator when progress data exists, and a **standard circle loader** for infinite loads. Never make an indeterminate wait look like a progress bar.

**i18n:** plan for text expansion. Shipped Editor languages: English, Simplified Chinese, Korean.

### 1.7 UI Writing Guide
Source: https://www.foundations.unity.com/fundamentals/ui-copy-style. This is the newest content (January 2024 changelog).

- **Six qualities:** clear, concise, consistent, action-oriented, user-centric (rewrite "Unity" and "we" into "you"), inclusive. Each has a QA question, e.g. "Are buttons limited to 3 words or less?"
- **Control labels:**
  - 1–2 words, maximum 3.
  - Lead with strong verbs plus an object: "Download package", not "Download the package" or "Download".
  - **Mirror the dialog title in the confirm button**: title "Download package?" → button "Download Package".
- **Capitalisation:**
  - **Title case** for labels, titles, buttons and menu items ("Create Material", "Open a Project").
  - **Sentence case** for complete sentences: tooltips, dialog text, help boxes.
  - Avoid camelCase except for code identifiers; avoid ALL CAPS except acronyms.
  - Note: the older Button page says "Use sentence case" for button labels. That is an internal conflict (§5).
- **Ellipsis convention:** add "…" when an action needs further input or opens a window ("Export Coordinates…"). Do not add it to a menu item that opens Preferences (Project Settings pattern).
- **Empty-state copy:**
  - State the purpose first ("To edit this spline, use…").
  - One-line description, optionally one CTA.
  - Be encouraging, never guilt-inducing.
- **Label punctuation:** none (US-0213).
- **Tooltips:** complete sentences. End with a period only if the tooltip is a full sentence; if there are two sentences, both get periods.

### 1.8 Messaging (Errors & Messaging, Help Box, Empty States)
Sources: https://www.foundations.unity.com/patterns/errors-and-messaging, /components/help-box, /patterns/empty-states

**Four message expression types, chosen by scope:**

| Type | Scope | Behaviour |
|---|---|---|
| **Dialog** (modal, OS-native by default) | Whole Editor | Blocks the app; 1–3 buttons (ok / alt / cancel); verb labels; use sparingly; opt-out via "Don't ask again for this session" or "…for this computer" |
| **Window banner** (`ShowNotification`) | Whole active window | Lower half of the window; size responsive to the window; **fades after 4 s by default** (`fadeoutWait`), scaled to message length; not for edge cases |
| **Help box** | A section or property | Appears **below the affected control and pushes content down**; persistent until resolved; **≤200 characters**; may contain **one button and one link** (UITK) |
| **Console log** | Editor operations | Time-stamped; status line shows the latest message; clicking it opens the Console; `context` arg highlights the object |

**Severity semantics**
- **Error**: will not complete; cannot recover. Red, octagon icon.
- **Warning**: completes but may surprise. Yellow, triangle icon.
- **Info / log**: non-critical. White speech-bubble icon.

**Copy formula: Problem → Cause → Solution**
- Be human-readable, concise and polite; never "illegal command".
- Include searchable exact phrasing.
- Never prefix with "Error:" or "Warning:", because colour and icon already say it.
- Example: "Unity cannot run the application, because it cannot load the textures. Refresh the textures and re-launch the application."

**Dialog button rules**
- In **Editor-native dialogs, destructive actions align left and secondary/primary align right.**
- OS-native dialogs follow OS order: macOS 12 = ok / alt / cancel; macOS 11 = alt / cancel / ok; Windows = ok / alt / cancel.
- OK is the default (Enter). Cancel, the X button and Esc only close the dialog.
- With opt-out, "Cancel" is never remembered.

**Help-box CTAs:** a **button** when the user can fix the issue in place; a **hyperlink** for external documentation. Use `<link>` rather than `<a>` when analytics are needed.

**Empty states** have three kinds:
- **Blank**: nothing to show, e.g. no results or offline. May offer a single action such as "Retry Connection".
- **Idle**: nothing selected. Copy pattern "Select ___ to ___". No actions.
- **Day-0**: onboarding with starter content.

Formatting:
- Centre-aligned in the viewport.
- 12 px default text, sentence case.
- Set a max-width.
- Actions use the `.minibutton` style.
- **Never use error or warning icons in empty states**, and never merge an empty state with a help box. The empty state explains the condition; a help box explains failed recovery.

### 1.9 Layout, spacing and density (consolidated)
There is no single layout page; the numbers below are compiled from several pages.

| Spec | Value | Source |
|---|---|---|
| Inspector inner padding | **18 px left, 4 px right, 8 px top/bottom** (`.unity-inspector-element--uie`) | /patterns/content-organization |
| Between single property fields | **2 px** (`.unity-base-field` = 1 px top + 1 px bottom margin) | same |
| Between grouped fields | **8 px** (last field bottom margin 7 px, or a 7 px spacer) | same |
| Nesting indent (foldout, tree, settings nav) | **15 px per level**, capped at 6 levels; arrow drawn offset into the gutter | /components/foldout, /tree-view, /patterns/project-settings-preferences |
| Settings nav sub-page indent | 15 px + 12 px for the arrow; 4 px padding all round | /patterns/project-settings-preferences |
| Settings content | title `font_very_big` (19 px), 8 px title padding top/bottom; content 8 px top/bottom, 4 px left/right; **label/field columns 50/50**; group bottom padding 4 px | same |
| Inline help icon | 4 px after the label or control | same |
| Button heights | **Mini 18 px (padding 2), Default 20 px (padding 3), Large 24 px (padding 5)**; width hugs content or fills | /components/button |
| Control line heights | 16 / 18 / 20 px | /fundamentals/typography |
| List/tree rows | Docs show **16 px** row heights; UITK ListView `fixedItemHeight` default **22 px**; IMGUI ReorderableList `elementHeight` **21 px**; multi-column UXML samples use 20 px | /components/list-view, /tree-view, /reorderable-list, /multi-column-views |
| List item spacing | Item padding 2 px top and bottom (4 px between items), 5 px right; list container 3 px top/bottom; adjacent controls inside an item have 3 px left/right margins (6 px gap) | /components/reorderable-list |
| Text field | Max recommended width **300 px**; consider a scrollbar after **9 lines** | /components/text-field |
| Search field | Minimum width **150 px (~20 characters)** | /components/search-field |
| Tooltip | Max width **300 px**, 1 px border, ≤3 lines and ≤200 characters, **10 px below the element, horizontally centred**, appears after **0.4 s** | /components/tooltip |
| Dropdown menu | Opens below the button with **1 px overlap**; in tight vertical layouts it opens over the button with the checked item aligned to it | /components/dropdown |
| Inspector minimum width | **275 px** with no horizontal scroll; Tab view ≤4 tabs at that width | UX Essentials, /components/tab |
| Icon artboard | 16 px (14 px live) | /fundamentals/iconography |

**Density philosophy, in Unity's own words**
- "Since the Unity Editor has a **high density interface** with many elements shown in the viewport at a time, it is important to group elements logically without creating visual clutter."
- Grouping tools, in order of preference:
  1. **Vertical spacing** ("the best way")
  2. Headers (for 2–5 always-visible fields)
  3. Foldouts (for larger, collapsible groups)
  4. Tabs
  5. Background tint (reserved for hierarchy or interactivity)
  6. Containers (only when the group shares an interaction, such as reordering or add/remove, or is transient or different, such as messages or progress)
- "Do **not** add high traffic controls under foldouts." Do not put foldouts or headers inside containers.
- Responsive windows: "avoid any design that necessitates both vertical and horizontal scrollbars". Use responsive layout, tabs, split views or foldouts, but never remove scrollbars entirely.

---

## 2. Editor Foundations: components and patterns

Format for each item: purpose, then anatomy, then sizes, states and behaviour, then do/don't. All URLs are under https://www.foundations.unity.com/components/ or /patterns/.

### 2.1 Components

**Button** (`/button`)
- Variants:
  - Basic button (action complete when done).
  - **Independent toggle buttons**: grouped thematically, multi-select (e.g. TextMeshPro style toggles).
  - **Dependent toggle buttons**: mutually exclusive, like a segmented control (e.g. Scene toolbar).
  - Toolbar button (`.toolbarbutton`).
- Anatomy: label, icon, container.
- Sizes: see §1.9. IMGUI group pieces use `.ButtonLeft`, `.ButtonMid` and `.ButtonRight` to fix radii and borders.
- Seven states: default, hover, active (pressed or open), active-focused, focused, hover-focused, disabled. Repeatable actions return to default but "still play an animation to convey it has been used".
- Labels: single line, centred, active verb; navigation buttons name the endpoint; confirmation buttons restate the action; append an ellipsis when more input follows.
- Choosing: basic button for discrete one-shot actions; toggle button for enabling a property or tool, or switching two states.

**Toggle** (`/toggle`) is Unity's checkbox ("checkbox" is discouraged as a name).
- Variants: default (box) and toolbar toggle.
- States: **checked (checkmark), indeterminate/mixed (dash), unchecked (empty)**. Interaction states: default, disabled, hover, focused, pressed.
- **Parent and child logic:**
  - Checking the parent checks all children.
  - Unchecking it unchecks all children.
  - Mixed children make the parent indeterminate.
- Rules:
  - Don't use "enable", "use" or "is" in labels.
  - Never create a toggle that *disables* something when enabled.
  - Only on/off, never this-or-that: "Is orthographic" should be a dropdown (Perspective / Orthographic).
  - No toggles for slow or waiting actions or destructive actions.
  - Toggles can't be resized.
  - The label sits left of the box. Exception: Inspector component toggles sit right of the component name.
- Toggle versus toggle button:
  - **Toggle** when the property needs a long explanation or reveals child properties.
  - **Toggle button** for well-known on/off tools, grouped related properties, or anything in a toolbar.

**Radio button** (`/radio-button`)
- For **≤5 options**; use a dropdown above 5.
- No indeterminate state.
- Label left of the radio; an optional value can sit to the right.
- RadioButtonGroup holds radios only. GroupBox allows custom layouts that mix radios with other controls.

**Dropdown** (`/dropdown`)
- Two body types: **OS menu** (flat string list) or custom **VisualElement menu**.
- APIs: DropdownField (any strings), EnumField (fixed), EnumFlagsField (multi, auto-adds Nothing/Everything), PopupField, Tag/Layer/Mask fields, ToolbarMenu, ToolbarDropDownToggle (split button).
- Rules:
  - Opens on click, **never on hover**.
  - Always attached to its trigger and never covering the trigger's label.
  - A single downward caret on the right.
  - ≤1 submenu level.
  - Separators group items.
  - Single-line items only; otherwise use radios or toggles.
- Overflow: interface dropdowns scroll; menu dropdowns nest the overflow into a submenu.
- States: default, hover (tooltip after a delay), focused (blue border, items highlight on navigation), hover-focused.

**Foldout** (`/foldout`)
- Anatomy: arrow, optional icon, label (bold allowed for header hierarchy), content.
- 15 px indent per level, maximum 6 levels.
- Click behaviour:
  - In **tree views, the arrow expands and the label selects**.
  - In Inspectors, **either the arrow or the label toggles**.
- **Never insert foldouts manually inside list views**; use the ListView's built-in foldout header.
- Choosing: Tree View for multi-tier hierarchy, List View for flat lists, Foldout for a single level of mixed content.
- States: expanded, collapsed, default, hovered (row highlight), focused (blue label), disabled.

**Label** (`/label`)
- Regular weight for control labels, buttons and tree items. Bold for nesting headers, component headers and main folders.
- Focused labels turn blue. Semantic colours: blue for external links only; red and orange for errors and warnings.
- Interactive labels (scrub or toggle).
- Truncation with tooltips (end or middle).
- ≤3 words, no punctuation.
- Tooltips are attached to labels.

**Text field** (`/text-field`)
- UITK TextField covers single and multi-line; IMGUI has TextField plus TextArea.
- Inset border.
- Label left, or above when needed.
- The body spans the window width with a thin margin; internal padding stays constant when resizing.
- Multi-line fields grow vertically, but never so much that they displace other UI.
- Keys: **Return inserts a new line; Shift+Return commits; Esc cancels and reverts.**
- **Delayed fields** commit only on Enter or blur. Use them only when the change is slow or destructive; otherwise update live.
- States: default, hover (border highlight plus I-beam cursor), focused (content selected), disabled.

**Numeric field** (`/numeric-field`)
- Single fields: Int, Float, Double, Long. Multi fields: Vector2/3/4 (and Int variants), Rect, RectInt, Bounds, BoundsInt.
- Always show a default value.
- Pair with a slider for large, imprecise changes. With a basic slider the field sits on the right; with a min-max slider, fields sit on both sides.
- Label scrub.
- Invalid input reverts to the last valid value on unfocus.
- Enter commits; Esc reverts.
- "If the value is bounded on both ends, use a slider."
- Avoid hidden or implicit behaviour when a value is unchanged; put meaningful changes behind an explicit toggle or popup.
- Sub-labels (X Y Z) sit left of each box.

**Slider** (`/slider`)
- Basic (float/int) and min-max.
- Anatomy: label, handle (thumb), groove (track), numeric field.
- Rules:
  - Linear values only; **not for position or rotation**.
  - One variable per slider.
  - Immediate feedback, preferably visualised in the scene.
  - **Consistent groove lengths** within an interface.
- Layout: the label aligns with the left edge, the field with the right edge, and the slider flexes.
- Mouse:
  - Dragging right increases.
  - Clicking the groove jumps to that point.
  - Label scrub.
  - Cursor shows the scrub glyph over the label and an I-beam over the field.
- Keys: arrows adjust; holding an arrow repeats.
- Focus highlights the label, control and field together. Disabled sliders still show their value.

**Object field** (`/object-field`)
- Anatomy: label, object icon, object label, picker button, body.
- Assign by drag-and-drop (**the whole body highlights blue when a compatible object hovers**) or by picker. The picker's header is "Select <Type>".
- Clicking the body pings the asset in the Project window.
- States: default, hover (button and border), focused (blue label and border), **accepted (drag)**, disabled.
- Avoid implicit behaviour when the field is unset.

**Color field** (`/color-field`)
- Anatomy: colour swatch, alpha swatch, eyedropper button, picker modal (standard or HDR).
- Properties: `hdr`, `showAlpha`, `showEyeDropper`.
- Swatch libraries are shareable across projects.
- States: default, hover, eyedropper-focus (blue), modal-focus.

**Search field** (`/search-field`)
- Variants:
  - Toolbar regular.
  - Toolbar **popup** (filter dropdown).
  - **Condensed**: an icon button that expands to a field and auto-focuses. It collapses on outside click only when empty, and pushes surrounding UI if space allows, otherwise overlays it.
- Results update live while typing.
- Minimum width 150 px.
- Placeholder disappears on focus in the regular field but stays until typing in the condensed field.
- Anatomy: search/popup icon, clear icon, body, input, filter label, popup menu, condensed button, collapse button.

**Help box** (`/help-box`): see §1.8. Anatomy: message icon, text, action button, hyperlink.

**Tooltip** (`/tooltip`)
- Text only in the Editor; drawn by the OS.
- **0.4 s delay.** Stays while hovered. **Hides immediately when dragging starts or the pointer moves to UI without a tooltip. Moving directly to another element that has a tooltip shows it instantly, with no delay.**
- Content: full label first, then a line break and the description.
- Don't hard-code shortcuts; read them from the Shortcut Manager.
- Use tooltips for new users, truncated text, unlabelled icons, explaining disabled UI, and surfacing shortcuts.
- Tooltip versus info help box: tooltips for non-vital information; help boxes when the user must discover it.
- Not shown in Play mode.

**Progress bar** (`/progress-bar`)
- Linear and determinate only.
- Placement: **after the control that initiates it**, in the same view; inside a container if it is scoped to that container.
- Show one overall bar for a sequence of tasks.
- Persistent (repeatable operations, user can clear) or temporary.
- Long blocking work uses `EditorUtility.DisplayProgressBar` (or the cancelable variant); background work uses the `Progress` API and the **Background Tasks window**.

**List view** (`/list-view`)
- UITK only, **virtualised** (elements are recycled).
- Requires a fixed `itemHeight`.
- Options: alternating rows, border, horizontal scrolling (off by default), selection None / Single / Multiple, reorderable.
- Anatomy: foldout header, list, row, scrollbar.
- States: default, hover, selected, focused (blue), disabled.

**Reorderable list** (`/reorderable-list`)
- Detailed configuration tables for UITK ListView versus IMGUI ReorderableList. UITK defaults:
  - fixedItemHeight **22 px**
  - showBorder off
  - alternating rows off
  - add/remove footer off
  - showBoundCollectionSize on
  - foldout header off
  - reorderable off
  - reorderMode **Simple** (blue drop line) or **Animated** (drag handles)
  - selection Single
- IMGUI defaults: element height 21 px; header, add, remove and draggable all on.
- Rules:
  - Enable reordering **only when order has functional meaning** (keyframes, render order, priority, execution order).
  - Enable the size field for bulk adds.
  - **With an add/remove footer, show the border** so they connect visually.
  - Performance: lightweight templates; reset all state in `bindItem` (items are pooled); test with realistic counts.

**Multi-column views** (`/multi-column-views`)
- MultiColumnListView and MultiColumnTreeView.
- Column properties: `minWidth`, `maxWidth`, **`optional`** (user can show or hide), **`reorderable`**, **`resizable`**, **`resizePreview`** (live versus on release), **`sortable`**, **`stretchable`**.
- Use them instead of tabs when users must compare data.

**Tree view** (`/tree-view`)
- Virtualised.
- Fixed row height (docs show 16 px).
- Alternating rows; bold parent labels for top folders.
- 15 px indent, maximum 6 levels.
- Arrow expands, label selects.
- **Double-click renames.**
- Drag to reorder or nest.
- States: expanded, collapsed, default, hovered, selected, focused, disabled.

**Scroll view** (`/scroll-view`)
- Content container versus content viewport.
- Vertical and horizontal scrollers; page-size controls scroll speed; elasticity.
- Anatomy: scrollbar button, groove, thumb, container, viewport.

**Toolbar** (`/toolbar`)
- A window toolbar sits under the tab and holds actions related to the window, not to the user's active task.
- **High-traffic actions on the left, low-traffic on the right.**
- Group by interaction type (tools versus toggles), with space between groups.
- Use a second toolbar when needed, but never pad with unnecessary actions.
- Remove edge borders on first and last controls (`.ToolbarDropdownLeft`, `.ToolbarDropdownRight`) to avoid double borders.
- Horizontal or vertical, aligned on one axis.

**Tab** (`/tab`, UITK TabView, 2023.2+)
- For segmenting panels in the same context.
- **Don't use tabs when users need to compare panels; use multi-column views instead.**
- Labels: 1–2 words, no all caps.
- **Avoid disabled tabs**: remove the tab instead.
- Inside the Inspector: ≤4 tabs at 275 pt.
- Closeable and reorderable; a unique `view-data-key` persists order and state.
- Replace legacy toggle-button "tabs".

### 2.2 Patterns

**Windowing** (`/patterns/windowing`). Seven window types and their exact behaviours:

| Type | Dock | Drag | Min/Max | Resize | Closes on outside click | Notes |
|---|---|---|---|---|---|---|
| Default (`Show`) | yes (tab dock) | title bar | yes | yes | no | tab plus window menu; persists layout across restarts |
| Dropdown (`ShowAsDropDown`) | no | no | no | no | **yes** | positioned by the trigger; auto-fits below, then above |
| Popup (`ShowPopup`) | no | no | no | no | no | frameless |
| Auxiliary (`ShowAuxWindow`) | no | title bar | no | no | yes | **single instance, reused** (e.g. colour picker) |
| Modal (`ShowModal`) | no | title bar | no | no | no | always on top, **blocks background** (and recompilation) |
| Utility (`ShowUtility`) | no | title bar | no | no | no | always on top, **allows background interaction** |
| Dialog (`DisplayDialog`) | n/a | n/a | n/a | n/a | n/a | OS-native, blocking |

Other windowing rules:
- Window anatomy:
  - Tab (`.dragtab`; the first tab `.dragtab-first` has only a right border).
  - Docking area (persistent even with one tab).
  - **Dock anchor / window menu** (kebab "⋮").
  - Toolbars, panels, OS frame.
- Window states: idle, active, always-on-top.
- Split-view panels show a double-arrow resize cursor.
- `minSize` and `maxSize` apply when floating; max is ignored when docked.

**Overlays** (`/patterns/overlays`). Persistent, customisable floating panels and toolbars over the Scene view.
- Anatomy:
  - Container and toolbar container.
  - **Dragger.**
  - Label and optional icon.
  - Content: use `EditorToolbarButton`, `…Dropdown`, `…DropdownToggle` and `…Toggle`.
  - Menu (right-click header or tab-well menu).
  - Drop zones.
- Docking: floating, **edge** (becomes a toolbar), **corner**.
- Layout modes:
  - **Collapsed**: icon, or the first two letters of the name.
  - **Panel.**
  - **Vertical.**
  - **Horizontal.**
  - Horizontal toolbar when edge-docked.
  - An overlay without horizontal or vertical layouts collapses when edge-docked.
- **Transient overlays** appear only for a relevant selection (e.g. Particle System, Camera).
- Presets save and restore layouts.

**Contextual Tooling** (`/patterns/contextual-tooling`). A framework that "automatically presents matching tools and features for the work at hand."
- Taxonomy:
  - **Edit Mode**: select and manipulate non-GameObject sub-objects. Entered via an edit toggle at the top of the Tools overlay plus a shortcut. Has a customisable Edit Mode colour.
  - **Component Tool**: shown only while a matching component is selected; auto-removed and falls back to the last transform tool when selection changes.
  - **Creation Tool**: always available, in a separate section at the bottom of the Tools overlay.
  - **Tool Setting**: per active tool.
  - **View Option**: always applicable, persists.
  - **Action**: one-click, in the right-click Actions menu; filtered to the selection or edit mode.
  - **Contextual Overlay** versus **Global Overlay**: global ones need sign-off because "too many will have a negative impact".
- UX essentials:
  - **"Non-usable tools are never shown."**
  - Aim for contextual, non-global solutions.
  - Don't 1:1 port old features.
  - **Never test a feature in isolation**; test alongside unrelated features.

**Authoring Flows** (`/patterns/authoring-flows`)
- **Core windows** (Hierarchy, Scene, Inspector) serve GameObject authoring; **dedicated windows** (Timeline, Animator, UI Builder) serve complex assets.
- **Focused Inspector**: pinned to one object, ignores selection, no lock or debug.
- Decision questions:
  - How dense or complex is the content? Multiple tabs or levels → dedicated window.
  - Vertical layout → Inspector.
  - Wide content (long sliders, timelines, audio) → dedicated window.
  - Must the Scene stay visible? → Inspector or in-scene.
  - Will selection be lost? → focused Inspector.
- **Simple selection** (broad authoring, hop between objects) versus **dedicated selection** (multi-step narrowing: isolation, mode toggles, double-click).
- "Context switching should not affect the layout greatly", so use dynamic UI in the same place.
- **Selection is hinted at both source and target**: a Hierarchy row plus an orange outline in the Scene.
- Isolation indicators: darkened or lightened background, de-emphasised others, **breadcrumbs or a back button** for the isolation level.
- Overrides are shown in **bold property names**.

**Content Organization** (`/patterns/content-organization`): see §1.9.
- Headers versus foldouts: headers for 2–5 always-visible fields; foldouts for larger collapsible groups.
- Avoid bold for grouping.
- Lighter backgrounds mark higher hierarchy (headers). Foldouts are not tinted at idle, only on hover.

**Inheritance** (`/patterns/inheritance`)
- Vocabulary: parent/original object → child/instance, override, variant, detach, override locking.
- **Override bar**: a blue vertical bar on the left of a property, **as tall as the property**; spans a whole component when the component is overridden. Interactable area includes the label.
- **Never use the override bar to mean "this line is different".**
- Value level: show the resolved value. Explain the source in a tooltip. Offer compare, revert and "apply to parent" in a context menu.
- Object level: an aggregate overrides view or dropdown.
- **Lock icon** next to a locked property, with the property UI disabled and an explanation.
- Variants get a distinct icon variation and an inheritance tree view.

**Project Settings & Preferences** (`/patterns/project-settings-preferences`)
- Project Settings are shared and bound to the project. Preferences are per user per machine; macOS calls them "Settings".
- Precedence: command line > local ini > build profiles > project settings > preferences.
- Two-panel layout: specs in §1.9.
- Pages alphabetical; page name equals the window-menu name; no "Settings" in sub-page names; no sub-page unless ≥2.
- Tabs for 3–5 categories; no titles above tabbed sections.
- Foldouts for grouping, not containers or borders.
- Buttons hug content (**no window-wide buttons**).
- No icons or branding in nav or content.
- Frequently changed settings also reachable in context: the **tab kebab menu opens the right Preferences page**. The in-content gear or kebab shows in-context options only.
- Don't label items "Open Preferences" or add an ellipsis.
- Help icon in the title bar or inline (4 px).

**Selection History Navigation** (`/patterns/selection-history-navigation`)
- **Global history** (anything changing the main Inspector): **Cmd/Ctrl+[ and ]**, optional main-toolbar buttons (hidden by default), **up to 50 entries**.
- **Local history** for self-contained windows: window toolbar back/forward on the right, optional Alt+←/→; clear it when the data set changes.
- Do: disable buttons at the boundaries; use `tab_prev` and `tab_next` icons; tooltips "Previous Selection" and "Next Selection".
- Don't: record duplicates or non-user selections.
- No animations; the selection highlight is the feedback.

**Empty States** and **Errors & Messaging**: see §1.8.

---

## 3. App UI 3.0 (com.unity.dt.app-ui 3.0.0-pre.1)

### 3.1 What it is and its architecture
Manual: https://docs.unity3d.com/Packages/com.unity.dt.app-ui@3.0/manual/index.html

**What it is**
- A cross-platform UI framework built on UI Toolkit: Android, iOS, Windows, macOS, Linux and web. It also runs inside **EditorWindows**.
- Platform minimums: Unity 6000.3; iOS 10+; Android 8+; macOS 10.14+; Windows 10+.
- It ships:
  - Components (namespace `Unity.AppUI.UI`, BEM USS classes `appui-<block>__<element>--<modifier>`).
  - Themes and tokens.
  - Inter fonts (Regular and SemiBold only).
  - Icons: PNG with six weight variants, tinted via `--unity-image-tint-color`.
  - MVVM: observables, RelayCommand/AsyncRelayCommand, DI with transient/singleton/scoped lifetimes and conditional resolution.
  - Redux (store, slices, thunks, middleware, DevTools).
  - Navigation graph with a visual editor and code generator.
  - Undo stack, localization, native plugins.
  - Storybook (React-Storybook-like component browser with a property-editor "Canvas" story).
  - A new Visual Documentation window.
  - A Claude Code plugin with skills.
- Stylesheets assume a **96 DPI reference** ("our stylesheets are designed to work with a 96 DPI screen… like in web browser"). `Platform.scaleFactor` and `referenceDpi` correct for OS scaling.

**Root `Panel`**
- Mandatory root that provides the global contexts.
- **Four z-ordered layers: `main-container` → `popup-container` → `notification-container` → `tooltip-container`.**
- `Panel` properties: `theme`, `scale`, `lang`, `layoutDirection`, `tooltipDelayMs`, `preferredTooltipPlacement`, `forceUseTooltipSystem`.

**Contexts** propagate down the visual tree, and any element can re-provide them via `ContextProvider` or `BaseVisualElement`:

| Context | Values |
|---|---|
| `ThemeContext` | `dark` (default), `light`, `editor-dark`, `editor-light`, or a custom `appui--<name>` |
| `ScaleContext` | `small`, `medium` (default), `large` |
| `LangContext` | locale |
| `DirContext` | LTR / RTL |
| `TooltipDelayContext` | ms |
| `TooltipPlacementContext` | placement |
| `SizeContext` | default component S/M/L for a subtree |

Notes:
- Others include `AvatarVariantContext`, `ThreadContext`, `EmojisContext` and `DragContext`.
- **Any subtree can be re-themed or re-scaled.** Example: "a dark-themed modal" or "a larger scale section for improved accessibility".
- Per-element overrides: `themeOverride`, `scaleOverride`, `langOverride`, `layoutDirectionOverride`, `preferredTooltipPlacementOverride`, `tooltipDelayMsOverride`.

**Theme files**
- `App UI.tss` contains every theme and scale as classes (`.appui--dark`, `.appui--small`, …) for runtime switching.
- Twelve fixed TSS files cover each theme × scale combination for UI Builder, e.g. `App UI - Editor Dark - Small.tss`.
- **"For editor tools: use the editor themes (e.g., App UI - Editor Dark - Small)"**. Small scale is the dense desktop density.

### 3.2 Token architecture (exact, from `PackageResources/Styles/Themes`)

Import order in each TSS (later wins):

```
unity-theme://default → App UI - Globals.uss (imports Palette) → App UI - Alias.uss → App UI.uss (84 component sheets, whose :root blocks define component tokens) → App UI - <Theme>.uss → App UI - <Scale>.uss
```

**Five layers:**
1. **Palette (primitive):** `--appui-color-<hue>-<100…1500>`. 14 hues × 15 steps; **step 800 is the base**, 100–700 are shades and 900–1500 tints. Also `black`, `white`, and `transparent-black-*` / `transparent-white-*` alphas from 0 to 1000 (0, .1, .25, .3, .4, .55, .6, .7, .8, .9, 1).
2. **Globals (primitive non-colour):**
   - `font-sizes-25…1800`
   - `sizing-0…3200` (the index ≈ px × 12.5 at Large: `sizing-100` = 8 px)
   - `spacing-25…1000`
   - `border-radius-xs…full`
   - `border-width-none…lg`
   - `animation-duration-50…500`, `animation-easing-*`
   - `opacity-*`, `alphas-*`, `font-weights-*`, `line-heights-*`, `letter-spacing-*`
   - `elevations-*-0…24`
   - Plus the `static-*` copies (`static-sizing`, `static-spacing`), which are not scaled.
3. **Theme (semantic):**
   - A **neutral ramp `--appui-primary-15…1300`** mapped per theme onto a palette gray.
   - Five-step semantic ramps: **`accent-`, `destructive-`, `warning-`, `positive-` with steps 25 (Active/Focus), 50 (Hover), 100 (base), 200, 300**.
   - Role groups built from the neutral ramp:
     - **`backgrounds-50` Canvas, `-100` App background, `-200` Subtle, `-300` Borders**
     - **`foregrounds-25` Disabled text, `-50` Placeholder/Secondary, `-100` Primary text/icon, `-200` High-contrast / text-on-hover**
     - **`base-25…500`** for UI elements: 50 = pressed, 100 = element, 200 = hover, 300 = active/selected, 400 = border, 500 = border-hover
4. **Alias (role × state):**
   - Pattern `--appui-alias-<family>-<property>-<state>`.
   - Families: `control`, `actions` (incl. `actions-accent`, `actions-quiet`, `actions-selected`, `actions-destructive`, `actions-warning`), `field`, `text`, `icon`, `menu`, `highlight`, `semantic`.
   - Properties: `background-color`, `border-color`, `foreground-color`.
   - States: `default`, `hover`, `active`, `focus`, `disabled`, `selected`, `invalid`.
   - Also sizing aliases (`control-sizing-{sm,md,lg}-{height,square}`, `control-sizing-icon-{xxs…lg}`, `control-gap-{xs…xl}`, `control-border-radius`/`-width`, `actions-padding-horizontal`, `actions-gap`), the focus outline (`control-outline-color/width/offset/style`) and **cursors** (pointer, text, not-allowed, resize ×6, move, grab/grabbing).
5. **Component tokens** (in component `:root` blocks): e.g. `--appui-checkbox__box-size-md`, `--appui-toggle__box-width-md`, `--appui-avatar-size-md`, `--appui-appbar-height-default`, `--appui-navigation-rail-width`, `--appui-linear-progress-height`, `--appui-slider-control-padding`, `--appui-tabitem-indicator-emphasized-color`, `--appui-dialog__icon-<semantic>-color`, `--appui-field-label-size`, `--appui-inputlabel-label-size: 33%`. Scale files can override them; Small does.

**Palette (primitive) ramps.** Step **800 = base** (bold); 100–700 shades, 900–1500 tints.

| Hue | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900 | 1000 | 1100 | 1200 | 1300 | 1400 | 1500 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| blue | #011220 | #022540 | #033760 | #044980 | #055b9f | #066ebf | #0780df | **#0892ff** | #27a0ff | #46adff | #65bbff | #84c9ff | #a2d6ff | #c1e4ff | #e0f1ff |
| green | #02150c | #042a18 | #063f24 | #095430 | #0b693b | #0d7e47 | #0f9353 | **#11a85f** | #2fb373 | #4dbe87 | #6ac99b | #88d4af | #a6dec3 | #c4e9d7 | #e1f4eb |
| red | #1b0809 | #361011 | #51181a | #6c2023 | #86282b | #a13034 | #bc383c | **#d74045** | #dc585c | #e17074 | #e6888b | #eba0a2 | #f0b7b9 | #f5cfd1 | #fae7e8 |
| red-orange | #1d0e08 | #391b11 | #562919 | #723622 | #8f442a | #ab5132 | #c85f3b | **#e46c43** | #e77e5b | #eb9172 | #eea38a | #f2b6a1 | #f5c8b9 | #f8dad0 | #fcede8 |
| orange | #1a0e00 | #341c00 | #4e2a00 | #693900 | #834700 | #9d5500 | #b76300 | **#d17100** | #d78320 | #dd9540 | #e2a660 | #e8b880 | #eeca9f | #f4dcbf | #f9eddf |
| yellow | #161200 | #2c2500 | #413700 | #574900 | #6d5b00 | #836e00 | #988000 | **#ae9200** | #b8a020 | #c2ad40 | #ccbb60 | #d7c980 | #e1d69f | #ebe4bf | #f5f1df |
| lime | #0d1403 | #1a2806 | #273c09 | #34500c | #40630e | #4d7711 | #5a8b14 | **#679f17** | #7aab34 | #8db751 | #a0c36e | #b3cf8b | #c6dba8 | #d9e7c5 | #ecf3e2 |
| cyan | #00151a | #002a33 | #003f4d | #005466 | #006880 | #007d99 | #0092b3 | **#00a7cc** | #20b2d2 | #40bdd9 | #60c8df | #80d3e6 | #9fdeec | #bfe9f2 | #dff4f9 |
| indigo | #0a0f1e | #151d3c | #1f2c5a | #2a3b78 | #344995 | #3e58b3 | #4966d1 | **#5375ef** | #6986f1 | #7e98f3 | #94a9f5 | #a9baf7 | #bfcbf9 | #d4ddfb | #eaeefd |
| purple | #130a1e | #26153c | #391f5a | #4c2a78 | #5e3495 | #713eb3 | #8449d1 | **#9753ef** | #a469f1 | #b17ef3 | #be94f5 | #cba9f7 | #d8bff9 | #e5d4fb | #f2eafd |
| pink | #1a0613 | #340d26 | #4d1339 | #67194d | #811f60 | #9b2673 | #b42c86 | **#ce3299** | #d44ca6 | #da65b3 | #e07fbf | #e799cc | #edb2d9 | #f3cce6 | #f9e5f2 |
| gray | #101010 | #202020 | #303030 | #404040 | #505050 | #606060 | #707070 | **#808080** | #909090 | #a0a0a0 | #b0b0b0 | #c0c0c0 | #cfcfcf | #dfdfdf | #efefef |
| light-gray | #050505 | #1a1a1a | #333333 | #4d4d4d | #666666 | #808080 | #999999 | **#b2b2b2** | #bfbfbf | #cacaca | #d5d5d5 | #e0e0e0 | #ebebeb | #f5f5f5 | #fafafa |
| dark-gray | #0c0c0c | #151515 | #1e1e1e | #282828 | #323232 | #3c3c3c | #484848 | **#555555** | #6a6a6a | #808080 | #959595 | #aaaaaa | #c0c0c0 | #d5d5d5 | #eaeaea |

**Semantic and alias tokens resolved per theme.** These are the exact computed values at Medium scale; colour does not vary by scale.

| Token | Dark | Light | Editor Dark | Editor Light |
|---|---|---|---|---|
| `alias-control-outline-color` | rgba(11, 126, 224, 0.8) | rgba(11, 126, 224, 0.8) | rgba(11, 126, 224, 0.8) | rgba(11, 126, 224, 0.8) |
| `alias-control-outline-width` | 2 | 2 | 2 | 2 |
| `alias-control-outline-style` | solid | solid | solid | solid |
| `alias-control-outline-offset` | 2 | 2 | 2 | 2 |
| `alias-actions-selected-background-color-default` | rgba(8, 146, 255, 0.5) | rgba(8, 146, 255, 0.5) | #46607c | #96c3fb |
| `alias-actions-selected-background-color-hover` | rgba(8, 146, 255, 0.6) | rgba(8, 146, 255, 0.6) | #4f657f | #6ba2e6 |
| `alias-actions-selected-background-color-active` | rgba(8, 146, 255, 0.4) | rgba(8, 146, 255, 0.4) | #4f657f | #5a90d3 |
| `alias-actions-selected-background-color-focus` | rgba(8, 146, 255, 0.6) | rgba(8, 146, 255, 0.6) | #537395 | #6ba2e6 |
| `alias-actions-border-color-selected` | rgba(8, 146, 255, 0.5) | rgba(8, 146, 255, 0.5) | #303030 | #b0b0b0 |
| `alias-actions-quiet-background-color-default` | rgba(0, 0, 0, 0) | rgba(0, 0, 0, 0) | rgba(0, 0, 0, 0) | rgba(0, 0, 0, 0) |
| `alias-control-border-color-invalid` | #d74045 | #d74045 | #d74045 | #d74045 |
| `alias-control-foreground-color-selected` | #0892ff | #0892ff | #0892ff | #96c3fb |
| `alias-control-foreground-color-invalid` | #d74045 | #d74045 | #d74045 | #d74045 |
| `alias-actions-border-color-invalid` | #d74045 | #d74045 | #d74045 | #d74045 |
| `alias-actions-accent-background-color-default` | #0892ff | #0892ff | #0892ff | #96c3fb |
| `alias-actions-accent-background-color-hover` | #0780df | #0780df | #0780df | #b0d2fc |
| `alias-actions-accent-background-color-active` | #066ebf | #066ebf | #066ebf | #b0d2fc |
| `alias-actions-accent-background-color-focus` | #066ebf | #066ebf | #066ebf | #b0d2fc |
| `alias-field-border-color-focus` | #0892ff | #0892ff | #3a79bb | #1d5087 |
| `alias-field-border-color-invalid` | #d74045 | #d74045 | #d74045 | #d74045 |
| `alias-semantic-positive` | #11a85f | #11a85f | #11a85f | #11a85f |
| `alias-semantic-destructive` | #d74045 | #d74045 | #d74045 | #d74045 |
| `alias-semantic-warning` | #d17100 | #d17100 | #d17100 | #d17100 |
| `alias-semantic-informative` | #0892ff | #0892ff | #0892ff | #96c3fb |
| `alias-control-background-color-default` | #323232 | #e0e0e0 | #424242 | #cbcbcb |
| `alias-control-background-color-hover` | #3c3c3c | #cacaca | #4f4f4f | #cbcbcb |
| `alias-control-background-color-active` | #282828 | #ebebeb | #383838 | #c0c0c0 |
| `alias-control-background-color-focus` | #282828 | #ebebeb | #383838 | #c0c0c0 |
| `alias-control-background-color-disabled` | #282828 | #ebebeb | #383838 | #c0c0c0 |
| `alias-control-border-color-default` | #555555 | #b2b2b2 | #202020 | #b0b0b0 |
| `alias-control-border-color-hover` | #6a6a6a | #999999 | #656565 | #6c6c6c |
| `alias-control-border-color-active` | #555555 | #b2b2b2 | #0d0d0d | #a0a0a0 |
| `alias-control-border-color-focus` | #323232 | #e0e0e0 | #3a79bb | #1d5087 |
| `alias-control-border-color-disabled` | #555555 | #b2b2b2 | rgba(32, 32, 32, 0.5) | rgba(176, 176, 176, 0.5) |
| `alias-control-foreground-color-default` | #c0c0c0 | #333333 | #d2d2d2 | #1d1d1d |
| `alias-control-foreground-color-hover` | #d5d5d5 | #1a1a1a | #eeeeee | #101010 |
| `alias-control-foreground-color-active` | #d5d5d5 | #1a1a1a | #eeeeee | #101010 |
| `alias-control-foreground-color-focus` | #d5d5d5 | #1a1a1a | #eeeeee | #101010 |
| `alias-control-foreground-color-disabled` | #6a6a6a | #808080 | #858585 | #858585 |
| `alias-actions-background-color-default` | #323232 | #e0e0e0 | #585858 | #e4e4e4 |
| `alias-actions-background-color-hover` | #3c3c3c | #cacaca | #676767 | #ececec |
| `alias-actions-background-color-active` | #282828 | #ebebeb | #6e6e6e | #bebebe |
| `alias-actions-background-color-focus` | #282828 | #ebebeb | #6e6e6e | #bebebe |
| `alias-actions-background-color-disabled` | #323232 | #e0e0e0 | #585858 | #e4e4e4 |
| `alias-actions-foreground-color-default` | #c0c0c0 | #333333 | #d2d2d2 | #1d1d1d |
| `alias-actions-foreground-color-hover` | #d5d5d5 | #1a1a1a | #eeeeee | #101010 |
| `alias-actions-foreground-color-active` | #d5d5d5 | #1a1a1a | #eeeeee | #101010 |
| `alias-actions-foreground-color-focus` | #d5d5d5 | #1a1a1a | #eeeeee | #101010 |
| `alias-actions-foreground-color-disabled` | #6a6a6a | #808080 | #858585 | #858585 |
| `alias-actions-foreground-color-selected` | #d5d5d5 | #1a1a1a | #eeeeee | #101010 |
| `alias-actions-border-color-default` | #555555 | #b2b2b2 | #303030 | #b2b2b2 |
| `alias-actions-border-color-hover` | #6a6a6a | #999999 | #303030 | #b2b2b2 |
| `alias-actions-border-color-active` | #555555 | #b2b2b2 | #242424 | #939393 |
| `alias-actions-border-color-focus` | #555555 | #b2b2b2 | #3a79bb | #1d5087 |
| `alias-actions-border-color-disabled` | #484848 | #bfbfbf | #303030 | #b0b0b0 |
| `alias-actions-quiet-background-color-focus` | #282828 | #ebebeb | #383838 | #c0c0c0 |
| `alias-text-callout` | #d5d5d5 | #1a1a1a | #eeeeee | #101010 |
| `alias-text-primary` | #c0c0c0 | #333333 | #d2d2d2 | #1d1d1d |
| `alias-text-secondary` | #aaaaaa | #4d4d4d | #cbcbcb | #363636 |
| `alias-text-disabled` | #6a6a6a | #808080 | #858585 | #858585 |
| `alias-field-background-color-default` | #323232 | #e0e0e0 | #2a2a2a | #f0f0f0 |
| `alias-field-background-color-hover` | #3c3c3c | #cacaca | #2a2a2a | #f0f0f0 |
| `alias-field-background-color-active` | #323232 | #e0e0e0 | #2a2a2a | #f0f0f0 |
| `alias-field-background-color-focus` | #323232 | #e0e0e0 | #2a2a2a | #f0f0f0 |
| `alias-field-background-color-disabled` | #323232 | #e0e0e0 | rgba(42, 42, 42, 0.5) | rgba(240, 240, 240, 0.5) |
| `alias-field-border-color-default` | #555555 | #b2b2b2 | #202020 | #b0b0b0 |
| `alias-field-border-color-hover` | #6a6a6a | #999999 | #656565 | #656565 |
| `alias-field-border-color-active` | #6a6a6a | #999999 | #0d0d0d | #a0a0a0 |
| `alias-field-border-color-disabled` | #555555 | #b2b2b2 | rgba(32, 32, 32, 0.5) | rgba(176, 176, 176, 0.5) |
| `alias-icon-callout` | #d5d5d5 | #1a1a1a | #eeeeee | #101010 |
| `alias-icon-primary` | #c0c0c0 | #333333 | #d2d2d2 | #1d1d1d |
| `alias-icon-secondary` | #aaaaaa | #4d4d4d | #cbcbcb | #363636 |
| `alias-icon-disabled` | #6a6a6a | #808080 | #858585 | #858585 |
| `alias-menu-border-color-default` | #484848 | #bfbfbf | #4f4f4f | #9a9a9a |
| `alias-highlight-background-color-default` | #0892ff | #0892ff | #3a79bb | #1d5087 |
| `alias-actions-quiet-background-color-hover` | #3c3c3c | #cacaca | #676767 | #ececec |
| `alias-actions-quiet-background-color-active` | #282828 | #ebebeb | #6e6e6e | #bebebe |
| `primary-15` | #000000 | #000000 | #000000 | #000000 |
| `primary-25` | #0c0c0c | #050505 | #161616 | #040404 |
| `primary-50` | #151515 | #1a1a1a | #202020 | #101010 |
| `primary-100` | #1e1e1e | #333333 | #2a2a2a | #1d1d1d |
| `primary-200` | #282828 | #4d4d4d | #383838 | #363636 |
| `primary-300` | #323232 | #666666 | #424242 | #595959 |
| `primary-400` | #3c3c3c | #808080 | #4f4f4f | #858585 |
| `primary-500` | #484848 | #999999 | #5d5d5d | #868686 |
| `primary-600` | #555555 | #b2b2b2 | #727272 | #909090 |
| `primary-700` | #6a6a6a | #bfbfbf | #858585 | #9a9a9a |
| `primary-800` | #808080 | #cacaca | #a2a2a2 | #ababab |
| `primary-900` | #aaaaaa | #e0e0e0 | #cbcbcb | #cbcbcb |
| `primary-1000` | #c0c0c0 | #ebebeb | #d2d2d2 | #c0c0c0 |
| `primary-1100` | #d5d5d5 | #f5f5f5 | #eeeeee | #a9a9a9 |
| `primary-1200` | #eaeaea | #fafafa | #e9e9e9 | #d9d9d9 |
| `primary-1300` | #ffffff | #ffffff | #ffffff | #ffffff |
| `accent-25` | #066ebf | #066ebf | #066ebf | #bac9e0 |
| `accent-50` | #0780df | #0780df | #0780df | #a9c4ec |
| `accent-100` | #0892ff | #0892ff | #0892ff | #96c3fb |
| `accent-200` | #27a0ff | #27a0ff | #27a0ff | #80b3ee |
| `accent-300` | #46adff | #46adff | #46adff | #649ce3 |
| `destructive-25` | #a13034 | #a13034 | #a13034 | #a13034 |
| `destructive-50` | #bc383c | #bc383c | #bc383c | #bc383c |
| `destructive-100` | #d74045 | #d74045 | #d74045 | #d74045 |
| `destructive-200` | #dc585c | #dc585c | #dc585c | #dc585c |
| `destructive-300` | #e17074 | #e17074 | #e17074 | #e17074 |
| `warning-25` | #9d5500 | #9d5500 | #9d5500 | #9d5500 |
| `warning-50` | #b76300 | #b76300 | #b76300 | #b76300 |
| `warning-100` | #d17100 | #d17100 | #d17100 | #d17100 |
| `warning-200` | #d78320 | #d78320 | #d78320 | #d78320 |
| `warning-300` | #dd9540 | #dd9540 | #dd9540 | #dd9540 |
| `positive-25` | #0d7e47 | #0d7e47 | #0d7e47 | #0d7e47 |
| `positive-50` | #0f9353 | #0f9353 | #0f9353 | #0f9353 |
| `positive-100` | #11a85f | #11a85f | #11a85f | #11a85f |
| `positive-200` | #2fb373 | #2fb373 | #2fb373 | #2fb373 |
| `positive-300` | #4dbe87 | #4dbe87 | #4dbe87 | #4dbe87 |
| `backgrounds-50` | #151515 | #f5f5f5 | #202020 | #a9a9a9 |
| `backgrounds-100` | #1e1e1e | #ebebeb | #2a2a2a | #c0c0c0 |
| `backgrounds-200` | #282828 | #e0e0e0 | #383838 | #cbcbcb |
| `backgrounds-300` | #323232 | #cacaca | #424242 | #ababab |
| `foregrounds-25` | #6a6a6a | #808080 | #858585 | #858585 |
| `foregrounds-50` | #aaaaaa | #4d4d4d | #cbcbcb | #363636 |
| `foregrounds-100` | #c0c0c0 | #333333 | #d2d2d2 | #1d1d1d |
| `foregrounds-200` | #d5d5d5 | #1a1a1a | #eeeeee | #101010 |
| `base-25` | #1e1e1e | #f5f5f5 | #2a2a2a | #a9a9a9 |
| `base-50` | #282828 | #ebebeb | #383838 | #c0c0c0 |
| `base-100` | #323232 | #e0e0e0 | #424242 | #cbcbcb |
| `base-200` | #3c3c3c | #cacaca | #4f4f4f | #cbcbcb |
| `base-300` | #484848 | #bfbfbf | #5d5d5d | #ababab |
| `base-400` | #555555 | #b2b2b2 | #727272 | #9a9a9a |
| `base-500` | #6a6a6a | #999999 | #858585 | #858585 |

Observations:
- **Dark and Light share the coloured ramps**: accent is blue-800 #0892FF in both. Only the neutral ramp changes: dark-gray versus light-gray hue.
- **Editor Dark and Editor Light override the gray hue values and many aliases with the exact Editor Foundations colours.**
  - Editor Dark: actions bg #585858 / hover #676767 / active #6E6E6E; selected #46607C; field bg #2A2A2A; field border #202020, hover #656565, active #0D0D0D, focus #3A79BB.
  - Editor Light: #E4E4E4 / #ECECEC / #BEBEBE; selected #96C3FB; field #F0F0F0; focus #1D5087.
  - **App UI therefore already implements a "dense pro / host-native" sub-theme of a general product design system.** This is exactly the parent/child relationship we need.
- Editor Light remaps accent to light blues (accent-100 #96C3FB) and sets accent foreground to #101010 (dark text on light blue).
- Editor Light's neutral ramp is **non-monotonic** (primary-1000 #C0C0C0, -1100 #A9A9A9, -1200 #D9D9D9) because it mirrors real Editor surfaces rather than a generated ramp.
- In Dark, `control-border-color-focus` resolves to `base-100` (#323232, invisible). **Focus is carried by an outline ring**, not the border; field focus uses accent #0892FF.
- Selected actions in Dark and Light are **translucent accent** rgba(8,146,255,.5) (hover .6, active .4, disabled rgba(16,133,225,.15)). The Editor themes use opaque Editor blues.

### 3.3 Scale system (density) with exact values

Three scales come from one formula: **Large = 1× of an 8 px-based grid, Medium = 0.75×, Small = 0.5×** for sizing and spacing.

Font sizes do **not** scale proportionally:
- Medium and Large share the global font scale (body-md **14 px**).
- Small is −2 px (body-md **12 px**, which equals the Editor default).
- Radii: Medium and Large are 6 px (control); Small is 3 px.
- Small also lightens weights: `font-weights-300` (bold) = 400, `-400` = 600, `-500` = 700.

| Token | Small | Medium | Large |
|---|---|---|---|
| `alias-actions-border-radius` | 3px | 6px | 6px |
| `alias-actions-gap` | 6px | 9px | 12px |
| `alias-actions-padding-horizontal` | 8px | 12px | 16px |
| `alias-control-border-radius` | 3px | 6px | 6px |
| `alias-control-border-width` | 1px | 1px | 1px |
| `alias-control-gap-lg` | 6px | 9px | 12px |
| `alias-control-gap-md` | 4px | 6px | 8px |
| `alias-control-gap-sm` | 2px | 3px | 4px |
| `alias-control-gap-xl` | 8px | 12px | 16px |
| `alias-control-gap-xs` | 2px | 2px | 2px |
| `alias-control-sizing-icon-lg` | 16px | 24px | 32px |
| `alias-control-sizing-icon-md` | 16px | 24px | 32px |
| `alias-control-sizing-icon-sm` | 12px | 18px | 24px |
| `alias-control-sizing-icon-xs` | 8px | 12px | 16px |
| `alias-control-sizing-icon-xxs` | 6px | 9px | 12px |
| `alias-control-sizing-lg-height` | 24px | 36px | 48px |
| `alias-control-sizing-lg-square` | 24px | 36px | 48px |
| `alias-control-sizing-md-height` | 20px | 30px | 40px |
| `alias-control-sizing-md-square` | 20px | 30px | 40px |
| `alias-control-sizing-sm-height` | 16px | 24px | 32px |
| `alias-control-sizing-sm-square` | 16px | 24px | 32px |
| `appbar-height-compact` | 20px | 30px | 40px |
| `appbar-height-default` | 28px | 42px | 56px |
| `avatar-size-lg` | 40px | 48px | 64px |
| `avatar-size-md` | 32px | 39px | 52px |
| `avatar-size-sm` | 24px | 30px | 40px |
| `border-radius-full` | 100% | 100% | 100% |
| `border-radius-lg` | 4px | 8px | 8px |
| `border-radius-md` | 3px | 6px | 6px |
| `border-radius-sm` | 2px | 4px | 4px |
| `border-radius-xl` | 8px | 16px | 16px |
| `border-radius-xs` | 1px | 2px | 2px |
| `border-width-lg` | 4px | 8px | 8px |
| `border-width-md` | 2px | 4px | 4px |
| `border-width-none` | 0px | 0px | 0px |
| `border-width-sm` | 1px | 2px | 2px |
| `border-width-xs` | 1px | 1px | 1px |
| `checkbox__box-size-lg` | 14px | 18px | 24px |
| `checkbox__box-size-md` | 13px | 15px | 20px |
| `checkbox__box-size-sm` | 10px | 12px | 16px |
| `font-sizes-body-lg` | 14px | 16px | 16px |
| `font-sizes-body-md` | 12px | 14px | 14px |
| `font-sizes-body-sm` | 10px | 12px | 12px |
| `font-sizes-body-xl` | 16px | 18px | 18px |
| `font-sizes-body-xs` | 8px | 10px | 10px |
| `font-sizes-body-xxl` | 18px | 20px | 20px |
| `font-sizes-body-xxs` | 6px | 8px | 8px |
| `font-sizes-body-xxxl` | 20px | 22px | 22px |
| `font-sizes-heading-lg` | 25px | 28px | 28px |
| `font-sizes-heading-md` | 20px | 22px | 22px |
| `font-sizes-heading-sm` | 16px | 18px | 18px |
| `font-sizes-heading-xl` | 32px | 36px | 36px |
| `font-sizes-heading-xs` | 12px | 14px | 14px |
| `font-sizes-heading-xxl` | 40px | 45px | 45px |
| `font-sizes-heading-xxs` | 8px | 10px | 10px |
| `font-sizes-heading-xxxl` | 52px | 58px | 58px |
| `font-weights-150` | 400 | 500 | 500 |
| `font-weights-300` | 400 | 700 | 700 |
| `font-weights-400` | 600 | 800 | 800 |
| `font-weights-500` | 700 | 900 | 900 |
| `linear-progress-height` | 5px | 8px | 10px |
| `navigation-rail-width` | 32px | 48px | 64px |
| `radio__button-size-lg` | 14px | 18px | 24px |
| `radio__button-size-md` | 13px | 15px | 20px |
| `radio__button-size-sm` | 10px | 12px | 16px |
| `sizing-10` | 1px | 1px | 1px |
| `sizing-25` | 1px | 2px | 2px |
| `sizing-50` | 2px | 3px | 4px |
| `sizing-75` | 3px | 5px | 6px |
| `sizing-100` | 4px | 6px | 8px |
| `sizing-125` | 5px | 8px | 10px |
| `sizing-150` | 6px | 9px | 12px |
| `sizing-200` | 8px | 12px | 16px |
| `sizing-250` | 10px | 15px | 20px |
| `sizing-300` | 12px | 18px | 24px |
| `sizing-350` | 14px | 21px | 28px |
| `sizing-400` | 16px | 24px | 32px |
| `sizing-500` | 20px | 30px | 40px |
| `sizing-600` | 24px | 36px | 48px |
| `sizing-700` | 28px | 42px | 56px |
| `sizing-800` | 32px | 48px | 64px |
| `sizing-1000` | 40px | 60px | 80px |
| `sizing-1200` | 48px | 72px | 96px |
| `sizing-1400` | 56px | 112px | 112px |
| `sizing-1600` | 64px | 128px | 128px |
| `sizing-2000` | 80px | 160px | 160px |
| `spacing-25` | 1px | 2px | 2px |
| `spacing-50` | 2px | 3px | 4px |
| `spacing-100` | 4px | 6px | 8px |
| `spacing-125` | 5px | 8px | 10px |
| `spacing-150` | 6px | 9px | 12px |
| `spacing-200` | 8px | 12px | 16px |
| `spacing-250` | 10px | 15px | 20px |
| `spacing-300` | 12px | 18px | 24px |
| `spacing-400` | 16px | 24px | 32px |
| `spacing-450` | 18px | 27px | 32px |
| `spacing-500` | 20px | 30px | 40px |
| `spacing-600` | 24px | 36px | 48px |
| `spacing-700` | 28px | 42px | 56px |
| `spacing-800` | 32px | 48px | 64px |
| `spacing-900` | 56px | 54px | 72px |
| `spacing-1000` | 40px | 60px | 80px |
| `toggle__box-height-lg` | 16px | 23px | 30px |
| `toggle__box-height-md` | 14px | 18px | 24px |
| `toggle__box-height-sm` | 12px | 15px | 20px |
| `toggle__box-width-lg` | 28px | 36px | 48px |
| `toggle__box-width-md` | 24px | 30px | 40px |
| `toggle__box-width-sm` | 20px | 24px | 32px |

**Two-axis sizing: scale context × component size.** Most controls expose `size` = S / M / L (enum `Size`). The control height matrix:

| Component size → / Scale ↓ | S | M (default) | L |
|---|---|---|---|
| **Small** (editor/dense) | 16 | **20** | 24 |
| **Medium** (default app) | 24 | **30** | 36 |
| **Large** (touch/accessibility) | 32 | **40** | 48 |

Notes on the matrix:
- Small-scale S/M/L **= Editor Foundations Mini/Default/Large buttons (18/20/24) and control lines (16/18/20) within 2 px.**
- Large-scale L (48 px) meets Material's 48 dp touch target.
- Medium-scale M is 30 px.
- **Icon sizes** (enum `IconSize` XXS/XS/S/M/L):
  - Small: 8 / 10 / 12 / 14 / 16
  - Medium: 12 / 15 / 18 / 21 / 24
  - Large: 16 / 20 / 24 / 28 / 32
- **Control gaps** xs/sm/md/lg/xl:
  - Small: 2/2/4/6/8
  - Medium: 2/3/6/9/12
  - Large: 2/4/8/12/16

**Quirks and bugs found in the token files.** Avoid copying them.
- Medium defines `sizing-*` only up to 1350 (81 px). Above that it falls back to the Large/global values, so **Medium `sizing-1400` = 112 px** (a discontinuity: 81 → 112).
- Small `spacing-900` = 56 px but `spacing-1000` = 40 px (non-monotonic).
- `spacing-450` = `spacing-400` = 32 px in Large and globals.
- Only Medium defines `spacing-275` (16 px).
- The Medium scale produces non-4-multiples (9, 15, 21, 27 px), which blur on 1× displays.
- Lesson: **generate scales from integer 4-pt steps, not multipliers.**

### 3.4 Motion and elevation (exact)

**Durations**

| Token | Value |
|---|---|
| `animation-duration-50` | 60 ms |
| `-100` | 90 ms |
| `-125` | 125 ms |
| `-150` | 150 ms |
| `-200` | 200 ms |
| `-250` | 250 ms |
| `-300` | 300 ms |
| `-350` | 350 ms |
| `-400` | 400 ms |
| `-450` | 450 ms |
| `-500` | 500 ms |

**Easings**
- `linear`, `ease-in`, `ease-out`, `ease-in-out`, plus `*-back` variants.
- **All component transitions use `ease-out`.**

**Transitions in components**
- Usage counts: 150 ms ×7, 90 ms ×6, 125 ms ×3, 500 ms ×1.
- The 500 ms one is Button background, border and colour. That is slow for dense UIs.
- Modal open: 150 ms.
- Popover enter: from `translate(0,-12px) scale(.96)`.
- Tooltip enter: from `scale(.96)`.
- Toast: fade from `scale(.8)` or slide 100% from its edge.
- Tray examples: fast 150 ms / standard 300 ms / slow 500 ms.
- `NavigationAnimation`: `None`, `FadeIn`/`FadeOut`, `ScaleDownFadeIn`/`ScaleUpFadeOut`.
- **`Platform.reduceMotion`** (with a change event) is exposed so apps can adapt.

**Elevation**

`appui-elevation-0…24`: offset-y = N, spread = N, blur = N, colour rgba(0,0,0,.65), offset-x = 0.

Fixed component shadows:

| Component | Offset-y | Spread | Blur |
|---|---|---|---|
| Popover | 6 | 8 | 8 |
| Tooltip | 8 | 16 | 15 |
| Toast | 10 | 15 | 15 |
| Modal content | 10 | 20 | 15 |
| Drawer | 10 | 20 | 15 |

Backdrops:
- Modal popover backdrop: rgba(0,0,0,.4).
- Drawer: configurable `backdropFinalOpacity`.

**Focus ring**
- `outline 2px solid rgba(11,126,224,.8)` with **2 px offset**.
- Applied **only on keyboard focus** (`.keyboard-focus` added by `KeyboardFocusController`), not on pointer focus.

### 3.5 Component catalog (App UI 3.0 API)

Pages are at `https://docs.unity3d.com/Packages/com.unity.dt.app-ui@3.0/api/Unity.AppUI.UI.<Name>.html`. Dimensions are given as Small / Medium / Large scale at the default component size M, unless noted.

**Actions**
- **Button**
  - Variants: Default, Accent (primary), Destructive; plus `quiet`.
  - Slots: leading/trailing icon, `title` plus optional `subtitle` (two-line button).
  - Size S/M/L → heights in §3.3.
  - Vertical padding is spacing-25/50/100 for S/M/L; label gap is control-gap-md.
  - Guidance: "use buttons for the most important actions; for secondary actions consider links or menu items".
  - Clicks are handled via the `Pressable` manipulator (`clickable.clicked`), so **mouse, keyboard, touch and voice converge on one event**. Don't use ClickEvent.
- **IconButton**: icon only; `primary`, `quiet`; square size = control height; focusable (tabIndex 0).
- **ActionButton**: toolbar-style, **`selected` state** (toggle), `accent`, `quiet`, icon and/or label plus trailing icon. Size S/M/L 16/20/24 · 24/30/36 · 32/40/48; horizontal padding spacing-100; 90 ms transitions.
- **ActionGroup**:
  - Horizontal or vertical; **`compact`** (joined, no gaps); `justified`; `quiet`.
  - Selection None / Single / Multiple, `allowNoSelection`.
  - **Automatic overflow into a "more" menu**.
  - Item gap control-gap-md.
  - This is Unity's dependent/independent toggle-button group made generic.
- **ActionBar**: contextual bulk-action bar for a collection view: select-all checkbox, "N selected" message, ActionGroup.
- **FloatingActionButton**: one per screen; `accent`; `elevation`.
- **Link**: `url` or action; TextSize.

**Inputs**
- **TextField**: placeholder, leading/trailing icon or element, `isPassword`, `maskChar`, `maxLength`, `isReadOnly`, `invalid`, `validateValue`. Heights S/M/L; horizontal padding control-gap-md (4/6/8).
- **TextArea**: multi-line text.
- **SearchBar**: a TextField with a magnifier and "Search…" placeholder.
- **NumericalField<T>** (IntField, LongField, FloatField, DoubleField):
  - `lowValue` / `highValue` (Optional).
  - **`formatString`** (e.g. "F1", "P0") or `formatFunction`.
  - **`unit`** label shown inside the field (trailing) and **draggable to scrub** (`acceptDragging`, DragContext with phase, delta and speed).
  - Arrow keys increment.
  - **Expression evaluation** (manual Inputs page: typing math expressions).
  - `invalid`, `validateValue`.
- **Vector2/3/4Field, Vector2Int/3IntField, RectField, RectIntField, BoundsField, BoundsIntField**: multi-component numeric fields, matching the Editor's multi fields.
- **InputLabel**:
  - Wraps any input with a label.
  - **horizontal (label column `--appui-inputlabel-label-size: 33%`) or vertical** direction.
  - `required` with `indicatorType` Asterisk / Text ("Required", localized) / None.
  - `helpMessage` plus `helpVariant` (Default / Warning / Destructive).
  - `labelOverflow` ellipsis; `inputAlignment`.
  - **`draggable`: drag the label to scrub child numeric inputs** (Unity's label-scrub, generalised).
  - **Hovering the label applies hover styling to the field.**
- **FieldLabel**: standalone label with required indicator.
- **HelpText**: Default, Warning or Destructive message under a field.
- **Checkbox**:
  - `CheckboxState` Checked / **Intermediate** / Unchecked. Intermediate is programmatic only; the user toggles between checked and unchecked.
  - `emphasized` (accent fill); `invalid`.
  - Box sizes: Small 13, Medium 15, Large 20 px (M size); radius 3/4/5.
- **Toggle**: a **switch** (track plus thumb), not a checkbox. Box M: 24×14 / 30×18 / 40×24, thumb 8/12/16. (Naming conflict with Unity Editor "Toggle" = checkbox; see §5.)
- **Radio / RadioGroup**: unique `key` per radio; `emphasized`; group validation. Button M: 13/15/20, dot 5/6/8.
- **Dropdown / Picker**:
  - `selectionType` Single / Multiple; `closeOnSelection`.
  - `defaultMessage` (placeholder), `bindItem`, `bindTitle` (custom title for multi-select).
  - `emphasized`; caret icon; menu `max-height: 180px`.
  - Guidance: **"Use Dropdown when you have 3–10 options. Fewer → radio or toggle buttons; more → a searchable ComboBox."**
- **EnumField**, **MaskField** (flags).
- **Stepper**: −/+ buttons emitting ±1; arrow and ± keys; button squares 16/20/24 at Small.
- **SliderFloat / SliderInt**:
  - Horizontal or vertical; step; **`RestrictedValuesPolicy`** (None / Step / CustomMarks / **CtrlStep** / **CtrlCustomMarks**: snapping only while Ctrl is held).
  - Marks plus mark labels; **`ValueDisplayMode`** Off / Auto (shows while dragging) / On.
  - **`TrackDisplayType`** On / Off / Inverted.
  - Optional inline input field; **Shift for larger steps**.
  - Track 2/3/4 px; control height = control-md.
- **RangeSliderFloat/Int**: two thumbs.
- **TouchSliderFloat/Int**: touch-optimised, value inside the bar.
- **ColorField**:
  - Swatch with optional hex text; `swatchOnly`, `swatchSize`.
  - `showAlpha`, **`hdr`**.
  - **Inline or popover picker**; `colorPickerType` Default or **UnityEditor**; custom picker interface.
- **ColorPicker**: wheel, SV square, RGB and HSV sliders, hex, alpha; **toolbar with previous/current swatches and an eyedropper**.
- **ColorSlider**, **ColorSwatch**, **ColorWheel**, **SVSquare**.
- **DateField / DateRangeField / DatePicker / DateRangePicker**: yyyy-MM-dd default with `formatString`; day/month/year views; configurable first weekday; localized.
- **AssetTargetField / Attachment / DropZone**: drop target with state feedback (the DropZone is editor-only for now).
- **Common input contract**:
  - **`ChangingEvent<T>`** fires continuously during interaction; **`ChangeEvent<T>`** fires once at commit or on programmatic set.
  - `validateValue` makes the field reject invalid values and **keep the previous value**.
  - `invalid` styling shows a destructive border.
  - `formatString`.

**Display**
- **Text**: TextSize XXS–XXXL; Small 6–20 px, Medium/Large 8–22 px; `primary`.
- **Heading**: HeadingSize XXS–XXL; Small 8/12/16/20/25/32/40, Medium 10/14/18/22/28/36/45; vertical padding control-gap-md or control-gap-xl. Rule: "don't skip levels".
- **Icon**: name plus variant (Regular, Bold, Light, DuoTone, Thin, Fill) plus IconSize; decorative, non-focusable.
- **Avatar / AvatarGroup**: Circular / Rounded / Square; image or initials with `autoLabelColor` (luminance); outline. AvatarGroup spacing −8 / −12 / −16 px with overflow.
- **Badge**: Default or **Dot**; anchors; overlap Rectangular or Circular (14% / 86% inset); minimum 12/18/24 px; label 8/10 px.
- **Chip**: Filled or Outlined; ornament (icon or avatar); `deletable` (delete button at opacity .55, 1 on hover); clickable; height = control-md.
- **Divider**: S/M/L = 1/2/3 px; spacing None/S/M/L; horizontal or vertical.
- **Spacer**: XS–XL or Expand.
- **Quote**, **CodeBlock** (language label, copy button revealed on hover, line-number gutter, TextMate highlighting), **MarkdownView**.
- **HelpBox**: `variant` = AlertSemantic; icon 16/24/32; padding control-gap-md × control-gap-lg; message sizes S/M/L.
- **Feedback**:
  - **LinearProgress** and **CircularProgress**, each Determinate or Indeterminate. Linear is 5/8/10 px high; circular 26/39/52 px.
  - **Preloader**: circular plus logo.
  - **ListViewItem `isLoading`**: skeleton title at 90% and subtitle at 65% width.

**Overlays and contextual UI** (see §3.6)
- `Popover`, `Modal`, `Dialog`, `AlertDialog`, `DialogTrigger`, `Tray`, `Toast`, `Tooltip`, `Menu`, `MenuItem`, `MenuSection`, `MenuDivider`, `MenuTrigger`, `MenuBuilder`, `RuntimeContextMenuManipulator` (context menus at runtime).

**Navigation**
- **AppBar**:
  - Height 28/42/56; compact 20/30/40.
  - Back and drawer buttons; actions.
  - **Stretch/collapse with a large title** (36 px) driven by `scrollOffset`.
  - Elevation.
- **Drawer**:
  - Temporary (backdrop, outside-click and back-button dismiss) or **Permanent**.
  - Left or right; **swipe-from-edge** (`swipeAreaWidth`, `hysteresis`).
  - `transitionDurationMs`.
- **NavigationRail**:
  - **3–7 destinations**; width 32/48/64.
  - Leading, main and trailing containers; group alignment start/center/end.
  - **LabelType All / Selected / None**.
  - "Don't combine with Drawer or BottomNavBar."
- **BottomNavBar**: **3–5 top-level destinations**; icon plus optional label plus badges.
- **Tabs / TabItem**:
  - Horizontal or vertical; `emphasized` (accent indicator) and `justified`.
  - Indicator 2 px, animated.
  - Item height = control-md.
  - Arrow-key navigation skips disabled tabs.
  - "Tabs should be used at the top level of navigation, not for subordinate views" (conflicts with Editor TabView usage; §5).
- **Breadcrumbs**: separator "/" (customisable); `isCurrent`.
- **PageIndicator** (dots), **PageView**, **SwipeView** (carousel, wrap, autoplay, resistance, `startSwipeThreshold`), **StackView** (push/pop/replace with per-transition animations).
- `NavHost`, `NavGraph`, `NavController`: §3.7.

**Layout and containers**
- **Panel**: root plus layers.
- **ContextProvider**.
- **SplitView / Pane / Splitter**:
  - Any number of panes, horizontal or vertical.
  - **`realtimeResize`** (live or deferred).
  - **Collapsible panes with expand buttons**.
  - `Pane.compactThreshold` **snaps to a compact mode**; `stretch` and `stretchFactor`.
  - **Persisted pane state**.
  - Splitter hit width 10/15/20 px with a **2 px visual anchor line**.
  - Pane minimum 10/15/20 px; RTL aware.
- **Toolbar**: horizontal or vertical; **`dockMode` Top / Bottom / Left / Right / Floating**; draggable with a drag bar; floating radius 4/6/8 with a 1 px border.
- **Accordion / AccordionItem**:
  - `isExclusive`.
  - Header height **24/36/48** (sizing-600, i.e. control-lg).
  - Indicator start or end; leading and trailing header slots.
  - Bottom border 1 px.
- **Canvas**:
  - Infinite pan and zoom with min/max zoom.
  - **Frame-to-fit**, grid background.
  - **Two control schemes:**
    - **Editor**: MMB pan, Alt+LMB pan, scroll zoom.
    - **Modern** (Figma-like): Space+LMB pan, Ctrl/Cmd+scroll zoom, pinch.
    - Both: Ctrl/Cmd + / − / 0.
  - Damping.
- **GridView / MasonryGridView**: virtualised, selection modes, keyboard navigation, drag-and-drop, context menu.
- **ListViewItem**: thumbnail, title (12/14 px), subtitle (8/10 px), options button, loading state; padding spacing-100; radius 6/9/12.
- **TreeViewItem**: caret plus title; **depth indent 12 / 18 / 24 px per level** (sizing-300); expanded and selected; usable without a TreeView.
- **Mask**, **ExVisualElement** (box-shadow, outline, dashed and dotted borders; render-pass mask for performance), **Scrollable** (drag-to-scroll, threshold 8 px).

**Collaboration** (new in 2.x/3.x, relevant to AI products)
- **Thread**: participants AvatarGroup; reply count; **resolve toggle**; likes, dislikes and reactions toggles; action menu.
- **ThreadMessage**: states, reactions bar.
- **ThreadComposer**:
  - TextArea; `maxTextLength` with a visible counter.
  - Attachments, DropZone, paste handling.
  - **`sending` state**; **editing mode with Cancel/Save**.
  - Mentions via `IMentionProvider`.
- **MentionPicker**, **ReactionPicker** (emoji grid), **ThreadResolveMessage** and **ThreadUnresolveMessage** (system rows).

### 3.6 Contextual UI and overlay system
Manual: https://docs.unity3d.com/Packages/com.unity.dt.app-ui@3.0/manual/overlays.html

**Layering:** `main-content` < `popup` < `notification` < `tooltip`. The tooltip is always highest.

**Popover**
- Anchored to a target.
- **32 placements**: 22 outside (Top / Bottom / Left / Right / Start / End, each with centre plus Start/End or Left/Right/Top/Bottom variants) and **10 Inside\*** placements, for overlays drawn within the target.
- `shouldFlip` when space is short; `offset` and `crossOffset`.
- Optional arrow tip: 12 px square rotated 45°, 24 px from the edge.
- `containerPadding`.
- **Transparent non-blocking backdrop by default, or `modalBackdrop`** (rgba 0,0,0,.4).
- `outsideClickDismiss` with strategy **Bounds versus Pick**; `keyboardDismiss` (Esc / back).
- **`movable` and `resizable`** (resize handle 8/12/16 px).
- Popover padding 12 px (8 px without arrow); container radius = control radius; bg `backgrounds-200`. The menu variant uses `base-100` with a 1 px `menu-border`.
- *"On small screen devices, it is recommended to use a Tray instead of a Popover."*

**Modal**
- Centred, blocking backdrop, focus trap.
- `ModalFullScreenMode`: **None / FullScreen (with margin "smir") / FullScreenTakeOver**.
- Outside-click dismiss optional.
- Content radius `border-radius-lg` (4/8/8 px); 12 px viewport padding; 150 ms open.

**Dialog / AlertDialog**
- Dialog sizes **S 400 px, M 500 px, L 640 px** wide.
- Padding spacing-400 (16/24/32); content and button-group top margin spacing-400; button gap control-gap-md.
- Dismissable close button.
- **AlertDialog semantics**: Default, Confirmation (positive), Information, Destructive, Error, Warning. Warning and error show a filled warning icon tinted with the semantic colour.
- **Up to three actions: primary (required), secondary, cancel**; primary and secondary can be disabled.

**DialogTrigger: one declaration, adaptive presentation**
- `type` (`PopupPresentationType`): **Modal / Popover / Tray / FullScreen / FullScreenTakeOver**.
- **`mobileType`** (`MobilePopupPresentationType`): Modal / Tray / FullScreen / FullScreenTakeOver. Popovers become modals on mobile by default.
- Plus placement, offsets, arrow, `trayPosition`, movable, resizable, `transitionDuration`.
- **This is the key cross-platform pattern: author once, present per form factor.**

**Tray**
- Slides from the **Bottom, Left or Right**; backdrop; drag handle 24×4 px (radius 2, margin 8); bottom tray max-width 640 px.
- Used for mobile menus and action sheets.

**Menu, MenuItem, MenuBuilder**
- Fluent `AddAction(id, label, icon, handler)`, `PushSubMenu`, `Pop`.
- MenuItem: label, icon, **`shortcut` text** (body-xs, disabled colour), **`selectable` checkmark**, submenu caret; `active`.
- Keyboard: Up/Down; **Left/Right enter and exit submenus (RTL-aware)**.
- Submenus open on click **or hover**.
- MenuSection has a title (secondary colour). MenuDivider.
- Item padding control-gap-md; radius = control radius. Hover/focus bg rgba(0,0,0,.1); selected = accent-selected alpha.
- *Menus show as Popovers on small screens "for the moment"; Trays are planned.*

**Toast (notifications)**
- **Single global queue across UIDocuments.**
- **One toast at a time; a new one replaces the previous one, even if it required interaction ("follow the Android design guidelines")**. The Toast API remarks claim stacking; see §5.
- `NotificationStyle`: Default / Informative / Positive / Negative / Warning, coloured fills with white text.
- `NotificationDuration`: Short / Long / **Indefinite**. Toasts with actions stay until acted on.
- `AnimationMode`: Fade or Slide.
- **10 placements**: Top / Bottom × Start / End / Left / Right / centre.
- Min-height = control-lg (24/36/48); padding 4 px × spacing-150; radius = control radius.
- `DismissType`: Action, Cancel, Consecutive, Manual, OutOfBounds, PanelDestroyed, Timeout.

**Tooltip**
- Shown on hover **or focus**; arrow tip; text or custom rich content via template.
- Container bg `backgrounds-300`; padding spacing-150 (6/9/12); radius = control radius; shadow y8/s16/b15.
- Delay and placement come from `TooltipDelayContext` and `TooltipPlacementContext`, configurable per subtree.
- *"Avoid putting critical information in tooltips as they may not be discoverable on touch interfaces."*

### 3.7 Navigation system
Manual: https://docs.unity3d.com/Packages/com.unity.dt.app-ui@3.0/manual/navigation.html

**Building blocks**
- An Android-Jetpack-style model: **NavGraph** (with a start destination, nestable) → **NavDestination** → **NavAction** (local or global) → **NavHost** (renders) plus **NavController** (back stack).
- **NavOptions:**
  - `enterAnim` / `exitAnim` / `popEnterAnim` / `popExitAnim`
  - `launchSingleTop`
  - `popUpTo` (route, inclusive, saveState, strategy)
  - `restoreState`
- **NavigationScreen** hooks: `SetupAppBar`, `SetupDrawer`, `SetupBottomNavBar`, `SetupNavigationRail`. An `INavVisualController` can do this globally.
- **DefaultDestinationTemplate** lets each destination declare which chrome it shows (AppBar, Drawer, BottomNavBar, NavigationRail).
- Visual **Navigation Graph Editor** (destination, action and nested-graph nodes; breadcrumbs for nested graphs; the start node is outlined green) plus **code generation** of action and destination constants.

**Chrome choice guidance, compiled from the API remarks**
- Phone: AppBar + BottomNavBar (3–5) or a temporary Drawer.
- Tablet/desktop: **NavigationRail** (3–7) or a permanent Drawer.
- Never combine a Rail with a Drawer or BottomNavBar.
- AppBar shows a back button automatically when the back stack is non-empty.

### 3.8 Input, gestures, keyboard and drag-and-drop

**Pointer and keyboard actions**
- **Pressable / Clickable** manipulators unify pointer, keyboard and other triggers.
- **KeyboardFocusController**: separate callbacks for keyboard-in, pointer-in and focus-out. It adds the `.keyboard-focus` class, so **focus rings show only for keyboard navigation**.
- **Draggable** manipulator: threshold, `actionKey` (Cmd/Ctrl), Alt, Shift, delta. **ResizeHandle**.

**Touch and trackpad gestures**
- `GestureRecognizer<T>`.
- **PinchGestureRecognizer**: two-touch; a distance threshold plus a movement-angle check separate pinch from pan.
- **TrackpadGestureManipulator**: macOS trackpad pinch.
- `AppUITouch` for Magic Trackpad touches.
- **Scrollable**: drag-to-scroll with an 8 px threshold.
- SwipeView: `startSwipeThreshold`, resistance.
- Drawer: edge swipe.
- `Platform.isTouchGestureSupported`.

**Drag and drop:** `DragAndDrop` (runtime or Editor), `DropZone`, `DropZoneController` (custom accept logic), `DragAndDropState` feedback.

**Haptics and clipboard**
- `Platform.RunHapticFeedback` (iOS and Android). No component uses haptics by default.
- **Clipboard** API with Text (UTF-8) and PNG formats.

### 3.9 Accessibility, localization, native integration
Manual pages: accessibility.html, localization.html, native-integration.html.

**Accessibility**
- Keyboard focus ring (keyboard-only), Tab and Shift+Tab via the UITK focus ring.
- **RTL via `DirContext`** (`.appui--rtl`), with mirrored components throughout.
- **System accessibility signals**: `highContrast`, **`reduceMotion`**, **`textScaleFactor`**, `darkMode` (with change events), `layoutDirection`, `scaleFactor`. The docs show a "System / Light / Dark" theme radio bound to `darkModeChanged`.
- Honest limitation: *"there are no universal standards"* for accessibility in game engines. **There is no screen-reader or semantics layer in App UI 3.0.**

**Localization**
- Any `text`, `title` or `label` that starts with `@` is a key: `@<table>:<entry>`, with fallback to the literal string.
- Works through the Unity Localization package. `LangContext` can be re-provided per subtree, with a custom translator function.

### 3.10 State, MVVM, undo
Manual pages: mvvm-*.html, state-management.html, undo-redo-sample.html.

**MVVM and state**
- MVVM via source generators: `[ObservableObject]`, `[ObservableProperty]`, `[ICommand]`, `[AlsoNotifyChangeFor]`.
- `RelayCommand` and `AsyncRelayCommand` (CanExecute drives enabled state).
- DI with transient, singleton and scoped lifetimes and conditional resolution.
- **Redux:** store, slices, action creators, **async thunks** (pending / fulfilled / rejected, abort with reason), middleware, enhancers, DevTools.

**UndoStack (Qt-like)**
- Push commands; `Undo()` and `Redo()`.
- **Command compression (merge)** and **macros** (multiple commands count as one).
- **Clean state** for "unsaved changes", with `cleanStateChanged`.
- **Memory-based `undoLimit`** and `memorySize`; `indexChanged`.

**Undo granularity sample**
- Live colour-picker drags and typing **do not push history**. A history entry is created **when the picker closes or the text field loses focus**.
- The Undo and Redo buttons disable at the boundaries.
- This maps directly onto ChangingEvent (preview) versus ChangeEvent (commit).

---

## 4. Why these are a good benchmark for dense, complex UIs

### 4.1 An explicit density strategy
- Foundations states it outright: "The Unity Editor is a **dense desktop software application**". From that follow:
  - a 6-step type scale with a 12 px default
  - 16/18/20 px control lines
  - 2 px between fields and 8 px between groups
  - 15 px nesting indent
  - text-only buttons
  - a "subtly nuanced palette"
- App UI turns density into a **runtime context**: `ScaleContext` small/medium/large, re-providable per subtree. It is orthogonal to per-component `Size` S/M/L.
- **Editor themes plus Small scale reproduce the Editor's density** inside a general-purpose system. This is the strongest piece of evidence for a parent system with a dense "pro" mode: the same component set, two token layers swapped.

### 4.2 Information hierarchy in inspectors
1. **Background lightness encodes level.** The object header and component headers are lighter; controls get darker as detail increases.
2. **Bold is a scarce resource.** It is reserved for component headers, top folders and override states (bold property name = overridden).
3. **Grouping escalates in order:** vertical space → header → foldout → tabs, with containers only for interactive groups.
4. **Two-column label/value grid.** The label column is 33% in App UI InputLabel and 50/50 in Unity Settings. Labels are left-aligned and unpunctuated, with tooltips on all labels.
5. **Messages live at the point of impact.** A help box sits under the affected property and pushes content down; the override bar runs on the left edge of the property; lock icons mark locked values.
6. **Focus is mirrored on the label** (the label turns blue), so the eye finds the active row in a long list.

### 4.3 Progressive disclosure
- Foldouts, with the arrow offset into the gutter and per-level indent.
- Accordions (exclusive or not).
- **Hide-versus-disable rules**, with hidden dependent controls placed below their trigger.
- Contextual tooling ("non-usable tools are never shown").
- Transient overlays, overlay layout modes (collapsed → panel), condensed search fields.
- ActionGroup **overflow menus**, splitter collapse and compact panes.
- Tooltips for depth: three lines, then a link to docs.

### 4.4 Keyboard-first and expert affordances
- Full keyboard map (§1.6); Esc reverts edits; Enter commits.
- **Delayed versus live fields.**
- Label-drag scrubbing (Editor and App UI `InputLabel.draggable`, `NumericalField.acceptDragging`).
- **Unit-aware formatted numeric fields with expression evaluation.**
- Slider Ctrl-snap policies and Shift for larger steps.
- **Shortcuts surfaced in tooltips from a central shortcut manager**, never hard-coded.
- Menu items show shortcut text.
- Selection history (Cmd/Ctrl+[ ]).
- Canvas control schemes (Editor versus Modern).

### 4.5 Multi-panel docking and windowing
- **Seven window types** with precise rules for dismissal and modality.
- Tab wells and kebab window menus; persistent layouts.
- **Overlays** docking to edge, corner or toolbar, with ghost and target drop zones and presets.
- App UI `SplitView` (live or deferred resize, collapse, compact threshold, persisted state) and `Toolbar.dockMode`.
- Movable and resizable popovers.
- **A responsive "no horizontal scroll at 275 px" contract for panels.**

### 4.6 Mixed values, validation, units, undo

**Mixed values: weak in both sources (a gap to fill)**
- Foundations defines toggle "indeterminate (or mixed)" and parent/child aggregation. App UI defines `CheckboxState.Intermediate`, which is programmatic only.
- **Neither documents a mixed-value display for numeric, text, colour or dropdown fields** (e.g. "—") in multi-object editing. Multi-editing is mentioned only as an Inspector "out of the box" benefit.
- We must specify this ourselves (§5).

**Validation**
- Editor: reject and revert to the last valid value; Esc reverts.
- App UI:
  - `validateValue` rejects the value and keeps the previous one.
  - `invalid` gives a destructive border.
  - InputLabel `required` (asterisk or text) and `helpMessage` with Default / Warning / Destructive variants.
  - Error and warning messages follow the Problem → Cause → Solution formula.

**Units and formatting:** App UI `unit` (scrubbable), `formatString`, `formatFunction`. The Editor's numeric page only covers int, float and double.

**Undo**
- The Editor relies on platform undo (not documented on the site).
- App UI provides a full **UndoStack** (compression, macros, clean state, memory limit) and documents **commit-point granularity**: blur or picker close.

**Contrast caveat:** the benchmark's own colours do not all pass (§1.2): Editor error text 2.25:1, link 3.2:1. App UI accent #0892FF with white text is 3.20:1, positive #11A85F with white 3.09:1, warning #D17100 with white 3.46:1 (all fail AA for normal text), and destructive #D74045 with white 4.46:1 (just short). Dark disabled text #6A6A6A on #1E1E1E is 3.08:1 (acceptable for inactive UI). App UI's dark text-primary #C0C0C0 on #1E1E1E (9.16:1) and secondary #AAAAAA (7.18:1) are comfortably AA.

---

## 5. Recommendations for the NEAR AI parent system

### 5.1 Adopt (high confidence)
1. **Two-axis sizing: density context × component size.**
   - Adopt App UI's model: a subtree-scoped **density context** (`compact` / `regular` / `touch`) plus a per-component `size` (S / M / L) on every control.
   - Suggested control heights on a **4-pt grid**. Do not use App UI's 0.75× multiplier, which yields 9/15/27 px.

   | Density | S | M | L | Body | Radius (control) | Gap md |
   |---|---|---|---|---|---|---|
   | compact (desktop pro surfaces, inspectors) | 16 | **20** | 24 | 12 | 4 | 4 |
   | regular (desktop app, web) | 24 | **28** | 32 | 13–14 | 6 | 8 |
   | touch (tablet/phone) | 36 | **44** | 48 | 16–17 | 10–12 | 12 |

   - Compact matches Unity Editor and App UI Small (16/20/24, 12 px). Touch M = 44 matches Apple HIG and L = 48 matches Material.
   - Regular sits near macOS (22–28 pt) and App UI Medium (24/30/36).
   - Density changes **sizes, spacing, radii and type step**, never colour.
2. **A five-layer token architecture**, mirroring App UI and naming like Unity:
   - Layers: palette (15-step ramps, base at step 800) → semantic → alias → component.
   - Semantic layer: neutral ramp plus **accent / destructive / warning / positive** each with **active / hover / base / tint1 / tint2**; backgrounds (canvas / app / subtle / border); foregrounds (disabled / secondary / primary / high-contrast); base (element pressed / element / hover / selected / border / border-hover).
   - Alias layer: family × property × state.
   - Use Unity's grammar: `{group}-{role_control}-{sub_element}-{states}`, with **multiple states alphabetical and underscore-joined** (`toolbar_button-text-focus_selected`).
   - Add a **`host-native` / pro theme slot**, the way App UI's Editor themes inject Editor colours via aliases. This is where a trace-commons dense mode (or a VS Code-like host) plugs in.
3. **Dense inspector spec.** Copy from Unity, adjusted to the 4-pt grid:
   - Panel padding 16 left / 4 right / 8 top-bottom (Unity uses 18 / 4 / 8).
   - Row height 20; 2 px between fields; 8 px between groups.
   - **Indent 16 per level** (Unity 15), capped at 6 levels.
   - Label column 33–40% (minimum 96 px), left-aligned, no colon, tooltip always present.
   - Bold only for section headers and overridden values.
   - Lighter header bands for higher hierarchy.
   - Help box under the control, ≤200 characters.
   - **Minimum panel width 275 px with no horizontal scroll.**
4. **Field behaviour contract** for every input:
   - `changing` (preview) versus `change` (commit) events. Undo entries are created on commit (blur, Enter, picker close).
   - **Enter commits, Esc reverts.**
   - Invalid input reverts to the last valid value and marks the field invalid with a reason.
   - Optional **delayed** mode only for slow or destructive properties.
   - Numeric fields: `unit`, `format`, **label/unit drag-scrub** (Shift = ×10, Alt = ×0.1), arrow-key nudge, and expressions.
5. **Mixed-value state.** This fills the gap in both sources.
   - Show "—" in text and numeric fields, a dash glyph in checkboxes and switches, "Mixed" in dropdowns, and a split or hatched swatch for colours.
   - Editing applies the value to all objects; Esc keeps them mixed.
   - The aggregation rules follow Unity's parent/child toggle logic.
6. **Hide-versus-disable rule.** Adopt it verbatim:
   - Disabled controls must explain why (tooltip).
   - **Never hide buttons.**
   - Dependent controls appear directly below their trigger.
7. **Messaging ladder.**
   - Four tiers: modal dialog → window/toast banner (auto-dismiss ~4 s, scaled to length) → inline help box → activity log/console. Choose by scope (app / window / section / operation) and severity (error / warning / info).
   - The **Problem → Cause → Solution** copy formula.
   - No "Error:" prefix.
   - Empty states (blank / idle / day-0) never use warning icons.
8. **Overlay system.**
   - App UI's four z-layers.
   - **`DialogTrigger`-style adaptive presentation:** popover on desktop → tray or sheet on phone; modal → full-screen on phone.
   - Popover placement vocabulary with flip; outside-click strategy (bounds versus pick); Esc dismiss.
   - **Tooltip delay as a context** (per-subtree), on hover *and* focus, instant hand-off between adjacent tooltips (Unity's rule), hidden on drag.
9. **Keyboard-only focus ring.**
   - A 2 px ring at 2 px offset, shown only for keyboard focus (App UI `KeyboardFocusController`).
   - Mirror focus onto the field's label (Unity).
   - ≥3:1 against adjacent colours.
10. **Contextual tooling principle:** "Non-usable tools are never shown". Expose tools, settings and actions by selection and mode. Test features together, not in isolation.
11. **Windowing and docking.** Define our window and panel types with Unity's exact dismiss and modality matrix (§2.2). Split panes with collapse, compact threshold and persisted state. Dockable toolbars and overlays with ghost and target drop zones.
12. **Copy rules:**
    - Labels ≤3 words, no ending punctuation.
    - Verbs plus object.
    - Confirm button mirrors the dialog title.
    - Ellipsis only when more input follows.
    - Tooltips in complete sentences, ≤3 lines, ≤200 characters, max width 300 px.
    - Shortcuts in tooltips come from a registry, never hard-coded.
13. **Collaboration and AI surfaces:** borrow App UI's **Thread / ThreadComposer / Mention / Reaction / Attachment / CodeBlock** anatomy and states (sending, editing, resolved, max length with counter, paste and drop) for agent chat and review UIs.
14. **Accessibility signals:** wire `reduceMotion`, `highContrast`, `textScaleFactor` and system dark mode into contexts (App UI exposes all four). Add the semantics and screen-reader layer that App UI lacks.

### 5.2 Conflicts to resolve (flagged)

| # | Topic | Unity Foundations | App UI 3.0 | Apple HIG / Material | Proposed resolution |
|---|---|---|---|---|---|
| 1 | **Depth model** | "Flat design… avoid shadows"; depth via accented borders and base layers | Elevation 0–24 shadows at rgba(0,0,0,.65); heavy popover, toast and modal shadows | Apple: vibrancy/glass materials; Material: tonal elevation plus shadow | Dense or in-flow surfaces: **layer by lightness and border, no shadow**. Shadows and glass **only on floating layers** (popover, menu, sheet, toast). Map trace-commons glass to the "floating" tier. |
| 2 | **Rounded corners** | Reserve radius for interactive elements, **not panels or containers** | Control radius 3/6/6; modal 4/8/8; list items 6/9/12 | Apple: concentric large radii on containers | Compact mode: 4 px controls, 0–4 px docked panels. Floating glass surfaces may use larger radii. Keep the rule "radius signals interactivity" *inside* panels. |
| 3 | **"Toggle" naming** | Toggle = **checkbox** ("checkbox" discouraged) | Toggle = **switch**; Checkbox separate | iOS Toggle = switch; macOS checkbox; Material Switch versus Checkbox | Name components **Checkbox** and **Switch**. Switch is for immediate-effect settings (mobile/web); Checkbox for forms, inspectors and multi-select. In compact desktop mode prefer Checkbox. |
| 4 | **Button and menu capitalisation** | Button page: sentence case. UI Writing Guide (newer): **Title Case** for labels, buttons, menus | n/a | macOS: Title Case buttons and menus; iOS and Material: sentence-style | **Platform-adaptive token.** Desktop (macOS) uses Title Case for buttons and menus; web and mobile use sentence case. Sentence case always for messages and tooltips. |
| 5 | **Tooltip timing** | Tooltip page: **0.4 s** delay, instant hand-off. Accessibility page: "default duration 1.5 s" | Delay via `TooltipDelayContext` (configurable) | macOS ~0.5–1 s; Material ~0.5 s hover | Show delay **500 ms** (dense: 400 ms), instant hand-off between neighbours, hide on drag, no auto-hide while hovered. Treat 1.5 s as a minimum *visible* time on focus. |
| 6 | **Toast stacking** | Window banners: one per window, 4 s | Manual: **one toast at a time, replaces previous** (Android). API remarks: "multiple toasts can be stacked" | Material snackbar: one at a time; macOS: notification stack | Desktop: stack up to 3 with collapse. Mobile: one at a time. Toasts with actions persist until acted on or timed out (≥6 s). |
| 7 | **Tabs scope** | TabView for in-panel segmentation (≤4 tabs in a 275 px inspector; no disabled tabs) | "Tabs should be used at the top level of navigation, not for subordinate views" | Apple segmented controls for in-view switching | Two components: **Tabs** (navigation) and **SegmentedControl** (in-panel view switch, ≤5 segments). Never show disabled tabs. |
| 8 | **Dropdown versus radio threshold** | Radios ≤5, dropdown above 5 | Dropdown 3–10; fewer → radio or toggle buttons; more → searchable combobox | Material: menus for many options | Inline radios or segmented for 2–5; dropdown for 6–15; **searchable combobox above 15**. |
| 9 | **Disabled styling** | 40% alpha on the whole control, label included | Colour token `foregrounds-25` plus component opacities (.5 picker items, .4 chip, .25 avatar) | Apple: system disabled colours; Material: 38% | One rule: **38–40% opacity on the whole control** (token `opacity-disabled`). Inactive UI is exempt from contrast, but disabled reasons must be in a tooltip. |
| 10 | **Click target** | Recommends 44×44 (WCAG 2.5.5) while controls are 16–20 px; solved with enlarged hit areas | Small-scale controls 16–24 px | Apple 44 pt; Material 48 dp; WCAG 2.2 AA 2.5.8 = 24×24 px (spacing exception) | Compact mode: hit area ≥24×24 via invisible padding or spacing (2.5.8 AA). Touch mode: ≥44 (Apple) or 48 (Android). Never ship compact density on touch-primary devices. |
| 11 | **Dialog button order** | Editor-native: destructive left, primary right; OS dialogs follow OS order (varies by macOS version and Windows) | AlertDialog: primary, secondary, cancel (order follows layout direction) | macOS: default rightmost, Cancel to its left, destructive separated; Windows: OK then Cancel; Material: confirm right | **Platform-adaptive ordering**, with destructive actions isolated at the far left on desktop. Primary is the default button (Enter); Esc = Cancel. |
| 12 | **Links** | Blue links reserved for **leaving the app**; underline only on hover | Link component; "use styling like underlines" | Web: underline by default | In-app navigation uses buttons or list rows. External links get a link style plus an external-link icon. Underline by default on web content; hover-underline in dense desktop chrome. |
| 13 | **Contrast of semantic fills** | Error text #D32222 on #383838 = 2.25:1; link 3.2:1 (yet docs claim the vars comply) | White on accent #0892FF 3.20:1; on positive 3.09:1; on warning 3.46:1; on destructive 4.46:1 | WCAG 4.5:1 text | Use **step 600–700** of each semantic ramp behind white text (white on blue-700 #0780DF = 4.07:1 (large text only); blue-600 #066EBF = 5.26:1; green-600 #0D7E47 = 5.13:1; orange-600 #9D5500 = 5.63:1; red-700 #BC383C = 5.57:1), or dark text on light fills. Run an automated contrast check over the generated token sets. |
| 14 | **Font size defaults** | 12 px default; 9 px minimum | Medium and Large body 14 px; Small 12 px | macOS body 13 pt; iOS body 17 pt; Material body 14–16 sp | Compact 12, regular 13 (desktop) or 14 (web), touch 16–17. Minimum 10 px (11 preferred); 9 px only for data labels inside charts and graphs. |
| 15 | **Icons** | PNG 16 px (14 live), `d_` dark variants, @2x | PNG tinted white, 6 weights, @2x | SF Symbols (vector, weights match text) | **Vector icons only**; 16 px compact / 20 regular / 24 touch; weight tied to text weight; tint via token. Keep Unity's verb accent colours (add / modify / select / remove) for tool-mode icons only. |
| 16 | **Shadow and glass legibility** | Text over translucent backgrounds must pass contrast "no matter what image may appear behind" | n/a | Apple Liquid Glass uses adaptive vibrancy | Glass surfaces need a guaranteed backdrop-tint floor (opacity or blur) so text keeps 4.5:1 against worst-case content. Test with a worst-case backdrop. |

### 5.3 Do not copy
- App UI Medium's 0.75× scale (fractional and odd values) and the token-file bugs listed in §3.3.
- The 500 ms button background transition. Use 90–150 ms ease-out for state changes in dense UIs.
- Single-hue blue for everything focus-, pressed- and selected-related *at full saturation* in dense views. Unity itself mutes selection to #2C5D87 / #46607C in dark mode; keep saturated accent for focus rings and primary actions only.
- IMGUI-era PNG and MIP icon pipelines.
