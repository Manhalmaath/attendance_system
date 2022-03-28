from django.contrib import admin
from app.models import Session, Student


# Register your models here.

class AdminSession(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_num', 'age', 'gender', 'attend')


admin.site.register(Student, AdminSession)
admin.site.register(Session)
