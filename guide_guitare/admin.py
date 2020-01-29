from django.contrib import admin
from .models import GuitareModel

class GuitareAdmin(admin.ModelAdmin):
    list_display = ("nom_guitare", "type_guitare", "prix_guitare")

admin.site.register(GuitareModel, GuitareAdmin)