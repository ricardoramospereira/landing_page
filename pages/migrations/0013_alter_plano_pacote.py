# Generated by Django 4.1.5 on 2023-01-31 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_alter_plano_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plano',
            name='pacote',
            field=models.CharField(max_length=100, verbose_name='Plano'),
        ),
    ]