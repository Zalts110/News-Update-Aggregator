from dapr.dapr_client import DaprServiceClient
import logging

class NotificationService:
    def __init__(self, dapr_client: DaprServiceClient):
        self.dapr_client = dapr_client
        self.pubsub_name = 'pubsub'  # Name of your pub/sub component
        self.topic_name = 'notifications'    # Topic to which messages will be published
        self.logger = logging.getLogger(__name__)
        
    def send_notifications(self, payload, user_mail):
        # Log the details
        self.logger.info(f'Sending notification with payload: {payload} to user: {user_mail}')
        
        self.logger.fatal(f'sending message to queue')
        
        message = {
            "subject": 'News Update',
            "recipients": [user_mail],
            "message": payload
        }
        
        # Publish the event to RabbitMQ
        try:
            self.dapr_client.publish_event(
                pubsub_name=self.pubsub_name,
                topic_name=self.topic_name,
                data=message
            )
            self.logger.info("Notification published successfully.")
        except Exception as e:
            self.logger.error(f"Failed to publish notification: {e}")
