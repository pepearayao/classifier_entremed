import pytest
import pandas as pd
import json
import os

data_path = os.path.join(os.path.dirname(__file__), '..', 'data')
config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'normalizer', 'config_files')

@pytest.fixture(scope='session')
def raw_data():
    raw_columns = [
    'title',
    'source_url',
    'posting_url',
    'geolocalization',
    'company',
    'salary',
    'experience',
    'work_schedule',
    'shift_type',
    'employment_type',
    'slots_avaliable',
    'urgency_required',
    'seniority_level',
    'driving_level',
    'description',
    'requisites',
    'pills',
    'inclusive_posting'
    ]

    df_raw = pd.read_csv(os.path.join(data_path,'final_labeled_data.csv'))[raw_columns]
    return df_raw.replace({pd.NA: None,'nan': None}).to_dict()

@pytest.fixture(scope='session')
def labeled_data():
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
    df_labeled = pd.read_csv(os.path.join(data_path,'final_labeled_data.csv'))[labeled_columns].rename(columns={
        'labeled_specialty': 'specialty',
        'labeled_comuna': 'comuna',
        'labeled_region': 'region',
        'labeled_job_schedule_type': 'job_schedule_type',
        'labeled_job_shift_type': 'job_shift_type',
        'labeled_job_engagement_type': 'job_engagement_type',
        'labeled_job_engagement_duration': 'job_engagement_duration',
        'labeled_company': 'company',
        'labeled_inclusive_offer': 'inclusive_offer',
        'labeled_certificates': 'certificates',
        'labeled_emails': 'emails'
    })
    return df_labeled.replace({pd.NA: None,'nan': None}).to_dict()

@pytest.fixture(scope='session')
def specialties():
    return json.load(open(os.path.join(config_path,'specialties.json')))

@pytest.fixture(scope='session')
def comunes():
    return json.load(open(os.path.join(config_path,'comunes.json')))
