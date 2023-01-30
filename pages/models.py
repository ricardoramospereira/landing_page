from django.db import models

# Create your models here.
class Teams(models.Model):
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=50)
    designation = models.CharField('Cargo', max_length=50)
    photo = models.ImageField('Imagem', upload_to='photos/%d/%m/%Y/')
    facebook_link = models.URLField('Facebook', max_length=100)
    twitter_link = models.URLField('Twitter', max_length=100)
    instagran_link = models.URLField('Instagram', max_length=100)
    linkedin_link = models.URLField('Lindedin', max_length=100)
    create_date = models.DateTimeField('Data de Criação', auto_now_add=True)

    class Meta: 
        verbose_name = "Team"
        verbose_name_plural = "Teams"

    def __str__(self) -> str:
        return self.first_name

class Servico(models.Model):
    name = models.CharField("Serviço", max_length=100)
    descriptions = models.CharField("descrição", max_length=200)

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

    def __str__(self) -> str:
        return self.name

'''class Servico(models.Model):
    name_servico = models.CharField("Serviços", max_length=100)
    descriptions = models.TextField("Descrição", max_length=255)

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

    def __str__(self) -> str:
        return self.name_servico'''

