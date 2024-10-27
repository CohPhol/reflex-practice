import reflex as rx

from ..ui.base import base_page

from . import state

def blog_post_detail_page() -> rx.Component:
    can_edit = True
    edit_link = rx.link("Edit", href=f"/blog/{state.BlogPostState.blog_post_id}/edit")
    edit_link_element = rx.cond(
        can_edit,
        edit_link,
        rx.fragment(""),
    )
    my_child = rx.vstack(
        rx.hstack(
            rx.heading(state.BlogPostState.post.title, size="9"),
            rx.heading(f" - {state.BlogPostState.blog_post_id}", size="9"),
        ),
        edit_link_element,
        rx.text(
            "User Info ID: ", state.BlogPostState.post.user_info_id,
            white_space="pre-wrap",
        ),
        rx.text(
            "User Info: ", state.BlogPostState.post.user_info.to_string(),
            white_space="pre-wrap",
        ),
        rx.text(
            "User Info: ", state.BlogPostState.post.user_info.user.to_string(),
            white_space="pre-wrap",
        ),
        rx.text(
            state.BlogPostState.post.publish_date,
            white_space="pre-wrap",
        ),
        rx.text(
            state.BlogPostState.post.content,
            white_space="pre-wrap",
        ),
        spacing="5",
        align="center",
        min_height="85vh",
    )
    return base_page(my_child)