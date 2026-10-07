"""Inventory numerical metrics with their source; missing keys are never zero."""
import argparse,csv,json,sys
from pathlib import Path
p=argparse.ArgumentParser(); p.add_argument('run',type=Path); a=p.parse_args()
if not a.run.is_dir(): p.error('run directory does not exist')
writer=csv.writer(sys.stdout); writer.writerow(['source','key','value'])
def walk(x,prefix=''):
    if isinstance(x,dict):
        for k,v in x.items(): yield from walk(v,f'{prefix}.{k}' if prefix else k)
    elif isinstance(x,(int,float)) and not isinstance(x,bool): yield prefix,x
found=0
for file in sorted(a.run.rglob('*metrics*.json')):
    try: data=json.loads(file.read_text())
    except (ValueError,OSError) as e: raise SystemExit(f'{file}: {e}')
    for k,v in walk(data): writer.writerow([file.relative_to(a.run),k,v]); found+=1
if not found: raise SystemExit('No numerical metric entries found; inspect report files directly.')
