import reflex as rx
import reflex_local_auth

from .. import navigation
from ..ui.base import base_page

# @rx.page(route=navigation.routes.ABOUT_ROUTE)
@reflex_local_auth.require_login
def protected_page() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.vstack(
        rx.heading("Protected Page", size="9"),

        rx.text(
            "Protected Page!!",
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