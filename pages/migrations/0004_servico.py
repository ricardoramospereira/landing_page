# Generated by Django 4.1.5 on 2023-01-30 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_teams_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
