from normalizer.match.global_matchers import GlobalMatcher
from normalizer.config_files.loader import load_config_file
from collections import Counter

class SpecialtyMatcher(GlobalMatcher):
    def find_specialty(self, title:str = None) -> list[str]:
        '''
        A method that finds the specialty of a title. It uses the specialties.json file to find the matches.

        Args:
            title (str): The title to find the specialty of

        Returns:
            list: A list of the specialties found
        '''
        # Load the specialties from the JSON file and create the target data list
        specialties = load_config_file('specialties')
        target_data = [title]

        # Find all the matches in the source data
        specialties_detected = self.find_all_matches(specialties, target_data)

        # Count the number of times each specialty was found
        final = [spec_detec['item'] for spec_detec in specialties_detected]
        final = dict(Counter(final))

        # In the case of TENS normally has the Enfermería word attached to it. With this logic we make sure not to flag Enfermería a TENS only job.
        if final.get('TENS') == final.get('Enfermería'):
            final['Enfermería'] = 0

        # Return the specialties that were found without duplicates
        return {"specialties": [key for key,times in final.items() if times > 0]}
