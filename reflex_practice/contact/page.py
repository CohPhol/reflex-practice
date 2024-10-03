import reflex as rx

from .. import navigation

from ..ui.base import base_page

from . import form, state, model

def contact_entry_list_item(contact: model.ContactEntryModel):
    return rx.box(
        rx.heading(contact.first_name),
        rx.text(contact.message),
        padding='1em',
    )

def contact_entries_list_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Contact Us", size="5"),
            rx.foreach(state.ContactState.entries, contact_entry_list_item),
            spacing="5",
            align="center",
            min_height="85vh",
        ))

# @rx.page(route=navigation.routes.CONTACT_ROUTE)
def contact_page() -> rx.Component:
    my_form = form.contact_form()

    my_child = rx.vstack(
        rx.heading("Contact Us", size="9"),
        rx.text(
            "Contact!!",
            size="5",
        ),
        rx.desktop_only(
            rx.box(
                my_form,
                width="50vw",
            )
        ),
        rx.tablet_only(
            my_form,
            width="75vw",
        ),
        rx.mobile_only(
            my_form,
            width="85vw",
        ),

        spacing="5",
        justify="center",
        align="center",
        text_align="center",
        min_height="85vh",
        id='my-child',
    )
    return base_page(my_child)