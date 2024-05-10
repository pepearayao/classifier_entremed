import re

def simple_regex_search(pattern:str,in_string:str):
    return re.search(pattern,in_string,re.IGNORECASE)

def multiple_patterns_match(patterns:list, in_string:str):
    return simple_regex_search("|".join(patterns),in_string)

def find_all_matches(target_classes:dict, source_data:list):
    normalized_classes = []
    for raw_data_item in source_data:
        for target_class, patterns in target_classes.items():
            if isinstance(patterns, dict):
                if patterns.get('Level1'):
                    result_match = find_all_matches({target_class:patterns['Level1']}, [raw_data_item])
                    if result_match: normalized_classes.append(*result_match)
                if patterns.get('Level2'):
                    patterns_first_half = patterns['Level2']['Patterns']
                    patterns_second_half = patterns['Level2']['Patterns_lvl2']
                    if multiple_patterns_match(patterns_first_half, raw_data_item):
                        result_match = find_all_matches({target_class:patterns_second_half},[raw_data_item])
                        if result_match: normalized_classes.append(*result_match)
            if isinstance(patterns, list):
                if multiple_patterns_match(patterns, raw_data_item): normalized_classes.append(target_class)
    return normalized_classes
