import normalizer.match.global_matchers as global_matchers
from normalizer.config_files.loader import load_config_file

def find_specialty(title:str = None, requirements:str = None, pills:str = None):
    specialties = load_config_file('specialties')
    target_data = global_matchers.get_non_empty_source_data([title, requirements, pills])
    specialties_detected = global_matchers.find_all_matches(specialties, target_data)
    final = dict(specialties_detected)
    if final['TENS'] == final['Enfermería']:
        final['TENS'] = 0

    return [key for key,times in final.items() if times > 0]
