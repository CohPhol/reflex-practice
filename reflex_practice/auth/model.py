import sqlmodel
import reflex as rx
from datetime import datetime
import sqlalchemy
from sqlmodel import Field
from .. import utils

import reflex_local_auth


class UserInfo(rx.Model, table=True):
    email: str
    user_id: int = sqlmodel.Field(foreign_key="localuser.id")

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