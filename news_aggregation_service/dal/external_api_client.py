import requests

class ExternalAPIClient:
    NEWS_API_URL = "https://newsdata.io/api/1/news"
    API_KEY = "pub_59620521282b1730d85e3f6d9b92918fcb355"  # Replace with your actual API key

    @staticmethod
    def fetch_news(categories: str, language: str, max_articles: int):
        params = {
            "apikey": ExternalAPIClient.API_KEY,
            "q": categories,
            "language": language,
            "size": max_articles
        }
        response = requests.get(ExternalAPIClient.NEWS_API_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching news: {response.status_code} - {response.text}")
            return None
