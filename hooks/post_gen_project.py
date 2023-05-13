import os
import shutil

project_type = '{{ cookiecutter.project_type }}'

if project_type == 'django':
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
