from __future__ import annotations

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Grid, VerticalScroll, Horizontal
from textual.widgets import Input, Select, TextLog, Label, Button, Header, Footer, RadioSet, RadioButton, Static
from textual.reactive import reactive, Reactive
from cookiecutter.main import cookiecutter
from textual.screen import Screen, ModalScreen

PROJECT_TYPE_OPTIONS = [("django", "django"), ("ddd", "ddd")]
CSS_PATH = "textual_static/cookiecutter.css"


class QuitScreen(ModalScreen):
    """Screen with a dialog to quit."""
    CSS_PATH = CSS_PATH
    BINDINGS = [
        ("enter", "confirm_quit", "Confirm Quit")
    ]

    def compose(self) -> ComposeResult:
        yield Grid(
            Label("Are you sure you want to quit?", id="question"),
            Button("Quit", variant="error", id="quit"),
            Button("Cancel", variant="primary", id="cancel"),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "quit":
            self.app.exit()
        else:
            self.app.pop_screen()

    def action_confirm_quit(self) -> None:
        self.app.exit()


class SuccessScreen(ModalScreen):
    """Screen with a dialog to quit."""
    CSS_PATH = CSS_PATH
    BINDINGS = [
        ("enter", "on_success", "Ok")
    ]

    def compose(self) -> ComposeResult:
        yield Grid(
            Label("Project created successfully!", id="success"),
            Button("Ok", variant="primary", id="ok"),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "ok":
            self.app.exit()

    def action_on_success(self) -> None:
        self.app.exit()


class ErrorScreen(ModalScreen):
    """Screen to display error messages."""
    CSS_PATH = CSS_PATH
    BINDINGS = [
        ("enter", "on_error_ok", "Ok")
    ]

    def __init__(self, error_message: str):
        super().__init__()
        self.error_message = error_message

    def compose(self) -> ComposeResult:
        yield Grid(
            Label(self.error_message, id="error-message"),
            Button("Ok", variant="error", id="error-button"),
            id="error-dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "error-button":
            self.app.pop_screen()

    def action_on_error_ok(self) -> None:
        self.app.exit()


class CookiecutterApp(App):
    """Prompts for project_type and project_name, then runs cookiecutter."""

    CSS_PATH = CSS_PATH
    BINDINGS = [
        ("q", "request_quit", "Quit"),
        ("enter", "on_success", "Ok"),
        ("enter", "on_error", "Ok"),
    ]

    # Reactive attributes

    project_type: str | None = reactive(None)
    project_name: str | None = reactive(None)
    app_name: str | None = reactive(None)
    project_base_name: str | None = reactive(None)

    def compose(self) -> ComposeResult:
        yield Header()
        yield TextLog(highlight=True, markup=True)
        with Horizontal():
            with RadioSet():
                yield RadioButton("django", id="project_type")
                yield RadioButton("ddd")
        yield Input(placeholder="Enter project name", id="project_name", classes="hidden")
        yield Input(placeholder="Enter app name", id="app_name", classes="hidden")
        yield Input(placeholder="Enter project base name", id="project_base_name", classes="hidden")
        yield Footer()

    def on_mount(self) -> None:
        # Focus the button with id first
        self.query_one(RadioSet).focus()

    async def on_radio_set_changed(self, event: RadioSet.Changed) -> None:
        self.project_type = str(event.pressed.label)
        self.query_one("#project_type").add_class(
            "hidden"
        )
        self.query_one("#project_name").remove_class(
            "hidden"
        )
        self.query_one("#project_name").focus()

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        self.query_one(TextLog).write(f"Event value: {event.value}, Event input: {event.input.id}")
        if event.input.id == "project_name":
            self.project_name = event.value.strip()
            self.query_one("#project_name").add_class(
                "hidden"
            )
            self.query_one("#app_name").remove_class(
                "hidden"
            )
            self.query_one("#app_name").focus()
        elif event.input.id == "app_name":
            self.app_name = event.value
            self.query_one("#app_name").add_class(
                "hidden"
            )
            self.query_one("#project_base_name").remove_class(
                "hidden"
            )
            self.query_one("#project_base_name").focus()
        elif event.input.id == "project_base_name":
            self.project_base_name = event.value
            self.query_one("#project_base_name").add_class(
                "hidden"
            )
        self.try_run_cookiecutter()

    def action_request_quit(self) -> None:
        self.push_screen(QuitScreen())

    def action_on_success(self) -> None:
        self.push_screen(SuccessScreen())

    def try_run_cookiecutter(self):
        if self.project_type and self.project_name and self.app_name and self.project_base_name:
            self.run_cookiecutter(self.project_type, self.project_name, self.app_name, self.project_base_name)

    def run_cookiecutter(self, project_type: str, project_name: str, app_name: str, project_base_name: str) -> None:
        try:
            cookiecutter(".", no_input=True, extra_context={
                "project_type": project_type,
                "project_name": project_name,
                "app_name": app_name,
                "project_base_name": project_base_name
            })
            self.action_on_success()
        except Exception as e:
            self.push_screen(ErrorScreen(str(e)))


if __name__ == "__main__":
    app = CookiecutterApp()
    app.run()
