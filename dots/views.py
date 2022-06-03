from hashlib import new
from django.shortcuts import render
from .forms import FormForm
from .models import Dot

# Create your views here.
def index(request):
    start_list = Dot.objects.all()
    end_list = Dot.objects.all()
    form = FormForm(start_list=start_list, end_list=end_list)
    return render(request, 'dots/index.html', {'form': form,})
