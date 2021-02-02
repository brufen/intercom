import pytest
import src.utils.utils as utils

customers = [
    {
        "id": 6,
        "name": "userC",
        "distance": 1
    },
    {
        "id": 3,
        "name": "userB",
        "distance": 1
    },
    {
        "id": 100,
        "name": "userA",
        "distance": 1
    }]

test_dict = {
    'id': 100,
    'name': 'userA',
}


@pytest.fixture
def data_dict():
    return test_dict


@pytest.mark.parametrize("list, order_by, direction", [[customers, 'id',
                                                        False]])
def test_sort_list(list, order_by, direction):
    sorted_list = utils.sort_list(list, order_by, direction)
    assert sorted_list[0]['id'] == 3
    assert sorted_list[2]['id'] == 100


def test_check_keys_exists(data_dict):
    key_exists = utils.check_keys(data_dict, ['id', 'name'])
    assert key_exists == True


def test_check_keys_not_exists(data_dict):
    key_exists = utils.check_keys(data_dict, 'user_id')
    assert key_exists == False
