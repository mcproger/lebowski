test:
	cd src/ && python3 -m pytest

lint:
	flake8 src/

types:
	mypy src/

check:
	make lint test