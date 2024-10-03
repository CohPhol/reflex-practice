import reflex as rx

from .state import BlogPostState
from .state import BlogEditFormState

def blog_form():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Title",
                    name="title",
                    width="100%",
                ),
                rx.text_area(
                    placeholder="Content",
                    name="content",
                    width="100%",
                ),
                rx.button("Submit", type="submit"),
                justify='center',
                align='center',
            ),
            on_submit=BlogPostState.handle_submit,
            reset_on_submit=True,
        ),
    )

def blog_post_edit_form() -> rx.Component:
    post = BlogEditFormState.post
    title = post.title
    post_content = BlogEditFormState.post_content

    return rx.vstack(
                rx.form(
                    rx.box(
                        rx.input(
                            type='hidden',
                            name='post_id',
                            value=post.id,
                        ),
                        display='none',
                    ),
                    rx.vstack(
                        rx.input(
                            defaul_value=title,
                            placeholder="Title",
                            name="title",
                            width="100%",
                        ),
                        rx.text_area(
                            value=post_content,
                            on_change=BlogEditFormState.set_post_content,
                            placeholder="Content",
                            name="content",
                            width="100%",
                        ),
                        rx.button("Submit", type="submit"),
                        justify='center',
                        align='center',
                    ),
                    on_submit=BlogEditFormState.handle_submit,
                ),
            )