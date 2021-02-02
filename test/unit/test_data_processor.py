import pytest
import mock
import os
from src.data_processor import ProcessData

TEST_DATA = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),'..',
    'integration/test_customers.csv')

TEST_DATA_EXPORT = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_customers.csv')


class TestProcessData:
    path = TEST_DATA
    ex_path = TEST_DATA_EXPORT
    office = 'test'
    distance = 1

    @pytest.fixture
    def data_processor(self):
        return ProcessData(self.path,self.ex_path, self.office, self.distance)

    def test_calc(self, data_processor):
        data_processor.calc()
        assert 'latitude' in data_processor.office_loc
        assert 'longitude' in data_processor.office_loc
