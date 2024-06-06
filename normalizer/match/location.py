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
        posting_link:str = None) -> dict:
        '''
        A method that finds the location of a job. It uses the comunes.json and conflicting_comunes.json files to find the matches.

        Args:
            geolocation (str): The geolocation of the job as found on the job posting.
            title (str): The title of the job as found on the job posting.
            description (str): The description of the job as found on the job posting.
            pills (str): The pills of the job as found on the job posting.
            posting_link (str): The posting link of the job as found on the job posting.

        Returns:
            dict: A dictionary with the comunes, provinces and regions found in the job posting.
        '''

        # Get the non empty source data. If some data is empty, it will be filtered out.
        target_data = self.get_non_empty_source_data(
            [title, geolocation, description, pills, posting_link]
            )

        # Load the comunes.json file
        locations = load_config_file('comunes')
        location_detected = self.find_all_matches(locations, target_data)

        # Get the comunes, provinces and regions found in the job posting.
        comunes = [loc['item'] for loc in location_detected]
        provinces = [loc['payload']['province'] for loc in location_detected]
        regions = [loc['payload']['region'] for loc in location_detected]

        # If no comunes, provinces or regions are found, load the conflicting_comunes.json file.
        # This file contains comunes that are not in the comunes.json file and might conflict when matching.
        # It containes mostly comunes with the similar name as other comunes or same names as provinces or regions.
        if not comunes and not provinces and not regions:
            locations = load_config_file('conflicting_comunes')
            location_detected = self.find_all_matches(locations, target_data)
            comunes = [loc['item'] for loc in location_detected]
            provinces = [loc['payload']['province'] for loc in location_detected]
            regions = [loc['payload']['region'] for loc in location_detected]

        # Get the unique comunes, provinces and regions found in the job posting.
        comunes_final = self.get_final_elements(comunes)
        provinces_final = self.get_final_elements(provinces)
        regions_final = self.get_final_elements(regions)

        # Return the comunes, provinces and regions found in the job posting. As lists within a dictionary.
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
