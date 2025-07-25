import duckdb
from config import DB_PATH, CSV_PATH

con = duckdb.connect(DB_PATH)
con.execute(f"""
    CREATE TABLE IF NOT EXISTS steam_flattened AS
    SELECT * FROM read_csv_auto('{CSV_PATH}');
""")
con.close()

print(f"Created DuckDB database at {DB_PATH}")