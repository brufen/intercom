import pytest
import csv
import os
import json
from src.data_processor import ProcessData

TEST_DATA = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_customers.csv',
)


TEST_DATA_WRONG = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test/',
)

TEST_DATA_EXPORT = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_customers.csv',
)



class TestOs:
    path = TEST_DATA
    ex_path = TEST_DATA_EXPORT
    ex_path_wrong = TEST_DATA_WRONG
    office = 'test'
    distance = 1

    @pytest.fixture
    def data_processor(self):
        return ProcessData(self.path,self.ex_path, self.office, self.distance)

    @pytest.fixture
    def data_processor_wrong_path(self):
        return ProcessData(self.ex_path_wrong,self.ex_path, self.office, self.distance)

    @pytest.fixture
    def expected_data(self):
        data =  {'latitude': '52.986375', 'user_id': '12', 'name': 'User1', 'longitude': '-6.043701'}
        return data

    def test_csv_reader(self, data_processor, expected_data):
        result = data_processor.read_data()
        assert expected_data == result[0]

    def test_csv_reader_file_not_found(self, data_processor_wrong_path, expected_data):
        with pytest.raises(FileNotFoundError):
            result = data_processor_wrong_path.read_data()
            raise FileNotFoundError









