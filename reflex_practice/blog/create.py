import reflex as rx

from ..ui.base import base_page

from . import forms

def create_blog_page() -> rx.Component:
    my_form = forms.blog_form()
    my_child = rx.vstack(
        rx.heading("CREATE BLOG", size="8"),
        my_form,
        spacing="5",
        align="center",
        min_height="85vh",
    )
    return base_page(my_child)