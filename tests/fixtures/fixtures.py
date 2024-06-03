import pytest
import pandas as pd
import json
import os
import ast

data_path = os.path.join(os.path.dirname(__file__), '..', 'data')
config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'normalizer', 'config_files')
converters = {
    'labeled_specialty': ast.literal_eval,
    'labeled_comuna': ast.literal_eval,
    'labeled_region': ast.literal_eval,
    'labeled_job_schedule_type': ast.literal_eval,
    'labeled_job_shift_type': ast.literal_eval,
    'labeled_job_engagement_type': ast.literal_eval,
    'labeled_job_engagement_duration': ast.literal_eval,
    'labeled_certificates': ast.literal_eval,
    'labeled_emails': ast.literal_eval
}

@pytest.fixture(scope='module')
def raw_data():
    raw_columns = [
    'title',            # 0
    'source_url',       # 1
    'posting_url',      # 2
    'geolocalization',  # 3
    'company',          # 4
    'salary',           # 5
    'experience',       # 6
    'work_schedule',    # 7
    'shift_type',       # 8
    'employment_type',  # 9
    'slots_avaliable',  # 10
    'urgency_required', # 11
    'seniority_level',  # 12
    'driving_level',    # 13
    'description',      # 14
    'requisites',       # 15
    'pills',            # 16
    'inclusive_posting' # 17
    ]

    df_raw = pd.read_csv(os.path.join(data_path,'labeled_jobs.csv'))[raw_columns]
    yield [tuple(x[1].replace({pd.NA: None,'nan': None})) for x in df_raw.iterrows()]

@pytest.fixture(scope='module')
def labeled_data():
    labeled_columns = [
    'labeled_specialty',        # 0
    'labeled_comuna',           # 1
    'labeled_region',           # 2
    'labeled_job_schedule_type',    # 3
    'labeled_job_shift_type',    # 4
    'labeled_job_engagement_type',  # 5
    'labeled_job_engagement_duration',  # 6
    'labeled_company',          # 7
    'labeled_inclusive_offer',  # 8
    'labeled_certificates',     # 9
    'labeled_emails'            # 10
    ]
    df_labeled = pd.read_csv(os.path.join(data_path,'labeled_jobs.csv'), converters=converters)[labeled_columns]
    yield [tuple(x[1].replace({pd.NA: None,'nan': None})) for x in df_labeled.iterrows()]

@pytest.fixture(scope='session')
def specialties():
    return json.load(open(os.path.join(config_path,'specialties.json')))

@pytest.fixture(scope='session')
def comunes():
    return json.load(open(os.path.join(config_path,'comunes.json')))

def data_for_param_tests():
    raw_columns = [
    'title',            # 0
    'source_url',       # 1
    'posting_url',      # 2
    'geolocalization',  # 3
    'company',          # 4
    'salary',           # 5
    'experience',       # 6
    'work_schedule',    # 7
    'shift_type',       # 8
    'employment_type',  # 9
    'slots_avaliable',  # 10
    'urgency_required', # 11
    'seniority_level',  # 12
    'driving_level',    # 13
    'description',      # 14
    'requisites',       # 15
    'pills',            # 16
    'inclusive_posting', # 17
    'id'                # 18
    ]

    labeled_columns = [
    'labeled_specialty',
    'labeled_comuna',
    'labeled_region',
    'labeled_job_schedule_type',
    'labeled_job_shift_type',
    'labeled_job_engagement_type',
    'labeled_job_engagement_duration',
    'labeled_company',
    'labeled_inclusive_offer',
    'labeled_certificates',
    'labeled_emails'
    ]

    df_raw = pd.read_csv(os.path.join(data_path,'labeled_jobs.csv'))[raw_columns]
    df_labeled = pd.read_csv(os.path.join(data_path,'labeled_jobs.csv'), converters=converters)[labeled_columns]
    for raw,label in zip(df_raw.iterrows(), df_labeled.iterrows()):
        yield (tuple(raw[1].replace({pd.NA: None,'nan': None})), tuple(label[1].replace({pd.NA: None,'nan': None})))
