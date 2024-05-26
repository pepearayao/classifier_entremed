import normalizer.match.global_matchers as global_matchers
from normalizer.config_files.loader import load_config_file

def find_location(
    geolocation:str = None,
    title:str = None,
    description:str = None,
    pills:str = None,
    posting_link:str = None):

    target_data = global_matchers.get_non_empty_source_data([title, geolocation, description, pills, posting_link])
    locations = load_config_file('comunes')

    location_detected = global_matchers.find_all_matches(locations, target_data)
    final = set(location_detected)
