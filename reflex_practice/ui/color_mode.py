import reflex as rx

def color_mode() -> rx.Component:
    return rx.fragment(
        rx.color_mode.button(position="bottom-right")
    )