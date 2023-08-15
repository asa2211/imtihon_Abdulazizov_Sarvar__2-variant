from datetime import datetime

from django.db import models


class UstaModel(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(default='', max_length=13)
    mutaxasislig = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} \n {self.mutaxasislig}'

    class Meta:
        db_table = 'ustalar'


class OrderModel(models.Model):
    client_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    buzilish_sababi = models.TextField(default='')
    added_at = models.DateTimeField(datetime.now)
    updated_at = models.DateTimeField(auto_now=True)
    usta_id = models.ForeignKey(to=UstaModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.buzilish_sababi

    class Meta:
        db_table = 'orders'
