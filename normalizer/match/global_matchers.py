import re
from collections import Counter

class GlobalMatcher:
    def get_non_empty_source_data(self, source_data:list) -> list[str]:
        '''
        Just a simple function to filter out empty strings from the source data

        Args:
            source_data (list): A list of strings

        Returns:
            list: A list of strings with no empty strings
        '''
        return [data for data in source_data if data]

    def simple_regex_search(self, pattern:str,in_string:str) -> re.Match:
        '''
        A simple regex search function that returns a match object. Used when you want to check if a pattern exists in a string

        Args:
            pattern (str): The regex pattern to search for
            in_string (str): The string to search in

        Returns:
            re.Match: A match object
        '''
    #
        return re.search(pattern,in_string,re.IGNORECASE)

    def multiple_patterns_match(self, patterns:list, in_string:str) -> list[str]:
        '''
        A simple regex findall function that returns a list with all the matches. Used when you want to check if multiple patterns exist in a string

        Args:
            patterns (list): A list of regex patterns to search for
            in_string (str): The string to search in

        Returns:
            list: A list of all the matches
        '''
        return re.findall(r"|".join(patterns),in_string, re.IGNORECASE)

    def get_final_elements(self, matches:list) -> list[str]:
        '''
        A function that returns the unique elements in a list

        Args:
            matches (list): A list of strings
        Returns:
            list: A list with the unique elements
        '''

        # Get all the elements found in the matches list
        return [key for key,times in dict(Counter(matches)).items() if times > 0]

    def find_all_matches(self, target_classes:list, source_data:list) -> list[dict]:
        '''
        A function that finds all the matches in the source data and returns a list of dictionaries with the matched item and any payload it might have.

        Args:
            target_classes (list): A list of dictionaries with the regex pattern, the name of the item and any payload it might have
            source_data (list): A list of strings to search in.

        Returns:
            list: A list of dictionaries with the matched item and any payload it might have.
        '''

        normalized_classes = []

        # Loop through all the items in the source data. Could be different origin of data like title, description, etc.
        for raw_data_item in self.get_non_empty_source_data(source_data):
            # Loop through all the target classes. Could be different classes like comunes, specialties, type of jobs, etc. Predefined in JSON files.
            for target_class_item in target_classes:
                # Check if the regex type is simple or complex. When cmplex it conforms lto a specific structure.
                if target_class_item['regex_type'] == 'simple':
                    if self.multiple_patterns_match(target_class_item['regex'], raw_data_item):
                        normalized_classes.append({'item': target_class_item['name'], 'payload': target_class_item['data']})
                elif target_class_item['regex_type'] == 'complex':
                    # Sometimes the item has a simple match pattern to check. If it matches, we add it to the normalized classes.
                    if target_class_item['regex'].get('simple_match'):
                        if self.multiple_patterns_match(target_class_item['regex']['simple_match'], raw_data_item):
                            normalized_classes.append({'item': target_class_item['name'], 'payload': target_class_item['data']})
                    # If the item has a complex structure, we check the level1 and level2 patterns.
                    if self.multiple_patterns_match(target_class_item['regex']['level1'], raw_data_item):
                        for final_pattern in target_class_item['regex']['level2']:
                            # It might have a match pattern which we check if it matches the raw data item. Then we add it to the normalized classes.
                            if final_pattern['type'] == 'match':
                                if self.multiple_patterns_match(final_pattern['regex'], raw_data_item):
                                    normalized_classes.append({'item': target_class_item['name'], 'payload': target_class_item['data']})
                            # It might have a reject pattern which we check if it doesn't match the raw data item. Then we add it to the normalized classes.
                            if final_pattern['type'] == 'reject':
                                if not self.multiple_patterns_match(final_pattern['regex'], raw_data_item):
                                    normalized_classes.append({'item': target_class_item['name'], 'payload': target_class_item['data']})

        return normalized_classes
