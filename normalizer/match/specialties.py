import normalizer.match.global_matchers as global_matchers
from normalizer.config_files.loader import load_config_file
from collections import Counter

def find_specialty(title:str = None):
    specialties = load_config_file('specialties')
    target_data = [title]
    specialties_detected = global_matchers.find_all_matches(specialties, target_data)

    final = dict(Counter(specialties_detected))
    if final.get('TENS') == final.get('Enfermería'):
        final['Enfermería'] = 0


    return [key for key,times in final.items() if times > 0]
