from django.db import models
import pandas as pd
import uuid


class Entity(models.Model):
    class Meta:
        abstract = True

    objects = models.Manager()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Object(Entity):
    name = models.CharField('name', max_length=100)
    email = models.EmailField('email', max_length=100, default=None, blank=True, null=True)
    phone_num = models.CharField('phone_num', max_length=100, )
    age = models.IntegerField('age')
    gender = models.CharField('gender', max_length=10)
    attend = models.BooleanField(default=False)
    session = models.ForeignKey('Session', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Session(Entity):
    name = models.CharField('name', max_length=100)
    date = models.DateField('date')
    presented_by = models.CharField('presented_by', max_length=100)
    file = models.FileField('file')

    def __str__(self):
        return f"{self.name}"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        print("stated")
        data = pd.read_excel(self.file, sheet_name='Sheet 1')
        self.file = None
        super().save()
        for i in range(0, len(data.index)):
            name = str(data.loc[i, 'First']) + ' ' + '' if str(data.loc[i, 'Second']) == 'nan' else str(
                data.loc[i, 'Second']) + ' ' + '' if str(data.loc[i, 'Third']) == 'nan' else str(
                data.loc[i, 'Third'])
            email = data.loc[i, 'Email']
            if str(email) == 'nan':
                email = None
            else:
                email = email
            print(email)
            gender = data.loc[i, 'Gender']
            age = data.loc[i, 'Age']
            phone_num = data.loc[i, 'Phone']
            Object.objects.create(
                name=name,
                email=email,
                gender=gender,
                age=age,
                phone_num=phone_num,
                session=self,
                attend=False
            )
            print(f'{name}')
            print(f"{i} added")
