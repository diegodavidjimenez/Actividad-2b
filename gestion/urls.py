
# gestion/urls.py

from django.urls import path
from .views import listar_veterinarias, crear_veterinaria, editar_veterinaria, listar_doctores, crear_doctor, editar_doctor

urlpatterns = [
    path('veterinarias/', listar_veterinarias, name='listar_veterinarias'),
    path('veterinarias/crear/', crear_veterinaria, name='crear_veterinaria'),
    path('veterinarias/editar/<int:id>/', editar_veterinaria, name='editar_veterinaria'),
    path('doctores/', listar_doctores, name='listar_doctores'),
    path('doctores/crear/', crear_doctor, name='crear_doctor'),
    path('doctores/editar/<int:id>/', editar_doctor, name='editar_doctor'),
]
