import duckdb
from tabulate import tabulate
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
sql_path = os.path.join(base_dir, '..', 'config', 'sql_script.sql')
csv_path = os.path.join(base_dir, '..', 'data', 'target_steam_flattened.csv')

with open(sql_path, 'r', encoding='utf-8') as f:
    query = f.read()

# Replace placeholder if you want to use {csv_path} in your SQL
query = query.format(csv_path=csv_path)

con = duckdb.connect()
result = con.execute(query).fetchdf()

print(tabulate(result, headers='keys', tablefmt='psql'))
con.close()