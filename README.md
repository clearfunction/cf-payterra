# cf-payterra

---

## Table of Contents

- [Project Organization](#project-organization)
- [Local Development](#local-development)

---

## Project Organization

---

```
.
├── .env
├── .env.example
├── README.md
└── src                                     <- Modules for deployable API
    ├── requirements.txt
    ├── api
    │   └── server.py                       <- API entrypoint
    ├── db
    │   ├── payterra_test.sqlite            <- SQLite Sample DB
    │   └── query.py                        <- Helper methods to query SQLite Sample DB
    ├── middleware
    │   └── exception.py                    <- Exception Handling for FastAPI endpoints
    ├── models
    │   ├── responses
    │   │   └── ... <Pydantic classes for API request/response specification> ...
    │   └── ... <Pydantic classes for API request/response specification> ...
    └── venv                                <- API Virtual Environment built with local requirements
```

---

## Local Development

---

### Activate Virtual Environment

Run the following commands to activate the appropriate virtual environment.

```bash
$ cd cf-payterra/src
$ source venv/bin/activate
$ pip install -r requirements.txt
```

When you are finished running commands, close the virtual environment by running:

```bash
$ deactivate
```

---

### Run the API Server

To start the API server locally, run:

```bash
$ cd cf-payterra/src
$ uvicorn api.server:app --host 0.0.0.0 --port 8000
```

---
