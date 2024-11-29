from flask import Blueprint, request, jsonify
from models.news_request import NewsRequest
from pydantic import ValidationError
from services.news_service import fetch_and_filter_news

news_bp = Blueprint('News', __name__)

@news_bp.route('/aggregate', methods=['POST'])
def aggregate_news():
    try:
        data = request.get_json()
        print(data)
        news_request = NewsRequest(**data)
        articles = fetch_and_filter_news(
            categories=news_request.categories,
            language=news_request.language,
            max_articles=news_request.max_articles
        )
        
        return jsonify(articles), 200
    
    except ValidationError as ve:
        return jsonify({"message": "Invalid data", "errors": ve.errors()}), 400
    
    except Exception as e:
        return jsonify({"message": "An error occurred"}), 500
