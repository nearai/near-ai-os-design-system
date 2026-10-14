# Unity community Figma files: findings for the NEAR AI parent design system

Research stream: three Unity community Figma files, read only. Nothing was created, duplicated, edited or commented on.

| File | fileKey | What it is |
|---|---|---|
| Unity Editor UI Toolkit Library (Community) | `i1I4ZMJSIDZLEwSR3OB9pE` | "LTS 2022.3 · Unity Editor ❖ Component Library · Editor Foundations Design System" (from the cover). This is the Editor Foundations (EFDS) component kit. |
| App UI v3.2 (Community) | `bxZuvMcV7ULoFkGnrMhCus` | "v3.2 · App UI Design System · App UI / Documentation" (from the cover). This is a Figma kit for Unity's App UI package, built on Variables, with one page per component. |
| Unity Editor Icon Library (Community) | `NjKHFVJ0jfB3H0GWmBbO6p` | The official Editor core icons as .png at 1x/2x, Light and Dark, with selected states |

The raw corpus is in `corpus/unity-figma/`: page index, verbatim errors, token dumps, component inventories, node ids and measurements. One screenshot is saved in `corpus/unity-figma/screens/`.

---

## 0. Access, method and confidence

### 0.1 What worked and what did not (exact errors are in `corpus/unity-figma/ERRORS.md`)

1. **Remote Figma MCP (`get_metadata` without a nodeId)** listed only the cover page of each file (for example `- 402:296: . Cover`). It did not list the other pages, but they could still be reached by id.
2. **Remote `get_metadata` on a whole page** (UITK Color Palette 405:297) failed with
   `Failed to parse SSE message … Invalid JSON: EOF while parsing a string at line 1 column 77271`. The response was too large to parse.
3. **Remote `get_variable_defs` on a page id** returned `You currently have nothing selected. You need to select a layer first before using this tool.`. Calling it on frame ids worked.
4. **Remote `get_variable_defs`** succeeded on 5 UITK frames (Component Colors, Inspector & Window, Toolbar, Text, Application Bar). It returned exact hex values for every Editor colour style, plus text and effect styles. These are the highest-confidence data in this report.
5. **About 20 calls in**, every remote tool started returning
   a message that the Figma MCP tool-call limit for the account's plan had been reached.
   The connector billed these community files to a plan with a call cap rather than to the team plan.
6. **Desktop MCP (`mcp__Figma__*`)** returned `To use this tool, you need to enable the Dev Mode MCP Server in the Figma desktop app.` I left the setting unchanged.
7. **`search_design_system`** against the UITK key returned empty arrays. **`get_libraries`** listed only Apple, Material and Simple Design System community kits, so these Unity files are not subscribed libraries.

### 0.2 Fallback used

I opened the Figma web viewer for each file in the Claude built-in browser, signed out and view-only. The banner read "Sign up to comment, edit, inspect and more", so Inspect and Dev Mode were unavailable. From there I collected:

- **Page lists and ids**, read from the pages panel React props (`nodeId`).
- **The full layer tree**: names, node types, hierarchy and ids. I expanded the layers panel programmatically and read `data-testid="<id>-layers-panel-row"` rows. That gave every component set with its variant value strings, every App UI page description (the kits embed long spec text in layer names), and all 283 icon layer names.
- **Exact sizes** from the canvas selection badge (for example "54 Hug × 20 Hug"). I navigated to each variant's `node-id` and zoomed on the badge.
- **Approximate colours and spacings** for App UI by decoding lossless PNG crops in Python (stdlib PNG decoder in `scripts/unity-figma/pngread.py`). The App UI ramps are screen-sampled and accurate to about ±2 per channel. App UI sizing/spacing bar widths are accurate to about ±1 px.

### 0.3 Confidence legend used below

- **[exact]**: values from `get_variable_defs` or from the selection badge.
- **[verbatim]**: text copied from layer names or doc text in the file (file content, treated as data).
- **[sampled]**: read from rendered pixels.
- **[inferred]**: my reading of screenshots or structure.

---

## 1. Unity Editor UI Toolkit Library (EFDS component kit, LTS 2022.3)

### 1.1 Page map

| Page id | Page | Contents |
|---|---|---|
| 402:296 | . Cover | "LTS 2022.3 / Unity Editor, ❖ Component Library / Editor Foundations Design System ↗" |
| 915:20168 | . Feedback | Rendered empty in the viewer |
| 405:296 | FUNDAMENTALS ↓ | Section separator page |
| 405:297 | 01. Color Palette | Intro, ". Base Layers", INDEX; colour-style boards: Application Bar Colors (579:4538), Component Colors (438:2546), Inspector & Window Colors (514:1792), Toolbar Colors (927:51545), Text Colors (429:818) |
| 405:298 | 02. Text Styles | ". Type Scale" (1859:86474) and "Text Styles / Editor Text Styles" (825:15737, 1920×2444) |
| 405:299 | COMPONENTS ↓ | Separator |
| 405:300 | 01. ❖ Components | 21 stickersheet frames, one per control family, each with Dark and Light component sets (§1.5) |
| 842:13210 | GROUPS ↓ | Separator |
| 842:13612 | 02. ⏣ UI Groups | Composed molecules: Button Groups, Control Rows, Inspector Header & Panels, Tabs & Navigation, Toolbars, View Groups (§1.6) |
| 1999:89894 | 03. Templates (Dark mode) | "Editor / 2022.3 Default layout" (full editor plus Hierarchy, Project, Scene, Inspector, Console, App Bar, Undocked window) and "Localization Package / v2.0" screens (§1.7) |
| 1983:89890 | 04. ❏ Window and Panels (Dark mode) | Default window variants (54), modals, empty states, panel atoms (§1.7) |
| 1463:75239 | 05. ✦ Other/Support | 36 cursor components; macOS 12 chrome (menus, window frame, dialog, light and dark); Windows chrome placeholder |
| 426:8 | LIBRARY COMPONENTS | "/ EDS Library Helper" with doc helper components "color style" and "text style" |
| 0:1 | ———— End ———— | Thumbnail instance |

**Structural pattern.** Every control has a **twin component set per theme** ("X - Dark" and "X - Light") with identical variants. The kit does **not** use Figma variable modes for Light and Dark. Colours are colour **styles** whose names carry the theme prefix, for example `Dark/Buttons/--unity-colors-button-background`. Each style name embeds the real Unity USS variable name. This makes the Figma kit a 1:1 map of the Editor's USS theme variables.

### 1.2 Colour tokens: Editor theme [exact]

The values come from `get_variable_defs` on the palette boards. Names are the Unity USS custom properties, shortened by dropping the `--unity-colors-` prefix. The screenshot of the Inspector & Window board also gives the highlight-hover overlay alpha: **dark `rgba(255,255,255,0.06)`, light `rgba(0,0,0,0.062)`**.

#### 1.2.1 Window, panel and selection surfaces

| Token (`--unity-colors-…`) | Dark | Light | Role |
|---|---|---|---|
| `window-background` | `#383838` | `#C8C8C8` | Main panel and window body |
| `default-background` | `#282828` | `#A5A5A5` | Recessed areas (scene and project list background, app bar context) |
| `alternated_rows-background` | `#3F3F3F` | `#CACACA` | Zebra rows in lists and tables |
| `highlight-background` | `#2C5D87` | `#3A72B0` | Selection, focused window |
| `highlight-background-inactive` | `#4D4D4D` | `#AEAEAE` | Selection when the window is not focused |
| `highlight-background-hover` | `#FFFFFF` @ 6% | `#000000` @ 6.2% | Hover overlay on rows |
| `highlight-background-hover-lighter` | `#5F5F5F` | `#9A9A9A` | Stronger hover |
| `inspector_titlebar-background` | `#3E3E3E` | `#CBCBCB` | Component header strip |
| `inspector_titlebar-background-hover` | `#474747` | `#D6D6D6` | |
| `toolbar-background` | `#3C3C3C` | `#CBCBCB` | Window toolbars |
| `app_toolbar-background` | `#191919` | `#8A8A8A` | Main application bar |

#### 1.2.2 Borders

| Token | Dark | Light |
|---|---|---|
| `default-border` | `#232323` | `#999999` |
| `window-border` | `#242424` | `#939393` |
| `toolbar-border` | `#232323` | `#999999` |
| `inspector_titlebar-border` | `#1A1A1A` | `#7F7F7F` |
| `inspector_titlebar-border_accent` | `#303030` | `#BABABA` |

Effect style **"Toolbar Mid - Dark"** draws 1 px hairline separators as three zero-blur inner shadows in `#232323`: offsets (1,0), (−1,0) and (0,−1). Separators are drawn as part of the control rather than as separate divider elements.

#### 1.2.3 Text

| Token | Dark | Light |
|---|---|---|
| `default-text` | `#D2D2D2` | `#090909` |
| `default-text-hover` | `#BDBDBD` | `#090909` |
| `window-text` | `#BDBDBD` | `#090909` |
| `label-text` | `#C4C4C4` | `#090909` |
| `label-text-focus` | `#81B4FF` | `#003C88` |
| `highlight-text` | `#4C7EFF` | `#0032E6` |
| `highlight-text-inactive` | `#FFFFFF` | `#FFFFFF` |
| `link-text` | `#4C7EFF` | `#4C7EFF` |
| `visited_link-text` | `#FF00FF` | `#AA00AA` |
| `error-text` | `#D32222` | `#5A0000` |
| `warning-text` | `#F4BC02` | `#333308` |
| `helpbox-text` | `#BDBDBD` | `#161616` |
| `preview_overlay-text` | `#DEDEDE` | `#FFFFFF` |
| `tab-text` | `#BDBDBD` | `#090909` |
| `toolbar_button-text` (default, hover, checked) | `#C4C4C4` / `#BDBDBD` / `#C4C4C4` | `#090909` |
| `dropdown-text` | `#E4E4E4` | `#090909` |
| `button-text` | `#EEEEEE` | `#090909` |

Disabled states in the stickersheets are rendered at reduced opacity; the kit has no separate disabled text colour [inferred].

#### 1.2.4 Controls

| Control / token | Dark | Light |
|---|---|---|
| **Button** `button-background` | `#585858` | `#E4E4E4` |
| `button-background-hover` | `#676767` | `#ECECEC` |
| `button-background-focus` | `#6E6E6E` | `#BEBEBE` |
| `button-background-pressed` | `#46607C` | `#96C3FB` |
| `button-background-hover_pressed` | `#4F657F` | `#B0D2FC` |
| `button-border` | `#303030` | `#B2B2B2` |
| `button-border_accent` (bottom edge) | `#242424` | `#939393` |
| `button-border_accent-focus` | `#7BAEFA` | `#018CFF` |
| `button-border-pressed` | `#0D0D0D` | `#707070` |
| **Input field** `input_field-background` | `#2A2A2A` | `#F0F0F0` |
| `input_field-border` | `#212121` | `#B7B7B7` |
| `input_field-border_accent` | `#0D0D0D` | `#A0A0A0` |
| `input_field-border-hover` | `#656565` | `#6C6C6C` |
| `input_field-border-focus` | `#3A79BB` | `#1D5087` |
| **Dropdown** `dropdown-background` | `#515151` | `#DFDFDF` |
| `dropdown-background-hover` | `#585858` | `#E4E4E4` |
| `dropdown-border` | `#303030` | `#B2B2B2` |
| `dropdown-border_accent` | `#242424` | `#939393` |
| **Object field** `object_field-background` | `#282828` | `#EDEDED` |
| `object_field-border` / hover / focus | `#202020` / `#656565` / `#3A79BB` | `#B0B0B0` / `#6C6C6C` / `#1D5087` |
| `object_field_button-background` / hover | `#373737` / `#4C4C4C` | `#DEDEDE` / `#CCCCCC` |
| **Toolbar button** `toolbar_button-background` | `#3C3C3C` | `#CBCBCB` |
| hover / focus | `#464646` | `#C1C1C1` |
| checked | `#505050` | `#EFEFEF` |
| `toolbar_button-border` | `#232323` | `#999999` |
| **App toolbar button** background / hover | `#383838` / `#424242` | `#C8C8C8` / `#BBBBBB` |
| pressed / checked | `#6A6A6A` | `#656565` |
| border / border_accent | `#191919` / `#222222` | `#6B6B6B` / `#6B6B6B` |
| **Tabs** `tab-background` | `#353535` | `#B6B6B6` |
| `tab-background-hover` | `#303030` | `#B0B0B0` |
| `tab-background-checked` | `#3C3C3C` | `#CBCBCB` |
| tab highlight (active accent) | `#2C5D87` | `#3A72B0` |
| **Slider** groove / groove-disabled | `#5E5E5E` / `#575757` | `#8F8F8F` / `#A4A4A4` |
| thumb / hover / disabled | `#999999` / `#EAEAEA` / `#666666` | `#616161` / `#4F4F4F` / `#9B9B9B` |
| thumb border / disabled | `#999999` / `#666666` | `#616161` / `#9B9B9B` |
| thumb halo (focus) | `#106FCD` | `#0C6CCB` |
| **Scrollbar** thumb / hover | `#5F5F5F` / `#686868` | `#9A9A9A` / `#8E8E8E` |
| thumb border / hover | `#323232` / `#686868` | `#B9B9B9` / `#8E8E8E` |
| button hover | `#494949` | `#A7A7A7` |
| groove, button background | `#000000` (used with alpha) | `#000000` (alpha) |
| **Help box** background / border | `#606060` / `#232323` | `#EBEBEB` / `#A9A9A9` |
| **Tooltip** background / border | `#373737` / `#191919` | `#DEDEDE` / `#8A8A8A` |

Kit-only helper styles (not Unity tokens): `Dark/Feedback/Scarlet #FF534A`, `Dark/Primary/LightGray #C4C4C4`, `Pro/Icon/figma-icon-color #C4C4C4`, `Pro/Icon/figma-icon-blue #80D8FF`, `DG Border #565758`, documentation chrome `Project/Canvas/Gray BG #F6F6F6` and `Project/Text/Default #383838`.

#### 1.2.5 Reading the palette (dense-UI lessons)

- **Raised controls, recessed wells.** In Dark the window is `#383838`. Buttons sit lighter at `#585858`, dropdowns at `#515151`, and text, numeric and object fields sit darker at `#2A2A2A` / `#282828`. The lightness relation itself signals whether an element is a command or a value well, with no shadows.
- **Two-tone bevel borders.** Buttons and dropdowns have a 1 px border plus a darker `border_accent`. In the screenshots the accent sits on the bottom edge [inferred]. It gives a crisp 1 px bevel at 20 px heights.
- **Focus-aware selection.** Selection is blue `#2C5D87` while the window has focus and grey `#4D4D4D` when it does not. This is an essential dense multi-pane pattern.
- **Overlay hover.** Row hover is white at 6% (black at 6.2% in Light), so a single overlay token works on any row background.
- **Separate focus colours.** Field focus border is `#3A79BB`, button focus ring is `#7BAEFA`, and the focused label text turns `#81B4FF`. The label of the focused field changes colour as well as its border.
- **A neutral grey ladder** of about 25 steps between `#191919` and `#EEEEEE` carries almost the whole UI. Hue appears only in selection, focus, links and status.

### 1.3 Typography [exact + verbatim]

The doc frame states "6 scale options. Text styles are purposely limited to only 6 size options. The Unity Editor is a dense desktop software application…". It also warns that the Editor default `--unity-font-size` is **12 px**, but Inter renders slightly larger in Figma than in the Editor, so the kit's default style is **11.5 px**.

| Name | USS variable | Size (Figma) | Line height | Weights | Annotated usage (Project Settings, Profiler screenshots) |
|---|---|---|---|---|---|
| Very Big | `--unity-font-size-very-big` | 19 px | 23 px | Regular | Settings page titles |
| Big | `--unity-font-size-big` | 14 px | 17 px | Regular | Window section headers |
| Default | `--unity-font-size` (12 px in Editor) | 11.5 px | 14 px or 16 px | Regular, Bold | All controls and labels |
| Semi-small | `--unity-font-size-semi-small` | 11 px | 13 px | Regular | Secondary labels |
| Small | `--unity-font-size-small` | 10 px | 12 px | Regular | Help text, captions |
| Tiny | `--unity-font-size-tiny` | 9 px | 11 px | Regular | Profiler and timeline annotations |

- The family is **Inter** throughout. The text-style objects returned by the MCP show `--unity-font-size (default)/11.5 Reg` as Inter Regular 11.5 with 100% line height and letter-spacing 0.1. `--unity-font-size-small/10px` is Inter Regular 10, 100% line height, letter-spacing 0.15.
- The documentation chrome uses Roboto Mono Medium 10/16 and 12/14 for token captions, and Inter 14/24 for body copy. These are kit styles, not product styles.
- Bold is used only for emphasis inside the Default size: component titles, scene root in Hierarchy, bold foldouts and tree items. There is **no separate heading scale inside panels**.

### 1.4 Effects

| Style | Definition | Use |
|---|---|---|
| Toolbar Mid - Dark | 3 × INNER_SHADOW `#232323`, radius 0, offsets (1,0), (−1,0), (0,−1) | Hairline segment separators in toolbars |
| Image Shadow | DROP_SHADOW `#0000001A`, (0,4), blur 8 | Doc imagery |
| EDS Frame | DROP_SHADOW `#EBEBEB` (0,8) r4 s1 + `#DBDBDB` (0,3) r6 | Doc frames only |

The product components use **no elevation shadows**. Depth comes from fills and 1 px borders. Floating surfaces (menus, modal windows) borrow macOS native chrome from the Support page.

### 1.5 Component inventory (Components page 405:300)

The 21 stickersheet sections are AppBar Button, Button, Color Field, Dropdown, Foldout, Help Box, Label, List View, Numeric Field, Object Field, Progress Bar, Radio Button, Scroll View, Search Field, Slider, Tab, Text Field, Toggle (Checkbox), Toolbar, Tooltip and Tree View. Variant values are shown as Figma lists them, comma-separated in property order. The layers panel does not show property names. **Sizes [exact]** come from the selection badge on the Dark Default variant.

| Component set (Dark id) | Variants (values) | Count | Measured size |
|---|---|---|---|
| Basic Button (480:1526) | {Default, Default+Hover, Pressed, Focus, Focus+Hover, Pressed+Focus, Disabled} × {mini, regular, large} | 21 | mini **46×18**, regular **54×20**, large **62×24** (hug, label "Label") |
| Basic Button Group L,M,R (482:1224) | 7 states × 3 sizes × {Left, Mid, Right} | 63 | Segment pieces: only outer corners rounded |
| Basic Button Groups (1134:55116) | mixed × 3 sizes × {Group of 3, Group of 4} | 6 | |
| Toggle Button (483:1127) and Group L,M,R (483:1235) and Groups (1134:55118) | Same matrices as Basic Button | 21 / 63 / 6 | |
| App Toolbar Button (933:46155) | Default, Default+Hover, Pressed, Disabled | 4 | **63×20** (icon + "Pivot") |
| App Toolbar Button Group L,M,R (933:46824) and Groups (933:55422) | 4 states × {Left, Mid, Right}; Group of 2/3 | 12 / 2 | |
| AppCommand (Toggle) (930:45926) | Default, Default+Hover, Pressed, Checked, Disabled | 5 | **30×20** icon-only |
| AppCommand Group L,M,R (931:46253) and Groups (933:55202) | 5 states × L/M/R; Group of 3/6 | 15 / 2 | |
| Text Field (438:2536) | Default, Hover, Focused, Disabled | 4 | **80×18** |
| Dimension Style Field (2579:110936) | Default, Hover, row-Focused, button-Focused, Disabled | 5 | **180×18** (value + unit button) |
| options pop-up (2579:110963 / 111073) | {Default, Hover, Focused} × {auto/initial, %, px} | 9 | Unit selector ("--", "%", "px") |
| Numeric Field (933:51128) | Default, Hover, Focused, Disabled | 4 | **80×18** |
| Numeric Fields, Vector (1072:55492) | 2 Fields, 3 Fields, 4 Fields | 3 | 3 fields **263×18** with inline X/Y/Z labels |
| Dropdown (915:16717) | {Default, Default+Hover, Focus, Focus+Hover, Disabled} × {Label, Icon} | 10 | Label variant **160×18** |
| Object Icon Button (1579:74921) | Default, Hover | 2 | |
| Object Fields (1080:55272) | {Default, Hover, Focused, Accepted, Disabled} × Object Icon={Ture [sic], False} | 10 | **200×18** (type icon + name + ⊙ picker) |
| Object Field Button (1082:55556) | Default, Hover | 2 | |
| Color Field (1969:91333) | Default, Hover, Focused, Disabled | 4 | **160×18** (swatch + eyedropper) |
| Color Picker Modal (1976:90042) | Composite: picker, colour wheel, RGB/A rows, hex, foldout, mac window | 1 | |
| Label (454:257) | Default, Focused, Disabled | 3 | **74×18** hug ("Control Label") |
| Toggles (496:1366) | {Default, Hover, Focused, Disabled} × {Unchecked, Checked, Indeterminate} | 12 | Box **14×14** |
| Radio Button (5108:101165) | Default, Hover, Focused, Disabled (checked and unchecked in sheet) | 4 | **12×12** |
| Slider (408:2405) | Default, Hover, Focused, Disabled | 4 | **230×10** track area |
| Slider Thumb (430:527) | Default, Hover, Focused, Disabled | 4 | **10×10** |
| MinMax Slider (422:0) and Thumb (430:492) | 4 states each | 4 / 4 | |
| Foldout (941:53577) | {Default, Hovered, Focused, Disabled} × {▶ Collapsed, ▼ Expanded} × {Regular, Bold} × {Base, Level 1, Level 2} | 48 | **64×18** hug |
| Foldout wIcon (944:54217) | 4 states × Collapsed/Expanded × Regular/Bold | 16 | |
| Foldout Arrow (941:53963) | Collapsed, Expanded | 2 | |
| Help Boxes (1460:73430) | Error, Warning, Info / Log | 3 | **378×37** hug (2 lines) |
| Tooltips (1909:93227) | 1 (wraps Label) | 1 | **300×48** hug (3 lines) |
| Tab (576:5853) | Default (Inactive), Hover, Checked, Checked+Focused | 4 | **69×20** hug |
| Tab + Icon (920:40804) | Same 4 | 4 | **68×20** hug |
| Tab Dock (576:6115) | Composite: Tabs + Icons (lock, kebab) + dock background | 1 | **380×20** |
| Toolbar Button / Toolbar Toggle / Toolbar Menu (549:4399 / 548:4252 / 640:4586) | {Default, Hover, Checked, Focus} × {Label, Icon} | 8 each | Label **97×20**, Icon **28×20**, Menu **115×20** |
| Toolbar Container (558:4283) | 1 | 1 | **260×20** |
| Toolbar Search Field (933:52823) / Toolbar Popup Search Field (993:55196) | Default, Hover, Focused, Disabled | 4 each | **200×16** |
| Scene Toolbar (2091:106527) | Controls / Left + Controls / Right | 1 | |
| Scroll View (1368:66776) | Horizontal, Vertical | 2 | |
| List View Item (1318:63546) | {Default, Hovered, Selected, Focused, Disabled} × {Regular, Bold} × {Base, Level 1 (15px)} | 20 | **113×16** hug |
| List View (2077:91834) | Scroll View + Foldout + Items | 1 | |
| Tree View Item (1240:62436) | {Default, Hovered, Selected, Focused, Disabled} × {▶ Collapsed, ▼ Expanded} × {Regular, Bold} at "Base 0", plus Default × {Collapsed, Expanded, End-node} × Level 1–5 (15/30/45/60/75 px) | 35 | **120×16** hug |
| Tree View (1631:77064) | Scroll View + Items | 1 | |
| Progress Bar (7036:13819) | 1 (Label + progress + bar) | 1 | **344×18**, centred label |

**State model.** The full Editor state vocabulary is **Default · Hover · Focused · Focus+Hover · Pressed · Pressed+Focus · Checked · Selected · Accepted · Disabled**. "Accepted" is the drag-and-drop accept state on object fields. Selection and focus are separate dimensions: a list row can be Selected without Focused, which is the grey inactive selection.

**Size model.** The buttons come in three sizes: **mini 18, regular 20, large 24**. Every other control has a single size, 18 px for value fields and 20 px for toolbar items and tabs. Rows in trees and lists are **16 px**. The Toolbar search field is a compact **16 px** variant of the 18 px field.

### 1.6 Composite patterns ("UI Groups" page 842:13612)

| Group | Components | Notes |
|---|---|---|
| Button Groups | Wide Button (fixed), 3 Buttons (fixed), 2 Buttons (fixed), Basic/Toggle Button Groups | Doc: "Add Component Button Panel, 2 Buttons, 3 Buttons" |
| Control Rows | 2 columns (fill), 2 columns (fixed), 3 columns (2controls), 3 columns (2labels), Enable-disable control, Controls in Foldout | Doc: "Content rows with 2 and 3 columns. Row: 2 columns (fill and fixed)". "Swappable control" slot. **Fill width**: control scales when resized. **Fixed width**: control keeps its width. Annotations "0 padding", "Indentation: Base / Level 1 / Level 2". Example 2-col fill block **390×179** |
| Inspector Header and Panels | Inspector Header (**360×60**), Component Header, Panel: Transform (**320×92**), Panel: Rect Transform, Panel: Simple, Panel: Complex (**320×373**), Component Panel + Helpbox | Doc: "Transform component panel, simple and complex component panels with indentation" |
| Tabs and Navigation | Tab Dock (primary and secondary), Window menu (macOS 12) | |
| Toolbars | Scene Toolbar **664×20**, Example Toolbar, Hierarchy Toolbar **454×20**, Console Toolbar **600×20**, Project Toolbar **600×20** | |
| View Groups | Tree View, List View | |

#### Inspector anatomy [exact sizes + inferred layout, from screenshots at 100%]

- **Inspector Header (GameObject) 360×60.** Row 1 has a 32 px object icon with a dropdown chevron, an active checkbox, the name field (fills the width) and "Static" checkbox ▾. Row 2 has Tag ▾ and Layer ▾ dropdowns side by side with inline labels.
- **Component Header, about 22 px.** In order: ▼ foldout arrow, 16 px component icon, enable checkbox, **bold** component name. Right-aligned are a help "?", presets "⇄" and a kebab "⋮". Background `inspector_titlebar-background`, with 1 px top and bottom borders `#1A1A1A` / `#303030`.
- **Property row pitch is 20 px**: an 18 px control plus 2 px gap. The **label column is about 120 px**, measured from the panel edge to the control start in Panel: Complex. The control fills the remaining width, so labels truncate rather than wrap [inferred].
- **Indentation is 15 px per level.** Panel: Complex shows Base 0, Level 1, Level 2 with labels stepping by about 15 px, and foldouts ("Foldout (Base level)", "Foldout (Level 1)") nest the same way.
- **Mixed composite rows** are common: `Label | [slider ————○] [0]` (slider plus numeric field) and `Label | Label [Input]` (sub-label plus field, the 3-column pattern). Vector rows are `Label | X [0] Y [0] Z [0]` with tiny inline axis labels.
- **Panel width defaults to 320 px**, and the Inspector template is 400 px.
- The Inspector ends with a warning HelpBox and a centred **Add Component** wide button of about 160×20.

### 1.7 Windows, panels, templates and layouts

**Default window (component set 2007:90728, 54 variants).** The properties are background {`window-bg`, `default-bg`, `alternated_row-bg`} × show Tab {Yes, No} × show Toolbar {Yes, No} × panels {1, 2, 3} × {Hide, Show}. The fourth property is probably splitter or padding visibility [inferred]. The 2-panel variant measures **360×240**. It has a **20 px tab strip** (active tab marked by a blue top line, lock and kebab at right), then a **20 px toolbar** (Menu ▾, layer filter ▾, Button, light toggle, search "All", hidden-count "👁 0"), then a vertical split. Each pane has thin overlay-style scrollbars with arrow buttons.

**Panels base (2007:90158).** Variants {window, default, alternated_rows} × Show padding {On, Off}. **window base** offers the same three backgrounds.

**Modals (macOS 12).** These are OS frame (Dark/Light), Modal template, Popup template, Export Modal (**334×163**: "Import Unity Package", bold header, body, right-aligned Re-Import / Done) and Confirm Popup. The template shows **Destructive** left-aligned and **Secondary + Primary** right-aligned.

**Empty states.** "Idle window" shows an Empty State / Message; "Day 0 window" shows an Empty State / withButton. Both are built on Window+Tabs with a Timeline Toolbar.

**Editor 2022.3 Default layout (Templates page)** is the canonical dense layout:

- **Application Bar: 1791×30.** On the left are transform tools (hand, move, rotate, scale, rect, transform), Pivot/Local toggles and snap. In the centre are Play, Pause and Step. On the right are search, settings, cloud, Account ▾, Layers ▾ and Layout ▾. The background is `#191919`.
- **Hierarchy: 455×612.** Toolbar (+▾ create, search). The scene root row is **bold**, has a scene icon and a `*` dirty marker. Child rows are 16 px with cube icons and 15 px indent. The left gutter is darker.
- **Scene view** sits in the centre, with its own 20 px Scene toolbar of about 664 px.
- **Inspector: 400×500**, as described in §1.6.
- **Project: 600×291.** Two panes: Favorites plus the Assets folder tree on the left, an "Assets" breadcrumb and asset area on the right. The toolbar holds filter-by-type, filter-by-label, a favourites star and a hidden count "👁10". The selected folder row is filled `#2C5D87`.
- **Console.** Toolbar (Clear ▾ · Collapse · Error Pause · Editor ▾ · search · counters ⓘ0 ⚠2 ⛔1). Each entry is two lines (`[13:36:10] message` + stack line) with a 32 px severity icon. Selected rows are blue and other rows alternate.
- **Status bar** at the bottom shows the last error message in red.
- **Undocked window.** A floating macOS window (traffic lights) containing a Project-style two-column browser and a component-header pane.

**Localization Package v2.0 screens** (templates of a real data-table tool) are built from Panels base, a tab dock, "LocPack Toolbar" (Controls/Left + Controls/Right), "Current Table options", **column groups "Clmn: Key" + "Clmn: 1…6"** (header Label + settings "meta button" + Text Field cells), **"alt rows"** zebra striping, and a vertical Scroll View. A redline helper layer is named "🖍 padding (hide me)". This is the Editor's spreadsheet or table pattern, made of text-field cells with zebra rows.

### 1.8 Support page

- **Cursors (36 components).** These are arrow (busybutclickable, poof, notallowed, copy, contextualmenu), zoom (in, out), cross, cell, ibeam-horizontal, hand (pointing, closed), make-alias, screenshot (window), resize plus 16 directional variants (up, down, left-right, north-south, east-west, NW-SE, NE-SW…), move and help. The full cursor vocabulary for drag, split and resize interactions is spelled out.
- **macOS 12 chrome.** Menu, Menu item and Menu Separator (Dark and Light), Window frame and Dialog. The Editor does **not** restyle OS menus; it uses native menus. That justifies NEAR AI's native glass for menus on macOS while keeping the Editor-style density inside panels.

---

## 2. App UI v3.2 (Community)

### 2.1 Page map (75 pages)

| Group | Pages (id) |
|---|---|
| Cover | Cover (0:1). The hidden internal canvas 0:2 is not selectable |
| Foundations | Colors (11:2), Typography (11:3), Sizing & Spacing (11:4), Elevations (11:5), Icons (11:6) |
| Actions | Button 21:2, ActionButton 22:2, FAB 23:2, ActionGroup 23:163, ActionBar 23:220, Toolbar 23:236 |
| Selection | Checkbox 25:2, Radio 25:311, Toggle 25:386, Chip 25:439, Badge 25:500 |
| Text and labels | Text 26:2, Heading 26:234, Link 26:267, Quote 26:278, HelpText 26:286, FieldLabel 26:299, HelpBox 26:314 |
| Inputs | TextField 26:347, TextArea 26:382, NumericalField 26:402, InputLabel 26:417, Picker 27:2, Stepper 27:359, Menu 28:2, Dropdown 28:353, MentionPicker 28:396, ReactionPicker 28:410 |
| Colour and date | ColorSwatch 29:2, ColorField 29:368, DateField 29:393, DatePicker 30:2, ColorSlider 30:536, ColorWheel 31:2, ColorToolbar 31:10, ColorPicker 32:2 |
| Value and progress | Slider 33:2, TouchSlider 33:428, Progress 33:445, Preloader 33:457, PageIndicator 33:464 |
| Navigation | Tabs 34:2, Breadcrumbs 35:2, AppBar 35:14, BottomNavBar 36:2, NavigationRail 36:21, Drawer 36:444 |
| Overlays | Dialog 37:2, Toast 37:454, Tooltip 37:474, Popover 37:482, Tray 37:491 |
| Layout and collections | Accordion 38:2, Divider 38:24, Spacer 38:465, SplitView 38:486, DropZone 39:2, ListViewItem 39:19, TreeViewItem 40:2, GridView 40:21, SwipeView/PageView/StackView 41:2, Canvas 41:25 |
| People and misc | Avatar 42:2, AvatarGroup 42:25, Icon 43:2, CodeBlock 43:52, AssetTargetField 44:2, VectorFields 44:27, Thread 45:2 |

Every component page has the same structure: an auto-layout **"Stage"** frame with the title, **one description paragraph that is a full token-level spec** [verbatim, in `corpus/unity-figma/appui/component-pages-descriptions-*.txt`], and the component set (or several sets).

### 2.2 Variable architecture [verbatim + inferred]

The file states its architecture in its own doc text:

- **Global**: primitives. "Global palette — every swatch bound to a Global color Variable. Source: release/2.2.x global/palette.json." Global also holds font-size aliases ("Roles map to steps via Global font-sizes/heading/body aliases").
- **Theme**: semantic ramps with **4 modes: Dark / Light / Editor Dark / Editor Light** ("switch the Theme mode on this frame to preview…"). The *Editor* modes exist so App UI tools can match the Unity Editor chrome inside the Editor. This is the clearest precedent for NEAR AI giving one component library an "app" palette and a "host/IDE-native" palette.
- **Scale**: **2 modes, Medium / Small** ("switch Scale mode (Medium / Small)…"). Sizing, spacing and font sizes bind to it. The doc adds that "Sizing steps above 1350 diverge between modes by design (USS values)".
- **alias**: for example `alias/field`, `alias/menu`, `alias/text/primary`.
- **components**: per-component tokens, for example `components/checkbox`, `/toggle`, `/radio`, `/dialog`, `/accordion`, `/splitview`, `/actionbar/background-color`, `/avatar`.
- Other semantic groups referenced: `semantic/{positive, informative, warning, destructive}`, `actions/{selected, hover}` and `highlight/background-color`.

So the layering is **Global → Theme (4 modes) → alias → components**, with **Scale** cutting across all of them for density. This is the same layering the NEAR AI parent system needs: primitives, then semantic tokens by theme, then component tokens, with a density axis.

### 2.3 Colour

**Global palette** layer names: `color/black`, `color/white`, `color/{gray, blue, cyan, green, lime, yellow, orange, red-orange, red, pink, purple, indigo}/{100…1500}` (15 steps each), and `color/transparent/{black, white}/{0, 100…1000}` (alpha ramps).

**Theme ramps, as rendered in the frame's displayed mode (assumed Dark) [sampled ±2]:**

| Ramp | Steps | Values |
|---|---|---|
| primary | 15, 25, 50, 100…1300 (16) | `#000000`, `#0F0F0F`, `#151515`, `#1C1C1C`, `#242424`, `#2C2C2C`, `#353535`, `#3F3F3F`, `#4B4B4B`, `#5F5F5F`, `#757575`, `#A0A0A0`, `#B8B8B8`, `#CFCFCF`, `#E7E7E7`, `#FFFFFF` |
| base | 25, 50, 100, 200, 300, 400, 500 | ≈`#1C1C1C`, `#242424`, `#2C2C2C`, `#353535`, `#3F3F3F`, `#4B4B4B`, `#5F5F5F` |
| backgrounds | 50, 100, 200, 300 | `#151515`, `#1C1C1C`, `#242424`, `#2C2C2C` |
| foregrounds | 25, 50, 100, 200 | `#5F5F5F`, `#A0A0A0`, `#B8B8B8`, `#CFCFCF` |
| accent | 25…300 | `#0064B4`, `#0076D8`, `#0287FD`, `#1C98FC`, `#3AA4FC` |
| destructive | 25…300 | `#982A2D`, `#B72E36`, `#D6353B`, `#DB4C52`, `#DD6567` |
| warning | 25…300 | `#924A0F`, `#AF5612`, `#CD6413`, `#D37724`, `#D8893E` |
| positive | 25…300 | `#0B7243`, `#088949`, `#089E57`, `#24AB69`, `#40B781` |

The App UI Dark theme is darker and more neutral than the Editor theme: the panel base is `#1C1C1C`–`#242424` against the Editor's `#383838`. It uses 4 background levels and 4 foreground levels. Foregrounds are used semantically across components: fg25 for disabled, fg50 for secondary, fg100 for primary and fg200 for emphasis or hover.

### 2.4 Typography, sizing, spacing, radius, border, elevation

**Typography [verbatim].** "Inter (font-families/body & heading). Font sizes bound to Scale variables". There are two role ramps, `font-sizes/heading/{xxxl, xxl, xl, lg, md, sm, xs, xxs}` and `font-sizes/body/{xxxl…xxs}`, mapped onto raw steps `font-sizes/{25, 50, 75, 100, 200…1000}`. Heading L/XL/XXL tighten letter-spacing (−1/−2/−4). FieldLabel uses `font-sizes/100`, shortcut labels in menus use `body/xs`, and AppBar titles use `font-sizes/100` (compact) and `/900` (large).

**Sizing and spacing [sampled ±1 px, displayed Scale mode, likely Medium].** The Scale unit is **step 100 = 6 px**, linear up to 1200:

| Token step | 25 | 50 | 75 | 100 | 125 | 150 | 200 | 250 | 300 | 320 | 400 | 500 | 600 | 700 | 800 | 900 | 1000 | 1200 | 1400 | 1600 | 2000 | 2400 | 3200 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| sizing (px) | 1.5 | 3 | 4.5 | 6 | 7.5 | 9 | 12 | 15 | 18 | ~20 | 24 | 30 | 36 | 42 | 48 | 54 | 60 | 72 | 112 | 128 | 160 | 192 | 256 |
| spacing (px) | 1.5 | 3 | – | 6 | 7.5 | 9 | 12 | 15 | 18 | – | 24 | 30 | 36 | 42 | 48 | 54 | 60 | – | – | – | – | – | – |

Above 1350 the ramp switches to 8 px per 100 steps (1400 = 112). This matches the note that large steps diverge between modes. Components reference these steps directly, for example "FAB S/M/L = sizing 400/500/600", "Stepper S/M/L = sizing 400/500/600 square buttons", "ColorSwatch S/M/L = sizing 225/300/400", "Icon XXS–XL = sizing 200/250/300/350/400" (12 to 24 px icons in Medium), and "Tree depth indents at sizing 300/600/900" (18/36/54 px).

**Measured button heights [sampled]:** S ≈ 20–24, M ≈ 30, L ≈ 36 px. That is about sizing 500 and 600 for M and L. App UI's Medium is roughly 1.5× the Editor's density.

**Border radius:** `xs, sm, md, lg, xl, full`. Dialog and Tray use `border-radius/lg`. Controls use a "control radius" that renders at about 4 px [inferred]. FAB uses 1000 px.
**Border width:** `xs, sm, md, lg, none`. Divider thickness S/M/L is 1/2/3 px [verbatim].

**Elevations [verbatim]:** "Effect styles Elevation/0-24 from global/elevations.json, plus Shadow/sm-md-lg-focus-slider-handle from global boxShadow tokens". Elevation/{0, 1, 2, 3, 4, 6, 8, 12, 16, 24} and Shadow/{sm, md, lg, focus, slider-handle}. Menus use Elevation/8. Focus is a **shadow token** ("Shadow/focus") and is also a bound outline stroke on Button.

### 2.5 Component catalogue (spec text condensed from the file) [verbatim, condensed]

| Component | Variants and spec (from the page description) |
|---|---|
| Button | default · accent · destructive · quiet × default · hover · active · focus · disabled × S/M/L. All colours and metrics bound to Variables; focus is a bound outline stroke |
| ActionButton | icon + label; default · quiet × default · hover · active · focus · **selected** · disabled × S/M/L; selected = actions/selected background + accent foreground |
| FAB | circular, base/accent ramps; S/M/L = sizing 400/500/600; radius 1000 px |
| ActionGroup | default (gap md) · **compact (joined, shared borders, outer radius only)** · vertical · justified |
| ActionBar | selection bar: checkbox + count label + trailing ActionGroup; `components/actionbar/background-color` |
| Toolbar | horizontal/vertical; **floating** adds sizing/100 radius + backgrounds/300 border; **draggable** shows drag-bar |
| Checkbox | unchecked/checked/**intermediate** × default/hover/focus/**invalid**/disabled × **emphasized** (accent box) |
| Radio | off/on × default/hover/focus/invalid/disabled × emphasized |
| Toggle | off/on × default/hover/active/focus/invalid/disabled; on = positive/100 track + white knob |
| Chip | outlined (fg25 border) / filled (base/100) × default/hover/focus/disabled × deletable (× at 55% opacity) |
| Badge | default (count, min sizing/300) / dot (sizing/150); destructive/100 bg; label font-sizes/50 |
| Text / Heading / Link / Quote | body xxs–xxxl; heading fg50 default (primary fg100); link accent/100 → hover 200 → active 50; quote rule sizing/25 |
| HelpText | default fg50 · warning · destructive · disabled fg25 |
| FieldLabel / InputLabel | font-sizes/100 fg100; required indicator; **InputLabel horizontal puts the label at 33% width**, vertical stacks with gap-md |
| HelpBox | default · confirmation · information · warning · error (semantic tokens, icon tinted) |
| TextField / TextArea | S/M/L × default/hover/focus/invalid/disabled; alias/field colours; placeholder fg50, value fg100; TextArea has a resize grip |
| NumericalField | Int/Float/Double/Long; **drag-to-adjust with ew-resize cursor** |
| Picker (Dropdown/EnumField base) | S/M/L × default/emphasized × default/hover/open/focus/disabled; caret sizing/300 |
| Stepper | joined −/+ on base/100 with base/400 border |
| Menu / MenuItem / MenuSection | items padded gap-md; hover transparent-black/100; selected actions/selected; **shortcut label body/xs**; popover with alias/menu border + Elevation/8 |
| Dropdown | Picker trigger + Menu popover; checkmark on the selected item |
| MentionPicker / ReactionPicker | Menu-surface popovers (avatar + name rows; emoji grid) |
| ColorSwatch / ColorField / ColorSlider / ColorWheel + SVSquare / ColorToolbar / ColorPicker | Colour gradients are "color data, not theme tokens"; the chrome around them is token-bound |
| DateField / DatePicker | segmented date input; DatePicker is 290 px wide in Medium with DayPicker, MonthPicker and YearPicker |
| Slider / RangeSlider | track base/300 at sizing/50; progress accent/100; thumb sizing/300 |
| TouchSlider | field-chrome bar filled with base/200 progress (label plus value inside the field) |
| Progress | Linear sizing/125 bar; Circular sizing/650 ring |
| Preloader | full-surface scrim with a 100 px ring and a 50 px logo slot |
| PageIndicator | sizing/200 dots |
| Tabs / TabItem | labels fg50 → fg200 on hover → fg100 selected; indicator fg100 (emphasized = accent); horizontal and vertical demos |
| Breadcrumbs | items fg100, current fg200 |
| AppBar | backgrounds/100; compact and large title |
| BottomNavBar / NavigationRail / Drawer | rail sizing/800 (48 px) wide on backgrounds/200; drawer on base/50 with elevation |
| Dialog / AlertDialog | backgrounds/200, radius lg, spacing/400 padding, transparent-black/400 scrim |
| Toast | base/100 bar; informative/positive/negative/warning recolour the background; optional action |
| Tooltip | backgrounds/300, spacing/150 padding, control radius, **12 px tip** |
| Popover | backgrounds/200 (menu variant base/100 + alias/menu border); optional resize handle |
| Tray | bottom sheet with scrim and drag handle |
| Accordion | sizing/600 headers, backgrounds/300 bottom rules, header weight 700 |
| Divider | backgrounds/300; 1/2/3 px |
| SplitView / Splitter | **sizing/250 splitter**; anchor backgrounds/50; hover primary/400 |
| DropZone | dashed 3 px frame; idle fg25, accept accent (bg accent/25), reject destructive (bg destructive/25) |
| ListViewItem | spacing/100 row padding, sizing/150 radius, sizing/600 thumbnail; hover backgrounds/300; **loading = skeleton blocks** |
| TreeViewItem | gap-md padded headers, actions radius, hover actions/hover; depth indents sizing 300/600/900; caret |
| GridView / MasonryGridView | virtualized tiles, half-gutter padding, selected ring actions/selected |
| SwipeView / PageView / StackView | paged containers |
| Canvas | infinite pannable surface, backgrounds/50 with a base/100 dot grid |
| Avatar / AvatarGroup | S/M/L; circular, rounded or square; +N overflow |
| Icon | tint fg50 default, fg100 primary, fg25 disabled; XXS–XL = sizing 200–400 |
| CodeBlock | backgrounds/50 body + backgrounds/200 header with language label and copy button |
| AssetTargetField | field with asset icon, name (fg100) and type label (fg50); the App UI analogue of the Editor's Object Field |
| VectorFields | Vector2/3/4, Rect, Bounds; labelled NumericalFields separated by gap-sm |
| Thread | Thread header, ThreadMessage (avatar, author, timestamp fg25, content fg200, reactions), Attachment card (backgrounds/300, 180 px wide), ThreadComposer (radius-lg input) |

### 2.6 App UI icons (Icons page 11:6) [verbatim]

The page holds "1734 icons from release/2.2.x @unity/app-ui-symbols (appui set: regular · bold · fill). Fills bound to alias/text/primary. Named `<icon>--<variant>`". It also says "Almost all theses icons come from Phosphor Icons open-source project (MIT)". The grid frame has **1684 children**, all `*--regular` in the visible portion (for example `360--regular`, `acorn--regular`, `add-layer--regular`, `align-bottom-simple--regular`). Icon sizes in components are 12–24 px via sizing 200–400.

### 2.7 "App UI v3.2" compared with the App UI 3.0 docs

- From the file alone I can only establish that **"v3.2" is the Figma kit's own version label**. Every component description cites **"UITK X (release/2.2.x)"**, and the palette cites `release/2.2.x global/palette.json` and `@unity/app-ui-symbols`. The kit version therefore does not match the package version it documents, which is a 2.2.x release line. Mapping to the App UI 3.0 docs has to be done against the docs themselves (the `unity-web` stream).
- Components in this kit that are likely candidates for newer-than-docs additions or differences, and should be checked against App UI 3.0 docs: Thread family, MentionPicker, ReactionPicker, CodeBlock, Canvas, StackView/PageView, AssetTargetField, DropZone, Preloader, ColorToolbar, TouchSlider.
- The kit adds **Editor Dark / Editor Light theme modes**, so App UI controls can sit inside Editor windows. Any runtime-only docs would describe only Dark and Light.

---

## 3. Unity Editor Icon Library

| Aspect | Finding |
|---|---|
| Pages | ". Cover" (2002:728), "❖ Icon Library (.png)" (30:4632) |
| Read me [paraphrased] | Unity icons are implemented at **1x and 2x (16×16 and 32×32)**. The icons here are 2x PNGs that Figma imports at 16×16; they can be resized to 32×32 for mockups without loss. Do not use larger (blurring). **Layers are named for folder structure on export.** Dark and Light theme icons are included with their **Selected States**. Links to "Editor Foundations / Iconography" |
| Frame | "External Creators Icon Library" (30:4633), 293 children: 8 category labels plus **283 image layers** |
| Canvas size | **16×16** per icon [exact, badge] |
| Naming | `<Theme>/<Category>/[Selected State/]<name>[ On]`. **Dark files are prefixed `d_`** (Unity `EditorGUIUtility` convention) and **selected-state files end with " On"**. Export names carry `@2x` (one stray layer `Icon Name=Warning, Theme=Light Theme, File Name=Warning@2x 2` shows the export naming scheme) |
| Counts | Light 73 + 68 selected, Dark 74 + 68 selected. 143 layers with `d_`, 136 with " On" |
| Board | Each category has 4 rows: Light Theme / Light Theme – Selected / Dark Theme / Dark Theme – Selected, on a periwinkle board (≈`#7A7FB0`) chosen to show both themes |
| Style [inferred] | Pixel-hinted 16 px monochrome glyphs, mostly solid with about 1 px strokes. Mid-grey in Light, light grey (≈`#C4C4C4`, matching `Pro/Icon/figma-icon-color`) in Dark, white for selected states (because selection rows are blue). Colour appears only in status icons (info white bubble, warning yellow triangle, error red octagon, True green check, False red ×, Pending orange) and the Color/ColorPicker image controls |

| Category | Layers | Base icons |
|---|---|---|
| Navigational Chevrons | 16 | Chevron, ChevronRight, ChevronLeft, ChevronUp, ChevronDown |
| Foldout Carets | 16 | CaretLeft, CaretRight, CaretDown, CaretUp |
| Panel Options | 56 | Settings, Locked, Unlocked, Visibility, VisibilityTool, VisibilityHidden, Link, Unlink, Fullscreen, JumpSearch, Help, Documentation, MenuOptions, Menu, Preset |
| Controls | 24 | Search, Close, Checkmark, Remove, Add, AddMore |
| Media Controls | 32 | Camera, Play, Pause, OneFrameForward, OneFrameBack, GoToCurrentFrame, Sound, SoundOff |
| Image Controls ("Image Contols" sic) | 48 | Greyscale, Color, ColorPicker, RotateTool, Lighting, LightingOff, RotateClockwise, RotateAntiClockwise, PreviewAwake, PreviewAsleep, FlipVertical, FlipHorizontal, Drag |
| File Management | 60 | Create, Edit, Copy, Paste, Remove, Save, Open, Folder, FolderOpen, FolderEmpty, Favorites, Image, UndoHistory, Server, NotOnServer |
| Messaging / Alerts | 31 | Log, Warning, Error, LogDimmed, WarningDimmed, ErrorDimmed, True, False, Pending, Loading |

Key lessons: icons are **raster, theme-specific and state-specific assets**: 4 files per glyph (light, light-on, dark `d_`, dark `d_… On`) × 2 resolutions. The "On" (selected) variant exists because selection rows invert the icon to white. "Dimmed" variants of Log, Warning and Error carry the console's filter-off state. App UI instead uses **vector Phosphor symbols tinted by tokens**, three weights, with no theme-specific files. For NEAR AI the App UI approach is better (one vector set tinted by tokens), but the Editor's *state* coverage (on-selection inversion, dimmed or filter-off) should be kept as tint tokens: `icon/on-selection`, `icon/dimmed`.

---

## 4. Cross-file comparison: Editor (UITK/EFDS) vs App UI

| Dimension | Unity Editor kit (EFDS, LTS 2022.3) | App UI v3.2 kit |
|---|---|---|
| Theming mechanism | Colour **styles** with `Dark/` and `Light/` prefixes; twin component sets per theme | **Variables** with Theme modes Dark/Light/Editor Dark/Editor Light |
| Density | Fixed. Fields 18, buttons 18/20/24, rows 16, toolbars and tabs 20, app bar 30 | Scale modes Medium/Small; Medium ≈ 30 px controls, sizing unit 6 px |
| Token naming | USS variables `--unity-colors-<component>-<property>-<state>` | Tiered: `color/blue/800` → `accent/100` → `alias/field/...` → `components/checkbox/...` |
| Surfaces (dark) | Window `#383838`, recessed `#282828`, fields `#2A2A2A`, buttons `#585858` | backgrounds 50–300: `#151515`–`#2C2C2C`; base 25–500 |
| Selection | `#2C5D87` focused / `#4D4D4D` unfocused | actions/selected background + accent foreground |
| Focus | Blue field border `#3A79BB`, button accent `#7BAEFA`, focused label turns blue | Bound outline stroke plus Shadow/focus |
| Elevation | None in panels (borders only); OS-native menus and windows | Elevation/0–24 + Shadow/sm, md, lg |
| Radius | Small (about 2–3 px controls) [inferred] | xs…full; control radius about 4 px; dialogs lg |
| Icons | 16 px PNG, d_ and On variants, 1x/2x | 1734 Phosphor-derived vectors, regular/bold/fill, token-tinted |
| Text | Inter, 6 sizes 9–19 px, default 12 (11.5 in Figma) | Inter; heading and body role ramps over Scale steps |

---

## 5. Implications for the NEAR AI parent system (dense desktop mode)

1. **Run two density axes.** Set a **"compact / editor" density whose baseline matches Unity's**: 18 px value fields, 20 px buttons, toolbars and tabs, 16 px tree and list rows, 20 px property-row pitch (18 + 2), 15 px indent per level, 30 px app bar, a 60 px object header and a 22 px section header. Map App UI's Medium (about 30 px controls) to a "comfortable" density, and keep both on a Scale collection the way App UI does.
2. **Use a token grammar** that can express Unity's breadth: `component-part-property-state`, such as `button-border_accent-focus` or `toolbar_button-background-checked`. Layer it the App UI way: primitives → semantic theme (modes) → alias → component. Give the theme collection at least **Dark / Light / Host-Dark / Host-Light** modes, mirroring App UI's Editor Dark and Editor Light. NEAR AI can then render inside other host chrome (for example VS Code- or Xcode-like panes) and still use its glass look in native shells.
3. **Show elevation by luminance in dense mode, without shadows.** Value wells sit darker than the surface and commands sit lighter. Use 1 px borders with a darker accent edge as the bevel. Keep glass and blur for shells, sidebars and floating overlays, not for every control.
4. **Keep window focus out of selection colour.** Selection is accent when the window is focused and neutral grey when it is not. Add `selection/active` and `selection/inactive`, plus a translucent **hover overlay** (6% white on dark, 6% black on light) so hover works on any row or zebra background.
5. **Give focus three cues**: a field-border focus colour, a button focus accent ring, and **the focused field's label recolouring** (Unity's `label-text-focus`). The last one matters in label-plus-field grids where the eye scans labels.
6. **Adopt the property-row system:** a label column of about 120 px (or App UI's 33% rule for horizontal InputLabel), a fill or fixed control column, 2- and 3-column variants (label | sub-label | control, or label | control | control), enable/disable rows with a leading checkbox, slider+number composites, inline X/Y/Z vector fields, and foldout groups with 15 px indentation.
7. **Use the full state set:** Default, Hover, Focused, Focus+Hover, Pressed, Pressed+Focus, Checked, Selected, Selected+Unfocused, Accepted (drop target), Invalid, Indeterminate, Disabled, Loading (skeleton). These are the states dense tools actually need (Unity has Accepted; App UI has invalid, intermediate and skeleton).
8. **Specify segmented groups explicitly** with L/M/R pieces where only the outer corners are rounded and borders are shared. Unity builds every button group (basic, toggle, app-toolbar, AppCommand) this way, and App UI ActionGroup "compact" does the same.
9. **Draw toolbar separators as a hairline effect** (inner 1 px) rather than separate divider nodes, to keep 20 px toolbars crisp. Use a 16 px search field inside 20 px toolbars.
10. **Specify docking chrome**: a 20 px tab strip whose active tab carries an accent top line; tab text and background states (inactive `#353535`, hover `#303030`, checked `#3C3C3C`); a lock and kebab at the right of each dock; an optional toolbar row; a split view with a thin splitter (App UI uses sizing/250 ≈ 15 px hit area) and hover highlight.
11. **Window and panel templates should be variant-driven**: background (window, default, zebra) × tab on/off × toolbar on/off × panes 1–3. Unity's 54-variant Default window shows that a small set of layout properties covers most tool windows.
12. **Use a hard-capped type scale of 6 sizes for desktop dense mode** (9, 10, 11, 12, 14, 19 in Unity), with bold used only for emphasis inside the default size. Calibrate to the renderer: Unity compensates Inter in Figma by using 11.5 px for its 12 px default. NEAR AI should calibrate SF Pro and Inter per platform the same way.
13. **Icons should be 16 px on a pixel grid in dense mode**, with explicit tint states for on-selection (white), dimmed or filter-off, and semantic status colours. Ship them as one vector family with weights (App UI's Phosphor regular/bold/fill) rather than per-theme rasters.
14. **Keep status colour sparse and semantic**: info, warning, error, positive. Console-style counters with icons (ⓘ 0 ⚠ 2 ⛔ 1) and two-line log rows with 32 px severity glyphs are a good pattern for agent and log output in NEAR AI.
15. **Use OS-native menus and dialogs on desktop.** Unity does not restyle macOS menus, window frames or dialogs; it ships them as reference chrome. Its dialog template places a destructive action on the left and secondary + primary on the right.
16. **Plan a data-table pattern** from the Localization screens: a key column, N value columns of text-field cells, per-column header with a settings button, zebra rows and a 20 px toolbar above.
17. **Specify cursors.** Dense tools need resize-in-8-directions, ew-resize drag-to-scrub on numeric fields (App UI NumericalField), copy and alias for drag, and notallowed.

---

## 6. Gaps and how to close them

- **Not captured:** exact paddings, gaps and corner radii inside UITK components (the selection badge gives only width and height; anatomy paddings need Inspect). The App UI Theme values for the Light, Editor Dark and Editor Light modes (only the displayed mode was sampled). App UI's Small Scale values and its exact font-size px per step. Text-style line heights in App UI. Effect values for App UI elevations.
- **Ways to finish:** (a) Use the Figma MCP from an account or plan without the call cap; if the files are viewed from a team context with a full seat, `get_design_context` and `get_variable_defs` on the node ids in `corpus/unity-figma/uitk/variant-node-ids.txt` would return exact padding, radius and variable bindings. (b) Enable the Dev Mode MCP server in Figma desktop. That is a user preference change, so I did not do it. (c) Sign in to the web viewer so the properties panel is available. Duplicating the community files to drafts would give full Dev Mode access, but it creates a file and so was out of scope for this read-only stream.
- All node ids needed for those follow-ups are recorded in the corpus.
