from normalizer.match.job_details import Matcher
from tests.fixtures.fixtures import data_for_param_tests
import pytest

def test_job_emails_data_type(raw_data):
    description = raw_data[0][14]

    result = Matcher(description = description).get_emails()

    assert type(result) == dict
    assert type(result['emails']) == list

@pytest.mark.parametrize('data', data_for_param_tests(), ids=lambda x: x[0][18])
def test_job_emails_result(data):
    raw_data = data[0]
    labeled_data = data[1]
    result = Matcher(description = raw_data[14]).get_emails()
    assert sorted(result['emails']) == sorted(labeled_data[10])
