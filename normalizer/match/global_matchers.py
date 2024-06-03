import re
from collections import Counter

class GlobalMatcher:
    def get_non_empty_source_data(self, source_data:list):
        return [data for data in source_data if data]

    def simple_regex_search(self, pattern:str,in_string:str):
        return re.search(pattern,in_string,re.IGNORECASE)

    def multiple_patterns_match(self, patterns:list, in_string:str):
        return re.findall(r"|".join(patterns),in_string, re.IGNORECASE)

    def find_all_matches(self, target_classes:list, source_data:list):
        normalized_classes = []
        for raw_data_item in self.get_non_empty_source_data(source_data):
            for target_class_item in target_classes:
                if target_class_item['regex_type'] == 'simple':
                    if self.multiple_patterns_match(target_class_item['regex'], raw_data_item):
                        normalized_classes.append({'item': target_class_item['name'], 'payload': target_class_item['data']})
                elif target_class_item['regex_type'] == 'complex':
                    if target_class_item['regex'].get('simple_match'):
                        if self.multiple_patterns_match(target_class_item['regex']['simple_match'], raw_data_item):
                            normalized_classes.append({'item': target_class_item['name'], 'payload': target_class_item['data']})
                    if self.multiple_patterns_match(target_class_item['regex']['level1'], raw_data_item):
                        for final_pattern in target_class_item['regex']['level2']:
                            if final_pattern['type'] == 'match':
                                if self.multiple_patterns_match(final_pattern['regex'], raw_data_item):
                                    normalized_classes.append({'item': target_class_item['name'], 'payload': target_class_item['data']})
                            if final_pattern['type'] == 'reject':
                                if not self.multiple_patterns_match(final_pattern['regex'], raw_data_item):
                                    normalized_classes.append({'item': target_class_item['name'], 'payload': target_class_item['data']})

        return normalized_classes

    def find_first_match(self, target_classes:dict, source_data:list):
        pass
