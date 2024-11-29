import unittest
from unittest.mock import patch
from app import app


class TestNewsService(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    @patch('services.news_service.fetch_and_filter_news')  # Adjust the path if necessary
    def test_aggregate_news(self, mock_fetch_and_filter_news):
        # Set the mock return value
        mock_fetch_and_filter_news.return_value = [
            {"title": "Food News 1"},
            {"title": "Sports News 1"}
        ]

        # Send the POST request
        response = self.client.post('/news/aggregate', json={
            "categories": ["food", "sports"],
            "language": "en",
            "max_articles": 5
        })

        # Debugging prints
        print("Was the mock called?", mock_fetch_and_filter_news.called)
        print("Response JSON:", response.json)

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 2)
        self.assertEqual(response.json[0]["title"], "Food News 1")
        self.assertEqual(response.json[1]["title"], "Sports News 1")


if __name__ == '__main__':
    unittest.main()
