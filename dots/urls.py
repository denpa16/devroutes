from django.urls import path
from . import views

app_name = 'dots'
urlpatterns = [
    path('', views.index, name='index'),
]