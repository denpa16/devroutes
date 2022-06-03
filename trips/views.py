from hashlib import new
from django.shortcuts import render
from .models import Trip
from dots.models import Dot
# Create your views here.
def trip(request, id):
    return render(request, 'trips/trip.html', {'trip_id': id,})

def trip_create(request):
    if request.method == 'POST':
        start_dot = Dot.objects.get(dot_title=request.POST.get('start_point'))
        end_dot = Dot.objects.get(dot_title=request.POST.get('end_point'))
        new_trip = Trip(start_dot = start_dot, end_dot = end_dot)
        new_trip.trip_shuttle = None
        new_trip.save()
        print(new_trip)
    return render(request, 'trips/trip.html', {'trip_id': id,})