import normalizer.match.global_matchers as global_matchers
from normalizer.config_files.loader import load_config_file

def find_geolocation(
    title:str = None,
    geolocation:str = None,
    description:str = None,
    pills:str = None,
    posting_link:str = None):

    target_data = global_matchers.get_non_empty_source_data([title, geolocation, description, pills, posting_link])
