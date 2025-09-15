import sys
from client import api

def main():
    if len(sys.argv) < 2:
        print("Usage: movie-client <year> [<year> ...]")
        sys.exit(1)

    years = sys.argv[1:]
    for year in years:
        try:
            count = api.get_movies_count(year)
            print(f"{year}: {count} movies found")
        except Exception as e:
            print(f"{year}: Error - {e}")

if __name__ == "__main__":
    main()
