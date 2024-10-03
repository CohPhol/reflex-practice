import reflex as rx

from typing import List
from .model import ContactEntryModel
from sqlmodel import select

class ContactState(rx.State):
    form_data: dict = {}
    entries: List['ContactEntryModel'] = []

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        data = {}
        for key, value in form_data.items():
            if value == "" or value is None:
                continue
            data[key] = value
        with rx.session() as session:
            db_entry = ContactEntryModel(**data)
            session.add(db_entry)
            session.commit()

    def list_entries(self):
        with rx.session() as session:
            entries = session.exec(
                select(ContactEntryModel)
            ).all()
            self.entries = entries