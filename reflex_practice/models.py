import sqlmodel
import reflex as rx
from datetime import datetime
import sqlalchemy
from sqlmodel import Field, Relationship
from typing import Optional, List
from . import utils

from reflex_local_auth.user import LocalUser


class UserInfo(rx.Model, table=True):
    email: str
    user_id: int = sqlmodel.Field(foreign_key="localuser.id")
    user: LocalUser | None = Relationship()
    posts: List['BlogPost'] = Relationship(back_populates='userinfo')
    contact_entries: List['ContactEntryModel'] = Relationship(back_populates='userinfo')

    created_at: datetime = Field(
        default_factory=utils.timing.get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default': sqlalchemy.func.now()
        },
        nullable=False,
    )
    updated_at: datetime = Field(
        default_factory=utils.timing.get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'onupdate': sqlalchemy.func.now(),
            'server_default': sqlalchemy.func.now(),
        },
        nullable=False,
    )
    # is_admin: bool = False
    # created_from_ip: str

class BlogPost(rx.Model, table=True):
    user_info_id: int = Field(default=None, foreign_key='userinfo.id')
    user_info: Optional['UserInfo'] = Relationship(back_populates="posts")
    title: str
    content: str
    created_at: datetime = Field(
        default_factory=utils.timing.get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default': sqlalchemy.func.now()
        },
        nullable=False,
    )
    updated_at: datetime = Field(
        default_factory=utils.timing.get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'onupdate': sqlalchemy.func.now(),
            'server_default': sqlalchemy.func.now(),
        },
        nullable=False,
    )
    publish_active: bool = False
    publish_date: datetime = Field(
        default=None,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={},
        nullable=True,
    )

class ContactEntryModel(rx.Model, table=True):
    user_id: int = Field(nullable=True)
    user_info_id: int = Field(default=None, foreign_key='userinfo.id')
    user_info: Optional['UserInfo'] = Relationship(back_populates="contact_entries")
    first_name: str
    last_name: str
    email: str = Field(nullable=True)
    number: str = Field(nullable=True)
    message: str
    created_at: datetime = Field(
        default_factory=utils.timing.get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default': sqlalchemy.func.now()
        },
        nullable=False,
    )