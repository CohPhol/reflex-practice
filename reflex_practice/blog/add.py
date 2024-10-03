import reflex as rx

from ..ui.base import base_page

from . import form

def create_blog_page() -> rx.Component:
    # Welcome Page (Index)
    my_form = form.blog_form()
    my_child = rx.vstack(
        rx.heading("CREATE BLOG", size="8"),
        my_form,
        spacing="5",
        align="center",
        min_height="85vh",
    )
    return base_page(my_child)