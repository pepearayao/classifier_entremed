from normalizer.match.global_matchers import simple_regex_search, multiple_patterns_match, find_all_matches

def test_simple_regex_search(jobpost_simple, specialties):
    assert simple_regex_search(specialties['Enfermería'][0],jobpost_simple['title'])
    assert not simple_regex_search(specialties['Kinesiología'][0],jobpost_simple['title'])

def test_multiple_patterns_match(jobpost_simple, specialties):
    assert multiple_patterns_match(specialties['Enfermería'],jobpost_simple['title'])
    assert not multiple_patterns_match(specialties['Kinesiología'],jobpost_simple['title'])
