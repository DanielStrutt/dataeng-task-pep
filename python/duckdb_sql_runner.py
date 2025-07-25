import duckdb
from tabulate import tabulate
import os
from config import CSV_PATH, SQL_PATH

with open(SQL_PATH, 'r', encoding='utf-8') as f:
    query = f.read()

# Replace placeholder if you want to use {csv_path} in your SQL
query = query.format(csv_path=CSV_PATH)

con = duckdb.connect()
result = con.execute(query).fetchdf()

print(tabulate(result, headers='keys', tablefmt='psql'))
con.close()