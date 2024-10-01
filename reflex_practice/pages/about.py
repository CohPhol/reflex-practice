import reflex as rx

from .. import navigation
from ..ui.base import base_page

@rx.page(route=navigation.routes.ABOUT_ROUTE)
def about_page() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.vstack(
        rx.heading("About Us", size="9"),

        rx.text(
            "About!!",
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