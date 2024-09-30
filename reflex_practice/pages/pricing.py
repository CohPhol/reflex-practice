import reflex as rx

from ..ui.base import base_page

def pricing_page() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.vstack(
        rx.heading("Pricing Page", size="9"),

        rx.text(
            "Pricing Page!!",
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