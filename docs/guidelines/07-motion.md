# Motion

Motion explains a change: where something came from, where it went, what responded to a touch. It is calm by default. Fades and fills use one curve; anything that moves uses a spring; nothing moves under Reduce Motion (decision NDS-11).

## The one curve

`ease-standard`, cubic-bezier(0.2, 0.8, 0.2, 1), is trace-commons' single curve. Use it for every change that does not move: fades, fill changes, hover, press, focus, color, opacity.

| Duration | Value | For |
|---|---|---|
| `duration-fast` | 150ms | Hover and press fills, focus ring, checkbox, chip selection |
| `duration-reveal` | 180ms | A compact pill or row expanding in place |
| `duration-standard` | 220ms | Modal fade, pane show and hide, menus appearing |
| `duration-slide` | 250ms | Footers and peeks sliding in, sub-list swaps |
| `duration-slow` | 300ms | Large-surface fades on the web and Android |
| `duration-spin` | 800ms | One spinner turn (`ease-linear`) |
| `duration-pulse` | 1600ms | One skeleton pulse (to `opacity-skeleton` and back) |

`ease-exit` (cubic-bezier(0.3, 0, 1, 1)) is for elements leaving for good on the web.

## Springs

Anything that changes position or size uses a spring, defined by stiffness and damping ratio. Native code uses the parameters; the web uses the `linear()` rendering of the same spring and its settle time.

| Token | Stiffness | Damping | Settles | For |
|---|---|---|---|---|
| `spring-spatial-fast` | 1400 | 0.9 | 224ms | Small moves: a switch knob, a segment's selection, a tab indicator |
| `spring-spatial` | 700 | 0.9 | 317ms | Panes opening, sheets, popovers and menus growing from their source |
| `spring-spatial-slow` | 300 | 0.9 | 484ms | Full-screen and window-level changes |
| `spring-effects` | 1600 | 1.0 | 231ms | Color, opacity and blur that must not overshoot |
| `spring-expressive` | 800 | 0.6 | 360ms | One or two hero moments per product |
| `spring-ember` | 322 | 0.85 | 488ms | The main-tab ember gliding between tabs (Trace) |

The standard springs are Material 3's standard motion scheme (damping 0.9), the closest match to Apple's calm defaults. The expressive spring is Material Expressive's fast spatial spring; it overshoots by about 9%, so keep it for content-layer hero moments: a first contribution, a completed agent run, onboarding's last step. Never use it for navigation, chrome or anything a person does many times a day.

| Platform | How to write a spring |
|---|---|
| SwiftUI | `.spring(response: 2π/√k, dampingFraction: ζ)`; for `spring-spatial` that is response 0.237, damping 0.9 |
| Jetpack Compose | `spring(dampingRatio = ζ, stiffness = k)`, or the M3 `MotionScheme.standard()` and `.expressive()` |
| Web | `transition: transform var(--duration-spring-spatial) var(--spring-spatial)` |

## Choreography

- **Grow from the source.** Menus, popovers, sheets and inspectors grow from the control that opened them (`spring-spatial`) and return to it when dismissed. Liquid Glass does this natively on Apple; emulate it on the web with View Transitions or a FLIP animation.
- **Navigation uses the platform default.** Push, pop, back swipe and predictive back are the system's; never replace them with custom or bouncy transitions.
- **Panes on the desktop** open by growing the window to the right on the `duration-standard` clock and the one curve; nothing else in the window moves.
- **Nothing fidgets.** Ambient loops (a shimmer, an aurora, a pulsing glow) run at most once on appearance or on a slow interval (trace-commons' map shimmer runs once, then every 40 seconds) and never behind text people are reading.
- **Press feedback** is a fill 8% darker on `duration-fast` on Apple, the web, Windows and Linux. Android may add Material's shape morph on press for buttons outside glass chrome.
- **Streaming output** appears in place without moving what is above it. Keep the reading position; never auto-scroll a person who has scrolled up.
- **Numbers** that update live change in place with tabular digits; do not count up decoratively.

## Reduce Motion

Under Reduce Motion (`prefers-reduced-motion`, Android's remove-animations setting), every change jumps to its end state:
- fades may remain, at `duration-fast`, but nothing slides, scales or bounces;
- springs, shape morphs and glass morphing stop;
- blur never animates;
- spinners stand still with their label, skeletons stop pulsing;
- loops hold one frame;
- desktop panes change the window frame at once.

trace-commons checks Reduce Motion in every component that animates; every parent component does the same.

## Haptics

On iPhone and Android, pair a light impact with a switch flipping, a selection snapping and a pull-to-refresh threshold; a success notification haptic with a completed send; an error haptic with a refused action. Never use haptics for streaming text, hover or anything continuous. Respect the system's haptics setting.
