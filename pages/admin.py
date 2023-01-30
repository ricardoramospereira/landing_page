from django.contrib import admin
from .models import Teams, Servico

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name", "designation",)


class ServicoAdmin(admin.ModelAdmin):
    list_display = ("name", "descriptions",)


admin.site.register(Teams, TeamAdmin)
admin.site.register(Servico, ServicoAdmin)