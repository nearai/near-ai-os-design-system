"""Checks for the Near AI OS Design System. Exits non-zero on any error.

usage: python3 scripts/check.py [--strict]

  - every color role has a valid value in every theme
  - contrast floors: parent themes must pass; a product theme that misses a
    floor is reported as flagged (it may not ship until fixed); --strict
    turns flagged product failures into errors too
  - dist/ is up to date with the token source and css/
  - every var(--…) in css/ and in component previews is a real token
  - every component has a README and a preview with a valid card marker
  - docs sections have titles, and the published page's 24-section cap holds
"""
import json
import os
import re
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import build  # noqa: E402
from contrast import checks  # noqa: E402

errors, warnings = [], []
src = build.load()
strict = '--strict' in sys.argv

# Values
HEX = re.compile(r'^#([0-9a-f]{3,4}|[0-9a-f]{6}|[0-9a-f]{8})$', re.I)
theme_ids = [t['id'] for t in src['themes']]
for name, role in src['color'].items():
    for tid in theme_ids:
        v = role['values'].get(tid)
        if v is None or not HEX.match(v):
            errors.append('color %s: bad or missing value for %s: %r' % (name, tid, v))
for name, b in src['brand'].items():
    if not HEX.match(b['value']):
        errors.append('brand %s: bad value %r' % (name, b['value']))

# Contrast
products = {t['id']: t['product'] for t in src['themes']}
for tid, token, label, ratio, floor in checks(src):
    if ratio < floor - 1e-9:
        line = '%s: %s is %.2f:1, floor %.1f:1' % (tid, label, ratio, floor)
        if products[tid] == 'parent' or strict:
            errors.append('contrast ' + line)
        else:
            warnings.append('flagged (blocks shipping the %s theme) %s' % (products[tid], line))

# dist/ drift
with tempfile.TemporaryDirectory() as tmp:
    build.build(tmp)
    for dirpath, _, files in os.walk(tmp):
        for f in files:
            new = os.path.join(dirpath, f)
            rel = os.path.relpath(new, tmp)
            old = os.path.join(ROOT, 'dist', rel)
            if not os.path.exists(old) or open(old).read() != open(new).read():
                errors.append('dist/%s is stale: run make build' % rel)

# Token references
art = build.artifact_tokens(src)
names = set()
for key, fam in art.items():
    if isinstance(fam, dict) and 'tokens' in fam:
        names.update(t['name'] for t in fam['tokens'])
names.update('font-' + k for k in art['type']['families'])
styles = {s['name'] for g in art['type']['groups'] for s in g['styles']}


def refs(text, where):
    for v in sorted(set(re.findall(r'var\(--([A-Za-z0-9_.-]+)', text))):
        if not v.startswith('nr-') and v not in names:
            errors.append('%s: var(--%s) is not a token' % (where, v))


for p in sorted(os.listdir(os.path.join(ROOT, 'css'))):
    if p.endswith('.css'):
        refs(open(os.path.join(ROOT, 'css', p)).read(), 'css/' + p)

# Components
comp_root = os.path.join(ROOT, 'components')
MARKER = re.compile(r'<!-- @dsCard( group="[A-Za-z]+")? height=\d+( subtitle="[^"]*")?( width=\d+)? -->$')
for c in sorted(os.listdir(comp_root)):
    d = os.path.join(comp_root, c)
    if not os.path.isdir(d):
        continue
    files = os.listdir(d)
    if c != 'Cover':
        if 'README.md' not in files:
            errors.append('components/%s: no README.md' % c)
        elif not open(os.path.join(d, 'README.md')).read().startswith('# '):
            errors.append('components/%s/README.md: no # title' % c)
    if 'preview.html' not in files:
        errors.append('components/%s: no preview.html' % c)
        continue
    html = open(os.path.join(d, 'preview.html')).read()
    if not MARKER.match(html.split('\n', 1)[0]):
        errors.append('components/%s/preview.html: bad card marker' % c)
    if re.search(r'<(iframe|frame|object|embed|portal|noscript)\b', html, re.I):
        errors.append('components/%s/preview.html: forbidden element' % c)
    for url in re.findall(r'(?:src|href)="(https?:[^"]+)"', html):
        errors.append('components/%s/preview.html: external url %s' % (c, url))
    refs(html, 'components/%s/preview.html' % c)
    for cls in set(re.findall(r'class="([^"]+)"', html)):
        for k in cls.split():
            if re.match(r'^(mac|web|ios|android|hero)-', k) and k not in styles:
                errors.append('components/%s/preview.html: unknown type class %s' % (c, k))

# Docs
sections = []
for dirpath, _, files in os.walk(os.path.join(ROOT, 'docs')):
    for f in files:
        if f.endswith('.md'):
            p = os.path.join(dirpath, f)
            rel = os.path.relpath(p, ROOT)
            if rel != 'docs/brand-book.md':
                sections.append(rel)
                if not open(p).readline().startswith('# '):
                    errors.append('%s: no # title' % rel)
            text = open(p).read()
            for bad in ('colour', 'behaviour'):
                if re.search(r'\b' + bad, text, re.I):
                    errors.append('%s: British spelling "%s"' % (rel, bad))
if len(sections) > 24:
    errors.append('docs: %d sections; the published page shows at most 24' % len(sections))

for w in warnings:
    print('warning:', w)
for e in errors:
    print('error:', e)
print('%d errors, %d warnings; %d themes, %d color roles, %d components, %d sections'
      % (len(errors), len(warnings), len(theme_ids), len(src['color']),
         len([c for c in os.listdir(comp_root) if os.path.isdir(os.path.join(comp_root, c))]), len(sections)))
sys.exit(1 if errors else 0)
