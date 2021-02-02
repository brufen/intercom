import requests
from mock import patch, MagicMock
import pytest
import os
from src.customer_crawler import CustomerCrawler

data_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_customers.csv',
)

test_data = {"latitude": "53.74452", "user_id": 1, "name": "user1",
             "longitude":
    "-7.11167"}

class TestRequests:
    thread = 1
    path = data_path

    @pytest.fixture
    def response_text(self):
        return test_data

    @pytest.fixture
    def crawler(self):
        return CustomerCrawler(self.thread,self.path)

    @patch('requests.get')
    def test_get_customers(response_text, crawler):
        mockresponse = MagicMock()
        crawler._get_customers = mockresponse
        mockresponse.text = response_text

