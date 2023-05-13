#!/bin/bash -e

PACKAGE_PATH="streamline"
TEMPLATE_PATH="{{cookiecutter.project_base_name}}"

ruff "$PACKAGE_PATH" "$TEMPLATE_PATH"
black "$PACKAGE_PATH" "$TEMPLATE_PATH" --check
