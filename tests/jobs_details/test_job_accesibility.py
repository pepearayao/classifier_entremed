from normalizer.match.job_details import Matcher
from tests.fixtures.fixtures import data_for_param_tests
import pytest

def test_job_inclusive_offer_data_type(raw_data):
    title = raw_data[0][0]
    work_schedule = raw_data[0][7]
    description = raw_data[0][14]
    requisites = raw_data[0][15]
    pills = raw_data[0][16]

    result = Matcher().get_job_inclusive_offer(
        title,
        work_schedule,
        description,
        requisites,
        pills
    )

    assert type(result) == dict
    assert type(result['job_inclusive_offer']) == bool

@pytest.mark.parametrize('data', data_for_param_tests(), ids=lambda x: x[0][18])
def test_job_inclusive_offer_result(data):
    raw_data = data[0]
    labeled_data = data[1]
    result = Matcher().get_job_inclusive_offer(
        raw_data[0],
        raw_data[7],
        raw_data[14],
        raw_data[15],
        raw_data[16]
    )
    assert result == labeled_data[8]
