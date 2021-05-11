import requests


def post(url, json):
    response = requests.post(url, json=json)
    if response.status_code != 200:
        return response.status_code, "Invalid response"
    return response.status_code, response.json()


def get(url):
    response = requests.get(url, headers={"User-Agent": "Chrome"})
    if response.status_code != 200:
        return response.status_code, "Invalid response"
    return response.status_code, response.json()
