#!/bin/bash -e

APP_PATH="{{cookiecutter.project_base_name}}"

ruff $APP_PATH --fix
black $APP_PATH