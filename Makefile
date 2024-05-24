EXPECTED_PYTHON_VERSION := 3.11.8
CURRENT_PYTHON_VERSION := $(shell python --version | awk 'NR==1{print $$2}')
PYTHON_ROOT_DIRECTORY := python_challenges

.PHONY: check requirements lint init

check: # @ HELP Verifies the version of python you are using is the version you are expecting.
check:
	@echo "Checking python version... expecting version of [${EXPECTED_PYTHON_VERSION}], [${CURRENT_PYTHON_VERSION}]" && \
	if [ "${EXPECTED_PYTHON_VERSION}" != "${CURRENT_PYTHON_VERSION}" ]; then echo "Please ensure you are running python ${EXPECTED_PYTHON_VERSION}" && exit 1; fi
requirements: check
	pip install -r ${PYTHON_ROOT_DIRECTORY}/requirements.txt
lint: requirements
	pylint ${PYTHON_ROOT_DIRECTORY}
test: lint
	python3 -m unittest discover -v ${PYTHON_ROOT_DIRECTORY}