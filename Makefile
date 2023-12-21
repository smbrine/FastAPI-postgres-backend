OS := $(shell uname -s)

ifeq ($(OS),Darwin)
    ACTIVATE_SCRIPT=source venv/bin/activate
    PYTHON=python3
else ifeq ($(OS),Linux)
    ACTIVATE_SCRIPT=source venv/bin/activate
    PYTHON=python3
else
    ACTIVATE_SCRIPT=venv\\Scripts\\activate.bat
    PYTHON=python
endif

setup: requirements.txt
	$(PYTHON) -m venv venv
	$(ACTIVATE_SCRIPT)
	pip install --upgrade pip
	pip install -r requirements.txt

run: ./app/main.py
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8001

combine:
	python combiner.py $(args)

docker: Dockerfile
	docker build -t smbrine/fastapi-postgres-backend .
	docker push smbrine/fastapi-postgres-backend