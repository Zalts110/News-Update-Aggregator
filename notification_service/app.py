from flask import Flask
from routes.notification_routes import notification_bp

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(notification_bp, url_prefix="/notification")

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5002)
