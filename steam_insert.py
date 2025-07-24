import os
import json
import pandas as pd
from config import CSV_PATH, JSON_PATH

def steam_insert():
    if os.path.exists(CSV_PATH):
        return False

    if not os.path.exists(JSON_PATH):
        print(f"{JSON_PATH} not found.")
        return True

    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    rows = []
    for entry in data:
        if not isinstance(entry, dict) or "appid" not in entry:
            continue
        platforms = entry.get("platforms", [])
        row = {
            "appid": entry.get("appid"),
            "name": entry.get("name"),
            "price": entry.get("price"),
            "release_date": entry.get("release_date"),
            "required_age": entry.get("required_age"),
            "genres": entry.get("genres"),
            "achievements": entry.get("achievements"),
            "positive_ratings": entry.get("positive_ratings"),
            "negative_ratings": entry.get("negative_ratings"),
            "windows": "windows" in platforms,
            "mac": "mac" in platforms,
            "linux": "linux" in platforms,
        }
        rows.append(row)

    df = pd.DataFrame(rows)
    df.to_csv(CSV_PATH, index=False)
    print(f"Created {CSV_PATH} with {len(df)} rows.")
    return True