# Apple Liquid Glass and Materials: research for the NEAR AI parent design system

Stream: Apple Liquid Glass + Materials (exhaustive). Compiled 2026-10-13.

Purpose: give the NEAR AI parent design system (derived from the trace-commons macOS app's custom "glass" language) the authoritative Apple rules for Liquid Glass, so the parent spec can fill its gaps from Apple's guidance and flag where the custom spec conflicts with it.

## How this was gathered

- **Apple developer documentation.** 150+ DocC JSON pages fetched with curl from `developer.apple.com/tutorials/data/...json` and converted to text. Saved in `corpus/apple-lg/` (196 files, about 209k words). This covers:
  - the Liquid Glass and Adopting Liquid Glass overviews;
  - HIG Materials and 38 other HIG pages, read for their Liquid Glass content;
  - every SwiftUI, UIKit, AppKit and WidgetKit symbol named in the brief;
  - the Landmarks sample and its four sub-articles;
  - "Applying Liquid Glass to custom views";
  - "Creating your app icon using Icon Composer".
- **WWDC transcripts.** Full transcripts and on-page code for:
  - all seven WWDC25 sessions in the brief: 219, 356, 323, 284, 310, 220, 361;
  - 13 WWDC26 sessions, including the Keynote (101), the Platforms State of the Union (102), What's new in SwiftUI (269), Modernize your AppKit app (289), Modernize your UIKit app (278), Communicate your brand identity on iOS (251) and Design intuitive search experiences (292).
- **Measurements on this Mac.** This machine runs macOS 27.0.1. Small Swift probes that I wrote measured AppKit control heights and window corner radii (`corpus/apple-lg/measured_macos27_*.txt`). Results are labelled **[measured]**.
- **Press and third-party sources.** Used only for user-facing settings timelines and for web and Android techniques. Labelled **[press]** or **[3rd-party]**.
- **trace-commons source.** Read only to make section 15 concrete: `design-tokens/glass.tokens.json`, `macos/Sources/TCDesign/Styling/GlassStyle.swift` and `GlassBackdrop.swift`.

Date-sensitive facts:

- HIG pages carry change logs. The relevant 2026 entries are:
  - App icons, Menus, Scroll views, Search fields, Sidebars and Tab bars: June 8, 2026.
  - Sheets: March 24, 2026.
  - Layout: September 9, 2026.
- Materials was last changed September 9, 2025. Color, Buttons and Toolbars were last changed December 16, 2025.
- Everything marked "27" comes from the iOS/iPadOS/macOS/visionOS 27 SDK docs or the WWDC26 sessions (June 8–12, 2026).

---

## 1. Concept and principles

**What it is.**
- Liquid Glass is "a new dynamic material… which combines the optical properties of glass with a sense of fluidity". It "forms a distinct functional layer for controls and navigation elements" and adapts "in response to a variety of factors to help bring focus to the underlying content" ([Liquid Glass overview](https://developer.apple.com/documentation/technologyoverviews/liquid-glass); [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass)).
- Apple calls it a "digital meta-material that dynamically bends and shapes light", not a recreation of a physical material ([WWDC25-219 Meet Liquid Glass](https://developer.apple.com/videos/play/wwdc2025/219/)).
- It draws on Aqua, the real-time blurs of iOS 7, the fluidity of iPhone X, the Dynamic Island and visionOS.

**The three stated principles** ([overview](https://developer.apple.com/documentation/technologyoverviews/liquid-glass)):
1. Establish hierarchy.
2. Create harmony.
3. Maintain consistency across devices and platforms.

The overview's design-principles list makes these concrete:
- Put the most important content in focus through layout and navigation structure.
- Give app icons simple, bold layers.
- Be judicious with colour in controls and navigation, so content can "infuse them and shine through".
- Fit hardware and software design together.
- Adopt standard iconography and predictable action placement.

**Optical properties (WWDC25-219):**

- **Lensing.** Previous materials *scattered* light. Liquid Glass "dynamically bends, shapes, and concentrates light in real time". Lensing is the primary way it defines its presence, its motion and its form against content. Controls can therefore be "ultra lightweight and transparent while still being visually distinguishable".
- **Materialization.** "Instead of fading, Liquid Glass objects materialize in and out by gradually modulating the light bending and lensing." The developer APIs expose this:
  - the SwiftUI `materialize` transition;
  - UIKit setting `effect` inside an animation block (and `nil` to dematerialize, never `alpha`).
- **Highlights layer.**
  - Light sources in a virtual environment produce highlights that respond to geometry.
  - On some interactions (lock and unlock) the lights move around the silhouette.
  - "In some cases the lighting responds to device motion."
- **Adaptive shadows.** "The element is aware of what's behind it and increases the opacity of its shadow when it is over text… lowers the opacity of its shadow when it is over a solid light background."
- **Illumination on interaction.** "The material illuminates from within… Starting right under your fingertips, the glow spreads throughout the element and onto any Liquid Glass elements nearby."
- **Thickness scales with size.** When glass grows (for example a menu opening from a toolbar button), it "simulate[s] a thicker, more substantial material. It casts deeper, richer shadows, has more pronounced lensing and refraction effects, and a softer scattering of light."
- **Ambient light spill on large surfaces (sidebars).** "Light from colorful content nearby can subtly spill onto its surface… the light reflects, scatters, and bleeds into the shadow as well."
- **Focus recession.** "When a window loses focus on the Mac or iPad, Liquid Glass shifts its appearance and visually recedes." In 27, iPad apps also dim icons and text when inactive ([WWDC26-269](https://developer.apple.com/videos/play/wwdc2026/269/)).
- **Sampling.** Glass "samples content from an area larger than itself", and "glass can not sample other glass". This is the technical reason for containers and for the no-glass-on-glass rule ([WWDC25-323](https://developer.apple.com/videos/play/wwdc2025/323/); [WWDC25-310](https://developer.apple.com/videos/play/wwdc2025/310/)).

**Behavioural properties (WWDC25-219):**
- "Responds to interaction by instantly flexing and energizing with light".
- An "inherent gel-like flexibility".
- Elements can "lift up into Liquid Glass temporarily" when touched. The resting state stays quiet and comes alive on touch, for example slider and toggle knobs.
- Controls "continually shape shift" between app states, keeping "a singular floating plane that the controls live on".
- Menus "pop open" from the button, keeping "a very clear and direct relationship between the button and the content".

**Scope.**
- Standard SwiftUI, UIKit and AppKit components pick up the material automatically.
- Custom glass is supported but should be used "sparingly" and limited "to the most important functional elements" ([Adopting](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass); [HIG Materials](https://developer.apple.com/design/human-interface-guidelines/materials)).

**2026 evolution (WWDC26, June 8, 2026).** "Updating the foundations of how Liquid Glass is built" ([Keynote 101 at 6:45](https://developer.apple.com/videos/play/wwdc2026/101/); [State of the Union 102 at 22:26–23:09](https://developer.apple.com/videos/play/wwdc2026/102/)):
- tuned "so it more effectively diffuses complex content behind it" (readability);
- "a darkened edge along with brighter specular highlights" (depth and separation);
- a new user slider, covered in section 10;
- apps already using Liquid Glass "get these improvements automatically… without even needing to recompile".

---

## 2. Variants: regular, clear, identity, tint, interactive

Sources: [HIG Materials](https://developer.apple.com/design/human-interface-guidelines/materials), [Glass](https://developer.apple.com/documentation/swiftui/glass), [Glass.clear](https://developer.apple.com/documentation/swiftui/glass/clear), [WWDC25-219](https://developer.apple.com/videos/play/wwdc2025/219/), [WWDC25-323](https://developer.apple.com/videos/play/wwdc2025/323/), [WWDC25-284](https://developer.apple.com/videos/play/wwdc2025/284/), [WWDC26-289](https://developer.apple.com/videos/play/wwdc2026/289/).

### Regular (default)

- "Blurs and adjusts the luminosity of background content to maintain legibility of text and other foreground elements." Most system components use it.
- Use it when background content could cause legibility problems, and for components with "a significant amount of text, such as alerts, sidebars, or popovers" (HIG).
- It is "the most versatile… gives you all the visual and adaptive effects… It works in any size, over any content and anything can be placed on top of it" (219).
- APIs: SwiftUI `Glass.regular` (the default of `glassEffect()`), UIKit `UIGlassEffect.Style.regular`, AppKit `NSGlassEffectView.Style.regular`.

### Clear

- "Highly translucent… ideal for prioritizing the visibility of the underlying content." Use it for components that "float above media backgrounds — such as photos and videos" (HIG).
- It "does not have adaptive behaviors. It is permanently more transparent" (219).
- **Use clear only when all three conditions hold** (219):
  1. The element sits over media-rich content.
  2. The content layer is not harmed by adding a dimming layer.
  3. The content on top of the glass is bold and bright.
- **Dimming-layer requirement.**
  - HIG: if the content underneath is bright, "consider adding a dark dimming layer of **35% opacity**". No dimming is needed if the content is "sufficiently dark", or if you use AVKit playback controls, which bring their own dimming.
  - The API doc example uses `.background(.black.opacity(0.3))`, which is 30%. That is a minor inconsistency; use 35% as the HIG value.
  - For small-footprint glass, "use localized dimming and allow the content to retain more of its original vibrancy" (219).
- **Never mix regular and clear** in one context: "They should never be mixed" (219).
- APIs:
  - SwiftUI `Glass.clear` and `.buttonStyle(.glass(.clear))`;
  - UIKit `UIGlassEffect.Style.clear`, `UIButton.Configuration.clearGlass()` and `.prominentClearGlass()`;
  - AppKit `NSGlassEffectView.Style.clear`.

### Identity

- `Glass.identity`: "your content remains unaffected as if no glass effect was applied" ([doc](https://developer.apple.com/documentation/swiftui/glass/identity)).
- It is a no-op value for toggling glass conditionally without changing the view tree, for example when switching between a glass state and a no-glass state.
- `GlassEffectTransition.identity` is the matching "no changes" transition.

### Tint

- `Glass.tint(_ color: Color?)`, UIKit `UIGlassEffect.tintColor`, AppKit `NSGlassEffectView.tintColor` ("the color the glass effect view uses to tint the background and glass effect toward").
- **How it renders.** "Selecting a color generates a range of tones that are mapped to content brightness underneath the tinted element… changing its hue, brightness and saturation depending on what's behind without deviating too much from the intended color" (219).
- A solid fill "is completely opaque and breaks the visual character". Built-in tinting "feels more transparent and more grounded".
- Tinted glass colour "automatically adapts to a vibrant version" (284).
- **When to tint.** Only "to bring emphasis to primary elements and actions" or to convey meaning, "not just for visual effect" (219, 323). Section 6 has the full rules.

### Interactive

- `Glass.interactive(_ isEnabled: Bool = true)`, UIKit `UIGlassEffect.isInteractive`, AppKit `NSGlassEffectView.effectIsInteractive`. The AppKit property is **new in macOS 27.0** and defaults to `NO` ([doc](https://developer.apple.com/documentation/appkit/nsglasseffectview/effectisinteractive)).
- **Behaviour.** "Glass reacts to user interaction by scaling, bouncing, and shimmering, matching the effect provided by toolbar buttons and sliders" (323). UIKit: "When tapping the button, it scales and bounces" (284).
- macOS 27: "the glass subtly bounces when clicked… optimized to work great with the mouse pointer" (289, 269).
- **When to use.**
  - On iOS, "for custom controls or for containers with interactive elements" (323).
  - On macOS, "use this effect with controls and buttons, or glass containers of interactive controls. A little goes a long way!" (289).
  - The AppKit doc: enable it "for glass that is used as the background for interactive controls or when used as the container of interactive controls".

### Composition examples ([Applying Liquid Glass to custom views](https://developer.apple.com/documentation/swiftui/applying-liquid-glass-to-custom-views))

```swift
Text("Hello").padding().glassEffect()                                   // regular, capsule
Text("Hello").padding().glassEffect(in: .rect(cornerRadius: 16.0))     // custom shape
Text("Hello").padding().glassEffect(.regular.tint(.orange).interactive())
```

### Button-level variants

| Intent | SwiftUI | UIKit | AppKit |
|---|---|---|---|
| Standard glass button | `.buttonStyle(.glass)` (`GlassButtonStyle`) | `UIButton.Configuration.glass()` | `NSButton.BezelStyle.glass` |
| Prominent (accent-tinted) | `.buttonStyle(.glassProminent)` | `.prominentGlass()` | `.glass` + `bezelColor`; `tintProminence = .primary` or make it the default button |
| Custom variant or tint | `.buttonStyle(.glass(.clear))` or `.glass(.regular.tint(...))` | `.clearGlass()`, `.prominentClearGlass()` | `bezelColor`, `tintProminence .secondary/.none` |

- In tvOS the glass button styles apply glass "regardless of whether the button has focus".
- AppKit tint prominence has four cases: `automatic`, `none`, `secondary` and `primary`. Use `secondary` for colour that should not upstage the default button, for example a destructive red at low prominence (310).

---

## 3. Layering model

Sources: [HIG Materials](https://developer.apple.com/design/human-interface-guidelines/materials), [Adopting](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass), [Applying Liquid Glass to custom views](https://developer.apple.com/documentation/swiftui/applying-liquid-glass-to-custom-views), [GlassEffectContainer](https://developer.apple.com/documentation/swiftui/glasseffectcontainer), [WWDC25-219](https://developer.apple.com/videos/play/wwdc2025/219/), [356](https://developer.apple.com/videos/play/wwdc2025/356/), [323](https://developer.apple.com/videos/play/wwdc2025/323/), [284](https://developer.apple.com/videos/play/wwdc2025/284/), [310](https://developer.apple.com/videos/play/wwdc2025/310/), [WWDC26-251](https://developer.apple.com/videos/play/wwdc2026/251/).

### Two layers

1. **Functional / navigation layer (glass).** Tab bars, sidebars, toolbars, navigation bars, floating controls, menus, popovers, sheets and alerts. It "floats above the content layer, establishing a clear visual hierarchy".
2. **Content layer.** App backgrounds, lists, tables, cards, media and data.

WWDC26-251 restates this for branding: "Think of your app as two distinct layers: the UI layer… and the content layer… Conceptually, the content layer is the best opportunity to express your brand identity."

### Hard rules

- **"Don't use Liquid Glass in the content layer."** Use *standard materials* (ultraThin, thin, regular, thick) for content-layer differentiation, such as app backgrounds (HIG Materials).
  - **Exception:** controls in the content layer with a *transient* interactive element, such as sliders and toggles, take a Liquid Glass appearance *only while activated*.
  - Example from 219: making a table view glass "would make it compete with other elements and muddy the hierarchy."
- **No glass on glass.** "Stacking Liquid Glass elements on top of each other can quickly make the interface feel cluttered and confusing." For elements placed on glass, "avoid applying the material to both layers. Instead, use fills, transparency, and vibrancy for the top elements to make them feel like a thin overlay that is part of the material" (219).
  - Maps removes its floating glass buttons when its sheet expands, "to keep the illusion of a single floating layer of glass intact" (284).
  - Adopting guide: "avoid overcrowding or layering Liquid Glass elements on top of each other."
- **No resting-state intersections.** "In steady states, such as when an app first launches, avoid intersections between content and Liquid Glass. Instead, reposition or scale the content to maintain separation" (219).
- **Apply the material to the control, not its inner views** (356). For AppKit, put content in `NSGlassEffectView.contentView`. "Avoid placing the NSGlassEffectView behind your content as a sibling view" (310). Only `contentView` is guaranteed to sit inside the glass; arbitrary subviews have no guaranteed z-order ([doc](https://developer.apple.com/documentation/appkit/nsglasseffectview/contentview)).
- **Modifier order (SwiftUI).** `glassEffect` "captures the content to send to the container to render. Apply the `glassEffect(_:in:)` modifier after other modifiers that affect the appearance of the view." It renders a shape anchored behind the view *and* applies "the foreground effects of Liquid Glass over a view", which gives the vibrant text ([doc](https://developer.apple.com/documentation/swiftui/view/glasseffect(_:in:))).
- **Remove custom backgrounds** from navigation elements: `NavigationStack`, `NavigationSplitView`, the `titleBar` window style, toolbars, `UINavigationBar`/`UITabBar`/`UIToolbar`/`UISplitViewController`, `NSToolbar`/`NSSplitView`.
  - Remove `UIBarAppearance` and `backgroundColor` customisations on bars.
  - Remove `presentationBackground` on sheets.
  - Remove `NSVisualEffectView` sidebar materials, which "prevent the glass material from showing through" (310).
  - Remove visual-effect views inside popovers (Adopting).

### Grouping with containers

- `GlassEffectContainer(spacing:)`, `UIGlassContainerEffect.spacing` and `NSGlassEffectContainerView.spacing`.
- **Why:**
  - **Visual correctness.** Nearby glass in different containers gives "inconsistent behavior", because glass cannot sample glass. A container "allows these elements to share their sampling region".
  - **Uniform adaptation.** A container "enforces a uniform adaptation… still gets a consistent appearance" (284). In AppKit, "the adaptive appearance of the glass is shared across the grouped elements" (310).
  - **Performance.** "Only needs one sampling pass for the entire group" (310). Adopting: "combine them using a GlassEffectContainer, which helps optimize performance".
  - **Morphing.**

### Spacing thresholds (exact semantics)

- "The larger the spacing value on the container, the sooner the Liquid Glass effects behind views blend together."
- "A spacing value on the container that's larger than the spacing of an interior HStack… causes Liquid Glass effects to blend together **at rest**."
- A view morphs into a neighbour "when the eraser's nearest edge is **less than or equal to the container's spacing**".
- Canonical example: container spacing 40 with HStack spacing 40, so shapes stay separate at rest and morph on insertion and removal.
- AppKit: the default spacing is **0**, which "is sufficient for batch processing eligible glass effect views, while avoiding distortion and merging effects for other views in close proximity" ([doc](https://developer.apple.com/documentation/appkit/nsglasseffectcontainerview/spacing)). **[measured]** On macOS 27.0.1, `NSGlassEffectContainerView().spacing == 0`.
- UIKit: spacing is "the distance between elements at which they begin to merge". Elements "start merging like small droplets of water".

### Union

- `glassEffectUnion(id:namespace:)` combines effects that share the **same shape, same variant and same ID** into a single glass shape even at rest.
- Use it for dynamically created views or views outside a single stack.

### Transitions

- `glassEffectID(_:in:)` with a `@Namespace` lets SwiftUI animate shapes into and out of each other.
- `GlassEffectTransition` values:
  - `.matchedGeometry`: the default for effects within the container's spacing. It adds scale and offset when the content changes under the default animation; opt out by passing an explicit `.spring`.
  - `.materialize`: for effects farther apart than the spacing. It fades content and animates the glass in or out without geometry matching.
  - `.identity`.
- Apple: "To provide people with a consistent experience, use matchedGeometry and materialize transitions across your apps. The system applies more than opacity changes."

### Focus and modality layering (356)

- When a task *interrupts* the main flow, "pair Liquid Glass with a dimming layer to help center attention".
- Parallel tasks get the glass's own natural separation.
- When focus deepens (dragging a sheet up), glass "subtly recedes, becoming more opaque and gently growing in size".

### Performance

- "Creating too many Liquid Glass effect containers and applying too many effects to views outside of containers can degrade performance. Limit the use of Liquid Glass effects onscreen at the same time."
- `backgroundExtensionEffect` should "often be used with only a single instance of background content".

---

## 4. Shape and concentricity

Sources: [WWDC25-356](https://developer.apple.com/videos/play/wwdc2025/356/), [ConcentricRectangle](https://developer.apple.com/documentation/swiftui/concentricrectangle), [concentric(minimum:)](https://developer.apple.com/documentation/swiftui/edge/corner/style/concentric(minimum:)), [rect(corners:isUniform:)](https://developer.apple.com/documentation/swiftui/shape/rect(corners:isuniform:)), [containerShape(_:)](https://developer.apple.com/documentation/swiftui/view/containershape(_:)-3br47), [UICornerConfiguration](https://developer.apple.com/documentation/uikit/uicornerconfiguration-swift.struct), [NSViewCornerConfiguration (macOS 27)](https://developer.apple.com/documentation/appkit/nsviewcornerconfiguration), [WWDC25-310](https://developer.apple.com/videos/play/wwdc2025/310/), [WWDC26-289](https://developer.apple.com/videos/play/wwdc2026/289/), [HIG Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars).

### The three shape types (356)

| Type | Radius rule | Typical use |
|---|---|---|
| **Fixed** | Constant radius | Cards and badges where nesting isn't relevant |
| **Capsule** | Radius = **½ of the container height** | Sliders, switches, bars, buttons, rounded corners of grouped tables; touch layouts |
| **Concentric** | Radius = **parent radius − padding**. Docs: "the container shape's corner radius minus the distance between corners" | Anything nested near a container or device corner |

- A computed concentric radius ≤ 0 renders **square**. Use `concentric(minimum:)` (SwiftUI), `UICornerRadius.containerConcentric(minimum:)` or `NSViewCornerRadius.containerConcentric(_:)` to guarantee rounding.
- 356 calls this a "**concentric shape with a fallback radius**": the concentric value adapts when nested, and the fallback applies when the component stands alone.
- Uniform corners (`isUniform: true`, or any `uniform*` factory): the system computes each corner and then applies the **largest** radius to all of them for symmetry.
- **Default glass shape is a capsule** (`DefaultGlassEffectShape`). Use rounded rectangles for larger components that "would look odd as a Capsule or Circle".
- **`NSGlassEffectView` default `cornerRadius` = 8 pt [measured]**, macOS 27.0.1. In AppKit, `cornerRadius = 999` gives a capsule (310 sample).

### Guidance

- **Optical centring.** "Views are mathematically centered when it makes sense — and subtly offset when it doesn't."
- **Watch for "pinched" or "flared" corners**, typically in nested containers such as artwork in a card. "Its shape probably needs to be concentric."
- **Near device edges:**
  - phone layouts: "use a capsule with extra margin";
  - iPad and Mac: "use a concentric shape that aligns with the window edge".
- **Capsules vs rounded rectangles on desktop.** Capsules "bring focus and clarity to touch-friendly layouts, but in dense desktop environments, they're best used for standout actions."
  - macOS: **mini, small and medium (regular) controls stay rounded rectangles**; **large and extra-large become capsules** (356, 310, 323).
  - `buttonBorderShape(_:)` (SwiftUI) and `NSControl.borderShape` (AppKit 26: buttons, pop-ups, segmented controls) override this so controls fit a custom container, for example capsule controls inside a capsule bar (310).
- **Bars.** "By default, standard buttons, text fields, headers, and footers have corner radii that are concentric with bar corners. If you need to create a custom component, ensure that its corner radius is also concentric with the bar's corners" (HIG Toolbars).
- **Sheets** have "an increased corner radius". At smaller heights "the bottom edges pull in, nesting in the curved edges of the display" (323). The Notes Format sheet is the canonical mixed shape: fixed top corners and device-concentric bottom corners (`ConcentricRectangle(uniformTopCorners: .fixed(24), uniformBottomCorners: .concentric)`).
- **Lists, tables and forms.** Sections have "an increased corner radius to match the curvature of controls"; rows have "larger row height and padding" (Adopting).
- **Widgets.** Coordinate content radius with the widget's radius through `ContainerRelativeShape` ([HIG Widgets](https://developer.apple.com/design/human-interface-guidelines/widgets)).

### Container shapes (SwiftUI)

- `containerShape(_:)` takes a `RoundedRectangularShape`: Rectangle, RoundedRectangle, UnevenRoundedRectangle, Capsule or Circle.
- System views provide container shapes by default. For your own views, declare one so `ConcentricRectangle` and `ContainerRelativeShape` resolve against it.
- If the container shape isn't a `RoundedRectangularShape`, `ConcentricRectangle` falls back to an inset copy, like `ContainerRelativeShape`.

### Window corner radii (macOS)

- **macOS 26:** windows have "a softer, more generous corner radius, which varies based on the style of window. Windows with toolbars now use a larger radius… scaling to match the size of the toolbar. Titlebar-only windows retain a smaller corner radius" (310).
- **macOS 27 (WWDC26):** "every window on macOS now has the same tighter corner radius ensuring greater consistency across all of your apps, even if they haven't been updated" (Keynote 101 at 7:40; State of the Union 102 at 23:25).
  - **[measured]** On macOS 27.0.1 every window style probed (titlebar-only, unified toolbar, unified-compact, expanded toolbar, utility panel) reports `_cornerRadius = 16` pt.
  - Read through a private property, so treat this as indicative, not API.
- **Avoiding corner clipping:** `NSView.layoutGuide(for: .safeArea(cornerAdaptation: .horizontal | .vertical))` and `.margins(cornerAdaptation:)` (`NSView.LayoutRegion`, macOS 26) (310).
- **macOS 27 adds concentric API for AppKit:** override `cornerConfiguration` to return `.uniformCorners(radius: .containerConcentric(minimum))`. "The closer the view is to the container's corner, the more its radius should match" (289).

**iOS device corner radius.** Apple does not publish a value; it is device-specific. Treat it as a container shape and let concentric APIs resolve it. Never hard-code it.

---

## 5. Adaptivity

Sources: [WWDC25-219](https://developer.apple.com/videos/play/wwdc2025/219/), [284](https://developer.apple.com/videos/play/wwdc2025/284/), [310](https://developer.apple.com/videos/play/wwdc2025/310/), [HIG Color, Liquid Glass color](https://developer.apple.com/design/human-interface-guidelines/color), [HIG Materials](https://developer.apple.com/design/human-interface-guidelines/materials).

### Light/dark flip depends on size

- **Small elements flip.** Navigation bars, tab bars and toolbars "constantly adapt their appearance… They also flip from light to dark based on the background." Symbols and glyphs on them "flip from light to dark and vice versa, mirroring the glass's behavior to maximize contrast" (219).
  - HIG: "For smaller elements like toolbars and tab bars, the system can adapt Liquid Glass between a light and dark appearance… symbols and text on these elements follow a monochromatic color scheme, becoming darker when the underlying content is light, and lighter when it's dark."
- **Large elements do not flip.** Menus and sidebars "adapt based on context, but they don't flip from light to dark. Their surface area is too big and transitions like these would be distracting" (219).
  - HIG: "Liquid Glass appears more opaque in larger elements like sidebars to preserve legibility over complex backgrounds."
- **UIKit makes size-dependence explicit** (284): "Glass adapts the appearance based on its size. **A larger size is more opaque. A smaller size is clearer, and switches between light and dark mode automatically.**" The demo animates between 250×88 and 150×44 pt to show the switch.
- **AppKit.** The toolbar glass "will even switch between a light and dark appearance if the scrolled content is especially bright or dark". This "is communicated to the toolbar's content using the NSAppearance system, so any work that you've done to support Dark Mode applies here as well" (310).
  - Consequence (HIG Color): "**Even if your app ships in a single appearance mode, provide both light and dark colors to support Liquid Glass adaptivity.**"

### Other adaptive layers

- **Shadows** grow over text and shrink over solid light backgrounds.
- **"The amount of tint and the dynamic range shift to always ensure buttons remain legible."**
- **Scroll edge effect** (section 9). Over dark content "the effect intelligently switches to apply a subtle dimming instead".
- **Window focus.** Glass recedes in inactive windows (Mac and iPad). In 27, iPad inactive windows dim icons and text. Use `@Environment(\.appearsActive)` to dim custom controls too; Apple's 27 sample sets opacity 0.5 when inactive (269).

### Vibrancy and foreground content

- SwiftUI "automatically uses a vibrant text color that adapts to maintain legibility against colorful backgrounds" inside `glassEffect` (323).
- UIKit: labels in a glass `contentView` "automatically become vibrant, based on [their] textColor". "Depending on the colors behind, the glass and its content will switch to light or dark mode automatically, **when using dynamic colors**" (284).
- When adding glass to an existing glass container, UIKit "adapts its appearance automatically".

### Legibility checklist (HIG Color and Materials)

- Avoid similar colours in control labels and the content behind them.
- Make sure the content's **resting state** (the top of a scroll view) keeps controls legible.
- Use system vibrant colours on materials.
- Thicker materials contrast better with fine text. Thinner ones preserve context.

### 2026 changes

- Tuned diffusion, a darkened edge and brighter specular highlights, all automatic.
- On macOS, "a more uniform toolbar across the top of apps" keeps "text labels and headings legible" (Keynote).

---

## 6. Tint and colour rules

Sources: [HIG Color](https://developer.apple.com/design/human-interface-guidelines/color) (updated Dec 16, 2025), [HIG Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons), [HIG Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars), [HIG Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars), [HIG Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars), [WWDC25-219](https://developer.apple.com/videos/play/wwdc2025/219/), [323](https://developer.apple.com/videos/play/wwdc2025/323/), [284](https://developer.apple.com/videos/play/wwdc2025/284/), [310](https://developer.apple.com/videos/play/wwdc2025/310/), [WWDC26-251](https://developer.apple.com/videos/play/wwdc2026/251/), [WWDC26-102](https://developer.apple.com/videos/play/wwdc2026/102/).

### Base behaviour

"By default, Liquid Glass has no inherent color, and instead takes on colors from the content directly behind it. You can apply color to some Liquid Glass elements, giving them the appearance of colored or stained glass" (HIG).

### Rules

1. **Tint only for meaning or primary actions.**
   - "Apply color sparingly… reserve it for elements that truly benefit from emphasis, such as status indicators or primary actions."
   - "Refrain from adding color to the background of multiple controls" (HIG).
   - "Avoid tinting all your elements. When every element is tinted, nothing stands out… If you want to imbue color into your app, do it in the content layer instead" (219).
2. **Colour the background, not the glyph, for primary actions.** "To emphasize primary actions, apply color to the background rather than to symbols or text. For example, the system applies the app accent color to the background in prominent buttons — such as the Done button" (HIG).
3. **One primary action per bar.**
   - "Use the `.prominent` style for key actions such as Done or Submit… Only specify one primary action, and put it on the trailing side of the toolbar" (HIG Toolbars).
   - Prominent items are "separated and tinted" and get their own glass background (`UIBarButtonItem.Style.prominent`; `NSToolbarItem.style = .prominent` plus `backgroundTintColor`).
   - HIG Buttons: "Keep the number of prominent buttons to **one or two per view**."
4. **Monochrome icons by default.**
   - "Icons use monochrome rendering in more places, including in toolbars… You can still tint icons… but use this to convey meaning" (323).
   - UIKit bar buttons default to `labelColor`. Setting `tintColor` colours "only the Flag symbol"; style `.prominent` tints the background (284).
5. **Colourful content means monochrome bars.** "If your app features colorful backgrounds or visually rich content, prefer a monochromatic appearance for toolbars and tab bars, or choose an accent color with sufficient visual differentiation. By contrast, in apps with primarily monochromatic content or backgrounds, choosing your brand color as the app accent color can be an effective way to tailor your app experience and reflect your company's identity" (HIG). Buttons, Toolbars and Tab bars repeat this.
6. **Custom colours** need light and dark variants **and an increased-contrast option for each** (Adopting; HIG Color).
7. **Brand placement (2026).**
   - "Our recommendation is to move color into the content area of your app, into the scroll view. That way, Liquid Glass controls sit above the content layer and pick up your brand color dynamically."
   - "Aim to use color in ways that create meaning such as portraying hierarchy, groupings, or indicating interaction… exercise restraint" (251).
   - The example: Slack moved its solid top-toolbar colour into the content area so it scrolls away.
8. **Non-interactive items get no glass.** "Non-interactive items like custom titles and status indicators should avoid the glass material… with the glass material backing, it almost looks like a button." Use `NSToolbarItem.isBordered = false` (310), SwiftUI `sharedBackgroundVisibility(.hidden)`, or UIKit `hidesSharedBackground` / `sharesBackground = false`.
9. **Sidebar icons (27).** They "regain their color using your app's accent color… List and Label APIs provide these updates automatically and support customizing the tint per item" (102).
   - HIG Sidebars (June 8, 2026): sidebar icons default to the accent colour. On macOS they follow the user's system accent. Fixed colours only "sparingly" for meaning, for example the yellow VIP icon in Mail.

### Vibrant colours on standard materials (HIG Materials)

- iOS defines vibrancy levels for:
  - labels: label (default, highest contrast), secondaryLabel, tertiaryLabel and quaternaryLabel. **Avoid quaternary on thin and ultraThin.**
  - fills: fill, secondaryFill and tertiaryFill;
  - separators: one level.
- macOS has vibrant versions of all system colours.
- visionOS uses label, secondary and tertiary. Tertiary is for inactive elements only.

### System colours relevant to a purple brand

Values as published in the HIG specifications table. **Don't hard-code them**; the HIG says values change between releases.

| Name | Light | Dark | Increased contrast light | Increased contrast dark |
|---|---|---|---|---|
| Purple | 203,48,224 | 219,52,242 | 176,47,194 | 234,141,255 |
| Indigo | 97,85,245 | 109,124,255 | 86,74,222 | 167,170,255 |
| Blue | 0,136,255 | 0,145,255 | 30,110,244 | 92,184,255 |

The Trace brand purple `#6d14f3` (109,20,243) sits between system Indigo and Purple in hue. As an app accent it will be what system tinting maps across glass, so it needs dark and increased-contrast variants.

---

## 7. Motion and interaction

Sources: [WWDC25-219](https://developer.apple.com/videos/play/wwdc2025/219/), [323](https://developer.apple.com/videos/play/wwdc2025/323/), [284](https://developer.apple.com/videos/play/wwdc2025/284/), [HIG Motion](https://developer.apple.com/design/human-interface-guidelines/motion), [Adopting](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass), [GlassEffectTransition](https://developer.apple.com/documentation/swiftui/glasseffecttransition), [TabBarMinimizeBehavior](https://developer.apple.com/documentation/swiftui/tabbarminimizebehavior), [WWDC26-269](https://developer.apple.com/videos/play/wwdc2026/269/), [WWDC26-278](https://developer.apple.com/videos/play/wwdc2026/278/).

### Interactive glass response

- On press: **scale, bounce, shimmer** (323).
- **Illumination from the touch point** spreads through the element and into nearby glass (219).
- Elastic, "gel-like" flex. On macOS 27, a subtle **bounce on click** (289).
- **Touch vs pointer.** "The movement of Liquid Glass responds to direct touch interaction with greater emphasis… but produces a more subdued effect when a person interacts using a trackpad" (HIG Motion).

### Controls that lift into glass

- "For controls like sliders and toggles, the knob transforms into Liquid Glass during interaction" (Adopting).
- "Control thumbs, like those on switch and segmentedControl, automatically have a new liquid glass appearance for interactions" (284).
- Sliders "preserve momentum and stretch when they are moved" (284).

### Materialize and dematerialize

- UIKit: "Always prefer setting the effect property over the alpha to ensure that the glass dematerializes or materializes with the appropriate animation." Animate `effect = UIGlassEffect()` in, and `effect = nil` out.
- To remove content from glass, animate the content's alpha, not the glass (284).
- SwiftUI: the `.materialize` transition.

### Morphing

- In containers with `glassEffectID`, elements merge "like small droplets of water" and split apart (section 3).
- **Splitting** (UIKit): add the views at the same frame without animation, then animate them out.
- **Merging:** animate the frames to overlap (284).
- Controls also morph between app states, so the control plane "continually shape shift[s]" (219).

### Presentations morph from their source

- **Menus** "pop open" from their button, automatically (219, 284).
- **Popovers** morph when their source is a bar button item: `popoverPresentationController.sourceItem` (284).
- **Sheets:**
  - SwiftUI: make the toolbar item a `matchedTransitionSource(id:in:)` and the sheet content `.navigationTransition(.zoom(sourceID:in:))` (323).
  - UIKit: `preferredTransition = .zoom { _ in barButtonItem }` (284).
- **Dialogs / confirmation dialogs** "automatically morph out of the buttons that present them" (323).
- **Action sheets** "originate from the element that initiates the action instead of from the bottom edge" and leave the rest of the UI interactive (Adopting).
  - Set `sourceView` or `sourceItem` on every device.
  - Inline action sheets have **no Cancel button**, because tapping outside cancels. Without a source they centre and show Cancel (284).

### Tab bar minimize (iPhone)

- `tabBarMinimizeBehavior(.onScrollDown | .onScrollUp | .automatic | .never)`, or UIKit `UITabBarController.MinimizeBehavior`.
- "Minimizing is supported for tab bars on only iPhone."
- The bar expands when scrolling in the opposite direction.
- `.onScrollUp` is recommended "if the scroll view content is aligned to the bottom".
- The bottom accessory animates down to sit inline (section 8).
- People exit the minimized state by tapping a tab or scrolling to the top (HIG Tab bars).

### Navigation bar minimize (27)

- SwiftUI: `.toolbarMinimizeBehavior(.onScrollDown, for: .navigationBar)` (269).
- UIKit: `navigationItem.barMinimizationBehavior = .always / .never`, plus `barMinimizationSafeAreaAdjustment = .never` if you manage insets yourself (278).

### Sheets

- Partial-height sheets are inset with glass.
- At full height the glass "gradually transitions, becoming opaque and anchoring to the edge of the screen" (323).
- Dragging up makes the glass "recede, becoming more opaque and gently growing in size" (356).

### Navigation

- iOS 26 makes standard push and pop interruptible.
- **Content backswipe** works anywhere in the content area. Custom gestures must set failure requirements on `interactiveContentPopGestureRecognizer` (284).

### Timing

- Apple publishes **no glass durations or curves**. Morphs use SwiftUI's default animation or springs.
- Under `matchedGeometry`, the default animation adds scale and offset effects. Specify `.spring` to opt out.
- **Implication for the parent system:** define motion as spring tokens, not fixed cubic-bezier durations, for glass morphs.

### Reduce Motion

It "decreases the intensity of some effects and **disables any elastic properties**" (219). Section 10 covers it.

---

## 8. Component changes by platform

### 8.1 Toolbars and navigation bars

Sources: [HIG Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars), [WWDC25-323](https://developer.apple.com/videos/play/wwdc2025/323/), [284](https://developer.apple.com/videos/play/wwdc2025/284/), [310](https://developer.apple.com/videos/play/wwdc2025/310/), [Landmarks toolbar](https://developer.apple.com/documentation/swiftui/landmarks-refining-the-system-provided-glass-effect-in-toolbars), [ToolbarSpacer](https://developer.apple.com/documentation/swiftui/toolbarspacer), [sharedBackgroundVisibility](https://developer.apple.com/documentation/swiftui/toolbarcontent/sharedbackgroundvisibility(_:)), [WWDC26-269](https://developer.apple.com/videos/play/wwdc2026/269/).

**Basic behaviour**
- Bars are **transparent**. Items float on glass "that floats above the app's content and automatically adapts to what's beneath it".
- Items are **grouped automatically**, and each group shares one glass background.

**UIKit grouping rules (284)**
- Image buttons share a background with other image buttons.
- Multi-item button groups share a background.
- These each get **separate** glass:
  - text buttons;
  - the system **Done** and **Close** buttons;
  - prominent-style buttons.
- Each `flexibleSpace` **separates** backgrounds. Set `hidesSharedBackground = false` on flexible spaces to distribute items evenly while keeping them in one group.

**AppKit grouping (310)**
- Multiple toolbar buttons are grouped on one glass piece.
- Segmented controls, pop-ups and search are separated.
- Override with `NSToolbarItemGroup` or spacers.

**APIs for separating and grouping**
- SwiftUI: `ToolbarSpacer(.fixed | .flexible, placement:)`, `ToolbarItemGroup`, `.sharedBackgroundVisibility(.hidden)`.
- UIKit: `UIBarButtonItem.fixedSpace(_:)`, `.sharesBackground`, `.hidesSharedBackground`.
- AppKit: `NSToolbarItem.Identifier.space`.

**Rules (HIG and Adopting)**
- **Group by function and frequency.** Undo/Redo is one group; Markup/More is another.
- **Aim for at most three groups.**
- Keep groupings consistent across platforms.
- **Don't mix text and icons in a shared background.** For example, "Select" next to a share icon reads as one button. Give text buttons their own containers (356).
- **Prefer SF Symbols without borders.** Outlined-circle symbols are unnecessary because the group provides a visible container.
- **Always give an accessibility label** to icon-only items.
- **Hide whole toolbar items, not their content views**, or you get empty glass: `ToolbarContent.hidden(_:)`, `UIBarButtonItem.isHidden`, `NSToolbarItem.isHidden`.
- **Overcrowding.** Move secondary actions into a More menu. iPadOS and macOS add the system overflow menu automatically; don't add one manually.
- Titles: under 15 characters, and don't use the app name.
- Badges: SwiftUI `.badge(n)` on toolbar items (323). AppKit `NSItemBadge.count(_:)`, `.text(_:)`, `.indicator` (310).

**UIKit navigation-bar extras (iOS 26)**
- `subtitle` and `largeSubtitleView`.
- Large titles now sit at the top of the scroll content and scroll under the bar (284).

**2026 (27) toolbar APIs**
- `visibilityPriority(.high)`: available on macOS 26.1+ and iOS 27.
- `ToolbarOverflowMenu { }`: iOS, iPadOS and visionOS 27.
- `ToolbarItemPlacement.topBarPinnedTrailing`: iOS 27. The item only moves to overflow when search is active and space is short.
- macOS 27: "bordered toolbar items over the sidebar adopt Liquid Glass as well" (289).

### 8.2 Tab bars

Sources: [HIG Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) (June 8, 2026), [WWDC25-323](https://developer.apple.com/videos/play/wwdc2025/323/), [284](https://developer.apple.com/videos/play/wwdc2025/284/), [356](https://developer.apple.com/videos/play/wwdc2025/356/), [tabViewBottomAccessory](https://developer.apple.com/documentation/swiftui/view/tabviewbottomaccessory(content:)), [TabRole.prominent](https://developer.apple.com/documentation/swiftui/tabrole/prominent), [WWDC26-278](https://developer.apple.com/videos/play/wwdc2026/278/).

**iOS**
- The tab bar **floats** at the bottom on glass, and can minimize (section 7).

**Bottom accessory**
- APIs:
  - SwiftUI `tabViewBottomAccessory { }`;
  - SwiftUI `tabViewBottomAccessory(isEnabled:content:)`, **iOS 26.1+**, for showing and hiding it;
  - UIKit `UITabAccessory(contentView:)` with `tabBarController.bottomAccessory`.
- It sits *above* the tab bar when the bar is full size, and *inline* when the bar is collapsed.
- Read `@Environment(\.tabViewBottomAccessoryPlacement)` (`.expanded` / `.inline`), or the UIKit trait `tabAccessoryEnvironment`, to switch layouts.
- **Use it only for persistent, app-wide features** such as media playback. "Avoid placing screen-specific actions here — a checkout button… belongs with the content it supports" (356).

**Search tab**
- `Tab(role: .search)` or `UISearchTab`. The system separates it and places it at the **trailing end**.
- Selecting it makes the search field take the place of the tab bar. `automaticallyActivatesSearch` focuses the field immediately.

**Prominent tab (27)**
- `Tab(role: .prominent)` or `UITabBarController.prominentTabIdentifier`.
- Only one tab can be prominent. It is pinned to the trailing edge and "is always visible, even when the tab bar collapses during scrolling".
- If no tab is marked, a search tab may get the prominent treatment by default (`.search`, or `automaticallyActivatesSearch`).

**iPadOS**
- The tab bar is near the top and floats on glass.
- `sidebarAdaptable` / `UITabBarController.Mode.tabSidebar` converts it to a sidebar.
- **iOS 27:** iPhone apps can opt into a sidebar with `tabBarController.sidebar.preferredPlacement = .sidebar`. The system decides availability (regular width), exposed through `sidebar.isAvailable` (278).

**Colour**
- Avoid label colours similar to the content backgrounds; prefer monochrome (HIG).

**Other platforms**
- visionOS: the tab bar is vertical and expands on gaze.
- tvOS: 68 pt high, top edge 46 pt from the top, translucent.

### 8.3 Sidebars, inspectors and split views

Sources: [HIG Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars) (June 8, 2026), [Adopting](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass), [WWDC25-310](https://developer.apple.com/videos/play/wwdc2025/310/), [284](https://developer.apple.com/videos/play/wwdc2025/284/), [323](https://developer.apple.com/videos/play/wwdc2025/323/), [backgroundExtensionEffect](https://developer.apple.com/documentation/swiftui/view/backgroundextensioneffect()), [Landmarks background extension](https://developer.apple.com/documentation/swiftui/landmarks-applying-a-background-extension-effect), [WWDC26-102](https://developer.apple.com/videos/play/wwdc2026/102/), [WWDC26-289](https://developer.apple.com/videos/play/wwdc2026/289/).

**macOS and iPadOS 26**
- **Sidebars are inset, floating panes of glass.**
- **Inspectors use "edge-to-edge glass that sits alongside the content"** with "more subtle layering" (310, 323).
- Use `NavigationSplitView` with `.inspector(isPresented:)`, `UISplitViewController` with `.inspector`, or `NSSplitViewController` with `init(inspectorWithViewController:)`. Split views reflow fluidly during continuous resizing.

**Extend content under sidebars**

Two techniques:
1. **Horizontal scroll views** that touch the leading and trailing edges scroll under the sidebar automatically. Add a leading `Spacer` to inset the first item (Landmarks).
2. **Background extension effect.**
   - APIs: `backgroundExtensionEffect()`, `backgroundExtensionEffect(isEnabled:)`, `UIBackgroundExtensionView` (`automaticallyPlacesContentView`), `NSBackgroundExtensionView`.
   - What it does: "takes a section of the leading end of the image that matches the width of the sidebar… flips that portion of the image horizontally… and applies a blur", then places it under the sidebar (the inspector side is mirrored). The view is clipped so the copies don't overlap.
   - **Apply it to the image only.** Put titles and buttons in an overlay added *after* the modifier, or as siblings in UIKit, so they don't extend or distort.
   - Use it on hero images, tinted backgrounds or "any surface meant to feel expansive". Use one instance per view, per section if needed.

**AppKit**
- `splitViewItem.automaticallyAdjustsSafeAreaInsets = true` on the *content* item, not the sidebar, extends its frame under the sidebar and applies a safe-area layout guide (310).

**Remove legacy sidebar materials**
- Remove the `NSVisualEffectView .sidebar` material.
- iOS: use `UICollectionLayoutListConfiguration.Appearance.sidebar` if not using SwiftUI.

**2026 (27)**
- "Sidebars expand to the edges on Mac and iPad, providing clearer structure while still refracting content from your app and the wallpaper" (102).
- macOS 27: "selection in the sidebar uses a semi-bold text style for emphasis… content still flows behind them" (289).
- Sidebar icons regain accent colour (section 6).
- The 26 inset-pane look should therefore be treated as superseded on macOS 27 and iPadOS 27.

### 8.4 Sheets, popovers, menus, alerts and action sheets

Sources: [Adopting](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass), [HIG Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets) (Mar 24, 2026), [HIG Menus](https://developer.apple.com/design/human-interface-guidelines/menus) (June 8, 2026), [WWDC25-323](https://developer.apple.com/videos/play/wwdc2025/323/), [284](https://developer.apple.com/videos/play/wwdc2025/284/), [356](https://developer.apple.com/videos/play/wwdc2025/356/), [WWDC26-278](https://developer.apple.com/videos/play/wwdc2026/278/), [WWDC26-269](https://developer.apple.com/videos/play/wwdc2026/269/).

**Sheets**
- Increased corner radius.
- **Half sheets are inset** from the display edge "to allow content to peek through"; at full height they become more opaque.
- **Audit:**
  - content too close to the rounder corners inside the sheet;
  - what peeks through between the inset sheet and the display edge;
  - remove `presentationBackground` and custom backgrounds.
- **iOS button placement** (HIG, Mar 2026):
  - Cancel on the leading edge of the top toolbar, Done on the trailing edge.
  - Always pair Done with Cancel or Back.
  - Never show all three (Cancel, Done, Back).
- Detents: `.medium` is about half height. Include a grabber.
- watchOS sheets are full-screen material. "Avoid removing or replacing material backgrounds for modal sheets."

**Popovers**
- Remove custom visual-effect backgrounds.
- They morph from bar-button sources.

**Menus**
- Liquid Glass; they morph from their button.
- Icons on the leading edge, now on macOS too.
- 2025 guidance: use standard selectors so Cut, Copy and Paste get icons automatically. Use one icon to introduce a group of related actions. Provide icons for all items in a group or none.
- **27 change:** "iPad and Mac Menu Bars now have a minimal set of icons by default, reserving them for key actions" (269).
  - SwiftUI opt-in: `.labelStyle(.titleAndIcon)`.
  - UIKit opt-in: `preferredImageVisibility` (278).
  - HIG (June 8, 2026): "Use menu item icons sparingly and with purpose."
- Match the top context-menu actions to the swipe actions for the same item.

**Alerts and dialogs**
- They adopt glass and morph from the presenting button.
- Typography is bolder and left-aligned in alerts and onboarding (356).

**Action sheets**
- Anchored to their source on iPhone too (iOS 26).
- Inline action sheets have no Cancel (section 7).

### 8.5 Search

Sources: [Adopting](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass), [WWDC25-323](https://developer.apple.com/videos/play/wwdc2025/323/), [284](https://developer.apple.com/videos/play/wwdc2025/284/), [searchToolbarBehavior](https://developer.apple.com/documentation/swiftui/view/searchtoolbarbehavior(_:)), [HIG Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields) (June 8, 2026), [WWDC26-292](https://developer.apple.com/videos/play/wwdc2026/292/).

**iPhone**
- Search in a toolbar sits **at the bottom**, within reach. On focus it slides up above the keyboard.
- The system may **minimize** it to a toolbar button, depending on device size and item count. Opt in with `.searchToolbarBehavior(.minimize)`.
- Bottom-toolbar search adapts its width to one leading and one trailing action. With more than two other items it starts as a button.
- Top-toolbar search is used when a sheet occupies the bottom, as in Stocks.

**iPad and Mac**
- Search sits in the **top-trailing** toolbar position, on its own glass.
- UIKit: `searchBarPlacementAllowsExternalIntegration = true`, `preferredSearchBarPlacement = .integratedCentered`, `searchBarPlacementBarButtonItem`.

**Tabbed apps**
- A dedicated search tab at the trailing end. On iPad and Mac the field is centred above suggestions.

**Styling and branding**
- "Depending on where your Search Field is placed, it will automatically adopt the correct presentation style. Such as using glass when placed in a Toolbar or using standard content styling when placed in the scroll region" (292).
- Branded icon sets must keep the core search elements: the magnifying glass, Clear and Cancel.

### 8.6 Controls

Sources: [Adopting](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass), [WWDC25-323](https://developer.apple.com/videos/play/wwdc2025/323/), [284](https://developer.apple.com/videos/play/wwdc2025/284/), [310](https://developer.apple.com/videos/play/wwdc2025/310/), [356](https://developer.apple.com/videos/play/wwdc2025/356/), [HIG Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons).

**General**
- "The shape of the hardware informs the curvature of controls, so many controls adopt rounder forms."
- "Controls also feature an option for an extra-large size."
- Don't hard-code control metrics; sizes changed.

**Buttons**
- "Bordered buttons now have a capsule shape by default", except macOS mini, small and medium (323).
- New styles: glass and glass-prominent (section 2).
- Hit target at least **44×44 pt** (visionOS **60×60 pt**).
- Always include a press state.
- One or two prominent buttons per view. Use style, not size, to mark the preferred option.

**Sliders**
- Tick marks:
  - SwiftUI: a `step` parameter, or a `ticks` closure;
  - UIKit: `UISlider.TrackConfiguration(allowsTickValuesOnly:neutralValue:numberOfTicks:)`.
- Neutral value: SwiftUI `neutralValue:`, AppKit `NSSlider.neutralValue`. The fill anchors at a non-minimum value, for example 1× speed.
- UIKit `sliderStyle = .thumbless` gives a progress-bar look.
- AppKit `tintProminence = .none` means no track fill.

**Switches and segmented controls**
- Updated sizes (UISwitch changed). Their thumbs turn to glass during interaction.

**Lists and forms**
- Larger row height and padding.
- **Section headers are no longer forced to uppercase.** Use title-style capitalisation.
- Use `.formStyle(.grouped)`.

**Typography**
- "Bolder and left-aligned… in alerts and onboarding."
- System colours were re-tuned across Light, Dark and Increased Contrast to work with glass (356).

### 8.7 macOS control sizes and heights

**[measured]** macOS 27.0.1, alignment-rect heights in points, from `fittingSize` of standard controls (`corpus/apple-lg/measured_macos27_control_metrics.txt`).

| `controlSize` | Font | Push / glass button | Pop-up | Segmented | Switch (w×h) | Search field | Text field | Shape (Apple) |
|---|---|---|---|---|---|---|---|---|
| mini | 9 pt | 16 | 16 | 16 | 36×16 | 16 | 19 | rounded rect |
| small | 11 pt | 20 | 20 | 20 | 44×20 | 20 | 22 | rounded rect |
| regular ("medium") | 13 pt | **24** | 24 | 24 | 54×24 | 24 | 24 | rounded rect |
| large | 13 pt | **28** | 28 | 28 | 64×28 | 28 | 24 | **capsule** |
| extraLarge (macOS 26+) | 13 pt | **36** | 36 | 36 | 80×36 | 36 | 24 | **capsule** |

With `prefersCompactControlSizeMetrics = true` (macOS 26+, inherited down the view tree) the "macOS 15 and earlier" metrics return: mini 13, small 16, regular **20**, large 28, extraLarge 36 (unchanged). Legacy push buttons report a larger frame with bezel insets, for example 31 pt frame for 20 pt visible.

Apple's guidance:
- Mini, small and medium are "slightly taller… more breathing room… enhancing the size of the click target".
- Use Auto Layout and avoid hard-coded heights.
- Use `prefersCompactControlSizeMetrics` (AppKit) or `.controlSize(.small)` (SwiftUI) for dense inspectors and popovers.
- Use XL for "the actions that people launch your app to get done", such as play or call (310).
- **Doc inconsistency to note:** SwiftUI `ControlSize.extraLarge` still says it "resolves to `.large` on platforms other than visionOS". The WWDC25-323 session and `NSControl.ControlSize.extraLarge` (macOS 26.0+) say macOS supports XL buttons, and the AppKit measurement shows 36 pt.

**visionOS button sizes (HIG Buttons):** mini 28, small 32, regular 44, large 52, XL 64 pt.

### 8.8 Windows (iPadOS and macOS)

Sources: [Adopting](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass), [WWDC25-310](https://developer.apple.com/videos/play/wwdc2025/310/).

- Rounder corners (section 4).
- iPadOS 26 adds window controls and continuous resizing down to a minimum size. Support arbitrary sizes, and use safe areas and layout guides so the system can place window controls.
- iOS 27: iPhone apps become resizable too (iPhone Mirroring, iPhone apps on iPad) (269).
- Split-item accessories (`NSSplitViewItemAccessoryViewController`, top or bottom aligned per split) and titlebar accessories are "the best way to incorporate floating content into the scroll edge effect" (310).

---

## 9. Scroll edge effect

Sources: [HIG Scroll views, Scroll edge effects](https://developer.apple.com/design/human-interface-guidelines/scroll-views) (updated June 8, 2026), [ScrollEdgeEffectStyle](https://developer.apple.com/documentation/swiftui/scrolledgeeffectstyle), [WWDC25-219](https://developer.apple.com/videos/play/wwdc2025/219/), [356](https://developer.apple.com/videos/play/wwdc2025/356/), [284](https://developer.apple.com/videos/play/wwdc2025/284/), [310](https://developer.apple.com/videos/play/wwdc2025/310/), [WWDC26-278](https://developer.apple.com/videos/play/wwdc2026/278/), [WWDC26-289](https://developer.apple.com/videos/play/wwdc2026/289/), [WWDC26-102](https://developer.apple.com/videos/play/wwdc2026/102/).

**What it is**
- A treatment on scroll content where pinned controls overlap it. "As content begins to scroll underneath a glass element, the effect gently dissolves the content into the background." Over dark content it applies "a subtle dimming instead" (219).
- It **replaces hard dividers and bar backgrounds** (356).

**Styles**
- **Soft:** "a subtle blurred transition"; translucent, getting progressively more opaque toward the edge.
- **Hard:** "a more opaque, clearly defined linear boundary", "nearly opaque". It is applied "uniformly across the height of the toolbar and the pinned accessory view" (219). It looks similar to iOS 18 bar backgrounds (284).
- **Automatic:** the system's choice.
- **Hidden:** `scrollEdgeEffectHidden(_:for:)`.

**2025 guidance (356)**
- Soft is "the default… especially on iOS and iPadOS… works well for interactive elements, like buttons or inputs, using Liquid Glass".
- Hard is "mostly used on macOS… ideal for interactive text, controls without backgrounds, or pinned table headers".
- Use hard for denser UIs with many floating elements, such as Calendar (323).

**Rules (HIG and 356)**
- "**Scroll edge effects aren't decorative.** They don't block or darken like overlays."
- "Only use a scroll edge effect when a scroll view is behind floating interface elements."
- "Apply one scroll edge effect per view." In split views each pane can have its own, but keep them **consistent in height**.
- "Avoid mixing or stacking them."
- Remove extra backgrounds and darkening behind bar items, which "interfere with the effect" (323).

**2026 changes (dated)**
- **HIG, June 8, 2026:** "**Prefer the automatic scroll edge effect style.** This style provides a more opaque visual separation for top toolbars that contain a large number of controls, text that appears outside of Liquid Glass controls, and pinned table headers. If you use the soft scroll edge effect style instead, thoroughly test."
- **iOS 27 (278):** "the `.automatic` style **no longer switches between the existing soft and hard styles but provides its own visuals** for additional clarity. If you have overridden the style… re-evaluate, especially when set to `.soft`, as that no longer matches the default system appearance."
- **macOS 27 (289):** "The automatic NSScrollEdgeEffectStyle resolves to a hard-edge effect when there is free-floating text, like the window title in the title bar."
- **macOS 27 (102):** "When content scrolls under floating bars, a uniform toolbar appears across the top… applied automatically for standard toolbars and can be customized using the existing scroll edge effect APIs."

**APIs for custom bars**

| Platform | APIs |
|---|---|
| SwiftUI | `safeAreaBar(edge:alignment:spacing:content:)`, which "extends the edge effect of any scroll views affected by the inset safe area" (`safeAreaInset` does not); `scrollEdgeEffectStyle(_:for:)` |
| UIKit | `UIScrollView.topEdgeEffect`, `bottomEdgeEffect`, `leftEdgeEffect`, `rightEdgeEffect` (`.style` = `.automatic`, `.hard`, `.soft`; `.isHidden`); `UIScrollEdgeElementContainerInteraction` (set `scrollView` and `edge`) on a container of floating controls, so labels, images, glass and controls shape the effect |
| AppKit | Built into `NSScrollView`, under toolbar items, titlebar accessories and split-item accessories; `NSScrollEdgeEffectStyle` (`.automatic`, `.hard`, `.soft`, **macOS 26.1+**); `NSSplitViewItemAccessoryViewController.preferredScrollEdgeEffectStyle` |

---

## 10. Accessibility and user settings

Sources: [WWDC25-219](https://developer.apple.com/videos/play/wwdc2025/219/), [Adopting](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass), [HIG Materials](https://developer.apple.com/design/human-interface-guidelines/materials), [HIG Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility), [HIG Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode), [accessibilityShowBorders](https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityshowborders), [accessibilityReduceTransparency](https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityreducetransparency), [WWDC26-102](https://developer.apple.com/videos/play/wwdc2026/102/), [WWDC26-269](https://developer.apple.com/videos/play/wwdc2026/269/).

### Automatic for system glass (219)

| Setting | What Liquid Glass does |
|---|---|
| **Reduce Transparency** | "Makes Liquid Glass **frostier** and obscures more of the content behind it" |
| **Increase Contrast** | "Makes elements **predominantly black or white** and highlights them with a **contrasting border**" |
| **Reduce Motion** | "Decreases the intensity of some effects and **disables any elastic properties**" |

"These are available automatically whenever you use the new material… Liquid Glass elements will get them across the board." In 2026: "Liquid Glass seamlessly adapts… such as reducing transparency or increasing contrast" (102).

### User preference timeline

- **iOS 26.1, iPadOS 26.1, macOS 26.1** (betas October 2025, released early November 2025). A binary **Liquid Glass: Clear / Tinted** setting **[press]**.
  - iOS path: Settings › Display & Brightness › Liquid Glass. macOS path: System Settings › Appearance.
  - Apple's description: "Clear is more transparent, revealing the content beneath… Tinted increases opacity and adds more contrast."
  - Clear is the default. It applies to third-party apps using system glass.
  - This is the "preferred look for Liquid Glass in their device's settings" that the HIG and Adopting guide tell you to test against.
- **iOS 26.2** (December 2025). A Lock Screen clock "Glass" opacity slider in the wallpaper editor **[press]**.
- **macOS 26.3 and 26.4** (February and March 2026). Reduce Transparency sidebar headers become opaque, and Tinted respects light and dark mode **[press: anderegg.ca, mjtsai]**.
- **iOS, iPadOS and macOS 27** (June 2026). A **continuous slider "from ultra clear to fully tinted"** replaces Clear and Tinted (Keynote; State of the Union).
  - Settings › Appearance › Liquid Glass. Endpoints "Most transparent" and "Most tinted"; the midpoint is "Default" **[press: 9to5Mac, June 15, 2026]**.
  - "For developers who have already adopted Liquid Glass, these customizations apply in your apps right away" (Keynote). SwiftUI glass "automatically responds to the new Liquid Glass slider to adjust its tint" (269).
  - **No public API to read the slider value was found** in the 27 docs I checked. Custom-painted (non-system) translucency will **not** follow it.
- **Show Borders.**
  - `@Environment(\.accessibilityShowBorders)`, back-deployed before iOS and macOS 26.1. "On macOS 27 and later, the system provides a dedicated Show Borders setting… On earlier versions of macOS, this value is true when Increased Contrast is enabled."
  - When true, "draw interactive custom controls… with clearly visible edges". The doc sample uses a stroke of `.secondary` on a radius-8 rounded rectangle.
  - "macOS 27 also supports the 'show borders' environment value, just like iOS" (102).

### What custom glass and custom surfaces must do themselves

1. **Test custom elements, colours and animations under** Reduce Transparency, Increase Contrast, Reduce Motion and the Clear/Tinted look (Adopting). System glass adapts; anything you paint does not.
2. **Painted translucency** (not `glassEffect`, `UIGlassEffect` or `NSGlassEffectView`) must read `accessibilityReduceTransparency`. When it is true, "UI (mainly window) backgrounds should not be semi-transparent; they should be opaque."
   - `NSVisualEffectView` and system materials turn opaque by themselves; custom alpha fills don't.
3. **Increase Contrast:** check `colorSchemeContrast == .increased` and supply high-contrast colour variants. Don't add your own border to *system* glass, which already gets one.
4. **Show Borders** (27): add visible edges to custom interactive controls.
5. **Reduce Motion:**
   - Disable elastic and bounce effects on custom glass animations.
   - Avoid "animating into and out of blurs".
   - Reduce zooming, scaling and peripheral motion (HIG Accessibility).
   - `accessibilityPrefersCrossFadeTransitions` is also available.
6. **Contrast floors** (HIG Accessibility, WCAG AA):
   - text up to 17 pt: **4.5:1**;
   - 18 pt and up, or bold: **3:1**.
   - Dark Mode guidance: "no lower than 4.5:1… strive for 7:1, especially in small text" for custom colours.
7. **Accessibility labels** on every icon-only toolbar item.
8. Respect **`appearsActive`**: dim accent and sidebar content in inactive windows, which is now also on iPad.
9. **No opt-out from the new design.** The Info.plist key `UIDesignRequiresCompatibility` "is ignored when you build for iOS 27… macOS 27… or tvOS 27 or later" ([doc](https://developer.apple.com/documentation/bundleresources/information-property-list/uidesignrequirescompatibility)). "We'll be removing support for opting to use the old design" (102).

---

## 11. App icon system

Sources: [HIG App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons) (June 8, 2026), [Creating your app icon using Icon Composer](https://developer.apple.com/documentation/xcode/creating-your-app-icon-using-icon-composer), [WWDC25-220](https://developer.apple.com/videos/play/wwdc2025/220/), [WWDC25-361](https://developer.apple.com/videos/play/wwdc2025/361/), [Adopting, App icons](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass), [WWDC26-101/102](https://developer.apple.com/videos/play/wwdc2026/102/).

### Specifications

| Platform | Canvas | Mask | Style | Appearances |
|---|---|---|---|---|
| iOS, iPadOS, macOS | **1024×1024 px** | Rounded rectangle; rounder new grid, concentric with the UI and hardware | Layered (Icon Composer) | **default, dark, clear light, clear dark, tinted light, tinted dark** |
| watchOS | **1088×1088 px**, which "overshoots" the rounded rectangle on the same grid | Circle | Layered | N/A; the light icon in the new look |
| visionOS | 1024×1024 | Circle | 3D: background plus 1–2 layers | N/A |
| tvOS | 800×480 | Rounded rectangle | Parallax, 2–5 layers | N/A |

- Colour spaces: sRGB, Gray Gamma 2.2, Display P3.
- macOS icons with irregular silhouettes are masked to the shape. Where art can't fit, the system **removes drop shadows and auto-scales** it into the rounded rectangle; redrawing is better (220).

### Layers and material

- A background plus one or more foreground layers.
- Icon Composer organises layers into **at most 4 groups**: "the right bounds for how much visual complexity an icon should have".
- The system applies specular highlights, refraction, translucency, blur, shadow and frostiness. On iOS the highlights respond to **gyro** input.

### Icon Composer controls

- **Groups:** Mode (Individual or Combined), Specular (Automatic, Inside, Outside, Off), Blur, **Refraction** (a 2D strength pad), Translucency, Shadow (Neutral or **Chromatic**).
- **Layers:** Liquid Glass toggle, fill (automatic, solid or gradient), opacity, blend mode.
- **Per-appearance overrides:** default, dark and mono, plus Clear and Tinted previews.
- **Per-platform composition overrides.**
- Annotations were renamed from light/dark/tinted to **default/dark/mono**.
- **2026 (27):**
  - "Additional layers of Liquid Glass directly into the icon artwork… refraction between these layers… icons appear sharper and more defined". This rendering applies to *all* app icons (Keynote 8:58; State of the Union 24:36).
  - New annotations for refraction and content effects.
  - A preview of earlier releases, with a 26 vs 27 toggle.
  - Doc note: "In versions earlier than 27, specular highlights appear on when you choose Inside or Outside, and **Refraction settings have no visible effect**."

### Artwork rules

- Prefer **SVG**. Use PNG for raster art or mesh gradients.
- Convert text to outlines.
- **Don't export the mask.**
- Export at full canvas and number layers back to front.
- Set backgrounds in Icon Composer. Prefer the System Light and System Dark gradients "instead of pure white or black". Prefer a **coloured** background for distinction in dark mode.
- **Remove baked effects:** drop shadows, bevels, blurs, glows and specular. "Let the system handle blurring and other visual effects."
- **Simplify:**
  - solid, filled, overlapping, semi-transparent shapes;
  - a frontal, flat perspective, not realistic 3D;
  - rounder corners;
  - bolder line weights; avoid thin lines and sharp edges;
  - clearly defined edges, no feathering.
- **Mono and tinted:** at least one prominent element should be white, with the others mapped to greys.
- **Consistency.** Keep core features the same across appearances. Alternate icons on iOS need their own dark, clear and tinted variants.

### Delivery

- An `.icon` file in Xcode **replaces** the AppIcon asset catalog.
- Xcode generates images for older OS versions. tvOS and visionOS still use asset catalogs.

---

## 12. API mapping: concept to SwiftUI, UIKit and AppKit

Availability is from the DocC JSON (iOS, iPadOS and Mac Catalyst are abbreviated to iOS). "27" means it is new in the 2026 SDKs.

| Concept | SwiftUI | UIKit | AppKit |
|---|---|---|---|
| Apply glass to a view | `glassEffect(_:in:)` (iOS, macOS, tvOS, watchOS 26) | `UIVisualEffectView(effect: UIGlassEffect(style:))` (iOS, tvOS 26) | `NSGlassEffectView` with `contentView` (macOS 26) |
| Variant | `Glass.regular`, `.clear`, `.identity` | `UIGlassEffect.Style.regular`, `.clear` | `NSGlassEffectView.Style.regular`, `.clear` |
| Tint | `Glass.tint(_:)` | `UIGlassEffect.tintColor` | `NSGlassEffectView.tintColor` |
| Interactive | `Glass.interactive(_:)` | `UIGlassEffect.isInteractive` | `NSGlassEffectView.effectIsInteractive` (**macOS 27**) |
| Shape | `in:` any `Shape`; default `DefaultGlassEffectShape` (capsule) | `UIView.cornerConfiguration` (`UICornerConfiguration`) | `NSGlassEffectView.cornerRadius` (default 8 [measured]); `NSView.cornerConfiguration` (**27**) |
| Group or merge | `GlassEffectContainer(spacing:)` | `UIGlassContainerEffect.spacing` | `NSGlassEffectContainerView.spacing` (default 0) |
| Morph identity | `glassEffectID(_:in:)` | Implicit: frames animated in a container | Implicit: proximity in a container |
| Union at rest | `glassEffectUnion(id:namespace:)` | Overlap frames in a container | Spacing in a container |
| Glass transitions | `glassEffectTransition(.matchedGeometry / .materialize / .identity)` | Animate `effect` (set to `nil` to dematerialize) | — |
| Glass buttons | `.buttonStyle(.glass)`, `.glassProminent`, `.glass(_:)` | `Configuration.glass()`, `.prominentGlass()`, `.clearGlass()`, `.prominentClearGlass()` | `NSButton.BezelStyle.glass`, `bezelColor`, `tintProminence` |
| Button shape | `buttonBorderShape(.capsule / .roundedRectangle(radius:) / .circle)` | `cornerConfiguration` | `NSControl.borderShape` (macOS 26) |
| Control sizes | `controlSize(.mini … .extraLarge)` | — | `NSControl.ControlSize` (`.extraLarge` macOS 26); `NSView.prefersCompactControlSizeMetrics` |
| Concentric shapes | `ConcentricRectangle`, `.rect(corners: .concentric(minimum:))`, `containerShape(_:)`, `ContainerRelativeShape`, `Edge.Corner.Style` | `UICornerRadius.containerConcentric(minimum:)`, `UICornerConfiguration.capsule(maximumRadius:)` | `NSViewCornerRadius.containerConcentric` (**27**); `NSView.LayoutRegion.safeArea(cornerAdaptation:)` |
| Scroll edge effect | `scrollEdgeEffectStyle(_:for:)` (`.automatic`, `.hard`, `.soft`); `scrollEdgeEffectHidden`; `safeAreaBar` | `UIScrollView.top/bottom/left/rightEdgeEffect`; `UIScrollEdgeElementContainerInteraction` | `NSScrollEdgeEffectStyle` (macOS 26.1); titlebar and split-item accessories |
| Background extension | `backgroundExtensionEffect()`, `(isEnabled:)` | `UIBackgroundExtensionView` | `NSBackgroundExtensionView` |
| Toolbar grouping | `ToolbarSpacer(.fixed / .flexible)`; `sharedBackgroundVisibility(_:)` | `UIBarButtonItem.fixedSpace`, `.sharesBackground`, `.hidesSharedBackground` | `NSToolbarItemGroup`; `NSToolbarItem.Identifier.space`; `isBordered = false` |
| Prominent bar item | `.buttonStyle(.glassProminent)` in a toolbar | `UIBarButtonItem.Style.prominent` | `NSToolbarItem.style = .prominent`, `backgroundTintColor` |
| Toolbar space management (**27**) | `visibilityPriority(_:)` (also macOS 26.1); `ToolbarOverflowMenu`; `.topBarPinnedTrailing`; `toolbarMinimizeBehavior(_:for:)` | `navigationItem.barMinimizationBehavior` | Automatic overflow |
| Tab bar minimize | `tabBarMinimizeBehavior(_:)` | `UITabBarController.tabBarMinimizeBehavior` | — |
| Bottom accessory | `tabViewBottomAccessory`; `(isEnabled:)` (26.1); `tabViewBottomAccessoryPlacement` | `UITabAccessory`; `bottomAccessory`; trait `tabAccessoryEnvironment` | — |
| Search tab / prominent tab | `Tab(role: .search)`, `Tab(role: .prominent)` (**27**) | `UISearchTab`; `prominentTabIdentifier` (**27**) | — |
| Search placement | `searchable` plus `searchToolbarBehavior(.minimize)` | `searchBarPlacementBarButtonItem`; `searchBarPlacementAllowsExternalIntegration`; `.integratedCentered` | `NSSearchToolbarItem` |
| Sheet morph from source | `matchedTransitionSource` plus `.navigationTransition(.zoom)` | `preferredTransition = .zoom { item }` | — |
| Popover or action-sheet source | `confirmationDialog` on the button | `popoverPresentationController.sourceItem / sourceView` | `NSAlert.beginSheetModal` |
| Sidebar under content | `NavigationSplitView`; `.inspector` | `UISplitViewController`; `.inspector`; `UITabBarController.Mode.tabSidebar` | `NSSplitViewItem.automaticallyAdjustsSafeAreaInsets`; `init(inspectorWithViewController:)` |
| visionOS glass | `glassBackgroundEffect(displayMode:)` (visionOS 1), `(_:in:displayMode:)` with `.automatic`, `.feathered(padding:softEdgeRadius:)`, `.plate` (visionOS 2.4) | — | — |
| Standard materials | `Material.ultraThin`, `.thin`, `.regular`, `.thick`, `.ultraThick` | `UIBlurEffect`, `UIVibrancyEffect` | `NSVisualEffectView.Material`, `.BlendingMode` |
| Accessibility environment | `accessibilityReduceTransparency`, `colorSchemeContrast`, `accessibilityReduceMotion`, `accessibilityShowBorders`, `appearsActive` | `UIAccessibility.isReduceTransparencyEnabled`; `UITraitCollection.accessibilityContrast`; `activeAppearance` | `NSWorkspace.accessibilityDisplayShouldReduceTransparency`, `…IncreaseContrast` |
| Opt out | — | `UIDesignRequiresCompatibility` (ignored on 27 SDKs) | Same key on macOS |

API names that changed between session code and the shipping docs (use the docs):
- UIKit session `.containerRelative()` is now `UICornerRadius.containerConcentric(minimum:)`.
- SwiftUI session `.rect(corner: .containerConcentric)` is now `.rect(corners: .concentric)`.
- The `searchToolbarBehavior` doc example uses `.minimized`, but the type property is `.minimize`.

---

## 13. Per-platform notes

**iOS (iPhone)**
- Floating, minimizable tab bar with a trailing search tab.
- Bottom toolbar search that slides up with the keyboard.
- Transparent navigation bars and toolbars with grouped glass items.
- Inset half sheets that go opaque at full height.
- Action sheets anchored to their source.
- Capsule controls; capsule and extra margin near screen edges.
- Small glass flips between light and dark.
- 27 additions:
  - navigation bar minimize;
  - prominent tab;
  - optional sidebar;
  - resizable iPhone apps;
  - continuous Liquid Glass slider;
  - `.automatic` scroll edge has its own visuals.

**iPadOS**
- Tab bar at the top, convertible to a sidebar.
- Floating glass sidebar; in 27 it extends to the window edges.
- Window controls and continuous resizing.
- A menu bar, new in iPadOS 26. In 27 menus show few icons by default.
- Inactive windows dim their content (27).
- Use concentric shapes aligned with the window edge.

**macOS (Tahoe 26, then 27)**
- Glass toolbar floating over full-size content, with automatic grouping.
- Sidebars and inspectors:
  - 26: an inset floating sidebar and edge-to-edge inspector glass;
  - 27: the sidebar extends to the window edges, uses semi-bold selection and coloured icons.
- Window corners:
  - 26: larger and varying by style;
  - 27: uniform and tighter, **16 pt [measured]**.
- Control heights changed (8.7). Large and XL controls are capsules.
- Scroll edge:
  - 26: hard is common;
  - 27: automatic resolves to hard with a free-floating title, plus the uniform toolbar.
- Menus with icons in 26, reduced to key actions in 27.
- Interactive glass bounce on click (27).
- A dedicated Show Borders setting (27).
- Desktop tinting: HIG Dark Mode says to include transparency in custom component backgrounds in neutral states so desktop tinting shows through, but not in coloured states.

**visionOS**
- The original glass. Windows use "an unmodifiable system-defined material called *glass*" that adapts to the surroundings.
- "visionOS doesn't have a distinct Dark Mode setting… glass automatically adapts to the luminance of the objects and colors behind it."
- "Prefer translucency to opaque colors in windows". Retain the window's glass background.
- Standard materials for custom parts:
  - **thin** for interactive elements such as buttons and selected items;
  - **regular** to separate sections such as sidebars and grouped tables;
  - **thick** for dark elements on top of regular.
- Buttons on a glass window use the **thin** material. Buttons floating in space use **glass**.
- Vibrancy levels: label, secondaryLabel and tertiaryLabel (tertiary for inactive only).
- Toolbars sit at the bottom edge in a parallel plane, with a variable blur.
- Tab bars are vertical.
- `Glass` and `glassEffect` are **not available on visionOS**. Use `glassBackgroundEffect` (`.automatic`, `.feathered`, `.plate`; display modes `.always`, `.implicit` meaning "only when not already contained in glass", and `.never`).
- Concentric, background-extension and scroll-edge styles are available on visionOS 26.
- Hit target 60×60 pt; buttons at least 60 pt apart.
- Prefer circles and capsules, because eyes are drawn to corners.

**watchOS**
- "Liquid Glass changes are minimal… appear automatically… even if you don't build against the latest SDK". Adopt the watchOS 10 toolbar and button-style APIs.
- App icons are circular, 1088 px, with no appearances.
- Full-screen modal sheets use materials; don't remove them.

**tvOS**
- Glass appears throughout navigation, Top Shelf and Control Center.
- Buttons and image views take glass **on focus**. Adopt the standard focus APIs (`focusable`, `isFocused`, `UIFocusItem`) so custom controls do too.
- Glass button styles apply glass regardless of focus.
- **Liquid Glass requires Apple TV 4K (2nd generation) or newer**; older models keep the old appearance.
- Standard materials for content structure:
  - ultraThin: full-screen light;
  - thin: light overlays;
  - regular: overlays;
  - thick: dark overlays.

**Widgets (iOS, macOS, watchOS)**
- In clear and tinted Home Screen appearances the system uses the `accented` rendering mode. It removes the background and replaces it with "a themed glass or tinted color effect", and tints primary and accent content white.
- Support it with `widgetAccentable(_:)` and `WidgetAccentedRenderingMode` (`accented`, `desaturated`, `accentedDesaturated`, `fullColor`; reserve fullColor for media) ([article](https://developer.apple.com/documentation/widgetkit/optimizing-your-widget-for-accented-rendering-mode-and-liquid-glass)).

---

## 14. Implications for non-Apple platforms: recommendation

Apple's principles carry over to other platforms, but its renderer does not. The parent system should specify glass as a **role with three render tiers**, not as one visual effect.

### 14.1 What carries over unchanged (platform-neutral rules)

1. **Two layers.** Glass is only for the floating navigation and control layer: top bar, tab bar or nav rail, floating toolbar, sidebar on large screens, menus, popovers, sheets and dialogs. The content layer uses opaque or "standard material" surfaces.
2. **No glass on glass.** Anything on a glass surface uses fills and vibrant ink, never another blurred layer.
3. **Regular vs clear.** Clear only over media, always with a dimming layer: 35% black under bright media.
4. **Tint only primary actions.** At most one prominent action per bar and one or two per view. Brand colour lives in the content layer.
5. **Three shape types.**
   - Fixed radius tokens.
   - Capsule, radius = height/2.
   - Concentric, radius = parent radius − inset, with a minimum fallback.
6. **A scroll-edge treatment, not bar backgrounds.** A soft fade or blur under floating bars, a hard opaque band for dense or text bars. One per pane, consistent heights.
7. **Group bar items** into at most three groups. Don't mix text and icon items in one group. Icon items need accessible labels.
8. **Accessibility.**
   - Reduced transparency means opaque.
   - Increased contrast means a black/white-dominant surface with a 1 px contrasting border.
   - Reduced motion means no elastic or bounce, and no animating of blur.

### 14.2 Web (desktop and mobile browsers)

**Tier 1, frosted (baseline)**
- `backdrop-filter: blur() saturate()` with a translucent tint and a 1 px inner highlight.
- Supported in Chromium, Safari and Firefox.
- Use `@supports (backdrop-filter: blur(1px))`, falling back to an opaque surface.

**Tier 2, lensing (progressive enhancement, Chromium only)**
- `backdrop-filter: url(#svg-filter)` with `feDisplacementMap`, built from a precomputed displacement map (refraction via Snell's law, n≈1.5, using a convex-squircle bezel profile) plus a specular-rim image blended on top ([kube.io](https://kube.io/blog/liquid-glass-css-svg/)).
- **Only Chromium renders SVG filters in `backdrop-filter`.**
  - Safari ignores the filter (a WebKit bug).
  - **Firefox parses it, passes `@supports`, then renders nothing**, so the glass disappears ([MDN BCD issue](https://github.com/mdn/browser-compat-data/issues/24110); [Mozilla Connect](https://connect.mozilla.org/t5/ideas/support-svg-filters-in-backdrop-filter-for-advanced-glass/idi-p/98453); [W3C svgwg #1142](https://github.com/w3c/svgwg/issues/1142)).
- Gate it on a user-agent or engine check, not on `@supports`, and keep the Tier 1 values in a separate layer.
- The displacement map must be regenerated when an element's size or shape changes. Animating `scale` is cheap; resizing is expensive.
- **Reserve lensing for a handful of fixed-size controls**, such as a floating tab bar or a toggle knob during drag. Never use it for resizable panes.

**Tier 0, opaque**
- Used when `prefers-reduced-transparency: reduce` (supported in Chromium; treat it as best-effort) or `forced-colors: active`.
- Also used when a performance governor trips, and offered as an explicit in-app "reduce transparency" switch, since there is no reliable media query everywhere.
- `prefers-contrast: more` swaps in the border-and-contrast variant.
- `prefers-reduced-motion` removes elastic morphs.

**Performance budget (recommendation)**
- At most about **4 simultaneously visible backdrop-filtered surfaces** per viewport, and **1** large one (sidebar size).
- No backdrop filters **on scrolling content items**: they are content layer, and each one is a separate compositing pass.
- Don't animate blur radius. Animate opacity and transform only.
- Under 2 ms of compositor cost per frame on mid-range hardware. Verify in DevTools paint profiling.
- Downgrade to Tier 0 on low-end devices (`navigator.hardwareConcurrency ≤ 4`, Save-Data, `prefers-reduced-data`).

**Morphing**
- Emulate container morphing with View Transitions (`view-transition-name`) or FLIP animations on a shared pill.
- Don't attempt metaball merging except in a WebGL canvas.

### 14.3 Android (phones and tablets)

- **No platform glass material.** Material 3 (including M3 Expressive) uses tonal elevation and scrims.
- Primitives:
  - `RenderEffect.createBlurEffect` (API 31+);
  - AGSL `RuntimeShader` (API 33+) for refraction;
  - cross-window background blur (API 31+), which **the system can disable**, for example on low-end devices or in power saving. Check `WindowManager.isCrossWindowBlurEnabled()` and listen for changes.
- Third-party liquid-glass libraries (Kyant's AndroidLiquidGlass, KMP Liquid Glass, Prismal) capture the backdrop and run AGSL. "Most of the performance work lies in backdrop capture and dirty-tracking" **[3rd-party]**.
- **Recommendation:**
  - Use Material navigation patterns: bottom navigation bar, navigation rail on tablets, top app bar, bottom sheets.
  - Express the NEAR glass role as an elevated tonal surface plus a scrim on API < 31.
  - Add blur on API 31+ for floating bars, menus and sheets only.
  - Reserve AGSL lensing for one or two hero controls, behind a capability flag.
  - Always honour the system "remove animations" setting and high-contrast text.
  - Don't put iOS-style floating capsule tab bars on Android unless the brand insists; it fights platform conventions.

### 14.4 Windows and Linux desktop (and Tauri/Electron shells)

- **Windows 11 maps directly onto Apple's split:**
  - **Mica** is "opaque, dynamic… for long-lived windows". Use it for window backgrounds, title bars and sidebars, the equivalent of the large, more opaque glass.
  - **Acrylic** is translucent and blurred, "for transient surfaces" such as menus, flyouts and tooltips: the equivalent of popover and menu glass.
  - **Mica Alt** is for tabbed title bars.
  - Mica blurs the wallpaper once (cheap). Acrylic samples live (expensive).
  - Use the DWM system backdrop (`DWMWA_SYSTEMBACKDROP_TYPE`) rather than painting your own.
- **Linux:** blur is compositor-dependent (KDE yes; GNOME/libadwaita generally no). Default to opaque surfaces with the Tier 1 tint colour; enable blur only where the compositor provides it.
- The trace-commons tokens already note that window-tier tokens (`--tc-blur-window`, `--tc-rim-window`, `--tc-shadow-window`, scene glow) were dropped for macOS because the native material does that work. **The parent system needs them back for Windows, Linux and web**, expressed as the Tier 1 and Tier 0 recipes above.

### 14.5 Where glass must not be used (any platform)

- Content-layer surfaces: cards, list rows, table cells, chart backgrounds, document canvases, chat bubbles, code blocks.
- On top of another glass surface: nested popovers or a toolbar inside a glass sheet. Use fills there.
- Large reading surfaces over busy imagery: use regular or opaque plus a scroll-edge treatment.
- As a modal scrim: use a dimming layer.
- Non-interactive status text and titles in bars (Apple: they "almost look like a button").
- Decoration, or "to make it look premium".
- Under Reduce Transparency, forced colours, low-power or low-end gates: use Tier 0.

---

## 15. Gaps and conflicts to flag for a custom glass system (trace-commons → parent)

Grounded in `design-tokens/glass.tokens.json` and `macos/Sources/TCDesign/Styling/{GlassStyle,GlassBackdrop}.swift` as of v0.15.0.

### Conflicts with Apple guidance

1. **Custom rims and shadows on glass that the system already lights.**
   - The tokens define `paneEdge`, `cardEdge`, `controlEdge`, `ctaEdge` (inset 1 px white highlights at 0.2–0.5 alpha, inset dark shades), and `popoverEdge` / `menuEdge` / `modal` drop shadows (up to y 24, blur 60, 0.5 alpha).
   - `glassEdge()` draws them as strokes and shadows.
   - Apple's glass already has adaptive specular highlights, adaptive shadows (stronger over text, weaker over light backgrounds) and, from 27, **a darkened edge plus brighter specular highlights**.
   - Static painted rims on `NSGlassEffectView` or `glassEffect` surfaces double the rim and don't adapt.
   - **Rule:** no custom edges or shadows on system-glass surfaces. Edges are only for the painted fallback tier (non-Apple, pre-26 macOS, Tier 0/1).

2. **Painted floating surfaces instead of system glass.**
   - `GlassSurfaceBacking.blur` paints popovers, menus and node cards "over a within-window blur… on macOS 26 too (owner ruling, 2026-10-07)".
   - Apple: "remove those custom background views"; use system popovers and menus, which morph from their source, adapt and handle accessibility.
   - Consequences:
     - lost morph-from-source;
     - painted alpha doesn't follow the user's Clear/Tinted or slider setting;
     - Increase Contrast and Reduce Transparency must be hand-built (partly done: the `edgeHighContrast` stroke).
   - **Decide explicitly:** either adopt system presentations on Apple platforms, or document this as a deliberate brand deviation and track the 27 slider gap.

3. **Glass in the content layer.**
   - The code correctly keeps the map pane opaque (`glassPaneIsContent`, "Apple keeps out of Liquid Glass").
   - But any pane that holds *content* (lists, cards, feeds) rendered as `NSGlassEffectView` is content-layer glass, which the HIG forbids.
   - Only the navigation pane (the sidebar equivalent) and inspectors qualify.
   - **The parent spec needs a classification table: surface → navigation layer or content layer.**

4. **Fixed radius tokens vs concentricity.**
   - Tokens: pane 16, card 14, cardQuiet 12, control 8, menuPanel 14.
   - macOS 27 windows measure **16 pt**, so a pane inset by *p* inside the window should be **16 − p** to be concentric. The 26 and 27 window radii also differ.
   - Express nested radii as `concentric(minimum:)` rules: "card = pane − inset, min 8". Keep capsule = height/2 for pills.
   - Watch for Apple's "pinched/flared corner" failure, for example a 14 pt card inside a 16 pt pane with 12 pt padding.

5. **Control height ladder differs from the system.**
   - Tokens: `control` 26, `controlLarge` 28, `cta` 34, `tab` 26, `segmentedTrack` 30.
   - macOS 27 system ladder: 16 / 20 / **24** / **28** / **36**.
   - Mixed system and custom controls will misalign. Shapes also differ: Apple uses rounded rectangles up to regular and capsules from large up; the tokens use `pill` 999 for wells and controls at every size.
   - **Recommend:** adopt the 24/28/36 ladder (and 20/16 for dense panes), or never mix custom and system controls in one row.

6. **Tinted glass panes.**
   - `GlassTheme.glassTint` tints `NSGlassEffectView` panes in the flat theme.
   - Apple: glass has no inherent colour, and "refrain from adding color to the background of multiple controls".
   - Brand purple belongs in the content layer and on the single primary action (`.glassProminent`, accent).

7. **Clear variant.**
   - The code already rejected `.clear` ("showed the desktop unblurred behind a focused window"), which matches Apple's three-condition rule.
   - The `clearTint` flat theme still uses `.clear`. It must add a 35% dimming layer over bright content, or move to regular.

8. **The user's Liquid Glass slider (27) is invisible to painted surfaces.**
   - No public read API was found.
   - Everything painted (cards, wells, popovers) keeps fixed alpha while system glass moves between ultra clear and fully tinted. The surfaces will visibly disagree at the slider extremes.
   - Mitigate by keeping painted surfaces closer to opaque, or by using system glass where possible.

9. **Show Borders (macOS 27) and Increase Contrast.** The code handles Increase Contrast for painted surfaces. Add `accessibilityShowBorders` (back-deployed) for custom interactive controls.

10. **Motion.**
    - Tokens use fixed cubic-bezier durations: fast 0.15, standard 0.22, slow 0.3, ease (0.2, 0.8, 0.2, 1).
    - Apple glass morphs use system springs and `matchedGeometry` / `materialize`.
    - Custom glass morphs should use `withAnimation` / spring with `glassEffectID` inside a container, and Reduce Motion must remove elasticity.
    - Keep the tokens for non-glass UI only.

11. **Containers.**
    - `GlassFloatingGroup` wraps floating controls in `GlassEffectContainer`, which is correct.
    - Every set of nearby glass shapes (toolbar clusters, tab pills, map controls) must share one container, or glass samples glass inconsistently.
    - The default spacing token `s4` should be checked against the "spacing ≤ layout spacing" rule so shapes don't merge at rest unintentionally.

12. **Scroll edge.**
    - Any custom bar (action bar, edge rail, map toolbar) over scrolling content must register with the scroll edge effect (`safeAreaBar`, titlebar or split-item accessory, `UIScrollEdgeElementContainerInteraction`).
    - It should not paint gradient scrims.
    - On 27, prefer `.automatic`; Apple says `.soft` overrides no longer match the system.

13. **App icon.**
    - The Trace mark's live-trace gradient (#5b14ff → #b412c4 → #ff0a6c) must be rebuilt as up to four flat, SVG-exported layers in Icon Composer, with effects (specular, refraction, shadow) set there, not baked in.
    - Provide dark and mono annotations. Mono needs a white key element.
    - On 27, consider per-layer refraction.

14. **No compatibility escape.** With 27 SDKs `UIDesignRequiresCompatibility` is ignored. Any fallback "flat theme" that mimics pre-26 must be self-built and must still obey the content/navigation layer split.

### Gaps in Apple's spec the parent system must fill itself

1. **Numbers Apple does not publish.** Glass blur radius, refraction strength, tint opacity, shadow parameters, and the iOS bar, tab bar and sheet metrics. Apple deliberately leaves them to the renderer.
   - The parent system must define its own Tier 1 and Tier 0 recipes (blur px, tint alpha by size class, rim) for non-Apple platforms.
   - Treat the Apple renderer as the reference look.
2. **Glass motion specification.** Apple publishes no durations or spring parameters. Define spring tokens (response and damping) for web and Android morphs and press feedback, and size the press scale (Apple shows scale, bounce and shimmer without values).
3. **Size thresholds for "small" (flips light/dark) vs "large" (more opaque, no flip).** Not numeric in Apple's docs. The UIKit demo shows 150×44 behaving as small and 250×88 as large. Recommend: any surface under about 64 pt tall and under about 400 pt wide flips; panes and sidebars don't.
4. **A content/navigation classification table** for NEAR AI surfaces, as described in conflict 3.
5. **Brand on glass.** Apple says put brand colour in content and use the accent for the single primary action. The parent system should state where purple may appear on glass: the primary action background, the selection indicator, sidebar icons (27-style), and nowhere else.
6. **Desktop parity with Windows, Linux and web**, as covered in 14.4.

---

## Appendix A: Sources fetched (primary)

**Technology overviews**
- [Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/liquid-glass)
- [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass)

**HIG.** [Materials](https://developer.apple.com/design/human-interface-guidelines/materials) plus Color, App icons, Toolbars, Tab bars, Sidebars, Sheets, Buttons, Search fields, Windows, Popovers, Menus, Sliders, Toggles, Segmented controls, Alerts, Action sheets, Accessibility, Motion, Dark mode, Icons, Scroll views, Split views, Layout, The menu bar, Context menus, Pull-down buttons, Designing for iOS/iPadOS/macOS/visionOS/watchOS/tvOS, Focus and selection, Typography, Widgets, Controls, Panels, Lists and tables. All are under `https://developer.apple.com/design/human-interface-guidelines/<page>`.

**SwiftUI**
- Applying Liquid Glass to custom views.
- The Landmarks sample and four sub-articles.
- `glassEffect`, `Glass` (regular, clear, identity, `tint`, `interactive`), `GlassEffectContainer`, `glassEffectID`, `glassEffectUnion`, `glassEffectTransition`, `GlassEffectTransition` (matchedGeometry, materialize, identity), `DefaultGlassEffectShape`.
- `GlassButtonStyle`, `GlassProminentButtonStyle`, `PrimitiveButtonStyle.glass` / `.glassProminent` / `.glass(_:)`.
- `backgroundExtensionEffect` (both), `scrollEdgeEffectStyle`, `ScrollEdgeEffectStyle` (automatic, hard, soft), `scrollEdgeEffectHidden`, `safeAreaBar`.
- `ToolbarSpacer`, `SpacerSizing`, `sharedBackgroundVisibility`, `tabBarMinimizeBehavior`, `TabBarMinimizeBehavior`, `tabViewBottomAccessory` (both), `TabViewBottomAccessoryPlacement`, `searchToolbarBehavior`, `SearchToolbarBehavior`.
- `ConcentricRectangle`, `rect(corners:isUniform:)`, `containerShape`, `ContainerRelativeShape`, `Edge.Corner.Style`, `concentric(minimum:)`, `RoundedRectangularShape`.
- `ControlSize`, `ButtonBorderShape`, `Material`.
- `glassBackgroundEffect` (three variants), `GlassBackgroundEffect`, `GlassBackgroundDisplayMode`, `FeatheredGlassBackgroundEffect`, `PlateGlassBackgroundEffect`.
- `ToolbarOverflowMenu`, `visibilityPriority`, `topBarPinnedTrailing`, `TabRole`, `TabRole.prominent`.
- `EnvironmentValues` (appearsActive, accessibilityReduceTransparency, colorSchemeContrast, accessibilityReduceMotion, accessibilityShowBorders).

**UIKit**
- `UIGlassEffect` (Style, `init(style:)`, `isInteractive`, `tintColor`), `UIGlassContainerEffect` (`spacing`), `UIBackgroundExtensionView`.
- `UIScrollEdgeEffect` (Style; automatic), `UIScrollView.topEdgeEffect`, `UIScrollEdgeElementContainerInteraction`.
- `UICornerConfiguration`, `UIView.cornerConfiguration`, `UICornerRadius`.
- `UIButton.Configuration` glass ×4.
- `UIBarButtonItem.hidesSharedBackground` / `.sharesBackground` / `.Style.prominent`.
- `UITabAccessory`, `UITabBarController.MinimizeBehavior`, `prominentTabIdentifier`.

**AppKit**
- `NSGlassEffectView` (style ×2, `cornerRadius`, `tintColor`, `effectIsInteractive`, `contentView`), `NSGlassEffectContainerView` (`spacing`), `NSBackgroundExtensionView`.
- `NSControl.ControlSize` (+ extraLarge), `prefersCompactControlSizeMetrics`, `NSButton.BezelStyle.glass`, `NSButton.borderShape`.
- `NSScrollEdgeEffectStyle` (automatic).
- `NSViewCornerConfiguration`, `NSViewCornerRadius`, `NSView.LayoutRegion`.
- `NSToolbarItem.style` / `.backgroundTintColor`, `NSSplitViewItemAccessoryViewController`.

**Other**
- Xcode: Creating your app icon using Icon Composer.
- Bundle Resources: `UIDesignRequiresCompatibility`.
- WidgetKit: Optimizing your widget for accented rendering mode and Liquid Glass.

**Videos.** WWDC25 219, 356, 323, 284, 310, 220 and 361; WWDC26 101, 102, 122, 269, 278, 289, 251, 250, 292, 322, 287, 220 and 272. URLs: `https://developer.apple.com/videos/play/wwdc20XX/<id>/`.

## Appendix B: Not accessed, or uncertain

- **Sample code archives** (Landmarks `.zip`) were not downloaded, so `Constants` values such as the badge radius and badge glass spacing are unknown.
- **Apple Design Resources** (Figma/Sketch UI kits, icon grids) were not downloaded. They are binary downloads that would need explicit permission. Precise iOS 26/27 bar, tab bar and sheet metrics live there, not in the docs.
- **iOS and iPadOS metrics were not measured.** It would need a simulator run. The macOS numbers above are measured; the iOS numbers are not published by Apple.
- **No public API to read the 27 Liquid Glass slider value** was found. The press confirms the slider and its path; Apple docs only say apps inherit it.
- **The window corner radius 16 pt** was read through a private AppKit property on macOS 27.0.1: indicative only.
- **Press-sourced dates** for 26.1, 26.2 and 26.3/26.4 behaviour came from 9to5Mac, Tom's Guide, MacRumors, anderegg.ca and mjtsai. They are not in Apple docs.
