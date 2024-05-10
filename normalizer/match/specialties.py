import pandas as pd
import normalizer.match.global_matchers
from normalizer.config_files.loader import load_config_file

def find_specialty():
    specialties = load_config_file('specialties')
    print(specialties)


if __name__ == '__main__':
    find_specialty()
