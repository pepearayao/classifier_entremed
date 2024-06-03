from normalizer.match.global_matchers import GlobalMatcher
from normalizer.config_files.loader import load_config_file
from collections import Counter

class SpecialtyMatcher(GlobalMatcher):
    def find_specialty(self, title:str = None):
        specialties = load_config_file('specialties')
        target_data = [title]
        specialties_detected = self.find_all_matches(specialties, target_data)
        final = [spec_detec['item'] for spec_detec in specialties_detected]
        final = dict(Counter(final))
        if final.get('TENS') == final.get('Enfermería'):
            final['Enfermería'] = 0
        return [key for key,times in final.items() if times > 0]
