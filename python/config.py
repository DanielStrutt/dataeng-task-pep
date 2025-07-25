import os
import glob

# Get the absolute path to the project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Paths to data files
CSV_PATH = os.path.join(PROJECT_ROOT, "data", "target_steam_flattened.csv")
JSON_PATH = os.path.join(PROJECT_ROOT, "data", "source_steam.json")
DB_PATH = os.path.join(PROJECT_ROOT, "data", "steam_data.duckdb")

# SQL paths
SQL_DIR = os.path.join(PROJECT_ROOT, 'sql')
SQL_PATH = os.path.join(SQL_DIR, 'test_sql_script.sql')

# SQL files prefixed with vw_
SQL_VIEW_FILES = sorted(glob.glob(os.path.join(SQL_DIR, 'vw_*.sql')))
