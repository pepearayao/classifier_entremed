import re
from collections import Counter

def get_non_empty_source_data(source_data:list):
    return [data for data in source_data if data]

def simple_regex_search(pattern:str,in_string:str):
    return re.search(pattern,in_string,re.IGNORECASE)

def multiple_patterns_match(patterns:list, in_string:str):
    return re.findall("|".join(patterns),in_string, re.IGNORECASE)

def find_all_matches(target_classes:list, source_data:list):
    normalized_classes = []
    for raw_data_item in get_non_empty_source_data(source_data):
        for target_class_item in target_classes:
            if target_class_item['regex_type'] == 'simple':
                if multiple_patterns_match(target_class_item['regex'], raw_data_item):
                    normalized_classes.append(target_class_item['name'])
            elif target_class_item['regex_type'] == 'complex':
                if target_class_item['regex'].get('simple_match'):
                    if multiple_patterns_match(target_class_item['regex']['simple_match'], raw_data_item):
                        normalized_classes.append(target_class_item['name'])
                if multiple_patterns_match(target_class_item['regex']['level1']):
                    if target_class_item['regex']['level2']['type'] == 'match':
                        if multiple_patterns_match(target_class_item['regex']['level2']['regex'], raw_data_item):
                            normalized_classes.append(target_class_item['name'])
                    if target_class_item['regex']['level2']['type'] == 'reject':
                        if not multiple_patterns_match(target_class_item['regex']['level2']['regex'], raw_data_item):
                            normalized_classes.append(target_class_item['name'])

    return normalized_classes

def find_first_match(target_classes:dict, source_data:list):
    pass
