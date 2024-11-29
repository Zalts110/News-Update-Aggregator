from flask import Blueprint, jsonify, request
from services.preferences_service import PreferencesService
from services.news_service import NewsService
from services.notification_service import NotificationService
import logging

# Define the Orchestrator Blueprint
orchestrator_bp = Blueprint('orchestrator', __name__)

class OrchestratorService:
    def __init__(self, user_service: PreferencesService, news_service: NewsService, notification_service: NotificationService):
        self.user_service = user_service
        self.news_service = news_service
        self.notification_service = notification_service
        self.logger = logging.getLogger(__name__)

    def get_news_and_notify(self, user_id):
        user_preferences = self.user_service.get_preferences(user_id)
        news_data = self.news_service.get_news(user_preferences)
        
        delivery_channel = user_preferences.get('delivery_channel')
        
        if delivery_channel == 'email':
            user_mail = self.user_service.get_user_mail(user_id)
            self.notification_service.send_notifications(payload=news_data, user_mail=user_mail)
