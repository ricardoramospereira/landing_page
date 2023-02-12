from django.shortcuts import render
from .models import Teams, Servico, Plano
from .form import ContactForm
from django.contrib import messages

# Create your views here.
def home(request):
    teams = Teams.objects.all()
    servico = Servico.objects.all()
    plano = Plano.objects.all()
    #form = ContactForm(request.Post or None)

    '''if str(request.method) == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            menssage = form.cleaned_data['message']

            print('Mensagem  enviada')
            print(f'Nome: {name}')
            print(f'Email: {email}')
            print(f'Assunto: {subject}')
            print(f'Mensagem: {menssage}')

            messages.success(request, 'Enviado com sucesso')
            form = ContactForm()
        else:
            messages.error(request, 'Erro ao enviar mensagem')'''


    data = {
        'teams': teams,
        'servico': servico,
        'plano': plano,
        #'form': form,
    }

    return render(request, 'home.html', data)