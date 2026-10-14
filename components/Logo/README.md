# Logo

The NEAR AI master-brand lockups from the logo kit, placed on the right ground for the theme.

## When to use
Use the primary wordmark wherever NEAR AI introduces itself: the web app header, sign-in, about and settings screens, onboarding, marketing. Use the secondary lockup when the wordmark does not fit (headers under 600px, compact toolbars). Use the tile only where an app icon would appear. Inside a product, the product name and mark (for Trace, `TraceMark`) lead and the NEAR AI lockup sits in the footer or about screen.

## Anatomy
1. Lockup image (an uploaded SVG asset; never inline, never redrawn).
2. Clear space: the margin drawn in the kit's clear-space files, about one fifth of the lockup's height on every side.
3. Ground: `brand-paper`, a light pane, or any light theme ground for the color lockup; `brand-ink`, a dark pane, or any dark theme ground for the white-and-color lockup.

## Sizes by density
| Context | Primary (730 by 138) | Secondary (291 by 136) | Tile (400 by 396) |
|---|---|---|---|
| Web header (regular) | 24px tall | 24px tall | n/a |
| Desktop about window (compact) | 28px tall | 28px tall | 64px |
| Phone header (touch) | 20px tall | 24px tall | n/a |
| Sign-in and onboarding hero | 40 to 56px tall | 48px tall | 96px |
The kit sets no minimum size; ask the brand owner before going below 72px wide for the wordmark.

## Variants
- `color`: light grounds. `white-color`: dark grounds. Theme switching picks between them (`.nr-logo--for-light`, `.nr-logo--for-dark`).
- `black` and `white`: single ink, for one-color contexts only.
- `tile` (a `brand-tile` tile with a `brand-paper` "N") and `tile-white-color` (a white tile with a `brand-tile` "N"): app-icon contexts.

## States
None. A logo is never a button by itself; when it links home, the link's focus ring (`focus-ring`) draws around the clear-space box.

## Behavior
No motion. The logo never animates, morphs or takes a glass effect.

## Accessibility
`alt="NEAR AI"` on the image; when the logo is a home link, the link's accessible name is "NEAR AI, home". Decorative repeats (a footer under a header that already names NEAR AI) take `alt=""`.

## Platforms
| macOS (SwiftUI/AppKit) | iOS/iPadOS | Android (Compose) | Web |
|---|---|---|---|
| Asset catalog SVG (single-scale, preserve vector data), `Image("near-ai-primary-color")` with a dark appearance variant | Same asset catalog | Vector drawable converted from the SVG, `painterResource` with a `-night` variant | `<img src>` of the uploaded asset; swap by theme with `.nr-logo--for-light` / `.nr-logo--for-dark` |

## Do and don't
- Do keep the kit's clear space on every side.
- Do use the white-and-color lockup on glass panes in the dark themes.
- Don't recolor the wordmark with a product accent (Trace purple included).
- Don't set "NEAR AI" in type to imitate the wordmark.
- Don't place a lockup over busy scene glows without a pane behind it.

## Source
Intentional addition: the NEAR AI logo kit (Primary, Secondary, Tertiary, with clear-space guides), supplied by the owner (decision NDS-8). trace-commons used the "N" only as a map texture (`GlassBrandMark`).
