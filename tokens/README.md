# Token source

`near-ai.tokens.json` is the only file to edit by hand. `make build` generates everything in `dist/` from it.

| Key | Shape | Notes |
|---|---|---|
| `themes` | `[{id, name, appearance, contrast, product}]` | `appearance` is `light` or `dark` (it picks the worst-case desktop); `contrast` is `standard` or `increased` (7:1 text); `product` is `parent` or a product id. The first theme is the default. |
| `contrast` | `{worstDesktop, floors}` | The ground model and the floors the checks hold. |
| `color.<role>` | `{usage, values: {<theme id>: "#rrggbb[aa]"}}` | One value per theme, always all six. Alpha is the last byte. |
| `brand.<name>` | `{value, usage}` | Theme-independent colors for marks. Never on controls. |
| `shadow.tokens.<name>` | `{usage, values: {<theme id>: "<box-shadow>"}}` | CSS box-shadow per theme. |
| `spacing`, `radius`, `size`, `opacity`, `blur`, `zIndex`, `breakpoint` | `{note, tokens: {<name>: {value, usage}}}` | Plain CSS values. Names are unique across every family (they become `--<name>`). |
| `motion.durations`, `motion.easings` | `{<name>: {value, usage}}` | |
| `motion.springs.<name>` | `{stiffness, damping, usage}` | Mass-1 springs. The build writes the CSS `linear()` curve and its settle duration, SwiftUI `response = 2π/√stiffness`, and Compose `spring(dampingRatio, stiffness)`. |
| `type.families` | `{<key>: "<font stack>"}` | `apple`, `web`, `android`, `mono`. |
| `type.steps.<step>` | `{usage, sample}` | The eleven steps. |
| `type.tiers[]` | `{id, name, family, note, styles: {<step>: {size, lineHeight, weight, tracking, maps}}}` | `maps` names the platform text style (`body`, `title3`, `bodyLarge` …). The CSS class is `<tier>-<step>`. |
| `type.hero` | `{name, family, note, styles: {<name>: {size, lineHeight, weight, tracking, sample, usage}}}` | The two hero styles. |

Values are pinned, not computed at build time. The parent accents and the increased-contrast inks were solved against the floors once; to derive a new accent family use `make accent SEED=#rrggbb` and write the result here. A token that misses a floor gets the miss appended to its usage note in the generated files, and `make check` reports it.
