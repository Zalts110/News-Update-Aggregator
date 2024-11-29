from dal.mongo_client import users_collection,preferences_collection
from models.user import User
from models.preferences import Preferences

#function to create a user
def create_user(user:User):
    
    if users_collection.find_one({"user_id":user.user_id}):
        raise ValueError("User already exists.")
    
    
    users_collection.insert_one(user.model_dump())
    
    default_preferences = Preferences(user_id=user.user_id, categories=[], delivery_channel="email")
    preferences_collection.insert_one(default_preferences.model_dump())
    
    return{"message":"User created successfully."}
    

#function to update a user 
def update_user(user_id,updated:dict):
    if not users_collection.find_one({"user_id":user_id}):
        raise ValueError("User not found.")
    #$set method is used to update the users fields with the updated fields , he know to update only the fields that are passed in the updated dictionary
    users_collection.update_one({"user_id":user_id},{"$set":updated})
    return{"message":"User updated successfully."}

def get_user_mail_from_db(user_id):
    if not users_collection.find_one({"user_id":user_id}):
        raise ValueError("User not found.")
    
    user_data = users_collection.find_one({"user_id":user_id})
    return { 'user_mail': user_data.get('email', '' ) }



