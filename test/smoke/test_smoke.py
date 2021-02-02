import pytest
from src.customer_crawler import CustomerCrawler
from app import main

def test_aa_smoke():
    app = main()
    assert app is not None
    assert app == True

