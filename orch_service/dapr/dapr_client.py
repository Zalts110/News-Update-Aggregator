from dapr.clients import DaprClient
import json
import logging

class DaprServiceClient:
    def __init__(self):
        self.client = DaprClient()
        self.logger = logging.getLogger(__name__)

    def invoke_service(self, app_id, method_name, data=None, http_verb="POST"):
        response = self.client.invoke_method(
            app_id=app_id,
            method_name=method_name,
            data=json.dumps(data) if data else None,
            content_type="application/json",
            http_verb=http_verb,
        )
        self.logger.fatal(response)
        data = response.data
        
        return json.loads(data.decode('utf-8'))

    def publish_event(self, pubsub_name, topic_name, data):
        self.client.publish_event(pubsub_name, topic_name, json.dumps(data))
