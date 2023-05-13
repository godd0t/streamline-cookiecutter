#!/bin/bash -e

{% if cookiecutter.use_pytest %}
coverage run -m pytest -v
exit 0
{% endif %}
