from django.contrib import admin
from .models import Teams

# Register your models here.
#@admin.site.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name", "designation",)

admin.site.register(Teams)