from flask import Flask
from services.orchestrator_service import OrchestratorService
from routes.orchestrator_routes import orchestrator_bp
from services.news_service import NewsService
from services.preferences_service import PreferencesService
from services.notification_service import NotificationService
from dapr.dapr_client import DaprServiceClient

def create_app():
    app = Flask(__name__)
    
    dapr_client = DaprServiceClient()

    # Initialize services
    user_service = PreferencesService(dapr_client)
    news_service = NewsService(dapr_client)
    notification_service = NotificationService(dapr_client)

    # Initialize the OrchestratorService with the services
    orchestrator_service = OrchestratorService(user_service=user_service,
                                               news_service=news_service,
                                               notification_service=notification_service)

    app.register_blueprint(orchestrator_bp, url_prefix='/api')
    
    app.orchestrator_service = orchestrator_service

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5003)
