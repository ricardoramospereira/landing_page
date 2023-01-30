from django.shortcuts import render
from .models import Teams, Servico

# Create your views here.
def home(request):
    teams = Teams.objects.all()
    servico = Servico.objects.all()

    data = {
        'teams': teams,
        'servico': servico,
    }

    return render(request, 'home.html', data)