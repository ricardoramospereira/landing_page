# Generated by Django 4.1.5 on 2023-01-30 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_servico_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plano', models.CharField(choices=[('1', 'Plano Free'), ('2', 'Plano Negócios'), ('3', 'Plano Desenvolvedor')], default='1', max_length=2)),
            ],
        ),
    ]