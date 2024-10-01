import reflex as rx

from .. import navigation
from ..ui.base import base_page

def form_field(
    label: str, placeholder: str, type: str, name: str, required=False
) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input(
                    placeholder=placeholder, type=type, required=required
                ),
                as_child=True,
            ),
            direction="column",
            spacing="1",
        ),
        name=name,
        width="100%",
    )

def contact_form() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="mail-plus", size=32),
                    color_scheme="blue",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.heading(
                        "Send us a message",
                        size="4",
                        weight="bold",
                    ),
                    rx.text(
                        "Fill the form to contact us",
                        size="2",
                    ),
                    spacing="1",
                    height="100%",
                ),
                height="100%",
                spacing="4",
                align_items="center",
                width="100%",
            ),
            rx.form.root(
                rx.flex(
                    rx.flex(
                        form_field(
                            "First Name",
                            "First Name",
                            "text",
                            "first_name",
                        ),
                        form_field(
                            "Last Name",
                            "Last Name",
                            "text",
                            "last_name",
                        ),
                        spacing="3",
                        flex_direction=[
                            "column",
                            "row",
                            "row",
                        ],
                    ),
                    rx.flex(
                        form_field(
                            "Email",
                            "user@reflex.dev",
                            "email",
                            "email",
                        ),
                        form_field(
                            "Phone", "Phone", "tel", "phone"
                        ),
                        spacing="3",
                        flex_direction=[
                            "column",
                            "row",
                            "row",
                        ],
                    ),
                    rx.flex(
                        rx.text(
                            "Message",
                            style={
                                "font-size": "15px",
                                "font-weight": "500",
                                "line-height": "35px",
                            },
                        ),
                        rx.text_area(
                            placeholder="Message",
                            name="message",
                            resize="vertical",
                        ),
                        direction="column",
                        spacing="1",
                    ),
                    rx.form.submit(
                        rx.button("Submit"),
                        as_child=True,
                    ),
                    direction="column",
                    spacing="2",
                    width="100%",
                ),
                on_submit=lambda form_data: rx.window_alert(
                    form_data.to_string()
                ),
                reset_on_submit=False,
            ),
            width="100%",
            direction="column",
            spacing="4",
        ),
        size="3",
    )

@rx.page(route=navigation.routes.CONTACT_ROUTE)
def contact_page() -> rx.Component:
    my_form = contact_form()

    my_child = rx.vstack(
        rx.heading("Contact Us", size="9"),
        rx.text(
            "Contact!!",
            size="5",
        ),
        my_form,

        spacing="5",
        justify="center",
        align="center",
        text_align="center",
        min_height="85vh",
        id='my-child',
    )
    return base_page(my_child)