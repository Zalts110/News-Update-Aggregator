from dapr.dapr_client import DaprServiceClient
import json
import logging

class PreferencesService:
    
    def __init__(self, dapr_client: DaprServiceClient):
        self.dapr_client = dapr_client
        self.app_id = 'user_service'
        self.logger = logging.getLogger(__name__)
    
    def get_preferences(self, user_id: str):
        response = self.dapr_client.invoke_service(
            app_id=self.app_id,
            method_name= f'preferences/{user_id}',
            http_verb='GET'
        )
        return response
    
    
    def get_user_mail(self, user_id: str):
        response = self.dapr_client.invoke_service(
            app_id=self.app_id,
            method_name= f'/{user_id}',
            http_verb='GET'
        )
        
        return response.get('user_mail', '')
