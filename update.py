import requests, json

all_contracts = []
offset = 0
limit = 1000

while True:
    r = requests.get(
        "https://api.nfldata.org/v1/contracts",
        params={"limit": limit, "offset": offset},
        timeout=30
    )
    r.raise_for_status()
    payload = r.json()
    batch = payload.get("data", [])
    all_contracts.extend(batch)
    if len(batch) < limit:
        break
    offset += limit

active = [c for c in all_contracts if c.get("year_signed", 0) >= 2024]

with open("nfl_contracts.json", "w") as f:
    json.dump(active, f)

print(f"Saved {len(active)} active contracts")
