# Register your models here.
# gestion/admin.py

from django.contrib import admin
from .models import Veterinaria, DoctorVeterinario

admin.site.register(Veterinaria)
admin.site.register(DoctorVeterinario)
