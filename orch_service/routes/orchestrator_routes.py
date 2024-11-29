from flask import Blueprint, jsonify, current_app

# Define the Orchestrator Blueprint
orchestrator_bp = Blueprint('orchestrator', __name__)

@orchestrator_bp.route('/get_news_and_notify/<user_id>', methods=['GET'])
def get_news_and_notify(user_id):
    orchestrator_service = current_app.orchestrator_service
    orchestrator_service.get_news_and_notify(user_id)
    
    return jsonify({"message": "News fetched and notification sent!"}), 200
