import reflex as rx
import sqlalchemy

from datetime import datetime
from sqlmodel import Field


class Chat(rx.Model, table=True):
    #id
    #messaghe
    created_at: datetime = Field(
        sa_type = sqlalchemy.DateTime(timezone=True)
    )
