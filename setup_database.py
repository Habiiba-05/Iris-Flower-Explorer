"""
Step 3: Build the Database
----------------------------
Same pattern as the Book Store example (setup_database.py):
reads a CSV with pandas, then writes it into a SQLite database.

Run once, AFTER data_prep.py:
    python setup_database.py
"""
import sqlite3
import pandas as pd

df = pd.read_csv("clean_iris.csv")

connection = sqlite3.connect("iris.db")

df.to_sql(
    "iris",
    connection,
    if_exists="replace",
    index=False
)

connection.close()

print("Database created successfully: iris.db")
