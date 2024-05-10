from normalizer.match.global_matchers import simple_regex_search, multiple_patterns_match, find_all_matches

def test_simple_regex_search(jobpost_sample, specialties):
    assert simple_regex_search(specialties['Enfermería'][0],jobpost_sample['title'])
    assert not simple_regex_search(specialties['Kinesiología'][0],jobpost_sample['title'])

def test_multiple_patterns_match(jobpost_sample, specialties):
    assert multiple_patterns_match(specialties['Enfermería'],jobpost_sample['title'])
    assert not multiple_patterns_match(specialties['Kinesiología'],jobpost_sample['title'])
