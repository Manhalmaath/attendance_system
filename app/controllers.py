import datetime

from ninja import Router
from typing import List
from app.models import Session, Student

from app.schemas import SessionOut, MessageOut, AttendanceIn

app_controller = Router(tags=['app'])


@app_controller.get('get_today_session', response=List[SessionOut])
def get_today_session(request):
    return Session.objects.filter(date=datetime.date.today())


@app_controller.post('Check_attendance', response={200: MessageOut, 400: MessageOut})
def check_attendance(request, payload: AttendanceIn):
    students = Student.objects.filter(session_id=payload.session_id, attend=False)
    for stu in students:
        if stu.email == payload.email or stu.phone_num == payload.phone_num:
            stu.attend = True
            stu.save()
            return 200, {"detail": 'Attend registered successfully'}
    return 400, {"detail": 'your not registered or your information is wrong'}
