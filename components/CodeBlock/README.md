# CodeBlock

Monospaced, selectable text on the consent ground for code, tool-call arguments, transcripts and logs, with an optional header holding a label and a copy action.

## When to use

- Tool-call arguments and results, generated code, shell commands, a redacted transcript excerpt, a log line, a request ID people will paste into a support thread.
- Use inline mono text (`web-mono` in a sentence) for a single path or hash, `KeyValueList` for labelled facts, and `ToolCall` for the full call card around a block.

## Anatomy

1. **Block**: `consent` fill, `radius-card-quiet` 14, no edge in flat glass, clips its content to the radius.
2. **Header** (optional): a caption label in `text-tertiary` (language or source: "Tool call · JSON", "Call log") and a copy action at the trailing edge; padding `space-6` top, `space-12` leading, `space-6` trailing.
3. **Copy action**: a quiet pill (`size-submit-pill` 24 tall, `radius-pill`, transparent, `text-secondary`) with a 12 glyph and the product's word; hover `control-hover`; its hit area grows to `--nr-target`.
4. **Body**: a `<pre>` with padding `space-12` (`space-6` under a header), mono step, `text-primary`, tab size 2, selectable.
5. **Text roles** (optional, never syntax rainbows): keys and keywords `accent-text`, comments `text-secondary`, redactions on a `neutral-tint` chip in `text-secondary` with the product's word for what was removed.

## Sizes by density

| | compact (macOS) | regular (web) | touch iOS | touch Android | dense |
|---|---|---|---|---|---|
| Body type | `mac-mono` (11/16) | `web-mono` (12/18) | `ios-mono` (13/18) | `android-mono` (12/16) | `mac-mono` |
| Padding | 12 | 12 | 12 | 12 | 8 |
| Header label | `mac-caption` | `web-caption` | `ios-caption` | `android-caption` | `mac-caption` |
| Copy target | 28 (`target-pointer`) | 28 | 44 | 48 | 20 minimum |
| Cap before inner scroll | 16 lines (288, 6 x `space-48`) | 16 lines | none: show 8 lines and a Show all `Expander` | as iOS | 16 lines |

## Variants

- **Wrapped** (default): transcripts and prose-like output wrap anywhere, so nothing hides off the edge.
- **Scrolling** (`.nr-code-block--scroll`): code and logs keep their lines and scroll sideways inside the block; the `<pre>` is focusable so keyboard users can scroll it.
- **Capped** (`.nr-code-block--capped`): a long block scrolls inside itself past 16 lines on desktop. On touch, never scroll inside a block: show the first lines and expand.
- **With header** or **bare**.

## States

| State | Treatment |
|---|---|
| Default | `consent` ground, `text-primary` |
| Copy hover / pressed | `control-hover` / `brightness(0.92)` |
| Copied | the action's word swaps to the product's confirmation for about 2 seconds and a polite live region announces it; the glyph does not animate |
| Streaming | new lines append at the end; the block does not jump to the top; under Reduce Motion lines appear without a fade |
| Redacted | the product's marker on a `neutral-tint` chip, never a blank |
| Empty | the product's sentence in caption type instead of an empty block |
| Increased contrast | 1px `edge-hc` inset edge |

## Behavior

- The whole body is selectable; Cmd-A or Ctrl-A inside a focused block selects the block only.
- Copy copies the raw text (no line numbers, no redaction chips' styling, the redaction marker as text).
- A scrolling block is a tab stop when it overflows, so arrow keys can scroll it.
- Long single tokens (hashes, URLs) break anywhere in the wrapped variant.
- Motion: fills on `duration-fast`; nothing moves.

## Accessibility

- Use `<figure>` with a `<figcaption>` (visible header or visually hidden) and `<pre><code>`. The copy button names its action from the product ("Copy"), with the block's label as its description.
- Text roles use text tokens that hold 4.5:1 on `consent`; color never carries meaning alone.
- Screen readers read code as text; do not insert visual-only characters into the copied or read text.
- The consumer supplies the text, the header label, the copy and copied words and the redaction marker.

## Platforms

| SwiftUI/AppKit (macOS) | SwiftUI/UIKit (iOS/iPadOS) | Jetpack Compose M3 | Web |
|---|---|---|---|
| `GlassCode(text)`: mono `Text` with `.textSelection(.enabled)` on `consentFill`; a `ScrollView(.horizontal)` for the scrolling variant; `NSPasteboard` copy | The same; `UIPasteboard`; a `DisclosureGroup` to expand long blocks | `SelectionContainer { Text(fontFamily = FontFamily.Monospace) }` on a 14dp `Surface`; `horizontalScroll` for code; `ClipboardManager` | `<figure class="nr-code-block">` with `.nr-code-block__header` and `<pre class="nr-code-block__pre">` |

## Do and don't

- Do keep code on the consent ground. Don't put a code block on glass or in a tooltip.
- Do make output, errors and request IDs copyable. Don't block selection.
- Do scroll code sideways and wrap transcripts. Don't scroll both ways in a small block.
- Don't color code with series or status colors; use the text roles.

## Source

`GlassCode` in StatCard.swift (mono 11 on `consentFill`, 12 padding, selectable, `cardQuiet` radius) [trace-commons §4.5]; HIG text views ("make useful text selectable"); App UI's CodeBlock for the header and copy anatomy; M3 cards for not scrolling inside a container on mobile.
