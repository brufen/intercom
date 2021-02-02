import os
from src.utils.utils import get_coordinates, sort_list, Direction, check_keys
import csv
import json
import logging
from math import radians, sin, cos, asin, sqrt
from src.utils import setup_logging


class ProcessData:
    """
    Class responsible for processing data set
    """

    def __init__(self, path, export_path, office, distance):
        self.path = path
        self.ex_path = export_path
        self.office_loc = get_coordinates(office)
        self.distance = distance
        self.customer_loc = self.get_location()
        self.customers = []

    def calc(self):
        """
        Calculate distance between office and customers
        """
        while True:
            try:
                customer = next(self.customer_loc)
                distance = self.distance_calc_two(self.office_loc, customer)
                if distance is not None:
                    customer['distance'] = distance
                    self.customers.append(customer)
            except StopIteration:
                break

        sorted_list = sort_list(self.customers, 'user_id', Direction.ASC)
        self.write_dataset(sorted_list)
        return True

    def read_data(self):
        """
        Read data from data storage
        """
        try:
            reader = csv.reader(open(self.path, 'r'))
            headers = next(reader)
            logging.info("Data successfully loaded.")
            return [dict(zip(headers, i)) for i in reader]
        except IOError as error:
            logging.error("Could not read/open file")
            return None
        except FileNotFoundError as error:
            logging.error("File not found")
            return None

    def get_location(self):
        """
         Yield customer per customer
        """
        for customer in self.read_data():
            if check_keys(customer, ('user_id', 'longitude',
                                     'latitude')):
                customer['user_id'] = int(customer['user_id'])
                yield customer
            else:
                pass

    def distance_calc_two(self, startloc, endloc):
        """
        Calculate geographical distance of longitude and latitude in radians
        of two points p1 and p2.
        It uses the spherical law ofcosines.
        """
        start_lat, start_long = map(radians, [startloc['latitude'], startloc[
            'longitude']])
        end_lat, end_long = map(radians, [float(endloc['latitude']),
                                          float(endloc['longitude'])])
        dlon = end_long - start_long
        dlat = end_lat - start_lat
        a = sin(dlat / 2) ** 2 + cos(start_lat) * cos(end_lat) * sin(
            dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371
        result = r * c
        if result < self.distance:
            return result
        else:
            pass

    def write_dataset(self, data_list):
        """
        Save data to the file
        """
        if data_list:
            try:
                with open(self.ex_path, 'w') as f:
                    json.dump(data_list, f, ensure_ascii = False, indent = 4)
                logging.info(f"Data successfully exported to {self.ex_path}")
                return True
            except IOError as error:
                logging.error("Data not saved to file!")
                return False
            except FileNotFoundError as error:
                logging.error("File not found!")
                return False
        else:
            return False
