#!/bin/bash -e

APP_PATH="{{cookiecutter.project_base_name}}"

ruff $APP_PATH
black $APP_PATH --check
