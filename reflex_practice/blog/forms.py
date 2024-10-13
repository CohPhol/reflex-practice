import reflex as rx

from . import state

def blog_post_create_form():
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
                    height="50vh",
                ),
                rx.button("Submit", type="submit"),
                justify='center',
                align='center',
            ),
            on_submit=state.BlogCreateFormState.handle_submit,
            reset_on_submit=True,
        ),
        width="50%",
    )

def blog_post_edit_form() -> rx.Component:
    post = state.BlogEditFormState.post
    title = post.title
    publish_active = post.publish_active
    post_content = state.BlogEditFormState.post_content

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
                            value=title,
                            placeholder="Title",
                            name="title",
                            width="100%",
                        ),
                        rx.text_area(
                            value=post_content,
                            on_change=state.BlogEditFormState.set_post_content,
                            placeholder="Content",
                            name="content",
                            width="100%",
                            height="50vh",
                        ),
                        rx.flex(
                            rx.switch(
                                default_checked=state.BlogEditFormState.post_publish_active,
                                on_change=state.BlogEditFormState.set_post_publish_active,
                                name='publish_active',
                            ),
                            rx.text("Publish Active"),
                            spacing="2",
                        ),
                        rx.cond(
                            state.BlogEditFormState.post_publish_active,
                            rx.box(
                                rx.hstack(
                                    rx.input(
                                        default_value=state.BlogEditFormState.publish_display_date,
                                        type='date',
                                        name='publish_date',
                                        width='100%',
                                    ),
                                    rx.input(
                                        default_value=state.BlogEditFormState.publish_display_time,
                                        type='time',
                                        name='publish_time',
                                        width='100%',
                                    ),
                                    width='100%',
                                ),
                                width='100%',
                            )
                        ),
                        rx.button("Submit", type="submit"),
                        justify='center',
                        align='center',
                    ),
                    on_submit=state.BlogEditFormState.handle_submit,
                ),
                width="50%",
            )