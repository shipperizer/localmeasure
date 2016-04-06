
.PHONY: test install run

PIP?=pip3
PYTHON?=python3

install:
	$(PIP) install -r requirements.txt

test:
	py.test test_find.py

run:
	$(PYTHON) prettyfind.py
