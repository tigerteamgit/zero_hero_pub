install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_*.py

format:
	black *.py mylib/*.py

lint:
	pylint --disable=R,C *.py mylib/*py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor:
	format lint

deploy:
	@echo "Deploying to production..."

all: install lint test format deploy

MAKE := make