# Generated by Django 4.1.5 on 2023-01-30 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_servico'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='descriptions',
            field=models.TextField(default=True, max_length=200, verbose_name='descrição'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Serviço'),
        ),
    ]