# Generated by Django 4.1.5 on 2023-01-31 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_plano_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plano',
            name='preco',
            field=models.IntegerField(default=0, verbose_name='Preço'),
        ),
    ]