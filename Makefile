init:
	pip install -r requirements.txt

test:
	pytest tests/test_montage.py

build:
	python3 setup.py sdist bdist_wheel

upload:
	twine upload --skip-existing dist/*

.PHONY: init test