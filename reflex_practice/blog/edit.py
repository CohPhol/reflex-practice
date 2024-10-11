import reflex as rx
from ..ui.base import base_page
from . import forms

from .state import BlogEditFormState

def edit_blog_page() -> rx.Component:
    my_form = forms.blog_post_edit_form()
    post = BlogEditFormState.post
    my_child = rx.vstack(
        rx.heading("EDIT BLOG ", post.title, size="8"),
        my_form,
        spacing="5",
        align="center",
        min_height="85vh",
    )
    return base_page(my_child)