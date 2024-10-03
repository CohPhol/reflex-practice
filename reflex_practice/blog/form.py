import reflex as rx

from .state import BlogPostState

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