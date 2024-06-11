from normalizer.match.job_details import Matcher
from tests.fixtures.fixtures import data_for_param_tests
import pytest

def test_job_certificates_data_type(raw_data):
    title = raw_data[0][0]
    work_schedule = raw_data[0][7]
    description = raw_data[0][14]
    requisites = raw_data[0][15]
    pills = raw_data[0][16]

    result = Matcher(
        title = title,
        work_schedule = work_schedule,
        description = description,
        requisites = requisites,
        pills = pills
        ).get_certificates()

    assert type(result) == dict
    assert type(result['certificates']) == list

@pytest.mark.parametrize('data', data_for_param_tests(), ids=lambda x: x[0][18])
def test_job_certificates_result(data):
    raw_data = data[0]
    labeled_data = data[1]
    result = Matcher(
        title = raw_data[0],
        work_schedule = raw_data[7],
        description = raw_data[14],
        requisites = raw_data[15],
        pills = raw_data[16]
    ).get_certificates()
    assert sorted(result['certificates']) == sorted(labeled_data[9])
