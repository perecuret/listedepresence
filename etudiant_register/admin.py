from django.contrib import admin

# Register your models here.

from .models import Etudiant, Evenement

admin.site.register(Etudiant)
admin.site.register(Evenement)