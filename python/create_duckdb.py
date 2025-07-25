import duckdb
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, '..', 'data', 'steam_data.duckdb')
csv_path = os.path.join(base_dir, '..', 'data', 'target_steam_flattened.csv')

con = duckdb.connect(db_path)
con.execute(f"""
    CREATE TABLE IF NOT EXISTS steam_flattened AS
    SELECT * FROM read_csv_auto('{csv_path}');
""")
con.close()

print(f"Created DuckDB database at {db_path}")