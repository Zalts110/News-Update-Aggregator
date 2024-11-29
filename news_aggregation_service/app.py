from flask import Flask
from routes.news_routes import news_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(news_bp, url_prefix='/news')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
