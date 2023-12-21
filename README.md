# FastAPI-postgres-backend

## Description
FastAPI-postgres-backend is an API designed to provide access to a diverse collection of job interview questions. It aims to assist users in preparing for job interviews by offering a variety of real interview questions, facilitated through a FastAPI framework.

## Features
- Access to a diverse set of job interview questions.
- Self-documentation through FastAPI, providing easy access to API endpoint documentation.

## Installation
### Prerequisites
- Python >=3.11
- pip
- Docker (optional)
- Make (optional)

### Setting up the Environment
FastAPI-postgres-backend requires the following environment variables to run:

```env
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_HOST
POSTGRES_PORT 
POSTGRES_DB 
SQL_DRIVER 'postgresql+asyncpg'
```

These variables are predefined but can be customized based on your database configuration.

### Running with Docker
FastAPI-postgres-backend includes a Dockerfile for easy deployment. To build and run the Docker container:

```bash
docker run -p 8001:8001 smbrine/fastapi-postgres-backend
```

The service will be available on `http://localhost:8001`.

## Usage
After running the application, you can access the self-documented API interface provided by FastAPI to explore and test available endpoints.

## Development
The project is currently in active development. Note that the Kubernetes file is still under development and not recommended for use at this stage.

## Makefile Usage
The Makefile includes commands for setting up the environment and running the application:

- `make setup`: Set up the Python virtual environment and install dependencies.
- `make run`: Run the application on `http://localhost:8001`.
- `make combine`: ...

The `make docker` command is intended for personal use and not recommended for general users.

## Contributing
There are no specific contribution guidelines. Feel free to change anything and offer updates to the project.

## Security
Currently, there are no specific security features implemented in the application.

## License
This project is licensed under the GNU General Public License.

