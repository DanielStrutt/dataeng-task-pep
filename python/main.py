from steam_insert import steam_insert
from steam_update import steam_update

def main():
    # steam_insert returns True if file was created, False if it already existed
    inserted = steam_insert()
    if not inserted:
        print("File exists, running updates.")
        steam_update()

if __name__ == "__main__":
    main()