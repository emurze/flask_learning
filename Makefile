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
	mypy --config setup.cfg tests src


# Tests

coverage:
	poetry run coverage run src/app.py && poetry run coverage report


unittests:
	poetry run pytest -s tests


# test: lint types coverage unittests
test: lint types unittests

# Run

run:
	docker compose up --build -d

run-prod:
	docker compose -f docker-compose.prod.yml up -d --build


# Clean

down:
	docker compose down
	docker compose -f docker-compose.prod.yml down

clean:
	docker compose down -v
	docker compose -f docker-compose.prod.yml down -v

