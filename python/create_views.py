import duckdb
import os
import glob
from config import DB_PATH

import duckdb
from config import DB_PATH, SQL_VIEW_FILES

# Connect to DuckDB
con = duckdb.connect(DB_PATH)

# Execute each view creation SQL script
for sql_file in SQL_VIEW_FILES:
    with open(sql_file, 'r', encoding='utf-8') as f:
        sql = f.read()
    print(f"Running {os.path.basename(sql_file)}...")
    con.execute(sql)

con.close()
print("All view scripts executed.")
