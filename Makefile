default: FORCE
	python3 app/yatta.py

tests: FORCE
	python3 tests/functional_tests.py

FORCE:
