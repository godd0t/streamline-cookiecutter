from rich.console import Console
console = Console()

project_name = '{{ cookiecutter.project_name }}'
project_type = '{{ cookiecutter.project_type }}'


if project_type == "ddd" and project_name == "core_config":
    console.print(
        "You cannot use the core_config name for a ddd project", style="bold red"
    )
    raise SystemExit(1)
