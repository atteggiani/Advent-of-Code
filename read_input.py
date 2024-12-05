import requests

# Replace with your session cookie value
SESSION_COOKIE = "53616c7465645f5f7a41f976c65b9af8e5b8a59e552e95157a19e1c128f85dae73bd9b9a08612a2da81b17120bdf83b4377a2d9b8605f581bab096a8a733e00f"

def read_input(day: int | str) -> str:
    # URL for the input data (update the year and day as needed)
    url = f'https://adventofcode.com/2024/day/{day}/input'

    # Send a GET request with the session cookie for authentication
    cookies = {'session': SESSION_COOKIE}
    response = requests.get(url, cookies=cookies)

    # Check if the request was successful
    if response.status_code == 200:
        return response.text.split()
    else:
        raise requests.RequestException(f"Failed to fetch input data. Status code: {response.status_code}")