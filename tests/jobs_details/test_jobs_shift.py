from normalizer.match.job_details import Matcher
from tests.fixtures.fixtures import data_for_param_tests
import pytest


def test_job_shift_data_type(raw_data):
    title = raw_data[0][0]
    work_schedule = raw_data[0][7]
    shift_type = raw_data[0][8]
    description = raw_data[0][14]
    requisites = raw_data[0][15]
    pills = raw_data[0][16]

    matcher_obj = Matcher(
        title=title,
        work_schedule=work_schedule,
        shift_type=shift_type,
        description=description,
        requisites=requisites,
        pills=pills
    )
    results = matcher_obj.get_job_shift()

    assert type(results) == dict
    assert type(results['job_shift']) == list

@pytest.mark.parametrize('data', data_for_param_tests(), ids=lambda x: x[0][18])
def test_job_shift_result(data):
    raw_data = data[0]
    labeled_data = data[1]
    matcher_obj = Matcher(
        title=raw_data[0],
        work_schedule=raw_data[7],
        shift_type=raw_data[8],
        description=raw_data[14],
        requisites=raw_data[15],
        pills=raw_data[16]
    )
    result = matcher_obj.get_job_shift()
    assert sorted(result['job_shift']) == sorted(labeled_data[4])
