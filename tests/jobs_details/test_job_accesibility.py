from normalizer.match.job_details import Matcher
from tests.fixtures.fixtures import data_for_param_tests
import pytest

def test_job_inclusive_offer_data_type(raw_data):
    title = raw_data[0][0]

    result = Matcher(title=title).get_inclusivity()

    assert type(result) == dict
    assert type(result['inclusive']) == bool

@pytest.mark.parametrize('data', data_for_param_tests(), ids=lambda x: x[0][18])
def test_job_inclusive_offer_result(data):
    raw_data = data[0]
    labeled_data = data[1]
    result = Matcher(title = raw_data[0], inclusive=raw_data[17]).get_inclusivity()
    assert (result['inclusive'] == labeled_data[8])
