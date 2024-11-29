from flask import Blueprint, request, jsonify
from models.notification import NotificationRequest
from services.sending_notification_serivice import send_notification
from pydantic import ValidationError
import json
import logging

logger = logging.getLogger(__name__)

notification_bp = Blueprint('Notification', __name__)

@notification_bp.route('/send', methods=['POST'])
def send_notification_route():
    try:
        data = request.get_json()
        message = json.loads(data['data'])
        logger.fatal(message)
        notification_request = NotificationRequest(**message)
        response = send_notification(
            recipients=notification_request.recipients,
            subject=notification_request.subject,
            message=notification_request.message
        )
        
        return jsonify(response),200
    except ValidationError  as ve:
         return jsonify({"message": "Invalid data", "errors": ve.errors()}), 400
    except Exception as e:
        return jsonify({"message": "An error occured"}),500
        
        