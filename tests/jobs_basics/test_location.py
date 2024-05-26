from normalizer.match.location import find_location
from tests.fixtures.fixtures import data_for_param_tests
import pytest

def test_comuna_result_data_type(raw_data):
    geolocation = raw_data[0][3]
    result = find_location(geolocation)

    assert type(result['comuna']) == list

def test_region_result_data_type(raw_data):
    geolocation = raw_data[0][3]
    result = find_location(geolocation)

    assert type(result['region']) == list

@pytest.mark.parametrize('data', data_for_param_tests(), ids=lambda x: x[0][18])
def test_comuna_result(data):
    raw_data = data[0]
    labeled_data = data[1]
    result = find_location(raw_data[3],raw_data[0],raw_data[14],raw_data[16],raw_data[1])

    assert sorted(result['comuna']) == sorted(labeled_data[1])

@pytest.mark.parametrize('data', data_for_param_tests(), ids=lambda x: x[0][18])
def test_region_result(data):
    raw_data = data[0]
    labeled_data = data[1]
    result = find_location(raw_data[3],raw_data[0],raw_data[14],raw_data[16],raw_data[1])

    assert sorted(result['region']) == sorted(labeled_data[2])
