.PHONY: all clean pytest coverage flake8 black mypy isort

CMD:=poetry run
PYMODULE:=src
TESTS:=tests

# Run all the checks which do not change files
all: pytest ruff-check ruff-check-fix ruff-format build deploy

# Run the unit tests using `pytest`
pytest:
	$(CMD) pytest $(PYMODULE) $(TESTS)

# Ruff 
ruff-check:
	$(CMD) ruff check $(PYMODULE) $(TESTS)

# Ruff 
ruff-check-fix:
	$(CMD) ruff check --fix $(PYMODULE) $(TESTS)

# Ruff 
ruff-format:
	$(CMD) ruff format $(PYMODULE) $(TESTS)

# build docs
build:
	$(CMD) mkdocs build

deploy:
	$(CMD) mkdocs gh-deploy --force