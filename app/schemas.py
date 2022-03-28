import datetime

from ninja import Schema
from pydantic import EmailStr, UUID4


class MessageOut(Schema):
    detail: str


class SessionOut(Schema):
    id: UUID4
    name: str
    date: datetime.date


class AttendanceIn(Schema):
    email: str = None
    phone_num: int = None
    session_id: UUID4
