from normalizer.match.job_details import Matcher
from tests.fixtures.fixtures import data_for_param_tests
import pytest


def test_job_engagement_data_type(raw_data):
    title = raw_data[0][0]
    work_schedule = raw_data[0][7]
    description = raw_data[0][14]
    requisites = raw_data[0][15]
    pills = raw_data[0][16]

    results = Matcher().get_job_engagement_type([
        title,
        work_schedule,
        description,
        requisites,
        pills
    ])

    assert type(results) == dict
    assert type(results['job_engagement_type']) == list

@pytest.mark.parametrize('data', data_for_param_tests(), ids=lambda x: x[0][18])
def test_job_engagement_result(data):
    raw_data = data[0]
    labeled_data = data[1]
    result = Matcher().get_job_engagement_type([
        raw_data[0],
        raw_data[7],
        raw_data[14],
        raw_data[15],
        raw_data[16]
    ])
    assert sorted(result) == sorted(labeled_data[5])
