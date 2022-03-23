from django.contrib import admin
from app.models import Session, Object


# Register your models here.

class AdminSession(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_num', 'age', 'gender')


admin.site.register(Object, AdminSession)
admin.site.register(Session)
