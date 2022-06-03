from statistics import mode
from django.db import models
from dots.models import Dot
from shuttles.models import Shuttle
# Create your models here.
class Trip(models.Model):
    start_dot = models.ForeignKey(Dot, related_name='start_dot', on_delete=models.CASCADE)
    end_dot = models.ForeignKey(Dot, related_name='end_dot', on_delete=models.CASCADE)
    trip_shuttle = models.ForeignKey(Shuttle, related_name='Шаттл', on_delete=models.CASCADE, blank=True, null=True)
    trip_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.start_dot) + ' - ' + str(self.end_dot)