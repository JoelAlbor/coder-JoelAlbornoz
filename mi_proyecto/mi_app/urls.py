from django.urls import path
from . import views

urlpatterns = [
    path('insertar/', views.insertar, name='insertar'),
    path('buscar/', views.buscar, name='buscar'),
    path('listar_libros/', views.listar_libros, name='listar_libros'),
    path('listar_autores/', views.listar_autores, name='listar_autores'),
    path('listar_editoriales/', views.listar_editoriales, name='listar_editoriales'),
]
