import reflex as rx

from .state import ContactState

def contact_form():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.hstack(
                    rx.input(
                        placeholder="First Name",
                        name="first_name",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Last Name",
                        name="last_name",
                        width="100%",
                    ),
                    width="100%",
                ),
                rx.hstack(
                    rx.input(
                        placeholder="Email",
                        name="email",
                        type="email",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Phone Number",
                        name="number",
                        width="100%",
                    ),
                    width="100%",
                ),
                rx.text_area(
                    placeholder="Message",
                    name="message",
                    width="100%",
                ),
                rx.button("Submit", type="submit"),
                justify='center',
                align='center',
            ),
            on_submit=ContactState.handle_submit,
            reset_on_submit=True,
        ),
    )