directories = src main.py tests

format:
	isort $(directories)
	black $(directories)

unit-test:
	pytest -n auto --disable-socket --tb=short tests/unit
