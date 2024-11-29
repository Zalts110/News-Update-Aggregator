from dal.external_api_client import ExternalAPIClient
from typing import List

def fetch_and_filter_news(categories: List[str], language: str, max_articles: int):
    joined_categories = ",".join(categories)
    raw_data = ExternalAPIClient.fetch_news(joined_categories, language, max_articles)
    
    if not raw_data or "results" not in raw_data:
        return []
    
    articles = {'articles': [
        {"title": item["title"], "url": item["link"]}
        for item in raw_data["results"]
        if "title" in item and "link" in item
    ]}
    
    return articles
