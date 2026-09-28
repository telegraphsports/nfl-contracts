!pip install nflreadpy

import nflreadpy as nfl

import polars as pl
active = contracts.filter(pl.col("is_active") == True)

rows = ""
for r in active.iter_rows(named=True):
    rows += (
        f"<tr><td>{r.get('player')}</td><td>{r.get('position')}</td>"
        f"<td>{r.get('team')}</td><td>{r.get('year_signed')}</td>"
        f"<td>{r.get('years')}</td><td>${r.get('value'):.1f}M</td>"
        f"<td>${r.get('apy'):.1f}M</td><td>${r.get('guaranteed'):.1f}M</td></tr>\n"
    )

html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<title>NFL Active Contracts</title>
<style>
  body {{ font-family: sans-serif; margin: 2rem; }}
  table {{ border-collapse: collapse; width: 100%; }}
  th, td {{ border: 1px solid #ccc; padding: 6px 10px; text-align: left; }}
  th {{ background: #1a1a2e; color: #fff; cursor: pointer; }}
  tr:nth-child(even) {{ background: #f5f5f5; }}
</style></head><body>
<h1>Active NFL Player Contracts</h1>
<p>Source: OverTheCap via nflreadpy. Values in millions.</p>
<table>
<thead><tr>
  <th>Player</th><th>Pos</th><th>Team</th><th>Signed</th>
  <th>Yrs</th><th>Total</th><th>APY</th><th>Guaranteed</th>
</tr></thead>
<tbody>
{rows}
</tbody></table>
<script>
document.querySelectorAll('th').forEach((th, i) => {{
  th.onclick = () => {{
    const t = th.closest('table'), rows = .rows];
    const asc = th.dataset.asc = th.dataset.asc !== '1';
    rows.sort((a, b) => {{
      const x = a.cells .innerText, y = b.cells .innerText;
      return asc ? x.localeCompare(y, undefined, {{numeric:true}})
                 : y.localeCompare(x, undefined, {{numeric:true}});
    }});
    rows.forEach(r => t.tBodies[0].appendChild(r));
  }};
}});
</script>
</body></html>"""

with open("nfl_contracts.html", "w") as f:
    f.write(html)

print("Wrote nfl_contracts.html")
