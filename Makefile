#################### PACKAGE ACTIONS ###################
reinstall_package:
	@pip uninstall -y classifier_entremed || :
	@pip install -e .


#################### TESTS ###################
all_test:
	@pytest -vv

data_type_test:
	@pytest -v -k 'data_type'

specialty_test:
	@pytest -v -k 'specialty'

location_test:
	@pytest -v -k 'location'

job_schedule_test:
	@pytest -v -k 'job_schedule'

job_shift_test:
	@pytest -v -k 'job_shift'

job_engagement_test:
	@pytest -v -k 'job_engagement'

job_company_test:
	@pytest -v -k 'company'

job_accesibility_test:
	@pytest -v -k 'inclusive'

job_certificates_test:
	@pytest -v -k 'certificates'

job_emails_test:
	@pytest -v -k 'emails'
