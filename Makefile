# Install

install:
	poetry install --no-root

	git init

	cp .github/hooks/pre-commit.sh .git/hooks/pre-commit

	chmod +x .git/hooks/pre-commit


# Lint

black:
	poetry run black .


lint:
	poetry run flake8 tests src


plint:
	flake8 tests src


types:
	poetry run mypy tests src


ptypes:
	mypy tests src


# Tests

coverage:
	poetry run coverage run src/main.py && poetry run coverage report


unittests:
	poetry run pytest -s tests


test: lint types coverage unittests run


# Run

run:
	docker compose up --build -d
