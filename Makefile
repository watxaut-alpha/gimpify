init:
	pip install -r requirements.txt

test:
	pytest tests/test_montage.py

.PHONY: init test