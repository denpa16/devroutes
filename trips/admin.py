from django.contrib import admin
from .models import Trip

# Register your models here.
@admin.register(Trip)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','start_dot', 'end_dot', 'trip_shuttle','trip_date')

    """@admin.display(ordering='start__dot', description='start_dor')
    def get_start_dot(self, obj):
        return obj.trip.start_dot

    @admin.display(ordering='end__dot', description='end_dot')
    def get_end_dot(self, obj):
        return obj.trip.end_dot"""