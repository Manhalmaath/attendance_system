import datetime
from typing import Optional

from ninja import Schema
from pydantic import EmailStr, Field, UUID4


class MessageOut(Schema):
    detail: str


class SessionOut(Schema):
    name: str
    date: datetime.date
