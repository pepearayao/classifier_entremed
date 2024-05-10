import json
import os

def test_large_data(jobpost_sample):
    print(jobpost_sample.keys())
    assert len(jobpost_sample) == 8
