from dapr.dapr_client import DaprServiceClient
from typing import Dict, Any
import logging

class NewsService:
    
    def __init__(self, dapr_client: DaprServiceClient):
        self.dapr_client = dapr_client
        self.app_id = 'news_aggregation_service'
        self.logger = logging.getLogger(__name__)
    
    def get_news(self, preferences: Dict[str, Any]) -> str:
        data = {
            "categories": preferences.get('categories', []),
            "language": preferences.get('language', 'en'),
            "size": preferences.get('size', 3)
        }
        
        try:
            response = self.dapr_client.invoke_service(
                app_id=self.app_id, 
                method_name='news/aggregate',
                data=data, 
                http_verb='POST'
            )
            
            return response.get('articles', []) 

        except Exception as e:
            print(f"Error invoking service: {e}")
            return "Error fetching news"
