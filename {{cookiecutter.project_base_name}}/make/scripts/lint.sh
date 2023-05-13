#!/bin/bash -e

APP_PATH="src"

{% if cookiecutter.use_ruff %}
ruff $APP_PATH
{% endif %}

{% if cookiecutter.use_black %}
black $APP_PATH --check
{% endif %}
