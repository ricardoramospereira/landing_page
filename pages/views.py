from django.shortcuts import render
from .models import Teams, Servico, Plano

# Create your views here.
def home(request):
    teams = Teams.objects.all()
    servico = Servico.objects.all()
    plano = Plano.objects.all()

    data = {
        'teams': teams,
        'servico': servico,
        'plano': plano,
    }

    return render(request, 'home.html', data)