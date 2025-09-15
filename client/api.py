import requests
import time

USERNAME = "username"
PASSWORD = "password"
SERVER_URL = "http://localhost:8080"

def authenticate():
    response = requests.post(
        f"{SERVER_URL}/api/auth",
        json={"username": USERNAME, "password": PASSWORD}
    )
    response.raise_for_status()
    return response.json().get("bearer")

def get_movies_count(year):
    count = 0
    page = 1
    token = authenticate()
    headers = {"Authorization": f"Bearer {token}"}

    print(f"Fetching movies for {year}:", end=" ", flush=True)

    while True:
        url = f"{SERVER_URL}/api/movies/{year}/{page}"
        response = requests.get(url, headers=headers)

        if response.status_code == 401:
            # Token expired
            time.sleep(0.5)
            token = authenticate()
            headers["Authorization"] = f"Bearer {token}"
            continue

        if response.status_code == 404:
            break

        if not response.ok:
            raise Exception(f"Failed to fetch movies for {year}: {response.text}")

        data = response.json()
        count += len(data)

        if len(data) < 10:
            break

        page += 1

    print(f"{count} movies found")
    return count