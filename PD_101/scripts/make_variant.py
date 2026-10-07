"""Generate alongside the baseline so dir::project.v keeps its meaning."""
from pathlib import Path
import argparse,json
p=argparse.ArgumentParser(); p.add_argument('--util',type=int,required=True); p.add_argument('--period',type=float,required=True)
a=p.parse_args()
if not 10 <= a.util <= 80 or a.period <= 0: p.error('util must be 10..80 and period positive')
d=Path(__file__).resolve().parents[1]/'files/design'
c=json.loads((d/'config.json').read_text()); c.update(FP_CORE_UTIL=a.util,CLOCK_PERIOD=a.period)
out=d/f'config_u{a.util}_t{a.period:g}.json'
out.write_text(json.dumps(c,indent=2)+'\n'); print(out)
