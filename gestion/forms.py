# gestion/forms.py

from django import forms
from .models import Veterinaria, DoctorVeterinario

class VeterinariaForm(forms.ModelForm):
    class Meta:
        model = Veterinaria
        fields = '__all__'

class DoctorVeterinarioForm(forms.ModelForm):
    class Meta:
        model = DoctorVeterinario
        fields = '__all__'
