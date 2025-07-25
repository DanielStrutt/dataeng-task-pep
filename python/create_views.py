import duckdb
import os
import glob

# Set up paths
base_dir = os.path.dirname(os.path.abspath(__file__))
sql_dir = os.path.join(base_dir, '..', 'sql')
db_path = os.path.join(base_dir, '..', 'data', 'steam_data.duckdb')

# Find all SQL files prefixed with vw_
sql_files = sorted(glob.glob(os.path.join(sql_dir, 'vw_*.sql')))

con = duckdb.connect(db_path)

for sql_file in sql_files:
    with open(sql_file, 'r', encoding='utf-8') as f:
        sql = f.read()
    print(f"Running {os.path.basename(sql_file)}...")
    con.execute(sql)

con.close()
print("All view scripts executed.")