from normalizer.match.global_matchers import simple_regex_search, multiple_patterns_match, find_all_matches
import pandas as pd

def test_large_data(raw_data):
    assert len(raw_data['title']) == 20

def test_simple_regex_search(raw_data, specialties):
    pattern = specialties[0]['regex'][0]
    sample = raw_data['title'][0]

    assert simple_regex_search(pattern,sample).group() == 'ENFERMERA'

def test_multiple_patterns_match(raw_data):
    sample_description = raw_data['description'][0]
    assert sorted(multiple_patterns_match(
        ["enfermer.?","kinesi.log.?","kinesiolog.?","fisioterapia","mesoterapia","erg.nomo","ergono[ií]a"],
        sample_description
        )) == sorted(['KINESIOLOGO','ENFERMERA', 'Enfermerí'])

    sample_description = raw_data['description'][1]
    assert sorted(multiple_patterns_match(
        ["iquique"],sample_description)) == sorted(['Iquique'])

def test_find_all_matches(raw_data, specialties):
    title = raw_data['title'][0]
    description = raw_data['description'][0]
    pills = raw_data['pills'][0]
    requisites = raw_data['requisites'][0]
    source_data = [title, description, pills, requisites]
    assert sorted(find_all_matches(specialties, source_data)) == sorted(['Enfermería','Kinesiología','Nutrición','Psicología','Enfermería','TENS','TENS'])
