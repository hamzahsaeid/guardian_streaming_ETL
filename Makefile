

# Example Makefile


# Useful variables

PYTHON_INTERPRETER=PYTHON_INTERPRETER
PIP=PIP
SHELL=/bin/bash # if this isn't set the shell will default to 'sh'

# creating virtual environment
create-environment:
	$(PYTHON_INTERPRETER) -m venv venv

# activate + run commands like pip install
install-requirements: create-environment
	source venv/bin/activate && $(PIP) install -r requirements.txt

# Pytest
unit-test: install-requirements
	source venv/bin/activate && PYTHONPATH=$(PYTHONPATH) pytest - vv

# install code quality tools
install-dev-tools:
source venv/bin/activate && $(PIP) install bandit safety flake8

# run code quality checks
security-checks:
source venv/bin/activate && safety check -r ./requirements.txt
source venv/bin/activate && bandit -lll */*.py *c/*.py

check-pep8-compliance:
source venv/bin/activate && flake8 src test

run-checks: unit-test security-checks check-pep8-compliance