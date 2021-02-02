import requests
from mock import patch, MagicMock
import pytest
import os
from src.customer_crawler import CustomerCrawler

data_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_customers.csv',
)

class TestRequests:
    thread = 1
    path = data_path

    @pytest.fixture
    def crawler(self):
        return CustomerCrawler(self.thread,self.path)

    def test_spider(self, crawler):
        crawler.spider()
        assert crawler.jobqueue.qsize() > 0