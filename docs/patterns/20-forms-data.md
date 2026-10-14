# Forms and data

Forms collect what a product needs and data views give it back. Words sit beside the controls they explain, nothing is drawn as zero that was never reported, and layouts change with density without changing meaning. This section covers form layout, validation, saving, control choice, pickers, drop zones, search, tables, charts, and how numbers and dates are written. It uses `TextField`, `TextArea`, `SearchField`, `Select`, `Checkbox`, `RadioGroup`, `Switch`, `SegmentedControl`, `Slider`, `NumberField`, `Chip`, `KeyValueList`, `PropertyInspector`, `DataTable`, `ListRow`, `StatCard` and `BarGraph`.

## Form layout by density

| Density | Label | Field height | Between fields | Notes |
|---|---|---|---|---|
| Touch, iOS | Above the field (`ios-label`, `text-secondary`); settings-style forms use grouped list rows with the label leading and the value or control trailing | `size-control-touch` (44) | `space-12` in a group, `space-24` between groups | Native grouped forms for settings; stacked fields for sign-up and profile |
| Touch, Android | The M3 outlined field's floating label, which stays visible on the border | 56dp | `space-16` | Supporting text 4dp under the field |
| Regular, web | Above the field (`web-label`, `text-secondary`), `space-4` above it | `--nr-h-control` | `space-16` | One column; never stretch fields across a wide window |
| Compact, macOS | Above the field as an eyebrow (`mac-eyebrow`, `text-tertiary`), 4 pt above a 28 pt field | `size-control-large` (28) | `space-12` | Settings rows put the label leading (wrapping) and the control on the trailing edge |
| Compact, read-only facts | `KeyValueList`: labels right-aligned in a 70 pt column, values selectable | Text height | `space-6` | Project facts, account details, proof summaries |
| Dense | `PropertyInspector`: label column 33 to 40% (minimum 96), left-aligned, no colon | `size-control-dense` (20) | `space-2` | Padding `dense-padding-left` 18 / 4 / 8; indent `dense-indent` 15 per level, 6 levels at most; panel at least 275 wide |

- Use one column. Group related fields under a section heading; Trace's Settings sections are eyebrow cards in a 20 / 12 padded column.
- Keep labels visible at all times. Labels are short noun phrases in sentence case with no colon. A placeholder is an example of valid input, never the label.
- Size each field to its expected input. A field for a six-digit code is short; a field for a name is long.
- Keep tab order equal to reading order.
- End the form with an `ActionBar`: bar-size buttons (`size-cta`), Cancel leading and the primary action trailing (NDS-19), and any sentence about what the action does directly above the bar at a `space-20` gap.
- Never mix field styles in one form (M3's filled and outlined, or wells and bare lines).

[trace-commons: Controls.swift GlassTextField, Containers.swift GlassKeyValueList] [Unity Foundations: inspector] [M3: text fields]

## Required, optional and helper text

- Mark whichever group is smaller. When most fields are required, add "(optional)" to the optional labels. When most are optional, add the word "Required" to the required ones, as a `Tag` or after the label. An asterisk alone is not enough; if a product uses one, explain it once at the top of the form.
- Include the marker in the accessible name and set the required semantics (`aria-required`, the platform's required trait).
- Show a required consent that cannot be refused as ticked and disabled, with a "required" `Tag` and an info button that explains why (Trace's first-run Uses step).
- Put helper text under the field in `<tier>-caption`, `text-tertiary`, `space-4` below the field. Use it for the format or the consequence ("Shown on your public profile."). Consequences belong beside the field or the action, never only in a tooltip.
- Show an error in the helper text's slot, replacing the helper, so the layout does not shift. The words are `critical-text`; the field gets a 1px `critical` ring inside its edge. The words carry the meaning, so color is never alone.

### Counters

- Show a character counter as "n/max" in `<tier>-mono` at the trailing end of the helper line.
- Show it from 80% of the limit, or at all times when the limit is short (280 or less). Trace's examples: title 100, outcome 600, instructions 4000, bio 280.
- Count in the limit's own unit, and say so when it is not characters (Trace's bio limit counts bytes).
- Past the limit, the counter turns `critical-text` and states the excess in words ("12 over").
- Give the counter an accessible value ("Character count, 140 of 280") and announce it at thresholds, never on every keystroke.

## Validation timing

| Check | When | Example |
|---|---|---|
| Format (email, URL, key shape) | When the field loses focus after an edit | "Enter an address like name@example.com." |
| Required | On submit | "Enter a name for this passkey." |
| Availability (handle, invite code) | After typing pauses for 150 to 300 ms, with a `Spinner` in the field | "That invite code has already been used." |
| Constraints (length, character rules) | Live, as progress (a counter or a rule list), never as errors | "64 characters at most" |
| Clearing an error | Live: once an error shows, re-check on every change and clear it the moment the value is valid | |

- Validate after the field is touched, never while someone types a first attempt, and never on page load. Trace's passkey name field shows its rule (not empty, at most 64 characters) only after the field has been touched.
- Never show an error on every keystroke.
- Keep Submit enabled and report problems inline. Disable a submit control only in trivial cases (an empty composer), or when a consent precondition is unmet, with the reason in words beside it.
- In dense numeric fields, Enter commits and Esc reverts; an invalid entry reverts to the last valid value and the field says why.

### Error summary

- When a submit finds two or more errors, or any error outside the visible area, show a `Notice` at the top of the form listing each problem as a link to its field, and move focus to the notice. This is the one time a form moves focus. Keep every inline error as well.
- When the whole submit fails on the server, keep everything entered and show an `InlineAlert` under the action bar: "Couldn't save. Nothing changed. Try again."

[HIG: text fields, entering data] [M3: text fields] [trace-commons: PasskeySheets.swift]

## Autosave or explicit save

| Surface | Model | Feedback |
|---|---|---|
| Settings, every platform | Apply each change at once | No Save button; say so where it is not obvious ("Changes here apply straight away."); on failure the control reverts and an `InlineAlert` explains |
| Documents, drafts, notes, prompts | Autosave on pause, on blur, on close and on app switch | macOS: no unsaved dot and no save prompt. Web: "Saving…" then "Saved" in the toolbar. Mod+S saves now and does nothing else |
| A record committed as a unit (a task, a profile, a specification) | Explicit Save in an `ActionBar` or `Modal` | The consequence beside the button ("A saved specification cannot be changed.") |
| Edit sheets on iOS | Cancel leading and Done trailing in the sheet header | Confirm before discarding edits |
| Full-screen editors on Android | Close leading and Save trailing in the top bar | Confirm before discarding edits |

- Never mix the two models on one surface.
- Confirm before closing a surface that would lose unsaved explicit-save edits, and offer Save in that confirmation.
- A setting that takes time to apply shows its in-flight state and draws "On" only after the service confirms it. Trace's menu-bar values never read "On" unless the daemon confirms, and its settings stay disabled until the daemon answers.

[HIG: file management] [HIG: settings] [trace-commons: SettingsStateRow.swift]

## Choosing a control

| The choice | Control |
|---|---|
| One on/off setting that takes effect at once | `Switch`, on the trailing edge of a settings row |
| On/off committed later, consent scopes, several independent options, hierarchies | `Checkbox` (a check row with its full sentence beside it) |
| 2 to 5 exclusive options shown together | `RadioGroup` |
| A view or mode with 2 to 5 options | `SegmentedControl` (Light / Dark / System) |
| 6 to 15 options | `Select` |
| More than 15 options, or open-ended | `Select` with search, or a `SearchField` |
| A bounded number | `Slider` with a `NumberField`; a `NumberField` alone for exact values |
| Filters or tags over a collection | `Chip` set |

- Use a switch only for immediate effect. Never use one for this-or-that choices (List or Map) or for destructive actions.
- Phrase options so that on means on. A switch never disables something when turned on.
- On iOS, put switches only inside list rows; elsewhere use a toggle-style button. On macOS, prefer checkboxes for ordinary options inside forms, and switches for settings that control a group.
- Show mixed values in multi-item editing: a dash in a `Checkbox`, "—" in text and number fields, and "Mixed" in a `Select`. Editing applies the new value to every item; Esc leaves them mixed.
- Trace's folder mode (Ask me / Automatic / Never) is a `Select` with a status dot per option. Choosing Automatic opens a confirmation, because it grants consent.

[HIG: toggles] [M3: switch, checkbox] [Unity Foundations: toggle, dropdown]

## Pickers, dates and times

| Platform | Date | Time | Presentation |
|---|---|---|---|
| macOS | Native picker: textual for exact entry, graphical for browsing or ranges | Native textual picker | Inline, or in a `Popover` |
| iOS, iPadOS | Compact style in forms; inline when choosing the date is the task | Compact or wheels | Popover on iPad, sheet on iPhone |
| Android | M3 docked picker at medium and wider; modal on compact; modal input for distant dates such as birthdays | M3 time picker, with its keyboard input variant | Dialog on compact, docked on medium and wider |
| Web | A text field that accepts typed dates in the locale's format, plus a calendar `Popover` | A text field with a time list | `Popover`; a `Sheet` on compact |

- Always allow typing a date or time.
- Offer presets before a custom range (Today, Last 7 days, Last 30 days, Last 90 days) as rows, with the custom range below a hairline.
- Schedule in 15-minute steps; any interval must divide 60.
- Show the time zone whenever an event or a run crosses zones.

[HIG: pickers] [M3: date pickers, time pickers]

## File drop zones

- Pair every drop zone with a Choose button that opens the system picker, and accept paste. Drop is never the only way in.
- Draw the zone with a dashed 1px edge (4 on, 3 off) and a label inside it ("Drop a folder here, or choose one"). The edge turns `accent` only while a valid item is over it; invalid items get no highlight.
- Show accepted items as rows or `Chip`s, with progress for slow transfers. Give rejected items a reason in an `InlineAlert` ("Only folders can be added here.").
- Dropping from another app copies; it never moves or deletes the source.
- Phones use the picker only. iPad, Android large screens, macOS and web accept drops.

[HIG: drag and drop] [trace-commons: first-run add tile]

## Search and filters

- Place search where each platform expects it: the bottom toolbar or a Search tab on iPhone, the top on Android, the trailing end of the toolbar on iPad, macOS and web. Mod+F focuses search in the current view; Mod+K opens the `CommandPalette`.
- Name the scope in the placeholder ("Search sessions"). The clear button appears at the trailing end once there is text. Esc clears, then a second Esc leaves the field.
- Update results as people type, after a 150 to 300 ms pause for remote searches. Show recent searches before typing, let people clear them, and keep them off shared surfaces.
- Report results in three states: a count ("12 matches"), none ("No matches"), or unavailable when the search could not run.
- Highlight matched text with `accent-tint` behind `text-primary`.
- Put filters in one row of `Chip`s above everything they scope, so lists, totals and charts always agree. A selected chip uses the `accent-tint` ground with a check. Beyond two rows, scroll the row horizontally. Add a Clear filters link.
- Persist filters per view. Show a filtered empty state that differs from a true empty state.

[HIG: searching, search fields] [M3: chips]

## Data tables

### Anatomy

- **Header.** `<tier>-eyebrow` in `text-tertiary`, with header semantics. It sticks at `z-sticky` while the body scrolls. Column headings are sentence-case noun phrases; units go in the heading ("Size (KB)"), never in each cell.
- **Rows.** A `hairline` above every row except the first, never around the table, and no alternating stripes. Rows are at least `--nr-h-row` tall (40 on desktop, 20 dense, 48 on touch), padded `space-8` vertically and `space-12` horizontally. Tables inside a `Card` use the flush card so rows reach its edges.
- **Alignment.** Text left. Numbers right, with tabular digits, and their heading aligned the same way. Status cells use `StatusLabel` or `ProofTag`. Row actions sit trailing, as `IconButton`s that appear on hover or focus on desktop and stay visible on touch.
- **Empty cells.** "—", with the product's word as its accessible value ("Not recorded"). Never blank, and never 0 unless 0 was reported.
- **Long values.** Truncate file and conversation titles in the middle so both ends stay readable; show the full value on hover and in the detail view.

### Behavior

- **Sorting.** Click a heading to sort, and again to reverse; a glyph shows the direction. One sort key is active at a time, with a stable secondary order. State the default ("Newest first") and expose the sort to assistive technology (`aria-sort`).
- **Selection.** A selected row uses `selection` with `text-on-accent`; `row-hover` never covers a selected row. Multi-select adds a `Checkbox` column with a mixed-state header box, and an `ActionBar` that counts the selection ("3 selected") and holds the bulk actions. Shift-click selects a range, Mod-click toggles a row, Mod+A selects all.
- **Keyboard.** The table is one tab stop. Arrows move, Return opens, Space toggles selection, Home and End jump.
- **Columns.** Resizing, reordering and hiding columns belong to dense tools (`PropertyInspector`-class surfaces); everyday tables keep fixed columns.
- **Long data.** Virtualize long local lists (logs, ledgers, transcripts) with fixed row heights. Paginate server results whose position should survive a shared link, in pages of 25, 50 or 100. A "Load more" control states what remains ("240 remaining"). Cap very long histories with a line that says so (Trace shows its latest 100 rows). Never use infinite scroll above other content.
- **Live data.** New rows never shift the row under the pointer; count them in a line above the table and insert them on request. A refetch keeps the current rows on screen.

### On compact screens

Below 600 wide, a table becomes a list. Each record is a `ListRow` whose title is the primary column, whose sub-line carries one or two key values, and whose trailing edge holds the status. Tapping opens a detail view with every column in a `KeyValueList`. Keep a horizontally scrolling table, with the first column frozen, only where people compare values across columns. Never shrink text to make a table fit.

[HIG: lists and tables] [Unity Foundations: multi-column views, list view] [trace-commons: GlassTableRow]

## Charts

Charts follow NDS-20. Use a chart to make one point. For lookup, use a `DataTable`; when the story is a single number, use a `StatCard`.

- **Ground.** Plot on the opaque `surface-chart`, never directly on glass. Inside a `Card`, the plot ground is an inset rectangle with a concentric radius.
- **Color.** Assign `data-1` to `data-8` in fixed order, never cycled. Color follows the entity, so filtering keeps every survivor's hue. A ninth series folds into "Other" or into small multiples. `positive`, `caution` and `critical` are reserved for status and never used as series colors.
- **One axis.** Never plot two y-scales. Two measures make two charts, or are indexed to a common base.
- **Labels.** Show a legend whenever there are two or more series. Add direct labels for up to four series, sparingly: the endpoint, the extreme, the series the story is about. A single series needs no legend; the title names it. Labels, values and axes use text tokens (`text-secondary`, `text-tertiary`), never series colors.
- **Grid.** `chart-grid` solid hairlines, kept recessive. No dashed gridlines; dashes read as projections or thresholds.
- **Marks.** Bars at most 24 px thick with a 4 px rounded data end and a square baseline; a 2 px surface gap between touching marks; lines 2 px; markers at least 8 px with a 2 px surface ring; area fills as a light wash; a lighter companion series at `opacity-series-reduced` (0.75). Bars start at zero; ticks fall on clean numbers (0, 5, 10).
- **Words.** Give every chart a title and a takeaway in plain language ("Most calls this week went to Private AI."). Accessibility descriptions give context, then value, with no subjective words.
- **Interaction.** Every mark has a tooltip on hover and the same on keyboard focus, with a hit area of at least 24 px. Tooltips add detail; nothing is reachable only through them.
- **Table view.** Every chart has a table twin, offered with a `SegmentedControl` (Chart / Table) or a link. Each bar bucket is one accessible element with its description. A chart hidden from assistive technology carries a text alternative (Trace's Sessions view pairs its chart with a column of marker cards).
- **Filters.** One row above all the charts it scopes, with the date range first.
- **Refreshing.** Hold the previous render at reduced opacity while new data loads. No skeleton and no layout jump.
- **Missing data.** Draw data that could not be read as a labelled gap, never as zero or as activity. Draw paused periods grey.
- **Projections.** Draw projected values with their own mark style (outlined or hatched) and the word "projected", never in the settled style.
- **Motion.** Animate changes on the spring tokens; nothing moves under Reduce Motion, and changes are announced.

`BarGraph` is the system's bar chart. Trace's tapered dot-matrix graph (shared above the axis, kept below) is a product treatment built on the same rules.

[HIG: charts, charting data] [trace-commons: Indicators.swift GlassBarGraph, Insights]

## Numbers and dates

- **Tabular digits** wherever numbers align or update in place: table columns, axis ticks, counters, timers, and `StatCard` values that change live. A lone, static figure in `hero-figure` may use proportional digits.
- **Mono** (`<tier>-mono`) for figures that describe what leaves the device (sizes, byte counts, hashes) and for identifiers. Prose is never mono.
- **Dates** as weekday, day, month: "Sat 12 Sep", adding the year only outside the current year ("Sat 12 Sep 2025"). Times follow the locale's 12- or 24-hour setting.
- **Durations** with a space between number and unit: "12 s", "52 min", "1 h 18 min". Relative times count up from a real moment and never count down to a deadline the product cannot see.
- **Stable days.** Read dates in the zone that keeps them stable for their meaning; Trace reads session dates in UTC so a session never moves to another day.
- **Large numbers** use the locale's separators. A `StatCard` may compact them ("12.9K") with the full value in its accessible label and tooltip. Units follow a space ("18 KB").
- **Counts and plurals** come composed from the product's copy source ("1 session", "2 sessions"). Components never branch on a count of one.
- **Credit.** Trace treats credit as "a record, not a currency": no currency symbol and no money estimate. Pending credit appears only beside its condition.
- **Projected values** carry the word and the condition ("+20 projected, if the commons accepts it") in `text-secondary` at regular weight, never styled like settled values.
- **Priced and billed.** When nothing was charged, say "priced", never "billed" or "cost".
- **Unknown** is "—" or the product's word, never 0 (see *Feedback and states*).

[trace-commons: numbers, dates, credit] [HIG: charts, accessibility labels]

## Platform mapping

| Pattern | macOS | iOS, iPadOS | Android | Web, Windows, Linux |
|---|---|---|---|---|
| Text field | 28 pt field, eyebrow label above | 44 pt, label above, or a grouped list row | M3 outlined field, 56dp, floating label | Label above, `--nr-h-control` |
| Settings | Settings window; trailing switches; changes apply at once | Settings screen, grouped list | Settings screen | Settings page |
| Date and time | Native textual or graphical picker | Compact or inline picker | M3 docked, modal or input picker | Text field and calendar `Popover` |
| Tables | `DataTable`, click to sort | Grouped list with detail | List with detail | `DataTable`; a list below 600 |
| Search | Trailing toolbar field, Cmd-F | Bottom toolbar or Search tab | Top search bar | Header field, Ctrl+F, Ctrl+K |
| Saving | Apply at once, or autosave | Cancel and Done in sheets | Save in full-screen editors | Autosave with "Saved" |
| File input | Drop zone and Choose | Files picker; drops on iPad | Picker; drops on large screens | Drop zone and file input |
