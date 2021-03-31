test:
	cd src/ && python3 -m pytest -vv

lint:
	@pre-commit run --all-files

check:
	make lint test

install-hooks:
	pre-commit install -t pre-commit -t commit-msg
