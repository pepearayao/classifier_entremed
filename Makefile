#################### PACKAGE ACTIONS ###################
reinstall_package:
	@pip uninstall -y classifier_entremed || :
	@pip install -e .
