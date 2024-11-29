from models.preferences import Preferences,ValidationError
from dal.mongo_client import preferences_collection


def update_preferences(preferences:Preferences):
    try:
        if not preferences_collection.find_one({"user_id":preferences.user_id}):
            raise ValueError("Preferences not found.")
    
        preferences_collection.update_one({"user_id":preferences.user_id},{"$set":preferences.model_dump()})
        return{"message":"Preferences updated successfully."}
    
    except ValidationError as ve:
        print(f"Validation error: {ve}")
        return {"message": "Invalid preferences data"}
    
    except Exception as e:
        print(f"Error updating preferences: {e}")
        #f"An error occurred - {str(e)}
        return {"message":f"An error occurred while updating preferences- {str(e)}"}

def get_preferences(user_id: str) :
    print("Querying preferences for user_id:", user_id)  # Debugging
    preferences = preferences_collection.find_one({"user_id": user_id})
    
    if not preferences:
        print("No preferences found, returning defaults.")  # Debugging
        return {"categories": [], "delivery_channel": "email"}
    
    preferences.pop('_id', None)
    print("Preferences found:", preferences)  # Debugging
    return preferences


    