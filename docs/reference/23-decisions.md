# Decisions and open questions

One register for the system. IDs are NDS-n and never reuse a product's own decision IDs (trace-commons has four colliding schemes: the #1173 D and R items, the R15 plan's D-1 to D-21, the glass spec's numbered decisions, and the Insights D1 to D8).

## Owner decisions

Made by the owner on 2026-10-13. They bind the system until the owner changes them.

| ID | Decision | Consequence |
|---|---|---|
| NDS-1 | **Neutral parent, product accents.** The parent defines roles; each product supplies its accent family. | The parent default accent is NEAR AI blue, derived from `brand-blue` #0091fd. Trace keeps purple in dark and blue in light as the `trace-` themes. |
| NDS-2 | **Flat glass is the baseline.** | Flat fills, no rims, larger radii, one soft shadow for floating things. Classic glass is an optional expressive treatment (`edge-classic-*`). |
| NDS-3 | **Shared core, native idioms.** | One token and semantics layer. Apple platforms use their native navigation and controls; Android uses Material 3 Expressive components in NEAR tokens; the web uses Material's adaptive layouts with CSS glass on navigation only. |
| NDS-4 | **Platform system faces on one shared scale.** | SF Pro and SF Mono on Apple only; Roboto Flex on Android; Segoe UI Variable on Windows; `system-ui` on the web. No bundled brand face. |
| NDS-5 | **Focus ring: product choice.** | The parent specifies a 2px `focus-ring` outline 2px outside the control and turns it on by default. A product may turn it off (`.nr-focus-off`). Turning it off fails WCAG 2.4.7. Trace has it off (its own ruling, 2026-10-11). |
| NDS-6 | **Strict contrast floors, no overrides.** | Text 4.5:1 and state marks 3:1 in every theme, over the worst-case ground behind glass; 7:1 text in the `-hc` themes. Source values that miss stay exact in their product theme, flagged, and block that theme from shipping until fixed. |
| NDS-7 | **Apple platforms keep Trace's painted glass.** | Veil and flat fill painted over the native material; floating surfaces painted over a within-window blur; the Mac control ladder 26 / 28 / 30 / 34. Painted surfaces do not follow the person's Clear-to-Tinted glass setting. |
| NDS-8 | **Marks come from the NEAR AI logo kit.** | Primary, secondary and tile lockups with clear-space guides (asset group Logos). The Trace mark and The Turn are Trace product marks (asset group Trace). |

## System defaults

Set when the system was written, from the research and the source code. The owner can revise any of them.

| ID | Default | Why |
|---|---|---|
| NDS-9 | Glass only on the navigation and floating layers; content is painted; never glass on glass. On phones and tablets the screen is an opaque pane and only chrome is glass. | Apple: "Don't use Liquid Glass in the content layer." trace-commons already paints everything inside a pane. |
| NDS-10 | Four densities (compact, regular, touch, dense); touch targets never below 44pt (Apple), 48dp (Android, touch web), 60pt (visionOS). | trace-commons is pointer-first (22 to 34pt); Unity's Editor sets the dense benchmark (16 to 20px rows). |
| NDS-11 | One curve for non-spatial change; standard springs for movement; the expressive spring for one or two hero moments; nothing moves under Reduce Motion. | trace-commons' one-curve rule; Material's standard and expressive schemes; Apple and Material both keep navigation on platform defaults. |
| NDS-12 | Layout classes are Material 3's breakpoints (600, 840, 1200, 1600) measured on the window or container; Apple size classes only pick idiom components. | One classification for every platform; size classes are binary. |
| NDS-13 | Navigation: bottom tab bar on phones, sidebar-adaptable tab bar or rail on tablets, sidebar or three-pane window plus toolbar and menu bar on desktop. No navigation drawer. | HIG tab bars and sidebars; Material deprecated the drawer in favor of the expanded rail. |
| NDS-14 | One command registry, rendered as the menu bar, context menus, a command palette (web, Windows, Linux), `Mod+Key` shortcuts and App Intents. Esc and Cmd-. stop a running generation. | HIG: every command in the macOS menu bar (now iPadOS too). |
| NDS-15 | Reversible actions act at once with Undo (a toast on every platform); confirm only irreversible or consent actions; destructive is never the default; an irreversible send is prominent but never answers Return. | trace-commons' confirmation ladder; HIG prefers undo to confirmation; Material's snackbar. |
| NDS-16 | Copy is single-sourced per product; components author no words; status is a dot plus words; unknown is a dash or "unknown", never zero. | trace-commons: the Rust core owns every sentence. |
| NDS-17 | Appearance follows the system; an in-app Light / Dark / System choice is allowed. Increased contrast follows the system. | Trace ships the in-app choice; Apple advises against it, the web and Android expect it. |
| NDS-18 | The web uses its own components on the parent tokens (React with headless accessible primitives). material-web is a reference only. | material-web is in maintenance mode, Expressive is "not planned", and its labs suite is unstable. |
| NDS-19 | Cancel leading, the primary action trailing, on every platform including the Windows and Linux shells. | Apple and Material agree; the Windows shells render the web. |
| NDS-20 | Charts plot on the opaque `surface-chart` with `data-1` to `data-8` in fixed order, one axis, a legend for two or more series and a table view. | A validated palette needs a known ground; glass is not one. |
| NDS-21 | Settings: a window on macOS (Cmd-,), a screen on iOS and Android, a page on the web; never a modal over the main window. | trace-commons settled on its own window (owner, 2026-10-08) after two reversals. |

## Open questions for the owner

1. **Trace contrast.** Three Trace values miss the floors: the dark selected fill #6d14f3 at 1.09:1 against the pane over a white desktop, and the hidden-toolbar glyph at 2.63:1 (dark) and 2.27:1 (light). Under NDS-6 the Trace theme ships under the parent only once they are fixed. The parent fixed its own versions. For Trace dark, `make accent SEED=#6d14f3` proposes a lavender selected fill #b5aaff with a dark label (#071a2e, 8.5:1), 3.06:1 against the worst pane, the way the parent handles blue; the hidden-toolbar glyph needs the parent's solved greys (#75757b light, #8d8d97 dark).
2. **Painted glass on macOS 27 (NDS-7).** macOS 27 draws its own darker edge and brighter highlight on glass, and adds a continuous Clear-to-Tinted setting. Painted panes ignore that setting. Review once the Trace team has measured both on device.
3. **Trace focus ring (NDS-5).** Allowed, and it fails WCAG 2.4.7 for keyboard users. Restoring it on the Monitor window is a one-line change per scene.
4. **Brand architecture.** How "Near.ai" (the macOS app name), NEAR AI (the master brand), Trace (the product theme) and Trace Commons (the commons) appear together, and whether The Turn retires in favor of the Trace mark. The logo kit sets no minimum sizes.
5. **Copy ownership beyond macOS.** Trace's Rust core owns every sentence for the desktop shells. Web and mobile need a decision: read the same tables, or a per-product copy service.
6. **The default parent accent.** NDS-1 left the parent neutral; the system uses NEAR AI blue from the logo kit as its default. Confirm, or name another.
7. **Classic glass.** Kept as an optional expressive treatment. Confirm whether any product will use it; if none, retire the `edge-classic-*` tokens.

## Dependencies outside this system

- **Apple Liquid Glass APIs** require the 26 SDKs; macOS 14 to 25 use the vibrancy fallback. Building with the 27 SDK ignores the opt-out key for the old design.
- **Material 3 Expressive** components ship in Compose Material 3 1.5, which is in beta (1.5.0-beta01, 7 October 2026); 1.4 is the stable line. MDC Views 1.14 is its final release.
- **Unity App UI 3.x** exists only as a pre-release (3.0.0-pre.1); its latest stable is 2.1.14. The dense specs here come from Editor Foundations and the 3.0 manual, not from code we depend on.
- **material-web** ships the Expressive token set in 2.5.0 but no stable Expressive components.
- **Figma.** The three Unity community files could be read only partly: the Figma connector's Starter-plan call limit stopped the read, and community files bill to that plan rather than the team seat. Duplicating them into the team's workspace, or enabling the Dev Mode MCP server in Figma desktop, would allow a complete read of their internal paddings and radii.
- **trace-commons** keeps its own token source and generator; the parent does not change that repository.
