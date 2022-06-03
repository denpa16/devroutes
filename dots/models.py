from statistics import mode
from django.db import models

# Create your models here.
class Dot(models.Model):
    dot_title = models.CharField('Название точки', max_length=200, blank=True ,null=True)

    def __str__(self):
        return self.dot_title
