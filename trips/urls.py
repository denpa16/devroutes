from django.urls import path
from . import views

app_name = 'trips'
urlpatterns = [
    path('trip/<int:id>', views.trip, name='trip'),
    path('trip/create', views.trip_create, name='trip_create'),
]