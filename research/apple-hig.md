# Apple Human Interface Guidelines: research findings for the NEAR AI parent design system

Source: the complete Apple HIG, crawled from DocC JSON on 2026-10-13. That is 173 pages: the index plus 172 pages, every doc://com.apple.HIG identifier referenced anywhere, with 0 page failures. Corpus: corpus/apple-hig/*.txt plus index.tsv. Converter and crawler: scripts/apple-hig/.
Tags: [AI] marks guidance that matters for an AI product. [XPLAT] marks a conflict with, or decision against, Material, Windows or web conventions. Citations use the form [hig:slug].
Not in the current HIG: the layout page (revised 2026-09-09) no longer has device screen-size or size-class tables. There are no pages for Writing Tools or Visual Intelligence, and no standalone Apple Intelligence page. Navigation bars were folded into Toolbars in June 2025.

# 1. Foundations

# A. HIG Foundations, part 1

Pages read in full: accessibility, app-icons, branding, color, dark-mode, icons, images, inclusion, materials, motion (corpus snapshot Oct 2026).

Tags: **[AI]** marks items especially relevant to an AI product. **[XPLAT]** marks a conflict with Material / Windows / web, or a point where the parent system must pick one rule. Hex values and contrast ratios marked *derived* are our calculations from the HIG's RGB values.

---

## Accessibility `[hig:accessibility]`

**Purpose:** make the interface **Intuitive** (familiar, consistent), **Perceivable** (never rely on one sense) and **Adaptable** (honor system features and personal settings). Audit with Accessibility Inspector, and declare support through App Store **Accessibility Nutrition Labels** (new in 2025).

**Scope:** VoiceOver guidance now lives in `[hig:voiceover]` and Dynamic Type in `[hig:typography]` (moved Mar 7 2025). This page has **no Reduce Transparency section**. That setting appears only in `[hig:dark-mode]` (as a test condition) and `[hig:materials]` (it changes glass).

### Vision
- **Text must enlarge by at least 200%** (watchOS: **140%**), using Dynamic Type or custom UI. **[XPLAT]** This matches WCAG 1.4.4. Map it to Android font scale and browser zoom.
- If you define custom type styles, use the platform defaults and minimums below. Thin weights need sizes larger than these.

| Platform | Default size | Minimum size |
|---|---|---|
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

  **[XPLAT]** Body text is 17 pt on iOS, against about 14–16 sp in Material and 16 px on the web. macOS uses 13 pt, against 14 px in Fluent. The parent type ramp therefore needs a separate base per family: mobile, desktop-native and web.
- **Contrast:** Apple cites WCAG and APCA. Accessibility Inspector applies these WCAG AA values:

| Text size | Text weight | Minimum contrast ratio |
|---|---|---|
| Up to 17 pts | All | 4.5:1 |
| 18 pts | All | 3:1 |
| All | Bold | 3:1 |

  **[XPLAT]** Apple's 18 pt (about 18 CSS px) "large" threshold is looser than WCAG, where large means 24 px regular or about 18.7 px bold. Apple's "any bold size → 3:1" row is looser still. **Adopt WCAG's px thresholds everywhere.**
- If the defaults fall short, offer a higher-contrast scheme at least under **Increase Contrast**, and check both appearances. Prefer system colors, which include accessible variants.
- **Never use color alone** (red–green and blue–orange fail). Add shapes or icons, and let people customize palettes such as chart colors. Describe all UI for VoiceOver.

### Hearing
- Audio must never be the only channel. Provide **captions** (synchronized text), **subtitles** (translated dialogue), **audio descriptions** (narration in natural pauses) and **transcripts** (complete audio and visual text), and let people style the text. **[AI]** Voice output from the assistant needs live text and a transcript.
- Pair audio cues with **haptics** (iOS also offers Music Haptics and Audio graphs) and with **visual cues**, especially for off-screen sources.

### Mobility

| Platform | Default control size | Minimum control size |
|---|---|---|
| iOS, iPadOS | 44x44 pt | 28x28 pt |
| macOS | 28x28 pt | 20x20 pt |
| tvOS | 66x66 pt | 56x56 pt |
| visionOS | 60x60 pt | 28x28 pt |
| watchOS | 44x44 pt | 28x28 pt |

- **Spacing:** about **12 pt** of padding around bezeled elements and about **24 pt** around the visible edges of bezel-less ones.
- **[XPLAT]** Material uses a 48 dp target, Fluent touch about 40 epx, and WCAG 2.2 requires 24 px (AA, 2.5.8) or 44 px (AAA, 2.5.5). Suggested parent rule: touch 44 default / 28 minimum, pointer desktop 28 / 20, with spacing so every touch target is effectively 44.
- Use simple gestures for frequent actions, with no custom multi-finger gestures. **Give every gesture an on-screen alternative**, such as swipe-to-delete plus an Edit mode.
- Support **Voice Control** (needs good labels), **Siri/Shortcuts** (Action button, Home Screen, Control Center), **VoiceOver, AssistiveTouch, Full Keyboard Access, Pointer Control and Switch Control**. **[AI]** Expose agent actions as intents/Shortcuts.

### Speech
- **Full keyboard operation** (Full Keyboard Access). Never override system shortcuts. **[XPLAT]** Define one focus and keyboard model across web, Windows and macOS.
- **Switch Control** must work. It drives the device through external hardware, game controllers or sounds (clicks, pops).

### Cognitive
- **Minimize time-boxed UI.** Prefer explicit dismissal to auto-dismiss timers. **[AI]** **[XPLAT]** Material snackbars and web toasts auto-dismiss after about 4–10 s. Parent rule: never auto-dismiss a message that carries an action (Undo, Retry, Approve) or an error.
- Games: offer difficulty accommodations (looser criteria, reaction time, control assistance).
- **No autoplay** without discoverable start/stop controls. Offer a global opt-out. Honor **Dim Flashing Lights**.
- **Reduce Motion:** reduce automatic and repetitive animation (zoom, scale, peripheral motion). Tighten springs to cut bounce, track animation to the gesture, avoid z-axis depth animation, replace x/y/z movement with fades, and avoid animating into or out of blur. **[AI]** This covers streaming shimmer, "thinking" pulses and auto-scroll. **[XPLAT]** Map to `prefers-reduced-motion`, Android "Remove animations" and Windows "Animation effects".
- **Assistive Access** (iOS/iPadOS): keep core functions only, one interaction per screen, and **confirm twice** before hard-to-recover actions such as deleting a file. **[AI]** Use the same pattern for consequential agent actions.

### Platforms
- iOS, iPadOS, macOS, tvOS, watchOS: nothing additional.
- **visionOS** (Pointer Control, Zoom): keep UI in view and prefer horizontal layouts. Slow peripheral animation, keep camera motion gentle, **don't head-lock content** (it breaks Pointer Control), and avoid large repetitive gestures.

**Change log:** Jun 9 2025 Assistive Access, Switch Control, Nutrition Labels. Mar 7 2025 rewrite and page split. Jun 10 2024 Unity Dynamic Type. Dec 5 2023 visionOS Zoom art. Jun 21 2023 visionOS. **New:** WWDC26 session "Refine accessibility for custom controls".

---

## App icons `[hig:app-icons]`

**Purpose:** a unique, recognizable identity mark that appears on the Home Screen, in search, notifications, Settings and share sheets.

### Layers (Liquid Glass era: 2025, refined Jun 2026)
- **iOS, iPadOS, macOS, watchOS:** a background layer plus one or more foreground layers. The system adds Liquid Glass effects (specular highlights, refraction, translucency), which vary by size and OS. Build in **Icon Composer**, which handles background, placement, effects, default/dark/mono annotation and export.
- **tvOS:** **2–5 layers** with parallax. **visionOS:** background plus **1–2 layers** as a 3D object. Both use an Xcode image stack.
- Give foreground layers crisp edges, not feathered ones. Vary their opacity for depth, setting transparency in Icon Composer. Imported backgrounds must be **full-bleed and opaque**, and gradients must survive system lighting.
- Prefer **vector** (SVG/PDF) with text outlined; use **PNG** for mesh gradients and raster art.

### Shape
- iOS/iPadOS/macOS: square art, masked to a rounded rectangle concentric with the device corners. tvOS: rectangular art with rounded corners. visionOS/watchOS: square art, masked to a **circle**.
- **Supply unmasked layers.** Pre-masked art breaks specular highlights and leaves jagged edges. **Center primary content**, especially under the circular masks, using the Apple Design Resources grids.

### Design
- One core idea, few shapes, a simple background, and the same design on every platform. Overlapping semi-transparent fills give depth.
- **No text** unless essential (a one-letter mnemonic is fine; never "Play" or "New"). Illustration, not photos. No UI replicas, hairlines, sharp corners or Apple hardware.
- **Don't bake in effects** (shadows, bevels, blur, glow). **Group layers** to get group-level glass settings. Test in Icon Composer or Device Hub.

### Appearances (iOS, iPadOS, macOS)
- **Default, dark, clear light, clear dark, tinted light, tinted dark.** The system generates any variant you omit.
- Keep the same features in every variant. Derive dark from light with complementary, not-too-bright colors; colored backgrounds give dark icons the most contrast.
- **Alternate icons** (iOS, iPadOS, tvOS, compatible visionOS apps): each needs its own dark, clear and tinted variants, and all go through App Review.

### Platforms
- iOS, iPadOS, macOS: nothing additional.
- **tvOS:** keep a safe zone. Foreground layers are cropped more than background layers during focus.
- **visionOS:** no "hole" or concave shapes in the background, because shading makes them protrude.
- **watchOS:** no black background; lighten it.

### Specifications

| Platform | Layout shape | Icon shape after system masking | Layout size | Style | Appearances |
|---|---|---|---|---|---|
| iOS, iPadOS, macOS | Square | Rounded rectangle (square) | 1024x1024 px | Layered | Default, dark, clear light, clear dark, tinted light, tinted dark |
| tvOS | Rectangle (landscape) | Rounded rectangle (rectangular) | 800x480 px | Layered (Parallax) | N/A |
| visionOS | Square | Circular | 1024x1024 px | Layered (3D) | N/A |
| watchOS | Square | Circular | 1088x1088 px | Layered | N/A |

- The system scales down to every smaller size. **This edition publishes no per-size table, corner radius or grid dimensions**; grids are only in the Design Resources templates.
- **Color spaces:** sRGB, Gray Gamma 2.2, and Display P3 (iOS, iPadOS, macOS, tvOS, watchOS only; **not visionOS**).
- **[XPLAT]** Android adaptive icons: two layers, 108 dp canvas, 72 dp safe zone, OEM mask, monochrome themed layer. Windows and web (favicon, PWA maskable) need flat multi-size assets. Keep one square, unmasked, center-safe master and export per platform.

**Change log:** Jun 8 2026 Liquid Glass refinements. Jun 9 2025 layered icons and Liquid Glass. Jun 10 2024 dark/tinted. Jan 31 2024 alternate icons. Jun 21 2023 visionOS. Sep 14 2022 Watch Ultra.

---

## Branding `[hig:branding]`

**Purpose:** a recognizable brand that still feels native to the platform.
- Keep a consistent brand **voice and tone** in all copy. **[AI]** This governs assistant-persona wording.
- **Use the accent color sparingly (refined Sep 9 2026).** Keep it off most controls and reserve it for primary actions and status (badges, the selected tab). **New:** move brand color into the **content layer**, where it scrolls under Liquid Glass and the glass picks it up. For a purple brand, that means purple content and neutral chrome.
- A custom font must stay legible at all sizes and support Bold Text and Dynamic Type. A good split is custom headlines with system body text and captions.
- Brand familiar components without changing their sizing, placement or behavior. Branding defers to content: no logo-only space, no repeated logos. Keep standard locations, symbols, navigation and modality.
- **The launch screen is not for branding**; put branding in welcome or onboarding. **[XPLAT]** Android 12+ SplashScreen shows the icon, and web/Electron splash screens are often branded. Parent rule: icon at most on launch, branding in onboarding.
- No Apple trademarks. **Platforms:** nothing additional. **Change log:** Sep 9 2026 brand-color guidance. WWDC26 session "Communicate your brand identity on iOS".

---

## Color `[hig:color]`

**Purpose:** color for communication, brand, continuity, status and feedback, adapting to appearance and accessibility settings.

### Best practices
- **One meaning per color.** Don't style non-interactive text in the color that marks interactive elements.
- **Every color needs four values:** light and dark, each with an **increased-contrast** version. Supply light and dark even for single-appearance apps, because Liquid Glass adapts.
- Test across lighting (bright light mutes, dim light saturates) and devices (True Tone, HD/4K TVs, P3 vs sRGB). Artwork and translucency shift nearby colors. Use the system color picker.

### Inclusive color
- Never use color alone for identity, interactivity or essential information. Add labels or glyphs, and avoid low-contrast and color-blind-confusable pairs.
- **Meaning varies by culture.** Red means gains in Chinese stock apps. **[XPLAT]** Success/danger tokens may need locale overrides in charts.

### System and semantic colors
- **Don't hard-code** documented values; they change between releases. Use APIs.
- iOS, iPadOS, macOS and visionOS have **dynamic semantic colors** named by purpose. **Don't repurpose them** (no separator color for text, no secondaryLabel for backgrounds). **[XPLAT]** Parent tokens should be role-based, as in Material 3 and Fluent. Map roles across platforms, not hex values.

### Liquid Glass color (brief)
- Glass has no inherent color; it takes color from the content behind it. Tint glass only for emphasis. The **prominent button** puts the accent color on the glass *background*.
- Small glass (toolbars, tab bars) flips light or dark with the content, with monochrome glyphs. Large glass (sidebars) is more opaque.
- **Color sparingly**, only for primary actions or status, on the background rather than the glyph. **Never tint several controls.** Over colorful content, keep bars monochrome; with monochrome content, a brand accent works well. Keep the **scroll-top resting state** legible.

### Color management
- Embed **color profiles**. sRGB is accurate on most displays.
- **Wide color:** Display P3 at **16 bits per channel**, exported as **PNG**, designed on a P3 display. Close P3 colors can merge, and P3 gradients can clip, on sRGB; supply per-gamut variants when that matters. **[XPLAT]** Web: `color(display-p3 …)` inside `@media (color-gamut: p3)` with sRGB fallback. Author tokens in sRGB and add P3 as an enhancement.

### Platforms
- **iOS/iPadOS backgrounds:** two sets, *system* (`systemBackground` / `secondary…` / `tertiary…`) and *grouped* (`systemGroupedBackground` / `secondary…` / `tertiary…`, for grouped tables). Primary is the whole view, secondary groups content within it, tertiary groups within secondary.
- **iOS foreground colors:**

| Color | Use for… | UIKit API |
|---|---|---|
| Label | A text label that contains primary content. | `label` |
| Secondary label | A text label that contains secondary content. | `secondaryLabel` |
| Tertiary label | A text label that contains tertiary content. | `tertiaryLabel` |
| Quaternary label | A text label that contains quaternary content. | `quaternaryLabel` |
| Placeholder text | Placeholder text in controls or text views. | `placeholderText` |
| Separator | A separator that allows some underlying content to be visible. | `separator` |
| Opaque separator | A separator that doesn’t allow any underlying content to be visible. | `opaqueSeparator` |
| Link | Text that functions as a link. | `link` |

- **macOS dynamic system colors:**

| Color | Use for… | AppKit API |
|---|---|---|
| Alternate selected control text color | The text on a selected surface in a list or table. | `alternateSelectedControlTextColor` |
| Alternating content background colors | The backgrounds of alternating rows or columns in a list, table, or collection view. | `alternatingContentBackgroundColors` |
| Control accent | The accent color people select in System Settings. | `controlAccentColor` |
| Control background color | The background of a large interface element, such as a browser or table. | `controlBackgroundColor` |
| Control color | The surface of a control. | `controlColor` |
| Control text color | The text of a control that is available. | `controlTextColor` |
| Current control tint | The system-defined control tint. | `currentControlTint` |
| Unavailable control text color | The text of a control that’s unavailable. | `disabledControlTextColor` |
| Find highlight color | The color of a find indicator. | `findHighlightColor` |
| Grid color | The gridlines of an interface element, such as a table. | `gridColor` |
| Header text color | The text of a header cell in a table. | `headerTextColor` |
| Highlight color | The virtual light source onscreen. | `highlightColor` |
| Keyboard focus indicator color | The ring that appears around the currently focused control when using the keyboard for interface navigation. | `keyboardFocusIndicatorColor` |
| Label color | The text of a label containing primary content. | `labelColor` |
| Link color | A link to other content. | `linkColor` |
| Placeholder text color | A placeholder string in a control or text view. | `placeholderTextColor` |
| Quaternary label color | The text of a label of lesser importance than a tertiary label, such as watermark text. | `quaternaryLabelColor` |
| Secondary label color | The text of a label of lesser importance than a primary label, such as a label used to represent a subheading or additional information. | `secondaryLabelColor` |
| Selected content background color | The background for selected content in a key window or view. | `selectedContentBackgroundColor` |
| Selected control color | The surface of a selected control. | `selectedControlColor` |
| Selected control text color | The text of a selected control. | `selectedControlTextColor` |
| Selected menu item text color | The text of a selected menu. | `selectedMenuItemTextColor` |
| Selected text background color | The background of selected text. | `selectedTextBackgroundColor` |
| Selected text color | The color for selected text. | `selectedTextColor` |
| Separator color | A separator between different sections of content. | `separatorColor` |
| Shadow color | The virtual shadow cast by a raised object onscreen. | `shadowColor` |
| Tertiary label color | The text of a label of lesser importance than a secondary label. | `tertiaryLabelColor` |
| Text background color | The background color behind text. | `textBackgroundColor` |
| Text color | The text in a document. | `textColor` |
| Under page background color | The background behind a document’s content. | `underPageBackgroundColor` |
| Unemphasized selected content background color | The selected content in a non-key window or view. | `unemphasizedSelectedContentBackgroundColor` |
| Unemphasized selected text background color | A background for selected text in a non-key window or view. | `unemphasizedSelectedTextBackgroundColor` |
| Unemphasized selected text color | Selected text in a non-key window or view. | `unemphasizedSelectedTextColor` |
| Window background color | The background of a window. | `windowBackgroundColor` |
| Window frame text color | The text in the window’s title bar area. | `windowFrameTextColor` |

  **[XPLAT]** Desktop tokens need separate selection colors for focused (key) and unfocused windows, a distinction web and Windows rarely make.
- **macOS app accent (macOS 11+):** applies to buttons, selection and sidebar icons **only when the user's accent setting is "multicolor"**. Any other user choice overrides it, except fixed-color sidebar icons. **[XPLAT]** Windows has a system accent and Android 12+ has Material You dynamic color. Parent rule: a "respect system accent" mode per platform, with brand color kept in content.
- **tvOS:** a limited palette tied to the logo. **Never show focus with color alone**; use scale and motion.
- **visionOS:** use color sparingly on glass, since surroundings show through. Prefer color in **bold text and large areas**. In full immersion, balance brightness and avoid bright or flashing objects on black.
- **watchOS:** background color must carry meaning (as in the Activity rings). No full-screen color in long-running views. Complications may render in tinted mode.

### Specifications: system colors (values updated Jun 9 2025)
The HIG now publishes **one cross-platform table**; **visionOS uses the Default (dark) column**. RGB values are verbatim; hex is *derived*.

| Name | SwiftUI API | Default (light) | Default (dark) | Increased contrast (light) | Increased contrast (dark) |
|---|---|---|---|---|---|
| Red | `red` | 255,56,60 `#FF383C` | 255,66,69 `#FF4245` | 233,21,45 `#E9152D` | 255,97,101 `#FF6165` |
| Orange | `orange` | 255,141,40 `#FF8D28` | 255,146,48 `#FF9230` | 197,83,0 `#C55300` | 255,160,86 `#FFA056` |
| Yellow | `yellow` | 255,204,0 `#FFCC00` | 255,214,0 `#FFD600` | 161,106,0 `#A16A00` | 254,223,67 `#FEDF43` |
| Green | `green` | 52,199,89 `#34C759` | 48,209,88 `#30D158` | 0,137,50 `#008932` | 74,217,104 `#4AD968` |
| Mint | `mint` | 0,200,179 `#00C8B3` | 0,218,195 `#00DAC3` | 0,133,117 `#008575` | 84,223,203 `#54DFCB` |
| Teal | `teal` | 0,195,208 `#00C3D0` | 0,210,224 `#00D2E0` | 0,129,152 `#008198` | 59,221,236 `#3BDDEC` |
| Cyan | `cyan` | 0,192,232 `#00C0E8` | 60,211,254 `#3CD3FE` | 0,126,174 `#007EAE` | 109,217,255 `#6DD9FF` |
| Blue | `blue` | 0,136,255 `#0088FF` | 0,145,255 `#0091FF` | 30,110,244 `#1E6EF4` | 92,184,255 `#5CB8FF` |
| Indigo | `indigo` | 97,85,245 `#6155F5` | 109,124,255 `#6D7CFF` | 86,74,222 `#564ADE` | 167,170,255 `#A7AAFF` |
| Purple | `purple` | 203,48,224 `#CB30E0` | 219,52,242 `#DB34F2` | 176,47,194 `#B02FC2` | 234,141,255 `#EA8DFF` |
| Pink | `pink` | 255,45,85 `#FF2D55` | 255,55,95 `#FF375F` | 231,18,77 `#E7124D` | 255,138,196 `#FF8AC4` |
| Brown | `brown` | 172,127,94 `#AC7F5E` | 183,138,102 `#B78A66` | 149,109,81 `#956D51` | 219,166,121 `#DBA679` |

### iOS, iPadOS system gray colors (SwiftUI `gray` = `systemGray`)

| Name | UIKit API | Default (light) | Default (dark) | Increased contrast (light) | Increased contrast (dark) |
|---|---|---|---|---|---|
| Gray | `systemGray` | 142,142,147 `#8E8E93` | 142,142,147 `#8E8E93` | 108,108,112 `#6C6C70` | 174,174,178 `#AEAEB2` |
| Gray (2) | `systemGray2` | 174,174,178 `#AEAEB2` | 99,99,102 `#636366` | 142,142,147 `#8E8E93` | 124,124,128 `#7C7C80` |
| Gray (3) | `systemGray3` | 199,199,204 `#C7C7CC` | 72,72,74 `#48484A` | 174,174,178 `#AEAEB2` | 84,84,86 `#545456` |
| Gray (4) | `systemGray4` | 209,209,214 `#D1D1D6` | 58,58,60 `#3A3A3C` | 188,188,192 `#BCBCC0` | 68,68,70 `#444446` |
| Gray (5) | `systemGray5` | 229,229,234 `#E5E5EA` | 44,44,46 `#2C2C2E` | 216,216,220 `#D8D8DC` | 54,54,56 `#363638` |
| Gray (6) | `systemGray6` | 242,242,247 `#F2F2F7` | 28,28,30 `#1C1C1E` | 235,235,240 `#EBEBF0` | 36,36,38 `#242426` |

**Derived WCAG contrast** (light values against `#FFFFFF`, dark values against `#000000`, plus dark default against `#1C1C1E`):

| Color | Light default on white | Light IC on white | Dark default on black | Dark IC on black | Dark default on `#1C1C1E` |
|---|---|---|---|---|---|
| Red | 3.57 | 4.56 | 6.12 | 7.15 | 4.96 |
| Orange | 2.31 | 4.55 | 9.41 | 10.41 | 7.62 |
| Yellow | 1.51 | 4.59 | 14.87 | 15.85 | 12.05 |
| Green | 2.22 | 4.54 | 10.39 | 11.42 | 8.42 |
| Mint | 2.12 | 4.55 | 11.82 | 12.79 | 9.57 |
| Teal | 2.16 | 4.57 | 11.30 | 12.74 | 9.15 |
| Cyan | 2.16 | 4.57 | 11.94 | 13.02 | 9.67 |
| Blue | 3.52 | 4.57 | 6.49 | 9.76 | 5.26 |
| Indigo | 5.09 | 6.12 | 5.98 | 9.84 | 4.84 |
| Purple | 4.17 | 5.21 | 5.79 | 9.75 | 4.69 |
| Pink | 3.65 | 4.57 | 5.96 | 9.68 | 4.83 |
| Brown | 3.53 | 4.58 | 6.84 | 9.74 | 5.54 |
| Gray | 3.26 | 5.23 | 6.44 | 9.50 | 5.22 |

**What this shows:** the light **increased-contrast** values sit just above **4.5:1 on white**. The light **default** values mostly *fail* AA for text (only Indigo passes); they are fill and tint colors. Parent rule: accent-as-text tokens use an IC-equivalent shade, and default accents are limited to fills and large or bold text. Brand purple must reach 4.5:1 as text in both modes.

**Change log:** Dec 16 2025 Liquid Glass. **Jun 9 2025 new system color values** (e.g. Blue is now `#0088FF`) and Liquid Glass. Feb 2 2024 gray APIs and visionOS brightness. Sep 12 2023 watchOS, tvOS swatches. Jun 21 2023 visionOS. Jun 5 2023 watchOS. Dec 19 2022 mint (dark) fix.

---

## Dark Mode `[hig:dark-mode]`

**Purpose:** a systemwide dark palette for low light. Dark colors are **not straight inversions** of light ones, and the system may raise perceptual contrast.
- **No app-specific appearance setting.** It doubles the settings people manage and makes the app look broken. **[XPLAT]** Web, Electron, Windows and Android apps commonly have an in-app System/Light/Dark toggle. Parent rule: *follow system* by default; allow an override on web and non-Apple desktop, and leave it out of Apple-native builds.
- Look right in both modes and handle **Auto** switching while running.
- **Test with Increase Contrast and Reduce Transparency**, separately and together. Increase Contrast in Dark Mode can *lower* the contrast of dark text on dark backgrounds.
- **Dark-only** is valid only for immersive media (Stocks is one example). **[AI]** A general AI app should support both modes.
- **Use adaptive colors** (`labelColor`, `controlColor`, `separator`, or Color Sets with bright and dim variants). Never hard-code.
- **Contrast: at least 4.5:1, aiming for 7:1** for custom color pairs, especially small text (7:1 is WCAG AAA).
- **Dim white backgrounds** in content images slightly so they don't glow.
- **Icons and images:** prefer SF Symbols (adaptive, tintable, vibrancy-aware). Make separate light and dark glyphs where edges disappear (a full moon needs an outline on light; a black oil drop needs a light rim on dark). Share one asset when it works in both modes; otherwise pair light and dark versions under one name.
- **Text:** use system label colors (primary through quaternary) and system text views.

### Platforms
- **iOS/iPadOS: base vs elevated backgrounds.** **Base** is dimmer and recedes. **Elevated** is brighter and advances, for popovers, sheets, multitasking and multiple windows. The system switches automatically, which custom backgrounds break. **[XPLAT]** Material 3 uses tonal surface-container steps and Fluent uses Mica, Acrylic and layer fills. Parent: `surface-base` plus `surface-elevated-1…n` tokens in dark mode.
- **macOS desktop tinting:** with the **graphite** accent, windows pick up color from the wallpaper. Give custom bezeled or backgrounded components some transparency, in neutral (uncolored) states only.
- tvOS: nothing additional. **visionOS and watchOS: Dark Mode not supported.**

**Change log:** Aug 6 2024 light/dark art.

---

## Icons (interface icons / glyphs) `[hig:icons]`

**Purpose:** simple, tintable glyphs that each express one concept, defined in black and clear areas. Distinct from detailed app icons.
- Make glyphs highly simplified with familiar metaphors. **Keep the set consistent** in size, detail, stroke weight and perspective; adjust individual dimensions for optical balance.
- **Match glyph weight to adjacent text.**
- **Optical centering:** asymmetric glyphs (such as a download arrow) look low when geometrically centered. Build the corrective padding into the asset.
- **No custom selected states** in standard toolbars, tab bars and buttons; the system handles them.
- Use gender-neutral, culture-neutral imagery. Avoid text; if a character is required, localize it. For abstract text lines, provide **RTL-flipped** versions.
- **Use vector (PDF/SVG)**, which scales automatically. PNG needs a file per scale. A custom SF Symbol can match the scale of adjacent text.
- **Give every custom icon an accessibility label.** No Apple hardware except official resources.

### Standard icons (new Jun 9 2025): SF Symbols for common actions
Blank cells in the HIG share the symbol of the row above; they are merged here as "A / B".

| Group | Action(s) | Symbol name |
|---|---|---|
| Editing | Cut | `scissors` |
| Editing | Copy | `document.on.document` |
| Editing | Paste | `document.on.clipboard` |
| Editing | Done / Save | `checkmark` |
| Editing | Cancel / Close | `xmark` |
| Editing | Delete | `trash` |
| Editing | Undo | `arrow.uturn.backward` |
| Editing | Redo | `arrow.uturn.forward` |
| Editing | Compose | `square.and.pencil` |
| Editing | Duplicate | `plus.square.on.square` |
| Editing | Rename | `pencil` |
| Editing | Move to / Folder | `folder` |
| Editing | Attach | `paperclip` |
| Editing | Add | `plus` |
| Editing | More | `ellipsis` |
| Selection | Select | `checkmark.circle` |
| Selection | Deselect / Close | `xmark` |
| Selection | Delete | `trash` |
| Text formatting | Superscript | `textformat.superscript` |
| Text formatting | Subscript | `textformat.subscript` |
| Text formatting | Bold | `bold` |
| Text formatting | Italic | `italic` |
| Text formatting | Underline | `underline` |
| Text formatting | Align Left | `text.alignleft` |
| Text formatting | Center | `text.aligncenter` |
| Text formatting | Justified | `text.justify` |
| Text formatting | Align Right | `text.alignright` |
| Search | Search | `magnifyingglass` |
| Search | Find / Find and Replace / Find Next / Find Previous / Use Selection for Find | `text.page.badge.magnifyingglass` |
| Search | Filter | `line.3.horizontal.decrease` |
| Sharing and exporting | Share / Export | `square.and.arrow.up` |
| Sharing and exporting | Print | `printer` |
| Users and accounts | Account / User / Profile | `person.crop.circle` |
| Ratings | Dislike | `hand.thumbsdown` |
| Ratings | Like | `hand.thumbsup` |
| Layer ordering | Bring to Front | `square.3.layers.3d.top.filled` |
| Layer ordering | Send to Back | `square.3.layers.3d.bottom.filled` |
| Layer ordering | Bring Forward | `square.2.layers.3d.top.filled` |
| Layer ordering | Send Backward | `square.2.layers.3d.bottom.filled` |
| Other | Alarm | `alarm` |
| Other | Archive | `archivebox` |
| Other | Calendar | `calendar` |

- **[AI]** Thumbs up/down are the canonical response-feedback glyphs. Copy, Undo/Redo, Share and Attach cover most chat actions.
- **[XPLAT]** SF Symbols are Apple-only. Build an **action → glyph map** (SF Symbols ↔ Material Symbols ↔ Fluent ↔ web set) keyed on this action list. Metaphors differ: Apple's Share (square with up-arrow) vs Android's node glyph, and Apple's horizontal "More" ellipsis vs Material's vertical ⋮.

### Platforms
- Nothing additional except macOS.
- **macOS document icons** (folded top-right corner; the system composites the app icon plus extension if you supply none): a custom icon combines a **background fill, a center image and text**, which the system masks and composites. Keep it simple, since it renders down to **16×16 px**; drop detail at small sizes and keep the top-right corner clear.
  - Background fill sizes: 512×512 @1x / 1024×1024 @2x; 256 / 512; 128 / 256; 32 / 64; 16 / 32 px.
  - The center image is **half the canvas** (16×16 inside a 32×32 icon). Sizes: 256 / 512; 128 / 256; 32 / 64; 16 / 32 px (@1x / @2x). Margin about **10%**, content about **80%** of the canvas (about 205×205 in 256).
  - Text defaults to the extension, auto-scaled and ALL CAPS. Supply a short term for an obscure extension ("scene" for `.scn`).

**Change log:** Jun 9 2025 standard-icons table. Jun 21 2023 visionOS.

---

## Images `[hig:images]`

**Purpose:** deliver artwork at the correct scale and format.
- A **point** is abstract: a variable number of pixels in 2D, and **an angle in visionOS**, so it scales with distance. @1x = 1 px per pt, @2x = 2:1, @3x = 3:1. Supply high-resolution versions of every bitmap, suffixed `@1x/@2x/@3x`.

| Platform | Scale factors |
|---|---|
| iPadOS, watchOS | @2x |
| iOS | @2x and @3x |
| visionOS | @2x or higher (see visionOS) |
| macOS, tvOS | @1x and @2x |

- **Design at the lowest resolution and scale up.** Put vector control points on whole values at 1× so they stay grid-aligned at 2× and 3×.

| Image type | Format |
|---|---|
| Bitmap or raster work | De-interlaced PNG files |
| PNG graphics that don’t require full 24-bit color | An 8-bit color palette |
| Photos | JPEG files, optimized as necessary, or HEIC files |
| Stereo or spatial photos | Stereo HEIC |
| Flat icons, interface icons, and other flat artwork that requires high-resolution scaling | PDF or SVG files |

- **Embed a color profile in every image** and test on real devices.
- **[XPLAT]** Android uses density buckets at 1, 1.5, 2, 3 and 4×, Windows 100–400% scaling, and the web `srcset`/DPR. Parent rule: SVG first. For raster, export 1, 2 and 3×, plus 1.5 and 4× for Android.

### Platforms
- iOS, iPadOS, macOS: nothing additional.
- **tvOS parallax:** focus raises, sways and lights an element. **Layered images (2–5 layers)** are **required for the app icon** and encouraged for other focusable images, including Top Shelf. Runtime-downloaded images use `.lcr` (from `layerutil`) and are never embedded. Standard focus views apply parallax automatically. Put text and prominent content in the foreground, shadows in the middle, and an **opaque** background at the back (transparency there is an error). Keep depth subtle, keep a safe zone, and preview on a real TV.
- **visionOS:** pixels aren't 1:1. App icons have 2–3 layers. **Prefer vector.** @2x raster goes soft up close; higher resolutions cost performance, **especially above @6x**, and need high-quality filtering. **Spatial photos and scenes (new Dec 2025):** stereo HEIC plus metadata. A scene is 3D generated from 2D and takes **up to several seconds**. Put text on the **feathered glass background**. Show spatial content standalone or generously spaced, generate it only on explicit action, keep UI minimal and scenes large and centered. **[AI]** Multi-second generation needs an explicit trigger and a progress state.
- **watchOS:** avoid transparency except in template images. Use **autoscaling PDFs** designed at 2× for 40 and 42 mm:

| Screen size | Image scale |
|---|---|
| 38mm | 90% |
| 40mm | 100% |
| 41mm | 106% |
| 42mm | 100% |
| 44mm | 110% |
| 45mm | 119% |
| 49mm | 119% |

**Change log:** Dec 16 2025 spatial photos and scenes. Dec 5 2023 visionOS raster. Jun 21 2023 visionOS. Sep 14 2022 Watch Ultra.

---

## Inclusion `[hig:inclusion]`

**Purpose:** respectful, accessible, understandable content. Inclusive is more than inoffensive, and the work is iterative.
- Consider 12 listed perspectives, including age, gender identity, race, disability (permanent, temporary and situational), culture, religion, education and socioeconomic context.
- **Language:** check tone from several viewpoints (academic tone excludes). **Address people as "you/your"**, never "the user". **Reserve "we/our" for the company or software.** Define or avoid jargon, replace colloquialisms (some have exclusionary origins), and be wary of humor. **[AI]** This decides persona pronoun policy: whether the agent says "I", what "we" means, and no jokes in system copy.
- **Approachable:** a clear UI, skippable onboarding, and room to deepen understanding over time.
- **Gender:** avoid unnecessary gendered references and use non-gendered person glyphs. Collect gender only when required, offering *nonbinary*, *self-identify*, *decline to state* and pronouns.
- **People and settings:** portray diversity of race, body type, age and ability. Avoid stereotypes and conspicuous affluence.
- **Stereotypes:** don't assume family structure. Base security questions on universal experiences (first friend, not first car).
- **Accessibility:** support VoiceOver, Display Accommodations, captions, Switch Control and Speak Screen. Disability is a spectrum and can be temporary or situational. Use people-first wording and never use disability as a negative metaphor.
- **Languages:** internationalize, then localize. Plain, gender-neutral copy localizes better. Use SF Symbols for localized and RTL glyphs. **Re-check color meanings per locale.**
- **Platforms:** nothing additional. **Change log:** none.

---

## Materials `[hig:materials]` (brief; covered by another stream)

**Liquid Glass** is the floating functional layer for controls and navigation. Keep it out of the content layer, except for transient states such as an active slider or toggle, and use it sparingly on custom controls. **Regular** (the default) blurs and adjusts luminosity for text-heavy components such as alerts, sidebars and popovers. **Clear** is highly translucent and only for use over rich media; add a **35% dark dimming layer** when that media is bright. **Standard materials** (blur, vibrancy, blending) structure the content layer. Choose them by purpose, not by apparent color, and always put vibrant colors on top.
- **iOS/iPadOS:** ultraThin, thin, regular (default), thick. Vibrant labels have four levels (no quaternary on thin or ultraThin), fills three, separators one. **macOS:** purpose-specific materials and blending modes (behind window / within window). **tvOS:** ultraThin through thick, by overlay type and color scheme.
- **visionOS:** a fixed adaptive *glass* with **no Dark Mode**. Thin for interactive elements, regular for sections, thick for dark elements. **watchOS:** keep the default material behind full-screen modals.

Reduce Transparency and Increase Contrast change glass. **[XPLAT]** Web, Linux and Android need opaque fallback tokens. **Change log:** Sep 9 and Jun 9 2025 Liquid Glass. Aug 6 2024 art. Dec 5 2023 terminology. Jun 2023 visionOS and watchOS.

---

## Motion `[hig:motion]`

**Purpose:** motion conveys status, feedback and instruction. **New:** Liquid Glass motion responds more strongly to direct touch than to trackpad input. **[XPLAT]** Motion tokens should vary by input type.

**This page has no durations or easing curves.** Its only numbers are **30–60 fps** for games and a **≈0.2 Hz** oscillation to avoid in visionOS. Duration and easing tokens must come from other sources (Material and Fluent publish them).
- **Purposeful and optional:** excess motion distracts and can make people unwell. Never make motion the only carrier of information; back it with haptics or audio and honor Reduce Motion.
- **Follow the gesture** (slide down to reveal means slide up to dismiss). Keep feedback **brief and precise**, and **don't animate frequent interactions** in custom elements.
- **Let people cancel motion.** Never block input behind an animation, especially a repeated one. **[AI]** Streaming, "working" and transition animations must not block typing, Stop or scrolling.
- Animated SF Symbols (SF Symbols 5+) suit status. **[AI]** Use them for thinking and done states.
- **Games:** a steady **30–60 fps** with good per-device defaults, plus quality and battery options such as power modes when external power is connected.

### Platforms
- iOS, iPadOS, macOS, tvOS: nothing additional.
- **visionOS:** no peripheral motion; if unavoidable, match its brightness to the scene. Make large moving objects translucent or lower in contrast, and keep movable windows small. **Fade out, move, fade in** instead of animating a relocation. Never rotate the world; change direction instantly during a fade. Provide a stationary frame of reference. Avoid sustained oscillation near **0.2 Hz**, or use low amplitude and translucency.
- **watchOS:** SwiftUI is preferred (WatchKit uses `WKInterfaceImage`). Animation easing is **built in and can't be disabled or customized**.

**Change log:** Sep 9 2025 Liquid Glass. Jun 10 2024 games. Feb 2 2024 visionOS peripheral motion. Jun 21 2023 visionOS.


# B. HIG Foundations, part 2: layout, typography, SF Symbols, spatial, writing, privacy, RTL

Pages read in full: `layout`, `typography`, `sf-symbols`, `spatial-layout`, `immersive-experiences`, `writing`, `privacy`, `right-to-left`.
**Citation convention:** every bullet cites the slug in its `##` heading unless it names another `[hig:…]`.

> **CORPUS GAP.** The current `hig:layout` (revised Sep 9 2026) has **no Specifications section**: no device screen-size, scale-factor, or per-device size-class tables and no numeric iOS/iPadOS margins. Its change log still mentions iPhone 17 and Watch spec additions. A grep of all 174 pages found per-device numbers only in `hig:live-activities` (Dynamic Island). **Coordinator:** source these from Apple Design Resources or an archived HIG and label the source; don't fabricate them.

---

## Layout `[hig:layout]`
**Purpose:** a consistent layout that adapts to display size, orientation, window size, and multitasking.

### Visual hierarchy
- Most important items go top and leading (reading order). Use system components so the order mirrors for RTL.
- Alignment shows relationships; indentation shows subordination. Group with space, containers, or separators.
- Use progressive disclosure (triangles, menus, nested views). **[AI]** Collapse reasoning, tool calls, and sources by default.
- **Separate controls from content (Liquid Glass).**
  - Put controls on glass with a **scroll edge effect**, not on solid or semi-opaque fills.
  - Extend backgrounds under sidebars and bars.
  - Use the **background extension effect** (mirror and blur) where a sidebar would cover art.
  - **[AI]** This is the pattern for a composer floating over a transcript.

### Adaptability
- Handle size classes, screen sizes, orientations and aspect ratios, the Dynamic Island, external displays, Display Zoom, resizable iPad and Mac windows, text size, and locale (direction, formats, text length).
- Respect safe areas, margins, and guides. Orientation-locked layouts must still resize well.
- **Dynamic Type:** stack adjacent views, let rows grow and wrap, and never clip text.
- Test the largest and smallest layouts first in **Device Hub**, including iPad resizing and **iPhone Mirroring on Mac**.
- Scale background art to fill the screen and never distort it.

### Size classes (iOS, iPadOS)
| Axis | Compact | Regular |
|---|---|---|
| Horizontal | narrow | wide |
| Vertical | short | tall |

*(Built from the page prose; the page has no table. The illustrations show an iPad window in all four combinations.)*
- The class is set by device, window configuration, and multitasking state (Slide Over, iPhone mirrored to Mac). Any combination can occur, so design for all of them.
- **Decide layout from size class, never from idiom or orientation.**
- **Keep functionality identical across sizes**; only visibility changes (tab bar → sidebar, overflow → on-screen). Keep the layout recognizable for the platform.
- **[XPLAT]** Apple's 2×2 compact/regular model has no breakpoints. Material 3 uses dp window classes (compact, medium, expanded, large, extra-large), and the web uses CSS breakpoints. The parent system has to set numeric breakpoints and map them to compact/regular behaviours.

### Guides and safe areas
- **Layout guide:** a rectangle for positioning and spacing. System guides apply standard margins and **limit text width for readability** (the readable-content guide). Custom guides are allowed. **No numeric margin or readable-width values are given.**
- **Safe area:** the part of a window not covered by hardware (Dynamic Island, camera housing) or by bars. Keep content and controls inside it.

### Platform considerations
- **iOS, iPadOS:** no additional considerations. The older iPadOS guidance on avoiding system controls has been removed.
- **macOS:**
  - **No controls or critical information at the bottom of a window**, because windows often get dragged partly off-screen. **[XPLAT]** This conflicts with Windows and web dialog convention (bottom-right buttons) and with mobile bottom bars. The parent system needs a desktop rule, for example primary actions in the header or toolbar and a bottom action row only in dialogs.
  - Keep content out from behind the camera housing.
- **tvOS:**
  - Safe area: inset **60 pt top and bottom, 80 pt sides** (covers overscan).
  - Pad focusable items, which grow on focus. Add extra space around row titles.
  - Keep spacing consistent; partially visible off-screen items equal on both sides.

  | Columns | Unfocused content width | Horizontal spacing | Minimum vertical spacing |
  |---|---|---|---|
  | 2 | 860 pt | 40 pt | 100 pt |
  | 3 | 560 pt | 40 pt | 100 pt |
  | 4 | 410 pt | 40 pt | 100 pt |
  | 5 | 320 pt | 40 pt | 100 pt |
  | 6 | 260 pt | 40 pt | 100 pt |
  | 7 | 217 pt | 40 pt | 100 pt |
  | 8 | 184 pt | 40 pt | 100 pt |
  | 9 | 160 pt | 40 pt | 100 pt |

  *(The page's nine tabbed tables, merged; values verbatim.)*
- **visionOS:**
  - Support resizing and centre content at large sizes. Min/max sizes only prevent overlap; they don't block resizing.
  - Use 3D in windows rarely and inset it.
  - Supplemental content goes in an **adjacent window**, not an ornament.
  - **Button centres at least 60 pt apart.**
- **watchOS:** **at most 3 glyph buttons or 2 text buttons per row**. Autorotate views people show to others (QR codes).

**Change log:**
- Sep 9 2026: update.
- Sep 2025: iPhone 17 and Watch specs (absent).
- Jun 9 2025: Liquid Glass.
- Mar 2025: device specs.

---

## Typography `[hig:typography]`
**Purpose:** legible text, clear hierarchy, and brand expression.

### Legibility
| Platform | Default size | Minimum size |
|---|---|---|
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

- The table applies to **custom and system fonts alike**. Thin custom weights need sizes above it.
- Test text in context (game text on every platform). If it's hard to read, increase size or contrast, or use the system fonts.
- **Avoid Ultralight, Thin, and Light.** Use Regular, Medium, Semibold, or Bold.
- **[XPLAT]** Body size differs by platform: iOS 17 pt, macOS 13 pt, Material Body Large 16 sp, web ≈16 px, Windows Fluent 14 px. Define per-platform base sizes.

### Hierarchy
- Use weight, size, and colour for hierarchy, and keep it intact at every text size. Use as few typefaces as possible.
- **Scale the content people care about first.** Tab titles don't need to grow; dialogue matters more than transient damage numbers. **[AI]** Scale message text fully and chrome or metadata less.

### System fonts
- **SF (sans):** Pro, Compact, Arabic, Armenian, Georgian, Hebrew, **Mono**. All but Mono have Rounded variants. **New York** is the serif.
- Both are **variable fonts with dynamic optical sizes**; use discrete optical sizes only in tools that can't handle variable fonts.
- **9 weights**, Ultralight to Black. **SF widths:** Condensed and Expanded (plus Compressed per WWDC22). SF Symbols weights match.
- **Text styles** (weight, size, leading) scale with Dynamic Type. Prefer them.
- **Symbolic traits:**
  - **Bold** gives the emphasized weight: medium, semibold, bold, or heavy (`bold()`, `traitBold`).
  - **Loose leading** for wide columns and long passages.
  - **Tight leading** for constrained rows, but **never for 3 or more lines**. **[AI]** Long answers use body text with standard or loose leading.
- Use `Font.Design` (`.default` = SF, `.serif` = NY). **Never embed system fonts.**
- The system sets tracking per size automatically. Mockups need manual tracking from the tables.

### Custom fonts
- Keep them legible at the recommended minimums.
- They must support Dynamic Type and **Bold Text**. Unity games use Apple's plug-ins or offer their own size control.
- **[XPLAT]** A brand font must honour OS text scaling everywhere: Dynamic Type, Android font scale, browser zoom/rem, Windows text scaling.

### Dynamic Type
Available on iOS, iPadOS, tvOS, visionOS, and watchOS. **macOS has no Dynamic Type.** **[XPLAT]** Desktop (macOS, Windows, Linux) needs its own text-size or zoom setting.
- Test every size, including Larger Accessibility Text Sizes (Settings > Accessibility > Display & Text Size > Larger Text).
- Scale meaningful icons with text; SF Symbols do this automatically.
- **Truncate as little as possible.** Show as much at the largest AX size as at the largest standard size. Don't truncate in scrolling regions without a full-text view. Allow multiple lines.
- At large sizes, stack inline glyphs and timestamps under the text and use fewer columns (`isAccessibilityCategory`).
- Keep primary elements at the top at every size.

### Platform considerations
- **iOS, iPadOS, tvOS:** SF Pro is the system font; NY is also available.
- **macOS:** SF Pro is the system font. NY is available only to Mac Catalyst apps. To match system controls, use the dynamic font variants:

| Dynamic font variant | API |
|---|---|
| Control content | `controlContentFont(ofSize:)` |
| Label | `labelFont(ofSize:)` |
| Menu | `menuFont(ofSize:)` |
| Menu bar | `menuBarFont(ofSize:)` |
| Message | `messageFont(ofSize:)` |
| Palette | `paletteFont(ofSize:)` |
| Title | `titleBarFont(ofSize:)` |
| Tool tips | `toolTipsFont(ofSize:)` |
| Document text (user) | `userFont(ofSize:)` |
| Monospaced document text (user fixed pitch) | `userFixedPitchFont(ofSize:)` |
| Bold system font | `boldSystemFont(ofSize:)` |
| System font | `systemFont(ofSize:)` |

- **visionOS:**
  - SF Pro is the system font. NY requires you to specify styles.
  - Body and title Dynamic Type styles are **bolder** than on iOS, and **Extra Large Title 1 and 2** exist for editorial layouts. There's no numeric visionOS table.
  - Use **2D text**, not 3D.
  - Test legibility at every scale.
  - Maximize contrast; text is white by default on the system material.
  - Make text with no background **bold**, and don't use shadows.
  - **Billboard** labels attached to points in space (rotate them on the y-axis so the baseline stays perpendicular to the line of sight).
- **watchOS:** SF Compact is the system font, NY is available, and complications use SF Compact Rounded.

### Specifications: verbatim tables

**macOS built-in text styles**

| Text style | Weight | Size (points) | Line height (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 26 | 32 | Bold |
| Title 1 | Regular | 22 | 26 | Bold |
| Title 2 | Regular | 17 | 22 | Bold |
| Title 3 | Regular | 15 | 20 | Semibold |
| Headline | Bold | 13 | 16 | Heavy |
| Body | Regular | 13 | 16 | Semibold |
| Callout | Regular | 12 | 15 | Semibold |
| Subheadline | Regular | 11 | 14 | Semibold |
| Footnote | Regular | 10 | 13 | Semibold |
| Caption 1 | Regular | 10 | 13 | Medium |
| Caption 2 | Medium | 10 | 13 | Semibold |

Point size based on image resolution of 144 ppi for @2x designs.

**tvOS built-in text styles**

| Text style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Title 1 | Medium | 76 | 96 | Bold |
| Title 2 | Medium | 57 | 66 | Bold |
| Title 3 | Medium | 48 | 56 | Bold |
| Headline | Medium | 38 | 46 | Bold |
| Subtitle 1 | Regular | 38 | 46 | Medium |
| Callout | Medium | 31 | 38 | Bold |
| Body | Medium | 29 | 36 | Bold |
| Caption 1 | Medium | 25 | 32 | Bold |
| Caption 2 | Medium | 23 | 30 | Bold |

Point size based on image resolution of 72 ppi for @1x and 144 ppi for @2x designs.

### Tables for the coordinator to insert (described only)
- **iOS/iPadOS Dynamic Type:** xSmall to xxxLarge (**Large = default**) plus AX1–AX5.
  - 11 styles; columns Style, Weight, Size, Leading, Emphasized weight.
  - Default Body is 17/22. Body runs from 14 to 53.
  - Footnote: 144 ppi @2x / 216 ppi @3x.
- **watchOS:** xSmall to xxxLarge. Defaults: Small for 38mm, Large for 40/41/42mm, xLarge for 44/45/49mm. Then **AX1–AX3 only**.
  - 10 styles, including Footnote 1–2. Leading is usually size + 2.5.
  - Keep source anomalies as-is (for example AX1 Title 2 34/41).
- **Tracking:** six tables.
  - SF Pro (iOS/iPadOS/visionOS): 12 pt = 0, 17 pt = −0.43.
  - SF Pro Rounded and New York (6–260 pt; the source has a "+.12" typo).
  - macOS and tvOS: like SF Pro, but 52/53 pt are swapped.
  - watchOS SF Compact (not monotonic at 20 pt) and SF Compact Rounded.

**Change log:**
- Dec 16 2025: emphasized weights added.
- Mar 2025: Dynamic Type guidance.
- Jun 2024: Unity and billboarding.
- Jun 2023: visionOS.

---

## SF Symbols `[hig:sf-symbols]`
**Purpose:** thousands of symbols that align with SF text at every weight and size, for toolbars, tab bars, menus, and inline text.
- Features depend on the OS version: anything from year N doesn't exist on earlier OSes.
- **License:** symbols (or lookalikes) can't be used in app icons, logos, or any trademarked use. Apple-product symbols (Info badge in the app) can be shown but **not customized**. **[XPLAT]** SF Symbols is for Apple platforms (licence details are outside the corpus; verify). The parent system needs a cross-platform icon set with matching weight and scale axes, mapped to SF Symbols on Apple platforms.

### Rendering modes
Paths sit on primary, secondary, and tertiary layers. For example, `cloud.sun.rain.fill` has the cloud, sun, and rain on separate layers.

| Mode | Behaviour |
|---|---|
| Monochrome | One colour for all layers; paths are coloured or transparent cut-outs |
| Hierarchical | One colour; opacity varies by layer level (≈100 / 50 / 25% in the example) |
| Palette | 2+ colours, one per layer; with 2 colours on a 3-level symbol, secondary and tertiary share one |
| Multicolor | Meaningful intrinsic colours (`leaf` green, `trash.slash` red); some layers take custom colours |

- System colours adapt to accessibility settings, vibrancy, and Dark Mode. **Automatic** picks the preferred mode, but check legibility at each size and background.
- **Gradients (SF Symbols 7, new):** a linear gradient from **one source colour**. Works in every mode, with system or custom colours, and on custom symbols. Looks best at large sizes.
- **Variable color:** fills layers as a value crosses thresholds from 0 to 100% (capacity, strength). Layers can opt out (the speaker in `speaker.wave.3`). **Use it for change, never for depth**; Hierarchical is for depth.
- **Variable Draw** (SF Symbols 7, for strength or progress) is named only in the WWDC25 video summary, with no guidance in the page body.

### Weights, scales, variants
- **9 weights** (Ultralight to Black) matching SF. **3 scales**: small, **medium (default)**, and large, relative to SF cap height, so 27 combinations. Scale changes emphasis without breaking the weight match.
- **Outline** is the default look (like text). **Fill** adds emphasis (iOS tab bars, swipe actions, accent-colour selection). **Slash** means unavailable or off. **Enclosed** (circle, square, rectangle) improves small-size legibility. Slash and enclosed combine with outline or fill. Containers often choose the variant: iOS tab bars use fill, toolbars use outline.
- **Localization:** script variants for Latin, Arabic, Hebrew, Hindi, Thai, Chinese, Japanese, Korean, Cyrillic, Devanagari, and Indic numerals. They switch automatically with the device language.

### Animations
These work on every symbol, mode, weight, and scale, and on custom symbols. Playback can run once or repeat until a condition, with adjustable speed and reverse-before-repeat.

| Effect | Behaviour | Use for |
|---|---|---|
| Appear / Disappear | Gradually emerges or recedes | Showing or hiding |
| Bounce | Brief elastic scale, then back; plays once by default | An action happened or is needed |
| Scale | Size change that **persists** until reset | Selection feedback |
| Pulse | Opacity cycles (annotated layers, or all) | Ongoing activity |
| Variable color | Steps through layers, **cumulative** or **iterative**; can autoreverse or hide inactive layers; symbols are **open loop** or **closed loop** (seamless) | Progress, connecting, broadcasting |
| Replace | **Down-up** (state change), **up-up** (state change with forward progress), **off-up** (emphasises the next state) | State swaps |
| Magic Replace | **Default** replace; morphs related shapes (slash, badge); falls back to down-up | Mute/unmute, badges |
| Wiggle | Back and forth along an axis | A missed change or call to action |
| Breathe | Opacity **and** size cycle | Ongoing status (recording) |
| Rotate | Whole symbol or by layer (fan blades) | In progress |
| Draw On / Off (SF Symbols 7) | Draws along guide points, all layers at once, staggered, or one by one | Progress, direction |

- Animate sparingly and only with a clear purpose, to convey information compactly, matching the brand's tone. **[AI]** States vocabulary:
  - Breathe or Pulse: thinking or listening.
  - Variable color or Rotate: tool running.
  - Draw On: progress.
  - Magic Replace: send ↔ stop.
  - Bounce: done.

### Custom symbols
- Start from a similar symbol's template. Match detail, optical weight, alignment, and perspective. Aim for simple, recognizable, inclusive, and directly relevant.
- Annotate layers with colours or hierarchy levels.
- Use **negative side margins** for badged symbols, named like `left-margin-Regular-M`.
- For animation, annotate layers. Z-order sets the variable-color order, and layer groups move together. **Test every preset.** Draw whole shapes plus offset **erase layers** instead of cut-outs (`person.2.fill`).
- Use the **component library** for enclosures and badges rather than drawing them.
- Give every symbol **VoiceOver alt text**. Never replicate Apple products.
- **Platforms:** no additional considerations.

**Change log:**
- Jul 28 2025: Draw and gradients (SF Symbols 7).
- Jun 2024: SF Symbols 6 animations.
- Jun 2023: animations section.
- Sep 2022: variable color.

---

## Spatial layout `[hig:spatial-layout]`
**Purpose:** comfortable use of the Vision Pro canvas. **visionOS only; not supported elsewhere.**
- **Field of view** is what's visible without moving the head. It varies with Light Seal fit and peripheral acuity. The illustration shows rings at **30°, 60°, and 90°**. **The system doesn't report field of view.**
  - Centre important content (apps launch in front of the person).
  - Avoid motion and bright, high-contrast objects in the periphery.
  - For reclined viewing, raise the window and tilt it toward the person.
- **Never anchor content to the head.** Anchor it in the room.
- **Depth:**
  - The system adds colour temperature, reflections, and shadow; SwiftUI adds depth to 2D windows. Use RealityKit and **volumes** (frameless windows) for 3D.
  - Depth cues must be accurate. Use depth for hierarchy (a sheet pushes its window back on z).
  - **Don't give text depth.**
  - Use depth only where it adds value: big elements like toolbars and tab bars, not button glyphs. Limit the number of depth levels, since refocusing tires the eyes.
- **Scale:**
  - **Dynamic scale** keeps a window the same apparent size at any distance. Use it for interactive content.
  - **Fixed scale** behaves like a physical object (smaller when farther). Use it rarely, for non-interactive true-to-life objects.
  - **A visionOS point is an angle, not pixels.** **[XPLAT]** Define tokens in logical units with a mapping for each platform (pt, dp, px, angular pt).
- **Best practices:**
  - Avoid too many windows.
  - Prefer **indirect gestures** (look and pinch); keep direct touch for brief, nearby manipulation.
  - The Digital Crown recenters content; no app work is needed.
  - **Place regular button centres at least 60 pt apart with at least 16 pt between them**, and never overlap interactive elements.
  - Support use with no physical movement.
  - Place large floor-up content on a floor-aligned plane.

**Change log:**
- Mar 29 2024: no overlapping interactive elements.
- Jun 2023: new page.

---

## Immersive experiences `[hig:immersive-experiences]`
**Purpose:** content beyond windows and volumes. **visionOS only.** Apps run in the **Shared Space** (alongside others) or a **Full Space** (alone) and can switch at any time.
- Passthrough is live camera video. Digital Crown: **press and hold to recenter**, **double-click to briefly hide content**.
- In `mixed`, content near physical objects dims or goes semi-opaque, with no boundary.
- In `progressive` and `full`, there's a **~1.5 m boundary from the initial head position**. Approaching it fades the experience to passthrough. Past it, the app icon replaces the visuals, which come back on return or recenter.

| Style / technique | Space | Behaviour |
|---|---|---|
| Dimmed passthrough (`SurroundingsEffect`) | Shared or Full | Dims or tints the surroundings (black by default, custom tint OK) |
| `mixed` | Full | Unbounded 3D over passthrough; can request room and object data (ARKit) |
| `progressive` | Full | Custom environment partly replaces passthrough. Crown sets immersion within a **default 120°–360°** range or a custom range. Portrait or landscape. 1.5 m boundary |
| `full` | Full | **360°** environment fully replaces passthrough. 1.5 m boundary |

- **Launch in the Shared Space or `mixed`.** Save deep immersion for key moments (Photos: browse in a window, go immersive for one photo).
- Support accessibility and more than one way to interact.
- Guide attention with dimming, tint, motion, scale, and Spatial Audio, starting subtle. Keep passthrough tints subtle (visionOS 2+).
- **Comfort:**
  - Keep content in the field of view and motion gentle.
  - Avoid `progressive` and `full` if people might go past 1.5 m.
  - Don't make people move; bring objects to them.
  - Don't block passthrough heavily in `mixed`; switch to `progressive` or `full`.
  - ARKit scene and hand data needs permission.
- **Transitions:**
  - Make them smooth and predictable.
  - **Let people choose when to enter and exit** (Keynote's Exit button); don't force them to use system controls.
  - Label exit buttons as "back" or "quit", and offer pause or save before quitting.
  - **[AI]** The same rule applies to agent focus or autonomous modes: explicit entry, labelled exit, save state.
- **Virtual hands:** match real hand poses. Be careful with oversized hands. If tracking drops, fade them out and show the real hands, then fade back in.
- **Environments:** keep distractions low, use proximity to signal interactivity, and keep motion subtle and away from the edges. Make the space expansive. Use Spatial Audio without heavy loops, ducked under other audio. Use lit meshes rather than flat 360° images. **Always include a ground plane.** Don't repeat assets too often.

**Change log:**
- Jun 9 2025: portrait progressive immersion.
- Nov 2024: style refinements.
- Jun 2024: passthrough tint and immersion min/max.
- May 2024: environments.
- Feb 2024: choosing a style.
- Jun 2023: new page.
- New WWDC26 video: environments for apps **and the spatial web**.

---

## Writing `[hig:writing]` (usable as a content style guide)
**Purpose:** words are part of the UX. No platform-specific considerations.

1. **Voice (constant).** Derive voice from the audience and how you want them to feel (a bank sounds steady, a game sounds fun). **Keep a glossary** and use it everywhere. **[AI]** Fix names for model, agent, run, tool, and source, with no synonyms.
2. **Tone (varies with context).** Match it to what the person is doing, in the app and in the world: direct for serious events (a fall alert), light for achievements. **[AI]** Use neutral tone for failures, refusals, money, data, and irreversible actions.
3. **Clarity.** Use simple words, cut every unnecessary word, and read it aloud. Put the most important information first. Give each idea its own screen.
4. **Inclusive language.** Use plain language with **no jargon and no gendered terms**. Write with accessibility and localization in mind (Apple Style Guide, "Writing inclusively").
5. **Capitalization.** Choose title case (formal) or sentence case (casual) **for each element type** and never mix within it. Examples: all alerts in title case, all headlines in sentence case. Buttons follow `hig:buttons#Content`. Purpose strings use sentence case and end with a period (`hig:privacy`). **[XPLAT]** Material and Fluent use sentence case nearly everywhere, while Apple system UI uses title case for buttons and alert titles. Sentence case everywhere is the easiest cross-platform choice; document any exceptions.
6. **Buttons and links.** **Start with a verb.** Be clear rather than clever ("Send", not a playful phrase). **Never "Click here"**; name the destination (this helps screen readers).
7. **Multistep flows.** Start with "Get Started". Use either a hint of the next step or "Continue"/"Next", consistently. End with "Done".
8. **Pronouns.** Use *my* and *your* rarely ("Favorites", not "Your Favorites"), and keep perspective consistent. **Avoid "we"** because it's unclear who that is: "Unable to load content" rather than a "we're having trouble" phrasing. **[AI]** Decide whether the assistant uses "I" in conversation, and keep system chrome and errors impersonal.
9. **Device verbs.** **Tap** for touch, **click** for pointer. Small screens (iPhone, Watch) and distant shared TVs both need brevity. **[XPLAT]** In shared strings use neutral verbs (select, choose, open) or per-platform variants.
10. **Errors.** Prevent them first. Place the message **next to the problem**, **don't blame**, and **say how to fix it** ("Choose a password with at least 8 characters"). No "oops" or "uh-oh". If wording can't fix a common error, redesign the interaction. **[AI]** For model, tool, or rate-limit failures, say what happened and what to do next.
11. **Field validation.** State the rule positively ("Use only letters for your name"). Avoid robotic messages ("Invalid name"). Label every field and use hint text with an example (`name@example.com`) or a description.
12. **Empty states.** Always give a next step with a button or link. Use them to welcome and teach in your voice. **Never put crucial information there**, since empty states are temporary. **[AI]** New chat: offer suggested actions as buttons.
13. **Delivery.** Choose notification, alert, or action sheet based on urgency, importance, whether action is needed, and how much detail is required.
14. **Settings.** Use literal labels. Describe what the **on** state does and leave the off state implied. Link directly to a setting rather than describing its location.
- **Numbers and units:** not covered on this page. Use locale formatting (`hig:layout`) and the RTL numeral rules below.

**Change log:**
- Dec 16 2025: language patterns and possessive pronouns.
- Feb 2023: new page.
- New WWDC26 video on naming features and labels.
- WWDC25 video: cut repetition, lead with benefits.

---

## Privacy `[hig:privacy]`
**Purpose:** be transparent about the data you need and protect it. App Store privacy details are required.

### Principles
- **Request only what a feature needs, only once people show interest, and as narrowly as possible.** **[AI]** Send the model only the context the task needs.
- **Be open about collection and use.** Respect Hide My Email, Mail Privacy Protection, and tracking obligations. **[AI]** Say whether content leaves the device, is retained, or is used for training.
- **Process on device where possible** (Neural Engine, Create ML). Use system protections (CloudKit encryption).

### Permission requests
- **Requires permission:** personal data, user content (mail, messages, calendar, photos, audio and video, HomeKit), Bluetooth, Wi-Fi, local network, camera, microphone, visionOS ARKit data, and the advertising identifier.
- The system alert shows your **purpose string** before the buttons. People can change their choice in Settings > Privacy.
- **Ask when a feature needs access**, not at launch, unless the app can't work without it (navigation). **[AI]** Ask for connectors, files, and microphone on first use.
- **Purpose string:** one short, specific sentence in **sentence case and active voice, ending with a period**, saying how and why. Bad: vague passive ("…for a better experience") or a bare command.
- Alert options: Location has Allow Once / Allow While Using App / Don't Allow. Photos has Select Photos / Allow Access to All Photos / Don't Allow.
- **Pre-alert screens** (only when context isn't enough; camera, mic, location, contacts, calendar, tracking):
  - **Exactly one button, labelled "Continue" or "Next"**, which opens the alert. **Never "Allow"** or anything that looks like the alert's allow button.
  - **No Close, Cancel, or Skip** unless legal consent requires it.
  - **[XPLAT]** Android rationale dialogs and web consent patterns allow dismissal. Set a per-platform rule.
- **Tracking (ATT):**
  - Show the system alert before collecting any tracking data.
  - **Rejected pre-alert designs:** incentives, imitation requests, images of the alert, arrows pointing at "Allow". A legally required consent screen before or after ATT is allowed (App Review 5.1.1(iv)).
  - **[AI]** Apply these anti-dark-pattern rules to AI data-use consent as well.

### Location button (iOS, iPadOS, watchOS)
- A tap grants **one-time** location access. Only the first tap shows an alert. Access expires when the app stops being used. With no prior status, a tap equals Allow Once.
- Use it for lightweight sharing (tag a post, find a store).
- **Customizable:** system title ("Current Location" etc.), filled or outlined glyph, colours, and corner radius. Nothing else.
- **Text must fit untruncated at every accessibility size and language.** If problems persist, the button stops granting location. **[XPLAT]** Apple only.

### Protecting data
- Use **passkeys**. If you keep passwords, add 2FA, and use Face ID, Optic ID, or Touch ID for apps that stay signed in.
- Keep secrets in the **Keychain**, never in plain-text files. **[AI]** This includes API keys, OAuth tokens, and agent credentials.
- No custom authentication; use passkeys, Sign in with Apple, or Password AutoFill.

### Platform considerations
- **iOS, iPadOS, tvOS, watchOS:** no additional considerations.
- **macOS:** sign with a **Developer ID** outside the store. **Sandbox** the app (required for the Mac App Store). **Don't assume who is signed in** (fast user switching).
- **visionOS:**
  - ARKit sends nothing to apps in the Shared Space; apps need a Full Space plus permission for planes, scene reconstruction, images, and hands.
  - **Input is private by design**: the system draws hover effects, so gaze stays private until a tap.
  - The back camera is blank and the front camera serves Personas only, with permission. When porting, replace camera features with import.

**Change log:**
- Jun 21 2023: consolidated page and visionOS.
- New WWDC26 video **"Meet Trust Insights"**: privacy-preserving ML that detects when someone is being coached into risky actions, plus intervention design. **[AI]** Relevant to agent and financial-action safeguards.
- WWDC25: privacy-by-design and passkeys videos.

---

## Right to left `[hig:right-to-left]`
**Purpose:** mirror the UI for Arabic, Hebrew, and other RTL scripts. System components flip automatically. No platform-specific considerations.

- **Text alignment:**
  - Mirror alignment when the system doesn't do it for you.
  - **Align paragraphs of 3 or more lines by their own language**; 1–2 line blocks follow the UI direction. **[AI]** Mixed-language chat output needs per-paragraph alignment.
  - **Give every item in a list the same alignment**, including items in another script.
- **Numbers:**
  - Hebrew uses Western Arabic numerals. Arabic uses Western or Eastern depending on region. Number-centric apps choose per locale; others use system formatting.
  - **Never reverse the digits within a number** (phone and card numbers).
  - **Reverse the order of numerals in progress or counting sequences** (sliders, ratings, ordered sequences), but **never mirror the glyphs**.
- **Controls:**
  - **Flip** progress controls and swap their end glyphs.
  - **Flip** fixed-order navigation: **Back points right**, and Next and Previous flip.
  - **Keep** controls that refer to real directions or on-screen areas.
  - Next to ALL-CAPS Latin, make Arabic or Hebrew text **about 2 pt larger** (those scripts have no capitals).
- **Images:**
  - **Don't flip** photos or artwork; it changes meaning and risks copyright. Make a new version if the image depends on direction.
  - **Reverse the positions** of images whose order is meaningful (chronological, alphabetical, favourites).
- **Interface icons:**
  - SF Symbols provide RTL and Arabic/Hebrew variants. Declare directionality for custom symbols.
  - **Flip** icons that represent text or reading direction, and icons that show forward or backward motion (speaker waves).
  - **Localize** icons that contain text (signature, rich text, I-beam). Redesign icons whose text has nothing to do with reading.
  - **Don't flip** logos, universal marks (✓), or real-world objects (clocks, right-handed tools, game controllers).
  - **Complex icons:** decide part by part.
    - Keep the negation **backslash** the same in both directions.
    - Flip a badge if it depicts UI that flips. Otherwise move it only for balance (cart: flip it and put the plus badge top-left).
    - Keep handed tools (magnifying glass) oriented as they are while flipping the base image.
- **[XPLAT]** These rules match Material's bidirectionality guidance, so one shared RTL rule set works. Use logical CSS properties (`inline-start`/`inline-end`) on the web.

**Change log:** none. WWDC25 video: Natural Selection for bidirectional text, and Language Discovery.

---

## Takeaways for the parent system
1. **Per-platform type ramps.** Base and minimum sizes (pt): 17/11 iOS, 13/10 macOS, 29/23 tvOS, 17/12 visionOS, 16/12 watchOS. No light weights, no tight leading for 3+ lines, an emphasized weight per style. Brand fonts must honour OS scaling. macOS has no Dynamic Type.
2. **Layout from available space, not device.** Compact/regular semantics with the parent system's own breakpoints, the same functionality at every size, and no bottom-of-window controls on macOS. Device tables are missing from the corpus.
3. **Symbol motion vocabulary for AI states.** Breathe or Pulse for thinking, Variable color or Rotate for working, Draw On for progress, Magic Replace for toggles, Bounce for done. One cross-platform icon set with 9 weights × 3 scales, outline/fill/slash/enclosed variants, and RTL variants.
4. **Content style guide.** One case per element type (sentence case for cross-platform), verb-first labels, no "we", errors placed next to the problem with no blame and a stated fix, actionable empty states, neutral input verbs, and a glossary.
5. **Consent as trust UX [AI].** Ask in context, write active-voice purpose strings, use single-button "Continue" pre-alerts with no incentives or imitations, minimise data, prefer on-device processing, and keep credentials in the Keychain. On visionOS, gaze stays private and 60 pt / 16 pt control spacing applies.


### Typography specification tables (generated programmatically from [hig:typography])

watchOS defaults: Small = default for 38mm; Large = default for 40/41/42mm; xLarge = default for 44/45/49mm.

#### iOS / iPadOS Dynamic Type — standard sizes (default = Large)

Cells are size/leading in points. Weight (emphasized weight) per style; if weight varies by size it is listed.

| Style | Weight (emph.) | xSmall | Small | Medium | Large (default) | xLarge | xxLarge | xxxLarge |
|---|---|---|---|---|---|---|---|---|
| Large Title | Regular (Bold) | 31/38 | 32/39 | 33/40 | 34/41 | 36/43 | 38/46 | 40/48 |
| Title 1 | Regular (Bold) | 25/31 | 26/32 | 27/33 | 28/34 | 30/37 | 32/39 | 34/41 |
| Title 2 | Regular (Bold) | 19/24 | 20/25 | 21/26 | 22/28 | 24/30 | 26/32 | 28/34 |
| Title 3 | Regular (Semibold) | 17/22 | 18/23 | 19/24 | 20/25 | 22/28 | 24/30 | 26/32 |
| Headline | Semibold (Semibold) | 14/19 | 15/20 | 16/21 | 17/22 | 19/24 | 21/26 | 23/29 |
| Body | Regular (Semibold) | 14/19 | 15/20 | 16/21 | 17/22 | 19/24 | 21/26 | 23/29 |
| Callout | Regular (Semibold) | 13/18 | 14/19 | 15/20 | 16/21 | 18/23 | 20/25 | 22/28 |
| Subhead | Regular (Semibold) | 12/16 | 13/18 | 14/19 | 15/20 | 17/22 | 19/24 | 21/28 |
| Footnote | Regular (Semibold) | 12/16 | 12/16 | 12/16 | 13/18 | 15/20 | 17/22 | 19/24 |
| Caption 1 | Regular (Semibold) | 11/13 | 11/13 | 11/13 | 12/16 | 14/19 | 16/21 | 18/23 |
| Caption 2 | Regular (Semibold) | 11/13 | 11/13 | 11/13 | 11/13 | 13/18 | 15/20 | 17/22 |

#### iOS / iPadOS Dynamic Type — accessibility sizes

Cells are size/leading in points. Weight (emphasized weight) per style; if weight varies by size it is listed.

| Style | Weight (emph.) | AX1 | AX2 | AX3 | AX4 | AX5 |
|---|---|---|---|---|---|---|
| Large Title | Regular (Bold) | 44/52 | 48/57 | 52/61 | 56/66 | 60/70 |
| Title 1 | Regular (Bold) | 38/46 | 43/51 | 48/57 | 53/62 | 58/68 |
| Title 2 | Regular (Bold) | 34/41 | 39/47 | 44/52 | 50/59 | 56/66 |
| Title 3 | Regular (Semibold) | 31/38 | 37/44 | 43/51 | 49/58 | 55/65 |
| Headline | Semibold (Semibold) | 28/34 | 33/40 | 40/48 | 47/56 | 53/62 |
| Body | Regular (Semibold) | 28/34 | 33/40 | 40/48 | 47/56 | 53/62 |
| Callout | Regular (Semibold) | 26/32 | 32/39 | 38/46 | 44/52 | 51/60 |
| Subhead | Regular (Semibold) | 25/31 | 30/37 | 36/43 | 42/50 | 49/58 |
| Footnote | Regular (Semibold) | 23/29 | 27/33 | 33/40 | 38/46 | 44/52 |
| Caption 1 | Regular (Semibold) | 22/28 | 26/32 | 32/39 | 37/44 | 43/51 |
| Caption 2 | Regular (Semibold) | 20/25 | 24/30 | 29/35 | 34/41 | 40/48 |

#### watchOS Dynamic Type — standard sizes

Cells are size/leading in points. Weight (emphasized weight) per style; if weight varies by size it is listed.

| Style | Weight (emph.) | xSmall | Small | Large | xLarge | xxLarge | xxxLarge |
|---|---|---|---|---|---|---|---|
| Large Title | Regular (Bold) | 30/32.5 | 32/34.5 | 36/38.5 | 40/42.5 | 41/43.5 | 42/44.5 |
| Title 1 | Regular (Semibold) | 28/30.5 | 30/32.5 | 34/36.5 | 38/40.5 | 39/41.5 | 40/42.5 |
| Title 2 | Regular (Semibold) | 24/26.5 | 26/28.5 | 28/30.5 | 30/32.5 | 31/33.5 | 32/34.5 |
| Title 3 | Regular (Semibold) | 17/19.5 | 18/20.5 | 19/21.5 | 20/22.5 | 21/23.5 | 22/24.5 |
| Headline | Semibold (Semibold) | 14/16.5 | 15/17.5 | 16/18.5 | 17/19.5 | 18/20.5 | 19/21.5 |
| Body | Regular (Semibold) | 14/16.5 | 15/17.5 | 16/18.5 | 17/19.5 | 18/20.5 | 19/21.5 |
| Caption 1 | Regular (Semibold) | 13/15.5 | 14/16.5 | 15/17.5 | 16/18.5 | 17/19.5 | 18/20.5 |
| Caption 2 | Regular (Semibold) | 12/14.5 | 13/15.5 | 14/16.5 | 15/17.5 | 16/18.5 | 17/19.5 |
| Footnote 1 | Regular (Semibold) | 11/13.5 | 12/14.5 | 13/15.5 | 14/16.5 | 15/17.5 | 16/18.5 |
| Footnote 2 | Regular (Semibold) | 10/12.5 | 11/13.5 | 12/14.5 | 13/15.5 | 14/16.5 | 15/17.5 |

#### watchOS Dynamic Type — accessibility sizes

Cells are size/leading in points. Weight (emphasized weight) per style; if weight varies by size it is listed.

| Style | Weight (emph.) | AX1 | AX2 | AX3 |
|---|---|---|---|---|
| Large Title | Regular (Bold) | 44/46.5 | 45/47.5 | 46/48.5 |
| Title 1 | Regular (Semibold) | 42/44.5 | 43/46 | 44/47 |
| Title 2 | Regular (Semibold) | 34/41 | 35/37.5 | 36/38.5 |
| Title 3 | Regular (Semibold) | 24/26.5 | 25/27.5 | 26/28.5 |
| Headline | Semibold (Semibold) | 21/23.5 | 22/24.5 | 23/25.5 |
| Body | Regular (Semibold) | 21/23.5 | 22/24.5 | 23/25.5 |
| Caption 1 | Regular (Semibold) | 18/20.5 | 19/21.5 | 20/22.5 |
| Caption 2 | Regular (Semibold) | 17/19.5 | 18/20.5 | 19/21.5 |
| Footnote 1 | Regular (Semibold) | 16/18.5 | 17/19.5 | 18/20.5 |
| Footnote 2 | Regular (Semibold) | 15/17.5 | 16/17.5 | 17/19.5 |

#### Tracking values (1/1000 em; points in parentheses)

| Size (pt) | iOS, iPadOS, visionOS / SF Pro | iOS, iPadOS, visionOS / SF Pro Rounded | iOS, iPadOS, visionOS / New York | macOS | tvOS | watchOS / SF Compact | watchOS / SF Compact Rounded |
|---|---|---|---|---|---|---|---|
| 6 | +41 (+0.24) | +87 (+0.51) | +40 (+0.23) | +41 (+0.24) | +41 (+0.24) | +50 (+0.29) | +28 (+0.16) |
| 7 | +34 (+0.23) | +80 (+0.54) | +32 (+0.22) | +34 (+0.23) | +34 (+0.23) | +30 (+0.21) | +26 (+0.18) |
| 8 | +26 (+0.21) | +72 (+0.57) | +25 (+0.20) | +26 (+0.21) | +26 (+0.21) | +30 (+0.23) | +24 (+0.19) |
| 9 | +19 (+0.17) | +65 (+0.57) | +20 (+0.18) | +19 (+0.17) | +19 (+0.17) | +30 (+0.26) | +22 (+0.19) |
| 10 | +12 (+0.12) | +58 (+0.57) | +16 (+0.15) | +12 (+0.12) | +12 (+0.12) | +30 (+0.29) | +20 (+0.20) |
| 11 | +6 (+0.06) | +52 (+0.56) | +11 (+.12) | +6 (+0.06) | +6 (+0.06) | +24 (+0.26) | +18 (+0.19) |
| 12 | 0 (0.0) | +46 (+0.54) | +6 (+0.07) | 0 (0.0) | 0 (0.0) | +20 (+0.23) | +16 (+0.19) |
| 13 | -6 (-0.08) | +40 (+0.51) | +4 (+0.05) | -6 (-0.08) | -6 (-0.08) | +16 (+0.20) | +14 (+0.18) |
| 14 | -11 (-0.15) | +35 (+0.48) | +2 (+0.03) | -11 (-0.15) | -11 (-0.15) | +14 (+0.19) | +12 (+0.16) |
| 15 | -16 (-0.23) | +30 (+0.44) | +0 (+0.00) | -16 (-0.23) | -16 (-0.23) | +4 (+0.06) | +10 (+0.15) |
| 16 | -20 (-0.31) | +26 (+0.41) | -2 (-0.03) | -20 (-0.31) | -20 (-0.31) | 0 (0.00) | +8 (+0.12) |
| 17 | -26 (-0.43) | +22 (+0.37) | -4 (-0.07) | -26 (-0.43) | -26 (-0.43) | -4 (-0.07) | +6 (+0.10) |
| 18 | -25 (-0.44) | +21 (+0.37) | -6 (-0.11) | -25 (-0.44) | -25 (-0.44) | -8 (-0.14) | +4 (+0.07) |
| 19 | -24 (-0.45) | +20 (+0.37) | -8 (-0.15) | -24 (-0.45) | -24 (-0.45) | -12 (-0.22) | +2 (+0.04) |
| 20 | -23 (-0.45) | +18 (+0.36) | -10 (-0.20) | -23 (-0.45) | -23 (-0.45) | 0 (0.00) | 0 (0.00) |
| 21 | -18 (-0.36) | +17 (+0.35) | -10 (-0.21) | -18 (-0.36) | -18 (-0.36) | -2 (-0.04) | -2 (-0.04) |
| 22 | -12 (-0.26) | +16 (+0.34) | -10 (-0.23) | -12 (-0.26) | -12 (-0.26) | -4 (-0.09) | -4 (-0.09) |
| 23 | -4 (-0.10) | +16 (+0.35) | -11 (-0.25) | -4 (-0.10) | -4 (-0.10) | -6 (-0.13) | -6 (-0.13) |
| 24 | +3 (+0.07) | +15 (+0.35) | -11 (-0.26) | +3 (+0.07) | +3 (+0.07) | -8 (-0.19) | -8 (-0.19) |
| 25 | +6 (+0.15) | +14 (+0.35) | -11 (-0.27) | +6 (+0.15) | +6 (+0.15) | -10 (-0.24) | -10 (-0.24) |
| 26 | +8 (+0.22) | +14 (+0.36) | -12 (-0.29) | +8 (+0.22) | +8 (+0.22) | -11 (-0.28) | -11 (-0.28) |
| 27 | +11 (+0.29) | +14 (+0.36) | -12 (-0.32) | +11 (+0.29) | +11 (+0.29) | -12 (-0.30) | -12 (-0.30) |
| 28 | +14 (+0.38) | +13 (+0.36) | -12 (-0.33) | +14 (+0.38) | +14 (+0.38) | -12 (-0.34) | -12 (-0.34) |
| 29 | +14 (+0.40) | +13 (+0.37) | -12 (-0.34) | +14 (+0.40) | +14 (+0.40) | -14 (-0.38) | -14 (-0.38) |
| 30 | +14 (+0.40) | +12 (+0.37) | -12 (-0.37) | +14 (+0.40) | +14 (+0.40) | -14 (-0.42) | -14 (-0.42) |
| 31 | +13 (+0.39) | +12 (+0.36) | -13 (-0.39) | +13 (+0.39) | +13 (+0.39) | -15 (-0.45) | -15 (-0.45) |
| 32 | +13 (+0.41) | +12 (+0.38) | -13 (-0.41) | +13 (+0.41) | +13 (+0.41) | -16 (-0.50) | -16 (-0.50) |
| 33 | +12 (+0.40) | +12 (+0.39) | -13 (-0.42) | +12 (+0.40) | +12 (+0.40) | -17 (-0.55) | -17 (-0.55) |
| 34 | +12 (+0.40) | +12 (+0.38) | -14 (-0.45) | +12 (+0.40) | +12 (+0.40) | -18 (-0.60) | -18 (-0.60) |
| 35 | +11 (+0.38) | +11 (+0.38) | -14 (-0.48) | +11 (+0.38) | +11 (+0.38) | -18 (-0.63) | -18 (-0.63) |
| 36 | +10 (+0.37) | +11 (+0.39) | -14 (-0.49) | +10 (+0.37) | +10 (+0.37) | -20 (-0.69) | -20 (-0.69) |
| 37 | +10 (+0.36) | +10 (+0.38) |  | +10 (+0.36) | +10 (+0.36) | -20 (-0.72) | -20 (-0.72) |
| 38 | +10 (+0.37) | +10 (+0.39) | -14 (-0.52) | +10 (+0.37) | +10 (+0.37) | -20 (-0.74) | -20 (-0.74) |
| 39 | +10 (+0.38) | +10 (+0.38) |  | +10 (+0.38) | +10 (+0.38) | -20 (-0.76) | -20 (-0.76) |
| 40 | +10 (+0.37) | +10 (+0.39) | -14 (-0.55) | +10 (+0.37) | +10 (+0.37) | -20 (-0.78) | -20 (-0.78) |
| 41 | +9 (+0.36) | +10 (+0.38) |  | +9 (+0.36) | +9 (+0.36) | -20 (-0.80) | -20 (-0.80) |
| 42 | +9 (+0.37) | +10 (+0.39) | -14 (-0.57) | +9 (+0.37) | +9 (+0.37) | -20 (-0.82) | -20 (-0.82) |
| 43 | +9 (+0.38) | +9 (+0.38) |  | +9 (+0.38) | +9 (+0.38) | -20 (-0.84) | -20 (-0.84) |
| 44 | +8 (+0.37) | +8 (+0.37) | -14 (-0.62) | +8 (+0.37) | +8 (+0.37) | -20 (-0.86) | -20 (-0.86) |
| 45 | +8 (+0.35) | +8 (+0.37) |  | +8 (+0.35) | +8 (+0.35) | -20 (-0.88) | -20 (-0.88) |
| 46 | +8 (+0.36) | +8 (+0.36) | -14 (-0.65) | +8 (+0.36) | +8 (+0.36) | -20 (-0.92) | -20 (-0.92) |
| 47 | +8 (+0.37) | +8 (+0.37) |  | +8 (+0.37) | +8 (+0.37) | -20 (-0.94) | -20 (-0.94) |
| 48 | +8 (+0.35) | +8 (+0.35) | -14 (-0.68) | +8 (+0.35) | +8 (+0.35) | -20 (-0.96) | -20 (-0.96) |
| 49 | +7 (+0.33) | +8 (+0.36) |  | +7 (+0.33) | +7 (+0.33) | -21 (-1.00) | -21 (-1.00) |
| 50 | +7 (+0.34) | +7 (+0.34) | -14 (-0.71) | +7 (+0.34) | +7 (+0.34) | -21 (-1.03) | -21 (-1.03) |
| 51 | +7 (+0.35) | +6 (+0.32) |  | +7 (+0.35) | +7 (+0.35) | -21 (-1.05) | -21 (-1.05) |
| 52 | +6 (+0.33) | +6 (+0.33) | -14 (-0.74) | +6 (+0.31) | +6 (+0.31) | -21 (-1.07) | -21 (-1.07) |
| 53 | +6 (+0.31) | +6 (+0.31) |  | +6 (+0.33) | +6 (+0.33) | -22 (-1.11) | -22 (-1.11) |
| 54 | +6 (+0.32) | +6 (+0.32) | -15 (-0.79) | +6 (+0.32) | +6 (+0.32) | -22 (-1.13) | -22 (-1.13) |
| 56 | +6 (+0.30) | +6 (+0.30) |  | +6 (+0.30) | +6 (+0.30) | -22 (-1.20) | -22 (-1.20) |
| 58 | +5 (+0.28) | +4 (+0.25) | -15 (-0.85) | +5 (+0.28) | +5 (+0.28) | -22 (-1.25) | -22 (-1.25) |
| 60 | +4 (+0.26) | +4 (+0.23) |  | +4 (+0.26) | +4 (+0.26) | -22 (-1.32) | -22 (-1.32) |
| 62 | +4 (+0.24) | +4 (+0.21) | -15 (-0.91) | +4 (+0.24) | +4 (+0.24) | -22 (-1.36) | -22 (-1.36) |
| 64 | +4 (+0.22) | +3 (+0.19) |  | +4 (+0.22) | +4 (+0.22) | -23 (-1.44) | -23 (-1.44) |
| 66 | +3 (+0.19) | +2 (+0.16) | -15 (-0.97) | +3 (+0.19) | +3 (+0.19) | -24 (-1.51) | -24 (-1.51) |
| 68 | +2 (+0.17) | +2 (+0.13) |  | +2 (+0.17) | +2 (+0.17) | -24 (-1.56) | -24 (-1.56) |
| 70 | +2 (+0.14) | +2 (+0.14) | -16 (-1.06) | +2 (+0.14) | +2 (+0.14) | -24 (-1.64) | -24 (-1.64) |
| 72 | +2 (+0.14) | +2 (+0.11) | -16 (-1.09) | +2 (+0.14) | +2 (+0.14) | -24 (-1.69) | -24 (-1.69) |
| 76 | +1 (+0.07) | +1 (+0.07) |  | +1 (+0.07) | +1 (+0.07) | -25 (-1.86) | -25 (-1.86) |
| 80 | 0 (0) | 0 (0.00) | -16 (-1.21) | 0 (0) | 0 (0) | -26 (-1.99) | -26 (-1.99) |
| 84 | 0 (0) | 0 (0.00) |  | 0 (0) | 0 (0) | -26 (-2.13) | -26 (-2.13) |
| 88 | 0 (0) | 0 (0.00) | -16 (-1.33) | 0 (0) | 0 (0) | -26 (-2.28) | -26 (-2.28) |
| 92 | 0 (0) | 0 (0.00) |  | 0 (0) | 0 (0) | -28 (-2.47) | -28 (-2.47) |
| 96 | 0 (0) | 0 (0.00) | -16 (-1.50) | 0 (0) | 0 (0) | -28 (-2.62) | -28 (-2.62) |
| 100 |  |  | -16 (-1.56) |  |  |  |  |
| 120 |  |  | -16 (-1.88) |  |  |  |  |
| 140 |  |  | -16 (-2.26) |  |  |  |  |
| 160 |  |  | -16 (-2.58) |  |  |  |  |
| 180 |  |  | -17 (-2.99) |  |  |  |  |
| 200 |  |  | -17 (-3.32) |  |  |  |  |
| 220 |  |  | -18 (-3.76) |  |  |  |  |
| 240 |  |  | -18 (-4.22) |  |  |  |  |
| 260 |  |  | -18 (-4.57) |  |  |  |  |



# 2. Patterns

# C — HIG Patterns (all 25 pages)

Scope: the `Patterns` collection [hig:patterns] ("guidance for supporting common user actions, tasks, and experiences") and its 25 pages. Tags: **[AI]** = relevant to an AI chat/agent product; **[XPLAT]** = cross-platform decision (details consolidated in table C.X); **[NEW]** = 2025–26 change. Numeric specs are collected in C.Z and change logs in C.Y.

## C.0 Cross-pattern principles (synthesis)

1. **Interruption ladder.** Match the delivery to the significance: inline status → tip → sheet → alert → notification interruption level. Overuse devalues every level [hig:feedback, hig:modality, hig:managing-notifications]. **[AI]**
2. **Never block.** Show something immediately, let people keep working, finish user-initiated tasks in the background, and notify only for important completions [hig:loading, hig:multitasking]. **[AI]**
3. **Reversibility beats confirmation.** Warn only about loss that is *unexpected and irreversible*. Otherwise make the action undoable, with multiple levels, labelled and visible [hig:feedback, hig:undo-and-redo]. **[AI]**
4. **Defer commitment.** No sign-in, setup, permissions, tutorials, ratings or purchases before value [hig:managing-accounts, hig:onboarding, hig:ratings-and-reviews]. **[AI]**
5. **Context over chrome.** Task options live in the task, settings stay few, help is contextual and dismissible [hig:settings, hig:offering-help].
6. **Preserve and restore state.** Autosave; restore the exact position; resume after switching [hig:launching, hig:file-management, hig:multitasking]. **[AI]**
7. **Respect system choices.** Volume, Focus, biometrics, accessibility and appearance belong to the OS; don't duplicate them [hig:settings, hig:managing-accounts, hig:playing-audio].

---

## Charting data `[hig:charting-data]`
**Purpose:** charts communicate insight, not raw data.
- Use a chart only to highlight something important. For plain data, use a scrollable, searchable, sortable list or table.
- Keep it simple and reveal detail or subsets progressively. Consider versions with increasing functionality to teach interaction.
- Make every chart accessible: labels for values and components plus interactive accessibility elements. A headline doesn't replace labels.
- Prefer common types (bar, line). A novel type must teach itself (Activity rings animate individually).
- Mine macro (totals, averages), mid (subsets) and micro (specific points) levels for enhancements.
- Add a title, subtitle, annotations and a summary headline ("Chance of light rain in the next hour").
- Size to function: large for interactive, small for a glanceable preview that expands.
- Keep similar-purpose charts consistent. Several charts of one dataset share type, colours, marks and annotations.
- Platforms: none. **[AI]** Generated charts need a plain-language takeaway plus a table fallback. A WWDC25 Chart3D video is linked **[NEW]**.

## Collaboration and sharing `[hig:collaboration-and-sharing]`
**Purpose:** simple sharing and collaboration via the share sheet, Messages and the Collaboration button.
- Put the **Share button** in the toolbar. The iOS 16 share sheet and the iPadOS 16 / macOS 13 sharing popover let people choose a method and set permissions (SwiftUI `ShareLink`).
- Customize the sheet for supported sharing types, including "send copy" (CloudKit: file + collaboration object; iCloud Drive: default; custom: include the file or a plain-text version).
- **Summarize permissions in a short phrase** ("Only invited people can edit", "Everyone can make changes"). Keep options few and grouped: who has access, edit vs read, whether collaborators can add people.
- Show the **Collaboration button** next to Share as soon as collaboration starts; it shows who's sharing. Its popover has **3 sections**: collaborators with Messages/FaceTime; essential custom items only (e.g. recent updates); a management button, default "Manage Shared File", whose title you can change.
- Post events (content change, membership change, mention) to Messages with a universal link. Custom infrastructure requires universal links. SharePlay for real time.
- Platforms: **not available in tvOS**. visionOS: the Shared Space streams the window; a Full Space pauses it for others. watchOS: `ShareLink`.
- **[AI]** Shared chats and projects: a permission phrase, a persistent "who has access" indicator (trust), and mention notifications that deep-link. **[XPLAT]** share icon and sheet.

## Drag and drop `[hig:drag-and-drop]`
**Purpose:** move or copy a selection from source to destination.
- **Semantics:** same container → move; different container → copy; **between apps → always copy**. Option held at drop forces a copy (release before drop → move). When changing defaults, pick whatever is least likely to cause data loss.
- Support it everywhere, and **always provide an alternative** (menu commands, accessibility drag/drop descriptors). Support multi-item drags (iPadOS adds items mid-drag; macOS across apps).
- Prefer undoable drops. Confirm ones that can't be undone (Finder: write-only folder), or offer a reversal (Photos: cancel sharing).
- Offer representations from highest to lowest fidelity (PDF → PNG → JPEG; native chart → image). Spring loading activates controls under a drag (iPad hover, Mac force-click).
- **Feedback:**
  - Show a translucent drag image after **~3 pt** of movement, held until the drop.
  - Morph it to predict the result, or *flock* multiple items, without constant radical change.
  - Highlight or show an insertion point only on valid destinations while hovering, otherwise nothing or `circle.slash`. Cue one destination at a time.
  - On failure, animate back to the source or scale up and fade.
- **Accepting:**
  - Auto-scroll destinations while hovering, and take the richest acceptable format, keeping only the relevant part (contact → name + email).
  - For slow transfers show progress plus a placeholder at the drop point. If a drop starts a task, show that it started and its progress.
  - Keep text styles if both sides support them. Keep dropped content selected and deselect the source on cross-container drags.
- Platforms: **not tvOS or watchOS**.
  - macOS: drag to the Finder as a reopenable file (`.ics`) or a clipping (not the Clipboard); drag from an inactive window without activating it or clearing its background selection; count badge (updates if a subset is accepted); copy, link, disappearing-item and not-allowed pointers; single-motion select-and-drag.
  - visionOS: dropping into empty space can launch the handling app.
- **[AI]** The composer is a drop target: hover highlight, an upload progress chip, and rejection with a reason; always paired with Attach and paste. Dragging output out offers rich → Markdown → plain text. **[XPLAT]** modifier keys.

## Entering data `[hig:entering-data]` **[AI]**
**Purpose:** minimize input and errors. Pre-gather data and support all input methods.
- Get data from the system or a permission (location, calendar) instead of asking.
- State what's needed with a placeholder ("username@company.com") or label ("Email"), and prefill sensible defaults.
- Use secure entry (a dot per character) for sensitive data. In visionOS only the wearer sees input, and secure fields blur over AirPlay.
- **Never prepopulate passwords**; use entry, biometrics or keychain.
- Prefer pickers and menus to typing, even with a keyboard. Accept drag and paste.
- **Validate dynamically, on entry.** Use number formatters (numeric only; decimals, %, currency).
- Enable Next/Continue only once required data is present.
- macOS: an *expansion tooltip* shows the full text of a truncated field on hover.
- **[AI]** Suggested-prompt chips; paste and drop into the composer; secure, never-echoed fields for API keys; inline key/URL validation; Send disabled when empty. **[XPLAT]** disabled vs enabled submit.

## Feedback `[hig:feedback]` **[AI]**
**Purpose:** show status, next steps and results, and help people avoid mistakes. Types: status, success/failure of an important task, warning, chance to correct. Status is passive; a data-loss warning interrupts.
- **Multimodal and accessible:** colour + text + sound + haptics, so feedback still works when the device is silenced, people look away, or VoiceOver is on.
- Put status next to what it describes (Mail toolbar: updated time, unread count).
- Use alerts only for critical, ideally actionable information.
- **Warn only for unexpected, irreversible data loss.** No warning when loss is the expected result (Trash).
- Confirm completion only for significant actions (Apple Pay). People expect success, so tell them about failures.
- When something can't be done, **say why** (Maps: same origin and destination).
- watchOS: avoid indeterminate indicators; promise a notification instead. Other platforms: none.
- **[AI]** Agent status, thinking and tool calls go inline in the transcript, not in alerts. Confirm only consequential completions (sent, bought, deployed). Every refusal or error gives the reason and a next step. Warn before surprising destructive steps, not before the expected outcome. Use notifications instead of spinners for background runs.

## File management `[hig:file-management]` **[AI]**
**Purpose:** create, open, save and preview documents consistently with Finder/Files. tvOS and watchOS have no document browsing.
- Provide New/Open as menu commands and shortcuts (iPadOS Command-key overlay, macOS File menu), plus an **Add (+)** button.
- A custom browser respects the system file system: open at a relevant location, allow full navigation.
- **Autosave** periodically, on close and on app switch; no explicit save needed. Work persists unless cancelled or deleted.
- Hide extensions by default with an option to show; reflect the choice everywhere.
- Quick Look: a viewer for unsupported files; a generator for custom types (Finder, Files, Spotlight previews).
- **Document launcher (iOS/iPadOS 18+):**
  - Parts: title card (app name + primary and secondary buttons); background plus *accessories*; a file-browser sheet (Recents/Shared/Browse) with optional controls.
  - Primary creates ("Start Writing"), secondary extends ("Choose a Template").
  - Simple, distinct background (solid, gradient, pattern). Accessories must not hide the name or buttons; avoid clutter.
  - Test across sizes and orientations; only gentle, repeating animation (breathe, sway).
- **File provider extension:** show only context-appropriate files with metadata (date, size, local/remote). Allow choosing the destination and new subfolders. No custom top toolbar.
- **macOS:**
  - Default panels unless there's a strong reason. A custom open panel can add Open Recent, filters, multi-select, or a retitled button ("Insert").
  - The save panel covers name, format and location; default name "Untitled"; optional accessory view (Mail: include attachments). Finder Sync adds badges, menu items and toolbar buttons.
  - With autosave off (the Desktop & Dock "Ask to keep changes" setting), prompt on close, quit, log-out or restart.
  - **Unsaved dot** on the close button and in the Window menu **only when autosave is off**. An "Edited" title suffix is fine but clear it on save.
- **[AI]** Autosave drafts and generated artifacts, show save/sync state, preview attachments inline, use native pickers. **[XPLAT]** save model.

## Going full screen `[hig:going-full-screen]`
**Purpose:** distraction-free mode on iPhone, iPad and Mac. **Not tvOS, visionOS or watchOS.**
- Offer it for games, media and in-depth tasks. Adjust proportions, but **never programmatically resize the window**, and avoid jarring transitions.
- Keep essential controls reachable. Except in games, keep the Dock revealable (games may defer the first swipe or hide the Dock).
- Auto-pause on switching away and resume in place. Let people choose when to exit; no auto-exit.
- **[NEW Jun 2025]** You may hide toolbars and navigation while content is the focus. Restore them on tap, swipe down or pointer at the top; keep essential navigation.
- iOS/iPadOS: the Home indicator auto-hides; one swipe exits, or two if accidental exits are a problem.
- macOS: use the system full screen (it handles the camera housing). Games never change the display mode. Enter via the window button, View menu or **Control-Command-F**; no custom window-mode menu.
- **[AI]** A focus/reading mode for long outputs or canvases. **[XPLAT]** shortcut.

## Launching `[hig:launching]`
**Purpose:** instant start. Launch runs from opening (including first download) to the first screen being ready; onboarding comes after.
- Launch instantly; people may not wait more than **a couple of seconds**.
- A launch screen is required on iOS, iPadOS and tvOS, **not on macOS, visionOS or watchOS**.
- A splash screen (branding) belongs at the start of onboarding, or right after launch if there is no onboarding.
- **Restore state in detail**: scroll position, window state and location.
- **Launch-screen rules:**
  - Purely for perceived speed; not onboarding, splash or art.
  - **Nearly identical to the first screen** (solid colour if that's what the first screen is), matching orientation and light/dark.
  - **No text** (it isn't localized). **No ads or logos** unless they're part of the first screen.
- iOS/iPadOS: launch in the current orientation; landscape-only apps handle both directions. tvOS: the launch screen is static; live apps may auto-play after a few seconds idle. visionOS: start in a Shared Space window and let people choose a Full Space.
- **[AI]** Restore the last conversation, scroll position, unsent draft and window layout. The launch screen is a logo-free shell. **[XPLAT]** Android splash.

## Live-viewing apps `[hig:live-viewing-apps]`
**Purpose:** live-TV apps that put live content first and keep it distinct from VOD.
- Live content goes in the first tab (**≤1 tap**). Play on 0–1 taps: a Watch Now button disappears into full-screen playback.
- Make live look live (badge, symbol, sash, "Live" row) and show progress through in-progress content.
- Playback is the primary action. Keep secondary actions in a consistent order (Watch, Start Over, Record, Favorite) and show re-air times.
- Content footer during playback: subtle darkening, current item badged, EPG categories, symmetric invoke/dismiss.
- Give instant feedback on channel change (also buys load time). Audio stops when people leave the live tab.
- **EPG:** current program prominent, easy return, fast paging, Favorites, familiar categories, browse while playing (PiP). **Cloud DVR:** record from the info panel; future/series rules; auto storage management.
- **[AI]** A "live" indicator for streaming or running sessions.

## Loading `[hig:loading]` **[AI]**
**Purpose:** "The best content-loading experience finishes before people become aware of it."
- **Show something ASAP**: placeholders, replaced progressively. A blank screen reads as a bug.
- Let people do other things while loading.
- For long waits show tips or features, with an accurate time estimate so content neither runs out nor repeats.
- Download large assets in the background (Background Assets, after install or update) **[NEW Jun 2025]**.
- **Progress:** for anything beyond "a moment or two", use a progress indicator: **determinate** if the duration is known, **indeterminate** if not. Games may use custom loaders.
- watchOS: avoid loaders, but for **1–2 s** a loader beats a blank screen.
- **[AI]** Stream the first tokens immediately (the stream is the placeholder) and use skeletons for history and results. The composer stays live during generation (Stop, draft the next prompt). Agent runs show a determinate "Step 3 of 7" when the plan is known, otherwise indeterminate progress plus an activity log. Show estimates only when reliable.

## Managing accounts `[hig:managing-accounts]` **[AI]**
**Purpose:** require an account only for core functionality, and make it trustworthy and easy to leave.
- Explain the benefits briefly in the sign-in view. **Delay sign-in as long as possible** (browse freely, sign in at purchase).
- Offer Sign in with Apple; otherwise **prefer passkeys**. If you keep passwords, require 2FA.
- Name the method ("Sign In with Face ID") and only mention methods the device has.
- No in-app biometric opt-in (that's a system setting). Never say "passcode".
- **Deletion (mandatory if accounts are created in-app):**
  - Real deletion, not deactivation; follow right-to-be-forgotten laws. If you must retain data, explain what and why.
  - Start it in-app, or give a direct, discoverable web link (not buried in the privacy policy). Same effort in-app and on the web.
  - Scheduled deletion is optional, but always alongside an immediate option. Say when it completes and notify when done.
  - With in-app purchases, explain that billing continues until people cancel the subscription and that refunds are separate. Support deletion regardless of where the purchase was made. With Sign in with Apple, revoke tokens on deletion.
- **TV provider:** use system TV Provider Authentication. No sign-out while signed in at system level (or route to Settings > TV Provider), and never via Privacy controls.
- tvOS: minimal input; sign in on another device (associated domains); shared accounts (tvOS 16+) don't re-ask the profile; long forms go to a website; email keyboard with recents. watchOS: iCloud Keychain sync.
- **[AI]** Try before sign-in, passkeys first. Deletion covers chats, memory and files, with schedule-or-now and completion notice. **[NEW]** The WWDC25 passkeys video covers the account-creation API and automatic upgrades. **[XPLAT]** biometric naming.

## Managing notifications `[hig:managing-notifications]` **[AI]**
**Purpose:** timely, important information. **Get permission before any notification.** People can change it or silence everything (government alerts excepted in some locales).
- **Focus** filters by activity (sleep, work, driving). **Scheduled delivery** batches alerts into summaries. People choose who breaks through. A Focus delays only the *alert*; the notification is available immediately.
- *Communication* notifications (calls, messages; SiriKit intents) are delivered according to the sender. *Noncommunication* notifications need an interruption level:
  - **Passive:** whenever convenient (a recommendation).
  - **Active (default):** on arrival (a score update).
  - **Time Sensitive:** directly impacts the person, needs immediate attention (a security issue, a delivery).
  - **Critical:** health or safety, extremely rare, **requires an entitlement**.

| Interruption level | Overrides scheduled delivery | Breaks through Focus | Overrides Ring/Silent switch on iPhone and iPad |
|---|---|---|---|
| Passive | No | No | No |
| Active | No | No | No |
| Time Sensitive | Yes | Yes | No |
| Critical | Yes | Yes | Yes |

- Represent urgency accurately; overclaiming erodes trust. Use **Time Sensitive only for events happening now or within an hour**. The system explains it the first time, offers to turn it off, and re-asks periodically.
- **Marketing:** explicit opt-in only, through UI that describes the content with a clear in/out. **Never Time Sensitive.** An **in-app notification settings screen is required**.
- watchOS: mirrors iPhone settings. Swipe left for Mute 1 Hour or Turn off Time Sensitive.
- **[AI]** Run finished → Active. Blocked on a time-bound approval → Time Sensitive (≤1 h only). Suggestions → Passive or summary. Never Critical. Per-category toggles. **[XPLAT]** level mapping.

## Modality `[hig:modality]` **[AI]**
**Purpose:** a dedicated mode that blocks the parent view and needs explicit dismissal. Use it for critical information, to confirm or modify the last action, for a scoped task that keeps context, or for immersion.
- **Types:** alert (all platforms); activity view; sheet; confirmation dialog / action sheet; popover; separate window (iPadOS, macOS, visionOS); full-screen modal for media or multistep editing. Nonmodal full screen is covered in [hig:going-full-screen].
- Use only with a clear benefit. Keep it **simple, short, streamlined**.
- No "app within the app": a single path through any subviews, and no buttons that look like Dismiss.
- Full-screen modal for in-depth content (video, camera, markup, photo edit). visionOS: it fills the window, or becomes immersive in a Full Space.
- **Obvious dismissal:** iOS, iPadOS and watchOS use a top-toolbar button or swipe down; macOS and tvOS use a button in the content view.
- **Confirm before closing if user content would be lost**, whether by gesture or button, and offer a fix (an action sheet with Save).
- Title the modal with its task.
- **Never stack modals.** At most **one alert at a time**, though an alert may sit above everything.
- Platforms: none.
- **[AI]** Tool approvals are modal only for consequential, irreversible steps; otherwise use inline approval cards. Queue approvals, never stack them. Dismissing a sheet with an unsent prompt autosaves or confirms. **[XPLAT]** dismiss placement.

## Multitasking `[hig:multitasking]` **[AI]**
**Purpose:** quick switching between apps. Every app must support it (except some games and visionOS Full Space).
- Always be ready to save and restore context.
- Pause attention-requiring activities (games, media) and resume seamlessly.
- Audio interruptions: **pause indefinitely** for primary ones (music, podcasts); **duck or pause, then restore** for short ones (GPS prompts).
- **Finish user-initiated tasks in the background** if no input is needed.
- Notify for important task completions only, not routine ones.
- Platforms: **not supported in watchOS**.
  - iOS: app switcher; PiP.
  - **iPadOS [NEW Jun 2025]:** full-screen or windowed apps. Windowed apps are resizable, macOS-style, with system controls for tiling, full screen, minimize and close. The frontmost window has coloured controls and casts a shadow. Multiple windows per app; PiP everywhere. **Apps can't control or detect the configuration**, so adapt to any size.
  - macOS: multitasking is the default, with layered shadows and window states.
  - tvOS: PiP.
  - visionOS: one active window; inactive windows go translucent and recede in z. Closing a window backgrounds the app (Now Playing audio pauses). Don't alter window edges (system feathering). Don't pause video when people look away. Expect ducking if you aren't Now Playing.
- The page **no longer specifies Split View or Slide Over fractions**; see [hig:windows] and [hig:layout].
- **[AI]** Agent runs continue in the background or server-side and notify only for important user-started tasks. Restore exact context on return. Support multiple conversation windows and fluid widths.

## Offering help `[hig:offering-help]` **[AI]**
**Purpose:** contextual help where the UI can't explain itself.
- Size help to the task: inline text for 1–2-step tasks, a tutorial for complex goals. Tie it to the current action and make it dismissible.
- Use device-correct language and images (no "click" on iPhone, no controller art for Siri Remote users). Keep it inclusive.
- Don't explain standard components; explain what they do here. For unique controls use animation or graphics, not paragraphs.
- **Tips (TipKit):**
  - *Popover* tips preserve flow but overlay content. *Inline* tips keep context visible: **annotation** style points at UI, **hint** style is untethered.
  - Simple features only (**>3 actions is too complex**). **1–2 sentences**, action-oriented, never promotional.
  - Use eligibility rules (parameter- or event-based) and skip people who already use the feature. With several tips, set a cadence (e.g. **once every 24 h**).
  - Use the feature's symbol in its **filled** variant, but not when the tip points at that same image. Buttons may link to settings or more information.
- **Tooltips (macOS, visionOS: hover or look):**
  - Describe only the indicated control, **verb-first** ("Restore default settings"), without repeating its name.
  - **Max 60–75 characters** (localization lengthens text); fragments are fine.
  - **Sentence case**, no ending punctuation. Text may vary by state. Long tooltips mean the UI should be simpler.
- **[AI]** Composer feature tips ("Type @ to add a file") hidden after use, ≤1 per 24 h. Every icon-only control gets a ≤75-character verb-first tooltip. **[XPLAT]** tooltips on touch and focus.

## Onboarding `[hig:onboarding]` **[AI]**
**Purpose:** a quick start that is **fast, fun and optional**, and happens after launch.
- **Teach through interactivity**: let people safely try the real action.
- Prefer contextual tips near the relevant UI to one big flow.
- Make any required flow brief, enjoyable and low on memorization. A separate tutorial is optional: if skipped, never re-shown automatically, but findable in help, account or settings.
- Teach the app, not the device.
- Show a splash only briefly. Don't let large downloads block the start; bundle enough content. No licensing text (the App Store shows it).
- **Postpone nonessential setup**; ship good defaults.
- Ask for permissions during onboarding only if the app can't work without them, explaining why. Otherwise ask at first use [hig:privacy].
- Ask for ratings or purchases only after people have experienced the app.
- **[AI]** First run is an interactive first prompt with starters, not a carousel. Request mic, files and connector access at first use. Defer model, persona and memory setup. No upsell before a successful first task.

## Playing audio `[hig:playing-audio]`
**Purpose:** audio that follows context.
- **Silent mode** plays only audio people explicitly start (media, alarms, A/V messaging). **Volume** governs everything (the iPhone ringer is separate). **Headphones:** connecting reroutes seamlessly; **disconnecting pauses immediately**.
- Adjust only relative mix levels, never system volume. Allow rerouting (AirPlay, Bluetooth) and use the system volume view.
- Choose the category:

| Category | Meaning | Behavior |
|---|---|---|
| Solo ambient | Sound isn’t essential, but it silences other audio. For example, a game with a soundtrack. | Responds to the silence switch. Doesn’t mix with other sounds. Doesn’t play in the background. |
| Ambient | Sound isn’t essential, and it doesn’t silence other audio. For example, a game that lets people play music from another app during gameplay in place of the game’s soundtrack. | Responds to the silence switch. Mixes with other sounds. Doesn’t play in the background. |
| Playback | Sound is essential and might mix with other audio. For example, an audiobook or educational app that teaches a foreign language, which people might want to listen to after leaving the app. | Doesn’t respond to the silence switch. May or may not mix with other sounds. Can play in the background. |
| Record | Sound is recorded. For example, a note-taking app that offers an audio recording mode. An app of this nature might switch its category to playback if it lets people play the recorded notes. | Doesn’t respond to the silence switch. Doesn’t mix with other sounds. Can record in the background. |
| Play and record | Sound is recorded and played, potentially simultaneously. For example, an audio messaging or video calling app. | Doesn’t respond to the silence switch. May or may not mix with other sounds. Can record and play in the background. |

- Respond to external controls only when playing or connected to Bluetooth/AirPlay. Never repurpose controls. Notify other apps when temporary audio ends.
- **Interruptions:**
  - **Privacy:** never auto-restart a muted mic session (iPad Smart Folio example).
  - Media apps resume only after *resumable* interruptions (calls), not *nonresumable* ones (a new playlist). Games auto-resume.
- Platforms:
  - macOS: notification sounds mix.
  - tvOS: only user-initiated audio.
  - visionOS: Spatial Audio. Never convey information by sound alone (all platforms). Prefer playing sound, since silence feels broken. Use custom sounds for custom UI. Ambient audio plus point sources that follow the window. Randomize pitch and volume to avoid repetition. Choose *fixed* or *tracked* sound.
  - watchOS: **64 kbps HE-AAC**; Now Playing view.
- **[AI]** Voice mode uses Play and record. **Never re-arm the mic automatically after an interruption**; always show mic state. Pause TTS when headphones disconnect.

## Playing haptics `[hig:playing-haptics]`
**Purpose:** touch feedback that reinforces cause and effect. Sources: iPhone controls, Watch Taptic Engine, Mac Force Touch trackpad, game controllers, Apple Pencil Pro and some iPad trackpads.
- Use system patterns **only for their documented meanings**, with consistent cause→effect.
- Pair haptics with visuals and sound, matching intensity and sharpness to the animation. Don't overuse; the ideal is unnoticed but missed when off.
- In apps, prefer short haptics for discrete events (no long ones on Pencil Pro).
- **Make haptics optional**; the app must work without them. Avoid disturbing the camera, gyro or mic.
- **Custom (Core Haptics):** *transient* (tap) and *continuous* (sustained) events, tuned by **sharpness** and **intensity**, with optional audio.

| iOS feedback generator category | Patterns (documented meaning) |
|---|---|
| Notification (outcome of a task) | **Success** — task/action completed (2 pulses); **Warning** — produced a warning (2 pulses); **Error** — error occurred (4 pulses) |
| Impact (physical metaphor) | **Light** — small/lightweight UI objects collide; **Medium** — medium-sized/weight; **Heavy** — large/heavyweight; **Rigid** — hard/inflexible; **Soft** — soft/flexible (single pulse each) |
| Selection | **Selection** — a UI element's values are changing |

| Haptic feedback pattern (macOS, Magic Trackpad: drag or force click) | Description |
|---|---|
| Alignment | Indicates the alignment of a dragged item. For example, this pattern could be used in a drawing app when the people drag a shape into alignment with another shape. Other scenarios where this type of feedback could be used might include scaling an object to fit within specific dimensions, positioning an object at a preferred location, or reaching the beginning/end or minimum/maximum of something like a scrubber in a video app. |
| Level change | Indicates movement between discrete levels of pressure. For example, as people press a fast-forward button on a video player, playback could increase or decrease and haptic feedback could be provided as different levels of pressure are reached. |
| Generic | Intended for providing general feedback when the other patterns don’t apply. |

| watchOS haptic (Digital Crown detents from Series 4) | Meaning |
|---|---|
| Notification | Something significant/out of the ordinary needs attention (also played on notification arrival) |
| Up / Down | Important value rose above / fell below a significant threshold |
| Success / Failure | Action completed successfully / failed |
| Retry | Action failed but can be retried |
| Start / Stop | Activity the person can start/stop (timer) started / stopped |
| Click | Dial-click at predefined increments; overuse or overlap confuses |

- **[AI]** On mobile, Success when a foreground run completes and Error on failure. **No per-token haptics.** Respect the system setting and offer an in-app toggle. **[XPLAT]** haptic tokens.

## Playing video `[hig:playing-video]`
**Purpose:** familiar, system-consistent playback.
- Default modes: **aspect-fill** for **2:1–2.40:1**; **aspect-fit** for **4:3, 16:9, ≤2:1 and >2.40:1**. PiP on most platforms. tvOS and visionOS add transport controls and content tabs (Info, Episodes, Chapters); in visionOS the controls are an ornament.
- Use the system player; a custom one must mirror its behaviour. Keep the **original aspect ratio**, never embedded padding (it breaks scaling and PiP). Metadata must not obscure playback.
- **Space plays/pauses** on all platforms (Bluetooth keyboard included).
- Prevent mixed audio across PiP and mode switches.
- **TV app:** show your own black screen immediately, play with no splash or intro, **auto-resume without asking** from the previous end time, and use the requested profile.
- **Loading:** avoid loading screens. If it takes **>2 s**, show black with a centred spinner and nothing else, only until playback can start.
- **Exit:** show a detail view with Resume, prepared in advance.
- tvOS: small logos only. Short, translucent SDR overlays because of image retention. Interactive overlays wait **≥0.5 s** after pausing, with a clear dismiss.
- visionOS: people start playback; small resizable window; surroundings visible; never auto-start immersive video; scrub thumbnails **160 px wide**; inline players never fill the window; RealityKit player for splash video.
- watchOS: clips **≤30 s**; posters represent content and never look like controls.

| Attribute (watchOS) | Value |
|---|---|
| Video codec | H.264 High Profile |
| Video bit rate | 160 kbps at up to 30 fps |
| Resolution (full screen) | 208x260 px (portrait orientation) |
| Resolution (16:9) | 320x180 px (landscape orientation) |
| Audio | 64 kbps HE-AAC |

## Printing `[hig:printing]`
**Purpose:** system printing on iOS, iPadOS, macOS and visionOS (**not tvOS or watchOS**).
- Make Print discoverable: macOS File menu (toolbar button optional); iOS toolbar → action sheet.
- **Only when possible**: dim it on macOS or remove it on iOS when there's nothing to print or no printer.
- Use the system view for page range, copies and duplex.
- macOS: a custom panel category named after the app; a page-setup dialog for per-document size and scale without duplicating system options; clear interdependencies; an **"Advanced Options"** disclosure; previews; settings stored with the document.
- **[AI]** Print/Export conversations and artifacts; disabled when empty.

## Ratings and reviews `[hig:ratings-and-reviews]`
**Purpose:** ask for ratings at the right time.
- Ask only after demonstrated engagement (a completed task or level). **Never on first launch or during onboarding.**
- Wait for natural breaks. Leave **at least a week or two** between requests.
- Prefer the system prompt (iOS, iPadOS, macOS): one tap, global opt-out, **max 3 times per app per 365 days**.
- Weigh a rating reset (current-version accuracy) against having fewer ratings.
- **[AI]** Keep inline per-response thumbs (always available, nonmodal) separate from rare store prompts after a successful task. Never prompt after errors.

## Searching `[hig:searching]` **[AI]**
**Purpose:** find content on the device, in the app and in documents.
- Use a search field. Personalize with recents, suggestions, completions and corrections. Scope with scope bars and tokens [hig:search-fields]. Support find-in-page.
- **Best practices [refined Jun 2026]:**
  - Important search gets a **primary position** (Notes: bottom toolbar; tab-bar apps: a Search tab).
  - **One location searches everything**; a section-local search filters the current view.
  - **Always show the current scope** (placeholder, scope bar, title).
  - Suggest recent searches before typing and predictions while typing.
  - **Consider privacy before showing history**, and allow clearing it.
- **Systemwide:** index content and metadata in Spotlight (File Importer for custom types); use Spotlight in-app for advanced search; prefer system open/save panels; add Quick Look generators.
- **[AI]** One global search over chats, projects and files, with scope chips. Clearable recents kept off shared surfaces. OS indexing of chats is **opt-in**. If one field does both "search" and "ask the AI", make the mode explicit. **[XPLAT]** placement.

## Settings `[hig:settings]` **[AI]**
**Purpose:** customization without breaking "just works". System Settings owns appearance, network, accounts, accessibility, language and per-app permissions. The in-app area holds general settings; task options go in the task.
- **Best defaults for most people.** Keep settings **few**.
- Open with **Command-Comma** (games: **Esc**).
- Don't ask for what you can detect (controller, Dark Mode).
- **Don't duplicate system-wide settings** (accessibility, scrolling, authentication); duplicates imply the system setting doesn't apply.
- Settings area: rarely changed options (window configuration, saves, key mappings, account). **Task-specific options in context** (show/hide, reorder, filter).
- Add to the system Settings app only the rarest options, and link to it.
- macOS:
  - Settings item in the **App menu**, never a toolbar button; document options in the File menu.
  - The settings window **dims minimize and zoom**, has a **noncustomizable, always-visible pane toolbar** showing the active pane, and takes **the pane's name as its title** ("*App Name* Settings" if there's a single pane).
  - **Restore the last pane.**
- watchOS: no system Settings entries; put options at the bottom of the main view or in a More menu.
- **[AI]** Model, tools and style live in the composer. Settings cover account, data and memory, and notifications (required). Cmd/Ctrl+, opens them. **[XPLAT]** appearance override, settings location.

## Undo and redo `[hig:undo-and-redo]` **[AI]**
**Purpose:** reversible actions make exploration safe. People undo repeatedly "until something changes", so outcomes must be predictable and visible.
- **Predict the result:** the iPhone shake alert names the action; menu labels say "Undo Typing" or "Redo Bold".
- **Show the result:** scroll to and highlight affected offscreen content; otherwise people repeat the undo.
- **Multiple undo**, with no arbitrary limit, back to the last open or save.
- **Batch revert:** group incremental tweaks and offer "revert all since open/save".
- Dedicated buttons only if needed, using standard symbols in a toolbar. Otherwise use the Edit menu, shortcuts or shake.
- Platforms: **not tvOS or watchOS**.
- iOS/iPadOS: don't redefine **three-finger swipe** or **shake**. The alert title is auto-prefixed **"Undo "/"Redo "**; supply 1–2 words ("Undo Name", "Redo Address Change").
- macOS: top of the **Edit menu**; **Command-Z / Shift-Command-Z**.
- **[AI]** Every agent mutation is undoable or checkpointed, with a labelled undo ("Undo Rename 12 Files"). Offer "Revert all changes from this run" (batch). Highlight restored items. Deleting a chat offers immediate undo. **[XPLAT]** undo toast and shortcuts.

## Workouts `[hig:workouts]`
**Purpose:** fitness tracking on Watch, iPhone and iPad (**not macOS, tvOS or visionOS**).
- Sessions keep the app visible between wrist raises: show key metrics and controls only. Typical pages: controls | metrics | Now Playing.
- Give an active session a distinct look with live values. Easy pause, resume and stop with clear feedback.
- Explain missing sensor data in Workout-app language (e.g. water may block heart rate, but the accelerometer still tracks calories and laps).
- End with a summary (optionally Activity rings). Discard or ask about sessions lasting a few seconds.
- Legible in motion: large type, high contrast. Activity rings only for their documented purpose.
- **[AI]** Explain degraded capability plainly; end agent runs with a summary.

---

## C.X Cross-platform decisions surfaced by Patterns **[XPLAT]**

| Topic | Apple (HIG) | Material / Android | Windows / Linux / Web | Parent-system recommendation |
|---|---|---|---|---|
| Modal dismissal | iOS: top-bar Cancel/Done + swipe down; macOS/tvOS: button in content (bottom-right) [hig:modality] | Dialog actions bottom-right; full-screen dialog ✕ top-left, Save top-right | Web: ✕ top-right, Esc, click-outside | Explicit button always; Esc closes non-destructive modals (desktop/web); swipe-down on mobile sheets; click-outside only for non-destructive popovers |
| Undo pattern | Edit menu, ⌘Z/⇧⌘Z, shake, 3-finger swipe; no toast | Snackbar with "Undo" action after destructive acts | Ctrl+Z / Ctrl+Y (or Ctrl+Shift+Z); toast-undo common on web | Undo toast on all platforms + standard shortcuts + Edit menu on desktop |
| Save model | Autosave; unsaved dot only when autosave off; "Edited" suffix [hig:file-management] | Autosave typical | Ctrl+S expected; "*" in title (Windows); "Saving…/Saved" text (web) | Autosave everywhere + text status; Cmd/Ctrl+S = harmless "save now/checkpoint" |
| Launch / splash | Launch screen = first-screen replica, no text/logo [hig:launching] | Android 12+ SplashScreen API: mandatory icon-centred splash | Desktop/web: no OS launch screen | iOS: skeleton replica; Android: system splash (icon on first-screen bg colour); desktop/web: app-shell skeleton |
| Notification urgency | Passive / Active / Time Sensitive / Critical [hig:managing-notifications] | Channels with Urgent/High/Default/Low/Min, user-controllable | Windows toast Default/High + Focus Assist; Web Push: no levels, permission on user gesture | 4 semantic levels mapped per platform (Passive→Low, Active→Default, Time Sensitive→High; Critical unused); per-category in-app toggles |
| Tooltips | macOS/visionOS only; hover/look; 60–75 chars [hig:offering-help] | Hover + focus; long-press on touch | Hover + keyboard focus (a11y) | Hover + focus on desktop/web; touch uses visible labels or long-press; never essential info only in a tooltip |
| Disabled submit | Enable Continue only when required data present [hig:entering-data] | Mixed | Web a11y often prefers enabled submit + inline errors | Disable only trivial cases (empty composer); forms keep submit enabled with inline errors |
| Settings access | ⌘, ; App menu; never toolbar; pane-toolbar window [hig:settings] | Settings screen from overflow/profile | Gear/avatar menu; page with left nav; Ctrl+, conventional (not standard) | Cmd/Ctrl+, everywhere; desktop App/File menu entry + avatar menu; web settings page with left nav |
| Appearance override | Don't duplicate system settings [hig:settings] | In-app theme common | In-app System/Light/Dark common | Default "System"; allow override |
| Full screen | ⌃⌘F, window button, View menu [hig:going-full-screen] | Immersive mode | F11; web Fullscreen API needs user gesture, Esc exits | Platform shortcut; always an on-screen toggle |
| Drag copy modifier | Option = copy; same container move, cross-app copy [hig:drag-and-drop] | Long-press drag | Windows: Ctrl = copy, Shift = move, Alt = link; default depends on volume | Platform-native modifiers; same-container move / cross-container copy as product default |
| Share | Share sheet / sharing popover; square-arrow glyph [hig:collaboration-and-sharing] | Share sheet; nodes glyph | Little/no share sheet; "Copy link" | Platform-native icon; web/desktop "Copy link" + invite dialog |
| Search placement | iOS bottom toolbar or Search tab [hig:searching] | Top search bar | Header field + Cmd/Ctrl+K or F | Per form factor: mobile bottom/tab (iOS), top (Android); desktop/web header + Cmd/Ctrl+K |
| Biometric naming | "Sign In with Face ID"; only available methods [hig:managing-accounts] | BiometricPrompt (fingerprint/face) | Windows Hello; WebAuthn passkeys | Method-specific labels per platform; passkeys first |
| Haptics | UIFeedbackGenerator / WKHapticType / trackpad patterns [hig:playing-haptics] | HapticFeedbackConstants (CONFIRM, REJECT…) | Mostly none; Vibration API absent on iOS Safari | Semantic haptic tokens (success/warning/error/selection/impact) with no-op fallback |

## C.Z Numeric spec quick reference (Patterns)

| Spec | Value | Source |
|---|---|---|
| Drag image appears after drag distance | ~3 pt | [hig:drag-and-drop] |
| Acceptable launch wait | ≤ "a couple of seconds" | [hig:launching] |
| Show progress indicator when loading exceeds | "a moment or two" | [hig:loading] |
| watchOS: indicator better than blank if load takes | 1–2 s | [hig:loading] |
| Video loading screen threshold | > 2 s → black screen + centred spinner | [hig:playing-video] |
| tvOS interactive overlay | ≥ 0.5 s delay to pause media before showing | [hig:playing-video] |
| visionOS scrub thumbnails | 160 px wide each | [hig:playing-video] |
| Aspect-fill default | 2:1 – 2.40:1 | [hig:playing-video] |
| Aspect-fit default | 4:3, 16:9, ≤2:1, and >2.40:1 | [hig:playing-video] |
| watchOS video clip length | ≤ 30 s | [hig:playing-video] |
| watchOS audio encoding | 64 kbps HE-AAC | [hig:playing-audio], [hig:playing-video] |
| Time Sensitive notification relevance | happening now or within 1 hour | [hig:managing-notifications] |
| Tip length / complexity / cadence | 1–2 sentences / ≤3 actions / e.g. once per 24 h | [hig:offering-help] |
| Tooltip length | max 60–75 characters | [hig:offering-help] |
| Rating prompt spacing / system cap | ≥ 1–2 weeks / 3 per app per 365 days | [hig:ratings-and-reviews] |
| Live content access | ≤ 1 tap (0–1 to start playback) | [hig:live-viewing-apps] |
| Haptic notification pulses | Success 2, Warning 2, Error 4 | [hig:playing-haptics] |
| Watch Digital Crown haptic detents | Series 4 and later | [hig:playing-haptics] |
| iOS full-screen exit | 1 swipe default; may require 2 | [hig:going-full-screen] |
| macOS keys: settings / undo / redo / full screen | ⌘, / ⌘Z / ⇧⌘Z / ⌃⌘F | [hig:settings], [hig:undo-and-redo], [hig:going-full-screen] |
| Undo alert title | "Undo " / "Redo " prefix + 1–2 words | [hig:undo-and-redo] |
| Collaboration popover | 3 sections; default button "Manage Shared File" | [hig:collaboration-and-sharing] |
| New document default name | "Untitled" | [hig:file-management] |
| Shared TV accounts w/o profile re-prompt | tvOS 16+ | [hig:managing-accounts] |
| Document launcher available | iOS 18 / iPadOS 18+ | [hig:file-management] |
| Share-sheet collaboration options | iOS 16, iPadOS 16, macOS 13 | [hig:collaboration-and-sharing] |

## C.Y Change log & "new" summary (one line per page)

| Page | Change log entries / new items |
|---|---|
| charting-data | Sep 23 2022 new page; WWDC25 Chart3D video linked |
| collaboration-and-sharing | Dec 5 2023 artwork (button placement, permissions); Jun 21 2023 visionOS; Sep 14 2022 new page |
| drag-and-drop | Oct 24 2023 artwork; Jun 21 2023 visionOS |
| entering-data | Jun 21 2023 visionOS |
| feedback | No change log |
| file-management | Jun 10 2024 document launcher (iOS/iPadOS 18); Jun 21 2023 visionOS |
| going-full-screen | **Jun 9 2025** hiding toolbars/nav controls + deferring Home-indicator gestures; Jun 10 2024 full-screen games |
| launching | Jun 10 2024 splash-screen guidance; Jun 21 2023 visionOS |
| live-viewing-apps | No change log |
| loading | **Jun 9 2025** downloading large assets in background; Jun 10 2024 showing progress, storing downloads, games |
| managing-accounts | No change log; WWDC25 passkeys video (account-creation API, automatic upgrades) |
| managing-notifications | No change log |
| modality | Dec 5 2023 in-depth modals + multiple modal views; Jun 21 2023 visionOS; WWDC25 "new design system" (Liquid Glass) video linked |
| multitasking | **Jun 9 2025** reorganized platform considerations + iPadOS windowed multi-window guidance (Split View/Slide Over size guidance gone); Dec 5 2023 artwork; Jun 21 2023 visionOS |
| offering-help | Dec 5 2023 visionOS tooltips; Sep 12 2023 tips (TipKit) |
| onboarding | Jun 10 2024 clarified approaches + splash screen; Jun 21 2023 visionOS |
| playing-audio | Jun 21 2023 visionOS; WWDC26 MusicKit video linked |
| playing-haptics | May 7 2024 Apple Pencil Pro; Jun 21 2023 visionOS |
| playing-video | Sep 12 2023 corrected visionOS thumbnail width; Jun 21 2023 visionOS; WWDC25 visionOS 26 immersive video formats |
| printing | No change log |
| ratings-and-reviews | Sep 12 2023 artwork |
| searching | **Jun 8 2026** updated terminology + refined best practices; **Jun 9 2025** merged Search-fields guidance, reorganized systemwide search; WWDC26 "Design intuitive search experiences" video |
| settings | Jun 10 2024 reorganized topics + game examples |
| undo-and-redo | No change log |
| workouts | No change log; WWDC25 HealthKit-on-iOS workouts video |


# 3. Components

# D. Components (1/2): Content · Layout and organization · Menus and actions

Source: Apple HIG corpus, Oct 2026. The Components collection [hig:components] has 8 groups: Content, Layout and organization, Menus and actions, Navigation and search, Presentation, Selection and input, Status, System experiences. This file covers the first 3, in HIG order. Collection pages read: `components`, `content`, `layout-and-organization`, `menus-and-actions`. Items marked "(x-ref)" come from pages the assigned pages point to: button order from [hig:alerts], shortcuts from [hig:keyboards].

## 0. Top-line takeaways

1. **One primary, never destructive.**
   - Use 1–2 prominent buttons per view.
   - Show preference by style, not size.
   - The primary button responds to Return.
   - A destructive button never gets the primary role [hig:buttons].
2. **One canonical home for every command.** On macOS, every toolbar and context-menu command must also be in the menu bar. Context menus and toolbars are shortcuts only [hig:the-menu-bar, hig:toolbars, hig:context-menus].
   - **[XPLAT]** Windows, Linux and web have no global menu bar. The parent system needs one command registry, rendered as an in-window menu or a command palette.
3. **Toolbar = title + navigation + actions.** Navigation bars were folded into toolbars in June 2025.
   - Use at most 3 groups.
   - Put 1 prominent primary action on the trailing edge.
   - Back and Close are symbols only [hig:toolbars].
4. **Menus.**
   - Title case, no articles.
   - Add "…" when the item needs more input.
   - Submenus: 1 level, about 5 items or fewer.
   - Context menus: about 3 groups or fewer; **hide** unavailable items (regular menus **dim** them); destructive items last, in red [hig:menus, hig:context-menus].
5. **Split view is the desktop/tablet backbone.**
   - Sidebar → content → detail/inspector.
   - Keep the selection highlighted persistently.
   - Use 1 pt resizable dividers.
   - Panes are hideable, with several ways to restore them [hig:split-views].

---

## 1. Content

### 1.1 Charts [hig:charts]
**Purpose:** highlight a few key insights in a dataset. Design-level guidance lives in [hig:charting-data].

**Anatomy:**
- *Marks* represent values and sit in the *plot area*.
- A *scale* maps a value to position, color or height.
- *Axes* carry *ticks* and *grid lines*.
- Labels, accessibility labels, titles, subtitles, annotations and a *legend* describe non-positional encodings.

**Marks**
- **Bar:** compare categories or parts of a whole. Over time, use for summed values, such as steps per day.
- **Line:** trend and rate of change.
- **Point:** individual values, correlations and outliers.
- Combine marks when it adds clarity (points on a line).

**Axes**
- Use a **fixed** range when the bounds are meaningful (battery 0–100%). Use a **dynamic** range when values vary widely (Health Steps).
- Bars usually start at 0. A zero baseline can hide meaningful differences, such as heart rate.
- Use familiar tick sequences: 0/5/10, not 1/6/11.
- Use fewer grid lines and lighter labels when the chart is interactive.

**Descriptions**
- Titles and labels explain the chart before people read the data.
- **Summarize the main message** in the title or subtitle (Weather: rain in the next hour). **[AI]** Every generated chart gets a plain-language headline.

**Best practices**
- The data is the most prominent element.
- In compact layouts, maximize plot width: short Y labels, units in the title, long category labels inside the plot.
- Make every chart accessible with VoiceOver and **Audio Graphs** (tones plus a summary).
- **Never require interaction to reveal critical info**. Stocks' scrubbing only adds detail. **[AI]**
- Small marks: make the whole plot area the scrub target.
- Keyboard and Switch Control:
  - Define a logical path, such as along the X axis.
  - Or let people move focus between subsets of a large dataset.
- **Make changes noticeable:** animate them, and also post accessibility notifications for VoiceOver and Reduce Motion users. **[AI]** This matters for streaming or live data.
- Align the chart's leading edge with surrounding content. Trailing-side grid labels or a trailing Y axis keep that edge clean.

**Color**
- Never rely on color alone. Add shapes or patterns (Health: circle vs. diamond).
- Put gaps between adjacent color segments.

**Accessibility labels**
- If you don't use Audio Graphs, give an overview: chart type, axis meanings, bounds.
- A chart often needs a label per important element. Decide between labelling each mark (Health bars) and summarizing groups (Maps elevation). A chart inside a button needs one summary label.
- Writing rules:
  - Give context, then the value.
  - **No subjective words** ("rapidly", "almost"). **[AI]**
  - Write "June 6", not "6/6", and "60 minutes", not "60m".
  - Describe meaning, not colors.
  - Mention axes in a consistent order.
- Hide visible axis and tick text from assistive technology.

**Platforms:** watchOS should be glanceable, with no complex interaction; put detail on the companion platform. No other considerations. **New:** a WWDC25 Chart3D resource is linked. **Change log:** 2022-09-23 new.

### 1.2 Image views [hig:image-views]
**Purpose:** display one image or an animated sequence; not interactive.
- For a clickable image, use a button that shows the image (macOS: *image button*).
- For icons, prefer SF Symbols or template icons, which accept accent colors.
- Formats include PNG, JPEG and PDF.
- Text over an image needs contrast: add a shadow or a background layer.
- Keep animation frames the same size and prescale them.
- **macOS:** an editable image is an *image well* (copy, paste, drag, Delete).
- **tvOS:** layered images.
- **visionOS:** 2D, stereoscopic and spatial photos.
- **watchOS:** use SwiftUI animation.
- **Change log:** 2023-06-21 visionOS.

### 1.3 Text views [hig:text-views]
**Purpose:** multiline, styled, scrollable text, optionally editable.
- Use a text view for long, editable or formatted text. Use a label for short static text and a text field for short input.
- Support Dynamic Type and Bold Text.
- **Make useful text selectable** (errors, serial numbers, IPs). **[AI]** Model output, errors, request IDs and code must be copyable.
- **iOS/iPadOS:** show the keyboard type that matches the content.
- **tvOS:** display only.
- **Change log:** 2023-06-05.

### 1.4 Web views [hig:web-views]
**Purpose:** embedded web content (Mail's HTML).
- When people may visit several pages, enable back/forward and show controls for them.
- **Don't build a browser.**
- **Not supported on tvOS or watchOS.**
- **[AI]** Fine for rendering generated HTML artifacts. Hand open-ended browsing to the system browser.

---

## 2. Layout and organization

### 2.1 Boxes [hig:boxes]
**Purpose:** a bordered or filled group with an optional title.
- Keep boxes small relative to the container.
- Use padding, not nested boxes, for subgroups.
- Titles are brief, in sentence case, with no punctuation; in settings panes, end with a colon.
- iOS uses secondary/tertiary backgrounds; macOS puts the title above.
- **Not supported on tvOS or watchOS.**

### 2.2 Collections [hig:collections]
**Purpose:** a visual, ordered set of items, ideal for images.
- Use the standard row or grid layout.
- Use a table for text.
- Pad items so hover and focus effects stay visible.
- Default gestures: tap selects, hold edits, swipe scrolls.
- Animate insert, delete and reorder.
- **iOS:** don't relayout while people interact with it.
- **Not supported on watchOS.**

### 2.3 Column views [hig:column-views]
**Purpose:** navigate a deep hierarchy in columns (Finder). Parent items show a triangle.
- Use when people move between levels often and don't need sorting.
- The root goes in column 1.
- A leaf shows a preview and metadata.
- Columns are resizable.
- **macOS only.** iPadOS and visionOS use a split view.

### 2.4 Disclosure controls [hig:disclosure-controls]
**Purpose:** progressive disclosure. Common controls stay visible; advanced ones are hidden by default.
- **Triangle** (for a view or list): points **inward from the leading edge when collapsed, down when expanded**. Label it descriptively ("Advanced Options").
- **Disclosure button** (for one control, like the Save sheet): points **down when collapsed, up when expanded**. Place it next to its content. **Max 1 per view.**
- iOS, iPadOS and visionOS use `DisclosureGroup`. **Not supported on tvOS or watchOS.**
- **[AI]** Use for "Show reasoning", "Tool calls (3)" and "Sources", collapsed by default.
- **[XPLAT]** Web and Material accordions use a down/up chevron, which matches the disclosure *button*. Define tree vs. accordion semantics explicitly.

### 2.5 Labels [hig:labels]
**Purpose:** static, non-editable text that people can often copy.
- Prefer system fonts and support Dynamic Type.
- Make useful text selectable.
- Use 4 system emphasis colors:

| System color | Example usage | iOS, iPadOS, tvOS, visionOS | macOS |
|---|---|---|---|
| Label | Primary information | label | labelColor |
| Secondary label | A subheading or supplemental text | secondaryLabel | secondaryLabelColor |
| Tertiary label | Text that describes an unavailable item or behavior | tertiaryLabel | tertiaryLabelColor |
| Quaternary label | Watermark text | quaternaryLabel | quaternaryLabelColor |

- watchOS has self-updating, auto-fitting date and timer text, suited to complications.
- **[XPLAT]** Define 4 text-emphasis tokens and map them explicitly to the fewer tiers Material and Fluent use.
- **Change log:** 2023-06-05.

### 2.6 Lists and tables [hig:lists-and-tables]
**Purpose:** rows in one or more columns, possibly grouped or hierarchical. They support select, add, delete and reorder. Used for navigation (iOS Settings) and for a split view's middle pane (Mail).

**Best practices**
- Prefer lists and tables for **text**. Use a collection for images or items of very different sizes.
- Allow editing; reordering alone is valued. **iOS/iPadOS need edit mode before people can select items.**
- Selection feedback:
  - **Navigation rows:** highlight persistently.
  - **Option rows:** brief highlight, then a checkmark.

**Content**
- Keep item text short. For long content, list titles and show the content in a detail view.
- For narrow or resizable tables, consider **middle truncation**, which keeps the start and end. **[AI]** Use it for conversation and file titles.
- Column headings: noun phrases in **title case**, no punctuation. Without a heading, give context with a label.

**Style**
- Match the list style to the platform:
  - iOS **grouped** (headers, footers, spacing).
  - watchOS **elliptical**.
  - macOS **bordered** with alternating rows.
- Use built-in row layouts (`UIListContentConfiguration`).

**Platforms**
- **iOS/iPadOS/visionOS:**
  - The info button (*detail disclosure*) shows details only.
  - To drill down, use the **disclosure indicator** (chevron).
  - **No alphabetical index** when rows have trailing accessories, because they get mis-hit.
- **macOS:**
  - Click a header to sort; click again to reverse.
  - Columns are resizable.
  - Consider alternating rows in wide tables.
  - Use an outline view for hierarchies.
- **tvOS:** focused rows scale up and round their corners. Don't pre-mask images.
- **watchOS:**
  - Limit rows and add "view more".
  - Keep detail views short so vertical paging between them works.
- **[XPLAT]** Stripes are a macOS idiom; Fluent, Material and web use dividers plus hover. Click-to-sort is universal.
- **Change log:** 2023-06-21, 2023-06-05.

### 2.7 Lockups [hig:lockups] (tvOS only)
**Purpose:** a focusable unit made of content, a header and a footer.
- **Cards:** ratings and reviews.
- **Caption buttons:** tilt with the swipe direction.
- **Monograms:** circular photo plus name, with initials as fallback. Prefer images.
- **Posters:** the title shows on focus.
- Leave space for focus growth and keep sizes consistent within a row.
- **[XPLAT]** The monogram fallback is a good model for a universal avatar.

### 2.8 Outline views [hig:outline-views] (macOS only)
**Purpose:** a hierarchical table, like Finder list view. Often the leading pane of a split view.
- If the data isn't hierarchical, use a table.
- Show the **hierarchy in column 1 only**.
- Headings: title case, **no trailing colon**. Required when there are several columns.
- Header-click sorts each level separately; clicking again reverses.
- Columns are resizable.
- **Option-click expands all descendants.**
- **Persist expansion state.**
- Consider alternating rows.
- Single-click edits a cell; double-click may open the item.
- Use **centered-ellipsis** truncation.
- For long outlines, put a search field in the toolbar.

### 2.9 Split views [hig:split-views]
**Purpose:** adjacent panes showing hierarchy levels: primary (sidebar) → secondary (list) → optional tertiary (detail). Can also hold tool panes around a canvas (Keynote: navigator, notes, inspector).

**Universal**
- **Persistently highlight the selection in every pane that leads to the detail.**
- Support dragging between panes.

**Per platform**
- **iOS (2025):** use only in **regular** width, not compact.
- **iPadOS:**
  - 2 panes (Mail) or 3 (Keynote).
  - Design for **narrow, compact and intermediate** widths, with logical navigation as panes collapse.
  - 2025 UIKit adds interactive column resizing and inspector columns.
- **macOS:**
  - Split vertically, horizontally or both.
  - Dividers are draggable.
  - **Set min/max pane sizes** so a divider never disappears.
  - Allow **hiding panes**.
  - Provide **multiple ways to reveal hidden panes**: toolbar button, menu item and shortcut.
  - **Thin divider = 1 pt** (preferred). Use a thicker divider only when strong row lines sit on both sides.
- **tvOS:**
  - Use for filtering.
  - Default ratio **1/3 : 2/3**, or 1/2 : 1/2.
  - **One title above the whole split view**: centered over a collection, or above the primary pane for a single main view.
- **visionOS:** prefer a split view over a new window; use a sheet for small tasks.
- **watchOS:**
  - The list or the detail shows full screen.
  - Auto-show the most relevant detail.
  - Show multiple details as a vertical tab view (Digital Crown, page indicator).

**[AI]** Chat layout: conversations → transcript → inspector (sources, artifacts, agent run). Persist pane visibility and widths. In compact width, collapse to a navigation stack.
**[XPLAT]** Fluent NavigationView and Material's list-detail layout are equivalents. Use one breakpoint-driven pane model.
**Change log:** **2025-06-09 iOS/iPadOS**, 2023-12-05 visionOS, 2023-06-05 watchOS.

### 2.10 Tab views [hig:tab-views] (macOS, watchOS)
**Purpose:** mutually exclusive panes switched by a tab control on the top edge.
- Tabs hold related content. A pane's controls affect only that pane.
- Labels: nouns, in **title case**.
- **Don't use a pop-up button to switch tabs**: 1 click vs. 2, and tabs show every option. A pop-up is acceptable only when there are too many panes.
- **Max 6 tabs.** The text says "more than six" in one place and "six or more" in another; treat 6 as the ceiling.
- The control can be hidden for programmatic switching. The content area is then borderless, bezeled or line-bordered.
- **Inset the tab view with window margins.** Edge-to-edge is unusual.
- **iOS/iPadOS:** use a segmented control. **watchOS:** page controls. Not supported on tvOS or visionOS.
- **[XPLAT]** Material and Fluent tabs use sentence case and allow scrolling strips with more than 6 tabs. Pick one casing rule for all chrome.

---

## 3. Menus and actions

### 3.1 Activity views (share sheet) [hig:activity-views]
**Purpose:** a sheet or popover of share and action tasks, opened from the **Share button**. App actions list before system actions; people can edit the list.
- Don't duplicate system actions. If an action is similar, give it a distinct title ("Print Transaction").
- Icon: SF Symbol, or a custom icon **centered in about 70×70 px**.
- Title: a verb phrase with **no company or product name**.
- You can exclude irrelevant system tasks but **can't reorder** them.
- Use only the Share button as the entry point.

**Share and action extensions**
- Use the system compose view.
- Keep to a few steps.
- **No modals on top of an extension** except alerts.
- **Long tasks:**
  - Continue in the background.
  - Show status in the main app.
  - **Don't notify on completion**, only on problems. **[AI]** Apply this to background agent tasks.
- macOS has extensions only, no activity view. **Not supported on macOS, tvOS or watchOS.**
- **[XPLAT]** Share glyphs and targets differ: Web Share API, Android Sharesheet, Windows Share. Use the native glyph for each.

### 3.2 Buttons [hig:buttons]
**Purpose:** start an instantaneous action. Three attributes: **Style** (size, color, shape), **Content** (symbol and/or text), **Role** (semantics that can change appearance).

**Basics**
- **Hit region ≥ 44×44 pt. visionOS ≥ 60×60 pt.**
- Leave visible spacing around buttons.
- **Custom buttons need a press state.**

**Style**
- Use a prominent (accent-filled) style for the **most likely action**.
- **Keep 1–2 prominent buttons per view.**
- **Use style, not size, to mark preference.** Equal sizes signal a set.
- (Liquid Glass) Don't color labels like a colorful content layer. Default to monochrome.

**Content**
- State the purpose with a symbol, text or both.
- macOS and visionOS show a hover **tooltip**.
- Use familiar icons for familiar actions (`square.and.arrow.up` = share).
- Text: verb-first, **title case** ("Add to Cart").

**Roles**

| Role | Meaning | Appearance / behavior |
|---|---|---|
| Normal | No specific meaning | Standard |
| Primary | Default; most likely choice | Accent color; Return activates; Return also closes sheets/alerts/editable views |
| Cancel | Cancels current action | Standard |
| Destructive | May destroy data | System red |

- **Never give the primary role to a destructive button**, even if it's the most likely choice.

**Button order (x-ref [hig:alerts])**
- Default/likely button goes **trailing in a row**, or at the **top of a stack**.
- **Cancel goes leading**, or at the bottom of a stack.
- Always title it "Cancel". **Never make Cancel the default.**
- A lone default button is "Done", not "Cancel".
- Make no button the default when people must read the content.
- Use destructive styling only when the result **wasn't the person's deliberate intent**: Empty Trash's confirmation is not red.
- Esc and Cmd-. also cancel.

**Platforms**
- **iOS/iPadOS:** for slow actions, show an **activity indicator inside the button**, optionally with a new label ("Checkout" → "Checking out…"). **[AI]** Use for Send → "Sending…" and Generate → "Generating…".
- **macOS:**
  - **Push button** (standard):
    - Can be the default and can be tinted.
    - Use flexible-height only for 2-line text or tall icons.
    - **Add a trailing "…" when it opens a window, view or app that needs more input.**
    - Consider spring loading.
  - **Square (gradient) button:** a symbol-only button that acts on a view, such as +/− rows. Place it in or under the view, **never in the toolbar or window frame**. No introductory label.
  - **Help button:** the round "?" button. Use the system one and open the topic for the current context. **Max 1 per window.** Never in a toolbar. No introductory text.

  | View style | Help button location |
  |---|---|
  | Dialog with dismissal buttons (like OK and Cancel) | Lower corner, opposite to the dismissal buttons and vertically aligned with them |
  | Dialog without dismissal buttons | Lower-left or lower-right corner |
  | Settings window or pane | Lower-left or lower-right corner |

  - **Image button:** in a view only. **About 10 px padding** to the button edge; usually no border; any label goes below.
- **visionOS:**
  - Buttons have a visible background and play sounds (no haptics).
  - Shapes: icon-only → **circle**; text → **rounded rectangle or capsule**; icon + text → **capsule**.
  - 4 states, plus a gaze tooltip. **No custom hover effects.**

  | Shape | Mini (28 pt) | Small (32 pt) | Regular (44 pt) | Large (52 pt) | Extra large (64 pt) |
  |---|---|---|---|---|---|
  | Circular | ✓ | ✓ | ✓ | ✓ | ✓ |
  | Capsule (text only) |  | ✓ | ✓ | ✓ |  |
  | Capsule (text and icon) |  |  | ✓ | ✓ |  |
  | Rounded rectangle |  | ✓ | ✓ | ✓ |  |

  - Use a visible fill, except in toolbars, menus, alerts and ornaments. Over a window, use the **thin** material; floating, use **glass**.
  - **A white fill with black content is reserved for the toggled-on state.**
  - Prefer circles and capsules; a standalone button is a capsule.
  - **Centers ≥ 60 pt apart.** Buttons ≥ 60 pt get **4 pt** padding.
  - Avoid rows of mini or small buttons.
  - Text buttons: rounded rectangles in vertical stacks, capsules in rows.
- **watchOS:**
  - Inline buttons are capsules on a material.
  - Corner buttons go in the toolbar, which gets Liquid Glass.
  - Primary actions use **full-width** buttons.
  - Paired or stacked buttons have equal heights.

**[XPLAT]**
- **Order:** Apple and Material put the primary button trailing. Windows dialogs put it first ([OK][Cancel], right-aligned). Choose trailing-primary globally or adapt only on native Windows. Mirror in RTL.
- **Target size:**
  - Apple: 44 pt (visionOS 60).
  - Material: 48 dp.
  - WCAG 2.2: AA 24 px, AAA 44 px.
  - Use 44 as the parent default and 48 dp on Android.
- **Casing:** Apple uses title case; Material and Fluent use sentence case.
- **Destructive:** Apple uses red, never as the default; Material uses the error color.

**Change log:**
- **2025-12-16:** Liquid Glass.
- **2025-06-09:** styles and content (Style/Content/Role framing).
- 2024-02-02, 2023-12-05, 2023-06-21: visionOS.
- 2023-06-05: watchOS.

### 3.3 Context menus [hig:context-menus]
**Purpose:** a hidden menu of item-specific commands. Opened by hold or pinch-hold (iOS, iPadOS, visionOS), or by Control-click or secondary click (macOS, iPadOS).
- Include **only the most relevant, frequent commands**, never advanced ones.
- **Keep the item count small.**
- Support context menus everywhere, consistently.
- **Every item must also exist in the main UI**: the toolbar on iOS, the menu bar on macOS.
- **Submenus: 1 level max**, with predictive titles.
- **Hide unavailable items; don't dim them.** Exception: macOS Cut, Copy and Paste.
- **Put frequent items nearest the pointer or finger.** Reverse the order when the menu opens above.
- **No keyboard shortcuts in context menus.**
- Use separators, with **about 3 groups or fewer**.
- **Destructive items (iOS, iPadOS, visionOS) go last and red.**
- Add a title only to clarify scope ("3 Messages").
- Use standard icons for Copy, Share and Delete.

**Platforms**
- **iOS/iPadOS:**
  - An item has a context menu **or** an edit menu, never both.
  - iPadOS: a context menu on empty space can create objects (New Folder).
  - Previews: show a condensed preview of the target, with a clipping path that matches its shape so it animates cleanly.
- **macOS:** called a "contextual menu".
- **visionOS:** prefer a context menu over panels for frequent functions. **Max height ≈ window height**, so window controls stay visible.
- **Not supported on watchOS.**

**[AI]** Message menu: Copy, Regenerate, Edit, Share, separator, Delete (red, last). Mirror these as hover actions.
**[XPLAT]** Windows and web (Office, Docs, VS Code) show shortcuts and dimmed items in context menus; Apple doesn't. On the web, also offer a visible "…" trigger.
**Change log:** 2023-12-05 hide unavailable items; 2023-06-21; 2022-09-14.

### 3.4 Dock menus [hig:dock-menus] (macOS only)
**Purpose:** secondary-click the Dock icon for system items plus custom items.
- Custom items must also exist elsewhere.
- Add a few high-value items for when the app isn't frontmost (Mail: Get New Mail, New Message, open windows).
- Avoid dynamic items.
- **[AI]** New Chat, New Window, recent chats. Windows Jump Lists and Android shortcuts are the analogues.

### 3.5 Edit menus [hig:edit-menus]
**Purpose:** commands on a selection (Cut, Copy, Paste, Translate, Look Up), plus data-detected actions on iOS and visionOS.

**Forms by platform**
- iOS: a horizontal bar on hold or double-tap; a chevron expands it into a context menu.
- iPadOS: horizontal for touch, vertical for pointer or keyboard.
- macOS: the context menu plus menu-bar Edit.
- visionOS: a bar or a context menu.
- Not available on tvOS or watchOS.

**Rules**
- **Use the system menu** with the standard gestures.
- Show only relevant items: no Copy or Cut without a selection, no Paste with an empty clipboard.
- Put custom items **after related system items**, and not too many.
- Allow copying non-editable *content* text, but not control labels.
- **Support Undo and Redo**, since menu actions don't ask for confirmation. **[AI]** Prefer undo over confirmation for reversible edits.
- Don't duplicate edit commands with other controls.
- Distinguish Delete from Cut.
- **iOS:** support both styles. You can move the menu, but not reshape it.

**Change log:** 2023-06-21; 2022-09-14.

### 3.6 Home Screen quick actions [hig:home-screen-quick-actions] (iOS/iPadOS)
**Purpose:** app actions on icon long-press. Each has a title, an icon and an optional subtitle, and can be dynamic.
- Expect at least 1; **maximum 4**.
- Changes must be predictable.
- Titles state the result ("New Message"). No app name. Plan for localization.
- Use SF Symbols or the template. **No emoji**, because icons are monochrome and adapt to Dark Mode.
- **[AI]** New Chat, Voice Mode. Android app shortcuts are the analogue.

### 3.7 Menus [hig:menus]
**Purpose:** a space-efficient list of commands, options or states. These rules apply to all menu types.

**Labels**
- Use a verb or verb phrase for actions.
- **Title case:** capitalize everything except articles, coordinating conjunctions and short prepositions; always capitalize the last word.
- **Drop articles.**
- **Dim** unavailable items. Keep a menu openable even when all its items are disabled.
- **Add "…" when the item needs more input.**
- Apps show shortcuts; games rarely do.

**Icons (2025–26)**
- Use standard icons for common actions.
- **Use icons sparingly**: key actions, locations, devices, visual concepts, user content. **No icon if none fits.** The anti-pattern is arbitrary icons on days of the week.
- **Within a group, give icons to every item or none.**

**Organization**
- **Put frequent items first.**
- Group related items with **separators**, even when their importance differs (Paste and Match Style stays with Paste).
- Split or submenu long menus. Exception: user or dynamic lists (History, Bookmarks) may scroll.

**Submenus**
- Marked with a chevron.
- Use sparingly. Create one when **a term repeats in more than 2 items** ("Sort by" ▸ Date, Score, Time).
- **1 level only.**
- **About 5 items or fewer**; beyond that, make a new menu.
- Always openable.
- **Never use indentation instead.**

**Toggled items**
- Changeable label: Show Map ↔ Hide Map.
- Add a verb if it's ambiguous ("Turn HDR On").
- Show both items when helpful.
- Use a **checkmark** for an active attribute.
- Offer a "clear all" item (Plain).

**Games:** use the platform's default input and scale menus for small screens.

**Platforms**
- **iOS/iPadOS** `preferredElementSize`:
  - **Small:** a top row of **4 icon-only** items. Use only for tight sets (B/I/U/S).
  - **Medium:** a top row of **3 icon + label** items (Notes: Scan, Lock, Pin).
  - **Large (default):** a plain list.
- **visionOS:**
  - Small or large layouts.
  - Can extend outside the window.
  - Show the menu near its content.
  - Breakthrough over 3D content: `automatic` = **subtle** (preferred); **prominent** can cause discomfort; **none** lets content occlude the menu.

**[AI]** Model and mode pickers use checkmarks. Toggles such as Show/Hide Sidebar use changeable labels.
**[XPLAT]** Material and Fluent use sentence case. The "…" convention and dimming are shared with Windows.
**Change log:**
- **2026-06-08:** icon guidance.
- **2025-12-16:** breakthrough.
- **2025-07-28:** icons.
- 2024-06-10: games.
- 2023-06-21.
- 2022-09-14: layouts.

### 3.8 Ornaments [hig:ornaments] (visionOS only)
**Purpose:** controls on a plane just in front of a window. They move with the window, don't scroll with it, and can sit on any edge. System toolbars and tab bars are ornaments.
- Use for frequent controls in a stable place (Music Now Playing).
- **Keep them visible**; hide only during immersive viewing.
- Limit how many there are, for visual balance.
- **Width ≤ the window's.**
- Use **borderless buttons**, which get the gaze hover effect.
- Use system toolbars and tab bars where possible.
- **Change log:** 2024-02-02; 2023-12-05; 2023-06-21 new.

### 3.9 Pop-up buttons [hig:pop-up-buttons]
**Purpose:** a menu of **mutually exclusive options**. The button shows the current selection.
- Use for flat, exclusive choices. Use a pull-down for actions, multi-select or submenus.
- **Provide a useful default.**
- Make the options predictable with a label.
- Saves space.
- An optional "Custom…" item can add explanatory text.
- **iPadOS:** in popovers and modals, use a pop-up instead of drilling into a detail view.
- **Not supported on tvOS or watchOS.**
- **[AI]** The **model picker** is a pop-up button with a sensible default.
- **[XPLAT]** Equivalents: Material exposed dropdown, Fluent ComboBox, HTML `<select>`.

### 3.10 Pull-down buttons [hig:pull-down-buttons]
**Purpose:** a menu of **actions related to the button** (Add ▸ type, Sort ▸ attribute, Back ▸ history).
- **Don't hide all of a view's actions** in one pull-down.
- **At least 3 items**; use plain buttons or toggles for 1–2. Avoid very long lists.
- Title only if it adds meaning.
- **Destructive items are red and need confirmation**: an action sheet on iOS, a popover on iPadOS. **[AI]** Use for "Delete conversation" and "Clear memory".
- Icons go *after* the label.
- **iOS:** a pull-down can open from a gesture (hold on Safari Tabs). A **More (…)** button trades discoverability for space.
- **Not supported on tvOS or watchOS.**
- **[XPLAT]** Overflow glyph: Apple "…" (often circled), Material ⋮ kebab, Windows "…".

### 3.11 The menu bar [hig:the-menu-bar]
**Purpose (macOS, iPadOS):** top-of-screen menus. They are how people discover what an app does, its commands and its shortcuts. iPadOS follows macOS.

**Fixed order:** *AppName* · File · Edit · Format · View · *app-specific* · Window · Help. macOS adds the Apple menu on the leading edge and extras on the trailing edge.

**Rules**
- Keep the system menus in their standard order.
- **Always show the same items; disable rather than hide** (the opposite of context menus).
- Use system icons.
- **Support the standard shortcuts**; add custom ones only when necessary.
- **Use one-word titles**, in title case if longer.

**App menu.** The name shows in bold. About goes first and alone.

| Menu item | Action | Guidance |
|---|---|---|
| About *AppName* | About window (copyright, version) | Name **≤ 16 characters**; no version number |
| Settings… | App settings (iPadOS: app's page in Settings) | App-level only; document settings → File |
| Optional app-specific items | App configuration | After Settings, same group |
| Services (macOS only) | Contextual services submenu | |
| Hide *AppName* (macOS only) | Hide app, activate last-used app | Same short name |
| Hide Others (macOS only) | Hide other apps | |
| Show All (macOS only) | Show other apps | |
| Quit *AppName* | Quit; **Option → Quit and Keep Windows** | Same short name |

**File menu.** Rename or remove it if the app has no files.

| Menu item | Action | Guidance |
|---|---|---|
| New *Item* | New doc/file/window | Name the type (Calendar: Event, Calendar) |
| Open | Open selection or chooser | "…" if chooser |
| Open Recent | Recent docs + Clear Menu | Names not paths; most recent first |
| Close | **Option → Close All**; Close Tab replaces it in tabbed windows | Add Close Window for tabbed windows |
| Close Tab | **Option → Close Other Tabs** | |
| Close File | File + all its windows | Multi-view files |
| Save | Save | Autosave; name/location prompt for new docs; format pop-up in Save sheet |
| Save All | Save all | |
| Duplicate | **Option → Save As** | Prefer over Save As/Export/Copy To/Save To |
| Rename… / Move To… | Rename / relocate | |
| Export As… | Name, location, format; original stays open | Only for non-native formats |
| Revert To | Versions submenu + browser | |
| Page Setup… | Doc-specific print parameters | Global/frequent → Print panel |
| Print… | Print panel (print, fax, PDF) | |

**Edit menu.** Useful even without documents. Find may belong in File instead when it searches objects or files.

| Menu item | Action / standard submenu items | Guidance |
|---|---|---|
| Undo | Reverse last operation | Name target: "Undo Typing", "Undo Paste and Match Style" |
| Redo | Reverse last Undo | Name target |
| Cut / Copy / Paste | Clipboard ops (Paste repeatable) | |
| Paste and Match Style | Paste, match surrounding style | |
| Delete | Remove without Clipboard | "Delete", never Erase/Clear |
| Select All | | |
| Find ▸ | Find, Find and Replace, Find Next, Find Previous, Use Selection for Find, Jump to Selection | |
| Spelling and Grammar ▸ | Show Spelling and Grammar, Check Document Now, Check Spelling While Typing, Check Grammar With Spelling, Correct Spelling Automatically | |
| Substitutions ▸ | Show Substitutions, Smart Copy/Paste, Smart Quotes, Smart Dashes, Smart Links, Data Detectors, Text Replacement | |
| Transformations ▸ | Make Uppercase, Make Lowercase, Capitalize | |
| Speech ▸ | Start Speaking, Stop Speaking | |
| Start Dictation | Dictation | System-added at bottom |
| Emoji & Symbols | Character Viewer | System-added at bottom |

**Format menu.** Omit it if there's no rich text.

| Menu item | Submenu items |
|---|---|
| Font | Show Fonts, Bold, Italic, Underline, Bigger, Smaller, Show Colors, Copy Style, Paste Style |
| Text | Align Left, Align Center, Justify, Align Right, Writing Direction, Show Ruler, Copy Ruler, Paste Ruler |

**View menu.** Appearance of all windows; no window navigation.
- **Always provide it**, even if it only holds Enter/Exit Full Screen.
- Show/Hide labels reflect the current state.

| Menu item | Action |
|---|---|
| Show/Hide Tab Bar | Toggle tab bar |
| Show All Tabs / Exit Tab Overview | Tab overview |
| Show/Hide Toolbar | Toggle toolbar |
| Customize Toolbar | Toolbar customization |
| Show/Hide Sidebar | Toggle sidebar |
| Enter/Exit Full Screen | Full screen in new space |

**App-specific menus** go between View and Window (Safari: History, Bookmarks).
- **List every custom command**, even if it's available elsewhere. This gives discoverability, shortcuts and Full Keyboard Access.
- Mirror the object hierarchy (Mail: Mailbox → Message → Format).
- Order from general to specialized.

**Window menu.** Navigate and manage windows, but not customize or close them.
- **Always provide it**, even for one window.
- Include Minimize and Zoom for Full Keyboard Access.
- Panel toggles are optional.

| Menu item | Action | Guidance |
|---|---|---|
| Minimize | **Option → Minimize All** | |
| Zoom | Content-fit ↔ user size; **Option → Zoom All** | Not for full screen |
| Show Previous Tab / Show Next Tab | | |
| Move Tab to New Window | | |
| Merge All Windows | Into one tabbed window | |
| Enter/Exit Full Screen | | Only if no View menu |
| Bring All to Front | **Option → Arrange in Front** | |
| *Open window names* | Bring to front | **Alphabetical**; no panels/modals |

**Help menu.** Trailing end. The Help Book format adds automatic search.

| Menu item | Action | Guidance |
|---|---|---|
| Send *AppName* Feedback to Apple | Feedback Assistant | |
| *AppName* Help | Help Viewer | |
| *Additional items* | Release notes, registration | Separator first; keep total small |

**Dynamic items** (a modifier reveals an alternate)
- Never the only path to a task.
- Menu bar only, not context or Dock menus.
- **One modifier key.**
- Menu width fits the widest alternate.

**Standard shortcuts (x-ref [hig:keyboards]).** The Windows/Linux column is common convention, not HIG. **[XPLAT]**

| Item | macOS | Windows/Linux convention |
|---|---|---|
| Settings… | ⌘, | Ctrl+, (Electron/VS Code); classic: Tools > Options |
| Hide / Hide Others | ⌘H / ⌥⌘H | n/a |
| Quit | ⌘Q | Alt+F4 (Win) / Ctrl+Q (Linux) |
| New / Open / Save / Print | ⌘N / ⌘O / ⌘S / ⌘P | Ctrl+N / O / S / P |
| Duplicate / Save As | ⇧⌘S | Ctrl+Shift+S |
| Page Setup | ⇧⌘P | (Ctrl+Shift+P = command palette in many apps) |
| Close / Close File / Close All | ⌘W / ⇧⌘W / ⌥⌘W | Ctrl+W / Ctrl+F4 |
| Undo / Redo | ⌘Z / ⇧⌘Z | Ctrl+Z / Ctrl+Y (or Ctrl+Shift+Z) |
| Cut / Copy / Paste | ⌘X / ⌘C / ⌘V | Ctrl+X / C / V |
| Paste and Match Style | ⌥⇧⌘V | Ctrl+Shift+V |
| Select All | ⌘A | Ctrl+A |
| Find / Next / Previous / Use Selection | ⌘F / ⌘G / ⇧⌘G / ⌘E | Ctrl+F / F3 / Shift+F3 |
| Bold / Italic / Underline | ⌘B / ⌘I / ⌘U | Ctrl+B / I / U |
| Show Fonts / Show Colors | ⌘T / ⇧⌘C | n/a |
| Show/Hide Toolbar | ⌥⌘T | varies |
| Enter Full Screen | ⌃⌘F | F11 |
| Minimize / Minimize All | ⌘M / ⌥⌘M | Win+Down |
| Next / previous window | ⌘` / ⇧⌘` | Alt+Tab-style |
| Help | ⌘? | F1 |
| Cancel | Esc, ⌘. | Esc |

**iPadOS** (new 2025-06-09)
- The bar is hidden until people point to or swipe from the top edge.
- **Every function must also be reachable in the UI.** Dynamic items need a keyboard. Don't use the bar as a catch-all.
- Settings opens the app's page in iPadOS Settings; put in-app preferences in an item beneath it.
- Consider listing tabs in the View menu with key bindings.
- Use submenus more often, because rows are taller.

| | iPadOS | macOS |
|---|---|---|
| Menu bar visibility | Hidden until revealed | Visible by default |
| Horizontal alignment | Centered | Leading side |
| Menu bar extras | Not available | System default and custom |
| Window controls | In the menu bar when the app is full screen | Never in the menu bar |
| Apple menu | Not available | Always available |
| App menu | About, Services, and app visibility-related items not available | Always available |

**macOS**
- The Apple menu is fixed.
- Under space pressure, the system tightens or truncates titles and hides extras. The bar hides in full screen.
- **Menu bar extras:**
  - A symbol or template icon. **Bar height = 24 pt.**
  - Clicking shows **a menu, not a popover**, unless the content is too complex.
  - **The user opts in** (in Settings or during setup).
  - Never rely on the extra being visible. Mirror its functions in the Dock menu.
- **Not supported on iOS, tvOS, visionOS or watchOS.**

**[AI]** Suggested menus:
- File: New Chat ⌘N, Export Conversation As…
- View: Show/Hide Sidebar and Inspector.
- A "Conversation" menu: Regenerate, Stop, Branch.
- A "Model" menu.
- An opt-in quick-prompt extra. A popover needs the "too complex" justification.

**[XPLAT]**
- Windows and Linux use an in-window menu: About under Help, Exit under File, Settings under File or Tools, no App menu. It's often hidden behind ☰ or "…".
- The web has none.
- Define one **command model** (id, label, shortcut, enablement) rendered as: macOS menu bar; Windows/Linux in-window menu; web/mobile command palette plus overflow.

### 3.12 Toolbars [hig:toolbars]
**Purpose:** frequent commands, controls, navigation and search in logical groups along the **top or bottom** edge. Content: **title**, **navigation** (back/forward, search), **actions** (buttons, menus). Tab bars are separate; they switch app areas.

**Navigation bars are now part of toolbars.**
- The 2025-06-09 change log says "incorporated navigation bar guidance".
- iOS calls a navigation toolbar "sometimes" a navigation bar.
- The corpus has no separate page for it.

**Best practices**
- **Avoid overcrowding.** Plan which items overflow as width shrinks.
- **macOS and iPadOS add the overflow menu automatically. Never add one manually**, and avoid layouts that overflow by default.
- Add a More menu for low-priority items, only if needed.
- **Allow customization on iPadOS and macOS** for pro or long-session apps.
- **(Liquid Glass) Minimize custom bar backgrounds and tints.**
  - Let the content set the tone.
  - Use `ScrollEdgeEffectStyle` for separation.
  - Use monochrome labels over colorful content.
- Use standard components; custom ones must keep **corner radii concentric** with the bar.
- Hiding the toolbar for focus is fine with a reliable way to restore it.

**Titles**
- Give each window a useful title, or none if redundant.
- **Never the app name.**
- **Under 15 characters.**

**Navigation**
- **Standard Back and Close as symbols, with no "Back" or "Close" text.** A symbol + "Back" capsule is shown as incorrect.
- Custom versions must match in look and behavior.

**Actions**
- Prioritize the main tasks.
- Controls must be self-explanatory. **Prefer symbols**; use text for things like Edit.
- **Use borderless system symbols**; the section is the container.
- **Use `.prominent` for Done or Submit, with exactly 1 primary on the trailing side.** **[AI]** Send is the prominent trailing action.

**Item groupings**

| Region | Contents | Behavior |
|---|---|---|
| Leading edge | Back, sidebar toggle, title, optional document menu (Duplicate, Rename, Move, Export) | Not customizable; always present |
| Center | Common controls; title if not leading | Customizable (macOS/iPadOS); collapses to system overflow |
| Trailing edge | Persistent important items, inspector toggles, optional search, More menu (hosts customization), primary action | Visible at all widths |

- Group by function and frequency.
- Give **navigation and critical actions (Done, Close, Save) their own distinct sections**. Back and forward are leading, tools are trailing; don't lump them together.
- **Keep the same groupings on every platform.**
- **Use at most 3 groups.**
- **Separate text-labelled actions with fixed space** so labels don't merge.

**Platforms**
- **iOS:**
  - Only essentials in the bar; the rest in More.
  - A **large title** collapses on scroll and returns at the top.
- **iPadOS:** a toolbar and a tab bar can share the top row.
- **macOS:**
  - The toolbar sits in the window frame, below or merged with the title bar, with an inline title. **Items have no bezel.**
  - **Every toolbar item must also be a menu-bar command.**
- **visionOS:**
  - The toolbar is at the **bottom** of the window, on a forward plane with variable blur. Gaze on a symbol reveals its label.
  - Use the system toolbar. **No vertical toolbars**, since tab bars are vertical there.
  - **The window must not shrink below the toolbar's width**, because there's no menu bar.
  - Use contextual controls in modal states and restore them afterward.
  - **No pull-downs**, because they cover window controls.
- **watchOS:**
  - Buttons go in the top corners or along the bottom.
  - The scrolling `primaryAction` is revealed by scrolling up. Use it for an important action that isn't the view's main purpose.

**[XPLAT]**
- Android: top and bottom app bars or a FAB. Windows: CommandBar.
- **Apple bans the app name as the in-view title.** Windows and web conventionally show "Doc – App" in the title bar or `<title>`.
- The parent system should keep the app name in the OS title or tab only.

**Change log:**
- **2025-12-16:** Liquid Glass.
- **2025-06-09:** groupings, symbols, **nav-bar merge**.
- 2023-06-21.
- 2023-06-05.

---

## 4. Change-log digest (2025–26 entries in bold)

| Page | Entries |
|---|---|
| charts | 2022-09-23 new (WWDC25 Chart3D linked) |
| image-views / text-views / labels | 2023-06-21 visionOS / 2023-06-05 watchOS 10 / 2023-06-05 |
| web-views, boxes, collections, column-views, disclosure-controls, outline-views, lockups, activity-views, dock-menus, home-screen-quick-actions | none |
| lists-and-tables | 2023-06-21; 2023-06-05 |
| split-views | **2025-06-09 iOS/iPadOS**; 2023-12-05 visionOS; 2023-06-05 watchOS |
| tab-views | 2023-06-05 watchOS |
| buttons | **2025-12-16 Liquid Glass; 2025-06-09 styles & content**; 2024-02-02; 2023-12-05; 2023-06-21; 2023-06-05 |
| context-menus | 2023-12-05 hide unavailable; 2023-06-21; 2022-09-14 |
| edit-menus | 2023-06-21; 2022-09-14 |
| menus | **2026-06-08 icons; 2025-12-16 breakthrough; 2025-07-28 icons**; 2024-06-10; 2023-06-21; 2022-09-14 |
| ornaments | 2024-02-02; 2023-12-05; 2023-06-21 new |
| pop-up-buttons | 2023-10-24 artwork; 2022-09-14 |
| pull-down-buttons | 2022-09-14 |
| the-menu-bar | **2025-06-09 iPadOS menu bar** |
| toolbars | **2025-12-16 Liquid Glass; 2025-06-09 groupings, symbols, nav-bar merge**; 2023-06-21; 2023-06-05 |

## 5. Platform support matrix

| Component | iOS | iPadOS | macOS | tvOS | visionOS | watchOS |
|---|---|---|---|---|---|---|
| Web views | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ |
| Boxes | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ |
| Collections | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ |
| Column views | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ |
| Disclosure controls | ✓ (SwiftUI) | ✓ (SwiftUI) | ✓ | ✗ | ✓ (SwiftUI) | ✗ |
| Lockups | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ |
| Outline views | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ |
| Tab views | ✗ (segmented control) | ✗ | ✓ | ✗ | ✗ | ✓ (page controls) |
| Activity views | ✓ | ✓ | ✗ (extensions only) | ✗ | ✓ | ✗ |
| Context menus | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ |
| Dock menus | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ |
| Edit menus | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ |
| Home Screen quick actions | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ |
| Ornaments | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ |
| Pop-up / pull-down buttons | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ |
| Menu bar | ✗ | ✓ | ✓ | ✗ | ✗ | ✗ |

## 6. Numeric spec digest

| Spec | Value | Source |
|---|---|---|
| Min button hit region | 44×44 pt (visionOS 60×60 pt) | buttons |
| Prominent buttons per view | 1–2 | buttons |
| visionOS button sizes | 28 / 32 / 44 / 52 / 64 pt | buttons |
| visionOS button spacing | centers ≥ 60 pt apart; +4 pt padding if button ≥ 60 pt | buttons |
| macOS image-button padding | ~10 px | buttons |
| Help buttons per window | ≤ 1 | buttons |
| Disclosure buttons per view | ≤ 1 | disclosure-controls |
| Custom activity icon area | ~70×70 px | activity-views |
| Context-menu groups | ≤ ~3 | context-menus |
| Submenus | 1 level; > ~5 items → new menu; create when term repeats > 2× | menus |
| iOS menu small / medium top row | 4 icons / 3 icon+label | menus |
| Pull-down min items | 3 | pull-down-buttons |
| Tabs per tab view | ≤ 6 | tab-views |
| Home Screen quick actions | ≤ 4 | home-screen-quick-actions |
| Toolbar title | < 15 characters | toolbars |
| Toolbar groups / primaries | ≤ 3 / exactly 1, trailing | toolbars |
| macOS menu bar height | 24 pt | the-menu-bar |
| App short name (About/Hide/Quit) | ≤ 16 characters | the-menu-bar |
| Split-view thin divider | 1 pt | split-views |
| tvOS split ratio | 1/3 : 2/3 (or 1/2 : 1/2) | split-views |


# E1 — HIG Components, part 2: Navigation and search · Presentation · Selection and input · Status

Source: Apple HIG corpus (Oct 2026). Read in full: collection pages `navigation-and-search`, `presentation`, `selection-and-input`, `status` and the 32 component pages below. Grouping follows the HIG exactly. Tags: **[AI]** = relevant to an AI product. **[XPLAT]** = differs from Material / Windows / web, or the parent system must choose a rule; details are in the §5 table. **[NEW]** = 2025–2026 (Liquid Glass era) guidance. "Leading/trailing" = left/right in LTR; mirror in RTL.

## 0. Platform support matrix

Y = supported; – = "Not supported" per the page.

| Component | iOS | iPadOS | macOS | tvOS | visionOS | watchOS |
|---|---|---|---|---|---|---|
| Path controls | – | – | Y | – | – | – |
| Search fields | Y | Y | Y | Y | Y | Y |
| Sidebars | Y | Y | Y | Y | Y | – |
| Tab bars | Y | Y | Y | Y | Y | – |
| Token fields | – | – | Y | – | – | – |
| Action sheets | Y | Y | Y | Y | – | Y |
| Alerts | Y | Y | Y | Y | Y | Y |
| Page controls | Y | Y | – | Y | Y (display only) | Y |
| Panels | – | – | Y | – | – | – |
| Popovers | Y | Y | Y | – | Y | – |
| Scroll views | Y | Y | Y | Y | Y | Y |
| Sheets | Y | Y | Y | Y | Y | Y |
| Windows | – | Y | Y | – | Y | – |
| Color wells | Y | Y | Y | – | Y | – |
| Combo boxes | – | – | Y | – | – | – |
| Digit entry views | – | – | – | Y | – | – |
| Image wells | – | – | Y | – | – | – |
| Pickers | Y | Y | Y | Y | Y | Y |
| Segmented controls | Y | Y | Y | Y | Y | – |
| Sliders | Y | Y | Y | – | Y | Y |
| Steppers | Y | Y | Y | – | Y | – |
| Text fields | Y | Y | Y | Y | Y | Y |
| Toggles | Y | Y | Y | Y | Y | Y |
| Virtual keyboards | Y | Y | – | Y | Y | Y |
| Activity rings | Y | Y | – | – | – | Y |
| Gauges | Y | Y | Y | – | Y | Y |
| Progress indicators | Y | Y | Y | Y | Y | Y |
| Rating indicators | – | – | Y | – | – | – |

---

## 1. Navigation and search `[hig:navigation-and-search]`

### 1.1 Path controls `[hig:path-controls]` — macOS only
**Purpose:** shows the file-system path of a selected item (Finder path bar).
- **Standard style:** root, parents and item in a row, each with icon and name. Middle names collapse when space is short. If editable, drop an item to set the path.
- **Pop-up style:** shows the item; clicking opens a menu of the path. If editable, the menu adds **Choose…** and accepts drops.
- Put it in the window **body**, never the toolbar or status bar.
- **[XPLAT]** Same idea as a breadcrumb. **[AI]** Shows an agent's working directory.

### 1.2 Search fields `[hig:search-fields]`
**Purpose:** a text field with Search icon, Clear button and placeholder, plus an optional scope bar and tokens.
- Placeholder states what's searchable.
- Search as people type when possible.
- Suggest recent searches before typing and predictions while typing.
- Most relevant results first, grouped by category. Add a scope bar to filter results.
- **Scope bar:** filters among clearly defined categories. Default to the **broadest** scope.
- **Tokens:** selectable, editable terms that filter other terms (a Mail contact, Messages photos). Pair them with suggestions so people discover them.
- **[AI]** Tokens are the model for scoping prompts ("in: Drive", "@repo"). For LLM search that can't run per keystroke, show suggestions instantly.

**iOS — three entry points [NEW]** (updated June 2025; terminology June 2026)
- **Search tab, standard style:** looks like other tabs and opens a search landing page. Use it for discovery and exploration (the Apple TV app's categories).
- **Search tab, button appearance:** a separate button at the trailing end. It focuses the field and raises the keyboard immediately, and exiting returns to the previous tab. Use it for quick lookup.
- **Toolbar:** bottom (expanded field or button) or top (button). Either animates into a field above the keyboard. **Prefer the bottom when there's room** (Settings, Mail, Notes). Use the top when bottom content must stay visible (Wallet) or there's no bottom toolbar.
- **Inline:** when sitting next to the content clarifies scope (Music library filter). Put it above the list it filters and consider pinning it on scroll.

**iPadOS + macOS** (keep them consistent)
- Default: field at the **trailing end of the toolbar**, especially in split views (Mail, Notes) or when filtering the detail view (Freeform).
- Search at the top of the sidebar when it filters sidebar navigation (Settings).
- Search as a sidebar item or tab for a dedicated discovery area (Music, TV).
- Auto-focus the field in a dedicated area. Exception: iPad with only a virtual keyboard.
- The field resizes with the window. In compact iPad widths, move it above the content-list column.

**Other platforms:** tvOS uses a keyboard screen with results below; offer popular, contextual and recent suggestions. On watchOS the field opens full-screen input that returns on Cancel or Search. visionOS: no extra guidance.
**[XPLAT]** iOS favors bottom search; Material, Windows and web put it at the top.

### 1.3 Sidebars `[hig:sidebars]`
**Purpose:** navigation on the leading side among app areas or collections. It needs a lot of space; when space is tight, use a tab bar or a tab bar that converts to a sidebar.
- **[NEW]** Sidebars float in the Liquid Glass layer (iOS, iPadOS, macOS). Extend content beneath them by horizontal scrolling or the **background extension effect** (mirrors and blurs adjacent content under the sidebar).
- Let people customize items and their order.
- Group large hierarchies with disclosure controls.
- Use SF Symbols or custom symbols, not bitmaps.
- Let people hide it: iPad edge swipe; on macOS a button plus View ▸ Show/Hide Sidebar. visionOS rarely needs this. **Don't hide it by default.**
- **Show ≤2 hierarchy levels.** For deeper data, add a content-list column (split view).
- Keep group titles succinct.
- **[NEW, 2026]** Icons use the app accent color, but on macOS they must follow the **user's system accent color**. Fixed colors only when meaningful (Mail's yellow VIP). **[XPLAT]** Brand purple gives way to the macOS accent.

**Platforms**
- iOS/iPadOS: `sidebarAdaptable` lets the app open as a sidebar or a tab bar, with a button to switch. It adapts to rotation and width. For a sidebar only, use a split view. **Consider a tab bar first.**
- macOS: row height, text and glyph size follow the sidebar size (small, medium or large), set by the app or in General settings. Auto-collapse when the window narrows. Nothing critical at the sidebar bottom.
- visionOS: put a sidebar *inside* a tab for deep hierarchies. Sidebar selections never switch tabs.
- tvOS: no extra guidance. watchOS: not supported.

### 1.4 Tab bars `[hig:tab-bars]`
**Purpose:** navigation among top-level sections, each keeping its own state.
- **Navigation only, never actions** (actions belong in a toolbar).
- Always visible. Only a modal may cover it.
- Use as few tabs as needed. For complex information architecture, use a sidebar or adaptive tab bar. No hard maximum is given (iPad default ≤5, below).
- **Avoid overflow.** The trailing tab turns into **More** (iOS/iPadOS) and hides content.
- **Never disable or hide tabs.** Explain empty sections instead. **[AI]** An empty Agents tab gets an empty state, not a disabled tab.
- Always label tabs, ideally one word each. Use SF Symbols, preferably filled. Compact: icon above label. Regular: icon beside label.
- Badges are a red oval with a white number or "!", only for critical information.
- Keep tab label color distinct from the content beneath. Over colorful content, use a monochrome tab bar.

**Platforms**
- **iOS [NEW]:** floats at the bottom on Liquid Glass. With an accessory (Music's MiniPlayer) it can **minimize on scroll**, with the accessory moving inline; tap a tab or scroll to the top to restore. Optional trailing search tab.
- **iPadOS:** near the top of the screen. Fixed (`tabBarOnly`) or convertible to a sidebar (`sidebarAdaptable`). Prefer the tab bar. Let people customize tabs, with a **default of ≤5** for continuity between compact and regular sizes.
- **macOS:** no extra guidance.
- **tvOS:** customizable background, fonts, tints and icons. Translucent, with only the selected tab opaque (shadowed when focused). Overflow fades at the edges. It scrolls away for single-view tabs and stays pinned for split views; Menu returns focus to it. Live-TV apps order tabs Live, then DVR, then other.
- **visionOS:** vertical, fixed to the window's leading side. It expands on gaze to show labels. Supply a symbol and a short label per tab.
- **watchOS:** not supported.

| tvOS tab bar spec | Value |
|---|---|
| Height | 68 pt (fixed) |
| Top edge offset from screen top | 46 pt (fixed) |

**[XPLAT]** Apple's tab placement differs by device. Material uses a bottom bar (3–5 destinations), a rail, or a drawer. iOS's More overflow has no Material equivalent.

#### Tab bar ↔ sidebar adaptivity (synthesized from `[hig:tab-bars]`, `[hig:sidebars]`, `[hig:search-fields]`)

| Context | Primary navigation | Adaptivity / notes |
|---|---|---|
| iPhone portrait | Bottom floating tab bar | Icon above label; overflow → More; optional trailing search tab; minimize-on-scroll with accessory |
| iPhone landscape | Bottom tab bar | Icon beside label |
| iPad regular | Top tab bar; optionally convertible to sidebar (`sidebarAdaptable`) | Switch button; user-customizable tabs, default ≤5; sidebar-only = split view |
| iPad compact / narrow window | Tab bar | Search moves above content-list column; auto-adapts on resize/rotation |
| Mac | Sidebar in split view (tab bar also supported) | Auto-collapse on narrow window; S/M/L size from system setting; icons follow system accent |
| visionOS | Vertical tab bar, leading edge | Expands on gaze; sidebar inside a tab for depth; sidebar never switches tabs |
| tvOS | Top tab bar, 68 pt high, 46 pt from top | Scrolls away unless split view; Menu returns focus |
| watchOS | None | Vertical tab views paged with Digital Crown |

### 1.5 Token fields `[hig:token-fields]` — macOS only
**Purpose:** a text field that turns typed text into tokens that can be selected, dragged and reordered (Mail recipients). Shows suggestions as people type.
- Give each token a context menu (edit, VIP, contact card).
- Comma creates a token by default. Consider adding Return.
- Tune the suggestion delay; the immediate default can distract.
- **[AI]** The model for composer mention chips (@agent, @file). **[XPLAT]** One Chip-Input component across iOS tokens, Material input chips and web tag inputs.

---

## 2. Presentation `[hig:presentation]`

#### Choosing a presentation (synthesized)

| Need | Use | Avoid |
|---|---|---|
| Unexpected critical problem; confirm uncommon irreversible destructive action | Alert | Popover (missable) |
| Clarifying choices for an action the person just initiated | Action sheet / confirmation dialog | Alert; menu |
| Scoped task tied to current context | Sheet (one at a time) | Sheet-on-sheet |
| Small transient info/controls anchored to a control (wide layouts) | Popover | Popover in compact width (→ sheet) |
| Repeated input while observing results; inspector (macOS) | Panel / split-view inspector | Sheet |
| Complex, long or multistep task | iOS full-screen modal; macOS new window/full screen; visionOS Full Space | Sheet |

### 2.1 Action sheets `[hig:action-sheets]`
**Purpose:** modal choices for an action the person initiated (`confirmationDialog`).
- Use an action sheet, not an alert, for **intentional** actions (Mail: Delete Draft or Save Draft). Alerts are for the unexpected.
- Use sparingly. One-line title. Message only if needed.
- **Cancel at the bottom** (top-left on watchOS) when data could be lost. SwiftUI adds it by default.
- **Destructive buttons:** destructive style, **at the top**.
- iOS/iPadOS: an action sheet, not a menu, for clarifying choices. **Never scroll.**
- watchOS: **≤4 buttons including Cancel.** visionOS: not supported.

| Style (watchOS) | Meaning |
|---|---|
| Default | No special meaning |
| Destructive | Destroys user data or performs a destructive action |
| Cancel | Dismisses the view without taking any action |

**[XPLAT]** Material has no action sheet (use a bottom-sheet list). Android Back must dismiss. **[AI]** "Discard generated draft?"

### 2.2 Alerts `[hig:alerts]`
**Purpose:** critical information needed immediately: problems, data-loss warnings, confirming important actions or purchases.

**When**
- Rarely. Each alert needs essential information and useful actions.
- Never just to inform. Use an in-context indicator.
- **No alert for common, undoable actions, even destructive ones.** **Do alert for uncommon, irreversible destructive actions.**
- **Never at launch.** Show cached data plus an unobtrusive label instead.
- **[AI]** Alert only before irreversible, uncommon agent actions (sending, deleting, paying). Offer undo for reversible ones. Show outages inline.

**Content**
- Title, optional message, **≤3 buttons**. A text field is available on iOS, iPadOS, macOS and visionOS. Icon and accessory view on macOS and visionOS. Suppression checkbox and Help button on macOS.
- Tone: direct, neutral, approachable. Never accusatory or downplaying.
- Title: what happened, where, why. **Never "Error" or "Error 329347 occurred".** **≤2 lines.** A sentence gets sentence case and a period; a fragment gets title case and no punctuation.
- Add a message only if it adds value. Don't explain the buttons (if you must, use "choose" plus the exact title).
- Add a text field only when input resolves the situation (a password).

**Buttons**
- 1–2 word verbs ("View All", "Reply"). Title case, no punctuation.
- **"OK" only in purely informational alerts. Never Yes/No. Always "Cancel" for cancelling.**
- **Default / most likely button trailing in a row or top of a stack. Cancel leading in a row or bottom of a stack.**
- Use the destructive style **only for destructive actions the person didn't deliberately choose**. A confirmation of a chosen Empty Trash stays default style, so Return confirms.
- Any destructive action needs Cancel. **Cancel is never the default.** Make no button the default when people must read. A lone default button is "Done".

| Action | Platform |
|---|---|
| Exit to the Home Screen | iOS, iPadOS |
| Pressing Escape (Esc) or Command-Period (.) on an attached keyboard | iOS, iPadOS, macOS, visionOS |
| Pressing Menu on the remote | tvOS |

**Platforms**
- iOS/iPadOS: avoid scrolling alerts (large text can cause it).
- macOS: shows the app icon automatically. Offers suppression for repeating alerts, accessory views and a Help button. Use `exclamationmark.triangle` only for possible unexpected data loss, not routine save or empty-trash.
- visionOS: Shared Space alerts sit in front of the window, slightly forward, and stay anchored if it moves. Full Space alerts are centered in view.
- tvOS, watchOS: no extra guidance.

| visionOS alert accessory view | Value |
|---|---|
| Maximum height | 154 pt |
| Corner radius | 16 pt |

**[XPLAT]** Button order differs from Windows. Destructive red styling and Yes/No labels differ from common web, Material and Windows practice. Esc works everywhere; Cmd-. is Apple-only.

### 2.3 Page controls `[hig:page-controls]`
**Purpose:** a row of indicators for pages in a **flat, ordered** list. The current page is solid; dots are equidistant and clipped on overflow.
- Only for sequential pages, never hierarchy.
- Center horizontally near the bottom.
- **About 10 dots at most.** Beyond that, use a grid.
- Custom images: **≤2 indicator types** (a default plus one special page, like Weather's `location.fill`). Keep shapes simple: no text or inner lines. **Don't color them.**
- iOS/iPadOS: edge dots shrink on overflow. Tap either side of the current dot to go back or forward; iPad pointers can target a dot. Scrub to move sequentially; past an edge jumps to first or last. **Animate taps only, not scrubbing.**
- Background styles. **Automatic:** shown while interacting; use when not the primary navigation. **Prominent:** always shown; only when it is the primary navigation. **Minimal:** never shown; **no scrubbing**.
- tvOS: full-screen peer pages. visionOS: non-interactive. watchOS: at the bottom or beside the Digital Crown; prefer vertical paging and one-screen pages. macOS: not supported.

### 2.4 Panels `[hig:panels]` — macOS only
**Purpose:** a floating window with supplementary controls for the active window or selection. **HUD** = dark, translucent variant. Other platforms use a modal view.
- Use for quick controls and **inspectors** (update with the selection). Fixed-content Info windows are regular windows. An inspector can also be a split-view pane.
- Prefer sliders and steppers over typing.
- Title bar with a short noun title in title case ("Inspector").
- Show all panels when the app is active; hide them all when it's inactive.
- Not listed in the Window menu's document list. No minimize button.
- Menus say "Show Fonts", never "panel".
- **HUD:** only in media apps, when a standard panel would hide content, or when no controls are needed. Keep the style when leaving full screen. Minimal color. **Small**, never covering what it adjusts.
- **[AI]** An inspector for agent runs, tool calls and sources. **[XPLAT]** Elsewhere, implement it as a docked trailing pane.

### 2.5 Popovers `[hig:popovers]`
**Purpose:** a transient view above content, revealed from a control.
- Hold a small amount of content: a few related tasks.
- Arrow points at the source. Don't cover the source or content people need.
- Close, Cancel or Done only when it adds clarity. Otherwise dismiss on an outside tap or on selection. Multi-select stays open.
- **Save work when a nonmodal popover auto-closes.** Discard only on explicit Cancel.
- **One at a time.** Never cascade. Only an alert may appear on top.
- One tap or click closes one popover and opens the next.
- Size to fit the content and animate size changes.
- Never use one for warnings (use an alert). Don't say "popover" in help.
- iOS/iPadOS: **none in compact width**; use a sheet.
- macOS: can be **detachable**, becoming a panel with nearly the same look.
- tvOS, watchOS: not supported.
- **[AI]** Citation previews, model details. Autosave on dismiss. **[XPLAT]** Material has no arrowed popover.

### 2.6 Scroll views `[hig:scroll-views]`
**Purpose:** scroll content larger than its bounds. Translucent indicators show position.
- Support system gestures and keyboard shortcuts. Custom scrolling keeps the elastic feel.
- Show that content scrolls (partial content at edges).
- **Never nest same-axis scroll views.** Cross-axis nesting is fine.
- Paging: a page is the view size **minus an overlap unit** (a line or row).
- Auto-scroll **only as far as needed**: to a hidden search match, an offscreen insertion point when typing starts, a drag-selection past the edge, or a scrolled-away selection before acting on it.
- Set minimum and maximum zoom.
- **[AI]** For streaming output (derived), follow it only while the reader is at the bottom. Never pull them back after they scroll up.

**Scroll edge effects [NEW]** (iOS, iPadOS, macOS; July 2025, updated June 2026)
- Separate floating bars from content scrolling beneath. Styles: **automatic** (default), **hard** (opaque blur with an edge), **soft** (variable-blur fade).
- **Prefer automatic.** It adds stronger separation for busy top toolbars, text outside Liquid Glass and pinned table headers. Test soft for legibility.
- **Only behind floating UI.** Not decoration, not an overlay.
- **One per view.** In split views, each pane gets one with matching heights.
- **[XPLAT]** No Material or Windows equivalent; on the web use `backdrop-filter` plus a mask.

**Platforms**
- iOS/iPadOS: in paged mode, use a page control and hide the scroll indicator on that axis.
- macOS: "scroll bar". Small or mini bars in tight panels, matching the panel's other controls.
- tvOS: no indicators; focus drives scrolling.
- visionOS: small, fixed-size indicator (thicker than iOS), centered on the trailing edge (vertical) or bottom edge (horizontal). Look plus drag gives a **jog bar** that controls speed. Widen tight margins. **Look to Scroll [NEW, March 2026]** scrolls by gaze near the edges and is opt-in per view. Use it for reading and browsing views, not dense, control-heavy or secondary ones, and apply it consistently. Scroll areas should be full-bleed or clearly bounded. Remove parallax first.
- watchOS: vertical scrolling with the Digital Crown. Page with vertical tab views and keep pages one screen tall.

### 2.7 Sheets `[hig:sheets]`
**Purpose:** a scoped task closely tied to the current context.
- **Modal** on macOS, tvOS, visionOS and watchOS. iOS/iPadOS also allow **nonmodal** sheets (Notes' format sheet).
- **Cancel/Close** dismisses without saving. **Done** dismisses after finishing or saving. **Back** goes to the previous step and never dismisses.
- For long or complex flows, use something else: a full-screen modal (iOS), a new window or full screen (macOS), a Full Space (visionOS).
- **One sheet at a time.** Close the first before opening the next.
- Nonmodal supplementary content: split view (visionOS), panel (macOS), nonmodal sheet (iOS).
- **Never Done alone** (pair it with Cancel or Back). **Never Cancel, Done and Back together.**

**iOS / iPadOS button placement [NEW, March 2026]**

| Sheet / step | Leading (top toolbar) | Trailing (top toolbar) |
|---|---|---|
| Single-view sheet | Cancel | Done (when present) |
| Multi-step: first step | Cancel | Done (inactive) |
| Multi-step: subsequent step | Back | Done (inactive) |
| Multi-step: final step | Back | Done |

**Detents** (a resizable sheet expands when content scrolls or the grabber is dragged)

| Detent | Height | Behavior |
|---|---|---|
| Large | Fully expanded sheet | Supported automatically |
| Medium | About half of the fully expanded height | Add to rest at both heights; medium only = cannot expand to full |
| Custom | App-defined | One or more allowed |

- iPhone: support **medium** for progressive disclosure (share sheet). Skip it when content needs full height (compose).
- Resizable sheets show a **grabber**: drag to resize, tap to cycle detents; VoiceOver-accessible.
- **Swipe down to dismiss.** If there are unsaved changes, confirm with an action sheet.
- iPadOS: prefer the **page** or **form** styles (centered, dimmed backdrop).
- macOS: a card over the dimmed parent window. Sensible default size; resizable when useful. Other app windows stay usable. Use a panel for repeated input with visible results (find and replace).
- visionOS: centered in the field of view, not rising from the bottom edge. Don't cover most of the window; allow resizing.
- watchOS: full-screen and translucent with a blurred backdrop. Only for custom titles or content; otherwise use an alert or action sheet. Brief, and not for navigation. Use an SF Symbol if you change the label, never a back-like label or title text.

**[XPLAT]** Android Back must step back through or close sheets. Windows has no sheet. **[AI]** Use a nonmodal sheet for generation settings while output stays visible. Confirm before a swipe discards an unsent prompt.

### 2.8 Windows `[hig:windows]`
**Purpose:** present an app's UI. On iPadOS, macOS and visionOS windows bound content and enable multitasking. iOS, tvOS, watchOS: not supported.
- A **primary** window holds main navigation and content. An **auxiliary** window holds one task, offers no navigation, and has a close button.
- Adapt fluidly to any size.
- Open new windows only when they help (Mail Compose). Offer **Open in New Window** in a context menu or the File menu.
- **No custom window frames or controls**, and no imitations of the system ones.
- Say "window", never "scene".

**iPadOS [NEW, June 2025]**
- Two modes: **Full screen** (switch windows with the app switcher) and **Windowed** (freely resizable, several onscreen, size and position remembered).
- In windowed mode, controls appear at the **leading edge of the toolbar**; inset leading toolbar items.
- Support gestures like pinch to open content in a new window. The app must support multiple windows.

**macOS**
- A **frame** (controls, toolbar, rarely a bottom bar) plus a **body**.
- Custom windows must use the system appearance for each state.
- **Nothing critical in a bottom bar** (it can sit off-screen). Use it only for brief status (Finder item count, free space); put more detail in a trailing inspector.

| macOS window state | Definition | Appearance |
|---|---|---|
| Main | The app's frontmost window; only one per app | Gray close/minimize/zoom unless also key; uses vibrancy |
| Key (active) | Accepts input; only one onscreen at a time; usually the main window, but a panel can be key | Colored close/minimize/zoom controls |
| Inactive | Not in the foreground | Gray controls; no vibrancy → subdued, appears farther away |

Panels such as Fonts become key only when people click the title bar or a text-input control. Clicking the Dock icon makes only the most recently used window key.

**visionOS**

| Style | What it is | Specs and rules |
|---|---|---|
| Window (default) | Upright plane with unmodifiable **glass** background; close button, window bar, resize controls; optional Share button, tab bar, toolbar, ornaments; dynamic scale | **Default 1280 × 720 pt**; opens **~2 m** in front of the wearer, apparent width **~3 m**; keep the glass; set min/max size; keep 3D shallow (deep content is clipped) |
| Volume | 2D/3D content viewable from any angle; close button and window bar turn to face the viewer | Fixed scale is the default (prefer dynamic unless it's a real-world object); baseplate glow (visionOS 2+); ≤1 extra ornament, never on the toolbar or tab-bar edge; baseplate parallel to floor or tilting with gaze |
| Plain | Default style without the glass background | — |

- Windows for familiar UI; volumes for bounded 3D (a game board). Pick an initial size with little empty space, shaped to content (Keynote wide, Safari tall). Use attachments to pin 2D labels to 3D content.
- **[XPLAT]** Chrome position and custom title bars differ from Windows, Linux and Electron. Windows has no main vs key state. **[AI]** "Open in New Window" suits long agent sessions.

---

## 3. Selection and input `[hig:selection-and-input]`

### 3.1 Color wells `[hig:color-wells]`
**Purpose:** shows a color and opens a picker. Prefer the **system picker** (saved colors, familiar on iOS, iPadOS and macOS). macOS: highlights while active and supports drag and drop between wells and from the picker. tvOS, watchOS: not supported.

### 3.2 Combo boxes `[hig:combo-boxes]` — macOS only
**Purpose:** a text field plus a pull-down button. Custom entries aren't added to the list.
- Prefill a meaningful default (not necessarily the first item).
- Label in title case, ending with a colon.
- Offer the likeliest choices, no wider than the field.
- **[AI]** A model picker that also accepts a custom model ID.

### 3.3 Digit entry views `[hig:digit-entry-views]` — tvOS only
**Purpose:** full-screen PIN entry with an optional title and prompt. Use **secure digit fields** (asterisks) for sensitive data, and state why digits are needed.

### 3.4 Image wells `[hig:image-wells]` — macOS only
**Purpose:** an editable image view supporting copy, paste, delete and drag-in. Revert to the default image when cleared if one is required. Support the Edit menu's Copy and Paste. **[AI]** An attachment drop target.

### 3.5 Pickers `[hig:pickers]`
**Purpose:** scrollable lists of distinct values; the order is locale-dependent.
- Use for **medium-to-long** lists. Short lists → pull-down button. Huge lists → list or table.
- Order values predictably (alphabetical).
- Show in context (below the field, at the bottom of the window, or in a popover). Don't switch views.
- Minutes: **60 values (0–59) by default.** An interval must divide 60 (15 → 0, 15, 30, 45).

| iOS/iPadOS date picker style | Behavior |
|---|---|
| Compact | Button showing value in accent color → modal calendar + time editor; tap outside to confirm |
| Inline | Time only: button revealing wheels. Dates / date+time: inline calendar |
| Wheels | Scrolling wheels; also accept keyboard entry |
| Automatic | System picks by platform and mode |

| Date picker mode | Values |
|---|---|
| Date | Months, days of the month, years |
| Time | Hours, minutes, optional AM/PM |
| Date and time | Dates, hours, minutes, optional AM/PM |
| Countdown timer | Hours and minutes, **max 23 h 59 min**; not available in inline or compact |

- iOS: compact when space is tight. macOS: **textual** (exact entry, tight space) or **graphical** (browse a calendar, date ranges, clock face). tvOS: SwiftUI Picker. watchOS: Digital Crown with wheels; long lists use `navigationLink` (a button opening the list, and the Crown scrubs). **[AI]** Schedule agent runs in 15-minute steps.

### 3.6 Segmented controls `[hig:segmented-controls]`
**Purpose:** ≥2 equal-width segments, each a button, containing text or images. Single choice; macOS also allows multiple choice and **momentary** action segments (Mail Reply / Reply All / Forward).
- Use for closely related choices affecting an object, state or view, especially when grouping or selection state matters.
- **Never mix action and selection segments.**
- **About 5–7 segments at most in wide layouts; about 5 on iPhone.**
- Equal widths and similar content sizes. Text **or** images, never both. Nouns in title case.
- iOS/iPadOS: switch related subviews (Event / Reminder). Separate app sections → tab bar.
- macOS: labels or **a tooltip per segment** for icon segments. Use a tab view for main-window view switching; segmented controls suit toolbars and inspectors. Support spring loading.
- tvOS: use a split view for filtering. Focus selects a segment, so keep other focusable items away.
- visionOS: icon segments show a tooltip on gaze. watchOS: not supported.
- **[AI]** Good for a Chat / Agent mode switch, not for model lists.

### 3.7 Sliders `[hig:sliders]`
**Purpose:** a track and thumb between min and max; the track fills from min to the thumb. Optional end icons.
- Customize only for meaning (small and large image icons).
- **Min leading, max trailing. Vertical: min at bottom.**
- For wide ranges, pair with a **text field** and **stepper**.
- iOS/iPadOS: **never for volume**; use the system volume view.
- macOS: optional tick marks. Lozenge thumb (linear) or small circular thumb (circular). Give **live feedback**. Linear for fixed ranges (0–100 %); circular for repeating values (0–360°; 4 spins = 1440°). Label in sentence case ending with a colon. Label the min and max ticks, or periodic ticks for nonlinear scales. Show a hover **tooltip with the value**.
- visionOS: prefer horizontal. watchOS: discrete or continuous, with +/− side buttons that step a fixed amount. tvOS: not supported.
- **[AI]** For temperature: slider plus numeric field, with labeled endpoints.

### 3.8 Steppers `[hig:steppers]`
**Purpose:** a +/− control next to a field that shows the value.
- Make the affected value obvious.
- Pair with a text field when large changes are likely.
- macOS: **Shift-click for bigger steps (e.g., 10×).**
- watchOS, tvOS: not supported.

### 3.9 Text fields `[hig:text-fields]`
**Purpose:** **small**, specific text (a name or email). Use a text view for more.
- Use placeholders as hints, **plus a separate label** (placeholders disappear when typing starts).
- **Secure fields** for sensitive data.
- Size the field to the expected text.
- Space fields evenly, stack them vertically, and keep group widths consistent.
- Keep tab order logical.
- **Validation timing:** email when leaving the field; username or password before leaving it.
- Use a number formatter for numbers, percent and currency, and stay locale-aware.
- Overflow: clip (default), wrap, or truncate with an ellipsis at start, middle or end. Show an **expansion tooltip** on hover.
- iOS, iPadOS, tvOS, visionOS: use the matching keyboard type. tvOS and watchOS: minimize typing.
- iOS/iPadOS: **Clear button at the trailing end**. Leading end shows purpose; trailing end holds extras.
- macOS: combo box for text plus choices. watchOS: only when necessary.
- **[XPLAT]** Label models differ (Material floating label; Windows header above). **[AI]** The composer is a text view. Use secure fields for API keys.

### 3.10 Toggles `[hig:toggles]`
**Purpose:** choose between two opposing states. Styles are switch and checkbox, plus radio buttons on macOS. Buttons can also act as toggles.
- Only for two-state settings. Choosing from a list → pop-up button.
- Make clear what's being toggled.
- Show state with **fill, shape or a checkmark, never color alone.**

**iOS / iPadOS**
- **Switches only in list rows**, with no label needed.
- Default switch color is **green**. Change it to the accent only if necessary, keeping contrast with off.
- **Outside lists, use a toggle-style button** (Phone's filter button, highlighted when on), with no explanatory label.

**macOS**
- Switches, checkboxes and radios belong in the **window body**, never the toolbar or status bar.
- **Switch:** for emphasized settings or one that controls a group. Use a **mini switch** in grouped-form rows. **Don't replace existing checkboxes with switches.**
- **Checkbox:** off, on, or **mixed (dash)**, with the title trailing. Use for **hierarchies** (leading-aligned, indented). Show mixed when children differ. A group label aligns to the first checkbox's baseline.
- **Radio buttons:** groups of **2–5** mutually exclusive options. **>~5 → pop-up button.** For a single on/off, prefer a checkbox. Space a horizontal set by its longest label.

| Control | Apple use | iOS/iPadOS | macOS |
|---|---|---|---|
| Switch | Two-state setting; emphasis | List rows only; default green | Emphasized/group settings; mini switch in grouped forms |
| Toggle-style button | State on a button (filter, formatting) | Required outside lists | Allowed |
| Checkbox | On / off / mixed; hierarchy | — | Preferred for ordinary settings and hierarchies |
| Radio buttons | 2–5 mutually exclusive options | — | >~5 → pop-up button |

**[XPLAT]** Material and Windows tie switches to immediate effect and checkboxes to forms and multi-select. iOS limits switches to list rows.

### 3.11 Virtual keyboards `[hig:virtual-keyboards]`
**Purpose:** on-screen keyboards with task-specific keys and **no shortcuts**. Apps can add custom **input views** (in-app) or **keyboard extensions** (system-wide on iOS, iPadOS, tvOS).
- Match the keyboard to the content and set the semantic **content type** (better keyboards and corrections).
- Customize the Return key when it clarifies the action (e.g., Search).

| Keyboard type | Keys shown (iPhone) |
|---|---|
| ASCII capable | 26 letters, Shift, Delete, Numbers, Space, Return; suggestions; Dictation |
| ASCII capable number pad | 10 digits + Delete (2–9 show phone letters) |
| Decimal pad | 10 digits, Delete, period |
| Default | 26 letters, Shift, Delete, Numbers, Space, Return; suggestions; Emoji + Dictation |
| Email address | 26 letters, Shift, Delete, Numbers, Space, period, @, Return; suggestions; Emoji |
| Name phone pad | 26 letters, Shift, Delete, Numbers, Space, Return; suggestions; Emoji + Dictation |
| Number pad | 10 digits + Delete |
| Numbers and punctuation | 10 numbers, 15 punctuation, secondary punctuation key, Delete, Letters, Space, Return; Dictation |
| Phone pad | 10 digits, Delete, a + * # key |
| Twitter | 26 letters, Shift, Delete, Numbers, Space, @, #; Emoji + Dictation |
| URL | 26 letters, Shift, Delete, Numbers, period, slash, ".com", Return; Emoji |
| Web search | 26 letters, Shift, Delete, Numbers, Space, period, Go; Emoji + Dictation |

- **Custom input views** must make sense in context, since people can't switch back to the system keyboard. Play the standard click sound.
- **Custom keyboards** never appear in secure or phone-number fields. Make switching obvious (the Globe convention). Don't duplicate the Emoji, Globe or Dictation keys. Put tutorials in the app, not the keyboard.
- iOS/iPadOS: use the **keyboard layout guide** so fields and buttons stay visible. **[NEW, June 2025]** Controls above the keyboard must be task-relevant, use Liquid Glass to match the UI (standard toolbars get it automatically), and use standard padding.
- tvOS: linear keyboard (Siri Remote), grid (other devices), digit keyboard for PINs. visionOS: a separate, movable keyboard window; no layout changes needed. watchOS: keyboard on large screens, otherwise dictation or Scribble. You can't change the keyboard type but can set the content type. macOS: not supported.
- **[AI]** Mobile composer: "Send" return key, pinned above the keyboard, suggestion chips in the accessory row. **[XPLAT]** Map one semantic field type to each platform's keyboard API.

---

## 4. Status `[hig:status]`

### 4.1 Activity rings `[hig:activity-rings]`
**Purpose:** one person's daily Move, Exercise and Stand progress. watchOS shows 3 rings. iOS shows Move only, or 3 rings when an Apple Watch is paired.
- Show them in health and fitness contexts.
- **Only for Move, Exercise and Stand.** No other data, and no ring-like copies of these metrics.
- One person, clearly identified.
- Never change colors or opacity. **Always on a black background**, enclosed in a circle via corner radius (not a mask). No gradients or shadows. Adapt the surrounding UI, never the rings.
- **Outer margin ≥ the gap between rings.** Nothing may encroach on it.
- Keep other ring-like elements visually separate.
- No duplicate Activity notifications. Never use rings as decoration or branding.
- macOS, tvOS, visionOS: not supported.

| Ring label / value color | R | G | B |
|---|---|---|---|
| Move | 250 | 17 | 79 |
| Exercise | 166 | 255 | 0 |
| Stand | 0 | 255 | 246 |

**[AI]** Don't design concentric multicolor quota rings that look like these.

### 4.2 Gauges `[hig:gauges]`
**Purpose:** a numeric value within a range, optionally with range context.
- Circular or linear path. The **standard** style marks the value with an indicator; the **capacity** style fills to it. An **accessory** variant looks like a watch complication (Lock Screen widgets).
- Label the value and both endpoints succinctly (VoiceOver reads the visible labels).
- Use a gradient when it adds meaning (hot to cold).
- **macOS level indicators:**
  - **Capacity**, continuous: a translucent track that fills with a bar. Use for large ranges.
  - **Capacity**, discrete: equal segments, filled whole only.
  - **Rating:** see 4.4.
  - **Relevance** (rare): a shaded bar, for example in search results.
  - The default fill is **green**. Change the color at thresholds, or use the **tiered** state (red → yellow → green).
- tvOS: not supported.
- **[AI]** Use a capacity gauge with tiered colors for context-window, quota or credit usage, and a relevance bar for retrieval scores. **[XPLAT]** Maps to the web `<meter>`; Material has no gauge.

### 4.3 Progress indicators `[hig:progress-indicators]`
**Purpose:** shows the app isn't stalled. Indicators are **transient**.

| Type | Use for | Forms |
|---|---|---|
| Determinate | Known duration (file conversion) | Bar (fills leading → trailing) or circular (fills clockwise) |
| Indeterminate ("activity indicator", "spinner") | Unquantifiable work (loading, syncing) | Spinning circle on all platforms; macOS also has an indeterminate bar |

- **Prefer determinate.** It lets people decide whether to wait, switch tasks or abandon.
- **Pace progress accurately and evenly.** 90 % in 5 s followed by the last 10 % in 5 min feels deceptive.
- **Keep it moving.** If work stalls, explain why and what to do.
- Switch from indeterminate to determinate once the duration is known. **Never switch between circular and bar.**
- Descriptions must be specific. **Avoid "loading" and "authenticating".**
- Keep the indicator in a consistent location.
- **Let people stop:** Cancel when stopping is harmless; **Pause plus Cancel** when cancelling loses progress. Confirm losing progress with an alert (cancel or resume).
- iOS/iPadOS **refresh control:** a pull-down spinner. Also **refresh automatically**. Its optional title gives useful information (last updated), never instructions.
- macOS: prefer a **spinner** for background work or small spaces (inside a field, next to a button). **Don't label spinners.**
- watchOS: white by default, tint can change.
- **[AI]** Core to generation. Start indeterminate and switch to determinate steps ("Step 3 of 7") once known. Use specific status ("Searching 12 sources") instead of "Thinking…". Always show a **Stop** button, plus Pause for long runs, and confirm before discarding work. Never fake an even pace. **[XPLAT]** The same split exists on Material, Windows and the web. Pull-to-refresh is mobile-only.

### 4.4 Rating indicators `[hig:rating-indicators]` — macOS only
**Purpose:** a row of symbols (stars by default) showing a rank. Whole symbols only (values round), fixed spacing.
- Let people edit ratings **inline** in lists.
- A custom symbol must still read clearly as a rating.
- **[AI/XPLAT]** macOS-only. Cross-platform response feedback (thumbs) needs a parent component that keeps the inline rule.

---

## 5. Cross-platform decision table [XPLAT]

Apple column = this corpus. Other columns are general platform knowledge, given for contrast.

| Topic | Apple HIG | Material / Android | Windows | Web | Proposed parent rule |
|---|---|---|---|---|---|
| Primary nav (phone) | Floating bottom tab bar (iOS); overflow → More | Bottom nav bar, 3–5 destinations; no overflow | n/a | Bottom bar or hamburger | Bottom bar ≤5 labeled tabs, no More, never disabled |
| Primary nav (tablet/desktop) | iPad top tab bar ↔ sidebar; Mac sidebar; visionOS vertical tab bar | Nav rail (medium), drawer (expanded) | NavigationView left pane / top nav | Top nav or left sidebar | Sidebar/rail with same destinations; ≤2 levels, else split view |
| Search placement | iOS bottom toolbar or trailing search tab; iPad/Mac trailing toolbar | Top search bar | Title-bar search | Top header | Phone: bottom; tablet/desktop/web: trailing top toolbar |
| Dialog button order | Default/primary trailing; Cancel leading; stack: default top, Cancel bottom | Confirming trailing, dismissive leading | ContentDialog Primary→Secondary→Close (L→R); Win32 "OK, Cancel" (affirmative first) | Varies | Pick one: trailing-primary everywhere, or native order on Windows |
| Destructive styling | Only when destruction wasn't deliberately chosen; Cancel never default | Often red confirm | Not standardized | Often red | Red/destructive style for unintended or irreversible cases only |
| Button labels | Specific verbs; OK only for info; never Yes/No; "Cancel" | Specific verbs | Legacy Yes/No | Varies | Specific verbs; ban Yes/No |
| Dismiss modal | Esc / Cmd-. / swipe down (sheets) / Home | System Back, scrim tap | Esc | Esc, backdrop click | Esc everywhere; Android Back always steps back or dismisses |
| Sheet header | Cancel leading, Done trailing; Back replaces Cancel in later steps | Full-screen dialog: X leading, Save trailing | Bottom-aligned buttons | Footer buttons | Cancel leading, confirm trailing in headers |
| Popover | Arrowed, wide layouts only; sheet in compact | Menus, rich tooltips (no arrow) | Flyout, TeachingTip | Popover API | Arrowed popover ≥ regular width, else sheet |
| Switch vs checkbox | iOS: switch only in list rows, toggle button elsewhere; macOS: checkbox preferred, switch for emphasis | Switch = immediate on/off; checkbox = select in lists/forms | ToggleSwitch = immediate; CheckBox = commit later / multi | Checkbox in forms | Switch = immediate setting row; checkbox = form/multi/mixed; radio 2–5; toggle button in toolbars |
| Switch "on" color | Green default; accent allowed with contrast | Primary color | Accent | Varies | Decide brand purple vs green; contrast-check |
| Text field label | Placeholder + separate label | Floating label + helper/error text | Header above | Label above | Persistent label above; placeholder as example only |
| Window chrome | No custom chrome; traffic lights top-leading; iPad window controls leading in toolbar; main/key/inactive | n/a | Caption buttons top-trailing; custom title bars common | Browser chrome | Platform-specific chrome inset; focused/unfocused tokens; no fake traffic lights |
| Scroll separation | Scroll edge effect (automatic/hard/soft) behind floating bars | App bar color change on scroll | Mica/Acrylic | `backdrop-filter` + mask | Scroll-edge tokens for glass bars only |
| Meter vs progress | Gauge / level indicator separate from progress | Progress only | ProgressBar/Ring | `<meter>` vs `<progress>` | Separate Meter and Progress components |
| Keyboard type | `keyboardType` + `textContentType`; Return key type | `inputType` + `imeOptions` | Input scope | `inputmode`, `autocomplete`, `enterkeyhint` | One semantic field type mapped per platform |

## 6. Change logs (one line per page)

| Page | Changes |
|---|---|
| search-fields | 2026-06-08 terminology + search-as-tab (iOS) refined; 2025-06-09 iOS placement, merged iPadOS/macOS, token guidance; 2023-09-12 merged common guidance; 2023-06-05 watchOS |
| sidebars | 2026-06-08 icon colors + adaptable style clarified; 2025-06-09 content beneath sidebar; 2024-08-06 SwiftUI adaptable sidebar; 2023-12-05 iPadOS art; 2023-06-21 visionOS |
| tab-bars | 2026-06-08 terminology/art; 2025-12-16 Liquid Glass update; 2025-07-28 Liquid Glass added; 2024-09-09 iPadOS 18 art; 2024-08-06 iPadOS 18 tab bar; 2023-06-21 visionOS |
| alerts | 2024-02-02 default/Cancel button guidance; 2023-09-12 visionOS anatomy art; 2023-06-21 visionOS |
| page-controls | 2023-06-21 visionOS; 2023-06-05 watchOS |
| scroll-views | 2026-06-08 scroll edge effects updated; 2026-03-24 Look to Scroll (visionOS); 2025-07-28 scroll edge effects added; 2024-02-02 visionOS indicator art; 2023-12-05 visionOS indicator; 2023-06-05 watchOS |
| sheets | 2026-03-24 button placement; 2024-03-29 iPadOS form/page styles; 2023-12-05 visionOS split view for supplementary items; 2023-06-21 visionOS; 2023-06-05 watchOS |
| windows | 2025-06-09 best practices + iPadOS resizable windows; 2024-06-10 visionOS 2 volumes, game examples; 2023-06-21 visionOS |
| pickers | 2023-06-05 watchOS |
| segmented-controls | 2023-06-21 visionOS |
| sliders | 2023-06-21 visionOS |
| text-fields | 2023-06-05 watchOS 10 |
| toggles | 2024-03-29 macOS switches, checkbox titles, radio art; 2023-09-12 artwork |
| virtual-keyboards | 2025-06-09 controls above keyboard + watchOS keyboard; 2024-02-02 visionOS gestures; 2023-12-05 visionOS art; 2023-06-21 renamed from "Onscreen keyboards", visionOS |
| activity-rings | 2024-03-29 display guidance + ring colors; 2023-12-05 iOS art |
| gauges | 2022-09-23 new page |
| progress-indicators | 2023-09-12 merged common guidance; 2023-06-05 watchOS 10 |
| rating-indicators | 2022-09-23 new page |

No change log: path-controls, token-fields, action-sheets, panels, popovers, color-wells, combo-boxes, digit-entry-views, image-wells, steppers. The search-fields page links the WWDC 2026 video "Design intuitive search experiences".


# E2 — HIG Components: System experiences

Pages read in full: `system-experiences` (collection), `app-shortcuts`, `complications`, `controls`, `live-activities`, `notifications`, `snippets`, `status-bars`, `top-shelf`, `watch-faces`, `widgets`. Also read for interruption levels: `managing-notifications`.

System experiences are app surfaces that live **outside the app's windows**: Siri, Spotlight and Shortcuts; Control Center; the Lock Screen; the Dynamic Island; the Mac menu bar; the watch face and Smart Stack; CarPlay; StandBy; tvOS Top Shelf `[hig:system-experiences]`. For an AI product, these are how people start, monitor, approve and collect agent work while the app is closed.

## Cross-cutting rules for the parent system

- **Glanceable first.** One current key fact in heavy type, deep-linked to the exact screen. No ads.
- **One action registry [AI].** App Intents powers App Shortcuts, snippets, controls, widget and Live Activity buttons, and the Action button. Define each action once (verb, symbol, parameters, confirm/auth need) and render it per surface. **[XPLAT]** Android spreads this across App Shortcuts, App Actions, Quick Settings tiles, Glance widgets and notification actions; Windows across jump lists, toasts and Widgets; the web has none. The parent system needs a platform-neutral "exposed action" model.
- **Ambient = public [AI].** The Lock Screen, Always-On display, watch face and StandBy are visible to others. Redact, summarise harmlessly, and require unlock for consequential actions. Prompts and outputs count as sensitive.
- **State honesty.** Update only on change. Animate in **≤2 s**. Show "last updated". Use skeleton placeholders.
- **Brand through tint**, not the app icon. Every surface must survive monochrome, tinted, clear (Liquid Glass), vibrant, Night-Mode red and Always-On rendering, so **colour is never the only signal**.

| Key spec | Value | Source |
|---|---|---|
| Widget margin / tight margin | 16 pt / 11 pt | widgets |
| Widget min text | 11 pt; Dynamic Type Large–AX5 | widgets |
| Live Activity Lock Screen margin | 14 pt | live-activities |
| Dynamic Island corner radius | 44 pt | live-activities |
| Inner radius rule | outer radius − margin (`ContainerRelativeShape`) | live-activities, widgets |
| Widget / Live Activity animation max | 2 s | widgets, live-activities |
| Live Activity max duration / post-end linger / suggested dismissal | 8 h / up to 4 h / 15–30 min | live-activities |
| Snippet custom view max height | 400 pt | snippets |
| App Shortcuts per app / parameters per shortcut | 10 / 1 optional | app-shortcuts |
| Notification actions (iOS detail view / watch long look) | up to 4 / up to 4 + Dismiss | notifications |
| Time Sensitive window | now or within 1 h | managing-notifications |
| Watch long-look system-matching background | white @ 18% opacity | notifications |
| Complication min line width | 2 pt | complications |
| Rectangular complication large-image radius | 4 pt | complications |
| visionOS widget user scale | 75–125% | widgets |
| StandBy Live Activity scale | 2x | live-activities |
| Top Shelf scrolling banner count | 3–8 images | top-shelf |

| Page | iOS | iPadOS | macOS | tvOS | visionOS | watchOS |
|---|---|---|---|---|---|---|
| App Shortcuts | Yes | Yes | No (App Intents actions usable in Shortcuts on Mac) | No | Yes | Yes |
| Complications | No | No | No | No | No | Yes |
| Controls | Yes | Yes | Yes | No | No | No |
| Live Activities | Yes (Lock Screen, Home Screen, Dynamic Island, StandBy) | Yes (Lock Screen) | Mirrored into menu bar of paired Mac | No | No | Smart Stack (+ CarPlay Dashboard) |
| Notifications | Yes | Yes | Yes | Yes | Yes | Yes (short/long look) |
| Snippets | Yes | Yes | Yes | No | No | No |
| Status bars | Yes | Yes | No | No | No | No |
| Top Shelf | No | No | No | Yes | No | No |
| Watch faces | No | No | No | No | No | Yes |
| Widgets | Yes | Yes | Yes | No | Yes | Yes (Smart Stack) |

---

## App Shortcuts `[hig:app-shortcuts]` **[AI]**

**Purpose:** expose key functions and content through Siri, Spotlight, Shortcuts, the Action button and Pencil squeeze. Built on App Intents. Live from install (before first launch). Can personalise (recent contacts). **Max 10 per app.** The same intents also feed user-built cross-app shortcuts.

- **[AI] Adopt app schemas first** (NEW, Jun 2026). Schemas expose a domain app's actions and content to **Apple Intelligence**, so Siri can surface them in context. Use App Shortcuts for what schemas don't cover.
- Cover the most common tasks. Completing in place is best; opening the app is fine for multistep tasks.
- **One optional parameter** at most, with predictable values (people can't see the options while speaking).
- **[AI] When input is missing:** offer the likeliest value as the default, plus a short list of alternatives. Ask for any further information in a follow-up step. Keep phrases easy to say.
- Help discovery with in-app tips (`SiriTipUIView`). Respond with a **snippet** (static result or confirmation) or a **Live Activity** (changing state).
- **[AI] Audio-only devices** (AirPods, HomePod): put all critical information in the full spoken dialogue.
- Editorial: phrases are brief, include the app name, and may have variants. Write "App Shortcuts" and "Shortcuts" in title case and plural; a generic "shortcut" is lowercase.

**Platforms:** iOS/iPadOS show them in Spotlight Top Hit and the Shortcuts area (SF Symbol or preview image each). **Order by importance**; the system later re-ranks by use. Not supported on macOS or tvOS. **NEW:** WWDC26 video covers a "Use Model" transcript for shaping how App Entities appear to LLMs. **Change log:** 2026-06-08 app schemas · 2025-01-17 streamlined · 2023-06-05 new.

---

## Complications `[hig:complications]`

**Purpose:** timely data on the watch face. Faces have at least 1 slot, some 4 or more. Since watchOS 9 complications are built with WidgetKit "accessory" families (circular, corner, inline, rectangular). ClockKit legacy templates are non-graphic and untinted.

- Show dynamic data, not just a launcher. Support **all families** (fall back to the app icon). Offer several per family, each with its **own deep link**.
- Mind Always-On privacy. Data comes from a **timeline** with a limited number of daily updates and stored entries.
- Gauges: **closed** = percentage, **open** = arbitrary range, **segmented** = app range with rapid change.
- **Tinted mode** desaturates to one colour, so never rely on colour. Lines **≥2 pt**. Provide static **placeholders**. Bezel text can span **~180°**.
- watchOS 10+: rectangular complications can appear in the **Smart Stack**.

| Layout | Style | Weight | Size 40 / 41 / 44 / 45–49 mm |
|---|---|---|---|
| Circular (regular) | Rounded | Medium | 12 / 12.5 / 13 / 14.5 pt |
| Circular extra-large | Rounded | Medium | 34.5 / 36.5 / 36.5 / 41 pt |
| Corner | Rounded | Semibold | 10 / 10.5 / 11 / 12 pt |
| Rectangular | Rounded | Medium | 16.5 / 17.5 / 18 / 19.5 pt |

**Circular (regular)** (circular mask applied):

| Image | 40mm | 41mm | 44mm | 45mm/49mm |
|---|---|---|---|---|
| Image | 42x42 pt (84x84 px @2x) | 44.5x44.5 pt (89x89 px @2x) | 47x47 pt (94x94 px @2x) | 50x50 pt (100x100 px @2x) |
| Closed gauge | 27x27 pt (54x54 px @2x) | 28.5x28.5 pt (57x57 px @2x) | 31x31 pt (62x62 px @2x) | 32x32 pt (64x64 px @2x) |
| Open gauge | 11x11 pt (22x22 px @2x) | 11.5x11.5 pt (23x23 px @2x) | 12x12 pt (24x24 px @2x) | 13x13 pt (26x26 px @2x) |
| Stack (not text) | 28x14 pt (56x28 px @2x) | 29.5x15 pt (59X30 px @2x) | 31x16 pt (62x32px @ 2x) | 33.5x16.5 pt (67x33 px @2x) |

**Circular extra-large** (X-Large face; circular mask on circular and gauge images):

| Image | 40mm | 41mm | 44mm | 45mm/49mm |
|---|---|---|---|---|
| Image | 120x120 pt (240x240 px @2x) | 127x127 pt (254x254 px @2x) | 132x132 pt (264x264 px @2x) | 143x143 pt (286x286 px @2x) |
| Open gauge | 31x31 pt (62x62 px @2x) | 33x33 pt (66x66 px @2x) | 33x33 pt (66x66 px @2x) | 37x37 pt (74x74 px @2x) |
| Closed gauge | 77x77 pt (154x154 px @2x) | 81.5x81.5 (163x163 px @2x) | 87x87 pt (174x174 px @2x) | 91.5x91.5 (183x183 px @2x) |
| Stack | 80x40 pt (160x80 px @2x) | 85x42 (170x84 px @2x) | 87x44 pt (174x88 px @2x) | 95x48 pt (190x96 px @2x ) |

**Circular-family placeholders:**

| Layout | 38mm | 40mm/42mm | 41mm | 44mm | 45mm/49mm |
|---|---|---|---|---|---|
| Circular | – | 42x42 pt (84x84 px @2x) | 44.5x44.5 pt (89x89 px @2x) | 47x47 pt (94x94 px @2x) | 50x50 pt (100x100 px @2x) |
| Bezel | – | 42x42 pt (84x84 px @2x) | 44.5x44.5 pt (89x89 px @2x) | 47x47 pt (94x94 px @2x) | 50x50 pt (100x100 px @2x) |
| Extra Large | – | 120x120 pt (240x240 px @2x) | 127x127 pt (254x254 px @2x) | 132x132 pt (264x264 px @2x) | 143x143 pt (286x286 px @2x) |

**Corner** (circular mask applied):

| Image | 40mm | 41mm | 44mm | 45mm/49mm |
|---|---|---|---|---|
| Circular | 32x32 pt (64x64 px @2x) | 34x34 pt (68x68 px @2x) | 36x36 pt (72x72 px @2x) | 38x38 pt (76x76 px @2x ) |
| Gauge | 20x20 pt (40x40 px @2x) | 21x21 pt (42x42 px @2x) | 22x22 pt (44x44 px @2x) | 24x24 pt (48x48 px @2x) |
| Text | 20x20 pt (40x40 px @2x) | 21x21 pt (42x42 px @2x) | 22x22 pt (44x44 px @2x) | 24x24 pt (48x48 px @2x) |
| Placeholder (38mm: –) | 20x20 pt (40x40 px @2x) [40/42mm] | 21x21 pt (42x42 px @2x) | 22x22 pt (44x44 px @2x) | 24x24 pt (48x48 px @2x) |

**Inline: utilitarian small** (corner rectangle) **and large** (text with a leading icon, along the bottom):

| Content | 38mm | 40mm/42mm | 41mm | 44mm | 45mm/49mm |
|---|---|---|---|---|---|
| Small: Flat | 9-21x9 pt (18-42x18 px @2x) | 10-22x10 pt (20-44x20 px @2x) | 10.5-23.5x21 pt (21-47x21 @2x) | N/A | 12-26x12 pt (24-52x24 px @2x) |
| Small: Ring | 14x14 pt (28x28 px @2x) | 14x14 pt (28x28 px @2x) | 15x15 pt (30x30 px @2x) | 16x16 pt (32x32 px @2x) | 16.5x16.5 pt (33x33 px @2x) |
| Small: Square | 20x20 pt (40x40 px @2x) | 22x22 pt (44x44 px @2x) | 23.5x23.5 pt (47x47 px @2x) | 25x25 pt (50x50 px @2x) | 26x26 pt (52x52 px @2x) |
| Large: Flat | 9-21x9 pt (18-42x18 px @2x) | 10-22x10 pt (20-44x20 px @2x) | 10.5-23.5x10.5 pt (21-47x21 px @2x) | N/A | 12-26x12 pt (24-52x24 px @2x) |

**Rectangular** (room for charts; both large-image layouts get an automatic **4 pt corner radius**):

| Content | 40mm | 41mm | 44mm | 45mm/49mm |
|---|---|---|---|---|
| Large image with title * | 150x47 pt (300x94 px @2x) | 159x50 pt (318x100 px @2x) | 171x54 pt (342x108 px @2x) | 178.5x56 pt (357x112 px @2x) |
| Large image without title * | 162x69 pt (324x138 px @2x) | 171.5x73 pt (343x146 px @2x) | 184x78 pt (368x156 px @2x) | 193x82 pt (386x164 px @2x) |
| Standard body | 12x12 pt (24x24 px @2x) | 12.5x12.5 pt (25x25 px @2x) | 13.5x13.5 pt (27x27 px @2x) | 14.5x14.5 pt (29x29 px @2x) |
| Text gauge | 12x12 pt (24x24 px @2x) | 12.5x12.5 pt (25x25 px @2x) | 13.5x13.5 pt (27x27 px @2x) | 14.5x14.5 pt (29x29 px @2x) |

**Legacy (ClockKit) templates.** In stack rows the width is the maximum.

| Template / Image | 38mm | 40mm/42mm | 41mm | 44mm | 45mm/49mm |
|---|---|---|---|---|---|
| Circular small: Ring | 20x20 pt (40x40 px @2x) | 22x22 pt (44x44 px @2x) | 23.5x23.5 pt (47x47 px @2x) | 24x24 pt (48x48 px @2x) | 26x26 pt (52x52 px @2x) |
| Circular small: Simple | 16x16 pt (32x32 px @2x) | 18x18 pt (36x36 px @2x) | 19x19 pt (38x38 px @2x) | 20x20 pt (40x40 px @2x) | 21.5x21.5 pt (43x43 px @2x) |
| Circular small: Stack | 16x7 pt (32x14 px @2x) | 17x8 pt (34x16 px @2x) | 18x8.5 pt (36x17 px @2x) | 19x9 pt (38x18 px @2x) | 19x9.5 pt (38x19 px @2x) |
| Circular small: Placeholder | 16x16 pt (32x32 px @2x) | 18x18x pt (36x36 px @2x) | 19x19 pt (38x38 px @2x) | 20x20 pt (40x40 px @2x) | 21.5x21.5 pt (43x43 px @2x) |
| Modular small: Ring | 18x18 pt (36x36 px @2x) | 19x19 pt (38x38 px @2x) | 20x20 pt (40x40 px @2x) | 21x21 pt (42x42 px @2x) | 22.5x22.5 pt (45x45 px @2x) |
| Modular small: Simple | 26x26 pt (52x52 px @2x) | 29x29 pt (58x58 px @2x) | 30.5x30.5 pt (61x61 px @2x) | 32x32 pt (64x64 px @2x) | 34.5x34.5 pt (69x69 px @2x) |
| Modular small: Stack | 26x14 pt (52x28 px @2x) | 29x15 pt (58x30 px @2x) | 30.5x16 pt (61x32 px @2x) | 32x17 pt (64x34 px @2x) | 34.5x18 pt (69x36 px @2x) |
| Modular small: Placeholder | 26x26 pt (52x52 px @2x) | 29x29 pt (58x58 px @2x) | 30.5x30.5 pt (61x61 px @2x) | 32x32 pt (64x64 px @2x) | 34.5x34.5 pt (69x69 px @2x) |
| Modular large: Columns / Standard body / Table (up to 3 rows) | 11-32x11 pt (22-64x22 px @2x) | 12-37x12 pt (24-74x24 px @2x) | 12.5-39x12.5 pt (25-78x25 px @2x) | 14-42x14 pt (28-84x28 px @2x) | 14.5-44x14.5 pt (29-88x29 px @2x) |
| Extra large: Ring | 63x63 pt (126x126 px @2x) | 66.5x66.5 pt (133x133 px @2x) | 70.5x70.5 pt (141x141 px @2x) | 73x73 pt (146x146 px @2x) | 79x79 pt (158x158 px @2x) |
| Extra large: Simple | 91x91 pt (182x182 px @2x) | 101.5x101.5 pt (203x203 px @2x) | 107.5x107.5 pt (215x215 px @2x) | 112x112 pt (224x224 px @2x) | 121x121 pt (242x242 px @2x ) |
| Extra large: Stack | 78x42 pt (156x84 px @2x) | 87x45 pt (174x90 px @2x) | 92x47.5 pt (184x95 px @2x) | 96x51 pt (192x102 px @2x) | 103.5x53.5 pt (207x107 px @2x) |
| Extra large: Placeholder | 91x91 pt (182x182 px @2x) | 101.5x101.5 pt (203x203 px @2x) | 107.5x107.5 pt (215x215 px @2x) | 112x112 pt (224x224 px @2x) | 121x121 pt (242x242 px @2x) |

watchOS only. **Change log:** 2023-10-24 WidgetKit links · 2023-06-05 rectangular in Smart Stack · 2022-09-14 Ultra specs.

---

## Controls `[hig:controls]` **[AI]**

**Purpose:** a button or toggle in Control Center, on the Lock Screen or on the Action button. Buttons act, deep link, or open a locked-device camera. Toggles switch between two states. **Anatomy:** a symbol + a title + an optional value. Control Center shows the symbol, plus title and value at larger sizes. The Lock Screen shows the symbol only. The Action button shows symbol + value in the Dynamic Island.

- Useful without opening the app. **[AI]** E.g. a control that starts a Live Activity ("Start agent task").
- Update on tap, completion or push. **Show in-progress state.**
- The symbol must work alone. Toggles need **on and off symbols**. Long actions **animate indefinitely until done** (**[AI]** the "working" idiom).
- The brand tint colours the on state and the Dynamic Island readout.
- Configure on first add. Action-button hints are **verbs** ("Hold for Silent"). Give **placeholders** for situational content.
- **[AI] Redact when locked. Require authentication** for security-affecting or consequential actions.
- Locked camera (iOS 18+): capture only; unlock for anything more.

iOS, iPadOS, macOS only. **[XPLAT]** The Android equivalent is the Quick Settings tile. **Change log:** 2024-06-10 new.

---

## Live Activities `[hig:live-activities]` **[AI]**

**Purpose:** at-a-glance tracking of a task with a **defined start and end**, updated over a few hours, optionally interactive. **[AI] The native surface for long-running generation and agent runs.** Shown on the iPhone/iPad Lock Screen, Home Screen, Dynamic Island and StandBy, the Mac menu bar, the Watch Smart Stack and CarPlay.

**Presentations (all required):** **Compact** (leading + trailing around the camera; 1 activity). **Minimal** (2+ activities; attached and detached). **Expanded** (touch and hold). **Lock Screen** (bottom banner like expanded; an alert banner on devices without a Dynamic Island). **StandBy** (minimal; a tap shows Lock Screen **at 2x**, full-screen background).

**Rules**
- **[AI] Tasks ≤8 h.** Key facts only; tap deep links. No ads. **[AI] Sensitive content:** show a harmless summary, or redact and let people opt in.
- Match the app's look in light and dark. Logo mark without a container, never the app icon. **Medium weight or heavier** text.
- Use only the space you need. Even, concentric margins so nothing pokes into corners. Separate blocks with an **inset shape or thick line**.
- **[AI] Variable height** (Lock Screen and expanded): grow as data arrives (rideshare "locating" → driver and ETA), which is the same arc as "thinking → steps → result".
- Compact, minimal and expanded have a **fixed black background**. Only the Lock Screen view takes a custom background (check contrast on dimmed Always-On). Use bold brand colours and tint the **key line** to match.
- Animation **≤2 s**, none on dimmed Always-On. Move existing elements rather than removing and re-adding them; fade neighbours.
- Interactivity: essential only, **ideally one control** (**[AI]** Stop, Pause, Approve).
- **[AI] Lifecycle:** start when expected and offer an in-app off switch. Offer an **App Shortcut** to start it. **Update only on change. Alert only for essential updates, and never send a push for the same update.** Use **one rotating activity** for several events. **End immediately.** It vanishes from the Dynamic Island and CarPlay but stays **up to 4 h** on the Lock Screen, Mac and Smart Stack. Set the dismissal time **~15–30 min** and use it for the summary.
- Compact: leading and trailing read as one unit, **snug to the camera** with no padding, balanced widths, same deep link. Minimal: live data, not just a logo. Expanded: keep compact's element positions and hug the camera.
- Lock Screen: **don't copy notification layouts**. Verify the auto dismiss-button colour. **Margin 14 pt.** StandBy: custom 2x layout; prefer the **default background**; **Night Mode tints red**.
- Design for iPhone first, then StandBy, CarPlay and Watch.

**CarPlay:** compact sides merged. Use `ActivityFamily.small` for a custom layout. **No interactivity.** **macOS:** paired-Mac menu bar; a click opens iPhone Mirroring. **[XPLAT]** Desktop needs its own tray or menu-bar "ongoing task" item. **watchOS:** top of the Smart Stack. A custom layout may add a button, but **CarPlay reuses that layout** without interaction. Not supported on tvOS or visionOS.

CarPlay sizes (pt): **240x78 · 240x100 · 170x78**. Test with Smart Display Zoom:

| Configuration | Resolution (pt) |
|---|---|
| Widescreen | 1920x720 |
| Portrait | 900x1200 |
| Standard | 800x480 |

iOS (pt):

| Screen dimensions (portrait) | Compact leading | Compact trailing | Minimal (width given as a range) | Expanded (height given as a range) | Lock Screen (height given as a range) |
|---|---|---|---|---|---|
| 430x932 | 62.33x36.67 | 62.33x36.67 | 36.67–45x36.67 | 408x84–160 | 408x84–160 |
| 393x852 | 52.33x36.67 | 52.33x36.67 | 36.67–45x36.67 | 371x84–160 | 371x84–160 |

Dynamic Island **corner radius 44 pt** (matches the TrueDepth camera). Width in pt:

| Device | Compact or minimal | Expanded |
|---|---|---|
| iPhone 17 Pro Max | 250 | 408 |
| iPhone 17 Pro | 230 | 371 |
| iPhone Air | 250 | 408 |
| iPhone 17 | 230 | 371 |
| iPhone 16 Pro Max | 250 | 408 |
| iPhone 16 Pro | 230 | 371 |
| iPhone 16 Plus | 250 | 408 |
| iPhone 16 | 230 | 371 |
| iPhone 15 Pro Max | 250 | 408 |
| iPhone 15 Pro | 230 | 371 |
| iPhone 15 Plus | 250 | 408 |
| iPhone 15 | 230 | 371 |
| iPhone 14 Pro Max | 250 | 408 |
| iPhone 14 Pro | 230 | 371 |

iPadOS Lock Screen (pt); macOS uses the iOS dimensions:

| Screen dimensions (portrait) | Lock Screen (height given as a range) |
|---|---|
| 1366x1024 | 500x84–160 |
| 1194x834 | 425x84–160 |
| 1012x834 | 425x84–160 |
| 1080x810 | 425x84–160 |
| 1024x768 | 425x84–160 |

watchOS Smart Stack (same as watchOS widgets):

| Apple Watch size | Size of a Live Activity in the Smart Stack (pt) |
|---|---|
| 40mm | 152x69.5 |
| 41mm | 165x72.5 |
| 44mm | 173x76.5 |
| 45mm | 184x80.5 |
| 49mm | 191x81.5 |

**NEW:** iPhone 17 and iPhone Air rows. WWDC26 video mentions a **landscape** Dynamic Island style. **Change log:** 2025-12-16 all platforms updated, macOS and CarPlay added · 2024-06-10 watchOS · 2023-10-24 expanded · 2023-06-05 iOS 17 · 2022-11-03 specs · 2022-09-23 new.

---

## Notifications `[hig:notifications]` + `[hig:managing-notifications]` **[AI]**

**Purpose:** timely, high-value information at a glance. **Consent required.** Shown as a banner, an app-icon **badge**, and a Notification Center item. **Communication** notifications show the sender's avatar instead of the app icon.

- Be concise. **[AI] Never repeat a notification for the same thing**, even if it's ignored. No nagging.
- Don't tell people to do tasks in the app; offer actions.
- **[AI] Errors go in an alert, not a notification.** **[XPLAT]** Web and Material use toasts. The parent system must decide where background-agent failures appear.
- In the foreground, update the app quietly instead. **[AI]** If the chat is open, stream the result in.
- **[AI] No sensitive content**, including prompts and outputs.

**Writing [AI]:** *Title*: short, title case, no ending punctuation; omit it if generic so the app name shows. *Body*: full sentences, sentence case, never truncated by hand. *Hidden-preview body* (`hiddenPreviewsBodyPlaceholder`): a generic sentence-case line such as "New comment" (**[AI]** "Response ready"). No app name or icon (the system adds them). Sound: short and distinctive, never essential. Custom vibration isn't possible.

**Actions:** **up to 4** in the detail view. Short title-case labels that name the result, no app name, allow for localisation. **No "open app" action.** **Prefer non-destructive actions**; destructive ones get a distinct style. Each gets an SF Symbol on the **trailing** side. **[XPLAT]** Android allows up to 3, shown inline.

**Badging:** **unread notification count only** (never weather, prices or scores). Never the only signal. Keep it current; **a count of 0 clears the related notifications from Notification Center**. No fake badges. **[XPLAT]** Android shows launcher dots; Windows a taskbar overlay.

**Interruption levels** (required for non-communication notifications; Focus and summaries delay only the alert):

| Interruption level | Overrides scheduled delivery | Breaks through Focus | Overrides Ring/Silent switch on iPhone and iPad |
|---|---|---|---|
| Passive | No | No | No |
| Active | No | No | No |
| Time Sensitive | Yes | Yes | No |
| Critical | Yes | Yes | Yes |

Passive = at leisure. Active (default) = on arrival. Time Sensitive = **now or within 1 h**; users periodically review it. Critical = health and safety, **entitlement required**. **Never send marketing as Time Sensitive**; marketing needs opt-in and in-app settings. **[AI]** Result ready = Active. Digest = Passive. Approval expiring within the hour = Time Sensitive. Never Critical.

**Grouping:** the HIG gives no threading rules, so the parent system must define them (e.g. per conversation or agent run). **[XPLAT]** Android uses channels.

**watchOS:** the **short look** is shown while the wrist is raised: discreet, never the only channel. The **long look** has a fixed structure: **sash** (icon and name; colour or blur), custom content, system **Dismiss**. A static interface is required (offline fallback); a dynamic one is preferred. Background: **white at 18% opacity** to match the system. **Up to 4 custom actions.** **Double tap runs the first non-destructive action.** **[AI] Never put Approve, Send or Run first**; lead with View or Snooze. **Change log:** 2023-10-24 double tap.

---

## Snippets `[hig:snippets]` **[AI]** (NEW page, 2026-06-08)

**Purpose:** a compact view for the **result** of an action run through Siri, Spotlight or Shortcuts, or a **confirmation** before it runs. **[AI] This is Apple's canonical assistant "confirm action" and "result" card.** A *confirmation* snippet confirms or cancels and can include options. A *result* snippet is informational and needs no action. **Every snippet intent ends in a result; confirmation is optional.**

**Anatomy:** dialogue (spoken; the text appears above the view by default), a custom view (**max height 400 pt**, may hold buttons), and system buttons: for confirmation, a secondary **Cancel (left)** and a primary with a custom label **(right)**; for a result, a single **Done**.

- Keep contrast with the system background in light and dark, and keep margins consistent.
- Stay **≤400 pt**, allowing for Dynamic Type. For more detail, deep link instead.
- **[AI] Give the primary button a specific verb** (system `ConfirmationActionName` or custom): "Order", not "OK" or "Proceed". **The default is "Continue."**
- Carry the meaning in the view. Don't repeat the spoken dialogue on screen.

iOS, iPadOS, macOS only (not supported on tvOS, visionOS or watchOS). **[XPLAT]** Cancel-left / primary-right matches Apple and Material; Windows dialogs put the primary button on the left.

---

## Status bars `[hig:status-bars]`

**Purpose:** a top-edge strip with time, connectivity and battery. iOS and iPadOS only.
- Keep it legible. The background is transparent by default; **prefer a scroll edge effect** (a blur behind the bar; `ScrollEdgeEffectStyle` / `UIScrollEdgeEffect`, Liquid Glass era). Never imply that content behind it is interactive.
- Hide it temporarily for full-screen media. **Never hide it permanently**; restore it with a simple gesture (a single tap in Photos).
- **[XPLAT]** On Android edge-to-edge, the app manages insets and scrims. Web and desktop have no equivalent.

---

## Top Shelf `[hig:top-shelf]`

**Purpose:** a content showcase at the top of the tvOS Home Screen when the app is focused in the Dock. tvOS only.
- Jump straight into content. Carousel layouts include **Play** and **More Info**. Feature new content, not items already bought or watched. Personalise (resume, recommendations). **No ads or prices.** Prefer dynamic, **layered images**.
- Fallback: provide at least one **static image**, which the system flips and blurs to fit **1920 px wide at 16:9**. It isn't focusable, so don't make it look interactive. Size: **2320x720 pt (2320x720 px @1x, 4640x1440 px @2x)**.
- Layouts: **Carousel actions** (full-screen media, title and optional subtitle). **Carousel details** (adds plot and cast; title near the top; optional "Featured on My App"). **Sectioned content row** (focusable; enough images to fill the width; at least 1 label). **Scrolling inset banner** (auto-advances and loops; **3–8 images**; text baked into the image and repeated in the accessibility label).

| Shape | Aspect | Image size |
|---|---|---|
| Poster (2:3) | Actual size | 404x608 pt (404x608 px @1x, 808x1216 px @2x) |
|  | Focused/Safe zone size | 380x570 pt (380x570 px @1x, 760x1140 px @2x) |
|  | Unfocused size | 333x570 pt (333x570 px @1x, 666x1140 px @2x) |
| Square (1:1) | Actual size | 608x608 pt (608x608 px @1x, 1216x1216 px @2x) |
|  | Focused/Safe zone size | 570x570 pt (570x570 px @1x, 1140x1140 px @2x) |
|  | Unfocused size | 500x500 pt (500x500 px @1x, 1000x1000 px @2x) |
| 16:9 | Actual size | 908x512 pt (908x512 px @1x, 1816x1024 px @2x) |
|  | Focused/Safe zone size | 852x479 pt (852x479 px @1x, 1704x958 px @2x) |
|  | Unfocused size | 782x440 pt (782x440 px @1x, 1564x880 px @2x) |
| Scrolling inset banner | Actual size | 1940x692 pt (1940x692 px @1x, 3880x1384 px  @2x) |
|  | Focused/Safe zone size | 1740x620 pt (1740x620 px @1x, 3480x1240 px @2x) |
|  | Unfocused size | 1740x560 pt (1740x560 px @1x, 3480x1120 px @2x) |

When sizes are mixed in a row, images scale up to the tallest (a 16:9 image becomes 500 px high next to posters or squares).

---

## Watch faces `[hig:watch-faces]`

**Purpose:** the main watchOS view. Faces can be shared (watchOS 7+) from apps, the web, Messages, Mail or social media. watchOS only.
- Share faces that showcase several of your complications, with accent colour, images and styles. If the app is missing, the system prompts people to install it.
- Show previews: email a face to yourself for one with an illustrated bezel, or composite a hardware bezel.
- California, Chronograph Pro, Gradient, Infograph, Infograph Modular, Meridian, Modular Compact and Solar Dial need **Series 4+**; Explorer needs **Series 3 (cellular)+**. Offer alternatives for older watches and label supported devices. On an incompatibility error, offer a compatible face instead of showing the error.

---

## Widgets `[hig:widgets]` **[AI]**

**Purpose:** glanceable information and focused interactions on the Home Screen, Lock Screen and Today View; the Mac desktop and Notification Center; visionOS surfaces; the Watch Smart Stack; StandBy and CarPlay. Not supported on tvOS.

| Widget size | iPhone | iPad | Mac | Apple Vision Pro |
|---|---|---|---|---|
| System small | Home Screen, Today View, StandBy, and CarPlay | Home Screen, Today View, and Lock Screen | Desktop and Notification Center | Horizontal and vertical surfaces |
| System medium | Home Screen and Today View | Home Screen and Today View | Desktop and Notification Center | Horizontal and vertical surfaces |
| System large | Home Screen and Today View | Home Screen and Today View | Desktop and Notification Center | Horizontal and vertical surfaces |
| System extra large | Not supported | Home Screen and Today View | Desktop and Notification Center | Horizontal and vertical surfaces |
| System extra large portrait | Not supported | Not supported | Not supported | Horizontal and vertical surfaces |

| Widget size | iPhone | iPad | Apple Watch |
|---|---|---|---|
| Accessory circular | Lock Screen | Lock Screen | Watch complications and in the Smart Stack |
| Accessory corner | Not supported | Not supported | Watch complications |
| Accessory inline | Lock Screen | Lock Screen | Watch complications |
| Accessory rectangular | Lock Screen | Lock Screen | Watch complications and in the Smart Stack |

**Appearances:** the Home Screen offers **light, dark, clear and tinted**. Clear desaturates and adds **Liquid Glass**; tinted desaturates and applies the user's tint. The iPad Lock Screen is untinted monochrome. StandBy scales widgets up without a background, **red monochrome in low light**. Rendering modes: **full-color** (unchanged). **Accented** (background removed; *accent* and *primary* groups each get a solid colour: white on iPhone/iPad/Mac; on Watch, primary white and accent in the face colour). **Vibrant** (desaturated for the Lock Screen and Mac desktop).

| Platform | Full-color | Accented | Vibrant |
|---|---|---|---|
| iPhone | Home Screen, Today view, StandBy and CarPlay (with the background removed) | Home Screen and Today view | Lock Screen, StandBy in low-light conditions |
| iPad | Home Screen and Today view | Home Screen and Today view | Lock Screen |
| Apple Watch | Smart Stack, complications | Smart Stack, complications | Not supported |
| Mac | Desktop and Notification Center | Not supported | Desktop |
| Apple Vision Pro | Horizontal and vertical surfaces | Horizontal and vertical surfaces | Not supported |

**Rules**
- One simple idea tied to the app's purpose, not a copy of the app icon. Content should change during the day.
- Multiple sizes only when each adds value; never stretch content. Balance density.
- Brand with restraint; any logo small, **top-right**. Don't mirror the widget inside the app. **[AI] Say when sign-in adds value.**
- **[AI] Updates are periodic, not real-time.** Show **"last updated"**. The system renders live dates and times. **Don't hide stale data behind placeholders.** For real-time progress use a **Live Activity** (shared frameworks; design them together).
- **Interaction:** a tap opens the right place. Simple related buttons and toggles, not app-like layouts. **Inline accessory = 1 tap target.** **[AI]** Good fits: New chat, recent threads, agent status.
- Margins are smaller on the Mac desktop and Lock Screen. No numeric widget radius is given; use `ContainerRelativeShape`. Never rasterise text. Custom fonts sparingly.
- **Colour** never carries meaning alone. Full-colour images only for media. Accented: mark the accent group (`widgetAccentable`). Vibrant: opaque greys (white or light for primary, darker for secondary), never reduced-opacity white.
- **[AI] Placeholder = skeleton** (static chrome plus semi-opaque bars and circles). Realistic gallery preview. The description starts with a verb ("See…"), never "This widget…", **one description for all sizes**. The Add button can take the brand tint.

**iOS/iPadOS:** Lock Screen widgets (inline above the clock, circular and rectangular below) follow complication principles. Support **Always-On** contrast. **StandBy** shows 2 small widgets scaled up. StandBy and **CarPlay** remove the background, so use large text and no background colour.

**visionOS:** persistent 3D widgets, user-scalable **75–125%**. Two detail levels: *simplified* at distance (bigger type, **no buttons**) and *default* up close. **Mounting:** *elevated* (default, any surface) or *recessed* (vertical only, window-like). Test every frame width. **Treatment:** *paper* (reacts to lighting) or *glass* (foreground stays bright; for information-rich widgets). Test every tint palette.

**watchOS:** a **meaningful background colour** (the default is black). Use RelevanceKit signals to rise in the Stack.

**[XPLAT]** Android uses resizable grid cells and Windows a Widgets board; the web has neither. Define a cross-platform "glance card".

iOS:

| Screen size (portrait, pt) | Small (pt) | Medium (pt) | Large (pt) | Circular (pt) | Rectangular (pt) | Inline (pt) |
|---|---|---|---|---|---|---|
| 430×932 | 170x170 | 364x170 | 364x382 | 76x76 | 172x76 | 257x26 |
| 428x926 | 170x170 | 364x170 | 364x382 | 76x76 | 172x76 | 257x26 |
| 414x896 | 169x169 | 360x169 | 360x379 | 76x76 | 160x72 | 248x26 |
| 414x736 | 159x159 | 348x157 | 348x357 | 76x76 | 170x76 | 248x26 |
| 393x852 | 158x158 | 338x158 | 338x354 | 72x72 | 160x72 | 234x26 |
| 390x844 | 158x158 | 338x158 | 338x354 | 72x72 | 160x72 | 234x26 |
| 375x812 | 155x155 | 329x155 | 329x345 | 72x72 | 157x72 | 225x26 |
| 375x667 | 148x148 | 321x148 | 321x324 | 68x68 | 153x68 | 225x26 |
| 360x780 | 155x155 | 329x155 | 329x345 | 72x72 | 157x72 | 225x26 |
| 320x568 | 141x141 | 292x141 | 292x311 | N/A | N/A | N/A |

iPadOS (* = Display Zoom set to More Space):

| Screen size (portrait, pt) | Target | Small (pt) | Medium (pt) | Large (pt) | Extra large (pt) |
|---|---|---|---|---|---|
| 768x1024 | Canvas | 141x141 | 305.5x141 | 305.5x305.5 | 634.5x305.5 |
|  | Device | 120x120 | 260x120 | 260x260 | 540x260 |
| 744x1133 | Canvas | 141x141 | 305.5x141 | 305.5x305.5 | 634.5x305.5 |
|  | Device | 120x120 | 260x120 | 260x260 | 540x260 |
| 810x1080 | Canvas | 146x146 | 320.5x146 | 320.5x320.5 | 669x320.5 |
|  | Device | 124x124 | 272x124 | 272x272 | 568x272 |
| 820x1180 | Canvas | 155x155 | 342x155 | 342x342 | 715.5x342 |
|  | Device | 136x136 | 300x136 | 300x300 | 628x300 |
| 834x1112 | Canvas | 150x150 | 327.5x150 | 327.5x327.5 | 682x327.5 |
|  | Device | 132x132 | 288x132 | 288x288 | 600x288 |
| 834x1194 | Canvas | 155x155 | 342x155 | 342x342 | 715.5x342 |
|  | Device | 136x136 | 300x136 | 300x300 | 628x300 |
| 954x1373 * | Canvas | 162x162 | 350x162 | 350x350 | 726x350 |
|  | Device | 162x162 | 350x162 | 350x350 | 726x350 |
| 970x1389 * | Canvas | 162x162 | 350x162 | 350x350 | 726x350 |
|  | Device | 162x162 | 350x162 | 350x350 | 726x350 |
| 1024x1366 | Canvas | 170x170 | 378.5x170 | 378.5x378.5 | 795x378.5 |
|  | Device | 160x160 | 356x160 | 356x356 | 748x356 |
| 1192x1590 * | Canvas | 188x188 | 412x188 | 412x412 | 860x412 |
|  | Device | 188x188 | 412x188 | 412x412 | 860x412 |

visionOS:

| Widget | Size in pt | Size in mm (scaled to 100%) |
|---|---|---|
| Small | 158x158 | 268x268 |
| Medium | 338x158 | 574x268 |
| Large | 338x354 | 574x600 |
| Extra large | 450x338 | 763x574 |
| Extra large portrait | 338x450 | 574x763 |

watchOS Smart Stack:

| Apple Watch size | Size of a widget in the Smart Stack (pt) |
|---|---|
| 40mm | 152x69.5 |
| 41mm | 165x72.5 |
| 44mm | 173x76.5 |
| 45mm | 184x80.5 |
| 49mm | 191x81.5 |

**NEW:** clear and tinted Liquid Glass appearances; visionOS mounting, treatment and LOD; CarPlay widgets. **Change log:** 2025-12-16 all platforms updated, visionOS and CarPlay added · 2025-01-17 watchOS dimensions corrected · 2024-06-10 accented (iOS 18) · 2023-06-05 watchOS, iPad Lock Screen, iOS 17 / macOS 14 · 2022-11-03 iPhone Lock Screen.

---

## AI-product mapping

| AI need | Apple surface | Key constraint |
|---|---|---|
| Invoke the assistant or an action from anywhere | App Intents → app schemas / App Shortcuts (≤10), controls, Action button | One optional parameter; clarify missing input with a default and short alternatives; full spoken dialogue for audio-only |
| Confirm a consequential action | Confirmation snippet | Specific verb on the primary button (default "Continue"); Cancel left; view ≤400 pt; auth for security-affecting controls |
| Show an action's result | Result snippet → deep link | Done button; no duplicate dialogue in the view |
| Long-running generation or agent run | Live Activity | ≤8 h; update only on change; ≤1 control (Stop, Approve); alert only when essential; no duplicate push; end immediately; 15–30 min summary linger (max 4 h) |
| Background completion or needs-input | Notification | Correct interruption level (Active / Time Sensitive ≤1 h, never Critical); ≤4 actions; non-destructive first (watch double tap); no sensitive content; hidden-preview placeholder |
| Ambient status or recent threads | Widget / complication | Not real-time; "last updated"; skeleton placeholder; 16/11 pt margins; ≥11 pt text |


# 4–5. Inputs and Platforms

# F — HIG Inputs + Getting started / Platforms

Pages read in full: `inputs`, `action-button`, `apple-pencil-and-scribble`, `camera-control`, `digital-crown`, `eyes`, `focus-and-selection`, `game-controls`, `gestures`, `gyro-and-accelerometer`, `keyboards`, `nearby-interactions`, `pointing-devices`, `remotes`, `getting-started`, `design-principles`, `designing-for-ios`, `designing-for-ipados`, `designing-for-iphone-duo`, `designing-for-macos`, `designing-for-tvos`, `designing-for-visionos`, `designing-for-watchos`, `designing-for-games`.

Tags: **[AI]** relevant to an AI product. **[XPLAT]** differs from Windows / Linux / web / Android, or needs a cross-platform decision. **[NEW]** new in 2025–26. Tables are verbatim unless marked *derived*.

---

# PART 1 — INPUTS

## 1.0 Inputs `[hig:inputs]` and cross-input rules
Collection page indexing 13 input pages; it has no rules of its own. The same rules recur across all of them:
- **Never make one input the only path.** This applies to custom gestures, motion, nearby interactions and gaze.
- **Behave the same across touch, pointer, eyes and keyboard**, including modifier semantics.
- **Never redefine system-reserved inputs**: standard shortcuts, systemwide trackpad gestures, visionOS palm/hand-roll overlays, watchOS edge swipes, crown press, controller Home button.
- **Keep accident-prone inputs (hover, Pencil double tap and squeeze, remote taps) non-destructive and undoable.** **[AI]** Never bind send, run, accept-all or delete to them.
- **Give feedback immediately and continuously, and show clearly when a gesture is unavailable.**

---

## 1.1 Keyboards `[hig:keyboards]`
A physical keyboard works on every device except Apple Watch.
- *Shortcut* = primary key + modifiers (Control, Option, Shift, Command).
- *Key binding* = a game key, often a single key.

**Rules**
- Support **Full Keyboard Access** (iOS, iPadOS, macOS, visionOS). It reaches every window, menu, control and system feature.
- **iPadOS (IMPORTANT):** implement keyboard navigation only for text fields, text views, sidebars and collections. **Don't** implement it for buttons, segmented controls or switches; leave those to Full Keyboard Access.
  - **[XPLAT]** Web (WCAG 2.1.1 / 2.4.7) and Windows require *every* control to be Tab-reachable with a visible focus indicator. The parent system must require full Tab coverage on web, Windows and Linux.
- **Respect standard shortcuts.** Repurpose one only if its action is meaningless in your app (example: no text editing, so ⌘I can mean Get Info instead of Italic).
- Games still honour ⌘Q and must allow rebinding.

### Standard keyboard shortcuts (verbatim)
| Primary key | Keyboard shortcut | Action |
|---|---|---|
| Space | Command-Space | Show or hide the Spotlight search field. |
|  | Shift-Command-Space | Varies. |
|  | Option-Command-Space | Show the Spotlight search results window. |
|  | Control-Command-Space | Show the Special Characters window. |
| Tab | Shift-Tab | Navigate through controls in a reverse direction. |
|  | Command-Tab | Move forward to the next most recently used app in a list of open apps. |
|  | Shift-Command-Tab | Move backward through a list of open apps (sorted by recent use). |
|  | Control-Tab | Move focus to the next group of controls in a dialog or the next table (when Tab moves to the next cell). |
|  | Control-Shift-Tab | Move focus to the previous group of controls. |
| Esc | Esc | Cancel the current action or process. |
| Esc | Option-Command-Esc | Open the Force Quit dialog. |
| Eject | Control-Command-Eject | Quit all apps (after changes have been saved to open documents) and restart the computer. |
|  | Control-Option-Command-Eject | Quit all apps (after changes have been saved to open documents) and shut the computer down. |
| F1 | Control-F1 | Toggle full keyboard access on or off. |
| F2 | Control-F2 | Move focus to the menu bar. |
| F3 | Control- F3 | Move focus to the Dock. |
| F4 | Control-F4 | Move focus to the active (or next) window. |
|  | Control-Shift-F4 | Move focus to the previously active window. |
| F5 | Control-F5 | Move focus to the toolbar. |
|  | Command-F5 | Turn VoiceOver on or off. |
| F6 | Control-F6 | Move focus to the first (or next) panel. |
|  | Control-Shift-F6 | Move focus to the previous panel. |
| F7 | Control-F7 | Temporarily override the current keyboard access mode in windows and dialogs. |
| F8 |  | Varies. |
| F9 |  | Varies. |
| F10 |  | Varies. |
| F11 |  | Show desktop. |
| F12 |  | Hide or display Dashboard. |
| Grave accent (`) | Command-Grave accent | Activate the next open window in the frontmost app. |
|  | Shift-Command-Grave accent | Activate the previous open window in the frontmost app. |
|  | Option-Command-Grave accent | Move focus to the window drawer. |
| Hyphen (-) | Command-Hyphen | Decrease the size of the selection. |
|  | Option-Command-Hyphen | Zoom out when screen zooming is on. |
| Left bracket ({) | Command-Left bracket | Left-align a selection. |
| Right bracket (}) | Command-Right bracket | Right-align a selection. |
| Pipe (\|) | Command-Pipe | Center-align a selection. |
| Colon (:) | Command-Colon | Display the Spelling window. |
| Semicolon (;) | Command-Semicolon | Find misspelled words in the document. |
| Comma (,) | Command-Comma | Open the app’s settings window. |
|  | Control-Option-Command-Comma | Decrease screen contrast. |
| Period (.) | Command-Period | Cancel an operation. |
|  | Control-Option-Command-Period | Increase screen contrast. |
| Question mark (?) | Command-Question mark | Open the app’s Help menu. |
| Forward slash (/) | Option-Command-Forward slash | Turn font smoothing on or off. |
| Equal sign (=) | Shift-Command-Equal sign | Increase the size of the selection. |
|  | Option-Command-Equal sign | Zoom in when screen zooming is on. |
| 3 | Shift-Command-3 | Capture the screen to a file. |
|  | Control-Shift-Command-3 | Capture the screen to the Clipboard. |
| 4 | Shift-Command-4 | Capture a selection to a file. |
|  | Control-Shift-Command-4 | Capture a selection to the Clipboard. |
| 8 | Option-Command-8 | Turn screen zooming on or off. |
|  | Control-Option-Command-8 | Invert the screen colors. |
| A | Command-A | Select every item in a document or window, or all characters in a text field. |
|  | Shift-Command-A | Deselect all selections or characters. |
| B | Command-B | Boldface the selected text or toggle boldfaced text on and off. |
| C | Command-C | Copy the selection to the Clipboard. |
|  | Shift-Command-C | Display the Colors window. |
|  | Option-Command-C | Copy the style of the selected text. |
|  | Control-Command-C | Copy the formatting settings of the selection and store on the Clipboard. |
| D | Option-Command-D | Show or hide the Dock. |
|  | Control-Command-D | Display the definition of the selected word in the Dictionary app. |
| E | Command-E | Use the selection for a find operation. |
| F | Command-F | Open a Find window. |
|  | Option-Command-F | Jump to the search field control. |
|  | Control-Command-F | Enter full screen. |
| G | Command-G | Find the next occurrence of the selection. |
|  | Shift-Command-G | Find the previous occurrence of the selection. |
| H | Command-H | Hide the windows of the currently running app. |
|  | Option-Command-H | Hide the windows of all other running apps. |
| I | Command-I | Italicize the selected text or toggle italic text on or off. |
|  | Command-I | Display an Info window. |
|  | Option-Command-I | Display an inspector window. |
| J | Command-J | Scroll to a selection. |
| M | Command-M | Minimize the active window to the Dock. |
|  | Option-Command-M | Minimize all windows of the active app to the Dock. |
| N | Command-N | Open a new document. |
| O | Command-O | Display a dialog for choosing a document to open. |
| P | Command-P | Display the Print dialog. |
|  | Shift-Command-P | Display the Page Setup dialog. |
| Q | Command-Q | Quit the app. |
|  | Shift-Command-Q | Log out the person currently logged in. |
|  | Option-Shift-Command-Q | Log out the person currently logged in without confirmation. |
| S | Command-S | Save a new document or save a version of a document. |
|  | Shift-Command-S | Duplicate the active document or initiate a Save As. |
| T | Command-T | Display the Fonts window. |
|  | Option-Command-T | Show or hide a toolbar. |
| U | Command-U | Underline the selected text or turn underlining on or off. |
| V | Command-V | Paste the Clipboard contents at the insertion point. |
|  | Shift-Command-V | Paste as (Paste as Quotation, for example). |
|  | Option-Command-V | Apply the style of one object to the selection. |
|  | Option-Shift-Command-V | Paste the Clipboard contents at the insertion point and apply the style of the surrounding text to the inserted object. |
|  | Control-Command-V | Apply formatting settings to the selection. |
| W | Command-W | Close the active window. |
|  | Shift-Command-W | Close a file and its associated windows. |
|  | Option-Command-W | Close all windows in the app. |
| X | Command-X | Remove the selection and store on the Clipboard. |
| Z | Command-Z | Undo the previous operation. |
|  | Shift-Command-Z | Redo (when Undo and Redo are separate commands rather than toggled using Command-Z). |
| Right arrow | Command-Right arrow | Change the keyboard layout to current layout of Roman script. |
|  | Shift-Command-Right arrow | Extend selection to the next semantic unit, typically the end of the current line. |
|  | Shift-Right arrow | Extend selection one character to the right. |
|  | Option-Shift-Right arrow | Extend selection to the end of the current word, then to the end of the next word. |
|  | Control-Right arrow | Move focus to another value or cell within a view, such as a table. |
| Left arrow | Command-Left arrow | Change the keyboard layout to current layout of system script. |
|  | Shift-Command-Left arrow | Extend selection to the previous semantic unit, typically the beginning of the current line. |
|  | Shift-Left arrow | Extend selection one character to the left. |
|  | Option-Shift-Left arrow | Extend selection to the beginning of the current word, then to the beginning of the previous word. |
|  | Control-Left arrow | Move focus to another value or cell within a view, such as a table. |
| Up arrow | Shift-Command-Up arrow | Extend selection upward in the next semantic unit, typically the beginning of the document. |
|  | Shift-Up arrow | Extend selection to the line above, to the nearest character boundary at the same horizontal location. |
|  | Option-Shift-Up arrow | Extend selection to the beginning of the current paragraph, then to the beginning of the next paragraph. |
|  | Control-Up arrow | Move focus to another value or cell within a view, such as a table. |
| Down arrow | Shift-Command-Down arrow | Extend selection downward in the next semantic unit, typically the end of the document. |
|  | Shift-Down arrow | Extend selection to the line below, to the nearest character boundary at the same horizontal location. |
|  | Option-Shift-Down arrow | Extend selection to the end of the current paragraph, then to the end of the next paragraph (include the paragraph terminator, such as Return, in cut, copy, and paste operations). |
|  | Control-Down arrow | Move focus to another value or cell within a view, such as a table. |

Corpus quirks are kept as-is:
- ⌘I is listed twice (Italic and Info).
- F12 "Dashboard" is legacy.
- "Left bracket ({)" labels the key with its shifted glyph.
- "Control- F3" has a stray space.

**[AI]** Map Esc and ⌘. (cancel) to **Stop generating / cancel agent**. Map ⌘Z / ⇧⌘Z to undo and redo of AI edits. ⌘, opens Settings.

### Input-source shortcuts (verbatim; for localized keyboards and input methods, not menu commands)
| Keyboard shortcut | Action |
|---|---|
| Control-Space | Toggle between the current and last input source. |
| Control-Option-Space | Switch to the next input source in the list. |
| [Modifier key]-Command-Space | Varies. |
| Command-Right arrow | Change keyboard layout to current layout of Roman script. |
| Command-Left arrow | Change keyboard layout to current layout of system script. |

**[XPLAT]** ⌘Space and ⌃Space are reserved on macOS (Spotlight and input source). Don't use Cmd/Ctrl+Space for an AI launcher; make launcher bindings configurable.

### Custom shortcuts, modifiers, order
- Add custom shortcuts **only for the most frequent app-specific commands**.
- Use modifiers as people expect:
  - ⌘-drag moves items as a group.
  - ⇧ while drag-resizing keeps the aspect ratio.
  - A held arrow nudges by the smallest app unit.
- Don't add a modifier to an existing shortcut for an **unrelated** command (⇧⌘Z must stay redo-related).
- **Don't add Shift to a key's upper character.** Help is ⌘?, not ⇧⌘/.
- The system **localizes and RTL-mirrors** shortcuts for you.
- **TIP:** some layouts need modifiers to type characters (French ⌥5 = "{"). ⌘ alone is safe. Use other modifiers only with letters.

| Modifier key | Symbol | Recommended usage |
|---|---|---|
| Command | ⌘ (outline of a stylized clover shape) | Prefer the Command key as the main modifier key in a custom keyboard shortcut. |
| Shift | ⇧ (outline of an upward-pointing arrow) | Prefer the Shift key as a secondary modifier that complements a related shortcut. |
| Option | ⌥ (horizontally transformed Z with a short top segment) | Use the Option modifier sparingly for less-common commands or power features. |
| Control | ⌃ (shallow upside-down V) | Avoid using the Control key as a modifier. The system uses Control in many systemwide features and shortcuts, like moving focus or capturing screenshots. |

(The corpus shows glyph images; the descriptions are an outline clover, an up arrow, a transformed Z, and a shallow inverted V.)

**Modifier order (mandatory): Control, Option, Shift, Command = ⌃⌥⇧⌘.**

**visionOS:**
- Holding ⌘ shows a **shortcut interface**: a flat list of available commands that have shortcuts, grouped by File / Edit / View… with no submenus. Shortcut titles must therefore be self-explanatory (`discoverabilityTitle`).
- A physical keyboard also brings up a virtual overlay with completions.

Not supported in watchOS. Change log: 2025-06-09 game bindings moved to Game controls; 2024-06-10; 2023-06-21.

**[XPLAT] Parent mapping (*derived*, not HIG):**
| Concept | macOS (HIG) | Windows / Linux / desktop web | Note |
|---|---|---|---|
| Primary modifier | ⌘ | Ctrl | Define shortcuts abstractly as `Mod+Key`. |
| Secondary | ⇧ | Shift | Same role. |
| Power / rare | ⌥ | Alt | Alt+letter on Windows triggers menu access keys, so use sparingly. |
| Control | ⌃ (avoid) | Ctrl is the *primary* | Never map Mac ⌃ to Windows Ctrl 1:1. |
| Display | Glyphs, no separators, order ⌃⌥⇧⌘ | Words joined by "+" (e.g. Ctrl+Shift+S) | Render per OS. On web, detect the platform. |
| Settings | ⌘, | Ctrl+, (convention in Electron/VS Code apps, not an OS standard) | |
| Quit | ⌘Q | Alt+F4 (Windows), Ctrl+Q (many Linux apps) | |
| Redo | ⇧⌘Z | Ctrl+Y (Windows) and/or Ctrl+Shift+Z | Support both on Windows/Linux. |
| Cancel | Esc, ⌘. | Esc | |
| Help | ⌘? | F1 | |
| Hide app | ⌘H | No equivalent | |
| Desktop web | — | Browser reserves Ctrl/⌘ +W/T/N/L/R/Q and others | A web app can't reliably override these, so pick non-colliding bindings. |

---

## 1.2 Pointing devices `[hig:pointing-devices]`
A trackpad or mouse is core on Mac, where it pairs with the keyboard. On iPad and Vision Pro it is **additive** and doesn't replace touch, eyes or gestures. Not supported in tvOS or watchOS.

**Rules**
- Match system gesture behaviour (e.g. Swipe between pages). **Never redefine systemwide trackpad gestures** (Dock, Mission Control); users can customize them.
- Keep the experience consistent across gesture, eyes, pointer and keyboard, including **modifier behaviour** (Option-drag duplicates whether by touch or pointer).
- **Pointer reveals and hides auto-minimized controls**, e.g. the minimized Safari toolbar or video controls.

### iPadOS pointer
- **Band selection** (iPadOS 15+): click-drag draws a rectangle. Standard non-list collections support it; custom views need `UIBandSelectionInteraction`.
- Distinguish pointer from finger only when it adds value, e.g. precise seek on a scrubber.
- **Default shape is a circle.** It morphs to system or custom shapes, e.g. an **I-beam over text**.

**Content effects (*derived*)**
| Effect | Behaviour | System default on |
|---|---|---|
| Highlight | Pointer becomes a translucent rounded-rect background behind the control, with gentle parallax. | Bar buttons, tab bars, segmented controls, edit menus |
| Lift | Pointer fades beneath the element. The element scales up, gains a shadow below and a soft specular highlight on top, with subtle parallax. Reads as floating. | App icons, Control Center buttons |
| Hover | Generic custom **scale, tint, shadow** values. Doesn't transform the pointer shape. | Custom / large elements |

**Choosing an effect:**
- **Highlight** for small elements with a transparent background.
- **Lift** for small elements with an opaque background.
- **Hover** for large elements, with custom scale, tint and shadow.

**Pointer accessories:** small secondary indicators that combine with any pointer, such as resize arrows (`UIPointerAccessory`). Keep their images simple. Animate accessory changes to show state, e.g. `plus` to `circle.slash` when an action becomes unavailable.

**Magnetism:**
- The pointer starts morphing as soon as it enters an element's **hit region**, which extends past the visible edge, so the element seems to pull the pointer.
- On a **flick**, the system projects the trajectory and snaps to the likely target's center.
- Applies by default to **lift and highlight** elements, **not hover** elements (no shape change, so snapping would feel out of control).
- Also applies to text areas, to stop line-skipping during selection.

**Hit regions (numbers):**
- Pad about **12 pt around bezeled elements** and about **24 pt around non-bezeled elements** (symbols, borderless buttons).
- Too small demands precision; too large makes the pointer "sticky".
- **Make adjacent bar-button hit regions contiguous**, so the pointer doesn't flicker back to a circle between them.
- Give the **corner radius** for non-standard lift shapes (`UIPointerShape.roundedRect(_:radius:)`).

**Customizing:**
- Use system effects for custom elements that behave like standard ones; a custom toolbar without highlight looks broken.
- Be consistent across the app. No gratuitous or decorative effects.
- Keep custom shapes simple.
- Useful **annotations** are fine (X/Y over a graph; Keynote's W×H while resizing). **Never put instructional text on the pointer.**
- Scale only when there's room (not table rows; use tint there). **Shadow without scale doesn't work.**

**[XPLAT]** Phones (iOS, Android) have no hover, so never use hover-only affordances. On web, gate hover with `@media (hover: hover)`. Morphing and magnetism are iPad-only. Define one parent "hover" token set (tint, plus optional scale with shadow).

### macOS clicks and gestures (verbatim)
| Click or gesture | Expected behavior | Mouse | Trackpad |
|---|---|---|---|
| Primary click | Select or activate an item, such as a file or button. | ● | ● |
| Secondary click | Reveal contextual menus. | ● | ● |
| Scrolling | Move content up, down, left, or right within a view. | ● | ● |
| Smart zoom | Zoom in or out on content, such as a web page or PDF. | ● | ● |
| Swipe between pages | Navigate forward or backward between individually displayed pages. | ● | ● |
| Swipe between full-screen apps | Navigate forward or backward between full-screen apps and spaces. | ● | ● |
| Mission Control (double-tap the mouse with two fingers or swipe up on the trackpad with three or four fingers) | Activate Mission Control. | ● | ● |
| Lookup and data detectors (force click with one finger or tap with three fingers) | Display a lookup window above selected content. |  | ● |
| Tap to click | Perform the primary click action using a tap rather than a click. |  | ● |
| Force click | Click then press firmly to display a Quick Look window or lookup window above selected content. Apply a variable amount of pressure to affect pressure-sensitive controls, such as variable speed media controls. |  | ● |
| Zoom in or out (pinch with two fingers) | Zoom in or out. |  | ● |
| Rotate (move two fingers in a circular motion) | Rotate content, such as an image. |  | ● |
| Notification Center (swipe from the edge of the trackpad) | Display Notification Center. |  | ● |
| App Exposé (swipe down with three or four fingers) | Display the current app’s windows in Exposé. |  | ● |
| Launchpad (pinch with thumb and three fingers) | Display the Launchpad. |  | ● |
| Show Desktop (spread with thumb and three fingers) | Slide all windows out of the way to reveal the desktop. |  | ● |

Users can customize the secondary-click region and finger combinations.

**[XPLAT]** Every context menu must open by right-click (Mac also ⌃-click; Windows also Shift+F10 / Menu key), by **touch-and-hold** on touch, and by keyboard.

### macOS standard pointers (verbatim; image column condensed)
| Pointer (image) | Name | Meaning | AppKit API |
|---|---|---|---|
| Diagonal arrow up-left | Arrow | Standard pointer for selecting and interacting with content and interface elements. | arrow |
| Closed gloved hand | Closed hand | Dragging to reposition the display of content within a view—for example, dragging a map around in Maps. | closedHand |
| Arrow + small menu square | Contextual menu | A contextual menu is available for the content below the pointer. This pointer is generally shown only when the Control key is pressed. | contextualMenu |
| Plus | Crosshair | Precise rectangular selection is possible, such as when viewing an image in Preview. | crosshair |
| Arrowhead + circled X | Disappearing item | A dragged item will disappear when dropped. If the item references an original item, the original is unaffected. For example, when dragging a mailbox out of the favorites bar in Mail, the original mailbox isn’t removed. | disappearingItem |
| Arrowhead + circled plus | Drag copy | Duplicates a dragged—not moved—item when dropped into the destination. Appears when pressing the Option key during a drag operation. | dragCopy |
| Curved arrow up-right | Drag link | During a drag and drop operation, creates an alias of the selected file when dropped. The alias points to the original file, which remains unmoved. Appears when pressing the Option and Command keys during a drag operation. | dragLink |
| Opposing vertical braces | Horizontal I beam | Selection and insertion of text is possible in a horizontal layout, such as a TextEdit or Pages document. | iBeam |
| Open gloved hand | Open hand | Dragging to reposition content within a view is possible. | openHand |
| Arrowhead + do-not-enter | Operation not allowed | A dragged item can’t be dropped in the current location. | operationNotAllowed |
| Gloved hand, index finger extended | Pointing hand | The content beneath the pointer is a URL link to a webpage, document, or other item. | pointingHand |
| Bar + down arrow | Resize down | Resize or move a window, view, or element downward. | resizeDown |
| Bar + left arrow | Resize left | Resize or move a window, view, or element to the left. | resizeLeft |
| Bar + left/right arrows | Resize left/right | Resize or move a window, view, or element to the left or right. | resizeLeftRight |
| Bar + right arrow | Resize right | Resize or move a window, view, or element to the right. | resizeRight |
| Bar + up arrow | Resize up | Resize or move a window, view, or element upward. | resizeUp |
| Bar + up/down arrows | Resize up/down | Resize or move a window, view, or element upward or downward. | resizeUpDown |
| Opposing horizontal braces | Vertical I beam | Selection and insertion of text is possible in a vertical layout. | iBeamCursorForVerticalLayout |

**[XPLAT]** On Mac (and native Windows), the **pointing hand is for links only**; buttons keep the arrow. Web design systems often use `cursor:pointer` on every clickable. The parent system must decide; suggestion: arrow for buttons in native shells, hand for links everywhere.

**visionOS:**
- Pointer and keyboard work alongside eyes and hands, with no app code needed. Looking at an element and then moving the pointer focuses that element.
- **Gaze sets the pointer's context**, e.g. which window it acts in.
- The pointer hides while gesturing and reappears where the person is looking.

Change log: 2023-06-21 visionOS.

---

## 1.3 Gestures `[hig:gestures]`
**Rules**
- Offer alternatives: voice, keyboard, Switch Control.
- Keep familiar gestures for familiar actions. **Don't use tap or swipe for app-unique actions, and don't invent gestures for standard ones.**
- Respond immediately and show the extent of movement needed.
- **Make unavailability obvious**: a locked object, a clearly disabled button.

**Custom gestures**
- Use only for frequent, specialized tasks (games, drawing).
- They must be **discoverable, straightforward, distinct, and never the only way**.
- Teach them in context. If they're hard to describe, they're too hard.
- **Shortcut gestures supplement standard controls.** Edge-swipe back coexists with a top-toolbar **Back button**.
- Don't conflict with system gestures. Games and immersive experiences may **defer** them.

**iOS / iPadOS extras (verbatim)**
| Gesture | Common action |
|---|---|
| Three-finger swipe | Initiate undo (left swipe); initiate redo (right swipe). |
| Three-finger pinch | Copy selected text (pinch in); paste copied text (pinch out). |
| Four-finger swipe (iPadOS only) | Switch between apps. |
| Shake | Initiate undo; initiate redo. |

Allow simultaneous recognition mainly in games (joystick plus fire).

**macOS:** keyboard and mouse first; gestures on Magic Trackpad / Magic Mouse. **tvOS:** standard gestures via remote or controller.

**visionOS**
- **Indirect** (look, then pinch-tap with hands at rest): prefer for UI; comfortable at any distance.
- **Direct** (touch the object): best within reach and for **infrequent** use, because of arm fatigue. All standard gestures have direct versions.

| Direct gesture | Common use |
|---|---|
| Touch | Directly select or activate an object. |
| Touch and hold | Open a contextual menu. |
| Touch and drag | Move an object to a new location. |
| Double touch | Preview an object or file; select a word in an editing context. |
| Swipe | Reveal actions and controls; dismiss views; scroll. |
| With two hands, pinch and drag together or apart | Zoom in or out. |
| With two hands, pinch and drag in a circular motion | Rotate an object. |

- Support tap everywhere. Offer both indirect and direct where possible.
- **Don't require specific body movements or positions.**
- **Custom gestures:**
  - Require a Full Space and hand-tracking permission.
  - Prioritize comfort: no raised arms, no repetitive motion.
  - Give two-hand or multi-finger gestures a low-effort alternative.
  - **Never require a specific hand.**
- **System overlays (visionOS 2+):**
  - Looking at the palm and gesturing opens Home and Control Center. This replaces visionOS 1's look-up, which remains as an accessibility setting.
  - Keep content out of the area around the hand; don't anchor content to hands or wrists.
  - Avoid **hand/wrist/forearm roll** gestures, which are reserved.
  - Immersive apps may **defer** the overlay so it needs a tap first (`persistentSystemOverlays`). Apps built for visionOS 1 defer by default.

**watchOS double tap (11+)**
- Scrolls lists and advances vertical tabs.
- Apps may set one button or toggle as the **primary action** (in the app, a widget, or a Live Activity in the Smart Stack).
- In notifications it triggers the first non-destructive action.
- Don't set a primary action in views with lists, scroll views or vertical tabs. Pick the most-used button (e.g. play/pause).

**Standard gestures (verbatim)**
| Gesture | Supported in | Common action |
|---|---|---|
| Tap | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Activate a control; select an item. |
| Swipe | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Reveal actions and controls; dismiss views; scroll. |
| Drag | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Move a UI element. |
| Touch (or pinch) and hold | iOS, iPadOS, tvOS, visionOS, watchOS | Reveal additional controls or functionality. |
| Double tap | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Zoom in; zoom out if already zoomed in; perform a primary action on Apple Watch Series 9 and Apple Watch Ultra 2. |
| Zoom | iOS, iPadOS, macOS, tvOS, visionOS | Zoom a view; magnify content. |
| Rotate | iOS, iPadOS, macOS, tvOS, visionOS | Rotate a selected item. |

(The page refers to a list of indirect gestures under "Specifications"; only this table exists.)

**[XPLAT]**
- Back: iOS uses a top-leading Back button plus an edge swipe; Android uses system Back. Define a per-platform back model.
- 3-finger undo and shake have no Android or web equivalent, so always show a visible Undo. **[AI]** This suits AI edits.
- Touch-and-hold for menus ≈ Android long-press.

Change log: 2024-09-09 visionOS overlays; 2023-09-15 watch double tap; 2023-06-21 renamed from Touchscreen gestures, visionOS added.

---

## 1.4 Focus and selection `[hig:focus-and-selection]`
Focus shows what a remote, controller or keyboard targets.
- Focus often also selects, unless that would cause a disruptive context shift (tvOS needs a separate press).
- iPadOS and macOS show a **ring or highlight**; tvOS shows **parallax and elevation**.
- Not supported in iOS or watchOS.

**Rules**
- **Use system focus effects**; customize only if unavoidable.
- **Never move focus without user action.**
  - Exception: with a discrete directional input, if the focused item disappears, move focus to a neighbour. Otherwise hide the indicator.
  - **[AI]** Streaming tokens, new messages and agent results must never steal focus from the composer.
- Platform scope:
  - iPadOS and macOS: focus only **content** (lists, text and search fields); Full Keyboard Access covers controls.
  - tvOS: make **every** element focusable.
- iPadOS/macOS lists: focused row = **white text on an accent background**; unfocused selection = standard text on **gray**.
- **Use a focus ring for text and search fields, and a full-row highlight for lists and collections.**

**iPadOS 15+ focus groups**
- **Tab** moves between groups (sidebar, grid, list); **arrows** move within a group.
- Group order is leading→trailing, then top→bottom. Fix custom order with `focusGroupIdentifier`.
- Each group has a **primary item** that gets focus first (`UIFocusGroupPriority`).
- The **halo** (focus ring) follows the item's shape and can be tuned to corner radius or a Bézier path. Keep it unclipped and under badges (`UIFocusHaloEffect`).
- The accent-text *highlighted* appearance is **not** a focus effect.

**[XPLAT]** This model matches WAI-ARIA roving tabindex and Windows lists. Adopt it as the parent focus model, **plus** a Tab stop on every control and a visible ring (WCAG 2.4.7 / 2.4.13) on web, Windows and Linux.

**tvOS**
- In full-screen content, gestures act on the content, not on focus.
- **Avoid pointers.** If one is needed, make it highly visible.
- Focused items scale up, so supply larger assets and leave room around them.

Five focus states (names from alt text):
| State | Description |
|---|---|
| Unfocused | The viewer hasn’t brought focus to the item. Unfocused items appear less prominent than focused items. |
| Focused | The viewer brings focus to the item. A focused item visually stands out from the other onscreen content through elevation to the foreground, illumination, and animation. |
| Highlighted | The viewer chooses the focused item. A focused item provides instant visual feedback when people choose it. For example, a button might briefly invert its colors and animate before it transitions to its selected appearance. |
| Selected | The viewer has chosen or activated the item in some way. For example, a heart-shaped button that people can use to favorite a photo might appear filled in the selected state and empty in the deselected state. |
| Unavailable | The viewer can’t bring focus to the item or choose it. An unavailable item appears inactive. |

**visionOS** uses the same keyboard/controller focus system. Gaze *hover* is separate. Change log: 2023-10-24; 2023-06-21.

---

## 1.5 Eyes (visionOS) `[hig:eyes]`
Looking at an element shows a **hover effect**, which confirms the target for an indirect tap. Components can auto-expand (tab-bar labels, tooltips).

**Privacy (IMPORTANT):** apps are **never told where people look** before they tap. **[AI][XPLAT]** No gaze analytics and no gaze-triggered logic.

**Rules**
- Always offer multiple input methods.
- Keep primary content in the field of view. Avoid rapid eye travel across wide areas or depths.
- Place content **≥ 1 m away** for sustained reading; closer only briefly.
- Prefer standard components, which give consistent hover feedback.

**Spacing (numbers):**
- Leave **≥ 16 pt margin around each interactive item**, **or** keep item centers **≥ 60 pt apart**. This compensates for involuntary eye micro-movements.
- From `designing-for-games`: buttons **60×60 pt** default, **28×28 pt** minimum.

**Visual design for gaze:**
- Minimize noise and motion, especially peripheral. Content revealed near a gazed button pulls the eye away.
- **No repeating pattern or texture filling the field of view** (it causes depth illusions).
- Use gentle cues (center position, motion, contrast, colour, scale) to suggest the likely target.
- **Prefer rounded shapes**; corners pull the gaze away from the center.
- Give multi-element components **one containing hover region**.

**Custom hover effects (2024):**
- Define two states. The system runs the effect **out of process**, so the app never knows when it is shown.
- Use sparingly, for special moments.
- Delay:
  - **none** (default): subtle or inviting cues, e.g. a slider knob;
  - **short**: e.g. tab-bar expansion;
  - **long**: extra info, e.g. tooltips.
- Keep at least one primary view constant. Test on device.

Change log: 2024-06-10 custom hover; 2024-03-29; 2023-10-24; 2023-06-21 new.

---

## 1.6 Apple Pencil and Scribble `[hig:apple-pencil-and-scribble]`
**iPadOS only.** Pencil = pixel-precise marking plus UI control. Scribble = private, on-device handwriting-to-text in any text field.

**Rules**
- Support natural pen behaviours, such as margin notes.
- **Every control must respond to Pencil**, so people never switch to a finger. Scribble is Pencil-only.
- **Ink immediately on contact**: no mode or button first.
- Map **altitude (tilt), pressure, azimuth and barrel roll** to stroke properties; pressure maps to continuous properties (opacity, size).
- Give direct feedback, with no remote effects.
- Support **left and right hands**: keep controls where neither hand covers them, and allow repositioning.

**Hover:**
- Preview the mark (size, colour), but **don't vary the preview with height**.
- **Never act on hover.**
- Preview a **mid-range** dynamic value; extremes occlude or vanish.
- Show menus near the tip, on hover plus squeeze or a modifier key.
- Show hover previews **for Pencil only, not the pointer**.

**Double tap:**
- Honour the system setting (eraser toggle by default; previous tool; colour picker; off).
- Custom modes must be explicit, discoverable and **off by default**.
- **Never modify content or destroy anything** with it.

**Squeeze (Pencil Pro):**
- Only works with the screen on and the Pencil not touching it. Users may remap it to an App Shortcut.
- Treat it as **one discrete action**.
- Show UI **near the tip**.
- Keep it non-destructive and undoable.

**Barrel roll:** modifies marking only (e.g. highlighter angle). Never use it for navigation or UI.

**Scribble:**
- Works in all standard text inputs except passwords. Custom fields must not need a tap first.
- Enable it wherever writing feels natural, even outside fields (`UIIndirectScribbleInteraction`).
- **No autocompletion while writing.** **[AI]** Suppress ghost-text AI suggestions.
- Hide the placeholder on the first stroke.
- Keep the field **stationary**; defer moves and resizes until a pause.
- **No autoscroll.**
- Enlarge the field before writing or during pauses, never mid-stroke.

**PencilKit:**
- Dark Mode colour adaptation is on by default; **turn it off when drawing over PDFs or photos**.
- In compact width the tool picker has no undo/redo, so add them to the toolbar. Support **3-finger undo**.

Change log: 2024-05-07 squeeze and barrel roll; 2023-09-12; 2022-11-03 hover. WWDC26 PencilKit / PaperKit videos.

**[XPLAT]** Web Pointer Events (`pen`, `pressure`, `tiltX/Y`, `twist`) and Android styluses support the same rules.

---

## 1.7 Game controls `[hig:game-controls]`
Controllers work everywhere except watchOS. Always also support the platform's default input.

**Touch controls (iOS/iPadOS, Touch Controller framework)**
- Prefer direct manipulation of game objects to overlay buttons.
- **Placement:**
  - Respect safe areas, the Home indicator and the Dynamic Island.
  - Put frequent buttons by the thumbs, outside the move and camera circles.
  - Put **menus at the top**.
- **Sizes:** frequent controls **≥ 44×44 pt**; less important controls (menus) **≥ 28×28 pt**.
- **Visible and tactile press states:** a glow visible around the finger, plus sound and haptics.
- **Symbols describing the action, not "A/X/R1".**
- Show and hide controls by context.
- Combine actions into one control (tap vs hold; walk/sprint).
- **Left = move, right = camera.** Use a **floating thumbstick** where the thumb lands; pan the camera by direct touch.

**Physical controllers**
- Always provide a default-input fallback.
- tvOS and visionOS may *require* a controller (App Store badge). Detect one and prompt gracefully.
- Detect pairing automatically. Use the **connected controller's** labels and glyphs; prefer SF Symbols over text.
- Support multiple controllers.

| Button | Expected behavior for UI |
|---|---|
| A | Activates a control |
| B | Cancels an action or returns to previous screen |
| X | — |
| Y | — |
| Left shoulder | Navigates left to a different screen or section |
| Right shoulder | Navigates right to a different screen or section |
| Left trigger | — |
| Right trigger | — |
| Left/right thumbstick | Moves selection |
| Directional pad | Moves selection |
| Home/logo | Reserved for system controls |
| Menu | Opens game settings or pauses gameplay |

**Keyboards (games)**
- Prefer **single-key** bindings (I = Inventory, M = Map, Space = main action).
- On Apple keyboards, **remap ⌃ to ⌘** (it sits next to Space for WASD play).
- Cluster related keys.
- Allow rebinding.

**visionOS:** spatial controllers (PS VR2 Sense) mirror hands: look plus trigger = indirect; reach plus trigger = direct.

Change log: 2025-06-09; 2024-06-10 renamed from Game controllers.

**[XPLAT]** The A = confirm / B = back convention matches Xbox. Nintendo's layout swaps positions, hence "use the connected controller's labels". ⌃→⌘ remapping is Mac-only.

---

## 1.8 Remotes (tvOS) `[hig:remotes]`
The Siri Remote clickpad and touch surface is the primary tvOS input.
- Use standard gestures; move focus in the gesture's direction.
- Give feedback (a resting thumb hints at swipe-down for info).
- Use custom gestures mainly in games.
- **Press = intentional** (choose, confirm). **Tap = navigation or info only.** Ignore stray taps, especially during live video.
- Use positional taps only where intuitive.
- **Back opens the hierarchical *parent*, not necessarily the previous screen.**
  - At top level, Back goes to Home.
  - In gameplay, Back opens a pause menu, and Back again resumes.
  - Press-and-hold Back goes Home from anywhere.
- Play/Pause controls playback.
- Swipe is inertial; an edge swipe moves fast; press-then-swipe scrubs.

| Button or area | Expected behavior in an app | Expected behavior in a game |
|---|---|---|
| Touch surface (swipe) | Navigates. Changes focus. | Performs directional pad behavior. |
| Touch surface (press) | Activates a control or an item. Navigates deeper. | Performs primary button behavior. |
| Back | Returns to previous screen. Exits to Apple TV Home Screen. | Pauses/resumes gameplay. Returns to previous screen, exits to main game menu, or exits to Apple TV Home Screen. |
| Play/Pause | Activates media playback. Pauses/resumes media playback. | Performs secondary button behavior. Skips intro video. |

**Compatible remotes:** guide/browse buttons open your EPG; page up/down pages the EPG while browsing and changes channel during playback. Without an EPG, the system routes these buttons to the default guide app.

**[XPLAT]** Hierarchical Back ≈ Android's Up-vs-Back distinction.

## 1.9 Digital Crown `[hig:digital-crown]`
**Vision Pro (system only; apps get no data):** volume, immersion level, recentering, Accessibility, exit to Home.

**Watch:**
- From watchOS 10 the crown is the **primary navigation input**: Smart Stack, Home Screen, vertical tabs, lists.
- **Apps never receive presses.**
- Linear haptic **detents** by default; tables can detent per row.

**Rules**
- Anchor navigation to the crown, with touch backups.
- Use it to inspect data where no navigation is needed (World Clock time scrub).
- Always give visual feedback.
- Match update rate to turn speed.
- Disable detents if they clash with your animation. Use linear detents for uneven row heights.

Not supported in iOS, iPadOS, macOS or tvOS.

## 1.10 Action button `[hig:action-button]`
Hardware button on supported iPhone and Watch (Ultra: workouts and dives). It runs App Shortcuts or system functions. Not supported in iPadOS, macOS, tvOS or visionOS.

**Rules**
- Offer **essential functions**. Don't add "open app"; the system provides it.
- **Labels:** title case, start with a verb, present tense, no articles or prepositions, **≤ 3 words** ("Start Race").
- Let the system teach configuration.
- **iOS:** act without leaving context, via a Live Activity or snippet ("Set Timer" asks for a duration and starts a Live Activity). **[AI]** Use this model for quick agent intents with progress in a Live Activity.
- **watchOS:**
  - Allow at most one secondary press that advances the task.
  - Use extra presses to add functions, not to stop; put Stop in the UI.
  - **Action + side button = pause**, unless pausing is unsafe (diving).

Change log: 2023-09-12 iOS; 2022-09-14 new.

## 1.11 Camera Control `[hig:camera-control]`
iPhone 16-series hardware control; iOS only.
- **Gestures:** light press opens the overlay from the bezel; light double-press lists controls; slide to adjust.
- **Control types:** **slider** (range) and **picker** (discrete), plus optional system **zoom** and **exposure**.

**Rules**
- **SF Symbols only** (no custom symbols); symbols don't show state.
- Short names; they follow Dynamic Type.
- Show **units** (EV, %).
- Define **prominent values** that sliders snap to.
- Keep your UI out of the overlay area in both orientations, and maximize the viewfinder.
- Don't duplicate controls.
- Enable or disable controls per mode; you **can't add or remove them at runtime**.
- Put the most-used controls in the middle; the system remembers the last-used one.
- Offer a **locked camera capture extension**.

New 2024-09-09.

## 1.12 Gyroscope and accelerometer `[hig:gyro-and-accelerometer]`
Available on iOS, iPadOS and watchOS, plus the Siri Remote gyro.
- Use motion only for tangible benefit.
- **You must supply purpose copy for the permission prompt.** **[AI]** Use the same explained, just-in-time permission pattern everywhere.
- **Outside gameplay, never use motion for direct UI manipulation**: it is imprecise, inaccessible and drains battery.

## 1.13 Nearby interactions `[hig:nearby-interactions]`
Ultra Wideband (U1) distance and direction. Needs permission and uses **session-scoped random device IDs**.

**Rules**
- Use physical-world metaphors (bring devices together to hand off).
- Use distance, direction and context (the share sheet suggests the nearest contact you're facing).
- Feedback **sharpens with proximity** (arrow → pulsing circle) and must be **continuous**.
- Blend visual, audio and haptic feedback: visual when looking at the screen, audio and haptic when looking at the surroundings.
- **Never the only way.**

**Device usage**
- Nudge people toward **portrait** implicitly.
- The sensor's field of view ≈ the Ultra Wide camera (iPhone 11+). Outside it you get distance only.
- Teach that bodies and objects in between degrade accuracy.

**Platforms:** iOS gives distance and direction. watchOS gives distance only, and the app must be in the foreground. Not supported in macOS, tvOS or visionOS. Renamed from Spatial interactions on 2023-06-21.

---

# PART 2 — GETTING STARTED / PLATFORMS

## 2.0 Getting started `[hig:getting-started]`
"Create an app or game that feels at home on every platform you support." It now indexes 9 pages:
- **Design principles [NEW]**
- iOS, iPadOS, macOS, tvOS, visionOS, watchOS, games
- **iPhone Duo [NEW]**

## 2.1 Design principles `[hig:design-principles]` **[NEW — "Reintroduced design principles", 2026-06-08]**
Principles are "tools to help you weigh competing priorities", not rules, and "there's no one right way to apply" them. There are eight, each with a symbol, a one-line imperative and 2–4 sub-rules. WWDC26 session: "Principles of great design". This is a standalone principles page again (absent since the 2022 restructure) and distinct from Liquid Glass's 2025 "hierarchy/harmony/consistency".

| # | Principle | Imperative | Sub-rules (condensed) |
|---|---|---|---|
| 1 | **Purpose** | Make something meaningful. | **Create value**: keep asking what the product is for and whether the design serves it. **Keep focused**: prioritize the most important features and make them great. **Find new ways to solve the problem**: don't re-create existing solutions; define what sets you apart. |
| 2 | **Agency** | Let people do things their own way. | **Stay out of the way**: take people straight to the task; be unobtrusive but present. **Freedom to explore**: no lock-in to flows or modes; guided flows must be easy to skip or escape. **Help people recover from mistakes**: build in forgiveness, make reversal easy, and never cost people time or work. |
| 3 | **Responsibility** | Act in people's best interest. | **Be fully transparent** about what the product does and why from the first interaction; give a clear rationale for permissions; say what data you collect and how it is used. **Keep information safe**: collect only what you need, anticipate misuse, and build protections against abuse and unintended consequences. |
| 4 | **Familiarity** | Build on what people know. | **Use known concepts** from the real world and other software. **Keep visuals and interactions consistent** once established. **Provide clear feedback**: show when controls are available, signal content changes, and use system patterns for alerts and choices. |
| 5 | **Flexibility** | Adapt to diverse contexts and needs. | **Design for everyone**: accessibility as a priority from the start. **Preserve a person's context**: keep content and controls in consistent, predictable positions across platforms and configurations, with natural transition animations. **Consider a variety of inputs**: voice, touch, keyboard and more. **Approach every platform with intention**: give each the same care. |
| 6 | **Simplicity** | Be clear and direct. | **Include just what's necessary**: "Simplicity isn't minimalism"; keep important things close and let the rest fall away. **Be concise**: exactly the words needed. **Establish hierarchy**: recognizable controls and consistent structure show where you are and what comes next. |
| 7 | **Craft** | Care about every detail. | **Quality sets the tone**: visuals, animation, wording, audio. **Experiment and iterate**: prototype early, discard freely, test in real-world settings for durability and performance. **Maintain your craft**: shipping isn't the finish line; keep current with platform capabilities. |
| 8 | **Delight** | Make it human. | **Identify the emotion** to inspire (energize, calm, thrill). **Create defining moments**, even in a button press or error message. **Don't mistake delight for decoration**: never at the expense of the core task. **Consider the whole**: delight is the sum of freedom to act, safety to explore, familiar metaphors and flexible context transitions. |

**[AI]** **Agency** and **Responsibility** are the trust backbone:
- Visible agent state.
- Cheap undo and checkpoints.
- Skippable guided flows.
- A rationale before every permission.
- Transparent data use.
- Anticipating misuse.

Other principles map to AI design too:
- "Simplicity isn't minimalism" = progressive disclosure, not hidden power.
- "Preserve a person's context" = composer, stop button and model picker in stable positions across breakpoints.

**[XPLAT]** The principles are platform-neutral. Adopt the 8-axis structure (reworded) for the parent system's principles page.

## 2.2 Platform characteristics (*derived* from the six platform pages)
| Platform | Display | Ergonomics / viewing distance | Primary inputs | Session pattern | Key system features |
|---|---|---|---|---|---|
| iOS | Medium, high-res | Handheld, 1–2 hands, portrait ↔ landscape; **≤ 1–2 ft** | Multi-Touch, virtual keyboard, voice; motion, personal data, nearby interactions | 1–2 min checks to 1 h+; frequent app switching | Widgets, Home Screen quick actions, Spotlight, Shortcuts, activity views |
| iPadOS | Large, high-res | Handheld, on a surface or stand; **≤ ~3 ft** | Touch, virtual or physical keyboard, pointer, Apple Pencil, voice — often combined | Quick actions to hours; multiple apps onscreen; drag and drop between apps | Multitasking, widgets, drag and drop |
| macOS | Large, high-res; extra displays incl. iPad | Stationary on a desk; **~1–3 ft** | Physical keyboard, pointer, game controllers, Siri | Minutes to hours of deep focus; many apps; smooth active/inactive transitions | Menu bar, file management, full screen, Dock menus |
| tvOS | Very large, high-res | Seated **≥ ~8 ft**, sometimes moving around the room | Remote, game controller, voice, companion apps | Hours-long immersion plus picture-in-picture | TV app, SharePlay, Top Shelf, TV provider accounts |
| visionOS | Infinite 3D canvas (windows, volumes, objects) | Content placed relative to the head (sitting, standing or lying); comfort is paramount; content **≥ 1 m** for reading (from `eyes`) | Eyes + indirect hand gestures; direct touch | Shared Space (multi-app) ↔ Full Space (single app, portals, worlds) | Passthrough (crown-controlled), Spatial Audio, SharePlay spatial Personas, rich accessibility |
| watchOS | Small, high-res, Always On | On the wrist, **≤ 1 ft**, other hand interacts | Digital Crown, tap/swipe/drag, Action button, Shortcuts; GPS, health sensors, altimeter, accelerometer, gyroscope | Glances under 1 min, many times a day; complications and notifications used more than the app | Complications, notifications, Always On, watch faces |

The platform pages contain **no device or screen tables**. Point sizes live on `layout` (last device additions 2025-09-09: iPhone 17 / Air / Watch S11 / Ultra 3 / SE 3), and **it does not list iPhone Duo**.

## 2.3 iOS `[hig:designing-for-ios]`
- **Limit onscreen controls.** Keep secondary actions discoverable with minimal interaction.
- Adapt to orientation, **Dark Mode** and **Dynamic Type**.
- **The middle and bottom of the screen are easiest to reach.** Support swipe-back and list-row swipe actions.
- With permission, use payments, **biometrics** and location instead of manual entry.
- No change log.

**[XPLAT]** Row swipe actions are less discoverable on Android and web; mirror them in overflow menus.

## 2.4 iPadOS `[hig:designing-for-ipados]`
- Elevate content. **Minimize modals and full-screen transitions.** Keep controls reachable but unobtrusive.
- **Size and density follow viewing distance and input mode.**
- Combine touch, keyboard, trackpad and Pencil.
- Adapt to orientation, **multitasking**, Dark Mode and Dynamic Type, and **transition effortlessly to macOS**.
- The WWDC25 video covers resizable windows, window controls, the iPad menu bar and the new pointer.

**[XPLAT]** The tablet class should share desktop patterns (sidebar, menu or command bar, pointer hover), not scaled-up phone patterns.

## 2.5 Designing for iPhone Duo `[hig:designing-for-iphone-duo]` **[NEW — 2026-09-09]**
**Device:**
- The first folding iPhone, "with a reimagined iOS" (tech talk).
- **Two displays (outer and inner), each with a front camera**, joined by a **center hinge**.
- It is still iPhone, so all iOS guidance applies. Apps built from standard, resizable components adapt "with little adjustment".
- Test in Xcode **Device Hub**.

**Dimensions: none published in the corpus** (no pt sizes, aspect ratio or hinge width). Facts available:
- The outer display is "**wider and shorter** than the display on other iPhone devices".
- **Outer = compact width; inner = regular width.**
- Calculator's grid goes from **4 columns × 5 rows** (iPhone 16 portrait) to **5 columns × 4 rows** (Duo outer), so the outer display is near-square or landscape-leaning.
- For exact metrics, use Apple Design Resources or the developer article "Preparing your app for iPhone Duo" (outside the corpus).

**Anatomy**
- **Outer display (closed):** toolbars and tab bars sit **on the side**, to maximize vertical content space.
- **Inner display, landscape:** controls stay on the side (continuity with the outer display).
- **Inner display, portrait:** tall enough for normal horizontal top and bottom bars.
- **Outer camera:** in a corner, always visible, aligned with the side controls. Expands into the **Dynamic Island**.
- **Inner camera:** under the display, hidden until active; UI moves aside when it activates.
- **Hinge:** costs space when partially folded.

**Poses:**
- Six are illustrated: "partially folded **like a book**", "**placed down on a surface**", "**standing on its edges**".
- **Don't build per-pose layouts.** Compact (outer) and regular (inner) size classes cover every pose. Let the layout **expand**, don't reinvent it.

**Best practices**
- **Build to resize.** Two displays, poses and **Split View multitasking** mean many sizes. Use size classes, layout margins and safe-area insets. **No fixed widths or display-specific code.**
- **Keep the same functionality and state on both displays.** Keep the hierarchy, optionally showing **one extra level on the inner display**. Mail: closed shows list *or* message; open shows **list + message side by side**.
- **Keep the same functionality across poses.** Items may overflow or resize but must stay reachable.
- **Follow the system's vertical bar layout.** Standard components get it automatically.
- **Games:**
  - Must be playable in every pose. Orientation lock is allowed, but **fill the screen** and keep text and control sizes constant.
  - **Change aspect ratio rather than letter- or pillarbox.** If bars are unavoidable, fill them with art.

**Reserved regions (dynamic layouts)**

| Region | Present | Behaviour |
|---|---|---|
| Outer front camera | Always; expands into the Dynamic Island for Live Activities | System accounts for it when controls are on the side |
| Inner front camera | Only while the camera is active | UI moves aside to reveal it |
| Folding region | Only when partially open | Splits the inner display into usable regions; the center is excluded |
(*derived* from the bulleted list)

- System **alerts, context menus and sheets move off the fold.**
- **Split views** rebalance column widths and margins to the inner display's symmetry.
- Custom views use `ReservedRegion` (SwiftUI) / `UIView.ReservedRegion` (UIKit). The concept is likened to iPad window controls.
- **Adapt on fold.** Notes: fully open, the list pane is **narrower** than the note; partially folded, both panes are **equal width**, one on each side.
- **Grids: use an even number of columns.**
- **Avoid extreme layout changes while folding**; prefer small shifts to rearrangement.

**Split views**
- They expand on the inner display and **collapse to one pane on the outer display**, just as regular ↔ compact does on other iPhones.
- APIs: `NavigationSplitView` / `UISplitViewController`.

**Arrangement views [NEW API]**
A container with a **primary** and a **secondary** view, arranged by size, orientation and reserved regions (`ArrangementView` / `UIArrangementViewController`).
- **Split arrangement:** splits **horizontally if wider than tall, vertically if taller than wide**. The allowed axes can be limited.
- **Overlay arrangement:**
  - Partially folded: each view takes one side of the fold.
  - Otherwise: the **primary sits atop the secondary** (diagram: a smaller, bottom-aligned primary over a full-bleed secondary).
  - The secondary can collapse.
- HStack/VStack map to split; ZStack maps to overlay.
- **Keep navigation containers outside arrangement views**, never inside.

**Vertical controls (the core Duo pattern)**
- Top and bottom bars **move to the side** (except the inner display in portrait). The trailing-edge column runs top to bottom: **Dynamic Island, status bar, toolbar (incl. navigation buttons), tab bar**.
- In Split View, each app puts controls on its **outer** edge (the left app on the left).
- Controls are **hardware-aligned**: fixed relative to the camera and **not mirrored in RTL**.

**Rules:**
- **Account for asymmetry.** Use safe areas so no controls cover content, including the other app's controls in Split View.
- **Keep relative control positions consistent across poses.**
- **Order:**
  - Top of the axis: primary navigation (**Back / Close**), then prominent actions (**Done**).
  - Other items keep their groupings. The system inserts a gap between items from the former top and bottom bars.
- **Overflow** runs **bottom → top**. Set **visibility priority** per group, then per item (`ToolbarItemVisibilityPriority` / `UIBarButtonItemVisibilityPriority`). Keep frequent actions (Compose, New Note) and **badged or status items** visible longest.
- **Don't override the default bar placement** ("one of the core patterns of iPhone Duo").
- **Full-width, bar-less layouts** suit non-scrolling, immersive UIs (Calculator) if they don't clash with the Dynamic Island or status bar. You can mix a full-bleed header with inset scrolling content.
- **Group toolbar items** (`ToolbarItemGroup` / `UIBarButtonItemGroup`). **No manual fixed spacing.**
- **Keep controls with their content.** Mail's list controls stay atop the leading pane; message controls go vertical on the trailing edge.
- Give **every non-text item a title and a symbol**. Titles are used in overflow and expanded forms.
- **Minimize text-only buttons.** Text labels force a horizontal bar.
- **Compression when space is short** (`ToolbarVerticalCompressionBehavior` / `UIVerticalBarCompressionBehavior`):
  - *Navigation-focused* (default): toolbar items go to overflow and the tab bar stays.
  - *Task-oriented*: the **tab bar minimizes** to one control and the toolbar stays.
- **Use the system overflow menu**; merge custom overflow into it. **Reserve the ellipsis for overflow.**

**Parent-system implications [XPLAT][AI]**
- Make **size class + reserved region** the mobile and tablet layout model.
  - Android equivalents: WindowSizeClass, Jetpack `FoldingFeature` (hinge bounds, FLAT / HALF_OPENED, book and tabletop postures), and Material list-detail / supporting-pane canonical layouts.
  - Arrangement view ≈ Material two-pane.
- Material's **navigation rail is leading-edge, RTL-mirrored and destinations-only**. Duo's bar is **trailing (hardware) edge, not mirrored**, and merges status, actions and tabs. Add a "bar axis" token (horizontal / vertical) with a per-platform edge rule.
- **AI chat on Duo:**
  - Closed: conversation list *or* thread.
  - Open: split.
  - The composer suits an overlay arrangement.
  - Keep Stop/Send and the model picker in stable relative positions.
  - Give "agent running" and unread badges high visibility priority.
  - Keep the composer off the fold.
- Even grid columns, no fixed widths, small shifts and title+symbol actions apply to every responsive breakpoint.

## 2.6 macOS `[hig:designing-for-macos]`
- **More content, fewer nesting levels, less modality**, at comfortable density.
- Resizable, hideable, movable windows; full-screen mode.
- **Every command in the menu bar.** **[XPLAT]** Windows and Linux use in-window menus; the web has none. Use a command-palette abstraction; **[AI]** a ⌘K palette doubles as the AI entry point.
- Pixel-precise input; keyboard shortcuts and keyboard-only workflows.
- **Personalization:** toolbars, window layouts, colours, fonts.

## 2.7 tvOS `[hig:designing-for-tvos]`
- Fluid remote gestures. **Embrace focus**: items highlight and expand.
- Edge-to-edge art and cinematic audio, legible across the room.
- **Multiuser:** easy and infrequent sign-in, shared sign-in, automatic profile switching.

Change log: 2022-09-14.

## 2.8 visionOS `[hig:designing-for-visionos]`
**Characteristics:**
- Space: windows, volumes, 3D.
- **Immersion:** Shared Space (default, multi-app) ↔ Full Space (sole app; portals and worlds).
- Passthrough, controlled with the crown.
- Spatial Audio, tuned with permission.
- Eyes and hands.
- Head-relative ergonomics.
- Accessibility: VoiceOver, Switch Control, Dwell Control, Guided Access, Head Pointer.

**Safety (IMPORTANT):** not while driving or near hazards; **ages 13+**.

**Rules**
- Embrace space, audio and immersion.
- **Use the minimum immersion each moment needs.**
- **Use windows for UI-centric tasks** (dynamic scaling keeps them legible).
- **Comfort:**
  - Content in the field of view, head-relative.
  - No jarring or frame-less motion.
  - Indirect gestures with hands at rest.
  - Direct targets near and brief.
  - Little movement in full immersion.
- SharePlay with spatial Personas.

Change log: 2024-02-02; 2023-09-12; 2023-06-21.

## 2.9 watchOS `[hig:designing-for-watchos]`
- **Glanceable, single-screen** interactions of one or two gestures.
- **Shallow hierarchy**; crown for vertical navigation.
- Proactive, on-device personalization.
- Complications and actionable notifications.
- Background **colour** for supporting info; **materials** for hierarchy.
- **The app must work independently.**

Change log: 2023-06-05. **[AI]** On Watch, AI = proactive glanceable results, not chat.

## 2.10 Designing for games `[hig:designing-for-games]`
**Getting started:**
- Playable right after install; **initial download ≤ 30 minutes**, the rest in the background.
- Smart defaults from device, accessories and accessibility settings.
- **Teach through play.** A written tutorial is a reference, not a gate.
- **Defer permissions to the moment of need**, and ratings until after real playtime. **[AI]** Same just-in-time pattern.

| Platform | Default text size | Minimum text size |
|---|---|---|
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

| Platform | Default button size | Minimum button size |
|---|---|---|
| iOS, iPadOS | 44x44 pt | 28x28 pt |
| macOS | 28x28 pt | 20x20 pt |
| tvOS | 66x66 pt | 56x56 pt |
| visionOS | 60x60 pt | 28x28 pt |
| watchOS | 44x44 pt | 28x28 pt |

**Display:**
- Use vector and resolution-independent art.
- Respect corners and camera housings via safe areas.
- **Menus must adapt to 16:10, 19.5:9 and 4:3** and both orientations. Use relative constraints, not fixed layouts.
- Design for full screen.

| Platform | Default interaction methods | Additional interaction methods |
|---|---|---|
| iOS | Touch | Game controller |
| iPadOS | Touch | Game controller, keyboard, mouse, trackpad, Apple Pencil |
| macOS | Keyboard, mouse, trackpad | Game controller |
| tvOS | Remote | Game controller, keyboard, mouse, trackpad |
| visionOS | Touch | Game controller, keyboard, mouse, trackpad, spatial game controller |
| watchOS | Touch | – |

**Input and inclusion:**
- Take care with sizing and menus when porting from pointer to touch.
- Always offer alternatives to controllers. Offer touch controls on iPhone and iPad.
- Never rely on colour alone; caption cutscenes.
- Let players personalize type size, mapping, motion and sound balance.
- Inclusive identity options; **avoid stereotypes**.

**Technologies:** Game Center, **GameSave** (cross-device saves), Core Haptics, Spatial Audio.

Change log: 2025-06-09; 2024-06-10 new.

**[XPLAT] Target sizes:**
- Apple: touch 44 / min 28 pt; Mac 28 / 20; visionOS 60 / 28 plus a 16 pt gaze margin; tvOS 66 / 56.
- Others: Material 48 dp; WCAG 2.2 24 px (AA) / 44 px (AAA); Fluent ≈ 40 epx.
- Suggested parent tokens: `target.touch 44` (48 on Android), `target.pointer 28` (min 20), `target.spatial 60`.

---

## Change-log digest
| Page | Changes |
|---|---|
| design-principles | **2026-06-08 Reintroduced design principles [NEW]** |
| designing-for-iphone-duo | **2026-09-09 New page: poses, dual-display dynamic layouts, vertical-axis bars [NEW]** |
| getting-started / inputs | Collections, no log; getting-started now lists Design principles and iPhone Duo |
| game-controls | 2025-06-09 touch, UI mapping, spatial controllers; 2024-06-10 touch, renamed |
| keyboards | 2025-06-09 game bindings moved out; 2024-06-10 games; 2023-06-21 visionOS |
| designing-for-games | 2025-06-09 touch and Game Center; 2024-06-10 new |
| gestures | 2024-09-09 visionOS overlays; 2023-09-15 watch double tap; 2023-06-21 renamed, visionOS |
| camera-control | 2024-09-09 new |
| eyes | 2024-06-10 custom hover; 2024-03-29 artwork; 2023-10-24 focus vs hover; 2023-06-21 new |
| apple-pencil-and-scribble | 2024-05-07 squeeze and barrel roll; 2023-09-12 artwork; 2022-11-03 hover |
| designing-for-visionos | 2024-02-02 user-guide link; 2023-09-12 artwork; 2023-06-21 new |
| digital-crown | 2023-12-05 no visionOS app data; 2023-06-21 visionOS; 2023-06-05 navigation |
| focus-and-selection | 2023-10-24 focus vs hover; 2023-06-21 visionOS |
| action-button | 2023-09-12 iOS; 2022-09-14 new |
| nearby-interactions | 2023-06-21 renamed from Spatial interactions |
| pointing-devices | 2023-06-21 visionOS |
| designing-for-watchos | 2023-06-05 glanceability, crown |
| designing-for-tvos | 2022-09-14 multiuser |
| remotes, gyro-and-accelerometer, designing-for-ios / ipados / macos | No log (iOS / iPadOS / macOS cite WWDC25 Liquid Glass videos) |

## Top implications for the NEAR AI parent system
1. **Shortcuts as `Mod+Key`** (⌘ on Apple, Ctrl elsewhere).
   - Apple glyphs in order ⌃⌥⇧⌘; Windows/Linux as "Ctrl+Shift+K".
   - Never repurpose standard shortcuts.
   - **Esc / ⌘.** = stop generation.
   - Avoid ⌘/Ctrl+Space and browser-reserved keys.
2. **Focus:** groups (Tab between regions, arrows within), as on iPadOS and in ARIA.
   - Every control Tab-reachable with a visible ring on web, Windows and Linux.
   - **Never move focus when AI output streams in.**
3. **Hover is enhancement only.**
   - No hover- or gaze-triggered actions.
   - Hit-region padding ~12 pt (bezeled) / ~24 pt (borderless); contiguous bar hit regions.
   - Hand cursor for links only (or an explicit web exception).
4. **Fold-aware adaptive layout** modelled on iPhone Duo:
   - size classes plus reserved regions;
   - split and overlay arrangements;
   - even columns;
   - small shifts;
   - title + symbol actions;
   - priority overflow;
   - a "bar axis" that can go vertical.
   Align with Android WindowSizeClass and FoldingFeature, except for edge and RTL rules.
5. **Adopt the 8 design principles' structure.** Agency (recoverability) and Responsibility (transparency, minimal data, harm anticipation) are the AI-trust core.
   - Size tokens: 44 / 28 / 60 pt.
   - Text minimums: 11 pt iOS, 10 pt macOS, 12 pt visionOS / watchOS.


# 6. Technologies

## 6. Technologies

The HIG has 29 technology pages. Six of them matter a lot for an AI product: Generative AI, Machine learning, Siri (rewritten for "Siri AI", June 2026), Sign in with Apple, Wallet/ID Verifier identity, and Apple In-App Purchase (subscriptions). Mac Catalyst is also covered closely because its iPad-to-Mac adaptation rules apply directly to a cross-platform system. The other pages get one line each.

Corpus search results: "Apple Intelligence" appears in app-shortcuts, generative-ai, machine-learning and siri. "Image Playground" appears in generative-ai and machine-learning. "Genmoji" and "Foundation Models" appear in generative-ai (Foundation Models also in machine-learning). "App Intents" appears in app-shortcuts, maps, siri, snippets and widgets. "Private Cloud Compute" appears in generative-ai, in a WWDC26 video blurb. "agent" appears only in generative-ai video blurbs ("Create UI prototypes using agents in Xcode"; Foundation Models "primitives for creating agentic experiences"). Passkeys appear in managing-accounts and privacy. **No HIG page covers Writing Tools or Visual Intelligence, and there is no dedicated Apple Intelligence page.** Apple Intelligence guidance is spread across Generative AI, Machine learning, Siri, App Shortcuts and Snippets.

### 6.1 Generative AI `[hig:generative-ai]` (new June 9, 2025; updated June 8, 2026) **[AI]**

The page covers using models to create and transform text, images and other content. Every rule on the page is condensed below.

**Best practices**
- **Design responsibly.** The same input can give different outputs, and you can't predict every request. Design for inclusiveness, care and privacy across all real-world inputs, not only the happy-path prototype.
- **Keep people in control.** Honor in-scope requests and handle sensitive content carefully. Let people *dismiss* unwanted generated content and *revert or retry* transformations. **Clearly identify when and where AI is used.**
- **Make it inclusive.** Models favor common data and can reproduce stereotypes. Ask people for the attributes you need (for example, when generating images of people) instead of inferring personal or cultural characteristics. Ask before assuming gender identity or relationship type. Test with diverse people.
- **Use AI only where it adds clear, specific value** (time saved, better communication, creativity). It isn't right for every situation.
- **Keep the experience working when AI is unavailable or declined.** Offer a non-AI fallback where you can; Apple's examples are regular emoji alongside Genmoji, and reading notifications without summaries.

**Transparency**
- **Disclose where the app uses AI.** Never let people think they're dealing with, or reading content written by, a human when it's AI. Follow regional disclosure regulations.
- **Set expectations about what the feature can and can't do.** Offer a brief tutorial when you introduce a feature. For open-ended inputs (a search bar or prompt), offer **curated suggestions**. State known limitations up front, show how to get good results, and explain why poor results happen (links to ML › Limitations).

**Privacy**
- **Choose the model type for privacy as well as capability.** On-device models keep data local, respond fast and work offline. Server models are for when you need more compute or a larger context. For server processing, do as much locally as possible, minimize what you send, **tell people their data may go to a server, show them what's shared, and say what may be stored off-device or used for training.**
- **Ask permission before using personal information or usage data.** Use the minimum data, always offer a clear opt-out, and get explicit consent before storing data or using it to improve the model. Understand the privacy practices of any third parties you share data with. Outputs can leak sensitive information. Apps for kids have stricter rules.
- **Disclose how the app and model use and store personal data.** Explain the benefits concisely and specifically, and **say whether personal information is used for training.**

**Models and datasets**
- Evaluate model capabilities early and hands-on (general-purpose vs task-specific). Models may be unavailable because of the device, network or battery; for example, Foundation Models needs a compatible device with Apple Intelligence turned on.
- Choose datasets deliberately: diverse representation, known provenance, proper licenses. Leave time to test for bias and misinformation.

**Inputs**
- **Guide people with diverse, predefined example inputs.**
- **Communicate that output may contain errors, and reduce hallucinations.** Scope generation tightly. Don't request factual output unless the model has verified, current data. Don't use generated content where a hallucination could misinform someone and harm them.
- **Get permission before irreversible or problematic actions.** Don't automate destructive actions (such as deleting photos) or hard-to-undo ones (such as purchases). **Ask for confirmation before any significant action on someone's behalf.** Follow model usage policies and regional AI regulations. *(This is the key rule for agentic features.)*

**Outputs**
- **Make results easy to refine or revert, and confirm when a correction has taken effect.** Put controls such as **Edit, Undo, Retry, Adjust near the generated content**, and give a clear signal when a personalization or adjustment has applied.
- **When output is blocked or poor, coach people toward a better request.** Image Playground, for example, says "Unable to use that description". Offer example requests.
- **Reduce harmful outcomes through design and adversarial testing.** Test out-of-scope, vague, ambiguous, sensitive and controversial prompts, and prompts that try to provoke harm.
- **Avoid reproducing copyrighted content.** Build on models that already protect against this, curate inputs or offer pre-approved prompts, and tell the model to avoid certain styles.
- **Design for latency.** Generative models are slow, so provide a loading experience or **generate in the background** while people use other parts of the app (see Loading).
- **Give specific, reassuring progress text** that says what is actually happening: "Summarizing key themes from your notes" instead of "Processing…". On failure, describe what happened in plain language and give a clear next step. *(Added June 2026.)*
- **Consider offering alternate versions** (several meaningfully different results to choose from).

**Continuous improvement**
- Plan model updates. Some changes, such as blocked-word lists, can ship outside the app release cycle. Re-test, re-tune and re-engineer prompts when you change the base model.
- **Let people share feedback on outputs.** Feedback is always voluntary and its affordance should sit in a clear spot that doesn't interrupt. Offer quick **thumbs-up / thumbs-down**, plus a way to give detailed feedback on complex issues. Act on feedback quickly.
- **Separate the model from the UX** so you can swap models without changing the experience.
- Platform considerations: none (all platforms are the same).

### 6.2 Machine learning `[hig:machine-learning]` (updated June 8, 2026) **[AI]**

**Classify each ML feature on five axes**, because each axis changes the design:

| Axis | Implication |
|---|---|
| Critical ↔ Complementary | The more central the feature, the more accuracy and reliability people expect. People forgive more in secondary features. |
| Private ↔ Public data | The more sensitive the data, the more serious an inaccurate result. Prioritize accuracy, and always protect privacy. |
| Proactive ↔ Reactive | People tolerate low-quality *unrequested* results less, so proactive features may need more data and stricter thresholds. |
| Visible ↔ Invisible | Invisible features find it hard to show reliability or collect feedback. |
| Dynamic ↔ Static | Dynamic models improve with use (calibration and feedback). Static ones improve only when the app updates. |

**Explicit feedback**: request it only when necessary and always make it voluntary. Use **option labels that state the consequence** ("Suggest less pop music", "Mute politics for a week") rather than vague terms like "dislike". Icons can support a label but never replace it. Offer several options that get progressively more specific. **Act immediately and persist the change**, hiding the item everywhere. Use the feedback to tune when and where results appear. (Favoriting and social reactions count as *implicit* feedback.)

**Implicit feedback**: secure the data and tell people how it flows; let them restrict it. Don't narrow exploration (avoid filter bubbles). Combine several signals. Withhold suggestions on private or sensitive topics, since devices get shared. Weight recent feedback most. Update at a cadence that matches people's mental model: keystroke-fast for typing, slower for recommendations. UI changes shift implicit signals. Watch for confirmation bias.

**Calibration** (only when the feature can't work without it): explain why you need the data, emphasizing *what* the feature does rather than *how*. Collect the minimum, once and early. Keep it quick and avoid info people would have to look up. Give an explicit goal and show progress. **Help immediately if progress stalls, never blame the person, and always give a next step.** Confirm success. Allow cancel at any time with no judgment. Let people edit or remove the data later, outside the flow.

**Mistakes**: anticipate them, help people handle them, and learn from them where useful. Match the corrective tooling to how serious the mistake is (a wrong keyboard suggestion vs a route that misses a flight). Make frequent mistakes easy to fix, keep the model current, and fix mistakes without cluttering the UI; a wrong attribution *magnifies* an error. **Take extra care with proactive features.** Improving one area can regress another.

**Corrections**: use familiar controls. Show the steps the automation took so people can reuse the same controls; Photos auto-crop exposes its crop controls, for example. Show corrected content instantly and persist it. Let people correct their corrections. Balance the effort: if correcting costs more than doing the task by hand, people abandon the feature. **Never rely on corrections to make up for low-quality results.** **Prefer guided corrections** (suggested alternatives) over freeform ones, or combine both.

**Multiple options** (suggested, requested, corrections): prefer *diverse* options, avoid too many (fit on one screen without scrolling), **put the most likely option first** and preselect it where sensible, make options easy to tell apart by describing their differences, and learn from what people pick.

**Confidence**: show confidence only once you've verified it tracks quality. Translate it into concepts people already understand: "Because you listen to pop music" rather than "97% match". Use ranking to imply confidence, or semantic categories such as "high chance" and "low chance". Use numbers only where people expect statistics (weather, sports, polls). Prefer actionable phrasing ("This is a good time to buy"). **Change the presentation by threshold:** high confidence → act, low → ask people to confirm, as Photos face recognition does. **Below a threshold, show nothing**, especially for proactive features.

**Attribution** (the basis for a result, not how the model works): use it to help people choose between options. Pitch it at the right level, neither too specific ("watching too closely") nor too general. Keep it factual: "Because you've read nonfiction", not "Because you love nonfiction". Avoid statistical jargon except in statistical domains.

**Limitations**: set expectations before use (in marketing or in context). Demonstrate how to get the best results, for example with **placeholder text that hints at valid input** ("Photos, People, Places…"), live coaching such as Memoji's "move closer, more light", and alternatives instead of an empty "no results". Explain why a result was poor. Tell people when a limitation has been removed.

### 6.3 Siri `[hig:siri]` (revised for "Siri AI", June 8, 2026) **[AI]**

- **Siri AI** is a version of Siri powered by Apple Intelligence on supported devices. It can start an app's actions from anywhere in the system, act on **on-screen content** ("Add this photo to my Landscapes album" → "And email it to Josh"), and reach deep features by voice.
- **Integration model:** apps expose **intents** (actions) and **entities** (content) via **App Intents**. These then appear in Siri, Spotlight and Shortcuts. **App schemas** are preset domain templates (email, music, photos, …) that the system already understands, so adopting them unlocks richer natural-language handling. Apps can also:
  - **annotate on-screen views with entities** so Siri knows what "this" refers to;
  - **donate entities to the on-device Spotlight index**;
  - **donate actions** (recent activity, items of interest) so Siri can anticipate what people want next.
- **Best practices:** expose your most popular actions and know the context where each is used (hands-free, specific device). Use familiar terms ("track", "song" or "podcast", whichever people use). Offer *relevant* content (recents, favorites, wishlist) rather than the whole catalog, though email and messaging may expose everything. **No ads, marketing or upsells in Siri content.** Write a custom response only when the built-in ones fall short.
- **Customization:** where no schema fits, use **App Shortcuts**. Optional intent or entity properties can enrich responses, such as a playback-control **snippet**. Responses appear in many contexts, some of them non-visual, so optional properties may not always show.
- **Response dialog rules:** clear and specific ("Which soup?" rather than "Which one?"). As short as possible, with no filler or humor, because people hear it repeatedly. **Works audibly and visually**, and the voice version must stand alone. Inclusive, with no unnecessary pronouns ("Who should I send it to?"). When there are too many options to read out, ask an open-ended question. Device-independent wording. **Omit the app name**, since the system attributes it. No offensive language; respect parental controls, and remember responses may be heard aloud. Errors should be specific ("Sorry, we're out of chicken noodle soup").
- **Editorial:** always call Siri "Siri", never a pronoun. Never impersonate Siri, reproduce its functions, or make a response look like it comes from Apple. Don't use reserved phrases ("Call 911", "Hey Siri"). When localizing "Hey Siri", translate only "Hey"; the page includes a 41-locale translation table, e.g. es "Oye Siri", fr "Dis Siri", de "Hey Siri", it "Ehi Siri", ko "Siri야", zh_CN "嘿Siri".
- **Implication for NEAR AI:** an AI assistant on Apple platforms must not present itself as Siri or as a system assistant. It should *expose* its actions (e.g. "Ask NEAR AI…", "Summarize with …") through App Intents and App Shortcuts so that Siri and Spotlight can invoke them.

### 6.4 Sign in with Apple `[hig:sign-in-with-apple]` (Sept 14, 2022) **[XPLAT]**

- **Available on every platform, including non-Apple platforms and the web.** It uses Face ID, Touch ID or Optic ID with built-in 2FA, and offers a **private relay email**.
- **Offering it:** ask people to sign in only in exchange for value, and explain the benefit. **Delay sign-in as long as possible**; let people explore first. If an account is required, explain why, set up the account, and then offer sign-in methods. Support linking existing accounts. In commerce, create the account *after* purchase (on the confirmation page). Welcome people immediately after sign-in. Show the current method ("Using Sign in with Apple") in account settings.
- **Data:** minimize. Say whether each extra field is required or optional. **Never ask for a password.** **Never ask for a personal email when the person chose a relay address.** Ask for optional data later, in context. Display the data you received, for example by greeting people by the shared name or email.
- **Buttons:** **no smaller than other sign-in buttons**, and visible without scrolling. Use the system button where possible: it guarantees approved appearance, auto-localizes titles, supports a corner radius (iOS, macOS, web) and includes a VoiceOver label. Titles are **Sign in with Apple / Sign up with Apple / Continue with Apple**; watchOS has only "Sign in". Styles are **white** (dark backgrounds, all platforms), **white with outline** (light backgrounds; iOS, macOS, web) and **black** (light backgrounds, all platforms; on watchOS it's a dark gray, not pure black).

| Minimum width | Minimum height | Minimum margin |
|---|---|---|
| 140 pt (140 px @1x, 280 px @2x) | 30 pt (30 px @1x, 60 px @2x) | 1/10 of the button's height |

- **Custom buttons** (iOS, macOS, web): use only Apple's downloadable logo artwork (PNG, SVG, PDF; black and white). Never use the logo itself as a button, and match the logo file's height to the button's height. Don't crop it or add vertical padding. Fixed elements: the three titles; the shape (logo+text buttons are rectangular, logo-only buttons are circular or rectangular); logo and title in **black or white only**. Changeable elements: font, weight and size; all caps; background (black or white, optionally with a subtle texture or gradient); corner radius; bezel and shadow. With the system font, **title size = 43% of button height** (height ≈ 233% of font size). **Use PNG logo files only in 44 pt-tall buttons**, which is the default and recommended iOS button height. **The right margin after the title must be ≥ 8% of the button width.** Logo-only buttons are 1:1 (PNG only at 44×44 pt) and may be masked to a circle or rounded rectangle; their margin is ≥ 1/10 of the height. App Review checks custom buttons.
- **[XPLAT]** On web and Android it sits alongside Google and other identity providers. Rule: equal visual weight, not smaller. The parent system should define a single "social sign-in button" spec (height 44 pt / 44 px+, identical width, logo inset aligned across providers), which Apple explicitly allows ("inset the logo… to align with other authentication logos").

### 6.5 Wallet identity + ID Verifier `[hig:wallet]` `[hig:id-verifier]` **[AI]** (trust and privacy)

- **Verify with Wallet** (iOS 16+): an app requests identity data from an ID card in Wallet without leaving context. Apple never sees the documents, and the app receives only encrypted data.
  - Show the option only when the device supports it, and have a fallback method ready.
  - **Ask at the precise moment you need it** (completing the regulated transaction), not when an account is created.
  - Write a **purpose string**: one brief, complete, sentence-case sentence in active voice, ending with a period. Example: "Federal law requires this information to verify your identity and also to help [App Name] prevent fraud."
  - **Ask only for the data you need**, e.g. an age-threshold request (`age(atLeast:)`) instead of a birth date. **State whether you keep the data and for how long.**
  - System button labels are Verify Age / Verify Identity / Continue / Verify with Apple Wallet, each with a multiline variant. They are always white text on black, with an optional light outline for dark backgrounds and an adjustable corner radius.
- **ID Verifier** (iOS 17+, iPhone only): reads ISO 18013-5 mobile IDs in person. *Display Only* requests keep the data inside system UI; *Data Transfer* requests need an entitlement and a legal requirement. Same minimum-data rule (age threshold). Button labels are "Verify Age" or "Verify Identity", with no NFC or QR glyphs and never the Apple logo. Provide "Matches Person" / "Doesn't Match Person" feedback buttons. Register with Apple Business Register so the organization's name and logo appear.

### 6.6 Apple In-App Purchase `[hig:apple-in-app-purchase]` (rebranded Sept 17, 2026) — subscription UX for an AI product

- **IAP vs Apple Pay:** use IAP for digital goods and subscriptions, and Apple Pay for physical goods, services and donations. Product types: consumable, non-consumable, auto-renewable subscription, non-renewing subscription.
- Let people experience the app before they buy, and offer limited free access (**freemium, metered paywall or free trial**). Make the store look like your app. Use short product names that don't truncate. **Display the total billing price for every item.** Hide the store when payments are restricted. **Never modify or replicate the system confirmation sheet.**
- **Family Sharing** (up to 5 additional members): mention it where people learn about the product ("Family", "Shareable"), and write copy that makes sense to both purchasers and family members.
- **Refund help:** offer a help screen before the refund flow (missing purchases, FAQ, contact). Label the action simply, "Refund" or "Request a Refund". Help people find the purchase (image, name, date). Alternatives are fine, but **the refund button must be reachable without scrolling or opening another screen**. Don't characterize Apple's refund policy.
- **Subscriptions:** show the benefits during onboarding with a strong CTA. Offer a range of tiers and durations. Prompt at relevant moments, such as nearing a free limit. **Don't upsell to people who already subscribe**, and offer sign-in for people who subscribed on the web or in another app. **The sign-up screen must include** the name, duration and what each period provides; a correctly localized billing amount; and sign-in/restore. If there's an intro price, show the intro price, its duration and the standard price afterwards. **Explain free trials explicitly, including the auto-charge when the trial ends.** Put a sign-up entry point in settings. In tvOS, complete sign-up on another device.
- **Offer codes:** one-time-use or custom codes (alphanumeric ASCII only). Explain where to redeem custom codes (URL or in-app; the App Store account page doesn't accept them). Add a "Redeem Code" entry in the paywall, onboarding or settings. Welcome people after they redeem.
- **Management:** show a subscription summary with the **next renewal date**. Use the system manage-subscriptions UI. A retention offer is fine, but **cancelling must always be easy and visible.**
- **watchOS:** show the same required information, ideally in a modal sheet with a Close button, with options laid out for easy comparison.
- **[XPLAT]** Web and Android billing differ: Stripe or Google Play Billing. The parent system's paywall component should still carry Apple's required-content checklist on every platform, since it's also good regulatory hygiene (EU, US auto-renewal laws).

### 6.7 Mac Catalyst `[hig:mac-catalyst]` **[XPLAT]** (iPad → Mac adaptation; it reads as a checklist for any tablet → desktop port)

- Good candidates already support drag and drop, keyboard navigation and shortcuts, multitasking/resizability, and multiple scenes (which become multiple Mac windows). Poor candidates depend on the gyroscope, rear camera, ARKit, HealthKit, or are handwriting- or navigation-centric.
- You get these automatically: pointer and keyboard focus, window management, toolbars, rich text editing with context menus, file management, menu bar menus, and a Settings pane.
- **Idioms:** the *iPad idiom* scales the UI to **77%** (17 pt iPad body → **13 pt** Mac body). The *Mac idiom* renders at 100%: sharper and more Mac-like, but you'll need to audit layout and fonts ("text can appear too large"). Use text styles, not fixed sizes, and a separate asset catalog.
- **Navigation:** replace an iPad **tab bar with a sidebar split view** (preferred) or a segmented control (flat hierarchies). **List top-level tab items in the View menu.** Add Next/Previous buttons alongside swipe gestures.
- **Input mappings:** Tap → left or right click (trackpad: click); Touch and hold → click and hold; Pan → left-click drag; Pinch and Rotate → trackpad pinch and rotate.
- **Layout:** split a single column into multiple columns. Reflow content side by side as the window resizes. **Show inspectors beside the content instead of in popovers.** Move controls into the window toolbar and mirror them as menu bar commands. **Top-down flow**: important actions go at the top. **Move buttons off the bottom and side edges**, because reachability ergonomics don't apply on Mac.
- **Menus:** Mac users expect *every* command in the menu bar and a context menu on *every* object.

### 6.8 Other technology pages, one line each

| Page | Gist (platforms) |
|---|---|
| AirPlay `[hig:airplay]` | Prefer the system media player. Don't stop playback in the background. Use the AirPlay icon only from Apple and never in custom buttons. "AirPlay" is a noun, not a verb. (Not watchOS.) |
| Always On `[hig:always-on]` | Dim and simplify the UI when the device is idle. Hide sensitive info. Reduce update frequency. (iOS, watchOS.) |
| App Clips `[hig:app-clips]` | Lightweight, instant, on-the-go or demo slice of an app. Focus on one task and defer sign-in (Sign in with Apple, Apple Pay). App Clip Code art: digital minimum **256×256 px** PNG/SVG. (iOS, iPadOS.) |
| Apple Pay `[hig:apple-pay]` | For physical goods, services and donations in apps and **any browser**. Make it the primary option when available. Use only the system buttons; minimum sizes **Apple Pay 100×30 pt; "Book/Buy/… with Apple Pay" 140×30 pt; margin ≥ 1/10 of height**. Website icon 60×60 pt (@2x 120 px, @3x 180 px). Line items for subscriptions and trials. No account required before purchase. (Not tvOS; updated June 2026.) |
| Augmented reality `[hig:augmented-reality]` | Coaching overlay, comfortable sessions, handle interruptions. (iOS, iPadOS; visionOS is covered elsewhere.) |
| CareKit `[hig:carekit]` | Care plans, tasks, charts, contact views for health care. (iOS, iPadOS.) |
| CarPlay `[hig:carplay]` | Driver-safe templates and glanceable UI only. (iOS.) |
| Game Center `[hig:game-center]` | Access point, dashboard, achievements, leaderboards, challenges. Activity art **1920×1080 pt (3840×2160 px @2x), safe crop 1465×767 pt**. (Updated 2025.) |
| HealthKit `[hig:healthkit]` | Request health data only when needed and explain why. Activity rings rules. Editorial terms. (iOS, iPadOS, watchOS.) |
| HomeKit `[hig:homekit]` | Accessory naming, setup, Siri interactions, how to refer to HomeKit. |
| iCloud `[hig:icloud]` | Sync should be transparent. Don't ask which documents to sync. Delete removes the item everywhere, so **confirm**. Detect conflicts automatically, or show an unobtrusive chooser. Don't alert when iCloud is off; quietly note that changes won't sync. Store cross-device state (last position). Include cloud content in search. **[AI]** This is the model for chat-history sync. |
| iMessage apps and stickers `[hig:imessage-apps-and-stickers]` | Compact and expanded presentation, sticker sizes. (iOS, iPadOS.) |
| Live Photos `[hig:live-photos]` | Use the system badge and playback. (Not watchOS.) |
| Maps `[hig:maps]` | MapKit annotations, place cards (added Dec 2024), App Intents. |
| NFC `[hig:nfc]` | Use the system scanning sheet and give succinct instructions. (iOS, iPadOS.) |
| Photo editing `[hig:photo-editing]` | Extension inside Photos. Confirm before discarding edits. (iOS, iPadOS, macOS.) |
| ResearchKit `[hig:researchkit]` | Consent flow, surveys, active tasks. (iOS, iPadOS.) |
| SharePlay `[hig:shareplay]` | Real-time shared activities. Easy to start and join, works across platforms, keeps people oriented. visionOS spatial and custom templates: **seats ≥ 1 m apart**, support the maximum seat count, roles independent of seats. (Not watchOS; reorganized Sept 9, 2026.) |
| ShazamKit `[hig:shazamkit]` | Audio recognition. Ask for microphone permission only when needed and show attribution. |
| Tap to Pay on iPhone `[hig:tap-to-pay-on-iphone]` | Merchant contactless acceptance. Rules for enablement and merchant education. (iOS.) |
| VoiceOver `[hig:voiceover]` | Label every key element and describe meaningful images. **Make charts fully accessible.** Hide decorative images. Unique screen titles and headings. Group related elements. **Announce layout or content changes** (important for streaming AI output). Support the rotor. On visionOS, custom gestures don't receive hand input under VoiceOver unless Direct Gesture mode is on. (New Mar 2025.) |
| Wallet passes `[hig:wallet]` | Pass styles (boarding, coupon, event, store, poster generic, generic) and image specs; e.g. logo **50–160 pt wide × 50 pt** (primary logo), **30–126 × 30 pt** (secondary). Order tracking. watchOS. Updated June 2026 for iOS 27 and the Pass Designer app. |


# 7. Cross-cutting rules

## 7. Cross-cutting rules for the NEAR AI parent design system

These rules come from the whole HIG crawl. Each says what the parent system should adopt, which HIG facts it rests on, and where Apple conflicts with Material Design, Windows (Fluent) or web conventions **[XPLAT]**.

### 7.1 Density and hit targets
- **Two density tiers, not one.** HIG defaults are *touch* 44×44 pt (iOS, iPadOS, watchOS; minimum 28×28) and *pointer* 28×28 pt (macOS; minimum 20×20). visionOS is 60×60 (minimum 28) and tvOS 66×66 (minimum 56) `[hig:accessibility]`. Adopt `density: touch` (mobile, tablets, touch web) and `density: pointer` (desktop apps and desktop web).
- **Spacing counts as much as size.** Leave about 12 pt around bezeled controls and about 24 pt around borderless ones `[hig:accessibility]`.
- **[XPLAT]** Material uses 48×48 dp touch targets. WCAG 2.2 requires 24×24 CSS px (AA, 2.5.8) and recommends 44×44 (AAA, 2.5.5). Windows Fluent controls are typically 32 epx tall in standard density and 40 in touch. Recommended tokens: `target.min.touch = 44` (≈48 on Android, satisfying Material), `target.min.pointer = 28` (Mac, Windows, web desktop; never below 24 px, per WCAG AA).
- On Mac, iPad-idiom UIs scale to **77%** (17 pt → 13 pt body) `[hig:mac-catalyst]`. Use this ratio when deriving pointer density from touch density.

### 7.2 Typography scale
- Apple's semantic text styles are **Large Title, Title 1–3, Headline, Body, Callout, Subhead(line), Footnote, Caption 1–2**. Body defaults are **iOS 17 pt / macOS 13 pt / visionOS 17 pt / watchOS 16 pt / tvOS 29 pt**. Minimums are **11 / 10 / 12 / 12 / 23 pt** `[hig:typography]`. Full Dynamic Type tables are in §1.
- **Adopt semantic style names across all platforms** and map each style to a platform size table: iOS-Large for mobile, macOS for desktop. **[XPLAT]** Material 3 uses Display, Headline, Title, Body and Label × L/M/S. Body Large is 16 sp and Body Medium is 14 sp. Web defaults to 16 px, and Windows Fluent body is 14 px. Proposal: mobile body 17 (iOS) / 16 (Android, web-mobile); desktop body 13 (macOS) / 14 (Windows, Linux, web-desktop).
- **Dynamic Type is mandatory.** Scale text through AX5 (Body 53 pt), keep the hierarchy, and reflow horizontal layouts to vertical at accessibility sizes. Prioritize scaling *content* over chrome such as tab titles. Avoid Ultralight, Thin and Light weights. **Use a tracking table** for SF (and for a custom font) instead of fixed letter-spacing. **Use the emphasized weights** listed per style.
- **Brand font:** HIG permits custom fonts. Apple's direction is to keep system fonts for UI and use the brand typeface sparingly, for headlines, while keeping Dynamic Type `[hig:branding]` `[hig:typography]`. For SF Pro / SF Mono on non-Apple platforms, see the licensing note: **SF fonts are licensed only for Apple-platform UI**. The parent system needs a cross-platform fallback stack (e.g. Inter or Geist plus a mono) for Windows, Linux, web and Android. This is the most important typography decision.

### 7.3 Color and contrast
- Use **semantic color tokens with light, dark, and increased-contrast variants**, mirroring Apple's label/secondaryLabel/…, system background/secondary/tertiary, grouped backgrounds, separators and fills `[hig:color]`. Define a *base* and an *elevated* surface for dark mode `[hig:dark-mode]`.
- **Contrast:** HIG requires ≥ **4.5:1** for text up to 17 pt and **3:1** for 18 pt+ or bold. Aim for **7:1** for custom colors and small text `[hig:accessibility]` `[hig:dark-mode]`. **[XPLAT]** The HIG large-text threshold (18 pt ≈ 18 CSS px) is *looser* than WCAG's (24 px regular, or 18.66 px bold). Adopt WCAG thresholds as the parent rule.
- **Never use color as the only signal.** Support Increase Contrast and Differentiate Without Color.
- **Brand purple:** Apple says to use the accent and brand color sparingly, on interactive elements, and not to reuse system meanings (red = destructive). Avoid putting brand color on large glass surfaces; in Liquid Glass, tint only primary actions `[hig:branding]` `[hig:color]` (see the Liquid Glass stream).

### 7.4 Navigation idiom per form factor
| Form factor | Apple idiom (HIG) | Android / Material | Windows / web desktop | Parent-system rule |
|---|---|---|---|---|
| Phone | **Tab bar** at the bottom for top-level sections (search can be a tab, iOS 26+); hierarchical push with a back button at top-leading plus edge swipe | Bottom navigation bar (3–5) + system Back; top app bar | n/a (mobile web: bottom bar or hamburger) | Bottom tab bar with 3–5 destinations. AI chat is the primary tab, with the composer docked to the bottom above the tab bar or replacing it in a thread |
| Tablet | **Tab bar at the top that can convert to a sidebar** (sidebar-adaptable); split view with 2–3 columns | Navigation rail (medium) → drawer (expanded) | n/a | Collapsible sidebar plus content, with an optional inspector column |
| iPhone Duo (new foldable/dual-display, Sept 2026) | Dynamic layouts across two displays; **tab bars and toolbars on the vertical axis** | Foldable posture guidance | n/a | Treat as a tablet-class split; see §5 |
| Desktop (Mac) | **Sidebar + window toolbar + menu bar**; every command in the menu bar; context menu on every object; settings in a separate Settings window (⌘,) | n/a | Windows: NavigationView/left pane + command bar, in-window menus; no global menu bar. Web: left sidebar + top bar | Sidebar + toolbar everywhere. On macOS also a full menu bar; on Windows, Linux and web, an in-window "⋯"/app menu and a command palette (⌘/Ctrl-K) that exposes the same command set |
| visionOS | Window + **ornaments**, tab bar as a vertical ornament on the leading side; no Dark/Light toggle (glass) | n/a | n/a | Considerations only |

- Apple folded **navigation bars into toolbars** (June 2025) `[hig:toolbars]`, so the parent system should have one "top bar / toolbar" component.
- **[XPLAT]** Back: iOS uses an in-UI back button plus a leading-edge swipe; Android uses system back (gesture or button); the web uses browser back. Every pushed view must be reachable through the platform back mechanism, and the web must keep deep-linkable URLs.

### 7.5 Modality
- HIG: use modality sparingly, only to focus on a self-contained task or a critical decision. Always give an obvious exit (Cancel/Done). Avoid stacking modals `[hig:modality]`. Sheets are for tasks and alerts are for critical information. Popovers are non-modal-ish on iPad and Mac and become sheets on iPhone.
- **Alerts:** at most a few buttons; Cancel is the bold, default *safe* choice when the action is destructive; destructive actions use the destructive (red) style `[hig:alerts]`. **[XPLAT]** Apple and Material both put the confirming action on the trailing side (right in LTR). **Windows puts the primary button on the left** (OK, Cancel). Parent rule: trailing primary on Apple, Android and web; follow the platform on native Windows.
- **[AI]** Agent actions: confirm before significant or irreversible actions taken on someone's behalf `[hig:generative-ai]`. Prefer undo over confirmation for reversible actions `[hig:undo-and-redo]` `[hig:feedback]`. Use an alert or confirmation sheet only for destructive or irreversible steps, and name the action and object in the button ("Delete Chat", not "OK").

### 7.6 Menus and commands
- macOS: the menu bar is the complete command inventory in a standard order (App, File, Edit, Format, View, app-specific, Window, Help), with standard shortcuts `[hig:the-menu-bar]` `[hig:keyboards]`. **iPadOS now has a menu bar too** (June 2025). **[XPLAT]** Windows, Linux and web have no global menu. Parent rule: define the command inventory once (id, title, shortcut, enabled state) and render it as the menu bar (macOS, iPadOS), a context menu, a toolbar overflow, and a command palette.
- Shortcuts: ⌘ on Apple ↔ Ctrl on Windows and Linux. Apple's reserved shortcuts (⌘Q, ⌘W, ⌘,, ⌘H, ⌘M, ⌘Tab…) must never be overridden. On the web, avoid shortcuts the browser reserves (Ctrl/⌘ T, W, N, L).
- Context menus: offer them on every object on desktop. Keep the most-used items first, group them with separators, keep them short, and avoid hiding primary actions only there (touch users may not find them) `[hig:context-menus]`.

### 7.7 Controls
- Switch vs checkbox **[XPLAT]**: iOS uses switches for settings. macOS prefers **checkboxes** in settings and forms, and switches only for prominent on/off groups `[hig:toggles]`. Windows uses ToggleSwitch for immediate-effect settings and checkboxes for commit-on-save forms; Material uses switches. Parent rule: a switch applies immediately, a checkbox applies on submit. On macOS, render settings with checkboxes.
- Button hierarchy: one prominent (filled) primary action per view, then secondary (tinted/bordered) and tertiary (borderless/plain). Destructive gets a role, not just a color. macOS uses a default button (Return) and a Cancel button (Esc) `[hig:buttons]`.
- Text fields: placeholder hints only, never instead of labels. Choose the right keyboard type. Avoid validating too early `[hig:text-fields]` `[hig:entering-data]`.

### 7.8 AI-product specifics distilled from the HIG
1. **Disclose AI**, set expectations, and offer curated starter prompts `[hig:generative-ai]`.
2. **Specific progress text** while generating ("Summarizing key themes…"), and generate in the background so the UI stays usable `[hig:generative-ai]` `[hig:loading]`.
3. Put **Edit / Undo / Retry / Adjust** next to outputs, and offer multiple alternatives where useful `[hig:generative-ai]` `[hig:machine-learning]`.
4. Make **thumbs up/down** voluntary and unobtrusive. Feedback options should name their consequence, and feedback should apply immediately `[hig:machine-learning]`.
5. **Confidence → presentation thresholds.** Show attributions such as "Because…", not percentages. Below the threshold, show nothing `[hig:machine-learning]`.
6. **Privacy:** prefer on-device processing, disclose server use and what's sent, ask before using personal data or training on it, and provide an opt-out `[hig:generative-ai]` `[hig:privacy]`.
7. **Agentic safety:** no automated destructive actions or purchases. Confirm significant actions. Follow regional AI regulation `[hig:generative-ai]`.
8. **System integration:** expose actions and content through App Intents (Siri AI, Spotlight, Shortcuts), Snippets and Live Activities for long-running tasks, and Controls and Widgets. Never impersonate Siri `[hig:siri]` `[hig:app-shortcuts]` `[hig:snippets]` `[hig:live-activities]`.
9. **Accessibility of streaming output:** announce content changes to VoiceOver, use headings in long answers, and make charts accessible `[hig:voiceover]` `[hig:charts]`.
10. **Monetization:** let people try the product before the paywall, list the required terms, explain auto-charge after a trial, make cancelling easy, and don't upsell existing subscribers `[hig:apple-in-app-purchase]`.

### 7.9 Where the parent system should *not* follow Apple
- SF Pro/SF Mono and SF Symbols are licensed for Apple platforms only. Off Apple platforms, use an equivalent open icon set (e.g. Lucide or Phosphor, mapped one-to-one to the SF Symbol names in use) and an open font.
- Liquid Glass and the system materials are Apple-rendered. On web, Windows and Android, emulate them with backdrop blur and tint tokens, with a solid fallback under "Reduce Transparency" / `prefers-reduced-transparency` and `prefers-contrast: more`.
- Apple's 18 pt large-text contrast threshold: use WCAG's instead (see §7.3).
- Bottom-edge controls on desktop: Apple tells Mac ports to move them to the top and toolbar `[hig:mac-catalyst]`. Keep the desktop flow top-down.


# Appendix: HIG change log entries from 2025–2026 (all pages)

| Page | Date | Change |
|---|---|---|
| `apple-in-app-purchase` | September 17, 2026 | Rebranded as Apple In-App Purchase and refined guidance to reflect current best practices. |
| `branding` | September 9, 2026 | Refined guidance for using brand color. |
| `designing-for-iphone-duo` | September 9, 2026 | New page. Introduces the fundamental concepts of designing for iPhone Duo, including device poses, dynamic layouts across dual displays, and toolbars and tab bars on the vertical axis. |
| `layout` | September 9, 2026 | Updated guidance to reflect current best practices. |
| `shareplay` | September 9, 2026 | Reorganized best practices, expanded visionOS guidance, and added a section on custom templates. |
| `app-icons` | June 8, 2026 | Refined guidance for Liquid Glass. |
| `app-shortcuts` | June 8, 2026 | Added guidance for adopting app schemas. |
| `apple-pay` | June 8, 2026 | Refined guidance to reflect the latest Apple Pay appearance and capabilities. |
| `design-principles` | June 8, 2026 | Reintroduced design principles. |
| `generative-ai` | June 8, 2026 | Added guidance for letting people refine results and providing feedback during content generation, and updated guidance for choosing a model type. |
| `machine-learning` | June 8, 2026 | Made minor updates for clarity. |
| `menus` | June 8, 2026 | Updated guidance for menu item icons. |
| `scroll-views` | June 8, 2026 | Updated guidance for scroll edge effects. |
| `search-fields` | June 8, 2026 | Updated terminology and refined guidance for search as a tab in iOS. |
| `searching` | June 8, 2026 | Updated terminology and refined best practices. |
| `sidebars` | June 8, 2026 | Updated guidance for sidebar icon colors, and clarified guidance for the adaptable sidebar style. |
| `siri` | June 8, 2026 | Revised for Siri AI. |
| `snippets` | June 8, 2026 | New page. |
| `tab-bars` | June 8, 2026 | Updated terminology and art. |
| `wallet` | June 8, 2026 | Updated to reflect guidance for iOS 27 and the Pass Designer app. |
| `scroll-views` | March 24, 2026 | Added guidance for Look to Scroll in visionOS. |
| `sheets` | March 24, 2026 | Updated guidance for button placement. |
| `apple-pay` | December 16, 2025 | Clarified supported platforms, including web browsers and Apple Vision Pro. |
| `buttons` | December 16, 2025 | Updated guidance for Liquid Glass. |
| `color` | December 16, 2025 | Updated guidance for Liquid Glass. |
| `images` | December 16, 2025 | Added guidance for spatial photos and spatial scenes in visionOS. |
| `live-activities` | December 16, 2025 | Updated guidance for all platforms, and added guidance for macOS and CarPlay. |
| `menus` | December 16, 2025 | Added guidance for presenting menus with breakthrough effects in visionOS. |
| `tab-bars` | December 16, 2025 | Updated guidance for Liquid Glass. |
| `toolbars` | December 16, 2025 | Updated guidance for Liquid Glass. |
| `typography` | December 16, 2025 | Added emphasized weights to the Dynamic Type style specifications for each platform. |
| `widgets` | December 16, 2025 | Updated guidance for all platforms, and added guidance for visionOS and CarPlay. |
| `writing` | December 16, 2025 | Clarified guidance on language patterns, and added guidance for possessive pronouns. |
| `layout` | September 9, 2025 | Added specifications for iPhone 17, iPhone Air, iPhone 17 Pro, iPhone 17 Pro Max, Apple Watch SE 3, Apple Watch Series 11, and Apple Watch Ultra 3. |
| `materials` | September 9, 2025 | Updated guidance for Liquid Glass. |
| `motion` | September 9, 2025 | Added guidance for Liquid Glass. |
| `menus` | July 28, 2025 | Added guidance for representing menu items with icons. |
| `scroll-views` | July 28, 2025 | Added guidance for scroll edge effects. |
| `sf-symbols` | July 28, 2025 | Updated with guidance for Draw animations and gradient rendering in SF Symbols 7. |
| `tab-bars` | July 28, 2025 | Added guidance for Liquid Glass. |
| `accessibility` | June 9, 2025 | Added guidance and links for Assistive Access, Switch Control, and Accessibility Nutrition Labels. |
| `app-clips` | June 9, 2025 | Updated guidance to include demo App Clips. |
| `app-icons` | June 9, 2025 | Updated guidance to reflect layered icons, consistency across platforms, and best practices for Liquid Glass. |
| `buttons` | June 9, 2025 | Updated guidance for button styles and content. |
| `color` | June 9, 2025 | Updated system color values, and added guidance for Liquid Glass. |
| `designing-for-games` | June 9, 2025 | Updated guidance for touch-based controls and Game Center. |
| `game-center` | June 9, 2025 | Added guidance for new challenges and multiplayer activities, and considerations for the Apple Games app and Game Overlay. Updated guidance and specifications for activity preview images. |
| `game-controls` | June 9, 2025 | Updated touch control best practices, updated game controller mapping for UI, and added guidance for spatial game controller support in visionOS. |
| `generative-ai` | June 9, 2025 | New page. |
| `going-full-screen` | June 9, 2025 | Updated guidance for hiding toolbars and navigation controls, and deferring Home Screen indicator gestures in full-screen iOS and iPadOS apps and games. |
| `icloud` | June 9, 2025 | Added guidance for synchronizing game data through iCloud. |
| `icons` | June 9, 2025 | Added a table of SF Symbols that represent common actions. |
| `immersive-experiences` | June 9, 2025 | Clarified guidance and noted the availability of portrait-oriented progressive immersion. |
| `keyboards` | June 9, 2025 | Moved game-specific key bindings guidance to the Game controls page. |
| `layout` | June 9, 2025 | Added guidance for Liquid Glass. |
| `loading` | June 9, 2025 | Revised guidance for storing downloads to reflect downloading large assets in the background. |
| `materials` | June 9, 2025 | Added guidance for Liquid Glass. |
| `multitasking` | June 9, 2025 | Reorganized guidance in platform considerations, and added guidance for multitasking with multiple windows in iPadOS. |
| `search-fields` | June 9, 2025 | Updated guidance for search placement in iOS, consolidated iPadOS and macOS platform considerations, and added guidance for tokens. |
| `searching` | June 9, 2025 | Updated best practices with general guidance from Search fields, and reorganized guidance for systemwide search. |
| `sidebars` | June 9, 2025 | Added guidance for extending content beneath the sidebar. |
| `split-views` | June 9, 2025 | Added iOS and iPadOS platform considerations. |
| `the-menu-bar` | June 9, 2025 | Added guidance for the menu bar in iPadOS. |
| `toolbars` | June 9, 2025 | Added guidance for grouping bar items, updated guidance for using symbols, and incorporated navigation bar guidance. |
| `virtual-keyboards` | June 9, 2025 | Added guidance for displaying custom controls above the keyboard, and updated to reflect virtual keyboard availability in watchOS. |
| `windows` | June 9, 2025 | Added best practices, and updated with guidance for resizable windows in iPadOS. |
| `accessibility` | March 7, 2025 | Expanded and refined all guidance. Moved Dynamic Type guidance to the Typography page, and moved VoiceOver guidance to a new VoiceOver page. |
| `layout` | March 7, 2025 | Added specifications for iPhone 16e, iPad 11-inch, iPad Air 11-inch, and iPad Air 13-inch. |
| `typography` | March 7, 2025 | Expanded guidance for Dynamic Type. |
| `voiceover` | March 7, 2025 | New page. |
| `app-shortcuts` | January 17, 2025 | Updated and streamlined guidance. |
| `wallet` | January 17, 2025 | Added specifications for pass image dimensions. |
| `widgets` | January 17, 2025 | Corrected watchOS widget dimensions. |


