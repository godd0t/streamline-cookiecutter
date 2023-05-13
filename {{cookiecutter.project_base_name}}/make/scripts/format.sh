#!/bin/bash -e

APP_PATH="src"

{% if cookiecutter.use_ruff %}
ruff $APP_PATH --fix
{% endif %}

{% if cookiecutter.use_black %}
black $APP_PATH
{% endif %}
