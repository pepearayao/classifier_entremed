from normalizer.match.global_matchers import GlobalMatcher
from normalizer.config_files.loader import load_config_file
from collections import Counter
import pandas as pd
import os
import re
import numpy as np

class Matcher(GlobalMatcher):

    def __init__(
        self,
        title:str = None,
        work_schedule:str = None,
        shift_type:str = None,
        employment_type:str = None,
        description:str = None,
        requisites:str = None,
        pills:str = None,
        posting_link:str = None,
        company:str = None
    ):
        '''
        Init method for the Matcher class. It receives the title, work_schedule, shift_type,
        employment_type, description, requisites, pills and posting_link.

        Also it calls the get_non_empty_source_data method to work only with non empty data.

        Args:
            title (str): The title of the job posting.
            work_schedule (str): The work schedule of the job posting.
            shift_type (str): The shift type of the job posting.
            employment_type (str): The employment type of the job posting.
            description (str): The description of the job posting.
            requisites (str): The requisites of the job posting.
            pills (str): The pills of the job posting.
            posting_link (str): The posting link of the job posting.
        '''
        self.title = title
        self.work_schedule = work_schedule
        self.shift_type = shift_type
        self.employment_type = employment_type
        self.description = description
        self.requisites = requisites
        self.pills = pills
        self.posting_link = posting_link
        self.company = company

        self.target_data = self.get_non_empty_source_data(
            [
                self.title,
                self.work_schedule,
                self.shift_type,
                self.employment_type,
                self.description,
                self.requisites,
                self.pills
            ]
        )


    def find_numbers_job_schedule(self, target_data) -> int:
        '''
        A method that finds the amount of hours requiered to work per week.

        Args:
            elements (list): A list with the job schedule elements.

        Returns:
            int: The integer found in the job schedule elements.
        '''
        for item in target_data:
            if re.search(r'hora.',item,re.IGNORECASE) != None:
                return int(re.search(r'\d+', item).group())

    def get_job_schedule(self) -> dict:
        '''
        A method that finds the type of schedule for a job. Can be Part-Time or Full-Time.
        It uses the title, work_schedule, description, requisites and pills to find the matches.
        It uses the job_schedule.json file to find the matches.

        Returns:
            dict: A dict with the type of schedule found in the job posting.
        '''
        # Load the job_schedule.json file
        job_schedule = load_config_file('job_schedules')
        target_data = [self.work_schedule]
        job_schedule_detected = self.find_all_matches(job_schedule, target_data)

        # Get the type of schedule found in the job posting.
        elements = self.get_final_elements([loc['item'] for loc in job_schedule_detected])

        # If the job schedule is in hours, check if it is Part-Time or Full-Time depending on the amount of hours.
        if 'Hours' in elements:
            hours = self.find_numbers_job_schedule(target_data)
            if hours < 44:
                elements.append('Part-Time')
            else:
                elements.append('Full-Time')
            elements.remove('Hours')
            elements = self.get_final_elements(elements)

        return {'job_schedule': elements}

    def get_job_shift(self) -> dict:
        '''
        A method that finds the type of shift for a job. Can be 4to Turno, 4to Turno Modificado or 4to Turno Rotativo.
        It uses the title, work_schedule, description, requisites and pills to find the matches.
        It uses the job_shift.json file to find the matches.

        Returns:
            dict: A dict with the type of shift found in the job posting.
        '''
        # Load the job_shift.json file
        job_shifts = load_config_file('job_shifts')
        job_shift_detected = self.find_all_matches(job_shifts, self.target_data)

        # Get the type of shift found in the job posting.
        elements = self.get_final_elements([loc['item'] for loc in job_shift_detected])

        return {'job_shift': elements}

    def get_job_engagement_type(self) -> dict:
        '''
        A method that finds the type of engagement for a job. Can be Honorario o a Contrata.
        It uses the title, work_schedule, description, requisites and pills to find the matches.
        It uses the job_engagement_type.json file to find the matches.

        Returns:
            dict: A dict with the type of engagement found in the job posting.
        '''
        # Load the job_engagement_type.json file
        job_engagement_type = load_config_file('job_engagement_types')
        job_engagement_type_detected = self.find_all_matches(job_engagement_type, self.target_data)

        # Get the type of engagement found in the job posting.
        elements = self.get_final_elements([loc['item'] for loc in job_engagement_type_detected])

        return {'job_engagement_type': elements}

    def get_job_engagement_duration(self) -> dict:
        '''
        A method that finds the duration of the engagement for a job. Can be Indefinido o Temporal.
        It uses the title, work_schedule, description, requisites and pills to find the matches.
        It uses the job_engagement_duration.json file to find the matches.

        Returns:
            dict: A dict with the duration of the engagement found in the job posting.
        '''
        # Load the job_engagement_duration.json file
        job_engagement_duration = load_config_file('job_engagement_duration')
        job_engagement_duration_detected = self.find_all_matches(job_engagement_duration, self.target_data)

        # Get the duration of the engagement found in the job posting.
        elements = self.get_final_elements([loc['item'] for loc in job_engagement_duration_detected])

        return {'job_engagement_duration': elements}

    def get_company(self) -> dict:
        '''
        A method that finds the company name in the job posting.

        Returns:
            dict: A dict with the company name in the key 'company'.
        '''
        # Return the name of the company Capitalized
        return {'company': self.clean_string(self.company).title()}

    def get_emails(self) -> dict:
        '''
        A method that finds the emails in the job posting.

        Returns:
            dict: A dict with the emails found in the job posting.
        '''
        # Get the emails found in the job posting
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = self.multiple_patterns_match([email_pattern], self.description)

        return {'emails': emails}

if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.abspath(os.path.join(path, '..', '..', 'tests', 'data', 'labeled_jobs.csv'))
    id = 9
    item = pd.read_csv(file_path).replace({pd.NA: None,'nan': None, np.nan: None})
    title = item[item['id'] == id]['title'].item()
    work_schedule = item[item['id'] == id]['work_schedule'].item()
    description = item[item['id'] == id]['description'].item()
    requisites = item[item['id'] == id]['requisites'].item()
    employment_type = item[item['id'] == id]['employment_type'].item()
    pills = item[item['id'] == id]['pills'].item()
    shift_type = item[item['id'] == id]['shift_type'].item()
    posting_link = item[item['id'] == id]['posting_url'].item()
    company = item[item['id'] == id]['company'].item()

    matcher_obj = Matcher(
        title = title,
        work_schedule = work_schedule,
        shift_type = shift_type,
        employment_type = None,
        description = description,
        requisites = requisites,
        pills = pills,
        posting_link = posting_link,
        company = company
    )

    print(matcher_obj.get_company())
