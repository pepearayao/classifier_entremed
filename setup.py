from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='classifier_entremed',
      version="0.0.1",
      description="Classifier package for Entremed project to clean data and classify job posts.",
      author="Entremed",
      author_email="pepe@entremed.io",
      url="https://github.com/pepearayao/classifier_entremed",
      install_requires=requirements,
      packages=find_packages(),
      test_suite="tests",
      include_package_data=True,
      zip_safe=False)
