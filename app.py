#!/usr/bin/python3
import os
from src.customer_crawler import CustomerCrawler
from src.data_processor import ProcessData
from src.utils.setup_logging import SetupLogging
from src.utils.get_config import Config
import logging
import asyncio

SetupLogging().setup_logging()
config = Config().parse()
office = config['office']['city']
distance = config['radius']
download_path = os.path.join(os.getcwd(), config['data_storage'])
export_path = os.path.join(os.getcwd(), config['export_path'])

def main():
    logging.info("App started")
    CustomerCrawler().run()

    if download_path:
        process_data = ProcessData(download_path, export_path, office,
                                   distance)
        process_data.calc()
        return True
    else:
        logging.info("Dataset is missing at the path")
        return False

if __name__ == '__main__':
    main()

