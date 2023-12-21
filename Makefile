OS := $(shell uname -s)

ifeq ($(OS),Darwin)
    ACTIVATE_SCRIPT=source venv/bin/activate
    PYTHON=python3.12
    FALLBACK_PYTHON=python3.11
else ifeq ($(OS),Linux)
    ACTIVATE_SCRIPT=source venv/bin/activate
    PYTHON=python3.12
    FALLBACK_PYTHON=python3.11
else
    ACTIVATE_SCRIPT=venv\\Scripts\\activate.bat
    PYTHON=python
    FALLBACK_PYTHON=python
endif

venv: requirements.txt
	@command -v $(PYTHON) >/dev/null 2>&1 \
		&& ( \
			$(PYTHON) -m venv venv \
			&& $(ACTIVATE_SCRIPT) \
			&& pip install --upgrade pip \
			&& pip install -r requirements.txt \
		) \
		|| ( \
			echo "${PYTHON} not found, using ${FALLBACK_PYTHON}"; \
			$(FALLBACK_PYTHON) -m venv venv \
			&& $(ACTIVATE_SCRIPT) \
			&& pip install --upgrade pip \
			&& pip install -r requirements.txt \
		)

run: ./app/main.py
	$(ACTIVATE_SCRIPT) && uvicorn app.main:app --reload --host 0.0.0.0 --port 8001

combine:
	$(ACTIVATE_SCRIPT) && python combiner.py $(args)

docker: Dockerfile
	docker build -t smbrine/fastapi-postgres-backend .
	docker push smbrine/fastapi-postgres-backend
