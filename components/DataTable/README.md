# DataTable

Rows of records in aligned columns inside a flush card, with an eyebrow head, a hairline above every row but the first, and optional sorting, selection and a sticky head for dense desktop and web views.

## When to use

- People compare values across records: model calls, agent run steps, contributions, invoices.
- The text alternative for a chart (NDS-20): the same buckets as a table.
- Use `KeyValueList` for one record's facts, `ListRow` for a navigable list of things, and a list on phones (see Behavior) where columns do not fit.

## Anatomy

1. **Card**: a flush card (`.nr-card--flush`), `radius-card` 16. Rows draw their own insets, so nothing touches the corners.
2. **Caption** (optional): the table's name, as a visible title above the card or a `caption`; the summary line beside it ("Calls 1,284 · Verified 1,279 · Priced 1,284").
3. **Head**: eyebrow step, uppercase, `text-tertiary`, padding `space-8` by `space-12`, bottom aligned. A sortable heading is a button; the sorted one turns `text-primary` and shows an 8 chevron.
4. **Row**: padding `space-8` by `space-12` (9 by 12 with the hairline), body step, `text-primary`. A 1px `hairline` sits above every row but the first; there is no rule around the table.
5. **Cells**: text starts at the leading edge; numbers end-align with tabular figures; secondary columns in `text-secondary`; times, hashes and paths in the mono step; one flexible column truncates (`.nr-data-table__truncate`).
6. **Status cell**: an 8 dot (`positive`, `caution`, `critical`, `accent-soft`, `neutral`) with the product's word in `text-secondary`, `inline-gap` 6 apart.
7. **Foot** (optional): a caption line in `text-tertiary` for a capped list ("Showing the latest 5 of 1,284 calls.").

## Sizes by density

| | compact (macOS) | regular (web) | touch iOS | touch Android | dense |
|---|---|---|---|---|---|
| Row height | about 34 | about 36 | 44 (as list rows) | 48 (as list rows) | 20 (`size-control-dense`) |
| Cell padding | 8 / 12 | 8 / 12 | list row insets | list row insets | 0 / 6 |
| Head padding | 8 / 12 | 8 / 12 | - | - | 2 / 6 |
| Body type | `mac-body` | `web-body` | `ios-body` | `android-body` | `web-caption` |
| Head type | `mac-eyebrow` | `web-eyebrow` | - | - | `web-micro`, uppercase |
| Mono cells | `mac-mono` | `web-mono` | `ios-mono` | `android-mono` | `mac-mono` |

Below `bp-medium` 600 a table becomes a list: each record is a `ListRow` whose title is the key column and whose sub-line joins two or three other values; the rest move to the detail page.

## Variants

- **Static** (read-only, `role="table"` semantics from `<table>`).
- **Interactive** (`.nr-data-table--interactive`): rows hover and select; a selected row opens its detail in the inspector.
- **Sortable**: header buttons with `aria-sort`; one sorted column at a time.
- **Sticky head** (`.nr-data-table--sticky`): when the table scrolls inside its card the head stays, drawn on `pane-base` with a `rule` under it, at `z-sticky`.
- **Dense**: inside `.nr-dense`, for pro-tool panels.
- Desktop extras where the platform offers them: resizable and reorderable columns, columns people can hide, alternating rows only in very wide tables (macOS).

## States

| State | Treatment |
|---|---|
| Hover (interactive) | `row-hover` across the row, rounded ends `radius-tile` |
| Selected | `selection` across the row; all cell text and status words `text-on-accent`; the hairlines on both sides give way |
| Sorted | heading `text-primary` with its chevron (down descending, up ascending); `aria-sort` set |
| Focus | grid focus moves by cell or row; ring 2px `focus-ring` on the active row or cell |
| Loading | the product's line in the card ("Reading calls…") or a `Spinner` with words; rows already shown stay |
| Empty | the product's sentence in the card, no head |
| Unknown cell | "—" or the product's unknown word, never 0 |
| Failed | an `InlineAlert` under the card with a retry; the last good rows stay |
| Increased contrast | the card's 1px `edge-hc` edge; `hairline` steps up to the hc value |

## Behavior

- Static tables are not tab stops. Interactive tables are one tab stop (`role="grid"`): arrows move between rows (and cells when cells hold controls), Home and End jump, Return opens the selected row, Space toggles selection in multi-select.
- Click a heading to sort; click again to reverse. Keep the sort and column widths per view.
- Pointer: click selects; double-click opens; right-click opens the row's context menu.
- Truncate the flexible column at the end on web. Where the product controls the string (file names, conversation titles), truncate in the middle so the start and end stay readable.
- A table caps long histories and says so in the foot; paging is the product's choice, never silent truncation.
- Motion: fills on `duration-fast` `ease-standard`; the sort chevron turns on the same curve. New rows appear in place. Nothing moves under Reduce Motion.

## Accessibility

- Use `<table>`, `<th scope="col">` and a name (`aria-label` or `caption`). Interactive tables add `aria-selected` on rows; sortable headings are buttons inside `th` with `aria-sort` on the `th`.
- Status cells carry words; the dot is supplementary and hidden.
- Text tokens hold 4.5:1 on `card` over the worst ground; on `selection` the text is `text-on-accent`.
- Headings use the product's nouns in sentence case. The consumer supplies every heading, cell, caption and foot line.

## Platforms

| SwiftUI/AppKit (macOS) | SwiftUI/UIKit (iOS/iPadOS) | Jetpack Compose M3 | Web |
|---|---|---|---|
| SwiftUI `Table` with `KeyPathComparator` sorting and resizable columns, or `NSTableView`; the flat painted look from `GlassTableHead` and `GlassTableRow` in a flush `GlassCard` | `Table` on iPad regular width; it collapses to its first column in compact width, so use a `List` of rows there | No M3 table: a `LazyColumn` with a sticky header row and `Row` cells; `HorizontalDivider` in `hairline` between rows | `<table class="nr-data-table">` in `.nr-card--flush`; `role="grid"` only when cells are interactive |

## Do and don't

- Do end-align numbers with tabular figures. Don't center columns.
- Do draw hairlines between rows only. Don't box the table or draw vertical rules.
- Do show "—" for a value not yet known. Don't show 0 or leave the cell blank.
- Do turn the table into a list on phones. Don't scroll a table both ways on a small screen.

## Source

Intentional addition. trace-commons has `GlassTableHead` and `GlassTableRow` in Containers.swift (eyebrow head, 9 by 12 rows, "hairline above, never around") but no sortable, scrollable or selectable table. Sorting, resizing and middle truncation follow HIG lists and tables and outline views; the multi-column model, 20px dense rows and comparison over tabs follow Unity Foundations (multi-column views, list view); the phone list fallback follows M3 lists and the HIG note that `Table` collapses in compact width.
