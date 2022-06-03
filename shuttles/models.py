from statistics import mode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Shuttle(models.Model):
    driver = models.ForeignKey(User, related_name='driver', on_delete=models.CASCADE)
    shuttle_licence_plate = models.CharField('Номер автомобиля', max_length=20, blank=True, null=False)
    shuttle_color = models.CharField('Цвет автомобиля', max_length=50, blank=True, null=False)
    shuttle_brand = models.CharField('Марка автомобиля', max_length=50, blank=True, null=False)
    shuttle_model = models.CharField('Модель автомобиля', max_length=50, blank=True, null=False)

    def __str__(self):
        return self.shuttle_brand + ' ' + self.shuttle_model + ' ' + self.shuttle_licence_plate