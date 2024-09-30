import reflex as rx
from .nav import navbar
from .color_mode import color_mode

def base_page(child: rx.Component, hide_navbar = False, *args, **kwargs) -> rx.Component:

    if not isinstance(child, rx.Component):
        child = rx.heading("Not a valid tye of component")

    if hide_navbar:
        return rx.container(
            child,
            rx.logo(),
            color_mode(),
        )
    
    return rx.fragment(
        navbar(),
        rx.box(
            child,
            id="my-content-area",
            padding="1em",
            text_align="center",
            width="100%",
        ),
        rx.logo(),
        color_mode(),
        id="my-base-container",
    )
