from normalizer.match.specialties import SpecialtyMatcher
from tests.fixtures.fixtures import data_for_param_tests
import pytest

def test_specialty_result_data_type(raw_data):
    title = raw_data[0][0]
    assert type(SpecialtyMatcher().find_specialty(title)) == dict

def test_specialty_result_labeled_data_type(labeled_data):
    assert type(labeled_data[0][0]) == list

@pytest.mark.parametrize('data', data_for_param_tests(), ids=lambda x: x[0][18])
def test_specialty_result(data):
    raw_data = data[0]
    labeled_data = data[1]
    result = SpecialtyMatcher().find_specialty(raw_data[0])
    assert sorted(result['specialties']) == sorted(labeled_data[0])
