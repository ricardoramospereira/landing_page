from django.shortcuts import render
from .models import Teams

# Create your views here.
def home(request):
    teams = Teams.objects.all()

    data = {
        'teams': teams,
    }

    return render(request, 'home.html', data)