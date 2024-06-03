from normalizer.match.global_matchers import GlobalMatcher
from normalizer.config_files.loader import load_config_file
from collections import Counter
import pandas as pd
import os

class LocationMatcher(GlobalMatcher):
    def find_location(
        self,
        geolocation:str = None,
        title:str = None,
        description:str = None,
        pills:str = None,
        posting_link:str = None):

        target_data = self.get_non_empty_source_data(
            [title, geolocation, description, pills, posting_link]
            )

        locations = load_config_file('comunes')
        location_detected = self.find_all_matches(locations, target_data)
        comunes = [loc['item'] for loc in location_detected]
        provinces = [loc['payload']['province'] for loc in location_detected]
        regions = [loc['payload']['region'] for loc in location_detected]
        if not comunes and not provinces and not regions:
            locations = load_config_file('conflicting_comunes')
            location_detected = self.find_all_matches(locations, target_data)
            comunes = [loc['item'] for loc in location_detected]
            provinces = [loc['payload']['province'] for loc in location_detected]
            regions = [loc['payload']['region'] for loc in location_detected]

        comunes_final = [key for key,times in dict(Counter(comunes)).items() if times > 0]
        provinces_final = [key for key,times in dict(Counter(provinces)).items() if times > 0]
        regions_final = [key for key,times in dict(Counter(regions)).items() if times > 0]
        return {'comunes': comunes_final, 'provinces': provinces_final, 'regions': regions_final}

if __name__ == '__main__':

    path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.abspath(os.path.join(path, '..', '..', 'tests', 'data', 'labeled_jobs.csv'))
    id = 9
    item = pd.read_csv(file_path)
    geo = item[item['id'] == id]['geolocalization'].item()
    title = item[item['id'] == id]['title'].item()
    description = item[item['id'] == id]['description'].item()
    pills = item[item['id'] == id]['pills'].item()
    posting_link = item[item['id'] == id]['posting_url'].item()

    print(LocationMatcher().find_location(geo, title, description, pills, posting_link))
