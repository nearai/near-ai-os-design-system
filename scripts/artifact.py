"""Assemble the published Design System artifact's files from this repository.

usage: python3 scripts/artifact.py [note]

Writes build/artifact/project/… in the layout the Design System page reads:
  README.md                 <- docs/brand-book.md
  guidelines/ patterns/ reference/  <- docs/…
  tokens.json               <- dist/artifact/tokens.json
  components/<Name>/…       <- components/<Name>/…
  components/bundle.css     <- dist/css/near-ai.css
  assets/<Group>/README.md  <- assets/<group>/README.md
  design-system.json        the index, with the uploaded asset records from artifact.json

Then prints the `files` map to publish with the Artifact tool:
  url = artifact.json "url", root = build/artifact,
  file_path = build/artifact/project/design-system.json, files = the printed map.
SVGs are not sent as files: they are uploaded assets (asset: true), recorded in
artifact.json. Upload a new or changed SVG first and record its id there.
"""
import datetime
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, 'build', 'artifact')


def copy(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(src, dst)


def main():
    note = sys.argv[1] if len(sys.argv) > 1 else 'Published from the Near AI OS Design System repository.'
    meta = json.load(open(os.path.join(ROOT, 'artifact.json')))
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    proj = os.path.join(OUT, 'project')
    copy(os.path.join(ROOT, 'docs', 'brand-book.md'), os.path.join(proj, 'README.md'))
    for sub in ('guidelines', 'patterns', 'reference'):
        for f in sorted(os.listdir(os.path.join(ROOT, 'docs', sub))):
            copy(os.path.join(ROOT, 'docs', sub, f), os.path.join(proj, sub, f))
    copy(os.path.join(ROOT, 'dist', 'artifact', 'tokens.json'), os.path.join(proj, 'tokens.json'))
    copy(os.path.join(ROOT, 'dist', 'css', 'near-ai.css'), os.path.join(proj, 'components', 'bundle.css'))
    for c in sorted(os.listdir(os.path.join(ROOT, 'components'))):
        d = os.path.join(ROOT, 'components', c)
        if os.path.isdir(d):
            for f in os.listdir(d):
                copy(os.path.join(d, f), os.path.join(proj, 'components', c, f))
    for group, g in meta['assetGroups'].items():
        folder = os.path.dirname(g['files'][0]['path'])
        copy(os.path.join(ROOT, folder, 'README.md'), os.path.join(proj, 'assets', group, 'README.md'))
    now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    index = {
        'v': 3, 'layout': 'files', 'createdOnFiles': {'v': 1, 'at': now}, 'title': meta['title'],
        'namespace': meta['namespace'], 'libraries': [], 'sections': {}, 'groups': list(meta['assetGroups']),
        'assetGroups': {gname: {'name': gname, 'tile': g['tile'], 'order': [f['name'] for f in g['files']],
                                'files': {f['name']: {'name': f['name'], 'blob': f['blob'], 'size': f['size'],
                                                      'type': 'image/svg+xml'} for f in g['files']}}
                        for gname, g in meta['assetGroups'].items()},
        'blobs': {}, 'docs': {'sections': []},
        'lastChange': {'by': 'Ron', 'at': now, 'via': 'Near AI OS Design System repository', 'note': note},
    }
    with open(os.path.join(proj, 'design-system.json'), 'w') as f:
        json.dump(index, f, indent=2)
        f.write('\n')
    files = {}
    for dirpath, _, fs in os.walk(proj):
        for f in fs:
            rel = os.path.relpath(os.path.join(dirpath, f), OUT)
            if rel != 'project/design-system.json':
                files[rel] = rel
    print(json.dumps(dict(sorted(files.items())), indent=0))
    print('%d files; index at %s' % (len(files), os.path.join(proj, 'design-system.json')), file=sys.stderr)
    print('Note: when the page already exists, read its index first and keep its createdOnFiles object.',
          file=sys.stderr)


if __name__ == '__main__':
    main()
