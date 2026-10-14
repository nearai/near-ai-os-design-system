# TabBar

A tab bar switches between three to five top-level destinations on a phone: a floating glass capsule over the content on iPhone and touch web, or the 64-tall M3 navigation bar docked to the bottom on Android.

## When to use

- Phones and compact windows under 600, for the app's top-level destinations (Home, Agents, Private AI, Settings).
- Not for actions (use `Toolbar`), not for views inside one screen (`Tabs` or `SegmentedControl`), and not at 600 and wider, where `NavigationRail` (Android, web) or the iPad tab bar that adapts to a sidebar takes over.
- Never with a `NavigationRail` or a docked `Toolbar` on the same screen. Screens below the top level that need a toolbar hide the tab bar.

## Anatomy

1. **Bottom accessory** `.nr-tabbar__accessory` (optional, iPhone): a glass capsule 48 tall above the tabs, for one persistent app-wide feature, such as the agent run in progress with its Stop button (36 visible, 44 target).
2. **Tabs** `.nr-tabbar__tabs`: a glass capsule (`glass-veil` + `pane-fill` over `blur-bar`, `shadow-float`), 4 padding, 2 between tabs.
3. **Tab** `.nr-tabbar__tab`: a 24 icon (`space-24`) over its label, 2 apart, padding 6 above and 4 below, at least 44 tall (`target-touch-apple`), equal widths.
4. **Search tab** `.nr-tabbar__search` (optional): its own glass circle at the trailing end, at least 44.
5. **Badge** `.nr-tabbar__badge`: 16 tall, `badge-fill` with `text-on-status`, on the icon's upper right.
6. **Pinning** `--pinned`: 16 from the sides (`margin-compact`), 8 above the bottom edge. On a page, use `position: fixed` and add `env(safe-area-inset-bottom)`.
7. **Docked** (`--docked`): full width, 64 tall (`space-64`), square corners, no shadow, a 56 by 32 indicator around the icon, the label 4 below.

## Sizes by density

| | touch iOS (floating) | touch Android (docked) | touch web | regular, compact, dense |
|---|---|---|---|---|
| Bar height | about 60 (44 tabs + padding) | 64 | as iOS | not used |
| Tab target | 44 or more | full item, 64 tall | 48 | |
| Icon | 24 | 24 | 24 | |
| Label | `ios-micro`, medium; semibold selected | `android-caption`, medium; semibold selected | `web-micro` | |
| Accessory | 48 | not used | 48 | |

## Variants

- **Floating** (default): iOS 26 and touch web.
- **Docked** (`--docked`): the M3 flexible navigation bar on Android.
- **Minimized** (`--minimized`, iPhone only): after a scroll down, only the selected tab's icon stays, the accessory moves inline and the search tab stays at the trailing end. A scroll up or a tap restores the bar.
- **With accessory**, **with search tab**: optional, iOS and touch web.

## States

| State | Floating | Docked |
|---|---|---|
| Default | icon and label `text-secondary` | same |
| Pressed | `filter: brightness(0.92)` | same |
| Selected | `aria-current="page"`: a `neutral-tint` lens behind the tab, icon and label `accent-text`, semibold | indicator `selection` with a `text-on-accent` icon; label `accent-text`, semibold |
| Hover (pointer on touch web) | none on the floating bar | `control-hover` on the indicator |
| Focus | 2px `focus-ring`, 2px outside (NDS-5) | same |
| Disabled | never; an empty destination shows its empty state | same |
| Badge | a count, or a dash when unknown; none at zero | same |

## Behavior

- **Selection**: a tap switches destination and keeps each destination's own state (stack and scroll). Tapping the current tab returns its stack to the root, then scrolls to the top.
- **Keyboard** (iPad keyboards, touch web): Tab reaches the bar; Left and Right move between tabs; Return selects.
- **Scroll**: on iPhone the bar may minimize on scroll down. It never minimizes or hides while VoiceOver or TalkBack is running.
- **Search**: selecting the search tab replaces the bar with a search field.
- **Motion**: selection fills change on `duration-fast`; minimizing and restoring run on `spring-spatial` over `duration-spring-spatial`; under Reduce Motion the bar changes at once.
- **Covering**: only a sheet, a modal or the keyboard may cover the bar.

## Accessibility

- A `nav` with a label from the product; tabs are links with `aria-current="page"`. Labels always show; never icon-only.
- Badge counts are hidden; their words ride in the tab's name ("1 needs your approval").
- The accessory is a named group; its Stop button names the run ("Stop Inbox triage").
- Labels hold 4.5:1 over the worst-case ground; `accent-text` holds on every ground `text-primary` uses. Selection is carried by the lens or indicator, the ink and the weight together.
- At large text sizes labels may grow to twice their size; iOS shows the large content viewer on a long press.
- **The product supplies**: destinations, icons, labels, badge counts and their words, the accessory's content and actions, the search label.

## Platforms

| SwiftUI/UIKit (iOS/iPadOS) | Jetpack Compose M3 | Web | SwiftUI/AppKit (macOS) |
|---|---|---|---|
| System `TabView` with `Tab`, `Tab(role: .search)`, `.tabBarMinimizeBehavior(.onScrollDown)` and `.tabViewBottomAccessory`; the system Liquid Glass bar is kept, never repainted. iPad: `.sidebarAdaptable` | `ShortNavigationBar` (flexible, 64dp) or `NavigationBar`; `NavigationSuiteScaffold` switches to the rail at medium width | Custom: this CSS, `position: fixed`, safe-area insets | Not used |

## Do and don't

- Do keep three to five tabs with one-word labels.
- Do keep the bar visible on every top-level screen.
- Don't put actions in the bar or in the accessory; a screen's own action belongs with its content.
- Don't disable, hide or reorder tabs while the app runs.
- Don't tint the whole bar with the brand; color goes only on the selected tab.

## Source

Intentional addition: trace-commons is macOS-only and has no phone navigation. The floating variant follows the iOS 26 Liquid Glass tab bar (minimize on scroll, bottom accessory, separate search tab; HIG tab bars, `apple-liquid-glass.md` §7 and §8.2). The docked variant follows the M3 Expressive flexible navigation bar (64dp, 56 by 32 indicator; `m3-components-B.md` §2). Selection maps both onto the parent accent (NDS-1, NDS-13).
