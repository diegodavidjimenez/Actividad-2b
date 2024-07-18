# gestion/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Veterinaria, DoctorVeterinario
from .forms import VeterinariaForm, DoctorVeterinarioForm

def listar_veterinarias(request):
    veterinarias = Veterinaria.objects.all()
    return render(request, 'gestion/listar_veterinarias.html', {'veterinarias': veterinarias})

def crear_veterinaria(request):
    if request.method == 'POST':
        form = VeterinariaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_veterinarias')
    else:
        form = VeterinariaForm()
    return render(request, 'gestion/form_veterinaria.html', {'form': form})

def editar_veterinaria(request, id):
    veterinaria = get_object_or_404(Veterinaria, id=id)
    if request.method == 'POST':
        form = VeterinariaForm(request.POST, instance=veterinaria)
        if form.is_valid():
            form.save()
            return redirect('listar_veterinarias')
    else:
        form = VeterinariaForm(instance=veterinaria)
    return render(request, 'gestion/form_veterinaria.html', {'form': form})

def listar_doctores(request):
    doctores = DoctorVeterinario.objects.all()
    return render(request, 'gestion/listar_doctores.html', {'doctores': doctores})

def crear_doctor(request):
    if request.method == 'POST':
        form = DoctorVeterinarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_doctores')
    else:
        form = DoctorVeterinarioForm()
    return render(request, 'gestion/form_doctor.html', {'form': form})

def editar_doctor(request, id):
    doctor = get_object_or_404(DoctorVeterinario, id=id)
    if request.method == 'POST':
        form = DoctorVeterinarioForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('listar_doctores')
    else:
        form = DoctorVeterinarioForm(instance=doctor)
    return render(request, 'gestion/form_doctor.html', {'form': form})
