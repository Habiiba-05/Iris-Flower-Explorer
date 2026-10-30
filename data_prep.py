"""
Step 2: Data Preparation
-------------------------
Loads Iris.csv, cleans it with pandas, and saves:
  - clean_iris.csv   (cleaned data)
  - summary.json      (basic stats, written with the json module -> File Handling lecture)

Run this once from the project folder:
    python data_prep.py
"""
import json
import pandas as pd

# ---- Load ----
df = pd.read_csv("Iris.csv")

# ---- Clean ----
df = df.drop_duplicates()
df = df.dropna()
df["Species"] = df["Species"].str.replace("Iris-", "", regex=False)

# ---- Save cleaned CSV ----
df.to_csv("clean_iris.csv", index=False)
print("Saved clean_iris.csv:", len(df), "rows")

# ---- Build a small JSON summary (File Handling lecture: working with JSON) ----
summary = {}
for species, group in df.groupby("Species"):
    summary[species] = {
        "count": int(len(group)),
        "avg_sepal_length": round(group["SepalLengthCm"].mean(), 2),
        "avg_sepal_width": round(group["SepalWidthCm"].mean(), 2),
        "avg_petal_length": round(group["PetalLengthCm"].mean(), 2),
        "avg_petal_width": round(group["PetalWidthCm"].mean(), 2),
    }

with open("summary.json", "w") as f:
    json.dump(summary, f, indent=4)

print("Saved summary.json")
