import json
import pandas as pd
import os
from config.config import CSV_PATH, JSON_PATH

def steam_update():
    if not os.path.exists(CSV_PATH):
        print(f"{CSV_PATH} does not exist. Please run insert first.")
        return

    # Load old CSV and new JSON
    old_df = pd.read_csv(CSV_PATH)
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

    new_df = pd.DataFrame(rows)

    # Ensure appid is comparable
    old_df["appid"] = old_df["appid"].astype(str)
    new_df["appid"] = new_df["appid"].astype(str)

    # Records Inserted: in new_df but not in old_df
    inserted = new_df[~new_df["appid"].isin(old_df["appid"])]
    # Records Deleted: in old_df but not in new_df
    deleted = old_df[~old_df["appid"].isin(new_df["appid"])]
    # Records Updated: in both, but with any column different (excluding appid)
    merged = pd.merge(old_df, new_df, on="appid", suffixes=('_old', '_new'))
    updated = merged[
        (merged.filter(regex='_old$').values != merged.filter(regex='_new$').values).any(axis=1)
    ]

    new_df.to_csv(CSV_PATH, index=False)
    print(f"Updated data in {CSV_PATH} with {len(new_df)} records.")
    print(f"Records Inserted: {len(inserted)}")
    print(f"Records Updated: {len(updated)}")
    print(f"Records Deleted: {len(deleted)}")