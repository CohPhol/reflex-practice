import reflex as rx
from ..ui.base import base_page
from . import form

from .state import BlogEditFormState

def edit_blog_page() -> rx.Component:
    my_form = form.blog_post_edit_form()
    post = BlogEditFormState.post
    my_child = rx.vstack(
        rx.heading("EDIT BLOG ", post.title, size="8"),
        my_form,
        spacing="5",
        align="center",
        min_height="85vh",
    )
    return base_page(my_child)