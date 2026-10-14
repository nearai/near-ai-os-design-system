# trace-commons design language: exhaustive inventory (research stream for the NEAR AI parent design system)

Prepared 2026-10-13 from the trace-commons repository (github.com/TraceCommons/trace-commons) at `main` (`6ed1e8c46`, "Prepare v0.15.0 release", 8 commits behind `origin/main`), plus read-only `git show` of `origin/macos-glass-spec`, `origin/ftux` and the `pr1146` branch (the Tauri design system, which is not on `main`). Nothing in the repo was edited or built. File references are `path:line` relative to the repo root; `GS` = `origin/macos-glass-spec:docs/superpowers/specs/2026-09-30-macos-glass-design.md` (not on main), `GP` = `docs/superpowers/plans/2026-10-02-macos-glass-rebuild-and-r15-cutover.md`, `TOK` = `design-tokens/glass.tokens.json`, `CG` = `docs/ui-copy-guide.md`, `FG` = `docs/design/flat-glass-theme/index.html`.

## 0. Reading guide

- Section 1: what the language is, who decides, and every named decision with dates.
- Section 2: every token (colour, gradient, edge, radius, spacing, size, opacity, blur, stroke, motion, elevation, type, chart).
- Section 3: themes (classic vs flat; light/dark; Increase Contrast; Reduce Transparency; Reduce Motion; pre-macOS 26).
- Section 4: every TCDesign component with API, anatomy, states, tokens and accessibility.
- Section 5: every screen and the reusable patterns, with the drift found in the views.
- Section 6: content and voice rules.
- Section 7: accessibility rules and the tests that enforce them.
- Section 8: Tauri (web), Windows and GTK translations and how they diverge; the mark system.
- Section 9: gaps for a multi-platform parent system, internal inconsistencies, and decisions the owner must make.

## 1. Design language summary and named decisions

### 1.1 What the language is

The trace-commons macOS app (product name now **"Near.ai"**; "Trace Commons" is the commons/account/server name, renamed in v0.13.0, `docs/announcements/2026-10-11-v0-13-0.md:3`, `crates/.../brand.rs:23-48`) is a SwiftUI app drawn entirely with a custom design system, **TCDesign** (`macos/Sources/TCDesign`, about 10,200 lines), over a typed token file (`TOK`) and a generator. Its visual source was Ron's Tauri PR **#1146** "Adopt the WYSIWYG UX and Glass design system" (frozen as the reference); its behaviour comes from the pre-glass shipping app. The language in one paragraph:

> Floating, translucent **panes** of native glass (Liquid Glass on macOS 26, the HUD vibrancy material on 14-25) sit directly on the desktop with 10pt gaps and no window chrome; everything inside a pane is **painted** (cards tint the pane, wells recess, controls sit on top: "never glass on glass"); only floating things (menus, popovers, node cards, controls over the map) get their own blur. One **purple** (#6d14f3) is "the one action"; status is always **a dot plus words**, never a fill; type is **SF Pro / SF Mono mapped to macOS text styles** so it follows the system text size; there is **one motion curve** (cubic-bezier 0.2, 0.8, 0.2, 1) at 150/220ms, and none under Reduce Motion; contrast floors are **WCAG 4.5:1 text / 3:1 UI** and are enforced by tests; every word comes from the **Rust core** and components author none; and the UI **fails closed** (an unknown is a dash or the core's "unknown", never zero, never "on").

Two themes exist: **classic glass** (gradient sheens, specular top highlights and bottom shades, thin dark veil) and **flat glass** (flat fills, no rims, heavier navy/grey veil, larger radii, purple selection in dark and **blue** in light). **Flat is the default on `main`** (`macos/Sources/TCDesign/Tokens/GlassTheme.swift:29-36`); classic is what the tests measure.

Surfaces: the three-pane **Monitor** window (Home / Inference / Traces tabs, a flow map, an inspector), a **menu-bar glass panel**, an OS-level **edge rail**, a **first-run** window, a **Settings** window, and many modals/sheets (section 5).

### 1.2 Who decides (and the precedence rule)

- **Ron** (rdisandro): visual design owner. **Zaki**: product owner ("owner" in most rulings). **Kristi** (poldsam): reviewer and core-copy lane.
- **Precedence (Zaki, 2026-10-02, narrowed 2026-10-05)**: "Ron's code and his decisions on #1173 bind the visual and component choices: materials, components, geometry and tokens and their values. Where this spec and Ron's code disagree on one of those, the spec is wrong and follows the code." The spec binds consent copy and notices, behaviour kept from `main`, accessibility duties and the contrast floors (GS:10-26).
- Consequence for a parent system: many of the newest rulings (2026-10-06 to 10-12) exist only in code comments, token `note` fields and squash-commit messages, not in a spec. The macOS glass spec itself lives on an unmerged branch.

### 1.3 Named decisions and rulings

Four ID namespaces exist and collide: **#1173 roadmap D/R items** (D1-D13, R1-R15), the **R15 plan's D-1..D-21**, the **glass spec's numbered Decisions 1-15**, and an **Insights owner-decision namespace D1-D8** (InsightsOverviewTab etc.). A parent system should not reuse these IDs.

**#1173 roadmap (native macOS glass) D/R decisions**

| ID | Date | Decision | Reference |
|---|---|---|---|
| D1 | 2026-09-28 | Native SwiftUI is the main macOS client; no new Tauri work on macOS | `CLAUDE.md:19-24`, `AGENTS.md:8-13`, GS:44-47 |
| (unnumbered) | 2026-10-02 | Native macOS is the lead client and the parity target; GTK, Windows and Tauri match its terminology, states, flows and affordances | `CLAUDE.md:21-24`, GP Global Constraints |
| D2 | 2026-10-02, then "revised" | Appearance: first dark only; tokens now follow the system appearance; where D2 was revised is still open | TOK:2; GS:352-360; GP D-2 |
| D3 | #1173 | Brand purple #6d14f3 replaces community green #178f70; whether the community site follows is open | GS:361-363; `TraceCommonsAppMain.swift:182-189` |
| D4 | 2026-09-30 | Minimum macOS 14, glass on every supported macOS; Liquid Glass on 26, system material on 14-25 | GS:364-371 |
| D6 | #1146 review | Pending credit appears only beside the commons' statement of its condition, else a dash | `Views/Monitor/HomeViews.swift:13,145,222` |
| D8 | 2026-10-02 -> revised 2026-10-05 -> **reversed 2026-10-08** | Settings: a separate window; then an opaque in-window modal over the Monitor (Zaki); then "in a window of its own beside the Monitor (owner, 2026-10-08), no longer a modal over it" (current code) | GS:372-384; `TraceCommonsAppMain.swift:128-141` |
| D9 | #1173 | Custom three-pane window, not `NavigationSplitView`; map and inspector hide independently; the main pane never hides | GS:391-393; `ThreePane.swift:202-214` |
| D10 | #1173 | A session's pill is Review: selects it and opens the inspector | GS "Behaviour changes" |
| D11 | #1173 | The map's second mode is labelled "Private AI", from core copy | GS:394 |
| D13 | default | Windows and Linux stay on frozen Tauri until macOS ships | `CLAUDE.md:21`; GS:165 |
| R1 | #1178 | Token source is typed JSON + generator (+ GTK/WinUI roles since #1228) | GS:385-388 |
| R2 | #1179 | SF Pro and SF Mono; every type step a macOS text style; no bundled fonts | TOK:2; `TokenDriftTests.swift:162` |
| R3 | #1180 | Materials: native backdrop on both OS paths; `paneOpaque` under Reduce Transparency; no own pane edge on 26 (the last part later reversed, see 2026-10-07) | `GlassStyle.swift:191-194`; `GlassMaterialTests.swift:7` |
| R4 | #1181 | One `glassSurface` call site; Liquid Glass belongs to the floating layer only; custom menus, popovers, toggles | `GlassStyle.swift:281`; `FloatingLayerTests.swift:6` |
| R5 | #1182 | Window shell (three panes, toolbar, tabs, restoration); Monitor is the main window since R15 | `TraceCommonsAppMain.swift:95` |
| R6-R12 | | Screens: R6 Traces, R7 badge/health, R8 map + Inference, R9 Home, R10 Missions, R11 Settings, R12 first run | `MonitorWindowView.swift:99-101,600`; `HomeStore.swift:24` |
| R13 | | Menu-bar glass panel (`MenuBarExtra(.window)`) | `MenuBarPanel.swift:3-5` |
| R14 | | Accessibility pass: Increase Contrast, focus, VoiceOver grouping; Reduce Transparency left to the system | `GlassBackdrop.swift:14-20,150-151`; TOK:342 |
| R15 | | Cutover: glass Monitor and menu-bar panel are the release default; legacy shell deleted (`DesignSystem.swift` is gone on main) | GP Phase 4 |

**Glass spec "Decisions" list (GS:347-411)**: 1 appearance follows the system (where decided: open); 2 purple brand (D3); 3 macOS 14 floor (D4); 4 Settings modal (D8 revised, since reversed); 5 JSON token source; 6 SF Pro/SF Mono; 7 three-pane layout (D9); 8 map label "Private AI" (D11); 9 Ron's custom-painted `GlassMenu`, `GlassPopover`, `GlassToggleStyle` with explicit accessibility duties; 10 **eyebrow weight 600** (conflicts with TOK:317 `bold`, set in #1273 `5835e8d1a`, 2026-10-07); 11 Reduce Transparency base `paneOpaque` #1c1e24; 12 precedence narrowed; 13 a permanent **Watching/Paused readout with pause/resume on every tab** ("paused is a state a person can forget they chose"); 14 folder Submit all and Submit all as kept (Submit all as is a modal); 15 view menu, graph toggle and chart footer are open with Ron (all three are now built).

**R15 plan owner decisions D-1..D-21 (GP:39-68)**: D-1 host legacy views in glass frames (done; legacy palette deleted); D-2 follow the system appearance, test both; D-3 Folders before Join on a fresh install (daemon needs roots); D-4 always-on data use locked and included (later: unticked-required 2026-09-28, then checked-and-disabled 2026-10-08, `30efd68af`); D-5/D-6 Sharing/Private AI in onboarding (later built via the first-run port); D-7 Skills in the History inspector (**settled 2026-10-06**, Ron); D-8 Compute = four glass buttons + a field (**settled 2026-10-06**); D-9 Missions ships fail-closed; D-10 menu-panel overrides ship disabled; D-11 services start when the Monitor opens (Insights-only launch lost; open); D-12 pause-duration words are core-owned (**done 2026-10-06**); D-13 live-client switch; D-14 an invite link while onboarded opens the Monitor; D-15 public profile as a `GlassCard` with an accent `GlassTag` (replacing the "black frame is the boundary of what becomes public" seam); D-16 Welcome hero = `display` type, no globe; D-17 stock Settings chrome (superseded); D-18 dev hooks debug-only; D-19 unknown status reads "Status unavailable", terminal, no Withdraw; **D-20 (owner ruling 2026-10-08) every button in a window/sheet/modal action bar is the primary CTA's size; only inline buttons use the smaller size** (TOK:4; `Controls.swift:22-40`); **D-21 (owner ruling 2026-10-08) text about taking the primary action sits directly above the action bar, plain secondary text, full width, left-aligned** (`ActionBar.swift:3-12`).

**Dated owner/designer rulings (chronological; from code comments, token notes, commits and docs)**

| Date | Ruling | Reference |
|---|---|---|
| 2026-08-08 | Notification actions are exactly Review and Not now; no action may upload | `docs/superpowers/specs/2026-08-08-contributor-shell-shared-design.md:38-48` |
| 2026-08-17 | "The Turn" (two brackets) adopted as the client mark (pre-glass; superseded by the Trace mark) | `.../2026-08-17-desktop-clients-design.md:20-45` |
| 2026-08-19 | Reversed `LSUIElement`: the macOS app has a Dock icon and a menu-bar item (notch-hidden status items make a menu-bar-only app unfindable) | `.../2026-08-19-macos-shell-shape-design.md:35-61` |
| 2026-08-19/20 | Icon pipeline: one geometry source, live drawing in UI, generated assets for packaging; mark palette teal #00d4aa + ink (pre-purple) | `.../2026-08-19-icon-pipeline-design.md:76-274` |
| 2026-10-02 | One name per folder mode on every surface: **Ask me / Automatic / Never** | `5dd0d17ba` (#1231); GP Global Constraints |
| 2026-10-02 | #1174: labelled projected credit allowed, never styled as earned (conflicts with the earlier no-gamification rule) | `.../2026-09-23-connect-and-forget-consent-design.md:965-984` |
| 2026-10-05 | Traces tree has no tool level; one approve control (the inspector card); Look inside is read-only; health banners always visible | `docs/superpowers/plans/2026-10-05-1241-ron-1146-inspector.md:15-30` |
| 2026-10-07 | **"Hold the WCAG floors"**: placeholder 30% -> 46%, `selection` #3a7bd5 -> #3275d3, `toolbarGlyphHidden` #7c7c86 -> #83838c, switch knob ring, off-row text by ink | TOK:24,55,62,85; `ListRow.swift:98-122`; `0e5dffe6b` |
| 2026-10-07 | **Hover states from #1146**: a hover fill replaces the tier fill | TOK:50; `GlassStyle.swift:222-226` |
| 2026-10-07 | **#1146 wins for components and theming**; pane gradient, veil and edge from #1146 on macOS 26 too; floating surfaces = #1146 fill + edge over a within-window blur on every macOS | `Glyphs.swift:3-7`; `GlassBackdrop.swift:134-141`; `GlassStyle.swift:307-325` |
| 2026-10-08 | Button size (D-20), action notes (D-21), button-label rule ("a verb, or a verb and an object") | TOK:4; CG:3-7 |
| 2026-10-08 | Every switch is purple (the watch switch dropped green); knob plain white with no ring | `Controls.swift:747-762` |
| 2026-10-08 | Settings in its own window | `TraceCommonsAppMain.swift:128-130` |
| 2026-10-08 | Main pane 400 + 40 = 440; inspector two thirds of it; no title-bar separator | `ThreePane.swift:35-41`; `GlassBackdrop.swift:242-245` |
| 2026-10-08 | Breadcrumb back is a bare chevron; `GlassInfoButton` for longer row text | `Navigation.swift:308-310`; `InfoButton.swift:3-5` |
| 2026-10-09 | Flat glass theme (from getone.one) explored and made default; Settings > General > Appearance (Light/Dark/System); frosted, not clear, glass; failures as unboxed red lines (Ron) | `897ac406e` (#1318); `GlassBackdrop.swift:59-62`; `StatCard.swift:43-46` |
| 2026-10-10 | **Ember Rule** main tabs (1.4x); flat dark cards are pane-navy, darker than the pane; rims dropped; icon-card head layout; tapered dot-matrix bar graph; map marks; chevrons on link cards; flat chips lose outlines; "owner chose Ron's design over the contrast fixes" for graph dots, flat secondary/status text, off-chip ink and the light tab ember (several contrast commits reverted) | TOK:65,342; `Containers.swift:114-121`; `Indicators.swift:442-446,512-518`; `9b86f414d` (#1342) |
| 2026-10-11 | Promotion card treatments (default `spotlight`); `GlassIconMenu`; folder tile glyph; radio row; menu-strip tint capsule; badge smaller with no edge; **focus ring not drawn** | `GlassPromo.swift:3-42`; `Controls.swift:583`; `MenuBarPanel.swift:405-412`; `TraceCommonsAppMain.swift:88-191` |
| 2026-10-12 | Flat Light = cool grey #e3e6ec veil at 66% with a **blue accent** (#1f7aa8 / #15608a) because "purple read muddy on grey"; flat dark veil 68%; frosted `regularTint` panes; `inactiveDim` on background windows; Trace mark live-trace icon; edge-rail icon in solid ink | TOK:48,342; `GlassTheme.swift:49-58`; `GlassTraceMark.swift:12-13`; `40b943119` (#1381); `docs/announcements/2026-10-12-v0-14-0.md:17-18` |

### 1.4 The principles, stated once

1. **One accent, one action**: #6d14f3 is the CTA and selection fill; `purpleText` is text only; every accent fill uses #6d14f3 or its gradients (GS "Accent contrast floor").
2. **Status is a dot plus words**, never a fill, never colour alone; status colours are for glyphs and labels.
3. **Panes are the containment; never glass on glass**; cards are painted tints; only floating layers blur; the map is content (classic).
4. **Containers get edges (specular inset highlight/shade + drop shadow), never solid borders**; hairlines only between rows inside a list.
5. **Type follows the system text size**; fixed sizes only for glyphs in fixed controls; controls use minimum heights.
6. **One motion curve**; nothing moves under Reduce Motion.
7. **Pressed is 8% darker, never a fade; hover replaces the fill; disabled is 0.45**.
8. **WCAG floors hold** (4.5 / 3) on every ground, measured, never lowered.
9. **The core owns every word**; components author none; fail closed.
10. **Screens never branch on the OS**; only the TCDesign tier code does.
11. **The safe action is the default**: Return is bound to Undo, never to Contribute; destructive actions are never the default; irreversible sends are "prominent" but have no Return key.
12. **Look from #1146, behaviour from `main`**.

## 2. Token inventory

All paths below are relative to the root of the trace-commons repository (branch `main`, HEAD `6ed1e8c46`, 8 commits behind `origin/main`). `glass.tokens.json:N` means `design-tokens/glass.tokens.json` line N.

### 2.0 Token architecture (how the values are stored, typed and emitted)

- **One source.** `design-tokens/glass.tokens.json` (554 lines, `version: 1`) is "the one source for the native macOS app (and, later, any other shell)" (`glass.tokens.json:2`). It was seeded from #1146's Tauri CSS tokens at `09a26c0d` and has since diverged (see section 8).
- **Groups and counts.** 103 colours (92 with a distinct light value), 7 gradients, 16 shadow/edge stacks, 9 radii, 27 spacing values, 52 sizes, 6 opacities, 11 type steps, 11 motion values, plus a `themes` block (`flatLight`: 27 colour, 5 gradient, 15 shadow, 5 radius overrides; `flatDark`: 39 colour, 5 gradient, 15 shadow, 5 radius overrides).
- **Typed composites.** CSS composites are typed groups because Swift cannot parse CSS strings: a colour is `hex` + optional `alpha` + optional `light {hex, alpha}` + `note`; a gradient is a CSS `angle` (180 = top to bottom, 160 = light leaning to the top-left, "the way the panes are lit", `GlassTokenTypes.swift:124-144`) and `stops`; a shadow is a list of layers `x, y, blur, hex, alpha, inset` where an inset layer is a specular highlight or shade and an outer layer is a drop shadow (`GlassTokenTypes.swift:156-172`).
- **Generator.** `scripts/design-tokens/generate.py` writes three outputs (`generate.py:7-14`): `macos/Sources/TCDesign/Generated/GlassTokens.swift` (every token, 620 lines), `crates/trace-commons-contributor-gtk/src/ui/brand_tokens.rs` and `windows/src/TraceCommons.App/Themes/BrandTokens.xaml` (only the 11 `SHELL_ROLES`, `generate.py:52-64`). It validates: lowerCamel identifiers (`:89-99`), `#rrggbb` only (`:102-105`), alpha in 0...1 (`:115-119`), every type step's `size` equals its macOS text style's default size (`:73-88`, `:326-327`), shell roles must be opaque (`:355-356`), and `onAccent` on `accent` must reach 4.5:1 in both schemes or generation fails (`:66-69`, `:387-392`). `--check` exits non-zero on drift (`:532-536`); `TokenDriftTests` also decodes the JSON and compares every value with the Swift constants.
- **Theme overrides.** A theme may override only `color`, `gradient`, `shadow`, `radius` (`generate.py:167-168`). `flatLight`/`flatDark` must override the same gradients/shadows/radii with the same stops and layer structure, and a radius must be equal in both appearances (`generate.py:171-196`). A themed token is emitted as a computed `static var` that calls `GlassTheme.pick(classic, flat:)` (`generate.py:265-272`; e.g. `GlassTokens.swift:22`).
- **Runtime colour type.** `GlassRGBA` stores the dark value plus an optional light value and resolves through a dynamic `NSColor` per appearance (`GlassTokenTypes.swift:7-60`); high-contrast appearances are detected with `NSAppearance.bestMatch` (`:64-70`, `:97-110`). `adaptive(highContrast:)` swaps to a partner token when Increase Contrast is on, resolved by the system with no environment read (`:76-92`).
- **Shell roles shared with GTK and WinUI** (`generate.py:52-64`): `accent` (light `purple` #6d14f3 / dark `purpleSoft` #8a3dff), `accentLine` (`purple` / `purpleText` #c9b3ff, because `purpleSoft` "sits under 3:1 on the shells' lighter dark grounds", `:46-50`), `accentText` (`purpleText`), `onAccent`, `statusOn`, `statusOnText`, `statusAsk`, `statusAskText`, `statusOutside`, `statusOutsideText`, `onStatus`. Windows additionally maps legacy keys (`TcGreenBrandBrush` and so on, named before the purple) onto these roles, with alpha bytes for borders (`generate.py:442-456`), and aliases every role to system brushes under High Contrast (`:457-460`, `:500-508`).
- **The window tier has no tokens on macOS.** #1146's `--tc-blur-window`, `--tc-blur-popover`, `--tc-blur-scrim`, `--tc-rim-window`, `--tc-rim-width`, `--tc-shadow-window` and the three `--tc-scene-glow` colours are deliberately absent: "On macOS the native material does that work ... A shell with no native material would need them back" (`glass.tokens.json:5`). This is the single biggest gap for a web/Android/Windows parent system (section 9).

### 2.1 Colour

Grouping (by role): **brand** `purple`, `purpleSoft`, `purpleText`, `blue`, `promoTintEnd`; **logo live trace** `traceLiveStart/Mid/End`; **text** `textPrimary/Secondary/Tertiary`, `placeholder`, `textOn{Accent,Status,Selected}`; **Increase Contrast partners** `textSecondaryHighContrast`, `textTertiaryHighContrast`, `hairlineHighContrast`, `edgeHighContrast`; **status (glyph/dot)** `statusOn/Ask/Off/Outside` and **status as text** `status{On,Ask,Outside}Text`, `destructiveText`, `badgeFill`; **data series** `dataShared/Kept/Inference`; **grounds** `sceneBase/Warm`, `paneBase`, `paneOpaque`, `glassVeil`, `inactiveDim`, `wellFill`, `fieldFill`, `consentFill`; **interaction states** `controlHover`, `cardHover`, `rowHover`, `controlSelected(Floating)`, `selection`, `toolbarExpanded`, `toolbarGlyph(Hidden)`; **switches** `toggleOn/Off`, `toggleOnSettings`, `watchOn`, `switchKnobEdge`; **lines** `hairline`, `rule`, `tabEmber(Halo)`, `menuSeparator`; **floating fills** `popoverFill`, `menuFill`, `nodeCardFill`, `scrim`, `modalScrim`, `menuHover(Text)`, `menuSelection`; **menu bar** `menuMode{Ask,Armed,Never}`, `menuPillOff`, `menuBarsPaused`, `menuStripTint`, `menuChip{Shared,Kept}`, `menuNoProof`; **map/charts** `map*`, `graphFocus*`; **tints** `tint{On,Ask,Outside,Accent,Neutral}`; **third-party tool tints** `tool*`; **tiles** `tileFolder(Ink)`; **overlay** `ink`.

Rules stated in notes: `purple` is "the one action" (`:11`); status colours are "Glyph and label only" and `statusOff` is "Never for text" (`:30-33`); `hairline` is "Rows inside a list only; never around a container" (`:63`); `ink` is "white on dark, black on light. Used at an alpha" (`:113`). Code adds "Status is carried by a dot and a label, never by a fill" (`GlassStyle.swift:26`) and "Tone never tints the card" (`Containers.swift:597-598`).

Full table (generated from the JSON; "= dark" means no separate light value; flat columns are blank where the flat theme keeps the classic value):

| Token | Dark | Light | flatDark | flatLight | Note (first clause) | JSON line |
|---|---|---|---|---|---|---|
| `purple` | #6d14f3 | = dark |  |  | Brand purple from the Trace logo; the one action. | 11 |
| `traceLiveStart` | #5b14ff | = dark |  |  | The Trace mark's live trace (Claude Design 1c): the gradient's violet start, at the root. | 12 |
| `traceLiveMid` | #b412c4 | = dark |  |  | The Trace mark's live trace: the gradient's purple middle. | 13 |
| `traceLiveEnd` | #ff0a6c | = dark |  |  | The Trace mark's live trace: the gradient's hot-pink end, and the glow on the current step. | 14 |
| `purpleSoft` | #8a3dff | #7a2cf5 |  | #1f7aa8 | Fills and the shared data series. | 15 |
| `purpleText` | #c9b3ff | #5b10cc | #e1d5ff | #0c3f5c | Accent text and tertiary links. | 16 |
| `blue` | #3a7bd5 | #2f6bc4 |  |  | Toggles on, the kept data series, selection. | 17 |
| `promoTintEnd` | #3a7bd5 | = dark |  | #6cb6d6 | The far stop of a promotion card's tint (Home's Missions card): blue, or the light theme's amber. | 18 |
| `textPrimary` | #f2f2f4 | #1d1d1f | #f2f3f8 |  |  | 19 |
| `textSecondary` | #c9c9d0 | #48484f | #f2f3f8 88% | #3c3c43 |  | 20 |
| `textTertiary` | #b4b4bc | #5c5c63 | #f2f3f8 84% | #3d3d43 | Raised from #a9a9b0 for 4.5:1 on glass. | 21 |
| `textSecondaryHighContrast` | #e6e6ec | #2a2a2e |  |  | textSecondary under Increase Contrast. | 22 |
| `textTertiaryHighContrast` | #d6d6dc | #3c3c42 |  |  | textTertiary under Increase Contrast. | 23 |
| `placeholder` | #ffffff 46% | #000000 57% | #ffffff 80% | #000000 64% | A text field's prompt: #1146's .tc-input::placeholder, white, raised from #1146's 30% to the least that clears 4.5:1 on the field fill over every gro... | 24 |
| `hairlineHighContrast` | #ffffff 40% | #000000 45% |  |  | hairline under Increase Contrast. | 25 |
| `edgeHighContrast` | #f2f2f4 40% | #1d1d1f 55% |  |  | A painted surface's edge under Increase Contrast: a solid 1pt stroke at 40% text colour (spec, Appearance). | 26 |
| `textOnAccent` | #ffffff | = dark |  |  |  | 27 |
| `textOnStatus` | #0c0c0e | = dark |  |  |  | 28 |
| `textOnSelected` | #f2f2f4 | #1d1d1f | #ffffff | #ffffff | Text on a selected fill (controlSelected): textPrimary in classic, white in the flat theme, whose selected fill is the brand purple. | 29 |
| `statusOn` | #3ddc84 | #1a8f4c | #30d158 |  | Watching, share automatically, automatic, always on. | 30 |
| `statusAsk` | #f5c142 | #a8690f | #ffc75c |  | Ask me, worth a second look. | 31 |
| `statusOff` | #a9a9b0 | #8a8a90 |  |  | Never, not used. | 32 |
| `statusOutside` | #ff6b6b | #d0342c |  |  | Leaves for an outside model, no proof. | 33 |
| `statusOnText` | #3ddc84 | #11613a | #acedbc | #0b4628 | statusOn as text (a pill label, the submit-done label): 4.5:1 or more on every light ground and on its own tint. | 34 |
| `statusAskText` | #f5c142 | #7a4a06 | #ffd585 | #573403 | statusAsk as text: 4.5:1 or more on every light ground and on its own tint. | 35 |
| `statusOutsideText` | #ff9494 | #a3221c | #ffd3d3 | #771814 | statusOutside as text: 4.5:1 or more on every light ground and on its own tint. | 36 |
| `destructiveText` | #ff8a8a | #c62828 | #ffd0d0 | #791313 | The destructive button's label (GlassButtonKind.destructive): the outside red lifted so it clears 4.5:1 on the glass control fill over the pane (5.0;... | 37 |
| `badgeFill` | #ff6b6b | #e04a42 |  |  | The decisions-owed badge behind textOnStatus. | 38 |
| `dataShared` | #8a3dff | #7a2cf5 |  |  |  | 39 |
| `dataKept` | #3a7bd5 | #2f6bc4 |  |  |  | 40 |
| `dataInference` | #a78bfa | #7d5ce0 |  |  |  | 41 |
| `sceneBase` | #0f1219 | #e6eaf1 | #070a1a |  |  | 42 |
| `sceneWarm` | #1d2430 | #f6f7fa | #11152b |  |  | 43 |
| `paneBase` | #161a22 96% | #f4f5f8 96% | #0d1124 96% |  | The neutral dark a pane's glass sits on where there is no native material. | 44 |
| `paneOpaque` | #1c1e24 | #f2f3f6 | #0d1124 |  | A pane under Reduce Transparency: solid, no material (spec). | 45 |
| `glassVeil` | #0c0e14 28% | #ffffff 30% | #070a1a 68% | #e3e6ec 66% | Over native glass, the thin dark veil kept for text contrast. | 46 |
| `edgeRailHandle` | #ffffff 28% | #1d1d1f 28% |  |  | The closed edge rail's handle, a 3 by 72 bar drawn straight on the desktop at the screen's right edge (Run 1 OS-level Explorations, 1b). | 47 |
| `inactiveDim` | #000000 0% | = dark | #070a1a 14% | #000000 4% | Painted over a pane's veil while its window is out of focus, so a background window reads darker, as the system's own windows do (owner, 2026-10-12). | 48 |
| `wellFill` | #000000 22% | #000000 6% | #000000 30% | #8a93a5 43% |  | 49 |
| `controlHover` | #ffffff 16% | #ebebed 84% | #000000 44% |  | Hover on a glass, round, pill-icon, picker or toolbar button (#1146 --tc-control-hover). | 50 |
| `cardHover` | #ffffff 10% | #ffffff 86% | #ffffff 8% | #f7f8fb 80% | Hover on an interactive card: #1146's .tc-card--interactive:hover fill, which replaces the card gradient. | 51 |
| `rowHover` | #ffffff 5% | #000000 4% | #ffffff 5% |  | Hover on an unselected list row (#1146 .tc-list-row:hover). | 52 |
| `toolbarExpanded` | #55555a | #d1d1d6 | #6d14f3 |  | A toolbar button whose menu is open (#1146 .tc-btn--icon[aria-expanded=true]). | 53 |
| `toolbarGlyph` | #e6e6ec | #1d1d1f |  |  | A toolbar button's glyph (#1146 monitor-toolbar.tsx). | 54 |
| `toolbarGlyphHidden` | #83838c | #8a8a90 |  |  | A toolbar glyph whose pane is hidden (#1146 .tc-btn--icon[aria-pressed=false]). | 55 |
| `controlSelected` | #ffffff 16% | #ffffff | #6d14f3 | #15608a |  | 56 |
| `controlSelectedFloating` | #ffffff 18% | #ffffff | #6d14f3 | #15608a | The chosen segment of a floating segmented control (the map's view tabs), drawn with no edge: #1146 .tc-segmented--floating .tc-segmented__item[aria-... | 57 |
| `toggleOn` | #3a7bd5 | #2f6bc4 | #6d14f3 | #15608a |  | 58 |
| `toggleOff` | #ffffff 18% | #000000 16% |  |  |  | 59 |
| `toggleOnSettings` | #8a3dff | #7a2cf5 |  |  |  | 60 |
| `watchOn` | #3ddc84 | #1a8f4c | #30d158 |  | The watch switch's track when on: statusOn in both appearances, as #1146's --tc-watch-on is var(--tc-status-on). | 61 |
| `switchKnobEdge` | #000000 65% | #000000 18% |  |  | A 1pt ring inside the white switch knob, drawn on the watch switch when on (owner ruling, 2026-10-07: hold the WCAG floors). | 62 |
| `hairline` | #ffffff 7% | #000000 8% | #ffffff 8% |  | Rows inside a list only; never around a container. | 63 |
| `rule` | #ffffff 12% | #000000 12% | #ffffff 12% |  | The 0.5pt rule under a modal's header and over its footer, and over the Traces graph footer (#1146 rgba(255,255,255,0.12)). | 64 |
| `tabEmber` | #8a3dff | #7a2cf5 84% |  | #2a8fc4 | The main window tabs' ember (owner choice, 2026-10-10, the Ember Rule at 1.4x): a 2pt line laid on the tab rule under the selected tab, this colour a... | 65 |
| `tabEmberHalo` | #8a3dff 31% | #7a2cf5 22% |  | #2a8fc4 30% | The faint halo rising from the tab ember behind the selected title: this colour at the rule, fading upward and outward to nothing. | 66 |
| `popoverFill` | #22242a 94% | #f7f7f9 84% | #0b0f22 82% |  |  | 67 |
| `menuFill` | #22242a 94% | #f7f7f9 80% | #0b0f22 82% |  |  | 68 |
| `menuHover` | #3a7bd5 85% | #2a62b5 90% | #6d14f3 90% | #15608a 90% | Light: deep enough for menuHoverText at 4.5:1 (4.91). | 69 |
| `menuHoverText` | #f2f2f4 | #ffffff |  |  | A menu item's text on menuHover: textPrimary in dark, white in light, as the macOS menu selection. | 70 |
| `menuSelection` | #2f6ac0 | #2a62b5 | #6d14f3 | #15608a | The menu-row hover behind white text. | 71 |
| `menuModeAsk` | #f0a030 | = dark |  |  | Menu-bar mode circle: ask me. | 72 |
| `menuModeArmed` | #34c759 | = dark |  |  | Menu-bar mode circle and Private AI on option: contribute automatically. | 73 |
| `menuModeNever` | #ff453a | = dark |  |  | Menu-bar mode circle: never; also the menu-bar badge. | 74 |
| `menuPillOff` | #5a5a5f | #aeaeb2 |  |  | Menu-bar pill circle when paused or off. | 75 |
| `menuBarsPaused` | #555555 | #b4b4b8 |  |  | Graph and strip bars while watching is paused. | 76 |
| `menuStripTint` | #000000 32% | #ffffff 60% |  |  | The tinted capsule behind the menu-bar strip's bars, so they read over any wallpaper (owner, 2026-10-11). | 77 |
| `menuChipShared` | #c86bfa 35% | #7a2cf5 18% |  |  |  | 78 |
| `menuChipKept` | #3aa0ff 35% | #2f6bc4 18% |  |  |  | 79 |
| `menuNoProof` | #ff8a8a | #c62828 |  |  |  | 80 |
| `menuSeparator` | #ffffff 14% | #000000 10% |  |  |  | 81 |
| `nodeCardFill` | #14161c 92% | #ffffff 84% | #0b0f22 82% |  |  | 82 |
| `scrim` | #000000 35% | #000000 25% |  |  | The general scrim, #1146's --tc-scrim at .35. | 83 |
| `modalScrim` | #000000 40% | #000000 25% |  |  | Behind a GlassModal, over a within-window blur of size.modalScrimBlur (#1146 --tc-modal-scrim and --tc-modal-scrim-blur). | 84 |
| `selection` | #3275d3 | #2f6bc4 | #6d14f3 | #15608a | #1146's --tc-selection, var(--tc-blue) #3a7bd5, darkened the least, at the same hue, that white row text clears 4.5:1 (4.55; #3a7bd5 was 4.22), owner... | 85 |
| `mapIdle` | #ffffff 35% | #000000 30% |  |  |  | 86 |
| `mapNodeOff` | #5d5d63 | #a1a1a6 |  |  |  | 87 |
| `mapHub` | #8e8e96 | #8a8a92 |  |  | The map's centre node. | 88 |
| `mapFieldInner` | #1e2a3a | #eef2f8 | #070a1a 15% | #ffffff 10% |  | 89 |
| `mapFieldOuter` | #131a24 | #dbe2ec | #070a1a 32% | #ffffff 22% |  | 90 |
| `mapRuleAutoFill` | #12321f | #d7f1e2 |  |  |  | 91 |
| `mapRuleAskFill` | #2b2412 | #f6ead0 |  |  |  | 92 |
| `mapRuleIgnoreFill` | #3a3a3e | #e4e4e7 |  |  |  | 93 |
| `mapRuleUnsetFill` | #2a2a2c | #ededf0 |  |  |  | 94 |
| `mapCredentialOn` | #2c7a5b | #27a06b |  |  |  | 95 |
| `graphFocusOn` | #4da3ff | #1f6fd1 |  |  | The graph footer's focus glyph while the map is focused on a tool (#1146 traces-graph.tsx). | 96 |
| `graphFocusIdle` | #d6d6dc | #3c3c42 |  |  | The focus glyph when a tool can be focused. | 97 |
| `graphFocusOff` | #6b6b70 | #a1a1a6 |  |  | The focus glyph with nothing selected to focus on. | 98 |
| `consentFill` | #000000 25% | #000000 4% | #000000 30% | #f4f6f9 45% |  | 99 |
| `fieldFill` | #000000 25% | #000000 5% | #000000 30% | #f4f6f9 60% |  | 100 |
| `tintOn` | #3ddc84 18% | #1a8f4c 14% |  |  |  | 101 |
| `tintAsk` | #f5c142 18% | #a8690f 14% |  |  |  | 102 |
| `tintOutside` | #ff6b6b 18% | #d0342c 12% |  |  |  | 103 |
| `tintAccent` | #8a3dff 22% | #7a2cf5 14% |  |  |  | 104 |
| `tintNeutral` | #ffffff 10% | #000000 6% |  |  |  | 105 |
| `toolClaude` | #e08a6a | #c2603e |  |  |  | 106 |
| `toolCodex` | #e6e6ec | #3a3a3c |  |  |  | 107 |
| `toolAntigravity` | #6d9cff | #3a68d8 |  |  |  | 108 |
| `toolOpenCode` | #4fd39a | #1d9467 |  |  |  | 109 |
| `toolTheia` | #9d93ff | #6152e0 |  |  |  | 110 |
| `tileFolder` | #2a2a2c | #e6e6ea |  |  |  | 111 |
| `tileFolderInk` | #8be28b | #2c8a37 |  |  |  | 112 |
| `ink` | #ffffff | #000000 |  |  | Overlay strokes and fills over a surface: white on dark, black on light. | 113 |

**Colours used in code that are not tokens** (token bypasses inside TCDesign itself):
- Map field marks: `GlassMapMarks.ink` white 9.6% / black 8%, `litInk` white 20% / black 15%, `bloom` white 3.5% / white 20%, `shimmerInk` white 24% / black 16% (`Indicators.swift:598-605`).
- Promotion card: tint gradient `purpleSoft` at 34% then 20% to `promoTintEnd` at 22%, times a strength of 1 (dark) or 0.85 (light) (`GlassPromo.swift:74-76`, `:136-142`); hover white 6% `plusLighter` (dark) or `purpleSoft` 7% (light) (`:83-92`); spotlight `purpleSoft` 25% resting / 50% under the pointer (`:220-233`); aurora blobs at 62%/50%/32% alpha, blur 34 (`:175-193`); shimmer white 22% (`:208`).
- `GlassColor.ink(alpha)` is used at 0.08 (status-dot halo, skeleton, section-nav hover), 0.1 (tool-tile ground, option-row hover), 0.12 (activity tile), 0.14 (kebab hover, split-button divider, section rule, axis rules, step connector), 0.16 (subtle badge), 0.18 (spinner track), 0.2/0.09/0.07 (bar-graph unlit dots and hover wash) (`Indicators.swift:23,284,397-403,486`; `Controls.swift:474,665`; `Containers.swift:591`; `Feedback.swift:45,93`; `MenuBarPanel.swift:173,253,470`; `Navigation.swift:401`).
- Literal white: state-pill glyph (`MenuBarPanel.swift:61`), checkmark/minus in the checkbox (`Controls.swift:877-879`), menu-row and activity-row hover text (`Surfaces.swift:210`, `MenuBarPanel.swift:472-487`), menu-bar badge text (`MenuBarPanel.swift:415,431`).
- `GlassActivityRow` hovers on `blue` #3a7bd5 under white text (`MenuBarPanel.swift:494`) although `menuSelection` exists precisely because white on #3a7bd5 is 4.22:1, under 4.5:1 (`glass.tokens.json:71`). A contrast bug the parent system should not inherit.

### 2.2 Gradients

| Token | Angle | Dark stops | Light stops | flatDark stops | flatLight stops | Line |
|---|---|---|---|---|---|---|
| `paneFill` | 160 | #ffffff 10% at 0, #ffffff 5% at 0.4, #ffffff 3% at 1 | #ffffff 55% at 0, #ffffff 35% at 0.4, #ffffff 25% at 1 | #ffffff 4% at 0, #ffffff 4% at 0.4, #ffffff 4% at 1 | #f4f6f9 8% at 0, #f4f6f9 8% at 0.4, #f4f6f9 8% at 1 | 116 |
| `cardFill` | 180 | #ffffff 8.5% at 0, #ffffff 4.5% at 1 | #ffffff 72% at 0, #ffffff 52% at 1 | #0d1124 35% at 0, #0d1124 35% at 1 | #ffffff 35% at 0, #ffffff 35% at 1 | 121 |
| `cardFillQuiet` | 180 | #ffffff 7.5% at 0, #ffffff 4% at 1 | #ffffff 60% at 0, #ffffff 42% at 1 | #0d1124 28% at 0, #0d1124 28% at 1 | #ffffff 29% at 0, #ffffff 29% at 1 | 125 |
| `controlFill` | 180 | #ffffff 14% at 0, #ffffff 7% at 1 | #ffffff 92% at 0, #ffffff 72% at 1 | #000000 30% at 0, #000000 30% at 1 | #ffffff 44% at 0, #ffffff 44% at 1 | 129 |
| `ctaFill` | 180 | #8a3dff 72% at 0, #6d14f3 62% at 1 | #7a2cf5 at 0, #6d14f3 at 1 | #6d14f3 at 0, #6d14f3 at 1 | #15608a at 0, #15608a at 1 | 133 |
| `ctaSecondaryFill` | 180 | #4a0ea6 60% at 0, #320878 55% at 1 | #5a12c9 at 0, #4a0ea6 at 1 |  |  | 137 |
| `checkboxOnFill` | 180 | #8a3dff 80% at 0, #6d14f3 70% at 1 | #7a2cf5 at 0, #6d14f3 at 1 |  |  | 141 |

Notes: `ctaFill` is translucent in dark "as #1146" and opaque in light because "a translucent purple over a light pane washes out under its white label (under 4.5:1)" (`glass.tokens.json:133`); `checkboxOnFill` is opaque in light "so the white check clears 4.5:1" (`:141`). The flat theme flattens every gradient to a single colour (equal stops), i.e. the flat theme is not gradient-based.

### 2.3 Shadows, edges, rims (elevation is expressed as edges, not borders)

| Token | Classic layers (x,y,blur,colour dark / light, inset) | flatDark | flatLight | Line |
|---|---|---|---|---|
| `paneEdge` | inset 0,1,0 #ffffff 30% / #ffffff 60%; inset 1,0,0 #ffffff 12% / #ffffff 24%; inset 0,-1,0 #000000 20% / #000000 9%; 0,12,36 #000000 30% / #000000 13.5% | 0,18,36 #02030a 60% | 0,14,30 #000000 12% | 147 |
| `cardEdge` | inset 0,1,0 #ffffff 20% / #ffffff 40%; inset 0,-1,0 #000000 12% / #000000 5.4% | none | none | 153 |
| `cardEdgeQuiet` | inset 0,1,0 #ffffff 18% / #ffffff 36%; inset 0,-1,0 #000000 10% / #000000 4.5% | none | none | 157 |
| `wellEdge` | inset 0,1,2 #000000 25% / #000000 11.3% | none | none | 161 |
| `controlEdge` | inset 0,1,0 #ffffff 32% / #ffffff 64%; inset 0,-1,0 #000000 18% / #000000 8.1%; 0,1,2 #000000 18% / #000000 8.1% | none | none | 164 |
| `controlSelectedEdge` | inset 0,1,0 #ffffff 30% / #ffffff 60%; inset 0,-1,0 #000000 20% / #000000 9%; 0,1,2 #000000 25% / #000000 11.3% | none | none | 169 |
| `ctaEdge` | inset 0,1,0 #ffffff 50% / #ffffff; inset 0,-2,0 #000000 20% / #000000 9%; 0,4,12 #6d14f3 30% / #6d14f3 30% | none | none | 174 |
| `ctaSecondaryEdge` | inset 0,1,0 #ffffff 28% / #ffffff 56%; inset 0,-1,0 #000000 20% / #000000 9% | none | none | 179 |
| `checkboxEdge` | inset 0,1,0 #ffffff 35% / #ffffff 70%; inset 0,-1,0 #000000 25% / #000000 11.3% | inset 0,0,0 #ffffff 18% | inset 0,0,0 #000000 20% | 183 |
| `popoverEdge` | inset 0,1,0 #ffffff 28% / #ffffff 56%; 0,24,60 #000000 50% / #000000 22.5% | 0,18,36 #02030a 60% | 0,14,30 #000000 12% | 187 |
| `menuEdge` | inset 0,1,0 #ffffff 25% / #ffffff 50%; 0,16,40 #000000 45% / #000000 20.3% | 0,18,36 #02030a 60% | 0,14,30 #000000 12% | 191 |
| `nodeCardEdge` | inset 0,1,0 #ffffff 22% / #ffffff 44%; 0,16,40 #000000 45% / #000000 20.3% | 0,18,36 #02030a 60% | 0,14,30 #000000 12% | 195 |
| `modal` | 0,24,60 #000000 50% / #000000 22.5% |  |  | 199 |
| `mapEdge` | inset 0,1,0 #ffffff 12% / #ffffff 24%; 0,10,30 #000000 28% / #000000 12.6% | 0,18,36 #02030a 60% | 0,14,30 #000000 12% | 202 |
| `barTrackEdge` | inset 0,1,0 #ffffff 14% / #ffffff 50% | none | none | 206 |
| `consentEdge` | inset 0,1,0 #ffffff 10% / #ffffff 20% | none | none | 209 |

How an edge is drawn (`GlassStyle.swift:98-159`): inset layers become a stroke `max(1, blur+1)` wide on the inside of the shape, offset by (x,y), blurred by blur/2 and clipped to the shape (a specular top highlight and a bottom shade); outer layers are drop shadows with radius blur/2 behind a near-transparent fill. "Containers get edges, never solid borders" (`GlassStyle.swift:155`). Under Increase Contrast all inset layers are dropped and replaced by a solid 1pt `edgeHighContrast` stroke (40% text colour dark / 55% light) (`GlassStyle.swift:105-118`). The CTA's outer glow is the only coloured shadow (`#6d14f3` 30%, y 4, blur 12) and it is removed when the CTA is disabled (`Controls.swift:179`). The modal's edge is `paneEdge + modal` (`Modal.swift:217`). Flat theme: every painted tier loses its rim, highlight and shade; only floating things keep one soft shadow (dark `#02030a` 60% y18 b36; light black 12% y14 b30); the checkbox keeps a 0-offset inset ring because "a checkbox keeps its rim, which is the unchecked box" (`glass.tokens.json:342`).

### 2.4 Radii

| Token | Value | flat | Line |
|---|---|---|---|
| `pane` | 16 | 20 | 214 |
| `card` | 14 | 16 | 215 |
| `cardQuiet` | 12 | 14 | 216 |
| `control` | 8 | 11 | 217 |
| `tile` | 6 |  | 218 |
| `checkbox` | 5 |  | 219 |
| `pill` | 999 |  | 220 |
| `menuPanel` | 14 | 16 | 221 |
| `menuStatePill` | 22 |  | 222 |

Tier to radius mapping (`GlassStyle.swift:168-175`): pane = `pane`; card, popover and node card = `card`; quiet card and menu = `cardQuiet`; well, control and selected control = `pill` (capsule). Large tool tile uses `control`, small tool tile `tile` (`Indicators.swift:267`). All shapes use the continuous (squircle) corner style. Hard-coded radii in components: 6 (kebab ground, activity row, day-graph chips; `Controls.swift:473`, `MenuBarPanel.swift:290,493`; `GlassMenuRowStyle` `Surfaces.swift:216`), 5 (menu item, activity-row tile; `Surfaces.swift:166`, `MenuBarPanel.swift:470`), 3 and 2 and 1 (chart bars). `menuPanel` (14, flat 16) is a token the spec quotes as 18 (spec "Values"), and `GlassMenu` actually renders at `cardQuiet` (12) via the `.menu` tier. #1146 also had a window radius of 22 that the JSON never took (spec, "Tokens #1146 has that the JSON does not carry").

### 2.5 Spacing

| Token | Value | flat | Line |
|---|---|---|---|
| `s1` | 2 |  | 225 |
| `s2` | 4 |  | 226 |
| `s3` | 6 |  | 227 |
| `s4` | 8 |  | 228 |
| `s5` | 10 |  | 229 |
| `s6` | 12 |  | 230 |
| `s7` | 14 |  | 231 |
| `s8` | 16 |  | 232 |
| `s9` | 20 |  | 233 |
| `s10` | 24 |  | 234 |
| `paneGap` | 10 |  | 235 |
| `windowPadding` | 0 |  | 236 |
| `windowControlsInset` | 30 |  | 237 |
| `windowControlsWidth` | 78 |  | 238 |
| `panePadding` | 12 |  | 239 |
| `inspectorPaddingHorizontal` | 16 |  | 240 |
| `inspectorPaddingVertical` | 18 |  | 241 |
| `treeInset` | 8 |  | 242 |
| `mapOverlayInset` | 14 |  | 243 |
| `cardPaddingVertical` | 12 |  | 244 |
| `cardPaddingHorizontal` | 14 |  | 245 |
| `cardGap` | 10 |  | 246 |
| `inlineGap` | 6 |  | 247 |
| `modalInsetTop` | 52 |  | 248 |
| `modalInset` | 28 |  | 249 |
| `edgeRailInset` | 12 |  | 250 |
| `edgeRailGap` | 16 |  | 251 |

The spacing scale is s1..s10 = 2, 4, 6, 8, 10, 12, 14, 16, 20, 24 (a 2pt-step scale to 16, then 20, 24; not a strict 4 or 8 grid). Fixed values used in components that are not tokens: card padding 10/12 for quiet cards and stat tiles (`Containers.swift:58-59`, `StatCard.swift:35-36`), node card 12/14 (`Indicators.swift:858-859`), modal header 14 top / 10 bottom / 18 leading / 16 trailing and the same for the footer (`Modal.swift:179-182, 202-205`), modal body 14 vertical / 18 horizontal (`Modal.swift:331-332`), table rows 9/12 and table head 8/12 (`Containers.swift:542-543, 567-568`), key-value grid 10 h-gap / 6 v-gap with a 70pt right-aligned label column and 6pt inset (`Containers.swift:503-526`), menu 5pt inset and 220 min width (`Surfaces.swift:128-129`), legend cell 10 horizontal (`Containers.swift:472`), consent block 10/12 (`Containers.swift:428-429`), code block 12 (`Feedback.swift:79`), expander padding 6/2/2/2 (`Controls.swift:497`), tree indent 8 + 18 per level (`ListRow.swift:251-253`), action-bar note gap `s9` (20) and note spacing `s2` (4) (`ActionBar.swift:23-25`).

### 2.6 Sizes (controls, layout, edge rail)

| Token | Value | flat | Line |
|---|---|---|---|
| `control` | 26 |  | 254 |
| `controlLarge` | 28 |  | 255 |
| `cta` | 34 |  | 256 |
| `submitPill` | 24 |  | 257 |
| `toggleWidth` | 40 |  | 258 |
| `toggleHeight` | 24 |  | 259 |
| `watchSwitchWidth` | 38 |  | 260 |
| `watchSwitchHeight` | 22 |  | 261 |
| `checkbox` | 15 |  | 262 |
| `dot` | 7 |  | 263 |
| `dotLarge` | 8 |  | 264 |
| `tab` | 26 |  | 265 |
| `segmentedTrack` | 30 |  | 266 |
| `glyph` | 16 |  | 267 |
| `toolTile` | 22 |  | 268 |
| `toolTileLarge` | 30 |  | 269 |
| `toolLogo` | 15 |  | 270 |
| `toolLogoLarge` | 20 |  | 271 |
| `listRow` | 40 |  | 272 |
| `paneLeftWidth` | 400 |  | 273 |
| `paneLeftCompactWidth` | 360 |  | 274 |
| `mapWidth` | 440 |  | 275 |
| `mapMinWidth` | 360 |  | 276 |
| `inspectorWidth` | 300 |  | 277 |
| `windowWidth` | 1320 |  | 278 |
| `windowHeight` | 614 |  | 279 |
| `paneLeftMinWidth` | 320 |  | 280 |
| `paneLeftWindowShare` | 0.34 |  | 281 |
| `mapBreakpoint` | 1100 |  | 282 |
| `inspectorBreakpoint` | 900 |  | 283 |
| `windowMinWidth` | 760 |  | 284 |
| `windowMinHeight` | 560 |  | 285 |
| `nodeCardWidth` | 260 |  | 286 |
| `modalWidth` | 780 |  | 287 |
| `modalNarrowWidth` | 450 |  | 288 |
| `modalNavWidth` | 180 |  | 289 |
| `modalScrimBlur` | 8 |  | 290 |
| `spinner` | 12 |  | 291 |
| `spinnerStroke` | 1.5 |  | 292 |
| `skeletonHeight` | 12 |  | 293 |
| `textAreaMinHeight` | 56 |  | 294 |
| `radio` | 15 |  | 295 |
| `radioDot` | 5 |  | 296 |
| `edgeRailWidth` | 56 |  | 297 |
| `edgeRailTile` | 44 |  | 298 |
| `edgeRailRuleWidth` | 28 |  | 299 |
| `edgeRailPeekWidth` | 380 |  | 300 |
| `edgeRailOpenHeight` | 680 |  | 301 |
| `edgeRailZoneWidth` | 4 |  | 302 |
| `edgeRailZoneHeight` | 240 |  | 303 |
| `edgeRailHandleWidth` | 3 |  | 304 |
| `edgeRailHandleHeight` | 72 |  | 305 |

**Control-height ladder** (points, default text size; heights are minimums so labels can grow with the system text size, per spec "Type"):

| Element | Height | Width / padding | Type | Source |
|---|---|---|---|---|
| Primary CTA (`.primary`, or any `.bar` button) | 34 (`size.cta`) | 16 horizontal | bodyStrong, bold (glass/destructive/link in a bar: semibold) | `Controls.swift:73-91` |
| Small CTA (`small: true`; every modal action) | 30 | 14 horizontal | label, bold | `Controls.swift:74-75`, `Modal.swift:144-146` |
| Secondary inline | 34 (or 30 small) | 14 | CTA type | `Controls.swift:99-101` |
| Glass / destructive inline pill | 28 (`controlLarge`) | 12 | label semibold | `Controls.swift:104-106` |
| Submit pill (tree rows) | 24 (`submitPill`) | 10 | caption bold | `Controls.swift:110-113` |
| Link | none | none | label semibold | `Controls.swift:107-109` |
| Round icon button | 28 (26 small) square, symbol 13 (11) | | | `Controls.swift:266-271` |
| Pill icon button | 30 x 26 | glyph 11 (symbol) or 14 (text) | | `Controls.swift:309-319` |
| Toolbar icon button | 28 x 24 in a capsule group with 2pt padding | symbol 13 | | `Controls.swift:360-405` |
| Folder button | 28 | 10 | label bold | `Controls.swift:421-433` |
| Kebab | 22 x 24 | dots 1.6pt in 4x14 | | `Controls.swift:468-471` |
| Picker / select pill | 28 | 10 leading, 8 (picker) or 10 (select) trailing | label semibold | `Controls.swift:697-723` |
| Text field | 28 min | 10 horizontal | label regular | `Controls.swift:937-942` |
| Text area | 56 min | 5 h / 8 v | label regular | `Forms.swift:358-360` |
| Toggle | 40 x 24, knob 18, inset 3 | | | `Controls.swift:772-799` |
| Watch switch | 38 x 22, knob 18, inset 2 | | | same |
| Checkbox / radio | 15 (radio dot 5) | check glyph 8 heavy | | `Controls.swift:869-882`, `Forms.swift:82-93` |
| Segmented tab | 26 in a 30 track (2pt padding) | 8 horizontal (12 floating) | label medium / semibold selected | `Navigation.swift:83-121` |
| Rule tab (main window tabs) | 38 (`segmentedTrack + s4`) | equal widths | body medium / semibold | `Navigation.swift:212-215` |
| List row | 40 min | 16 chevron col, 22 tile, 38 switch col, 22 kebab col | body semibold (medium at session) + caption sub | `ListRow.swift:131-222` |
| Legend cell | 28 fixed | 10 horizontal | label | `Containers.swift:457-476` |
| Menu-bar state pill | 44 (31 circle) | collapses to 44 square | micro over bodyStrong | `MenuBarPanel.swift:55-81` |
| Edge-rail tile | 44 square | radius 12 | | `EdgeRail.swift:51-55` |
| Menu row (panel) | text + 2x4 padding inside, 4 outside, so the hit rect clears 28 | | body | `Surfaces.swift:207-225` |
| Breadcrumb back | 26 square target, glyph 12 | | label semibold | `Navigation.swift:312-317` |

Smallest hit targets are 22-26pt (kebab 22x24, toolbar 28x24, info glyph 12pt with a text-sized hit rect, refresh glyph 13+7 = 20pt square, `Containers.swift:83`). These are desktop-pointer sizes; none meets a 44pt (Apple touch) or 48dp (Material) target. See section 9.

**Window and pane geometry as built** (`ThreePane.swift`): main pane fixed at `paneLeftWidth + 40` = 440 (owner 2026-10-08/09, `:35-37`); inspector two thirds of that, 293 (`:39-41`); map opens at `mapWidth` 440 and is the only pane that takes window resizes, minimum `mapMinWidth` 360 (`:17-18`); pane gap 10, window padding 0 (`:22-23`); opening a pane grows the window to the right by the pane plus its gap, closing shrinks it, nothing else moves (`:19-21`, `:132-143`); first launch shows the map at a screen width >= 1100 and the inspector at >= 900 (`:160-166`); the traffic lights sit inside the main pane, which reserves `windowControlsInset` 30 x `windowControlsWidth` 78 (`ThreePane.swift:4-8`, `:279`). Default window = 440 + 10 + 440 + 10 + 293 = 1193 wide (`ThreePane.swift:370-372`) by `windowHeight` 614 (`TraceCommonsAppMain.swift:190-191`); min height 560. Several layout tokens are now unused or contradicted by code: `inspectorWidth` 300 (code 293), `windowWidth` 1320, `windowMinWidth` 760, `paneLeftCompactWidth` 360, `paneLeftMinWidth` 320, `paneLeftWindowShare` 0.34 (the #1146/spec formula `min(400, max(320, 0.34 x width))` is no longer used), plus `glyph`, `treeInset`, `scrim`, `mapIdle`, `watchOn`, `switchKnobEdge`, `barTrackEdge`, `motion.slow` have no reference in `macos/Sources` outside the generated file (checked by search).

**Edge rail measures** (`glass.tokens.json:6`, `EdgeRail.swift:8-24`): closed, a 4 x 240 hover zone on the screen's right edge holding a 3 x 72 handle (`edgeRailHandle` white/black at 28%), vertically centred; open, a 56-wide rail of 44pt tiles, inset 12 from the edge, with a 380-wide peek pane 16 to its left, 680 tall at most; the open window width is shadowRoom (16+4) + 380 + 16 + 56 + 12 = 484. Tiles use `cardQuiet` radius; a 28 x 1 `rule` separates section tiles from the app tile (`EdgeRail.swift:86-95`).

### 2.7 Opacity

| Token | Value | flat | Line |
|---|---|---|---|
| `disabled` | 0.45 |  | 308 |
| `disabledSubmit` | 0.55 |  | 309 |
| `disabledCheck` | 0.7 |  | 310 |
| `rowOff` | 0.6 |  | 311 |
| `skeletonDim` | 0.5 |  | 312 |
| `chartSeriesReduced` | 0.75 |  | 313 |

Inconsistency: the JSON note says `disabled` 0.45 "is the one disabled dimming for every control ... the submit pill and the checkbox, which #1146 dims to .55 and .7, use it too" (`glass.tokens.json:7`), but code uses `disabledSubmit` 0.55 for the submit pill (`Controls.swift:146-149`) and `disabledCheck` 0.7 for checkboxes and radios (`Controls.swift:836`, `Forms.swift:149,248`). `rowOff` 0.6 now fades only the row's tool tile; the title steps down to `textSecondary` instead (owner ruling 2026-10-07; `ListRow.swift:114-128,157-159`), contradicting the JSON note that describes a faded sub-line. Pressed is not an opacity: the fill goes 8% darker (`GlassPress.swift:9-27`).

### 2.8 Blur and materials

There are **no blur tokens**. Blur comes from native materials (`GlassBackdrop.swift`):
- Pane (navigation layer): `NSGlassEffectView` style `.regular` (frosted) on macOS 26 (`GlassBackdrop.swift:57-66`); `NSVisualEffectView` `.hudWindow`, `.behindWindow`, before 26 (`:120-131`); the flat theme defaults to `regularTint`: Liquid Glass tinted with 25% of the veil's alpha (`GlassTheme.swift:76-92`, `GlassBackdrop.swift:88-97`). Over the material the pane paints `glassVeil`, then `paneFill`, then `inactiveDim` when the window is not key, then (flat + Increase Contrast) the veil again at 50% (`GlassBackdrop.swift:142-175`).
- Floating surfaces (popover, menu, node card, floating segmented control): the painted tier over `NSVisualEffectView` `.hudWindow` blending `.withinWindow` (`GlassBackdrop.swift:182-201`; `GlassStyle.swift:295-336`), "on macOS 26 too (owner ruling, 2026-10-07)". The spec's popover tier asked for "blur 24 at 170% saturation" which has no native knob; saturation is omitted.
- Modal scrim: the window content blurred by `modalScrimBlur` 8 under `modalScrim` black 40% / 25% (`Modal.swift:461-465`, `:538-539`); "Never a system material, which hides it".
- Content layer (the map): classic draws it opaque (`paneOpaque`), "as Apple keeps content out of Liquid Glass"; flat puts it on the same glass (`GlassTheme.swift:43-47`, `GlassBackdrop.swift:21-25`).
- On macOS 26, `GlassFloatingGroup` wraps floating siblings in a `GlassEffectContainer` so they "blend and morph as one surface" (`GlassStyle.swift:350-373`).
- #1146 (Tauri) values for reference: window blur 30 at 180% saturation, popover 24 at 170%, scrim 6 (spec "No blur tokens"). Section 8 has the CSS.

### 2.9 Strokes, hairlines, rules, rims

| Element | Stroke | Colour | Source |
|---|---|---|---|
| Hairline / rule | one device pixel (0.5pt on Retina, 1pt at 1x; never < 0.5) | `hairline` (rows only) or `rule` | `Containers.swift:7-31` |
| Modal header/footer rule, graph footer, tab rule | 1 device px / 1pt | `rule` white or black 12% | `Modal.swift:336-341`, `Navigation.swift:176-179` |
| Tab ember | 2pt line, 30% past the tab each side, fading to 0; halo 26pt tall | `tabEmber`, `tabEmberHalo` | `Navigation.swift:137-263` |
| Invalid field / select ring | 1pt inside | `statusOutside` | `Controls.swift:922-925, 976-979` |
| Failed tag outline | 1pt | its ink | `Indicators.swift:138` |
| Chip outline (classic) | 0.5pt at 60% of ink; none in flat (owner 2026-10-10) | status text colour | `Indicators.swift:100-103` |
| Status-dot halo / ring | 2pt ink 8% / 3pt status 25% | | `Indicators.swift:21-28` |
| Increase Contrast edge | 1pt solid | `edgeHighContrast` | `GlassStyle.swift:113-118` |
| Split-button divider | 1pt, 6pt vertical inset | ink 14% | `Controls.swift:664-668` |
| Menu separator | 1pt, 8pt side inset | `menuSeparator` | `Surfaces.swift:178-189` |
| Promo edge | 1pt gradient `purpleSoft` 70% to `promoTintEnd` 35%; glowBorder 1.5pt + 4pt blurred 6 rotating | | `GlassPromo.swift:239-277` |
| Spinner | 1.5pt track ink 18% + quarter arc `textSecondary` round cap | | `Feedback.swift:41-50` |

### 2.10 Motion

| Token | Value | flat | Line |
|---|---|---|---|
| `fast` | 0.15 |  | 329 |
| `standard` | 0.22 |  | 330 |
| `slow` | 0.3 |  | 331 |
| `reveal` | 0.18 |  | 332 |
| `slide` | 0.25 |  | 333 |
| `easeX1` | 0.2 |  | 334 |
| `easeY1` | 0.8 |  | 335 |
| `easeX2` | 0.2 |  | 336 |
| `easeY2` | 1 |  | 337 |
| `spin` | 0.8 |  | 338 |
| `pulse` | 1.6 |  | 339 |

- **The one curve**: `timingCurve(0.2, 0.8, 0.2, 1)` at the duration tokens, and no animation under Reduce Motion (`GlassMotion.swift:4-27`); `fast` 150ms for hover and press fills (`GlassStyle.swift:270`, `GlassHover.swift:38`, `GlassPress.swift:84,95`); `standard` 220ms for modal fade (`Modal.swift:482`) and pane show/hide, where the window frame animates on the same clock and curve via `NSAnimationContext` (`ThreePane.swift:349-358`).
- **Documented exceptions in code** (each deviates from "one curve", which the spec says should be the only curve apart from `flowDash`): switch knob `.easeOut` 220ms (150ms watch switch) (`Controls.swift:766-768, 788`); main-window tab ember `spring(response: 0.35, dampingFraction: 0.85)` (`Navigation.swift:186`); bar-graph period slide 0.45s `cubic-bezier(.4,0,.2,1)` kept from #1146 (`Indicators.swift:500-501`); map shimmer 1.1s `timingCurve(0.3, 0, 0.15, 1)`, first pass 1s after showing, then every 40s (`Indicators.swift:606-616`); spinner one turn per `spin` 0.8s, linear (`Feedback.swift:35-39`); skeleton opacity 1 to 0.5 over `pulse/2` each way (`Feedback.swift:80-88`); promo aurora at 30fps, shimmer 1.4s per 6s, glowBorder one turn per 8s (`GlassPromo.swift:156-264`). `slide` (0.25) is used for the graph footer show/hide (`MonitorWindowView.swift:758`), the edge-rail peek (`EdgeRailView.swift:83`) and the menu-bar sub-list swap (`MenuBarGlassPanel.swift:60`); `reveal` (0.18) for the menu-bar state-pill expansion (`MenuBarGlassPanel.swift:86`); `slow` (0.30) has no call site.
- **Reduce Motion**: every TCDesign animation checks `accessibilityReduceMotion` or `GlassMotion.systemReducesMotion`: hover/press fades, the switch slide, the expander rotation, the modal fade, pane transitions (window jumps to its new frame), bar slide, tab ember (moves at once), spinner (stands still), skeleton (no pulse), map shimmer (never runs) and map light, promo treatments (hold one frame). Verified in the files cited above.

### 2.11 Z / elevation tiers

`GlassTier` (`GlassStyle.swift:163-218`): "Panes are the containment; cards tint a pane; wells recess into a card; controls sit on top. Never glass on glass."

| Order (back to front) | Tier | Fill | Edge | Radius |
|---|---|---|---|---|
| 0 | Scene | the desktop through a transparent window (`window.backgroundColor` white 0 alpha 0.004 so gaps still take clicks and resizes, `GlassBackdrop.swift:218-246`); `sceneBase/Warm` only behind first run | none | |
| 1 | Pane (navigation layer) | native material + veil + `paneFill` (+ `inactiveDim`) | `paneEdge` (drawn on Liquid Glass too, owner 2026-10-07) | 16 / flat 20 |
| 1c | Content pane (map) | classic: `paneOpaque` + `paneFill`; flat: glass | `mapEdge` | 16 / 20 |
| 2 | Card / quiet card | `cardFill` / `cardFillQuiet` gradient (painted, never blurred) | `cardEdge` / `cardEdgeQuiet` | 14 / 12 (flat 16 / 14) |
| 2- | Well (recessed) | `wellFill` | `wellEdge` (inner shadow) | capsule |
| 3 | Control / selected control | `controlFill` gradient / `controlSelected` | `controlEdge` / `controlSelectedEdge` | capsule |
| 4 | Floating: popover, menu, node card, floating tabs | `popoverFill` / `menuFill` / `nodeCardFill` over within-window blur | `popoverEdge` / `menuEdge` / `nodeCardEdge` | 14 / 12 / 14 |
| 5 | Modal | `paneBase` + `paneFill` (opaque-ish pane, "one more pane on a solid backing"), scrim `modalScrim` + blur 8 behind | `paneEdge` + `modal` | 16 |
| 6 | System popovers (info button, icon-card info) and native `Menu`s | system | system | system |

Layer environment: `glassLayer` = `.content` or `.floating` (`GlassStyle.swift:286-293`); `glassSurface(_:floating:)` is the single call site that turns a surface into floating glass (spec "One call site").

### 2.12 Typography

| Step | textStyle | Size | Weight | Line height | Tracking | Other | Line |
|---|---|---|---|---|---|---|---|
| `micro` | caption2 | 10 | bold | 13 | 0 | SF Pro | 316 |
| `eyebrow` | caption2 | 10 | bold | 14 | 0.8 | uppercase, SF Pro | 317 |
| `caption` | subheadline | 11 | regular | 16 | 0 | SF Pro | 318 |
| `label` | callout | 12 | medium | 16 | 0 | SF Pro | 319 |
| `body` | body | 13 | regular | 18 | 0 | SF Pro | 320 |
| `bodyStrong` | body | 13 | semibold | 18 | 0 | SF Pro | 321 |
| `title` | title3 | 15 | semibold | 20 | 0 | SF Pro | 322 |
| `heading` | title2 | 17 | semibold | 22 | 0 | SF Pro | 323 |
| `display` | title | 22 | bold | 28 | -0.22 | SF Pro | 324 |
| `number` | largeTitle | 26 | bold | 34 | 0 | tabular, SF Pro | 325 |
| `mono` | subheadline | 11 | regular | 16 | 0 | SF Mono | 326 |

- Faces: SF Pro and SF Mono only, via `Font.system(textStyle, design:)` (`GlassTokenTypes.swift:301-304`); no fonts are bundled. Every step maps to a macOS text style at that style's default size, so the whole scale follows the macOS text-size setting; tracking and line spacing are scaled by the same ratio (`GlassTokenTypes.swift:242-321`). Leading is approximated by assuming a 1.2x default line box (`:316-321`). The macOS text-style sizes the generator assumes: largeTitle 26, title 22, title2 17, title3 15, headline 13, body 13, callout 12, subheadline 11, footnote 10, caption 10, caption2 10 (`generate.py:76-88`).
- Variants applied in code: `.weight(_)` (selected tabs, bold counts), `.tracking(_)`, `.monospaced`; `number` uses `monospacedDigit()`; `GlassStatCard` value is `heading` bold (#1146's 18px/700 mapped to title2 17) (`StatCard.swift:16-18`); step-progress labels track 0.06em = 0.6pt (`Navigation.swift:417-418`); `GlassSectionRule` eyebrow tracks 1pt in accent text (`Containers.swift:585-590`).
- Fixed point sizes are forbidden for words; `glassGlyph(size)` is only for SF Symbols and marks inside fixed-size controls (`GlassStyle.swift:85-94`), enforced by a source-scan test (spec "Type", `FixedPointTypeTests`).
- Decision drift: spec Decision 10 says eyebrow weight is 600 (semibold, "from #1179 on the JSON has semibold"), but the JSON has `"weight": "bold"` (`glass.tokens.json:317`).
- Copy is never authored in Swift: "this shell authors no sentences (ShellWordingTests), and real wording reaches the screens from the Rust core" (`GlassGallery.swift:6-9`). Every component takes its words (labels, accessibility values, placeholders, close labels, state words) from the caller.

### 2.13 Chart and data-visualisation tokens

- Series: `dataShared` #8a3dff / #7a2cf5 (rises above the axis), `dataKept` #3a7bd5 / #2f6bc4 (hangs below), `dataInference` #a78bfa / #7d5ce0; `chartSeriesReduced` 0.75 for a lighter step of `accentText` beside the full-strength series (Insights' cache-write series, Patterns weekly bars), which "clears 3:1 against the flat pane, a card and a quiet card over the worst desktop" (`glass.tokens.json:7`, `:313`).
- `GlassBarGraph` (`Indicators.swift:338-488`): a tapered dot matrix, 7 dots per half column (shared up, kept down) on a 1pt axis rule (ink 14%); column height 96, matrix end inset 6; 3 dot columns of radius 1.9 per bucket, or 1 column of radius 1.5 when there are more than 14 buckets ("thin"); dot alpha tapers 0.35 + 0.65 x (row+1)/tip and the last lit dot carries the remainder (min 0.35); a count of one always lights a dot; unlit dots ink 9% (20% when hovered); hover is a solid wash (ink 7%) "never an outline"; labels `statusOff`, primary when hovered, never wrapped; each bucket is one accessibility element with the caller's description.
- `GlassDayGraph` (menu-bar panel, `MenuBarPanel.swift:203-292`): 104pt plot, columns 2pt apart with 2pt top/bottom radii, min bar 6pt, chips `menuChipShared`/`menuChipKept` behind `textPrimary`, grey `menuBarsPaused` while paused, range labels caption tertiary, one accessibility label for the plot.
- `GlassMenuBarStrip` (status item, `MenuBarPanel.swift:299-445`): last 7 columns, 2.5pt bars 2-9pt tall, 20pt tall on a `menuStripTint` capsule, 13pt red badge (`menuModeNever`) 8.5pt bold, `!` attention mark, hollow 9pt `purpleText` news ring, a 2pt `purpleText` halo around the badge for "ready"; unavailable data draws flat 2pt bars and no badge ("data that could not be read is never drawn as activity").
- Map: `mapFieldInner/Outer` radial (80% x 60% radii, centre 50%/55%) (`Indicators.swift:512-555`) with the NEAR AI "N" mark tiled at 5.6pt on a 28pt diagonal pitch plus 1.6pt dots, faded to the edges, lit within 140pt of the pointer (`:585-729`); node styles active `blue` r11 + ring, idle `mapNodeOff` r11, outside `statusOutside` r11 + ring, hub `mapHub` r16 + ring (`:866-895`); node card 260 wide on the floating layer (`:843-864`); rule fills `mapRule{Auto,Ask,Ignore,Unset}Fill`, `mapCredentialOn`; graph footer focus glyph `graphFocusOn/Idle/Off`. Flow-map drawing itself lives in the app (section 5).
- Menu-bar mode colours `menuModeAsk` #f0a030, `menuModeArmed` #34c759, `menuModeNever` #ff453a are dark-only, Apple system-colour-like values with no light variant (`glass.tokens.json:72-74`).

## 3. Theme variants and adaptive modes

### 3.1 Two themes x two appearances

The app has **two themes** (`GlassTheme.classic`, `.flat`) and **three appearance choices** (`GlassAppearance.light`, `.dark`, `.system`), giving four rendered looks: classic-dark, classic-light, flat-dark, flat-light.

- **Theme selection** (`GlassTheme.swift:19-41`): fixed for the life of the process, from `TC_GLASS_THEME` or `defaults write <bundle> TCGlassTheme`; with neither, **`flat` is the default** ("On this branch the default is `flat`") and **`classic` under a test run** ("which is what the design suites measure"). Introduced by #1318 "Explore a flat glass theme for the macOS app" (commit `897ac406e`, 2026-10-09) and on `main` at the v0.15.0 release commit (`6ed1e8c46`). So the *shipping* look is the flat theme, while most contrast tests measure classic (FlatThemeContrastTests covers flat; section 7).
- **Appearance** (`GlassTheme.swift:95-139`): Settings > General > Appearance offers Light, Dark, System; stored in `TCAppearance`, applied app-wide by setting `NSApplication.shared.appearance` (aqua / darkAqua / nil). Every token resolves per appearance through dynamic `NSColor` (section 2.0). History: #1173 D2 said dark only; the token file says "D2 revised" (follow the system); the R15 plan's D-2 and the spec's Decision 1 record that where D2 was revised is still open (spec "Decisions" 1; plan D-2).
- **Provenance of flat**: "from getone.one's glass components" (`glass.tokens.json:342`, `GlassTheme.swift:6-13`). A third-party site's look; the parent system should treat this as inspiration, not as a licensed source.

### 3.2 Classic glass (the token defaults)

Translucent white gradients over native glass: `paneFill` 10% to 3% white at 160 degrees, cards 8.5%/4.5% white, controls 14%/7% white, every painted tier with a 1pt top highlight and 1pt bottom shade (inset shadows), a thin dark `glassVeil` (#0c0e14 28%) over Liquid Glass for text contrast, the map on an opaque `paneOpaque` ground, selected states as a brighter white fill (`controlSelected` white 16%) with `textPrimary` on it, toggles blue (`toggleOn` #3a7bd5), selection blue (`selection` #3275d3), CTA a translucent purple gradient with a purple glow. Light: white fills at 55-92% with dark text, and the CTA becomes opaque purple.

### 3.3 Flat glass (the shipping default)

What flat changes (`glass.tokens.json:341-552`, summary in its `$comment` at `:342`):
- **Flat fills**: every gradient becomes one value (pane white 4% dark / #f4f6f9 8% light; card navy #0d1124 35% dark / white 35% light; quiet card 28% / 29%; control black 30% / white 44%; CTA solid #6d14f3 dark / solid #15608a light).
- **No rims**: card, quiet card, well, control, selected control, CTA and consent edges are emptied; panes, popovers, menus, node cards and the map keep one soft shadow (dark `#02030a` 60% y18 blur36; light black 12% y14 blur30). The checkbox keeps a flat inset ring (white 18% / black 20%). "Cards, panes, wells, controls, pills, menus, popovers and node cards drop the rim and are told apart by fill (and, where they float, a soft shadow) alone" (owner 2026-10-10).
- **Bigger radii**: pane 20, card 16, cardQuiet 14, control 11, menuPanel 16.
- **Heavier veil**: dark #070a1a at 68% ("the lightest that holds the floors", owner 2026-10-12 "a little more translucent"); light #e3e6ec at 66% ("a cool grey", owner 2026-10-12). The veil was tuned repeatedly (git log of the JSON: #1342, #1364, "Return flat Light's veil to 55%" #1370 `c7b78eba8`, #1368, #1381); the file now holds 66% for light and 68% for dark.
- **Navy dark**: `sceneBase` #070a1a, `sceneWarm` #11152b, `paneBase`/`paneOpaque` #0d1124, popover/menu/node card #0b0f22 at 82%; text #f2f3f8 at 100/88/84% for primary/secondary/tertiary.
- **Selected = brand purple in dark** (`controlSelected`, `controlSelectedFloating`, `toggleOn`, `selection`, `menuSelection`, `toolbarExpanded` all #6d14f3; `menuHover` #6d14f3 90%; `textOnSelected` white). Dark status brightened to Apple-like #30d158 / #ffc75c with pale text twins (#acedbc, #ffd585, #ffd3d3, #ffd0d0).
- **Light accent is blue, not purple** (owner reference painting, 2026-10-12, "purple read muddy on grey and orange was set aside"): `purpleSoft` #1f7aa8, `purpleText` #0c3f5c, selection/toggles/CTA #15608a, tab ember #2a8fc4, promo far stop #6cb6d6, darker status texts (#0b4628, #573403, #771814, #791313). Because `.tint(GlassTokens.Color.purpleSoft.color)` is applied at the window root (`TraceCommonsAppMain.swift:182-189`), **the system accent in flat Light is teal-blue #1f7aa8**, not the brand purple. This directly contradicts D3 "purple everywhere" and is the biggest brand question for the parent system.
- **Map on glass**: `GlassTheme.contentIsGlass` is true for flat, so the map pane is on the same frosted glass under a light field (`mapFieldInner/Outer` navy 15%/32% or white 10%/22%) (`GlassTheme.swift:43-47`).
- **Inactive window dim**: flat paints `inactiveDim` (#070a1a 14% dark, black 4% light) over an out-of-focus pane "as the system's own windows do" (owner 2026-10-12); classic paints nothing (`glass.tokens.json:48`).
- **Material**: flat panes use `NSGlassEffectView` `.regular` tinted with 25% of the veil (`regularTint`); `TC_GLASS_MATERIAL` can pick `clearTint`, `regular`, `sidebar` (vibrancy) or `hud` for comparison (`GlassTheme.swift:49-92`). Owner 2026-10-09 rejected `.clear` glass because it "showed the desktop unblurred behind a focused window" (`GlassBackdrop.swift:59-62`).
- **Chips** lose their 0.5pt outline in flat and take a neutral tint instead (owner 2026-10-10, `Indicators.swift:100-103`).
- **One pane spec**: "the menu-bar popover, the edge rail and the main window share the one pane spec" (`glass.tokens.json:342`).

### 3.4 Increase Contrast

- `textSecondary`, `textTertiary` and `hairline` swap to their `*HighContrast` partners through `GlassRGBA.adaptive` (`GlassStyle.swift:6-17`): dark #e6e6ec / #d6d6dc / white 40%; light #2a2a2e / #3c3c42 / black 45%.
- Painted edges (all inset highlight/shade layers) are replaced by a solid 1pt `edgeHighContrast` stroke (#f2f2f4 40% dark; #1d1d1f 55% light) (`GlassStyle.swift:105-118`). Liquid Glass takes the system's own contrasting border (R14).
- Flat theme: the veil is painted a second time at 50% opacity (`GlassBackdrop.swift:164-166`).
- Flow map: quiet and dashed links drawn stronger (spec "Appearance", `FlowMapView.swift`).
- `textPrimary` and status colours do not change.

### 3.5 Reduce Transparency

- Decision R14 (as built): "Reduce Transparency is the system's to apply: it frosts Liquid Glass and turns the materials opaque" (`GlassBackdrop.swift:150-151`; `GlassMaterial.current` explicitly does not handle it, `:14-20`; floating surfaces keep their within-window HUD blur, which `NSVisualEffectView` renders opaque by itself, `GlassStyle.swift:330-335`).
- `paneOpaque` (#1c1e24 / #f2f3f6; flat #0d1124) remains the token "under Reduce Transparency: solid, no material (spec)" (`glass.tokens.json:45`), but in current code it is used only for the content-layer (map) pane and `OpaquePaneView` (`GlassBackdrop.swift:168-172, 265-299`). Conflict: the spec ("Appearance": "Every tier swaps blur and translucent fill for an opaque fill: the pane is the paneOpaque token, solid ... and a card is one step lighter") and the R15 plan's Global Constraints ("paneOpaque under Reduce Transparency") describe an app-painted opaque fallback, while the code defers to the system (R14). Flat's `$comment` also says "Reduce Transparency is left to the system (R14)".

### 3.6 Reduce Motion

See 2.10. All component motion is removed; the pane-composition change becomes an instant window frame change (`ThreePane.swift:341-345`); the knob jumps; the ember tab moves at once; the spinner stands still; looping decoration (map shimmer, promo aurora/shimmer/glow) holds one frame.

### 3.7 Pre-macOS 26 fallback (macOS 14-25)

Minimum macOS 14 (`.macOS(.v14)`), built with the macOS 26 SDK; decision D4 "glass on every supported macOS" (spec Decision 3). Before 26:
- Panes: `NSVisualEffectView` `.hudWindow` blending behind the window, under the veil and pane gradient, with our own `paneEdge` (`GlassBackdrop.swift:120-131`).
- Floating surfaces: painted tier over a within-window HUD blur (same code on 26).
- `GlassFloatingGroup` drops the `GlassEffectContainer` (`GlassStyle.swift:363-370`).
- Open: "The pre-26 material in the light appearance. `GlassBackdrop` uses `.hudWindow` whatever the appearance, and HUD is a dark material; the first revision adopted it for a dark-only app" (spec "Open").
- "The fallback is not pixel-identical ... judged on layout, radii, colour and legibility, not on refraction" (spec "Materials by OS").
- Glass-only APIs (`NSGlassEffectView`, `.glassEffect`, `GlassEffectContainer`, `.glassProminent`) are allowed only in the tier code behind `#available(macOS 26, *)`; "Screens never branch on the OS; only TCDesign's tier code does" (R15 plan, Global Constraints), enforced by a source scan (section 7).

### 3.8 Window focus

Out of focus, flat panes take `inactiveDim` (`GlassBackdrop.swift:159-163`). The focus ring is **disabled app-wide** on the Monitor window (`.focusEffectDisabled()`, owner 2026-10-11, `TraceCommonsAppMain.swift:88,110,123,137,191`) and on `GlassRadioRow` (`Forms.swift:255-257`); the spec and the R15 plan both require "the system focus ring" (spec "Components"; plan Global Constraints, "Follow Apple HIG: system focus ring"). This is an accessibility regression the parent system must resolve (section 9).

### 3.9 The flat-glass exploration sheet (`docs/design/flat-glass-theme/index.html`, 671 lines, + `screens/monitor-flat{Dark,Light}.png`)

An HTML mock that rebuilds getone.one's glass components with Trace Commons content, drawing eight component rows (hub + tools, connected endpoints, segmented control + notice, question card "Share this trace?", status rail with 44pt dots, field + filter chips + tiles, display card, command row) in a light and a dark tint over four backdrops (Sky, Dusk, Dark desktop, Light desktop) (FG:306-448). Its source values (FG:80-137): veil `rgba(12,18,44,.42)` light / `rgba(7,10,26,.70)` dark; a 1px inset rim at white 20%/12% plus a top highlight at 32%/18%; drop `0 14px 30px -12px rgba(4,7,22,.6)` / `0 18px 36px -12px rgba(2,3,10,.75)`; blur 18px saturate 1.4 / 22px saturate 1.2; text white / #f2f3f8 with a text shadow; wells, chips, rings, focus (white 80%, 2px outline, offset 2); selected = a solid white pill with near-black ink (brand-purple option `--g-sel: #6d14f3`); geometry pill 32, answer rows 36 at radius 11, chips 28, tiles 92 x 84 at radius 18, hit target 44; motion 150ms ease-out ring, 200ms well colour, 220ms `cubic-bezier(.2,.8,.2,1)` segmented thumb, 1.6s halo, 300ms fade with a 4px rise, all removed under `prefers-reduced-motion` (FG:147-218). Its contrast table shows the light tint failing 4.5:1 for white text on bright backdrops (about 2.4-3.0) because the source relies on a text shadow (FG:450-499). It lists the rulings the theme would reopen (FG:272-282): D3 brand purple (the source has no accent), hover-from-#1146 (the source draws a 50% white ring and keeps the fill), WCAG floors on light grounds, type sizes (source 14 medium body / 15 titles; 14 has no macOS text style), radii (source 24/20/18/16/14/11/6 vs 16/14/12/8/6), and native material (veil-only vs painted fill + rim + drop). A token-mapping table maps each source value to the JSON entry it would replace (FG:629-666). The shipped flat theme kept the navy dark, swapped the light tint for a cool grey with dark text, dropped the rims and text shadows, and kept our type scale.

## 4. Component catalog (TCDesign, `macos/Sources/TCDesign`)

TCDesign is a Swift package target (about 10,200 lines) with: `Tokens/` (theme, types), `Generated/GlassTokens.swift`, `Styling/` (tiers, edges, materials, hover, press, motion, promo), `Components/` (17 files), `Logos/`, and a debug-only `Gallery/GlassGallery.swift` (sections: Colour, Materials, Type, Controls, Forms, Feedback, Modal, Navigation, Indicators, Patterns, Promo, Floating; `GlassGallery.swift:56-70`) runnable as `swift run TCDesignGallery` (`macos/Sources/TCDesignGallery/TCDesignGalleryApp.swift`). Origin: the components are the #1146 Tauri components (`design-system/index.ts`) rebuilt natively, and "#1146 wins for components" (owner ruling 2026-10-07, `Glyphs.swift:3-7`).

### 4.0 Cross-cutting state model (applies to every interactive component)

| State | Rule | Source |
|---|---|---|
| Default | tier fill + tier edge | `GlassStyle.swift:245-279` |
| Hover | a hover fill **replaces** the tier fill (never stacks), faded on `fast`; only while enabled. `controlHover` for glass/round/pill-icon/picker/toolbar controls, `cardHover` for interactive cards, `rowHover` for unselected list rows (never over a selected row), menu items use `menuHover` + `menuHoverText`, panel menu rows `menuSelection` + white, section-nav rows ink 8% + primary text, the link underlines | `GlassStyle.swift:220-243`, `GlassHover.swift`, `Controls.swift:121-130,209`, `ListRow.swift:107-112`, `Surfaces.swift:161-168,210-217`, `SectionNav.swift:26-41` |
| Pressed | the fill 8% darker (`brightness(-0.08)`) on `fast`; "Never a fade, which reads as disabled, and never the label"; glyph-only controls darken a black 8% wash behind the glyph | `GlassPress.swift:9-27,61-97` |
| Focus | the system focus ring (spec), but disabled on the Monitor window and the radio row by owner choice 2026-10-11 | `TraceCommonsAppMain.swift:88,110,123,137,191`, `Forms.swift:255-257` |
| Selected | `controlSelected` + `controlSelectedEdge` + `textOnSelected` (segments, rail tiles); `selection` solid + white text and white sub-line (list rows); a selected glass button turns into the CTA purple with white text and `.isSelected` | `Navigation.swift:94-103,130-134`, `EdgeRail.swift:46-60`, `ListRow.swift:94-112`, `Controls.swift:185-191` |
| Disabled | `opacity.disabled` 0.45 on the whole control; submit pill 0.55 with `statusOff` ink; checkbox and radio 0.7; a disabled control shows no hover | `GlassPress.swift:33-58`, `Controls.swift:143-149,166` |
| Off (list row) | tool tile at `rowOff` 0.6, title in `textSecondary`, sub-line stays `textTertiary` | `ListRow.swift:114-128,157-159` |
| Invalid | 1pt `statusOutside` ring inside the field or pill; the reason in words beside it, from the core | `Controls.swift:922-925` |
| Unknown | "Unknown is neither on nor off": no dot, the core's word; badges draw an em dash, never a number | spec "Appearance"; `Indicators.swift:149-166`, `Navigation.swift:3-7` |
| Busy | modal `busy` makes scrim, Escape, close button and cancel inert | `Modal.swift:104-106,139-150` |

Wording rule for every component: no component authors words, including accessibility values, state words and default labels; callers pass the core's strings or the component uses a native control whose system wording is spoken ("expanded", "checked", "mixed") (spec "Components"; e.g. `Controls.swift:519-523, 805-809, 837-845`).

### 4.1 Buttons (`Components/Controls.swift`)

**`GlassButtonStyle(_ kind: GlassButtonKind, size: GlassButtonSize = .inline, small: Bool = false, selected: Bool = false)`** (`:57-150`)
- Kinds (`:6-20`): `.primary` ("The one purple action on a surface"; CTA gradient, white label, `ctaEdge` with purple glow; glow dropped when disabled, `:175-179`); `.secondary` (dark purple gradient `ctaSecondaryFill`, white label, e.g. Download); `.glass` (control-tier pill, primary text, `controlHover`; `selected` makes it the CTA purple, `:185-195`); `.submit(done:)` (24pt pill on tree rows, label `textPrimary`, `statusOnText` when done "Sent", `statusOff` when disabled, `:136-141`); `.link` (accent text, underline on hover, no container); `.destructive` (glass pill with `destructiveText` red label; "Never the default action", `:17-19`).
- Sizes (owner ruling 2026-10-08, R15 plan D-20): `.inline` (default: inside cards, rows, fields, popovers, toolbars) and `.bar` (in a window/sheet/modal action bar every button is the CTA's height, type size and padding, keeping its own fill/ink/weight) (`:22-40`). Metrics table in section 2.6.
- Anatomy: label only (`configuration.label` in the kind's type and padding, `:214-220`); capsule shape; content shape is the capsule (`:167`).
- A11y: native `Button`; selected glass adds `.isSelected` (`:169`).

Icon-only buttons (all take a `label` that becomes `accessibilityLabel` and `.help` tooltip):
- **`GlassRoundButton(_ label:, systemImage:/icon:, small:, action:)`** 28 (26) round on the control tier with `controlHover` (`:248-277`). Used for modal close (`xmark`, small).
- **`GlassPillIconButton(_ label:, systemImage:/glyph:, ink:, action:)`** 30x26 pill; text glyphs (‹ − + › ›|) for the graph's period controls (`:279-326`).
- **`GlassToolbarButton(_ label:, systemImage:/icon:, pressed: Bool?, expanded: Bool?, action:)`** 28x24 glyph with no fill; `toolbarGlyph` ink, `toolbarGlyphHidden` when its pane is hidden (`pressed == false`), `toolbarExpanded` fill when its menu is open, `controlHover` on hover, `.isSelected` when pressed (`:331-391`). Grouped in **`GlassToolbarGroup`**: a control-tier capsule with 2pt padding and 2pt spacing (`:394-406`).
- **`GlassIcon`** = `.symbol(String)` (SF Symbol) or `.glyph(GlassGlyph)` (#1146 artwork) (`:225-228`).
- **`GlassFolderButton(_ label:, action:)`** folder glyph + "…" pill, 28 tall, 10 sides, label bold (`:411-440`).
- **`GlassKebab(_ label:, open:, action:)`** three 1.6pt dots in a 22x24 target; lit (primary ink on ink 14%, radius 6) when open or hovered, else `statusOff` ink (`:443-484`).
- **`GlassRefreshButton(_ label:, size: 13, action:)`** bare `arrow.clockwise` in `textSecondary`, no pill (owner 2026-10-10) (`Containers.swift:67-90`).
- **`GlassSplitButton(_ title:, menuLabel:, action:, menu:)`** inline glass pill split by a 1pt ink-14% divider; left = action, right = `chevronDown` opening a native `Menu` (owner 2026-10-10) (`Controls.swift:636-690`).

### 4.2 Disclosure, pickers, menus

- **`GlassExpander(_ title:, isOpen:)`** "›" rotating 90 degrees on `fast`, label semibold, padding 6/2/2/2, represented to VoiceOver as a native `DisclosureGroup` (`Controls.swift:487-525`).
- **`GlassPicker<Value>(_ label:, selection: Binding<Value?>, options:, placeholder:)`** a native `Menu` dressed as the glass pill (`GlassPickerPill`: optional 7pt status dot, label semibold, 10pt chevron, 28 tall), placeholder from the caller when nothing is chosen; `accessibilityLabel` + `accessibilityValue` (`:529-581`, `:697-724`). Carries the folder's three modes (Ask me / Automatic / Never).
- **`GlassSelect<Value>(_ label:, selection: Binding<Value>, options:, invalid:)`** always-valued variant with an inline native `Picker` inside the menu so the system draws the check; replaces stock `Picker` (`Forms.swift:13-52`).
- **`GlassIconMenu<Value>(_ label:, systemImage:, selection:, options:)`** a round 28pt icon control opening a native inline picker (owner 2026-10-11) (`Controls.swift:583-630`).
- **`GlassPickerOption<Value>(_ title:, value:, dot: GlassStatus?)`** (`:529-541`).
- **`GlassMenu(onDismiss:, content:)`** custom-painted floating menu: 5pt inset, min width 220, `menu` tier floating, a focus section, Escape dismisses, one VoiceOver container (`Surfaces.swift:110-135`). **`GlassMenuItem(_ title:, checked: Bool?, action:)`** body type, optional leading "✓" in a 12pt column, hover `menuHover` with `menuHoverText`, radius 5, `.isSelected` when checked (`:137-176`). **`GlassMenuSeparator`** (`:178-189`). **`GlassMenuRowStyle`** for menu-like panels: full-width rows, `menuSelection` blue/purple hover with white text, radius 6, 4pt padding inside and outside so the hit rect clears 28pt (`:191-228`).
- **`GlassPopover(onDismiss:, content:)`** popover tier, 10pt padding, floating, focus section, Escape dismisses (`Surfaces.swift:57-79`).
- **`GlassInfoButton(_ label:, text:)`** `info.circle` 12pt tertiary; hover shows a system popover (260 wide, caption secondary, 10pt padding), click pins it (`info.circle.fill`), outside click/Escape unpins; VoiceOver reads the label then the text as value (owner 2026-10-08) (`InfoButton.swift:3-70`).

### 4.3 Toggles, checkboxes, radios

- **`GlassToggleStyle(_ kind: GlassSwitchKind = .standard, showsLabel: Bool = true)`** (`Controls.swift:726-811`): `.standard` 40x24 blue (`toggleOn`), `.settings` 40x24 purple (`toggleOnSettings`), `.watch` 38x22 also purple ("every switch matches", owner 2026-10-08; the earlier green `watchOn` track lost its dark knob ring and white-on-green was ~1.8:1); knob 18pt plain white on every track; off `toggleOff`; Settings switches sit on the trailing edge with labels wrapping on the left (Ron 2026-10-09); represented to VoiceOver as a native `Toggle`. Note the token notes still describe a green `watchOn` with a `switchKnobEdge` ring (`glass.tokens.json:61-62`), and the spec describes a `textOnStatus` knob on green; all three disagree.
- **`GlassCheckboxStyle()`** 15pt rounded square (radius 5): `checkboxOnFill` purple gradient with a white 8pt heavy check, or `wellFill` when off, `checkboxEdge` rim; mixed state from a native `Toggle(sources:isOn:)` draws a minus and VoiceOver says "mixed"; disabled 0.7 (`:813-854`). **`GlassCheckMark(checked:, mixed:)`** the look alone, hidden from assistive tech, for read-only states (`:856-886`). **`GlassCheckRow(_ title:, isOn:)`** a checkbox with its full sentence wrapping beside it (consent rows) (`Forms.swift:285-307`).
- **`GlassRadio(checked:)`** 15pt round well, purple gradient + 5pt white dot when chosen (`Forms.swift:72-96`). **`GlassRadioGroup<Value>(_ label:, selection:, options: [GlassRadioOption])`** a column (6pt spacing) with title + optional caption sub-line; one keyboard stop, arrow keys move between enabled options (wrapping); native `.radioGroup` picker for assistive tech (`:98-171`). **`GlassRadioRow<Value>(_ label:, selection: Value?, options:, none:, choose:)`** a row of short optional choices; pressing the chosen one clears it; arrows move, Space/Return re-press; no focus ring (owner 2026-10-11) (`:173-283`).

### 4.4 Text input

- **`GlassTextField(_ label:, text:, prompt:, secure:, invalid:, showsLabel:, focus:)`** eyebrow label (tertiary) 4pt above a 28pt field: `fieldFill` + `wellEdge` (inner shadow), radius `control`, label-regular type, prompt in `placeholder` ink (raised from #1146's 30% to clear 4.5:1, owner ruling 2026-10-07), system focus ring, disabled 0.45, invalid 1pt red ring; `SecureField` when `secure` (`Controls.swift:888-967`). **`glassFieldWell(invalid:)`** the reusable well (`:969-982`).
- **`GlassTextArea(_ label:, text:, prompt:, invalid:, showsLabel:)`** `TextEditor` in the same well, min 56pt, grows with text; prompt overlay (`Forms.swift:309-366`).
- No search field, stepper, slider, date picker, segmented input, combobox, token field or file picker component exists (search appears in screens using `GlassTextField` with `focus` for Command-F; section 5).

### 4.5 Containers and surfaces

- **`GlassPane(padding: 12, isContent:, edge:, content:)` / `GlassPane(insets:, ...)`** the outermost containment: pane tier, fills the space, `isContent` puts it in the content layer (map) (`Surfaces.swift:3-44`); **`GlassPaneInsets.inspector`** 16 x 18 (`:46-55`).
- **`GlassThreePane(showsMap:, showsInspector:, onFirstLayout:, main:, map:, inspector:)`** the window layout (section 2.6; `ThreePane.swift:202-373`), with **`GlassPaneLayout`** pure layout maths (`:10-200`) and **`glassWindow()`** (transparent full-size title bar window, movable by background, no title-bar separator, `GlassBackdrop.swift:203-263`).
- **`GlassCard(quiet:, flush:, interactive:, content:)`** card or quiet card; padding 12/14 (quiet 10/12, flush 0); interactive lifts with `cardHover` (`Containers.swift:33-63`).
- **`GlassIconCard(systemImage:, title:, subtitle: [String], info:, refresh:, interactive:, promo:, chevron:, accessory:/trailing:, content:)`** the house card head (owner 2026-10-10): 22pt SF Symbol in a 26pt column whose drawn top meets the title's cap height; title bodyStrong (header trait) with an optional refresh glyph; caption subtitle lines with an info glyph set after the last word (hover help + pinned popover); accessory on the right; optional chevron centred on the whole card; optional promo treatment (icon turns accent) (`Containers.swift:114-316`).
- **`GlassEyebrowCard(_ eyebrow:, title:, action:, chevron:, accessory:, content:)`** eyebrow (tertiary) over an optional title (`title` step, header trait), accessory top-right; with `action` the whole card is a button (`:318-387`). **`GlassChevron`** decorative 10pt `chevron.right` (`:389-400`).
- **`GlassPromoCard(_ treatment:, interactive:, content:)`** the promotion card (owner 2026-10-11, Home's Missions card) with `GlassPromoTreatment` `.aurora`, `.shimmer`, `.glowBorder`, `.spotlight` (default), `.tint`; brand tint under the content so text keeps card contrast; still under Reduce Motion (`GlassPromo.swift`).
- **`GlassWell(content:)`** inset track (`Containers.swift:402-413`).
- **`GlassSheet(title:, subtitle:, content:)`** a sheet's padded column inside a pane or modal, "never a pane on a pane" (`Surfaces.swift:81-108`).
- **`GlassConsentBlock(_ text:)`** the core's consent sentence verbatim, directly above Submit, on `consentFill` with `consentEdge`, radius 12, 10/12 padding (`Containers.swift:415-437`).
- **`GlassCode(_ text:)`** mono 11 on `consentFill` with `wellEdge`, selectable (`StatCard.swift:63-84`).
- **`GlassKeyValueList([Item(label, value, mono:)])`** labels right-aligned in a 70pt column, selectable values (`Containers.swift:479-527`).
- **`GlassTableHead` / `GlassTableRow(first:)`** rows inside a flush card: hairline above every row but the first ("hairline above, never around"), 9/12 padding; head in eyebrow type, header trait (`:529-573`). There is no sortable/scrollable data table, column resizing, or pagination.
- **`GlassSectionRule(_ title:)`** Settings section heading: accent eyebrow + hairline (ink 14%) to the right (`:575-595`).
- **`GlassHairline(_ color:, axis:)`** one-device-pixel rule (`:4-31`).
- **`GlassActionBar(notes:, noteInset:, bar:)`** + **`GlassActionNote`**: the footer row with the CTA; text about the action sits directly above the bar, label type secondary, full width, left-aligned, 20pt above the bar (owner ruling 2026-10-08, plan D-21) (`ActionBar.swift`).

### 4.6 Modal system (`Components/Modal.swift`)

- **`GlassModal(title:, subtitle:, width: .regular|.narrow, closeLabel:, actions: [GlassModalAction], busy:, onCancel:, content:)`** "The replacement for a stock `.sheet`" (`:93-244`). Anatomy: header (title `title` bold + optional caption subtitle tertiary; round small close button; padding 14/10/18/16; `rule` under it), body (caller's), footer (actions right-aligned with 8pt spacing; `rule` over it). Backing: `paneBase` + `paneFill`, radius 16, `paneEdge + modal` shadow. Width 780 regular / 450 narrow (`:78-89`).
- **`GlassModalAction(_ title:, role: .cancel|.standard|.destructive, isDefault:, isEnabled:, isProminent:, id:, action:)`** (`:7-76`). Order: cancel left-most, standard, destructive right-most. Return takes the default action (never destructive, never cancel); `isProminent` draws a standard action as primary with no Return key ("an action that must never be one Return away (an irreversible send)"). Every modal action is `.bar` + `small` (30pt) (`:142-146, 188-206`).
- Presentation: `.glassModal(isPresented:)` / `.glassModal(item:)` + `.glassModalHost()` at the window root (`:386-489`). Modals stack; only the topmost answers the keyboard (Escape = `onCancel`, Return = default); covered content is disabled and hidden from VoiceOver; the modal is a modal container (`.isModal`, `focusSection`); a scrim click cancels (as #1146), except while busy or when the cancel action is disabled. Scrim `modalScrim` over the content blurred by 8; the layer is inset 52 top and 28 elsewhere; fade on `standard` (`:491-546`).
- **`GlassConfirmation(title:, subtitle:, message:, actions:, busy:, onCancel:)`** "The replacement for a stock `.alert` or `.confirmationDialog`": always the regular (780) width, message paragraphs split on blank lines, body type secondary (`:246-305`).
- **`GlassModalBody(spacing:, content:)`** sized to content until it no longer fits, then scrolls (`ViewThatFits`), 14 vertical / 18 horizontal padding (`:307-334`).
- Environment: `glassModalCloseLabel` (set once at the window root from the core's copy), `glassFolderMark` (the folder tile's word) (`:345-358`).

### 4.7 Navigation (`Components/Navigation.swift`, `SectionNav.swift`, `EdgeRail.swift`)

- **`GlassSegmentedTabs<Value>(_ label:, selection:, segments: [GlassSegment], floating:)`** tabs in a well (30 track, 26 items) or the floating variant on the map (control tier, floating, `controlSelectedFloating` without edge); segment ink: `textOnSelected` selected, primary on hover, else tertiary (well) or secondary (floating); a container with the caller's label; each segment `.isButton` + `.isSelected` (`:44-135`).
- **`GlassSegment<Value>(_ title:, value:, badge: Int? | badgeValue: GlassBadgeValue?, dot: GlassStatus?, accessibilityValue:)`** a segment's badge is decisions owed only, "Never queue depth or credit"; `.count(0)` draws none; `.unknown` draws a dash; the dot is colour only, so `accessibilityValue` must carry the words (`:9-42`).
- **`GlassRuleTabs<Value>(_ label:, selection:, segments:, bleed:)`** the main window's tabs ("the Ember Rule", owner choice 2026-10-10): equal-width titles (body, medium/semibold) over a 1pt `rule` that bleeds to the pane edges (`toPaneEdge` 48); the selected tab gets a 2pt `tabEmber` line reaching 30% past the tab each side and a 26pt elliptical `tabEmberHalo`; the ember glides between tabs with a matched-geometry spring (instant under Reduce Motion) (`:137-274`).
- **`GlassBreadcrumb([GlassCrumb], backLabel:, onBack:)`** a bare back chevron (no round container, owner 2026-10-08) with a 26pt target, then crumbs secondary › tertiary separator › current primary (header trait); crumbs turn primary on hover (`:276-359`).
- **`GlassStepProgress(labels:, current:, stateValues:)`** first-run step nodes: 14pt circles (`purpleSoft` with a 3pt 25% ring when done/current, else `wellFill`) joined by 2pt connectors, eyebrow labels tracked 0.6pt (current primary, others tertiary); "Not a tab control: the steps are not chosen, they are reached"; VoiceOver values done/current/pending from the core (`:361-428`).
- **`GlassSectionNavRowStyle`** a modal's section list row (Settings modal's 180pt list): label regular, secondary (primary on hover), ink 8% hover, radius 8, "Never the blue menu selection: the row scrolls a body to its section, it selects nothing" (`SectionNav.swift`).
- **`EdgeRailGeometry`**, **`GlassRailTile(selected:, action:, label:)`**, **`GlassRailHandle`**, **`GlassRailRule`** (`EdgeRail.swift`, section 2.6).

### 4.8 Indicators and status (`Components/Indicators.swift`, `StatCard.swift`, `Feedback.swift`)

- **`GlassStatus`** `.on .ask .off .outside .shared .kept .inference` with glyph colours and text-safe colours (`GlassStyle.swift:26-57`).
- **`GlassStatusDot(_ status:, size: 8, halo:, ring:)`** hidden from assistive tech (`Indicators.swift:3-31`). **`GlassStatusLabel(_ title:, status:)`** "A dot and its label: the only way status is shown" (7pt gap, label type, secondary ink, combined element) (`:33-52`).
- **`GlassChip(_ title:, status:)`** mono pill with an optional 6pt dot, ink = status text colour, 0.5pt ring at 60% (classic) or neutral tint (flat); **`GlassChip(glass:, muted:)`** #1146's glass chip, accent ink on the quiet-card edge (`:54-107`).
- **`GlassTag(_ title:, tone: .neutral|.on|.ask|.outside|.failed|.accent)`** micro-type verdict pill on a tint with text-safe ink; `failed` adds a 1pt outline so it is "never colour only" (`:109-140`). Examples: Contributed, Under review, Taken back, Drafts.
- **`GlassBadge(count: Int?, subtle:, label:)`** decisions owed; red `badgeFill` with dark `textOnStatus` count (16pt min), or subtle ink-16% inside a tab (14pt); cap `99+`; nil draws "—"; VoiceOver reads the caller's label (`:142-181`).
- **`GlassTool`** (`.claudeCode .codex .antigravity .geminiCLI .cline .openCode .theia .other(initials:)`), with tint, logo and two-letter initials (`:183-229`). **`GlassToolTile(_ kind: .tool|.folder|.session|.add|.folderInitial, large:)`** 22pt (30pt large) tile; logo 15 (20) in the tool's tint on ink 10%; folder = white `folder.fill` on `tileFolder`; folder initial in `tileFolderInk`; session "▤" in `statusOff`; hidden from assistive tech (`:231-316`). **`GlassToolLogoShape(_ id: GlassToolLogoID)`** vector logos for Claude, Codex, Antigravity, OpenCode, Theia (`Logos/GlassToolLogo.swift`, paths in `GlassLogoPaths.swift`); Gemini CLI and Cline have no artwork.
- **`GlassLegendCell(_ label:, value:, status:)`** a 28pt well pill: haloed 8pt dot, label shrinking to 85% then truncating, tabular semibold value (`Containers.swift:439-477`).
- **`GlassStatCard(_ label:, value:)`** eyebrow label (wraps at spaces, 2 lines) over a heading-bold tabular value, 10/12 padding, card tier (`StatCard.swift:3-41`).
- **`GlassAlert(_ text:)`** a failed request's line: caption in `statusOutsideText`, no frame, under the buttons it is about (Ron 2026-10-09: a boxed alert "read as a disabled text field") (`StatCard.swift:43-61`).
- **`GlassNotice(tone:, title:, content:)`** a notice on a quiet card; the title carries the tone as a status dot; the body stays in text colours (`Containers.swift:597-627`).
- **`GlassSpinner(_ label:, size: 12, standalone:)`** 12pt ring, 1.5pt, quarter arc turning every 0.8s; native indeterminate `ProgressView` to assistive tech; hidden when unlabelled unless standalone (`Feedback.swift:3-59`). No determinate progress bar component exists.
- **`GlassSkeleton(width:, height: 12)`** ink-8% bar, radius 8, pulsing to 0.5 over 1.6s; hidden from assistive tech (`Feedback.swift:61-101`). Spec intent: "a loading state per `ScreenState`, drawn as a dash, never as zero".
- **`GlassWarningGlyph(_ label:, size: 12)`** #1146's 16-unit triangle (1.4 stroke) replacing the SF warning symbol "so it matches the other shells" (`Feedback.swift:103-158`).
- **`GlassGlyph`** #1146's own glyph artwork: `viewMenu`, `graph`, `map`, `inspector` (14x12 toolbar glyphs, 1.3-1.4 stroke), `gear` (15pt), `chevronDown` (10pt, 1.8 stroke), `folder` (13pt), `kebab` (filled 4x14); decorative (`Glyphs.swift`).

### 4.9 Charts and map primitives

`GlassBarGraph` + `GlassBarBucket` + `GlassBarSlide`; `GlassMapField` / `GlassMapStage` (field, tiled NEAR AI marks, shimmer, pointer light); `GlassNodeCard(_ title:, detail:)` (260 wide floating); `GlassMapNodeStyle(.active|.idle|.outside|.hub)` (fill, ring, radius) for the app's `Canvas` flow map; `GlassFloatingGroup(spacing:, content:)`. Details in section 2.13.

### 4.10 Menu-bar panel parts (`Components/MenuBarPanel.swift`, "R13 of #1173")

- **`GlassStatePill(caption:, value:, systemImage:, fill: GlassPillFill, expanded:, action:)`** a 44pt control-tier pill (radius `menuStatePill` 22) with a 31pt filled circle (`.solid(color)` or `.mixed`, an angular gradient of the three mode colours) and a white 14pt glyph; expanded it shows caption (micro) over value (bodyStrong); the row expands the hovered pill and collapses the others (`:31-87`).
- **`GlassSubListHeader(_ title:, closeLabel:, onClose:)`** 44pt back-chevron header that replaces the pills while a sub-list is open (`:91-124`).
- **`GlassOptionRow(_ title:, sub:, fill:, checked:, action:)`** check column (16pt), 24pt colour circle, title body-medium + caption sub-line, ink-10% hover, radius 8 (`:126-184`).
- **`GlassDayGraph`**, **`GlassMenuBarStrip(columns:, condition: .live|.paused|.attention|.unavailable, badge:, mark: .none|.news|.ready)`** (section 2.13; "A strip never draws a dead or unknown core as healthy", `:300-313`).
- **`GlassActivityRow(tool:, text:, trailing:, action:)`** 18pt tool tile, body text, optional trailing word in `menuNoProof`; hover blue fill + white text (`:447-502`).

### 4.11 Brand marks (`Logos/`)

- **`GlassTraceMark(ink:)`** the Trace product mark "1c Live trace" (owner's Claude Design project): a 3x3 diagonal lattice in a 200-unit box; five visited nodes (radius 10) joined by four necked joins, filled with a linear gradient `traceLiveStart` #5b14ff → `traceLiveMid` #b412c4 → `traceLiveEnd` #ff0a6c from (68,68) to (134,134); a radial glow (radius 30, #ff0a6c 55% at 0.3 → 0) on the current step; four unvisited nodes in `purple` #6d14f3; `ink:` draws it solid in one colour (the edge rail icon, owner 2026-10-12); decorative (`GlassTraceMark.swift`).
- **`GlassBrandMark`** the NEAR AI "N" mark path from the brand kit (`Tertiary/02_White & Color/tile-white-color.svg`), used only as the faint map-field tile (`GlassBrandMark.swift`, `Indicators.swift:713-720`). Note the macOS spec says "The app shows no near.ai logo or lockup ... without near.ai's written permission" (spec "Copy and third-party marks"); for a NEAR AI parent system this rule needs re-deciding.
- **`SVGPathData`** a small SVG path parser used by every mark and glyph (`Logos/SVGPathData.swift`).

## 5. Screen and pattern catalog (the app's views)

Paths in this section are relative to `macos/Sources/TraceCommonsApp/` unless noted. `MWV` = `Views/MonitorWindowView.swift`, `M/` = `Views/Monitor/`, `ER/` = `Views/EdgeRail/`, `App` = `TraceCommonsAppMain.swift`. Two architectural rules shape every screen: **all copy comes from the Rust core** (`MonitorWords.table`, `M/MonitorWords.swift:12-29`; a missing word renders as an empty string, never a Swift fallback), and **fail closed** ("an absent signal never renders as healthy. A dot, a tag or a count with no core answer is absent or '—', never 'on', never zero", R15 plan Global Constraints).

### 5.1 Scene inventory and window chrome

| Scene | Definition | Chrome and size |
|---|---|---|
| Monitor (main window, release default since R15) | `Window("Monitor")` (`App:175`) | `.windowStyle(.hiddenTitleBar)`, `glassWindow()` (transparent, full-size content, traffic lights inside the main pane), default 1193 x 614, `.windowResizability(.contentSize)` |
| Menu bar | `MenuBarExtra { MenuBarGlassPanel } label: { Launcher }`, `.menuBarExtraStyle(.window)` (`App:83-93`) | 380-wide panel (literal, `M/MenuBarGlassPanel.swift:39`) |
| First run | `Window("First run")` (`App:118-126`) | hidden title bar, default 860 x 760, painted scene backdrop, 450-wide pane |
| Settings | `Window(settingsTitle, id: .settings)` (`App:128-141`) | standard title bar, default 780 x 640, min 540 x 420; "in a window of its own beside the Monitor (owner, 2026-10-08), no longer a modal over it" |
| Edge rail | borderless `.nonactivatingPanel` `NSPanel`, level `.statusBar`, joins all spaces (`ER/EdgeRailController.swift:143-160`) | 4 x 240 closed / 484 x 680 open; off by default, enabled in Settings > General |
| Menu-bar preview (debug) | `Window("Menu bar")` | |

Every scene sets `.tint(purpleSoft)` and `.focusEffectDisabled()` (`App:86-88, 108-110, 121-123, 135-137, 189-191`). Keyboard: Cmd-1/2/3 Home/Inference/Traces, Cmd-Shift-M Private AI (opens only; never writes "on"), Cmd-, Settings (`App:223-296`).

### 5.2 Monitor window: navigation model

- **Three floating panes** (`GlassThreePane`, section 2.6): main (440, always shown, holds navigation), map (flexible, content layer), inspector (293). Map and inspector are toggled independently from a toolbar capsule; the window grows/shrinks to the right. Pane visibility, tab, map mode, graph footer, ignored-folder filter, selection and Home sub-page persist per window with `@SceneStorage` (`MWV:71-93`).
- **Main pane top row** (`MWV:648-700`): trailing `GlassToolbarGroup` of four `GlassToolbarButton`s using #1146 glyphs (View menu `expanded:`, Graph, Map, Inspector `pressed:`), then a 28pt round gear button for Settings; 78pt leading clearance for the traffic lights; vertical centre on the lights is a literal 26 (`MWV:624`). The View menu is a 250-wide `GlassMenu` with one checked item ("Show ignored folders").
- **Notices and gate** above the tabs: `ShellNotices` (5.8), then the `MonitorGate` triad: `.down` (refused-startup banner), `.signedOut` (`GlassNotice(.ask)` + open-first-run button), `.awaiting` (`SettingsAwaiting` replacing content) (`MWV:704-739, 770-774`).
- **Tabs**: `GlassRuleTabs` (ember rule) Home / Inference / Traces, `bleed: .toPaneEdge`; Traces carries the decisions-owed badge (or a dash) and an amber dot when the queue shield needs attention; Inference carries the Private AI listener dot; each has an `accessibilityValue` in words. Before onboarding only Inference shows (`MWV:40-49, 717-730`).
- **Sub-navigation** inside Home uses `GlassBreadcrumb` (Home > History / Missions / Insights / Mission drafts; Escape goes back) (`MWV:507-522, 743-748`).
- **Inspector demand**: keyed events (undo, contributed, kept, folder submit, review) auto-open the inspector; nothing auto-closes it; selecting a session or opening a History row opens it, selecting a folder does not (`MWV:311-323`, `M/MonitorShell.swift:46-66`). The inspector is available only on Traces and Home > History.
- **Map pane** (`MWV:781-900`): `GlassPane(isContent: true, edge: mapEdge)` + `GlassMapStage`; a floating `GlassSegmentedTabs` (Traces / Private AI, the latter only once the core names it) inset 14 in a `GlassFloatingGroup`; an error line on a floating node-card surface pinned bottom-leading; the Inference tab switches the map to Private AI, Traces to Traces, Home leaves it.

### 5.3 Traces tab (`M/TracesViews.swift`, `TracesTree.swift`, `TracesStore.swift`, `NudgeViews.swift`, `MonitorShell.swift`)

- **Purpose**: the folder > session tree of local traces waiting for a decision (no tool level in this tree).
- **Regions**: a prompts shelf capped at 45% of the pane (folder notice, health banners, inspector prompts, nudge cards, offer cards), list controls (title, idle-filter tag + clear link, a `GlassIconMenu` order picker Suggested/Queue), the tree, and an optional graph footer (206 tall, `GlassLegendCell` pair, `GlassBarGraph`, a pill row ‹ binoculars − range + › now; ranges 24h in 2h buckets, 11 days, 42 days).
- **Rows**: `GlassListRow` folder rows (sub-line: mode word + "N sessions waiting"; Submit pill only when the core offers it, removed rather than disabled; row menu is a floating pill offset (-6, 38)); session rows (title = time, sub = size and state, `flag` ask/on, Review pill, Dismiss in the row menu behind a confirmation modal; nudge tags under the row with an info popover 260 wide).
- **Keyboard**: the tree is one focusable element (no ring); up/down move, left/right collapse/expand, Return opens review, clicking the selected row deselects (back to Summary); VoiceOver focus follows the selection (`@AccessibilityFocusState`).
- **States**: loading = a text line "Reading local queue..." (deliberately no spinner, matching #1146); empty = `tray` glyph 22 + bodyStrong title + caption; failed load keeps the last tree and adds a core-down banner; per-row write errors as captions; `writing` disables controls.
- **Confirmations**: mode change via `GlassConfirmation` (Ignore = destructive; Arm = default); Dismiss session via `GlassModal` (Keep = cancel, Dismiss = destructive, refusal shown inside the modal as a `GlassNotice(.outside)`).

### 5.4 Inspector views

- **Pattern**: `InspectorHeader` (optional large tool tile + heading bold one line + caption tertiary) and `InspectorSection` (quiet card + `GlassExpander`, collapsible or static) (`M/TracesInspectorHost.swift:93-159`); content scrolls in `GlassPaneInsets.inspector` (16/18) at `cardGap` 10.
- **Summary** (nothing selected): header with counts, Shared/Kept legend, Decisions section (SF Symbol lines), statistics (top projects/tools), safeguards eyebrow card, certificate section, "not offered" disclosure; unknown counts are "—"; pending credit only beside the commons' condition sentence (`M/SummaryInspector.swift`).
- **Folder inspector**: header, legend, key-value project facts, contribution-rule `GlassPicker`, decisions with `GlassSplitButton` "Submit all" / "Submit all as" (a narrow `GlassModal` with Worked / Partly / Failed) and an Ignore link (`M/ToolFolderInspectors.swift`).
- **Session review card** (`M/SessionReviewCard.swift:61-654`): the review lives in the inspector, not in a sheet. Preview body (enrolment chip, heading, opening prompt on a quiet card limited to 8 lines, measures, redactions with tooltips, "still present" notice, surviving-secret label, residual risk, consent scopes, eligibility, verdict `GlassRadioRow` Worked/Partly/Failed with an optional text area max 140 tall and an n/max counter). Actions: scrubbing caveat above the buttons, then `ViewThatFits` row: Contribute (`.primary`, small; disabled with a `.help` reason unless the core is answering, the preview is enrolled, consent words are present, the session is eligible and the full review was shown), Dismiss link, Look inside link, Keep link; refusals as `GlassAlert` under the buttons. The preview is requested after a 300ms settle.
- **History detail**: status tag, defects notice, explanations, and the legacy `SessionDetailView` embedded.

### 5.5 Home tab (`M/HomeViews.swift`, `HomeStore.swift`)

- **Overview**: prompts header; **status card** (interactive card: ringed status dot + bodyStrong status line + secondary waiting line aligned under the words via a custom alignment guide + chevron; the same component appears in the edge rail); **three `GlassStatCard`s** (Waiting, Contributed, Credit pending) with a condition caption; **Missions card** (`GlassIconCard` `sparkles`, promo treatment `spotlight`, chevron, accessory tag, up to 2 draft rows); **History card** (`clock.arrow.circlepath`); hosted Insights (`chart.xyaxis.line`) and mission catalogue (`list.bullet.rectangle`) cards.
- **History page**: description, failure notice, nudge/offer cards, stats, community card (4-cell grid between hairlines), Submissions card (eyebrow + title + refresh link), filter pills (custom wrapping flow layout; selected = `controlSelected` + `textOnSelected`), groups by project (PROJECT eyebrow), rows with `ViewThatFits` (three layouts: inline actions, stacked, below), Open (`.glass`) and Withdraw (`.destructive` -> `WithdrawalConfirmationModal`), both forced to `minHeight: 44`; list states: "Reading history..." or a spinner, empty, filter-empty, a cap line at 100 rows; credit card, held-for-review card, period key-value card.
- **Store states**: per-method failures; a failed read keeps the last value but views gate on freshness and show a dash.

### 5.6 Inference / Private AI tab (`M/InferenceViews.swift`, `InferenceAccount.swift`)

Content by startup state: `.needsRoots` embeds onboarding at 450 wide; `.starting` shows `SettingsAwaiting`; `.refused` a health banner; `.running` the ledger: prompts, `PrivateAIInspectorView` (status / credential / connected-tools fact rows with a dot, plus a Connected/Not connected legend), ledger sections (totals as 3 legend cells Calls/Verified/Priced; models eyebrow card with proof `GlassTag`s: verified = on, pending/gateway-only = ask, failed = failed, outside = outside; calls table with mono time column), then the account section (managed sessions, balance icon card with refresh, funding row, settings link card). The inspector is always closed on this tab.

### 5.7 Menu-bar glass panel (`M/MenuBarGlassPanel.swift`, `MenuPanelStore.swift`)

- **Surface**: inside `MenuBarExtra` the panel draws one pane tier (radius `menuPanel` 14/16) and masks the system's own `NSVisualEffectView`s so there is one glass layer ("glass on it is glass on glass (R14)"); it re-pins its top edge to the menu bar (`:506-681`).
- **Layout** (380 wide, 10 padding, 8 spacing), top to bottom: three `GlassStatePill`s in a 44-high row (Contribution mode `bell` with mode colours or mixed; Watching `eye`/`eye.slash` in `blue` or `menuPillOff`; Private AI `arrow.left.arrow.right` in `dataShared`) that expand on hover (`reveal` 0.18); or a sub-list (`GlassSubListHeader` + `GlassOptionRow`s on a card) swapped in with `slide`; a nudge row; Shared/Kept legend; `GlassDayGraph` (36 days); an Insights glance card (fresh data only); recent activity (up to 3 `GlassActivityRow`s); hairline-separated menu rows (Flagged · N; Open app, Manage rules, Settings, Quit) in `GlassMenuRowStyle`.
- **Behaviour**: values never read "On" unless the daemon confirms; mode override rows are disabled until the core can apply them and show an inline confirmation (not a modal; "sheets there are unreliable"); pause durations (hour, morning, indefinitely) in the Watching sub-list; the event stream resubscribes after 5s; the glance re-reads every 60s while open.
- **Status item**: `GlassMenuBarStrip` rendered to an `NSImage` via `ImageRenderer` (non-template), with an accessibility label and `.help` from the core (`:686-767`).

### 5.8 Edge rail (`ER/EdgeRailController.swift`, `ER/EdgeRailView.swift`)

An OS-level, off-by-default glanceable surface on the screen's right edge (design "Run 1 OS-level Explorations, 1b"; #1381 "compact tab summaries"). Hovering the 4pt zone opens it; leaving starts a 300ms grace before closing; hovering a tile selects its peek. The rail is a 56-wide pane of 44pt tiles (`house`, `shield`, the Trace mark at 30, a rule, then the app tile at 30); the peek is a 380-wide pane with a heading, content and an "Open X ->" link plus a "nothing sent" caption. Peeks: Home (status card, 3 stat cards, Missions/History icon cards), Private AI (fact rows, totals card with a 110-high calls bar graph, balance card), Traces (place rows, watcher label + Pause/Resume, the first 3 folders as list rows, a 110-high graph). Its only write is pause/resume; everything else opens the app. Animated with `slide` on the token curve (opacity only under Reduce Motion); the handle has an accessibility action to open.

### 5.9 Settings (`M/SettingsModal.swift`, `Views/Settings/**`)

- **Frame**: header (title bold, subtitle, Watching/Paused `GlassChip`), rule, then two columns: a 180-wide nav list (`GlassSectionNavRowStyle`, disabled "—" placeholder when a name has not loaded) and one scrolling body with every section introduced by `GlassSectionRule`; nav clicks scroll the body; pane fill `paneOpaque`; Escape closes. Gated by the same awaiting/down/signedOut triad.
- **Sections** (15 cases, 13 listed): General (Appearance as `GlassSegmentedTabs` Light/Dark/System applied immediately; edge-rail toggle), Connection, Startup (+ Notifications, Updates), Watching, How traces may be used (consent checkboxes, "required" tag, disabled until the daemon answers), Public profile (opt-in, handle, bio with a /280 byte counter, a go-public modal whose acknowledgement checkbox gates a prominent non-default action), Watched folders, Tools (+ Insights settings card), Private AI (route disclosure), Redaction witness, Projects (per-project `GlassPicker`; arming confirmation default; ignore-with-waiting destructive), Changes on this machine (audit log rows), Compute. Each is built from `GlassEyebrowCard`s inside a column padded 20/12 (`Settings/GlassSettingsContent.swift:11-41`).
- **Read-state rows** (`Settings/SettingsStateRow.swift:26-108`): awaiting -> standalone spinner; failed or core down -> unavailable line + Retry (only when failed); answered -> content.

### 5.10 First run / onboarding (`Views/FirstRun/**`, `OnboardingCoordinatorView.swift`, `M/FirstRunViews.swift`)

- **Window**: painted radial scene (`sceneWarm` -> `sceneBase`, radii 40 -> 900), `ShellNotices` above a 450-wide pane, 30 vertical padding, min 530 x 640. No logo, mark or hero art (D-16 replaced the community-brand hero with a `display` headline).
- **Flows**: Quick (Join -> Folders -> Uses) and Custom (Join -> Tools -> Rules -> Uses); Quick's Folders step offers "Customize" (`TCShellCore/FirstRun/FirstRunNavigation.swift:7-12`). Decision D-3: Folders before Join on a fresh macOS install because the daemon needs session roots first.
- **Step frame** (`FirstRunFrame`, `FirstRunFrame.swift:139-246`): `GlassPane` (12 padding, 16 spacing) > `GlassStepProgress` > header (two-weight `display` title, light half + bold half, inset 20) > scrolling cards (12 spacing, inset 20) with the step failure as an unboxed `GlassAlert` after the cards > optional pinned zone (add tile) > `GlassActionBar` (notes above at a 20 gap; Back `.glass .bar` left; Customize `.glass .bar`; Cancel `.secondary .bar` only while a browser sign-in waits; primary CTA right with an inline spinner when busy; a disabled CTA explains itself with `.help`).
- **Join**: invite card (field + Look up; five status states), passkey and NEAR AI account cards (eyebrow + line, action that becomes "done" `GlassStatusLabel(.on)`, undo with `arrow.uturn.backward`); action note "doesn't authorize any data sharing" above the bar; CTA "Skip" or "Continue".
- **Folders / Tools**: answer rows (30pt tool tile, name + home-relative mono path with full path in `.help`, `GlassPicker` "Choose..." with Watch = on dot / Don't use = off dot, folder button; Download for uninstalled tools); a dashed add tile (1pt `[4,3]` ink 28%, purple when a folder is dragged over; accepts drops); loading/failed/found states; discovery re-runs when the app becomes active.
- **Rules**: repos card with per-row mode pickers (Automatic requires a `GlassConfirmation`; "never written silently"); past-sessions card with mixed-state checkboxes per folder, expanders, show all/fewer link.
- **Uses**: consent scopes (required scope ticked and locked + info button + "required" in mono `statusOnText`; optional scopes behind a mixed checkbox); Sharing card (Ask me / Automatic picker, disabled until the grant copy is read); Private AI card (Custom only, settings toggle); on Start, a disclosure sub-flow of `GlassModal`s (scrub -> witness) whose Continue is `isProminent` but not default, so it never answers Return.
- **Passkey popups** (P-1 Choose, P-2 Name, P-5 Verify, P-7 Welcome back; `PasskeySheets.swift`): presented with `.glassModal` but drawn with their own pane surface at 380 wide (not `GlassModal`): a 52pt tinted icon circle, centred heading/display title, 40-high block buttons, a 44-high name field with an 18pt clear button, validation shown only after the field is touched (non-empty, at most 64 Unicode scalars), round Back/Close corner buttons.

### 5.11 Review sheet "Look inside" (`Views/PreviewSheet.swift`)

Read-only ("Exactly what would be sent"); footer is Close only; approve/decline live on the inspector card. Presented as `PreviewModal` (a `GlassModal`) or a pane-tier sheet at 760 x 620. Header: eyebrow, title, description, gate statement, a sizes quiet card ("would send X · on disk Y", monospaced digits), send disclosure (sizes, routes, certificate in mono), native review (Prepare admission, Request witness review). Content states as centred `GlassNotice(.ask)` at max 480 wide. Tabs (`GlassSegmentedTabs`, 4): Transcript (virtualized chunks on a flush quiet card, Copy everything, Load more, optional turn separators), Search original (count check), Turn index, Search (field auto-focused and on Cmd-F, recents as links, a three-state result label, up to 20 mono snippets with 120 bytes of context). Redaction marks (`<PRIVATE_*>`, `[REDACTED*]`) render as inline bold-mono chips on `controlSelected` with spoken labels; search highlight is `statusAsk` at 32% (no token). Witness consent is a `GlassModal` whose Confirm is prominent-not-default and enabled only after a `GlassCheckRow` tick.

### 5.12 Detail, withdrawal, skills

- `SessionDetailView` (breadcrumb at 44 min height; read states beside held data, "a reload does not replace it"; `PublicRunEditor` in published / editor / review modes, with field counters "n/max" and hardcoded limits title 100, outcome 600, instructions 4000; evidence capped at 4; a hand-built radio list).
- `SessionContributionOverview` (four eyebrow cards; **Withdraw** with an inline confirmation in a `GlassWell` (Keep `.cancelAction`, Confirm `.destructive`, both 44 min) or the `WithdrawalConfirmationModal`; outcome label or alert + Try again; all words from `WithdrawalCopy.swift`).
- `ScrubbingCaveat` (one canonical sentence used in three places: a note, an at-commit status label, a row status).
- `SkillLearningView` (staged flow idle -> candidate -> reviewed -> evaluated -> planned -> installed; validation debounced 150ms; rollback via a destructive `GlassConfirmation`; plan D-7 placed it in the History inspector).

### 5.13 Insights (Home-hosted; `Views/Insights*.swift`, `Comparison*.swift`, `MissionDraftsView.swift`)

`GlassSegmentedTabs` Overview / Patterns / Sessions / Analyze (max 480 wide, 24 padding). Overview: title + week `GlassSelect`, three interactive stat cards (min 120 tall, title-type figures with monospaced digits, not `GlassStatCard`), recap and lever cards (primary small + "Turn off"/"Not useful" links), a Swift Charts stacked `BarMark` tokens-by-day chart (220 tall; series uncached = `textPrimary`, cache read = `accentText`, cache write = `accentText` at `chartSeriesReduced` 0.75, output = `textTertiary`), share bars (6pt capsule in `tintNeutral` filled `accentText`, a 2 x 10 best-week tick), a 320-wide breakdown card, drill-down tables with 90pt columns. Patterns: 220-tall pattern cards, a 48-tall axis-less weekly bar sparkline at 75%, goals. Sessions: stacked bars per turn, a dashed `[4,3]` `RuleMark` threshold in the outside text colour, lettered point markers; chart hidden from accessibility with a 320-wide column of marker cards as the text alternative. Analyze: a long form with `GlassSelect`, file importers, three native `DatePicker`s (TCDesign has none), episodes, comparison tasks (8 text fields + 2 selects), specifications, cards, snapshots. Owner decisions recorded here use a separate D1-D8 namespace (section 1.3). Insights is the most drift-heavy area (literal 24/16/12/8/6/5/3 spacing; errors as plain text rather than `GlassAlert`).

### 5.14 Other account surfaces

Managed sessions (three `GlassIconCard`s; account rows with kebab -> popover `GlassMenu`; narrow modals for add account / launch / rename; remove via destructive confirmation; polls every 10s), harness list (Connect `.glass`, Disconnect `.destructive`, narrow preview/exposure modals with default Confirm and `busy:`), Private AI switch card (settings toggle disabled when the state cannot be read), credential section (polls every 2s while sign-in pending), funding row, balance row (`TypeScale.number`), Compute (Resume, Pause, Disable all `.glass`; "Disable is not destructive"; plan D-8).

### 5.15 Shell notices (`Views/ShellNotices.swift`)

One notice stack shared by the Monitor's main pane and first run: a scroll capped at 320pt; a "Dismiss all" link when two or more can be acknowledged; cards are `GlassNotice`s (attached daemon `.off`; grant voids `.ask` with heading, bullets, re-arm sentence, primary action + acknowledge link, `GlassAlert` refusal; arming rewordings; gate held with per-project "Ask first" buttons and no dismiss; first-run notice; legacy migration notice and offer with an invite field and a Move button hidden, not disabled, when unusable). Notices never tint the card; tone is the title's dot.

### 5.16 Cross-screen patterns (the reusable vocabulary)

1. **Floating three-pane window** with a fixed main pane, fixed inspector, flexible content pane, window growing to the right; first-launch breakpoints 1100/900.
2. **Inspector demand** (events open the inspector; nothing auto-closes it).
3. **Inspector header + collapsible inspector section** (quiet card + expander).
4. **Shared/Kept legend pair** (two `GlassLegendCell`s) reused in 6+ places; generalises to 2-3 metric legend cells.
5. **Status card** (dot + two aligned lines + chevron, whole card is a button).
6. **Icon card as navigation link** (`GlassIconCard` + chevron), optionally as a promotion.
7. **Undo bar card** (eyebrow/title/live "approved Ns ago" detail on the left; Undo glass button bound to Return + Dismiss link on the right). This is the app's toast equivalent: there are no transient toasts; the approval/undo region is a persistent card (spec "The approval and undo region": a single instance at the top of the inspector, or the bottom of the left pane when the inspector is closed).
8. **Notice** (`GlassNotice` with tone dot, body, primary action + acknowledge link, alert underneath), **health banner** (notice with no action), **inline alert** (`GlassAlert` directly under the control it refers to).
9. **Offer card** (eyebrow, evidence, question, body; Accept glass then Decline link; optional close X counting as decline).
10. **Action ordering**: the action first as a primary/glass button, then decline/dismiss/secondary as `.link`, then the failure line under both ("Ron, 2026-10-09").
11. **Confirmation ladder**: reversible confirm = `isDefault` (Return); destructive = right-most, never default; irreversible send/consent = `isProminent` (looks primary, no Return); checkbox-gated confirm for consent (witness review, go public, admission); inline well confirmation where sheets are unreliable (menu bar) or in-place (withdraw).
12. **Empty / loading / error / unknown**: loading is a text line or a spinner + line (never `GlassSkeleton`, which is unused); empty is the core's sentence (quiet card or caption, Traces adds a glyph); request failure is `GlassAlert`; section failure is `GlassNotice(.outside)` + Retry; a reload never replaces held data; unknown is "—" or the core's unknown word, never zero.
13. **Gate triad** for any daemon-backed surface: awaiting / down / signed out.
14. **Tree list** with a single tab stop, arrow keys, Return to act, floating row-menu pill.
15. **Floating overlay on content** (`GlassFloatingGroup`: tabs, zoom toolbar, node card, state line) to avoid glass on glass.
16. **State pills with sub-lists** and **menu rows** for compact menu-bar UIs.
17. **Edge rail** (hover zone, 300ms grace, tile peeks, open-the-app links).
18. **Onboarding step frame** with action bar and pinned zone.
19. **Answer row / account card** for setup choices.
20. **Settings section** = eyebrow card + read state + controls + alert.
21. **Review sheet** (read-only "exactly what would be sent", sizes card, segmented tabs, redaction chips, Close-only footer).

### 5.17 Drift found in the views (token bypasses worth fixing before generalising)

- **Two different selection fills**: History rows use `ink(0.12)` while filter pills use `controlSelected` (`M/HomeViews.swift:852` vs `:712-740`); lists elsewhere use `selection`.
- **Two curves for one motion**: the graph footer toggle uses `.easeInOut(0.25)` (`MWV:656`) and `GlassMotion.curve(slide)` (`MWV:758`); the bar-graph step uses a literal 0.45s `(0.4, 0, 0.2, 1)` (`M/MonitorShell.swift:293`).
- **Unknown values**: the window shows a literal "—" while the menu bar uses the core's unknown word and says "never a bare dash" (`M/MenuPanelStore.swift:401-406`).
- **Hit targets**: most controls have no minimum, but History rows, detail views and skill learning force a literal 44 (about 35 call sites, e.g. `SessionDetailView.swift:64...428`, `SkillLearningView.swift:82...631`); there is no hit-target token.
- **Hardcoded white in the flow map** (`M/FlowMapView.swift:100, 172`) stays white in the light appearance; map labels use `.font(.system(size:))` instead of the type scale (`:191, 195`).
- **Hand-rolled controls**: native `DatePicker`s, a native number field in a hand-made well, `Divider()` in place of `GlassHairline`, an SF warning symbol in place of `GlassWarningGlyph`, a radio list built from checkmarks, a reimplemented code block, `.opacity(0)` to hide a card, passkey popups at 380 instead of the 450 narrow modal.
- **Charts bypass the data-series tokens**: Insights charts use text/accent inks; `dataShared/Kept/Inference` are used only inside TCDesign.
- **Missing tokens implied by repeated overrides**: `label.weight(.regular)` (about 20 uses), `heading.weight(.bold)`, `title.weight(.bold)`, `caption.weight(.semibold)`, a 320pt panel width, a 380pt menu-bar width (equal to `edgeRailPeekWidth` by coincidence), 260pt popover width (equal to `nodeCardWidth` by coincidence), a search-highlight colour, a redaction-chip token, an icon-name registry (SF Symbol names are inline strings throughout).
- **Hardcoded user-facing strings** remain in a few files despite the core-owns-copy rule (`PreviewSheet.swift:101, 162, 864...`, `SettingsSections.swift:118-127`).

## 6. Content and voice rules

### 6.1 Ownership: the core owns every word

- "A sentence a contributor reads is composed once, in `crates/trace-commons-contributor`, and every shell reads it" (`docs/superpowers/specs/2026-09-06-shell-copy-migration-design.md:7-9`). Sentences cross the FFI already assembled; counts inflect in Rust ("1 session" / "2 sessions"; a shell never branches on `n == 1`); a chosen sentence crosses as a `_line` + `_tone` pair; English only, no localisation, no server-delivered copy (same spec, :101-110, :273-310).
- Enforcement: `ShellWordingTests` (per-file sentence ceilings and floors; 19 surfaces at zero), `NudgeWordingTests` (28 banned fragments), the FFI copy ratchet `crates/trace-commons-contributor-ffi/tests/swift_copy_surface_is_central.rs` (no pinned core sentence may be a Swift literal; Swift never says "private inference"). Windows and GTK carry the same wording ratchet.
- New consent wording is "DRAFT, NEEDS APPROVAL, listed as sentences and never built" (GP Global Constraints). Do not paraphrase per platform; only sentence case and platform punctuation may be adapted.
- Names: the app is **"Near.ai"**; the commons, account and server are **"Trace Commons"**; "a sentence about where a trace ends up names [the commons], and a sentence about what the device is doing names [the app]" (`crates/.../brand.rs:23-48`). "Private AI" is the destination's name, read from `PrivateInferenceCopy.destination`. "NEAR AI" appears only where the core's copy uses it, and the app shows no near.ai logo or lockup without written permission (GS "Copy and third-party marks"; note the in-app map texture uses the NEAR AI "N", section 4.11).

### 6.2 UI copy guide (`docs/ui-copy-guide.md`, 124 lines; based on PR #1288 and the 2026-10-08 button rule)

1. **Buttons name actions** (CG:9-27): an action verb, or a verb and an object; aim for 1-2 words; longer only when shorter would be ambiguous or misleading; no word limit on explanations or confirmations; never a vague "OK" just to shorten. Examples: "Keep on this Mac" -> **Keep**; "Request server refresh" -> **Refresh**; "Custom setup instead" -> **Customize**; "Send this session for review" -> **Send**; "Move to my NEAR AI account" -> **Move**; "Create comparison task" -> **Create task**; "Save user-reported outcome" -> **Save outcome**. Implemented examples: "For 1 hour" -> "1 hour"; first-run answers **Watch / Not used / Download** with "Download {tool}" as the accessible name and tooltip.
2. **Name what this click does** (CG:29-38): a button that opens settings is **Review settings**; reserve **Turn on** for the enabling action; a notice's **Dismiss** must not reuse the session-decline **Not this one** (separate copy keys); prefer the user's action over machinery.
3. **Move essential context beside the action** (CG:40-53): Load more -> "{size} remaining"; Save -> "A saved specification cannot be changed."; Skip -> what skipping sets up; Send -> destination and scope. Consequences, immutability, scope, consent and destructive effects belong in nearby copy or the confirmation; "a tooltip or accessibility name alone is not adequate". (This is the copy-side twin of D-21's action notes.)
4. **Titles and buttons have separate jobs** (CG:55-69): "Create new passkey" / **Create**; "Launch managed session" / **Launch**; "Clear episode assessment" / **Clear**; distinct keys even when the visible labels match.
5. **Repeated controls must be distinguishable to assistive technology** (CG:71-79): the accessible name includes the visible action plus its object ("Save episode assessment", "Refresh saved specifications"), wired into each shell's accessibility API.
6. **Navigation names things; choices name values** (CG:81-88): sections are noun phrases ("Data uses", "Change log"); the heading equals the nav label; duration choices are values ("1 hour", "Until morning", "Until resumed").
7. **Update references when a label changes** (CG:90-96): "Choose Verify account", "Choose Refresh"; search hints, confirmations, accessible names, fixtures, tests and docs.
8. **Keep shared copy shared** (CG:98-107): edit the owning Rust table and update macOS, GTK and Windows consumers; no shell-local prose; keep old payloads compatible.
- Review checklist (CG:109-124): 1-2-word actions, clear target, consequences visible, separate keys, distinguishable accessible names, headings match, all consumers updated, ratchets run; report unexercised platforms; never raise wording baselines to hide prose; never imply an approval that has not happened.

### 6.3 Voice and tone (from the specs)

- **"Direct, and centred on proof rather than promises."** No sentence may promise privacy or security; consent copy always comes from the core (GS "Copy and third-party marks").
- **"Never name the mechanism. Always state the data consequence."** Banned internal words include "privacy filter", "claim", "ingest", "canary"; say "your queue is safe" or "nothing has been lost" (`.../2026-08-08-contributor-shell-shared-design.md:508-511`).
- **Concede imperfection first**: "It is good and it is not perfect — which is why you look before anything is sent."; "Nothing matched a pattern. That is not the same as nothing being there." (`.../2026-08-17-desktop-clients-design.md:474`; `plans/macos-design-pass-report.md:124-129`).
- **Core promise**: "You decide what gets contributed. Nothing is sent unless you say so." (shared shell spec :56-73).
- **Honest limits and timers**: never state a turnaround you cannot honour ("Typical wait: we don't have a reliable number yet."); undo counts **up** from a real instant ("approved 12s ago"), never down to a deadline the app cannot see (`plans/macos-consent-moment-report.md:114-140`; `InspectorPrompts.swift:176-179`).
- **Titles are full sentences with terminal punctuation** in state copy ("Nothing is waiting.", "The watcher isn't running.") (desktop clients spec :1912-1916).
- **Trust relaxes what may be sent, never what may be said** (`.../2026-09-23-connect-and-forget-consent-design.md:179-184`).

### 6.4 Banned or restricted words

- Private AI / harness surfaces: "ironwire", "proxy", "backend", "route"/"routing", "endpoint", "localhost", "private" (as a promise), "secure", "encrypt", "anonym", "protect", "credit", "earn", vendor names; say a tool "sends its calls here" and this computer "answers" them (`specs/...harness-routing-design.md:261-271`). Consequence: "Manage billing", not "Manage credits".
- "Share automatically" appears nowhere (owner rule); use Ask me / Automatic / Never.
- No consent label begins with "Training"; "PII filter" and "NEAR AI" are never headlined on the scan screen (shared shell spec :161-175).
- Detector keys (`secret:aws access key`) are "detector namespace, not contributor language".

### 6.5 Terminology

| Concept | Canonical words |
|---|---|
| Folder modes | **Ask me / Automatic / Never** ("Never is an absolute exclusion. An Auto override is a grant.") |
| Watch readout | **Watching / Paused** |
| Pause durations | **1 hour / Until morning / Until resumed** |
| Unknown | the core's "Unknown"; an unknown History status is **"Status unavailable"** (terminal, no Withdraw); the badge reads "unavailable" |
| Queue actions | Look inside, Contribute, Keep, Dismiss, **Not this one** (tooltip: "Skips this session only. This project will keep being offered.") |
| Folder actions | Submit all, Submit all as, "Submit all eligible ({n})" |
| Verdicts | Worked / Partly / Failed |
| First run | Quick setup / Custom setup, Customize, Skip (until signed in) then Continue, Start |
| Tabs | Home, Inference, Traces; map: Traces / Private AI |
| Home counts | Waiting (= decisions owed), Contributed (all-time accepted); Credit pending only beside its condition |
| Badge | counts **decisions owed** only, "never queue depth or credit"; capped at **99+** |

### 6.6 Numbers, dates, credit

- Unknown is never zero: "—" or the core's word, never a confident 0; never render "(0 distinct)".
- Credit is "a record, not a currency": no currency symbol, no fiat estimate; projected credit only when labelled ("+20 projected, if the commons accepts it"), never styled like settled credit (#1174, 2026-10-02).
- Session dates in Ron's format ("Sat 12 Sep", "52 min", "1 h 18 min"), read in UTC so a session never shifts a day; Insights uses ISO weeks at the shell's UTC offset ("analysis dates, not work dates").
- Figures that describe what leaves the machine are monospaced; prose never is ("a customs declaration, not a feed", `plans/macos-design-pass-report.md:89-96`).
- Platform idioms: "log in" (macOS) / "sign in" (Windows); ellipses on macOS menu items, none on Windows.

### 6.7 Product stance that shapes copy (`docs/contributor-ux-review.md`)

The UX review argues for "Connect -> consent -> contribute automatically -> earn credits", to "exclude selectively, rather than approve continuously", with review-everything as an optional high-control mode, and an onboarding that ends with "It is running ... and I don't need to think about it again." It proposes the line "We remove private information before anything leaves your machine", which `.../2026-08-31-contributor-trust-by-default-design.md:87-121` explicitly forbids as overclaiming. The current product sits between the two: arming a folder (Automatic) is consent (C&F rev 8 trust model), each folder is Ask me / Automatic / Never, Automatic is never set without a confirmation, and Contribute stays the one irreversible action with no keyboard shortcut.

## 7. Accessibility rules and the tests that enforce them

### 7.1 The stated rules

From the R15 plan's Global Constraints and the #1152 spec (Components, Appearance, Acceptance), with code references:

1. **Contrast floors**: 4.5:1 for all text (no large-text exemption anywhere; placeholders, micro tags and badge counts included) and 3:1 for non-text UI (fills, knobs, glyphs, status dots, strokes). "Hold the WCAG floors" (owner ruling 2026-10-07) is cited at every token raised for contrast: `placeholder`, `textTertiary`, `toolbarGlyphHidden`, `selection`, `destructiveText`, `statusOutsideText`, `switchKnobEdge` (`glass.tokens.json:21-62, 85`). "If a surface fails, raise the glassVeil alpha or pin the glass appearance; never lower the floor" (spec "Materials by OS").
2. **Accent contrast floor**: `purpleText` #c9b3ff is text only; every accent fill/tint uses #6d14f3 or the gradients built from it; white on #6d14f3 ~6.9:1, white on #c9b3ff ~1.85:1 ("the #1178 blocking regression") (spec "Accent contrast floor").
3. **Status never by colour alone**: "Status is carried by a dot and a label, never by a fill" (`GlassStyle.swift:26`); `GlassStatusLabel` "the only way status is shown"; a failed `GlassTag` adds an outline; a segment's dot needs an `accessibilityValue` in words.
4. **Unknown is neither on nor off**; never zero, never "on"; badges draw a dash read as "unavailable".
5. **No component authors words**, including accessibility labels/values/state words; callers pass core copy; native controls are used as `accessibilityRepresentation` so the system speaks state ("expanded", "checked", "mixed", radio-group counts) in the person's language (`Controls.swift:519-523, 805-809, 837-845`; `Forms.swift:162-169, 272-281`).
6. **Custom controls must carry the semantics of the system control they replace** (keyboard: Tab, Full Keyboard Access, Space/Return activation, Escape closes a menu or popover and returns focus; VoiceOver roles; Reduce Motion removes knob slides and transitions) (spec "Components").
7. **Keyboard**: lists are one tab stop with arrow-key selection (not a stop per row) (`ListRow.swift:229-235`); radio groups are one stop with arrows; modals: Escape cancels, Return takes the default (never destructive, never cancel), only the topmost modal answers; Cmd-F focuses search; Cmd-1/2/3 tabs; Cmd-, Settings.
8. **Focus**: spec says "the system focus ring ... not #1146's custom 2px purple ring". As built, the focus ring is disabled at every scene root (owner 2026-10-11) and on `GlassRadioRow`; only flow-map nodes keep it. This is the most serious accessibility conflict (section 9).
9. **Dynamic text**: every type step is a macOS text style so it follows the system text size; controls use minimum heights, not fixed ones, so labels grow (`LargeTextTests`); fixed point sizes only for glyphs inside fixed-size controls.
10. **Increase Contrast / Reduce Transparency / Reduce Motion**: left to the system where it adapts (R14), with explicit token swaps for Increase Contrast and explicit no-animation paths for Reduce Motion (section 3).
11. **Charts need words**: "the bars are a picture, and a picture needs its words (R14)" (`MenuBarPanel.swift:214-216`); each bar bucket is one element with a description; charts hidden from accessibility must be paired with a text alternative (Insights Sessions marker cards).
12. **Headings and grouping**: `.isHeader` on titles, tree depth exposed as heading levels h1/h2 (`ListRow.swift:240-261`), combined elements for rows and cards, containers for notices/menus/modals, `.isModal` for modals.
13. **Tooltips**: every icon-only control has `accessibilityLabel` = `.help` = the caller's label (round, pill-icon, toolbar, folder, kebab, refresh, icon menu).

### 7.2 Contrast methodology (as tested)

- WCAG 2.x relative luminance everywhere (no APCA), ratio `(L1+0.05)/(L2+0.05)`; two different linearisation thresholds (0.04045 and 0.03928) across six duplicated Swift helpers plus Python (`generate.py:364-375`), C# and Rust copies; no shared production helper.
- Glass is composited as plain sRGB alpha-over on solid grounds; the native material is never modelled. Classic text is measured on solid `paneBase` (alpha ignored), `paneOpaque`, `sceneWarm`; classic light uses 11 grounds (`LightContrastGroundsTests.swift:14-32`); classic dark uses 8 grounds for accent fills and placeholders only (`AccentFillContrastTests.swift:48-63`).
- Flat theme assumes a **worst desktop** behind the pane: #333333 for flatLight ("which light Liquid Glass frosts no darker than") and #FFFFFF for flatDark, then `glassVeil`, then `paneFill` at its most opaque stop, then the card/field fill (`FlatThemeContrastTests.swift:72-82`).
- The spec's Acceptance item ("measured on device over a pure-white and a pure-black wallpaper ... the PR that ships the shell records the measured values") is a manual check with no automated equivalent.

### 7.3 Test inventory (rule -> test)

| Rule | Test (file:line under `macos/Tests/` unless stated) |
|---|---|
| Text tokens reach 4.5 on the pane base, dark and light; off rows keep 4.5 and are dimmed by ink, not opacity | `TCDesignTests/TextContrastTests.swift:15,30,43` |
| Every text ink (incl. high-contrast and status text) reaches 4.5 on 11 light grounds and on its own tint; white reaches 4.5 on every light CTA/checkbox stop; badge count 4.5; menu hover text 4.5; IC strokes 3:1 | `TCDesignTests/LightContrastGroundsTests.swift:37-142` |
| Colours resolve per appearance; status/data colours 3:1 on `paneOpaque`; no dark-only translucent white | `TCDesignTests/LightAppearanceTests.swift:14-75` |
| Accent fills (toggles, selection, checkbox and CTA stops) reach 3:1 against their ground, both appearances; **known failure**: dark `checkboxOnFill` and `ctaFill` stops at 1.56-2.84:1 wrapped in `XCTExpectFailure` | `TCDesignTests/AccentFillContrastTests.swift:25-114` |
| Switch knob 3:1 on every on-track; knob always white; watch switch purple because white on green < 3:1 | `TCDesignTests/SwitchContrastTests.swift:11-38` |
| Selected-row ink 4.5 on `selection`; sub-line solid white; selection keeps blue's hue (+/-1 degree) | `TCDesignTests/SelectionContrastTests.swift:13-29` |
| Toolbar glyphs 3:1 on every control-fill stop, lit glyph 4.5 | `TCDesignTests/ToolbarGlyphContrastTests.swift:13-42` |
| Flat theme: 9 text tokens 4.5 on pane/card/quiet card/field over the worst desktop; `textOnSelected` 4.5 on `controlSelected` | `TCDesignTests/FlatThemeContrastTests.swift:24-115` |
| Reduced chart series (`purpleText` x 0.75) 3:1 in and out of focus, flat light/dark; at least 1.25:1 from the full series | `TCDesignTests/ChartSeriesContrastTests.swift:15-86` |
| Placeholder 4.5 on the field fill over every ground | `TCDesignTests/FormControlTests.swift:29-53` |
| Increase Contrast swaps; RT left to the system (no `accessibilityReduceTransparency` in tier code); floating surfaces painted over blur | `TCDesignTests/AccessibilityTests.swift:18-65` |
| Liquid Glass only for the navigation layer; no `.glassEffect(` callers; floating = blur, in-pane = painted | `TCDesignTests/FloatingLayerTests.swift:9-53`, `GlassMaterialTests.swift:12-76` |
| Pressed = 8% darker fill or 8% wash, never the label, never `.plain`; components author no accessibility words; list row not its own tab stop; Escape counts; one motion curve; stock curves banned in TCDesign | `TCDesignTests/ComponentContractTests.swift:11-142` |
| Spinner turns per 0.8s and stops under Reduce Motion; unlabelled spinner hidden; skeleton pulse nil under Reduce Motion | `TCDesignTests/FeedbackTests.swift:10-44` |
| Info button: hover or pin, real button, label + value, no animation, no `.help` | `TCDesignTests/InfoButtonTests.swift:16-36` |
| Checkbox mixed = two native sources | `TCDesignTests/CheckboxMixedTests.swift:11-31` |
| Controls grow with text (min height), list row >= 40 | `TCDesignTests/LargeTextTests.swift:18` |
| Hover only when enabled, replaces not stacks; disabled 0.45 / 0.55 / 0.7 | `TCDesignTests/HoverStateTests.swift:8-135` |
| Modal order, Return/Escape rules, topmost only, widths 780/450, scrim tap cancels, fade on `standard` | `TCDesignTests/ModalTests.swift:16-149` |
| Action-bar buttons are 34; inline 28; modal bar small | `TCDesignTests/ButtonSizeTests.swift:11-56` |
| Menu-bar graphs never draw unavailable data as activity; menu row hit rect >= 28 | `TCDesignTests/MenuBarPanelTests.swift:10-68` |
| Three-pane geometry 440/440/293, 1193 x 614, breakpoints 1100/900, traffic-light clearance >= 78 | `TCDesignTests/ThreePaneTests.swift:25-200` |
| Edge-rail measures are tokens; selected ink `textOnSelected` | `TCDesignTests/EdgeRailGeometryTests.swift:11-53` |
| Token drift (classic only; themes not compared); brand is #6d14f3; no retired greens; type sizes equal text-style defaults; one fixed-point font call; no hand-drawn 0.5pt hairlines anywhere | `TCDesignTests/TokenDriftTests.swift:41-287` |
| App files (62-file append-only list): no legacy palette, no colour literals, no own materials, every animation mentions Reduce Motion on the same line, no fixed type, every status dot followed by words | `TraceCommonsAppTests/GlassSurfaceRulesTests.swift:14-177` |
| Insights: no stock button styles, declines are links after the action, reduced series uses the token, no literal white/black | `TraceCommonsAppTests/InsightsGlassConventionsTests.swift:12-95` |
| Wording ratchet: per-file sentence counts are ceilings and floors; 19 surfaces must hold zero | `TCShellCoreTests/ShellWordingTests.swift:33-446` |
| Screen-state precedence core down > loading > paused > unknown > ready; a missing signal is never healthy | `TCShellCoreTests/ScreenStateTests.swift:8-56` |
| Menu-bar badge: none at 0 or unavailable, cap 99+, label says "unavailable" | `TCShellCoreTests/MenuBarStatusTests.swift:8-70` |
| Generator: onAccent on accent >= 4.5 in both schemes, shell roles opaque, type sizes match text styles | `scripts/design-tokens/generate.py:66-69, 320-327, 349-392` |
| Windows brand brushes: text 4.5 / lines 3.0 on 5 grounds; HighContrast aliases | `windows/tests/TraceCommons.Interop.Tests/BrandTokensTests.cs:32-270` |
| GTK accent/status text 4.5 on 3 grounds; rules 3; every `tc-` class defined | `crates/trace-commons-contributor-gtk/src/ui/style.rs:619-783`, `css_contract.rs:142-247` |

### 7.4 CI

`.github/workflows/clients.yml` runs `generate.py --check` and the full `swift test` on macos-26, plus a `macos-15-fallback-tests` lane (the only lane where the vibrancy branch runs); Windows and GTK suites run there too. **None of these is a required status check** ("a client regression therefore surfaces on main after the merge", `clients.yml:7-9`). Tauri has copy tests only, no token or contrast tests.

### 7.5 Gaps in enforcement

- The shipping theme is flat but most contrast tests measure classic; flat lacks 3:1 UI checks, well/menu/popover/node-card/map grounds, out-of-focus text and Increase Contrast checks; `TokenDriftTests` ignores `themes`.
- Classic glass composites (veil + pane fill over the real material or desktop) are not modelled.
- No hit-target rule (menu row 28 is the only minimum; 44 is pinned by needle in a few app views).
- No automated VoiceOver traversal, focus-ring visibility or keyboard-reachability audit ("SwiftUI builds no in-process accessibility tree", `TraceCommonsAppTests/ActionNoticeDismissTests.swift:16-18`).
- 38 of about 100 view files are outside the glass-rules allow-list (including `FlowMapView.swift` with fixed fonts and white literals, and `MenuBarGlassPanel.swift` touching `NSVisualEffectView`).
- The stock-curve ban covers TCDesign only; the app's `.easeInOut(0.25)` passes because the same line mentions Reduce Motion.
- Docs and tests contradict on disabled opacities, off rows, Reduce Transparency and the brand colour (flat Light is blue, unchecked).

## 8. Existing cross-platform translations and how they diverge

### 8.1 Summary

| Shell | Toolkit | Glass? | Takes from the JSON | Own palette | Theme handling | Accessibility media |
|---|---|---|---|---|---|---|
| macOS (lead) | SwiftUI + AppKit | Liquid Glass (26) / HUD vibrancy (14-25) | everything (generated Swift) | none | light + dark + classic/flat | Increase Contrast, Reduce Motion (Reduce Transparency left to the system) |
| Tauri web shell, glass branch (`pr1146`, newest on `claude/tc-monitor-frontend-refactor-8ecf22` = `ftux`) | React + hand-written CSS custom properties + Tailwind 4 | CSS `backdrop-filter` (native NSGlassEffectView regions on macOS only, R branch) | nothing (hand-kept fork of the JSON's ancestor) | the #1146 tokens | **dark only** (`color-scheme: dark`) | `prefers-reduced-motion` only |
| Tauri on `main` | React + shadcn ("base-vega") + Tailwind 4.3.3 + Base UI | no | nothing | oklch neutral + indigo, IBM Plex Sans / Source Sans 3 | `.dark` class, System/Light/Dark, "d" hotkey | none found |
| Windows | WinUI 3 (Windows App SDK 1.6) | **no** Mica/Acrylic; opaque brushes | 11 brand/status roles (generated `BrandTokens.xaml`) | warm green-grey "DESIGN-SPEC §2.1" (file absent from the repo) | Light / Default (dark) / **HighContrast** dictionaries | full High Contrast aliasing to system brushes; stock Fluent focus |
| Linux | GTK4 + libadwaita 0.5 | **no**; opaque | 11 roles (generated `brand_tokens.rs` `@define-color` sheets) | same warm green-grey palette | reloads on `adw::StyleManager` dark changes | none (app-priority provider overrides HC themes) |

The generator writes no CSS (`scripts/design-tokens/generate.py:7-14`); D1/D13 froze Tauri ("Tauri gets no generated output", GS "Non-goals").

### 8.2 Tauri glass CSS (#1146 design system, `pr1146:tauri-desktop/frontend/src/design-system/`)

Files: `tokens/colors.css`, `tokens/materials.css`, `tokens/components.css`, `tokens/spacing.css`, `tokens/typography.css`, `glass.css`, `styles.css`, React components (`containers`, `controls`, `indicators`, `list-row`, `logos`, `navigation`, `surfaces`), Storybook `design-system.stories.tsx`.

**Window-tier tokens the JSON dropped** (needed by any shell without a native material):

| CSS variable | Value (dark only) | Source |
|---|---|---|
| `--tc-blur-window` | `blur(30px) saturate(180%)` | `tokens/materials.css:7` |
| `--tc-blur-popover` | `blur(24px) saturate(170%)` | `materials.css:8` |
| `--tc-blur-scrim` | `blur(6px)` (never referenced; the modal scrim uses `--tc-modal-scrim-blur` 8px) | `materials.css:9`; `components.css:35` |
| `--tc-scene` | three radial glows + a 160 degree warm -> base linear gradient: `radial-gradient(60% 80% at 15% 10%, glow-1, transparent 60%)`, `radial-gradient(50% 60% at 85% 90%, glow-2, ...)`, `radial-gradient(40% 50% at 60% 40%, glow-3, ...)` | `materials.css:12-16` |
| `--tc-scene-glow-1/2/3` | #3f6a8a / #6a3f7a / #2f6b5a | `tokens/colors.css:30-32` |
| `--tc-rim-window` | 135 degree gradient of white .7 / .22 / .04 / .03 / .28 / .5 | `materials.css:19-27` |
| `--tc-rim-width` | 1.5px | `materials.css:28` |
| `--tc-shadow-window` | `0 30px 80px rgba(0,0,0,.45), inset 0 0 0 .5px rgba(255,255,255,.06)` | `materials.css:29` |
| `--tc-radius-window` | 22px | `tokens/materials.css:65` |
| `--tc-cta-edge-flat` | the CTA edge without its glow (disabled primary) | `components.css:8` |

**How the web shell styles glass** (`glass.css`): "A card never has backdrop-filter; a pane always does" (`:1-4`). Pane = `background: var(--tc-pane-fill)`, `backdrop-filter: var(--tc-blur-window)` (with `-webkit-` prefix), `box-shadow: var(--tc-pane-edge)`, radius 16 (`:165-174`); popover = popover fill + popover blur + radius 14 (`:178-185`); menu = menu fill + **window** blur (30px, not popover 24px) + radius 12 (`:186-196`); scrim = `--tc-modal-scrim` + 8px blur, fading in (`:227-239`); modal (pr1146) = radius 22, a 1.5px transparent border revealing `--tc-rim-window` through `border-box`, `--tc-modal-fill` in `padding-box`, window blur; the newest branch changed the modal to pane radius 16, pane fill over `--tc-pane-base`, pane edge + modal shadow, no rim (R `glass.css:278-297`). The floating segmented control has its own `backdrop-filter: blur(20px)` literal (`:518-519`), a glass-on-glass breach. On the R branch, `html.tc-native-glass .tc-window--floating .tc-pane` drops the CSS blur and paints the pane fill over `--tc-glass-veil` when the macOS native material is under it (R `glass.css:157-187`; `src-tauri/src/glass.rs`, `native_macos.m:186-200`, `use-native-glass.ts:5-43`; window `transparent: true`, `shadow: false`, `macOSPrivateApi: true`).

**Focus (web)**: 2px solid `--tc-purple-text` outline, offset 2, on `:focus-visible` for buttons, toggles, checkboxes, segments, pickers (`:619-626`); inputs offset 1 (`:991-995`); menu items take the menu-hover fill on focus (`:210-214`). This is the only shell with a designed focus ring, and it contradicts macOS (system ring per spec; none as built).

**Reduced motion (web)**: a global `!important` kill of animation and transition under `.tc-root` (`:1376-1385`). No `prefers-color-scheme`, `prefers-contrast`, `prefers-reduced-transparency` or `forced-colors` handling.

**Fonts (web)**: `--tc-font-sans: -apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Display", "Helvetica Neue", system-ui, sans-serif`; `--tc-font-mono: "SF Mono", ui-monospace, Menlo, monospace` (`typography.css:3-4`). Off Apple platforms this falls to Segoe UI (not Segoe UI Variable) / Consolas on Windows and the fontconfig default / DejaVu Sans Mono on Linux; no webfont is bundled.

**Responsive (web)**: glass branch breakpoints are the JSON's 1100 (map) and 900 (inspector) at mount, left pane `clamp(320px, 34vw, 400px)`, feature views collapse at an untokenised `max-[860px]`; window 1320 x 760, min 760 x 560 (`monitor-shell.tsx:39-41, 67-68, 116`; `tauri.conf.json:21-26`). No phone layout. On `main`: `useIsMobile` at 768px, `ResponsiveOverlay` swaps Dialog for a Drawer below 768, the shadcn sidebar goes off-canvas (`hooks/use-mobile.ts:3-18`; `components/responsive-overlay.tsx:36-62`).

**React components (web)**: `Window(rim, floating)`, `Pane(padded)`, `Popover`, `Sheet`, `Menu`, `MenuItem(checked, disabled, onSelect)`, `MenuSeparator`, `Modal(open, onClose, title, subtitle, headerAccessory, footer, narrow 450, viewport)`; `SegmentedTabs(items{value,label,badge,badgeLabel,dot}, floating, label)`, `Breadcrumb`, `StepProgress`; `Card(quiet, flush, interactive)`, `QuietCard`, `EyebrowCard`, `Well`, `ConsentBlock`, `TableRow`, `TableHead`, `LegendCell`, `KeyValueList`, `Notice(tone, title, role alert|status)`, `SectionRule`; `ButtonPrimary`/`ButtonSecondary(size md 34 | sm 30)`, `GlassButton(aria-pressed)`, `RoundButton(small 26/28)`, `PillIconButton` 30 x 26, `ToolbarIconButton(pressed)`, `SubmitPill(done)`, `FolderButton`, `Kebab`, `TertiaryLink`, `Expander`, `Picker`, `Toggle(settings)`, `WatchSwitch` (green 38 x 22), `Checkbox(indeterminate)`, `CheckRow`, `TextField(hint, multiline)`, `Input`, `TextArea`, `Select`, `RadioGroup`, `Radio`; `StatusDot(size sm 6 | md 7 | 8, halo, ring, empty)`, `StatusLabel`, `Chip(glass, dot)`, `Tag(on|ask|outside|accent)`, `Badge`, `ToolTile`, `BarGraph`, `MapNode`, `MapArc(tone, pulse, dim, bend)`, `NodeCard`, `Spinner`, `WarningGlyph`, `Skeleton`; `ListRow`; `ToolLogo`. The macOS TCDesign API is a superset (adds icon cards, promo cards, rule tabs, split button, icon menu, radio row, info button, action bar, modal host/stacking, menu-bar parts, edge rail, map field, trace mark).

### 8.3 Tauri CSS vs the JSON: every value mismatch (JSON is newer)

| # | CSS (`pr1146`) | JSON | Why the JSON changed |
|---|---|---|---|
| 1-3 | popover .78, menu .72, node card .72 | .94, .94, .92 | fixed on the R branch too |
| 4 | `--tc-selection` #3a7bd5 | #3275d3 | white text 4.22 -> 4.55 |
| 5 | placeholder white 30% | 46% / black 57% | prompt is text: 2.60 -> 4.61 |
| 6 | hidden toolbar glyph #7c7c86 | #83838c | 3:1 glyph floor |
| 7 | number 28px | 26 | macOS largeTitle default |
| 8 | window padding 10px | 0 (gap 10) | floating layout (#1273) |
| 9 | map width 600 (unused) | 440 | |
| 10 | window height 760 | 614 | |
| 11 | submit disabled .55, checkbox/radio .7 | note says one .45 (code still .55/.7) | see 2.7 |
| 12 | modal radius 22 with rim and modal fill | pane radius, pane base, no rim | |
| 13 | scrim padding 28 | 52 top / 28 | |
| 14 | bar slide .45s `(.4,0,.2,1)` | one curve | kept as a literal on macOS too |

Tokens the CSS lacks: **every light value**, both flat themes, all Increase Contrast partners, `paneOpaque`, the status-text twins (`status*Text`, `destructiveText`), `badgeFill`, `micro`, `chartSeriesReduced`, and all macOS-only additions (menu bar, edge rail, tab ember, map rules, graph focus, `inactiveDim`, `promoTintEnd`, `traceLive*`, `ink`).

### 8.4 Windows (WinUI 3)

`App.xaml` merges `XamlControlsResources` then `Themes/DesignSystem.xaml`, which merges the generated `BrandTokens.xaml` (`windows/src/TraceCommons.App/App.xaml:22-23`; `DesignSystem.xaml:35-37`). No Mica, Acrylic or SystemBackdrop anywhere; custom title bar (`ExtendsContentIntoTitleBar`). Hand-written grounds and ink: window #23251d / #f6f7f4, sidebar #262922 / #eceee8, chrome #2b2d28 / #f3f3f0, card #21241e / #ffffff (opaque), inset #2a2e27 / #eef2f0, hairline #3b4038 / #d9dfdc (drawn **around cards**, where the JSON says never), ink #e8eae3 / #20241f, secondary #a6ac9f / #5c635b, tertiary #878d81 / #6d7269; blue #7fa0ec / #315fba (differs from glass `blue`); redaction chip #4a3c18 on #f0ebdd (`DesignSystem.xaml:47-156`). Fonts: "Segoe UI Variable Text, Segoe UI" and Consolas (`:220-222`); type ramp has steps the JSON lacks (10.5, 12.5, 16, 18, 20), body line height 19, eyebrow 10 ExtraBold at 0.05em, heading 17 Bold, metric 20 SemiBold (`:226-423`). Spacing 2...32 (adds 18, 22, 28, 32). Radii: control 4, card 8, window 8. "1px hairlines, never shadows" (`:271-274`). Buttons: radius-4 Fluent buttons with stock hover/pressed/focus. High Contrast: every brand and ground key aliases to system brushes (`:159-209`; `BrandTokens.xaml:74-99`), the only shell with a complete forced-colours path. Tests: `BrandTokensTests.cs` (text 4.5, lines 3.0 on five grounds; accent is purple; retired greens absent).

### 8.5 GTK / libadwaita (`crates/trace-commons-contributor-gtk`)

One CSS provider at APPLICATION priority: generated `LIGHT_CSS`/`DARK_CSS` roles, then `LIGHT_TOKENS`/`DARK_TOKENS`, then `style.css`, chosen from `adw::StyleManager::is_dark()` and reloaded on change (`src/ui/style.rs:415-452`). The GNOME accent is deliberately overridden with brand purple ("please do not fix", `style.rs:35-49`; whole libadwaita palette recoloured `:191-230, 295-329`). Same warm green-grey grounds and ink as Windows. Radii control 6, card 8 (1px border), window 12, pill 999 (`style.css:17-473`). Type: system font, weights one step heavier (display 20/800, screen title 17/700, card title 14/700, eyebrow 10/800 at 0.8px, figure mono 22/700). Spacing 4/6/8/12/16/20/28 (`style.rs:334-342`). Tone system = colour + glyph (`· ✓ ! ◴ ✕`) + words (`style.rs:351-389`). A second, light-only "community brand" provider (black/white/mint #00d4aa, Helvetica, no rounding) styles the public-web panels (`community_brand.rs:1-68`). No High Contrast or reduced-motion handling; libadwaita default focus rings derived from the overridden accent (inferred).

### 8.6 The mark system

| Mark | Geometry | Colours | Where it is used |
|---|---|---|---|
| **"The Turn"** (two corner brackets; adopted 2026-08-17) | 64-unit box; frame `rect 1,1,62,62` stroke 2; open bracket `M11 28V11h17`, close bracket `M53 36v17H36`, stroke 7 framed / 8 template (`assets/mark/geometry.json:2-8`; `crates/trace-commons-mark/src/lib.rs:8-84`) | crate & packaging: open bracket **mint #00d4aa**, close bracket/frame ink (black or white); GTK and Windows in-window: open bracket **purple**; Tauri app icon: retired **#178f70** + blue #315fba; Tauri main sidebar: indigo + grey | macOS .icns, Linux hicolor + tray SVG (64), Windows MSIX tiles (44/50/150 at 1.25-4x via the crate's own rasterizer), GTK header 20 / onboarding 84, Windows title bar 16 / 40. `mark-export` regenerates `assets/mark/*` and CI checks `git diff --exit-code`. Assets: `mark-{light,dark}.svg` (framed), `mark-glyph-*` (frameless, mint + ink), `mark-template-*` (one ink, stroke 8) |
| **Trace mark, "1c Live trace"** (macOS only) | 3x3 diagonal lattice in a 200-unit box; 5 visited nodes r10 joined by 4 necked joins; 4 unvisited nodes | visited: linear gradient #5b14ff -> #b412c4 -> #ff0a6c, glow on the current node (#ff0a6c 55% -> 0, r30); unvisited: purple #6d14f3; `ink:` solid one-colour variant; no light variant | only the edge rail, at 30 x 30, in solid ink; the gradient version is unused in the app (`GlassTraceMark.swift`; `EdgeRailView.swift:147-148`) |
| **NEAR AI "N"** (brand kit `tile-white-color.svg` path) | normalised to a unit square | white 9.6% / black 8% at rest, up to 20% / 15% under the pointer | only as the flow map's tiled background texture (5.6pt marks on a 28pt pitch) (`GlassBrandMark.swift`; `Indicators.swift:585-729`) |
| **Third-party tool logos** | Claude, Codex, Antigravity, OpenCode (24-unit boxes), Theia (64-unit) | per-tool tints (`toolClaude` #e08a6a / #c2603e, etc.) | macOS and Tauri only (paths copied by hand: "keep the two in step"); 15pt in the 22pt tile, 20pt in the 30pt tile, 12pt in menu-bar rows; Gemini CLI and Cline fall back to two-letter initials; the spec requires a trademark-use check before shipping vector marks (GS "Icons") |

Icon pipeline decisions (2026-08-19/20): one geometry source; live drawing for in-app UI, generated assets only for packaging; per-platform icon targets; the mint/purple convergence of The Turn is pending "when the final brand lands" (`style.rs:454-458`; `mark.rs:44-54`; `DesignSystem.xaml:84-88`). The docs still describe the close bracket as blue (stale).

### 8.7 Divergence list (what a parent system must reconcile)

1. Three palettes: glass cool blue-black (#0f1219, #f2f2f4 text), Windows/GTK warm green-grey (#23251d, #e8eae3 ink) from a spec file not in the repo, and Tauri main's oklch neutral/indigo. Only the purple accent and status roles are shared, and only by macOS/Windows/GTK.
2. Material strategy: native glass (macOS), CSS backdrop-filter (Tauri glass), opaque with hairlines (Windows, GTK). "Edges are specular highlights, never solid borders" (glass) vs "1px hairlines, never shadows" (Windows, GTK).
3. Radii: control 8 (classic) / 11 (flat) / 4 (Windows) / 6 (GTK); card 14 / 16 / 8 / 8; window 22 (Tauri) / 8 (Windows) / 12 (GTK) / none (macOS, transparent).
4. Type: SF Pro text styles (macOS); system-ui fallback (Tauri glass); Segoe UI Variable with extra steps (Windows); system font one weight heavier (GTK); IBM Plex Sans + Source Sans 3 (Tauri main). `number` is 26 (JSON), 28 (Tauri), 20 (Windows metric).
5. Blue: #3a7bd5 (glass), #7fa0ec / #315fba (Windows, GTK), a grey `--chart-2` (Tauri main).
6. Light theme: macOS full; Windows/GTK light grounds from the other palette; Tauri glass none.
7. Accessibility coverage: Increase Contrast only on macOS; forced colours only on Windows; reduced motion on macOS and Tauri; Reduce Transparency nowhere explicitly (macOS defers to the system); GTK none. Focus: designed purple ring on Tauri, system/Fluent/Adwaita defaults on Windows/GTK, disabled on macOS.
8. Marks: The Turn in four colourings (mint, purple, retired green, indigo); the Trace mark and the NEAR AI "N" only on macOS; no defined hierarchy between product mark, Trace mark and the NEAR AI brand.
9. Breakpoints: 1100/900 (JSON, Tauri glass), 860 (Tauri features, untokenised), 768/640 (Tauri main), 720 (Windows preview sheet min width); window 1320 x 760 (Tauri) vs 1193 x 614 (macOS).
10. The JSON claims to be "the one source for ... any other shell" (TOK:2) but the web shell neither reads nor is generated from it.

## 9. Gaps, inconsistencies and decisions for the parent system

### 9.1 What trace-commons does not define (needed for Desktop + Web + Mobile)

1. **Touch and hit targets.** The system is pointer-first: controls are 22-34pt (kebab 22 x 24, toolbar 28 x 24, round 26/28, refresh 20, info glyph about 12, checkbox 15 with a text-sized row); the only minimum enforced is a 28pt menu row; 44 appears only as a literal on some app rows. Nothing meets 44pt (Apple touch) or 48dp (Material). There is no hit-target token, no touch slop, no density modes (compact / regular / comfortable).
2. **Hover-dependent interaction.** Info text shows on hover; the menu-bar state pills expand on hover; the edge rail opens on hover with a 300ms grace; map nodes light and show node cards on hover; bar-graph columns reveal values on hover; the promo spotlight follows the pointer; tooltips (`.help`) carry secondary names. Every one needs a tap/long-press/focus equivalent.
3. **Mobile navigation.** No tab bar, bottom navigation, navigation stack, drawer, back gesture, sheet detents, pull-to-refresh, swipe actions or safe-area handling. The only navigation patterns are the desktop three-pane window, rule tabs, segmented tabs, breadcrumb, a section list and an OS edge rail.
4. **Responsive layout.** Layout is fixed-width panes (440 / 293 / flexible map) with two launch-time breakpoints (1100 map, 900 inspector). There is no grid, column system, breakpoint scale, container queries, reflow rules for the inspector (sheet? stacked page?), or any layout below 440pt. The web shell's breakpoints (860, 768) are untokenised and differ per branch.
5. **Window-tier and non-native materials.** Blur radii, saturation, the window rim, window shadow, window radius and scene glows were deliberately removed from the JSON (TOK:5). Any shell without Liquid Glass (web, Android, Windows, Linux, iOS before 26) needs these back, plus a defined opaque fallback per tier, plus a performance budget for `backdrop-filter`.
6. **Light theme for the web.** The only CSS implementation is dark-only.
7. **Forms beyond basics.** No form layout grid, label/field alignment rules, required/optional markers, helper text, character counters as a component (they are hand-built per screen, e.g. "n/max" mono counters), inline validation timing (only the passkey name field defines "after touched"), error summary, stepper, slider, date/time picker (native `DatePicker` used ad hoc), search field with clear/scope, combobox/autocomplete, token input, file drop zone (hand-built dashed tile), segmented input, or multi-select.
8. **Data-dense tables.** `GlassTableRow`/`GlassTableHead` are static rows in a flush card. No sorting, column resizing, sticky headers, pagination/virtualisation (except the review transcript's own `LazyVStack`), row selection model for tables, numeric alignment rules, empty-cell rules (other than "—"), or responsive table collapse.
9. **Feedback and messaging.** No transient toast/snackbar component (the undo card is persistent and lives in the inspector or above the tree), no banner hierarchy beyond `GlassNotice` tones, no determinate progress bar, no skeleton usage (the component exists but is unused), no empty-state illustration system, no system notification design beyond copy rules.
10. **Iconography.** SF Symbols are named inline as strings; a handful of #1146 glyphs are hand-ported SVG paths; there is no icon token registry, size scale, stroke rule or cross-platform icon set (Tauri main uses Phosphor; Windows/GTK use text glyphs and Fluent/Adwaita icons). SF Symbols cannot ship on web, Android or Windows.
11. **Typography off Apple platforms.** The scale is defined as macOS text styles (body 13, title3 15, largeTitle 26) and the type tokens fail generation unless a size equals the macOS style default. iOS defaults differ (body 17), web has no text styles, and SF Pro cannot be licensed for web, Android or Windows use (Apple's font licence restricts SF Pro to Apple platforms and mock-ups). A parent system needs a platform-neutral scale with per-platform mappings and a licensed web/Android face (or system stacks).
12. **Elevation and z-index as numbers.** Elevation is implicit in edge stacks and tier order; there is no z-index scale, no elevation token per tier for web, and no dark-mode elevation tinting rule.
13. **Motion beyond desktop.** No enter/exit choreography, shared-element or navigation transitions, spring tokens (one spring is hard-coded), gesture-driven motion, or haptics.
14. **Data visualisation.** No categorical palette beyond Shared/Kept/Inference and the text/accent ramp Insights uses; no axis, gridline, tooltip or legend tokens; Insights charts bypass the data tokens; there is no colour-blind-safe validation of series beyond contrast.
15. **Content.** English only, no localisation or RTL; no pluralisation rules outside Rust; no date/number formatting tokens beyond the conventions in 6.6.
16. **Accessibility verification.** No automated VoiceOver/TalkBack/ARIA audit, no focus-order tests, no target-size tests; the classic glass composite and live-desktop glass are not measured automatically.
17. **Brand architecture.** There is no defined relationship between the NEAR AI master brand, the "Near.ai" app name, the "Trace Commons" commons name, the Trace live-trace mark, The Turn product icon and the NEAR AI "N"; and no lockup, clear-space or minimum-size rules for any of them.

### 9.2 Internal inconsistencies found (token file vs code vs spec vs tests)

| # | Topic | Sources in conflict |
|---|---|---|
| 1 | **Default theme** | Flat is the shipping default (`GlassTheme.swift:29-36`); the contrast suites measure classic; `TokenDriftTests` ignore `themes` |
| 2 | **Brand accent** | D3 "purple everywhere" (GP Global Constraints; `TokenDriftTests` brand check) vs flat Light's blue #1f7aa8 / #15608a applied as the app tint (`TraceCommonsAppMain.swift:189`) |
| 3 | **Focus ring** | Spec "the system focus ring" (GS "Components"), plan "Follow Apple HIG: system focus ring" vs `.focusEffectDisabled()` on every scene (owner 2026-10-11; v0.14.0 "Controls no longer draw a focus ring") vs the web's designed 2px purple ring |
| 4 | **WCAG floors** | "Hold the WCAG floors" (owner 2026-10-07) vs "owner chose Ron's design over the contrast fixes" (2026-10-10, `9b86f414d`) for graph dots, flat secondary/status text, off-chip ink and the light tab ember; `AccentFillContrastTests` tolerate dark CTA/checkbox stops at 1.56-2.84:1 via `XCTExpectFailure`; `GlassActivityRow` hovers white on #3a7bd5 (4.22:1) |
| 5 | **Reduce Transparency** | spec and plan: app-painted opaque `paneOpaque` fallback; code and tests: left to the system (R14), `paneOpaque` only for the content pane |
| 6 | **Edges on Liquid Glass** | spec: "Specular edges are not drawn on a Liquid Glass surface" (`drawsOwnEdge`, #1180) vs owner ruling 2026-10-07 and code: every tier draws its edge, panes on Liquid Glass too (`GlassStyle.swift:257-260`; `GlassMaterialTests` forbid `drawsOwnEdge`) |
| 7 | **Settings presentation** | D8: window -> in-window modal (2026-10-05, spec) -> own window again (owner 2026-10-08, code) |
| 8 | **Eyebrow weight** | spec Decision 10: 600 vs TOK:317 `bold` |
| 9 | **Disabled opacity** | TOK note: one 0.45 for every control vs code/tests: 0.55 submit, 0.7 checkbox/radio |
| 10 | **Off rows** | TOK note: row faded at 0.6 with a secondary sub-line vs code/tests: only the tile fades; title steps to secondary; sub-line tertiary |
| 11 | **Watch switch** | TOK: green `watchOn` + `switchKnobEdge` ring; spec: green with a dark `textOnStatus` knob; code (owner 2026-10-08): purple track, plain white knob (both tokens now unused) |
| 12 | **Pane geometry** | TOK `inspectorWidth` 300, `windowWidth` 1320, `paneLeftWindowShare` 0.34, `windowMinWidth` 760 (unused) vs code 440/293, default 1193 x 614; spec says 10pt window padding and 1320 x 760; Tauri 1320 x 760 |
| 13 | **Radii** | spec quotes menu panel 18, TOK 14; `GlassMenu` renders at 12 (cardQuiet) |
| 14 | **Motion** | "one curve" (spec, `ComponentContractTests` ban stock curves in TCDesign) vs `.easeOut` knob, a spring on the rule tabs, a 0.45s `(.4,0,.2,1)` bar slide, a 1.1s `(0.3,0,0.15,1)` shimmer, and `.easeInOut(0.25)` in the app; "don't fidget / only the mark animates" (pre-glass rule) vs map shimmer every 40s, promo aurora/shimmer/glow |
| 15 | **Map layer** | classic: content, opaque, never glass ("as Apple keeps content out of Liquid Glass") vs flat: glass |
| 16 | **Unknown display** | window shows a literal "—"; menu bar shows the core's unknown word and says "never a bare dash" |
| 17 | **Selection fills** | `selection` (rows), `controlSelected` (segments, filter pills, rail tiles), `ink(0.12)` (History rows), `menuSelection`/`menuHover` (menus), `blue` (activity rows): five ways to show "selected/hovered" |
| 18 | **Marks** | The Turn in four colourings; Trace mark gradient tokens exist but no surface renders the gradient; NEAR AI "N" used as texture while the spec forbids near.ai marks without permission |
| 19 | **Copy authority** | "the core owns every word" vs hardcoded strings remaining in `PreviewSheet.swift`, `SettingsSections.swift:118-127` and a few format strings |
| 20 | **Token claims** | TOK:2 "the one source for ... any other shell" vs the web shell neither reading nor generating from it |
| 21 | **Spec location** | the macOS glass spec is on an unmerged branch; most recent rulings live only in commit messages and token notes |

### 9.3 Apple-only dependencies

- **SF Pro / SF Mono** (licence restricts use to Apple platforms; the web CSS and Windows/GTK fall back to system fonts); macOS **text styles** as the type scale's definition (the generator rejects any size that is not the macOS default).
- **Liquid Glass** (`NSGlassEffectView`, `GlassEffectContainer`) and **NSVisualEffectView** materials (`.hudWindow`, behind/within window); `plusLighter` blend; continuous (squircle) corners.
- **SF Symbols** for most icons (about 40 names inline).
- **AppKit window tricks**: transparent full-size title bar with traffic lights inside a pane, `isMovableByWindowBackground`, near-transparent background to keep clicks, `NSPanel` at `.statusBar` level for the edge rail, `MenuBarExtra(.window)` with system material masking.
- **System accessibility settings** read through AppKit (Increase Contrast via `NSWorkspace`, high-contrast appearances, Reduce Motion), and native controls used as `accessibilityRepresentation` to get system-spoken state.

### 9.4 Decisions the owner must make for the parent system

1. **Brand accent per appearance**: keep #6d14f3 purple as the one accent everywhere (D3), or adopt flat Light's blue (#1f7aa8/#15608a) as a light-mode accent? If purple stays, the light theme needs a purple that works on cool grey (the stated reason for blue).
2. **Which theme is canonical**: classic (gradients, specular rims, map as content) or flat (flat fills, no rims, larger radii, map on glass)? The parent tokens and tests must measure the one that ships.
3. **Focus ring policy**: restore a visible focus indicator (system ring or a designed ring such as the web's 2px `purpleText`) on every platform; the current macOS state fails keyboard accessibility expectations.
4. **Contrast policy**: "hold the WCAG floors" with no exceptions, or allow designer overrides? Fix or formally accept the dark CTA/checkbox fill failures; decide whether to adopt APCA or a large-text exemption; adopt one reference contrast implementation.
5. **Material strategy per platform**: native glass where available (macOS/iOS 26) and what on web/Android/Windows (CSS backdrop blur with the #1146 window-tier values? Mica/Acrylic on Windows? opaque?), plus the Reduce Transparency fallback (app-painted `paneOpaque` vs system).
6. **Type**: a platform-neutral scale (the current 10/11/12/13/15/17/22/26 is macOS-specific and small for touch) and licensed fonts for non-Apple platforms.
7. **Hit-target minimums and density modes** for touch (44pt / 48dp) vs the current 26-28pt desktop controls.
8. **Brand architecture**: the role of the NEAR AI "N", the Trace mark (gradient or ink), The Turn (and its mint vs purple open bracket), the "Near.ai" app name and the "Trace Commons" commons name; and whether the "no near.ai logo without written permission" rule is void now that NEAR AI owns the parent system.
9. **Copy ownership model**: keep "the core owns every word" (one Rust copy table for every client) for the parent system, and how web/mobile consume it.
10. **Motion stance**: "one curve, don't fidget" vs the glass era's decorative loops (map shimmer, promo treatments); whether springs are allowed and tokenised.
11. **Settings and secondary surfaces**: window vs modal vs page (D8 has flipped three times).
12. **Which spec is authoritative**: merge or supersede the unmerged macOS glass spec; collapse the four decision-ID namespaces into one register.
