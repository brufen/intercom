import time
import os
import csv
from src.utils.get_config import Config
from enum import Enum

config = Config().parse()


class Direction(Enum):
    """
    Sort direction class
    """
    DESC = True
    ASC = False


def get_header():
    """
    Sending identification to server where we crawl data
    """
    return {
        'User-ASgent': config['user_agent']
    }


def get_time():
    """
    Get current time
    """
    return int(time.time())


def get_coordinates(city):
    """
    Get coordinates for given city
    """
    lat = config['office']['coordinates']['lat']
    long = config['office']['coordinates']['long']
    return {"latitude": lat, "longitude": long}


def write_file(path, list, newline):
    """
    Write to file data from list
    """
    with open(path, 'w', newline = newline) as f:
        f_csv = csv.DictWriter(f, fieldnames = list[0].keys())
        f_csv.writeheader()
        for i in list:
            f_csv.writerow(i)
    return True


def sort_list(list_of_dicts, order_by, Direction):
    """
    Sort list of dictionaries using built in sorted function based on given
    field and
    direction
    """
    sorted_list = sorted(list_of_dicts, key = lambda x: x[order_by],
                         reverse = False)
    return sorted_list

def check_keys(data_dict, keys):
    """
    check if set of keys exists in dictionary python
    """
    if set(keys).issubset(data_dict):
        return True
    else:
        return False
