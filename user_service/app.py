from flask import Flask
from routes import user_routes, preferences_routes

app = Flask(__name__)

# Register routes
app.register_blueprint(user_routes.user_bp)
app.register_blueprint(preferences_routes.preferences_bp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
