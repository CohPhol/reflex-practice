import reflex as rx

from typing import List
from ..models import ContactEntryModel
from sqlmodel import select
from ..auth.state import SessionState

class ContactState(SessionState):
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
        if self.my_user_id is not None:
            data['user_id'] = self.my_user_id
        if self.my_user_info_id is not None:
            data['user_info_id'] = self.my_user_info_id

        print("Contact data: ", data)
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