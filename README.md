# Streamline Cookiecutter

[![Generate Template](https://img.shields.io/badge/Generate%20Template-Click%20Here-brightgreen)](
(python3 -m streamline.run_cookiecutter)
)

This is a cookiecutter template for Django projects. The main goal is to have a
streamlined process for creating new Django projects, with a focus on fast
development and deployment. The template is based on the
[django-docker-quickstart](https://github.com/godd0t/django-docker-quickstart) project.


## Features

Two project structures: `django` and `ddd` (Domain Driven Design).

- `django` is a standard Django project structure. It is a good choice for
  smaller projects.
- `ddd` is a Domain Driven Design project structure. It is a good choice for
  larger projects.

Full Docker support for development and production environments.

- Development environment with hot reloading.
- Production environment with Nginx and Traefik.
- PostgreSQL database as the default database.
- Redis for caching and Celery.
- Celery worker and beat service for running background and scheduled tasks.


## Included Packages and Tools

- Pytest: Testing framework
- Pytest Sugar: Plugin for pytest that changes the default look
- Pytest Django: Plugin for pytest that provides useful tools for testing Django applications
- Coverage: Test coverage
- Ruff: Linter
- Black: Code formatter


## Requirements

- Docker & Docker Compose [Install and Use Docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)
- Python 3.10 or higher
- Make(optional for shortcuts)
- Cookiecutter


## Getting Started

To get started, follow these steps:

If you want to use cookiecutter, you need to install it first:

```
pip install cookiecutter
```

If you want to use the make shortcuts, install the dependencies in `requirements` directory:

```
pip install -r requirements/requirements.txt
```

Then, run the following command:

```
cookiecutter .
```

You will be prompted to enter some values. After that, the project will be
created in the current directory.

If you want to use the make shortcuts, run the following command:

```
make template
```

Why I used make instead of cookiecutter? Because the project provides a
custom CLI that is based on [Textual](https://github.com/textualize/textual/). I wanted to provide a better experience
for the user, so I used make to run the CLI.



