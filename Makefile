install:
	@poetry install

lint:
	@poetry run flake8 gendiff

test:
	@poetry run pytest -vv
	@poetry run coverage run ./tests/test_gendiff.py

.PHONY: install lint test
