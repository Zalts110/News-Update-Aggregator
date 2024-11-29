from flask import Blueprint,request,jsonify
from services.preferences_serivce import update_preferences,get_preferences
from models.preferences import Preferences
from pydantic import ValidationError


preferences_bp = Blueprint('Preferences',__name__)

@preferences_bp.route('/preferences/<user_id>',methods=['PUT'])
def modifiy_preferences(user_id):
    data = request.get_json()
   
    try:
        preferences = Preferences(user_id=user_id, **data)
        response = update_preferences(preferences)
        return jsonify(response),200
    
    except ValidationError as ve:
        return jsonify({"message":"Invalid data","errors":ve.errors()}),400
    except Exception as e:
        
        print("preferences")
        return jsonify({"message": f"An error occurred - {str(e)}"}),500
    
@preferences_bp.route('/preferences/<user_id>', methods=['GET'])
def fetch_preferences(user_id):
    try:
        print("Fetching preferences for user_id:", user_id)  # Debugging step
        response = get_preferences(user_id)
        return jsonify(response), 200
    except Exception as e:
        print(f"Error fetching preferences: {e}")  # Debug unexpected errors
        return jsonify({"message": "An error occurred"}), 500

