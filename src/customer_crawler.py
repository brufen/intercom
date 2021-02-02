import threading
import os
import requests
import json
import csv
import queue
import logging
from src.utils.utils import get_header, write_file
from src.utils.setup_logging import SetupLogging
from src.utils.get_config import Config
import src.utils.errors as app_errors


class CustomerCrawler:
    """
    Represents data crawler
    """

    def __init__(self, thread = 1, path = os.getcwd()):
        self.thread = thread
        self.path = path
        self.jobqueue = queue.Queue()
        self.url = self.get_url()
        self.headers = get_header()

    def _get_customers(self):
        """
        Get customers from provided URL
        """

        try:
            response = requests.get(url = self.url, headers
            =self.headers)
            response.raise_for_status()
        except requests.RequestException as e:
            logging.info('RequestException url', url)
            logging.error(e)
            return None
        except Exception as e:
            logging.error(e)
            return None
        logging.info(f"Response {response.status_code} from {self.url}")
        return response.text

    def get_url(self):
        """
        Get URL
        """
        config = Config().parse()
        return config['url']

    def spider(self):
        """
        Responsible for processing response
        """

        data = self._get_customers()
        if data:
            for line in data.splitlines():
                self.jobqueue.put(json.loads(line))


    def run(self):
        """
        Stores data in a file
        """
        thread_list = []
        for i in range(self.thread):
            t = threading.Thread(target = self.spider)
            thread_list.append(t)
        for t in thread_list:
            t.setDaemon(True)
            t.start()
        for t in thread_list:
            t.join()
        if os.path.exists(self.path):
            data_list = []
            self.path = os.path.join(self.path, Config().parse()[
                'data_storage'])
            while not self.jobqueue.empty():
                data_list.append(self.jobqueue.get())
            if data_list:
                with open(self.path, 'w', newline = '') as f:
                    f_csv = csv.DictWriter(f, fieldnames = data_list[0].keys())
                    f_csv.writeheader()
                    for i in data_list:
                        f_csv.writerow(i)
                logging.info(f"Data saved to {self.path}")
            else:
                raise app_errors.DataError

