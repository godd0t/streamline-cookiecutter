import os
import shutil

project_type = "{{ cookiecutter.project_type }}"
use_pytest = "{{ cookiecutter.use_pytest }}" == "True"
use_ruff = "{{ cookiecutter.use_ruff }}" == "True"
use_black = "{{ cookiecutter.use_black }}" == "True"
use_docker = "{{ cookiecutter.use_docker }}" == "True"
use_make = "{{ cookiecutter.use_make }}" == "True"
use_celery = "{{ cookiecutter.use_celery }}" == "True"
use_celery_beat = "{{ cookiecutter.use_celery_beat }}" == "True"
use_postgres = "{{ cookiecutter.use_postgres }}" == "True"
use_nginx = "{{ cookiecutter.use_nginx }}" == "True"
use_traefik = "{{ cookiecutter.use_traefik }}" == "True"
use_git = "{{ cookiecutter.use_git }}" == "True"


if project_type == "django":
    # Remove the ddd folder
    shutil.rmtree("ddd")
    # Copy the django folder,subfolders and files to the root of the project
    for entity in os.listdir("django"):
        if os.path.isdir("django/" + entity):
            shutil.copytree("django/" + entity, entity)
        else:
            shutil.copy("django/" + entity, entity)
    # Remove the django folder
    shutil.rmtree("django")
elif project_type == "ddd":
    # Remove django folder
    shutil.rmtree("django")
    # Copy the ddd folder,subfolders and files to the root of the project
    for entity in os.listdir("ddd"):
        if os.path.isdir("ddd/" + entity):
            shutil.copytree("ddd/" + entity, entity)
        else:
            shutil.copy("ddd/" + entity, entity)
    # Remove the ddd folder
    shutil.rmtree("ddd")


if not use_docker:
    print("Removing docker files")
    print(os.getcwd())
    # Remove docker files
    shutil.rmtree("docker-compose")
    shutil.rmtree("deployment")

if not use_make:
    print("Removing Makefile")
    print(os.getcwd())
    shutil.rmtree("make")


if not use_git:
    print("Removing git files")
    print(os.getcwd())
    # Remove git files
    shutil.rmtree("git")
