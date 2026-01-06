import requests

API_KEY = "YOUR_NEWSAPI_KEY"
BASE_URL = "https://newsapi.org/v2/everything"

def fetch_news(keyword=None, source=None, from_date=None, to_date=None):
    params = {
        "apiKey": API_KEY,
        "q": keyword,
        "sources": source,
        "from": from_date,
        "to": to_date,
        "language": "en",
        "pageSize": 50
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()["articles"]
