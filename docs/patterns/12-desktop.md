# Desktop patterns

The macOS app is the lead desktop client. It is built in SwiftUI and AppKit, and the Trace monitor ("Near.ai") is its reference. Windows and Linux run the same product as the web app inside a Tauri shell, drawn with our web components on the parent tokens (NDS-18). This section generalizes the trace-commons window and its surfaces into patterns any NEAR AI desktop app can use, and says how each one renders on Windows and Linux. Navigation, the menu bar and shortcuts are in Navigation and commands; browser specifics are in Web patterns.

## Windows a desktop app owns

| Window | Role | Default size | Minimum | Chrome |
|---|---|---|---|---|
| Main window | Primary: navigation and content | 1193 × 614 with three panes (440 + 10 + 440 + 10 + 293) | Height 560; width is the sum of the visible panes | Hidden title bar; window controls inside the main pane |
| Settings | Auxiliary, one instance | 780 × 640 | 540 × 420 | Standard title bar; `pane-opaque` |
| First run | Auxiliary, one instance | 860 × 760 | 530 × 640 | Hidden title bar; painted scene; a 450 pane |
| Review | Auxiliary, or a `Modal` in the main window | 760 × 620 | None | Pane-tier sheet, Close only |
| Menu-bar panel | Glance and quick controls from the status item | `size-panel-width` 380 wide | None | One glass layer pinned under the menu bar |
| Edge rail | Opt-in glance at the screen edge (macOS) | 4 × 240 closed, 484 × 680 open | None | Borderless, does not take focus, on every Space |
| `Modal` | Confirmations and scoped tasks inside a window | `size-modal-width` 780 or `size-modal-narrow` 450 | Inset `modal-inset` 28, `modal-inset-top` 52 | `scrim-modal` over a `blur-scrim` of the window |

[trace-commons: TraceCommonsAppMain.swift, ThreePane.swift]

## The floating three-pane window

The main window is three floating panes with nothing drawn between them. Each is a `Pane` on the navigation layer: glass, `radius-pane` 20, one `shadow-float`. Everything inside a pane is painted content (NDS-9).

1. **Main pane**, `size-pane-main` 440, always shown. It holds the top row, the notice stack, the gate, the `Tabs` and the tab's content.
2. **Content pane**, flexible, at least `size-pane-content-min` 360. It holds the map, a canvas, a transcript or a document. Overlays on it (segmented tabs, a zoom toolbar, a node card) sit on the floating layer, never as a second glass pane.
3. **Inspector**, `size-pane-inspector` 293, two thirds of the main pane. It holds detail for the selection.

Panes sit `pane-gap` 10 apart. On macOS the window background is clear, so the panes meet the window edge; in the web shell the same gap separates them from the window edge.

- Turning the content pane or the inspector on grows the window to the right by the pane plus its gap; turning it off shrinks it. Nothing else moves.
- The content pane is the only pane that takes window resizes. The main pane never hides.
- On first launch, show the content pane when the screen is at least `bp-map` 1100 wide and the inspector when it is at least `bp-inspector` 900 wide.
- Persist per window: pane visibility, the selected tab, the selection, sub-pages, the graph footer, filters. Restore them on relaunch.
- The empty parts of the window move it. In the web shell, mark the top row's empty space as a drag region.

On macOS the window is the sum of its panes, so its class follows from what is shown. In the Windows and Linux shells people resize freely, so the panes reflow by layout class (NDS-12):

| Window width | Panes shown | Inspector | Content pane |
|---|---|---|---|
| 1200 and up | Main, content, inspector | Trailing pane | Flexible |
| 840 to 1199 | Main plus one | Trailing pane; opening it hides the content pane, and the reverse | Trailing pane |
| Under 840 | Main only | A trailing side `Sheet` over the main pane | A full-window view with a back chevron in the top row |

[trace-commons: GlassThreePane, ThreePane.swift] [M3: panes]

## Inspector demand

Events open the inspector; nothing closes it but the person.

- Open it when something happens whose result people need to see: an action that can be undone, an item contributed or kept, a folder submitted, a review requested, an agent run finishing.
- Open it when people select an item that has detail (a session, a history row). Selecting a container (a folder) does not.
- Show the inspector only on tabs that have detail. Elsewhere its toolbar toggle is hidden with the pane.
- With nothing selected, the inspector shows a summary: counts, the legend pair, the decisions waiting, the safeguards.
- Build it from an inspector header (an optional large tool tile, the heading in one bold line, a caption in `text-tertiary`) and inspector sections (a quiet `Card` holding an `Expander`, collapsible or fixed). Pad it `inspector-padding-x` 16 by `inspector-padding-y` 18, with `card-gap` 10 between sections.
- Keep decisions next to the list. The session review, with Contribute, Keep, Look inside and Dismiss, lives in the inspector. Sheets are for read-only deep looks.
- In pro tools the inspector becomes a `PropertyInspector` at dense density. See Dense and pro-tool patterns.

[trace-commons: MonitorShell.swift, SessionReviewCard.swift]

## The main pane top row

- **Leading.** Clear space for the window controls. macOS reserves 78 × 30 and centers the row on the traffic lights. On Windows and Linux the caption buttons sit at the trailing edge, so the clearance moves there and an app menu button takes the leading end.
- **Trailing.** One `Toolbar` group: a control-tier capsule with `space-2` padding holding `IconButton` toggles (View menu, Graph, Map, Inspector). A toggle whose pane is hidden draws its glyph in `toolbar-glyph-off`; a toggle whose menu is open takes `toolbar-expanded`. After the group, a round 28 `IconButton` opens Settings.
- Every toolbar item is also a View menu command with the same label and state, and its tooltip equals its accessible name.
- On macOS, Settings lives in the App menu on ⌘,. Trace's gear in the top row is a second path for people who never open the menu bar. On Windows and Linux the gear is the main path.

## Notices and the gate triad

Above the tabs, the main pane stacks the window's notices, then the gate.

- **Notice stack.** `Notice` cards in one scroll capped at 320, with a Dismiss all link once two or more can be acknowledged. A notice never tints its card; its tone is the dot in its title. A health banner is a `Notice` with no action. A notice that the service holds open (a gate held for a project) has no dismiss.
- **Gate triad.** Every surface backed by a service (the local watcher, the account, a server) shows one of three gates before content. *Awaiting*: a standalone `Spinner` with a line of words replaces the content. *Down*: a health banner, with held data kept visible. *Signed out*: a caution `Notice` with the action that opens sign-in or first run. The main window, Settings and the menu-bar panel use the same triad.
- **Fail closed.** A value the service has not answered is absent or a dash, never "On" and never zero (NDS-16).
- **Held data stays.** A failed reload adds an `InlineAlert` or a `Notice` with Retry and keeps the last value on screen.

[trace-commons: ShellNotices.swift, MonitorWindowView.swift]

## Tabs with the ember rule

The main pane's top-level areas use the rule variant of `Tabs`: equal-width titles over a 1px `rule` that bleeds to the pane edges. The selected title gets a 2px `tab-ember` line reaching past it on both sides, with `tab-ember-halo` rising behind it. The ember glides between tabs on `spring-ember` (`duration-spring-ember` 488) and jumps under Reduce Motion.

- A tab carries a `Badge` for decisions owed, or a dot whose meaning is also in the tab's accessibility value in words.
- ⌘1 to ⌘9 select tabs. Sub-pages inside a tab use a `Breadcrumb`, and Esc goes back one level.
- Tabs are never disabled. See Navigation and commands for the depth rules.

[trace-commons: Navigation.swift]

## Menu-bar glass panel

The status item opens a panel of glances and quick controls. In Trace it is the panel people use most.

1. **Frame.** `size-panel-width` 380, `space-10` padding, `space-8` between rows, `radius-pane`. The panel is the only glass layer: it masks the system's own material so nothing is glass on glass, and it keeps its top edge pinned under the menu bar.
2. **State pills.** A 44 row of control-tier pills (`radius-state-pill` 22), each a 31 filled circle with a glyph: contribution mode (Ask me, Automatic, Never), Watching or Paused, Private AI. A pill expands on hover and on keyboard focus (`duration-reveal` 180) to show its caption over its value; activating it opens its sub-list.
3. **Sub-list.** Swapped in on `duration-slide` 250: a 44 header with a back chevron, then option rows with a check column (pause for 1 hour, Until morning, Until resumed).
4. **Glances.** A nudge row, the Shared and Kept legend pair, a 36-day `BarGraph`, an insights card when its data is fresh, and up to three recent activity rows.
5. **Menu rows.** Separated by `hairline`: Open app, Manage rules, Settings, Quit.

- Never show "On" unless the service confirms it. Override rows stay disabled until the service can apply them.
- Confirm inside the panel with an inline well (Keep and Confirm). Sheets are unreliable in a menu-bar window.
- Resubscribe to the event stream 5 s after it drops, and re-read glances every 60 s while the panel is open.
- Draw the status item as an image with an accessibility label and help text from the copy source.
- Never rely on the status item being visible; a notch or a crowded bar hides it. Every panel command also lives in the main window and the Dock menu.
- Show the status item by default only for apps whose job is ambient, such as Trace watching folders, and offer a switch in Settings to remove it.
- **Windows** opens the same panel as a flyout from the notification area, on Acrylic. **Linux** shows it from the tray where the desktop supports status items (GNOME needs an extension), so the main window must carry everything.

[trace-commons: MenuBarGlassPanel.swift, MenuBarPanel.swift] [HIG: the menu bar]

## Edge rail

`EdgeRail` is an opt-in glance on the right edge of the screen. It is off by default and turned on in Settings > General. macOS only: on Windows and Linux the notification-area panel carries the same peeks.

- **Closed:** a 4 × 240 hover zone holding a 3 × 72 handle, centered vertically.
- **Open:** a 56-wide rail of 44 tiles inset 12 from the edge, and a 380-wide peek pane 16 to its left, at most 680 tall.
- Hovering the zone opens it; leaving starts a 300 ms grace (`duration-slow`) before it closes. Hovering a tile selects its peek.
- Each peek shows glance content and one "Open Home" style link with a line saying nothing was sent. The rail's only write is Pause and Resume; everything else opens the app.
- The keyboard and assistive path: the handle has an Open action, and a Show edge rail command in the registry opens it with focus on the first tile. Esc closes it.
- It slides on `duration-slide` with `ease-standard` and fades only under Reduce Motion.

[trace-commons: EdgeRailController.swift, EdgeRailView.swift]

## Settings window

Settings opens in a window of its own with ⌘, (Ctrl+, on Windows and Linux), from the App menu, the gear, or the palette. It is never a modal over the main window (NDS-21). A second ⌘, brings the open window forward.

1. **Header.** Title, subtitle, and a `Chip` with the state people most need to see (Watching or Paused). A `rule` below.
2. **Section list.** `size-modal-nav` 180 wide. Rows use `text-secondary` and `row-hover`; they scroll the body to a section and select nothing, so they never take the menu-selection fill. A name that has not loaded yet shows a disabled dash row.
3. **Body.** One scroll. Each section starts with a section rule (an accent eyebrow and a hairline) and is built from eyebrow `Card`s in a column padded `space-20` by `space-12`.

- Fill the window with `pane-opaque`. Esc and ⌘W close it. Reopen at the last section.
- Gate it with the same triad as the main window. Each setting that reads from the service has a read state: a `Spinner` while awaiting, a line and Retry when it failed, the control when answered.
- Apply changes at once; there is no Save button. A consequential change follows the confirmation ladder, and consent changes are checkbox-gated.
- Appearance is a `SegmentedControl` (Light, Dark, System) in General, applied immediately (NDS-17).
- Keep Settings for things people change rarely: account, data and consent, notifications, folders, startup. Task options stay where the task is. Never duplicate a system setting.

[trace-commons: SettingsModal.swift, SettingsStateRow.swift] [HIG: settings]

## First-run window and the step frame

- **Window.** 860 × 760, at least 530 × 640, painted with the scene (`scene-warm` to `scene`, radial). This is the only place a macOS app paints the scene. The `Notice` stack sits above a 450 pane (`size-modal-narrow`) with 30 of vertical padding.
- **Step frame.** A `Pane` (`pane-padding` 12, 16 between parts) holding, top to bottom: `StepProgress`; a header with a two-weight `mac-display` title (a light half and a bold half) inset 20; cards that scroll, 12 apart, inset 20, with the step's failure as an `InlineAlert` after the last card; an optional pinned zone (a drop target for folders); then the `ActionBar`.
- **Action bar.** Notes about the primary action sit `space-20` above it in `text-secondary`, full width, left-aligned. Back leads; Customize follows; Cancel appears only while a browser sign-in waits; the primary action trails with an inline `Spinner` when busy. Every bar button is `size-cta` 34. A disabled primary explains itself in its note and tooltip.
- **Flows.** Quick (Join, Folders, Uses) and Custom (Join, Tools, Rules, Uses), with Customize to branch. Steps are reached, never chosen, so `StepProgress` is not navigation.
- The headline carries the welcome; the frame has no hero art.
- Quitting during first run resumes at the same step. The signed-out gate reopens it.

[trace-commons: FirstRunFrame.swift, ActionBar.swift]

## Review sheet

Any flow that sends data off the device offers a read-only review of exactly what would leave. Trace calls it Look inside.

- Present it as a `Modal` at `size-modal-width` 780 or a pane-tier sheet at 760 × 620. The footer has Close only; Contribute, Keep and Dismiss stay on the inspector card.
- The header holds an eyebrow, a title, a description, the gate statement, a quiet card of sizes in monospaced digits ("would send 41 KB · on disk 118 KB") and the send disclosure.
- A `SegmentedControl` switches Transcript, Search original, Turn index and Search. The search field takes focus on its tab and on ⌘F.
- Long content is virtualized, with Copy everything and Load more naming what remains ("214 KB remaining").
- Redactions render as inline mono chips with spoken labels.
- A consent step inside the review (a witness review) is a checkbox-gated `Modal` whose Confirm is prominent and never the default.

[trace-commons: PreviewSheet.swift]

## Action ordering and the confirmation ladder

**Inline cards.** In an offer card, a review card or a notice, the action comes first as a primary or glass `Button`, then decline, dismiss and secondary actions as link buttons, then the failure line (`InlineAlert`) under both.

**Action bars and modals.** Cancel leads and the primary trails, with at most one primary per surface (NDS-19). Window and sheet action bars use `size-cta` 34 for every button; modal action bars use `size-cta-small` 30.

| Rung | Use for | Desktop rendering | Keys |
|---|---|---|---|
| Act and offer Undo | Reversible actions: Keep, pause watching, dismiss a notice | Runs at once; a `Toast` or the undo card offers Undo; Edit > Undo names it | ⌘Z |
| Default confirmation | Reversible but consequential: setting a folder to Automatic | `Modal` with a default confirm | Return confirms, Esc cancels |
| Destructive confirmation | Destroys data: Dismiss session, Withdraw, Delete run | `Modal`; the destructive button trails in `destructive-text` and is never the default | Return does not confirm; Esc cancels |
| Prominent, no Return | Irreversible sends: Contribute, send to an outside model | Drawn as the primary, never the default, no shortcut | Return does nothing |
| Checkbox-gated | Lasting consent: go public, a new reviewer, automatic sending | Confirm enables only after a `Checkbox` stating the consequence | Esc cancels |
| Inline well | Where sheets are unreliable (menu-bar panel) or the choice belongs in place (Withdraw on a card) | A well under the control with Keep and Confirm | Esc keeps |

While a modal is busy, its scrim, Esc, close button and Cancel do nothing until the work finishes.

[trace-commons: Modal.swift, cross-screen patterns 10 and 11]

## Window sizes and breakpoints

| Measure | Value | Token |
|---|---|---|
| Main, content minimum, inspector panes | 440, 360, 293 | `size-pane-main`, `size-pane-content-min`, `size-pane-inspector` |
| Gap between panes | 10 | `pane-gap` |
| First launch shows the inspector, the content pane | 900, 1100 | `bp-inspector`, `bp-map` |
| Shell reflow (Windows, Linux, web) | 600, 840, 1200, 1600 | `bp-medium`, `bp-expanded`, `bp-large`, `bp-xlarge` |
| Modal widths, insets | 780 or 450; 28 sides, 52 top | `size-modal-width`, `size-modal-narrow`, `modal-inset`, `modal-inset-top` |
| Settings section list | 180 | `size-modal-nav` |
| Panel and peek width | 380 | `size-panel-width` |
| Running text | at most 680 | `size-readable-width` |

## Multi-window and the menu bar

- The macOS app has a Dock icon and a status item. Clicking the Dock icon reopens the main window. An ambient app keeps running when its last window closes; other apps follow the platform.
- Only the key window answers shortcuts and draws the focus ring. Panes in background windows take `inactive-dim`.
- The Window menu lists open windows. Settings and first run are single instance and never appear twice.
- Open in New Window detaches a conversation, an agent run or a review into an auxiliary window that keeps its own state.
- On Windows and Linux each window has its own app menu button and `CommandPalette`. On Windows, closing the last window quits unless the app lives in the notification area, and Settings says which.

See Navigation and commands for the menus, the shortcuts and the registry.

## Pointer and hover

Every hover has a keyboard-focus equivalent and a tap equivalent. Nothing important exists only under the pointer.

| Hover behavior | Keyboard focus | Without hover |
|---|---|---|
| Info text in a `Tooltip` or an info glyph's `Popover` | Shows on focus; activating the info button pins the popover | Click or tap pins it; Esc or an outside click unpins |
| Menu-bar state pills expand | Expand on focus | Activating opens the sub-list; the caption and value are in the accessibility label |
| Edge rail opens with a 300 ms grace | The Show edge rail command focuses the first tile | Not offered without a pointer |
| Map nodes light and show a node card | Arrow keys move between nodes; focus shows the card | Tap selects and shows the card |
| Bar-graph columns reveal values | Arrow keys step columns; values are announced | Tap a column; a table view gives every value (NDS-20) |
| Row actions appear (kebab, Submit pill) | Shown on the focused or selected row | Always shown; also in the context menu |
| Icon-only buttons show a label | `Tooltip` on focus | Visible labels on touch toolbars |

- A hover fill replaces the resting fill (`control-hover`, `card-hover`, `row-hover`); it never stacks, never applies to a selected row or a disabled control, and fades on `duration-fast` with `ease-standard`.
- On the web shell, gate hover styles with `@media (hover: hover)`.
- Hover never commits anything. No send, run, delete or consent happens on hover. Menus open on click; submenus may open on hover.
- Pointer shapes: the arrow over buttons, the pointing hand over links only, the I-beam over text, resize pointers over splitters, the copy and not-allowed pointers during a drag. The web shell keeps the arrow on buttons to match the OS.
- The pointer target is `target-pointer` 28, never below 20. Adjacent toolbar targets touch so the pointer never falls between them. Small glyphs (info, refresh) get an invisible hit area up to 28.
- A secondary click always opens the context menu.

[trace-commons: gaps 9.1 item 2] [HIG: pointing devices]

## Drag and drop

- Within one container a drag moves; into another container it copies; between apps it always copies. Use the platform's copy modifier: Option on macOS, Ctrl on Windows and Linux.
- Show the drag image after about 3 points of movement. Highlight a destination only while a valid item hovers over it; an invalid one shows the not-allowed pointer and nothing else. A failed drop springs back on `spring-spatial`, or fades under Reduce Motion.
- A drop zone at rest is a dashed 1px border in `text-tertiary` with `radius-control`. While a valid item hovers, the border turns `accent` over an `accent-tint` fill.
- Every drop has another path: an Add button or file chooser, paste, and a Move to… command for assistive technology.
- A drop stages; it never sends. Dropping files on the composer or a folder onto first run adds them for the person to review. Make drops undoable.
- Show a placeholder and a `ProgressBar` at the drop point while a slow drop lands. A rejected drop says why in an `InlineAlert`.
- Reorder only lists whose order means something. The insertion line is 2px `accent`; in a tree it starts with a small circle at the target depth.
- Dragging content out offers the richest format first, then Markdown, then plain text.

[HIG: drag and drop] [Unity Foundations: interactions]

## Undo and redo

Reversible actions act at once and offer Undo (NDS-15). One Undo command renders three ways on the desktop: Edit > Undo with the action's name (⌘Z; Ctrl+Z, with Ctrl+Y and Ctrl+Shift+Z for Redo), a `Toast` with an Undo button, and in Trace the undo card at the top of the inspector, which stays until dismissed.

- Name the action: "Undo Keep", "Undo Pause watching".
- Count up from a real moment ("Kept 12 s ago"). Never count down to a deadline the app cannot see.
- Show the result. Scroll to and select what came back, and open the inspector if that is where it lives.
- Keep undo back to when the window opened. A drag, a scrub or a burst of typing is one entry, committed on release, Return or blur.
- Batch agent changes: every change an agent makes can be undone, and "Undo changes from this run" reverses the run.
- Irreversible actions cannot be undone, which is why they confirm.

[HIG: undo and redo] [trace-commons: InspectorPrompts.swift]

## Notifications on desktop

- Ask permission when a notification first helps, such as after people start work that finishes later. Never ask at first launch. Settings has a switch per category.
- Notify only about work people started and decisions they owe. When the window is in front, update it in place instead.
- Map urgency: a result ready is Active; a decision with a deadline within the hour is Time Sensitive; digests and suggestions are Passive; nothing is Critical. Windows and Linux use their normal urgency; Linux never uses critical.
- Keep prompts, outputs, file paths and personal data out of the title and body. Payloads carry ids.
- Offer at most two actions: one that opens the item (Trace: Review) and one that defers it (Not now). No notification action sends, uploads or grants consent.
- Notify once per event; never repeat for something people ignored.
- The Dock badge and the Windows taskbar overlay show decisions owed only, the same number as the tab's `Badge`. Clear it at zero; show nothing when the count is unknown.
- Words come from the product's copy source, like every other surface.

[HIG: notifications, managing notifications] [trace-commons: contributor shell spec 2026-08-08]

## Windows and Linux shells

The shells render every pattern above with the web components. These are the differences.

| Concern | macOS (lead) | Windows | Linux |
|---|---|---|---|
| Toolkit | SwiftUI and AppKit | Tauri (WebView2), React components on the parent tokens | Tauri (WebKitGTK), same components |
| Panes | Liquid Glass `regular` tinted with the veil on macOS 26 and later, vibrancy on 14 to 25, then `glass-veil` and `pane-fill` (NDS-7) | Windows 11: Mica behind the window, `glass-veil` and `pane-fill` painted over it. Without Mica: `.nr-scene` with `blur-pane` | `pane-base`, with blur only where the compositor provides it and the frame budget holds |
| Floating layer | Painted over a within-window blur | `.nr-floating`; separate flyouts on Acrylic | `.nr-floating`, or `pane-base` |
| Frame | Hidden title bar; traffic lights in the main pane | System title bar and caption buttons, or content extended into the title bar with the system buttons kept | The desktop's own decorations |
| Window corners | System | The OS rounds a system frame; `radius-window` 22 only on a window the app draws, such as the tray panel | Same as Windows |
| Commands | Menu bar | App menu button and `CommandPalette` (Ctrl+K) | Same as Windows |
| Ambient surface | Menu-bar panel, edge rail | Notification-area flyout | Tray, where supported |
| Type | SF Pro text styles, `mac-*` | `web-*` steps in Segoe UI Variable through `--font-web` | `web-*` steps in the desktop's sans through `--font-web` |
| Focus ring | On by default (NDS-5); Trace turns it off | On | On |
| Increased contrast | Increase Contrast selects the `-hc` themes | Contrast themes arrive as `forced-colors: active`: system colors and real borders | `prefers-contrast: more` selects the `-hc` themes |
| Reduced transparency | `pane-opaque` | Transparency effects off: `pane-opaque` | `pane-opaque` |

- The shells use the web app's regular density with pointer targets (`.nr-regular`, `target-pointer` 28) and never ship SF (NDS-4). Pro-tool panels opt into dense as on the Mac.
- Keep Cancel leading and the primary trailing (NDS-19) although native Windows dialogs lead with the primary.
- Turning the focus ring off, as Trace does, fails WCAG 2.4.7 (Focus visible).
- Test every Windows screen with a contrast theme on.

[trace-commons: cross-platform 8.1 to 8.5] [Liquid Glass: Windows and Linux]
