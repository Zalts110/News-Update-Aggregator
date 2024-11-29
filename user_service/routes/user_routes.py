from flask import Blueprint,request,jsonify
from services.user_service import create_user, update_user, get_user_mail_from_db
from models.user import User
from pydantic import ValidationError

user_bp = Blueprint('User',__name__)

@user_bp.route('/register',methods=['POST'])
def register_user():
    data = request.get_json()
    
    try:
        user = User(**data)
        response = create_user(user)
        return jsonify(response),201
    
    except ValidationError as ve:
        return jsonify({"message":"Invalid data","errors":ve.errors()}),400
    
    except Exception as e:
        return jsonify({"message": f"An error occurred - {str(e)}"}), 500
    
    
@user_bp.route('/<user_id>',methods=['PUT'])
def modify_user(user_id):
    data = request.get_json()
    
    try:
        response = update_user(user_id,data)
        return jsonify(response),200
    
    except Exception as e:
        print("user")
        return jsonify({"message":"An error occurred"}),500
    
@user_bp.route('/<user_id>',methods=['GET'])
def get_user_mail(user_id):
    try:
        response = get_user_mail_from_db(user_id)
        return jsonify(response),200
    
    except Exception as e:
        print("user")
        return jsonify({"message":"An error occurred"}),500
    
        
        
