"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import reflex_local_auth

from rxconfig import config
from .ui.base import base_page

from .auth.pages import (
    my_login_page,
    my_register_page,
    my_logout_confirmation_page,
)

from .auth.state import SessionState

from . import auth, blog, navigation, pages, contact

class State(rx.State):
    """The app state."""
    label = "Welcome to Reflex!"

    def handle_input_change(self, value):
        self.label = value
    

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    my_user_object = SessionState.authenticated_user

    my_child = rx.vstack(
        rx.heading(State.label, size="9"),
        rx.text(my_user_object.to_string()),
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

app.add_page(
    my_login_page,
    route=reflex_local_auth.routes.LOGIN_ROUTE,
    title="Login",
)
app.add_page(
    my_register_page,
    route=reflex_local_auth.routes.REGISTER_ROUTE,
    title="Register",
)
app.add_page(
    my_logout_confirmation_page,
    route=navigation.routes.LOGOUT_ROUTE,
    title="Logout",
)

app.add_page(
    blog.blog_post_list_page, 
    route=navigation.routes.BLOG_POSTS_ROUTE,
    on_load=blog.BlogPostState.list_entries,
)
app.add_page(
    blog.create_blog_page, 
    route=navigation.routes.BLOG_POSTS_ADD_ROUTE,
)
app.add_page(
    blog.blog_post_detail_page, 
    route="/blog/[blog_id]",
    on_load=blog.BlogPostState.get_post_detail,
)
app.add_page(
    blog.edit_blog_page, 
    route="/blog/[blog_id]/edit",
    on_load=blog.BlogPostState.get_post_detail,
)

app.add_page(contact.contact_page, route=navigation.routes.CONTACT_ROUTE)
app.add_page(
    pages.protected.protected_page, 
    route="/protected",
    on_load=SessionState.on_load
)
app.add_page(
    contact.contact_entries_list_page, 
    route=navigation.routes.CONTACT_ENTRIES_ROUTE,
    on_load=contact.ContactState.list_entries,
)
