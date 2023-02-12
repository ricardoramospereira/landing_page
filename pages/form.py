from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nome")
    email = forms.EmailField(label="Email")
    subject = forms.CharField(label="Assunto")
    menssage = forms.CharField(label="Mensagem", widget=forms.Textarea())
    
