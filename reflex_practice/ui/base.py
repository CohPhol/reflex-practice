import reflex as rx
from ..auth.state import SessionState
from .nav import navbar
from .dashboard import base_dashboard_page

from .color_mode import color_mode

def base_layout_component(child, *args, **kwargs) -> rx.Component:
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

def base_page(child: rx.Component, *args, **kwargs) -> rx.Component:
    is_logged_in = True
    if not isinstance(child, rx.Component):
        child = rx.heading("Not a valid tye of component")

    return rx.cond(
        SessionState.is_authenticated,
        base_dashboard_page(child, *args, **kwargs),
        base_layout_component(child, *args, **kwargs),
    )