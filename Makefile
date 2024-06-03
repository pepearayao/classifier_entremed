#################### PACKAGE ACTIONS ###################
reinstall_package:
	@pip uninstall -y classifier_entremed || :
	@pip install -e .


all_test:
	@pytest -vv

data_type_test:
	@pytest -v tests/jobs_basics -k 'data_type'
