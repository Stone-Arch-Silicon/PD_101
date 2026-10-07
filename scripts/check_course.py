from pathlib import Path
import re, json, ast
root = Path(__file__).resolve().parents[1]
errors = []
for n in range(1,13):
    p = root/'Pages'/f'page_{n}.md'
    if not p.exists():
        errors.append(str(p)); continue
    t = p.read_text(encoding='utf-8')
    for heading in ['## Read first', '## Lab', '## Exercises', '## Checkpoint']:
        if heading not in t: errors.append(f'{p}: missing {heading}')
for p in root.rglob('*.md'):
    if p.name == 'TEMPLATE.md': continue
    for u in re.findall(r'\]\(([^\s)]+)',p.read_text(encoding='utf-8')):
        if ':' not in u and not u.startswith('#'):
            target=(p.parent/u.split('#')[0]).resolve()
            if not target.exists(): errors.append(f'{p.relative_to(root)}: {u}')
for p in root.rglob('*.json'): json.loads(p.read_text(encoding='utf-8'))
for p in root.rglob('*.py'): ast.parse(p.read_text(encoding='utf-8'),filename=str(p))
if errors: raise SystemExit('\n'.join(errors))
print('PASS: 12 lessons, required sections, local Markdown links, JSON, Python syntax')
