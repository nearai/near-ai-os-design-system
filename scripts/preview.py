"""Render component previews to PNG with headless Chrome.

usage:
  python3 scripts/preview.py <Component> [theme,theme,…]   one component
  python3 scripts/preview.py --all [theme,theme,…]          every component, plus contact sheets

Writes build/render/<Component>-<theme>.png (and build/render/sheet-NN.png
for --all). Previews load dist/css/tokens.css and dist/css/near-ai.css the
way the published page loads tokens.css and bundle.css; uploaded-asset URLs
(/_blob/<id>) resolve to the files in assets/ through artifact.json.
Set CHROME to the browser binary if it is not at the default macOS path.
"""
import json
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CHROME = os.environ.get('CHROME', '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
OUT = os.path.join(ROOT, 'build', 'render')


def asset_map():
    meta = json.load(open(os.path.join(ROOT, 'artifact.json')))
    out = {}
    for group in meta['assetGroups'].values():
        for f in group['files']:
            out['/_blob/' + f['blob']] = 'file://' + os.path.join(ROOT, f['path'])
    return out


def shot(comp, themes):
    src = os.path.join(ROOT, 'components', comp, 'preview.html')
    html = open(src).read()
    first, body = html.split('\n', 1)
    h = re.search(r'height=(\d+)', first)
    w = re.search(r'width=(\d+)', first)
    height = int(h.group(1)) if h else 200
    width = int(w.group(1)) if w else (960 if comp == 'Cover' else 760)
    for blob, path in asset_map().items():
        body = body.replace(blob, path)
    os.makedirs(OUT, exist_ok=True)
    head = ('<link rel="stylesheet" href="file://%s"><link rel="stylesheet" href="file://%s">'
            % (os.path.join(ROOT, 'dist', 'css', 'tokens.css'), os.path.join(ROOT, 'dist', 'css', 'near-ai.css')))
    pngs = []
    for th in themes:
        doc = body.replace('<html', '<html data-theme="%s"' % th, 1)
        doc = doc.replace('<head>', '<head>' + head, 1) if '<head>' in doc else head + doc
        page = os.path.join(OUT, '%s-%s.html' % (comp, th))
        open(page, 'w').write(doc)
        png = page[:-5] + '.png'
        subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--allow-file-access-from-files',
                        '--window-size=%d,%d' % (width, height + 8), '--screenshot=%s' % png, 'file://' + page],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=90)
        pngs.append(png)
    return pngs


def sheets(comps, themes):
    """Contact sheets: each component in the first two themes, side by side."""
    pair = themes[:2]
    out = []
    for i in range(0, len(comps), 6):
        rows = ''.join(
            '<div style="display:flex;gap:6px;margin-bottom:6px;align-items:flex-start">'
            '<div style="width:110px;font:12px sans-serif">%s</div>%s</div>'
            % (c, ''.join('<img src="%s-%s.png" style="width:640px;border:1px solid #ccc">' % (c, t) for t in pair))
            for c in comps[i:i + 6])
        page = os.path.join(OUT, 'sheet-%02d.html' % (i // 6))
        open(page, 'w').write('<html><body style="margin:6px;background:#fff">%s</body></html>' % rows)
        png = page[:-5] + '.png'
        subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--allow-file-access-from-files',
                        '--window-size=1410,2400', '--screenshot=%s' % png, 'file://' + page],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=90)
        out.append(png)
    return out


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    if sys.argv[1] == '--all':
        themes = sys.argv[2].split(',') if len(sys.argv) > 2 else ['light', 'dark']
        comps = sorted(c for c in os.listdir(os.path.join(ROOT, 'components'))
                       if os.path.isdir(os.path.join(ROOT, 'components', c)))
        with ThreadPoolExecutor(6) as ex:
            list(ex.map(lambda c: shot(c, themes), comps))
        print('\n'.join(sheets([c for c in comps if c != 'Cover'], themes)))
    else:
        themes = sys.argv[2].split(',') if len(sys.argv) > 2 else ['light', 'dark']
        print('\n'.join(shot(sys.argv[1], themes)))
