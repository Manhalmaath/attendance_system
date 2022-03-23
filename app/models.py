from django.db import models
from django.contrib import admin


class Session(models.Model):
    name = models.CharField('name', max_length=100)
    date = models.DateField('date')
    presented_by = models.CharField('presented_by', max_length=100)
    file = models.FileField('file', upload_to='sessions_file/')

    def __str__(self):
        return f"{self.name}"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        print(f"{self.name} has been saved")
        self.file = None
        super().save()
