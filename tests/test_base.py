from normalizer.match.global_matchers import GlobalMatcher
import pandas as pd

def test_large_data(raw_data):
    assert len(raw_data) == 20

def test_simple_regex_search(raw_data, specialties):
    pattern = specialties[0]['regex'][0]
    sample = raw_data[0][0]

    assert GlobalMatcher().simple_regex_search(pattern,sample).group() == 'ENFERMERA'

def test_multiple_patterns_match(raw_data):
    sample_description = raw_data[0][14]
    assert sorted(GlobalMatcher().multiple_patterns_match(
        ["enfermer.?","kinesi.log.?","kinesiolog.?","fisioterapia","mesoterapia","erg.nomo","ergono[ií]a"],
        sample_description
        )) == sorted(['KINESIOLOGO','ENFERMERA', 'Enfermerí'])

def test_find_all_matches(raw_data, specialties):
    title = raw_data[0][0]
    description = raw_data[0][14]
    pills = raw_data[0][16]
    requisites = raw_data[0][15]
    source_data = [title, description, pills, requisites]

    specialties_found = [item['item'] for item in GlobalMatcher().find_all_matches(specialties, source_data)]

    assert sorted(specialties_found) == sorted(['Enfermería','Kinesiología','Nutrición','Psicología','Enfermería','TENS','TENS'])
