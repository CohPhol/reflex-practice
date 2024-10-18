import reflex as rx
from .sidebar import sidebar

from .color_mode import color_mode

def base_dashboard_page(child: rx.Component, *args, **kwargs) -> rx.Component:

    if not isinstance(child, rx.Component):
        child = rx.heading("Not a valid tye of component")

    return rx.fragment(
        rx.hstack(
            sidebar(),
            rx.box(
                child,
                rx.logo(),
                id="my-content-area",
                padding="1em",
                text_align="center",
                width="100%",
            ),
        ),
        id="my-base-container",
    )
