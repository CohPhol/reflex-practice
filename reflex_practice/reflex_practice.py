"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .ui.base import base_page

from . import pages

class State(rx.State):
    """The app state."""
    label = "Welcome to Reflex!"

    def handle_input_change(self, value):
        self.label = value
    

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.vstack(
        rx.heading(State.label, size="9"),

        rx.text(
            "Get started by editing ",
            rx.code(f"{config.app_name}/{config.app_name}.py"),
            size="5",
        ),

        rx.input(
                default_value=State.label,
                on_change=State.handle_input_change,
            ),

        rx.link(
            rx.button("Check out our docs!"),
            href="https://reflex.dev/docs/getting-started/introduction/",
            is_external=True,
        ),
        spacing="5",
        justify="center",
        align="center",
        text_align="center",
        min_height="85vh",
        id='my-child',
    )
    return base_page(my_child)

app = rx.App()
app.add_page(index)
app.add_page(pages.about_page, route='/about')
app.add_page(pages.pricing_page, route='/pricing')