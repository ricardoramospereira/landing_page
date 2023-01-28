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

    def __str__(self) -> str:
        return self.first_name