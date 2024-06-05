from normalizer.match.global_matchers import GlobalMatcher
from normalizer.config_files.loader import load_config_file
from collections import Counter
import pandas as pd
import os
import re

class Matcher(GlobalMatcher):
    def find_numbers_job_schedule(self, target_data):
        '''
        A method that finds the amount of hours requiered to work per week.

        Args:
            elements (list): A list with the job schedule elements.

        Returns:
            list: A list with the numbers found in the job schedule elements.
        '''
        for item in target_data:
            if re.search(r'hora.',item,re.IGNORECASE) != None:
                return int(re.search(r'\d+', item).group())

    def get_job_schedule(
        self,
        title = None,
        work_schedule = None,
        description = None,
        requisites = None,
        pills = None) -> list[str]:
        '''
        A method that finds the type of schedule for a job. Can be Part-Time or Full-Time.
        It uses the title, work_schedule, description, requisites and pills to find the matches.
        It uses the job_schedule.json file to find the matches.

        Args:
            title (str): The title of the job as found on the job posting.
            work_schedule (str): The work schedule of the job as found on the job posting.
            description (str): The description of the job as found on the job posting.
            requisites (str): The requisites of the job as found on the job posting.
            pills (str): The pills of the job as found on the job posting.

        Returns:
            list: A list with the type of schedule found in the job posting.
        '''
        # Get the non empty source data. If some data is empty, it will be filtered out.
        target_data = self.get_non_empty_source_data(
            [title, work_schedule, description, requisites, pills]
            )

        # Load the job_schedule.json file
        job_schedule = load_config_file('job_schedules')
        job_schedule_detected = self.find_all_matches(job_schedule, [work_schedule])

        elements = self.get_final_elements([loc['item'] for loc in job_schedule_detected])

        if 'Hours' in elements:
            hours = self.find_numbers_job_schedule(target_data)
            if hours < 44:
                elements.append('Part-Time')
            else:
                elements.append('Full-Time')
            elements.remove('Hours')
            elements = self.get_final_elements(elements)

        return {'job_schedule': elements}





if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.abspath(os.path.join(path, '..', '..', 'tests', 'data', 'labeled_jobs.csv'))
    id = 928
    item = pd.read_csv(file_path)
    title = item[item['id'] == id]['title'].item()
    work_schedule = item[item['id'] == id]['work_schedule'].item()
    description = item[item['id'] == id]['description'].item()
    pills = item[item['id'] == id]['pills'].item()
    posting_link = item[item['id'] == id]['posting_url'].item()

    print(Matcher().get_job_schedule(title, work_schedule, description, pills, posting_link))
