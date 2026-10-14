"""Derive a product accent family from one seed color.

usage: python3 scripts/accent.py "#6d14f3"

Holds the seed's OKLCH hue and chroma and steps its lightness until each
accent role meets the parent floors over the worst-case grounds of the parent
light and dark themes. Prints the minimum passing values; pin them, with a
little margin, into a product theme's columns in tokens/near-ai.tokens.json.
Nothing is written for you.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from colorkit import contrast, cr, hex_to_rgba, oklch_hex, rgb_to_hex, to_oklch  # noqa: E402
from contrast import grounds  # noqa: E402


def darken8(hx):
    r, g, b, _ = hex_to_rgba(hx)
    return rgb_to_hex(max(0, r - .08), max(0, g - .08), max(0, b - .08))


def worst(hx, gr):
    return min(cr(hx, *g) for g in gr.values())


def main():
    seed = sys.argv[1]
    src = json.load(open(os.path.join(ROOT, 'tokens', 'near-ai.tokens.json')))
    floors = src['contrast']['floors']
    L0, C0, H0 = to_oklch(seed)
    print('seed %s  OKLCH L %.3f C %.3f H %.1f' % (seed, L0, C0, H0))
    for theme in [t for t in src['themes'] if t['id'] in ('light', 'dark')]:
        gr = grounds(src, theme)
        dark = theme['appearance'] == 'dark'
        ladder = [oklch_hex(i / 200, C0, H0) for i in range(20, 197)]
        on = '#071a2e' if dark else '#ffffff'
        fill = [h for h in ladder if worst(h, gr) >= floors['mark']
                and contrast(hex_to_rgba(on), hex_to_rgba(h)) >= floors['text']]
        fill = fill[0] if dark else (fill[-1] if fill else None)
        text = [h for h in (oklch_hex(i / 200, C0 * (0.6 if dark else 0.9), H0) for i in range(20, 197))
                if worst(h, gr) >= floors['text']]
        text = text[0] if dark else (text[-1] if text else None)
        soft = [h for h in ladder if cr(h, src['color']['pane-opaque']['values'][theme['id']]) >= floors['mark']]
        soft = min(soft, key=lambda h: abs(to_oklch(h)[0] - L0)) if soft else None
        print('\n%s theme' % theme['id'])
        if not fill:
            print('  no accent fill at this hue holds the floors; choose another seed')
            continue
        print('  accent          %s   (%.2f:1 on the worst ground; label %.2f:1)'
              % (fill, worst(fill, gr), contrast(hex_to_rgba(on), hex_to_rgba(fill))))
        print('  accent-pressed  %s' % darken8(fill))
        print('  text-on-accent  %s' % on)
        print('  accent-text     %s   (%.2f:1)' % (text, worst(text, gr)) if text else '  accent-text     none at this hue')
        print('  accent-soft     %s' % soft)
        print('  accent-tint     %s at %d%%' % (soft, 22 if dark else 14))
        print('  focus-ring, selection: accent; menu-hover: accent at 90%')


if __name__ == '__main__':
    main()
