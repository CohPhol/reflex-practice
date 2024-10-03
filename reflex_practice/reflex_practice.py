"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .ui.base import base_page

from . import blog, navigation, pages, contact

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
app.add_page(blog.blog_post_list_page, route=navigation.routes.BLOG_POSTS_ROUTE)

app.add_page(contact.contact_page, route=navigation.routes.CONTACT_ROUTE)
app.add_page(
    contact.contact_entries_list_page, 
    route=navigation.routes.CONTACT_ENTRIES_ROUTE,
    on_load=contact.ContactState.list_entries,
)
