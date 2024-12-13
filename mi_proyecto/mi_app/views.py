from django.shortcuts import render

# Views

from django.shortcuts import render, redirect
from .models import Libro, Autor, Editorial
from .forms import LibroForm, AutorForm, EditorialForm

# Vista para insertar libros, autores y editoriales
def insertar(request):
    if request.method == 'POST':
        if 'libro' in request.POST:
            libro_form = LibroForm(request.POST)
            if libro_form.is_valid():
                libro_form.save()
                return redirect('insertar')
        elif 'autor' in request.POST:
            autor_form = AutorForm(request.POST)
            if autor_form.is_valid():
                autor_form.save()
                return redirect('insertar')
        elif 'editorial' in request.POST:
            editorial_form = EditorialForm(request.POST)
            if editorial_form.is_valid():
                editorial_form.save()
                return redirect('insertar')
    else:
        libro_form = LibroForm()
        autor_form = AutorForm()
        editorial_form = EditorialForm()
    
    return render(request, 'insertar.html', {
        'libro_form': libro_form,
        'autor_form': autor_form,
        'editorial_form': editorial_form
    })

# Vista para buscar libros
def buscar(request):
    libros = None
    if request.method == 'GET' and 'titulo' in request.GET:
        titulo = request.GET['titulo']
        libros = Libro.objects.filter(titulo__icontains=titulo)
    
    return render(request, 'buscar.html', {'libros': libros})

