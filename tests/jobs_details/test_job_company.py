from normalizer.match.job_details import Matcher
from tests.fixtures.fixtures import data_for_param_tests
import pytest

def test_job_company_data_type(raw_data):
    company = raw_data[0][4]

    result = Matcher(company=company).get_company()

    assert type(result) == dict
    assert type(result['company']) == str


@pytest.mark.parametrize('data', data_for_param_tests(), ids=lambda x: x[0][18])
def test_job_company_result(data):
    raw_data = data[0]
    labeled_data = data[1]
    result = Matcher(company = raw_data[4]).get_company()
    assert result['company'] == labeled_data[7]
