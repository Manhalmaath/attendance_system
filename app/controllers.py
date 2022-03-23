from ninja import Router
from typing import List
from app.models import Session

from app.schemas import SessionOut

app_controller = Router(tags=['auth'])


@app_controller.get('get_all_session', response=List[SessionOut])
def get_all_session():
    session = Session.objects.all()
    return session


@app_controller.get('get_session', response=SessionOut)
def get_all_sessions(request):
    return Session.objects.all()
