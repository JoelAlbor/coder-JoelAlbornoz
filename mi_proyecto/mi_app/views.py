from django.shortcuts import render

# Views

from django.shortcuts import render, redirect
from .models import Libro, Autor, Editorial
from .forms import LibroForm, AutorForm, EditorialForm

# Vista para insertar libros, autores y editoriales:

from django.shortcuts import render, redirect
from .models import Libro, Autor, Editorial
from .forms import LibroForm, AutorForm, EditorialForm

def insertar(request):
    if request.method == 'POST':
        # Procesar los formularios dependiendo del botón presionado
        if 'libro' in request.POST:
            libro_form = LibroForm(request.POST)
            if libro_form.is_valid():
                libro_form.save()
                return redirect('insertar')  # Redirigir para que se muestre el formulario limpio
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
        # Crear formularios vacíos para cuando no se ha hecho un POST
        libro_form = LibroForm()
        autor_form = AutorForm()
        editorial_form = EditorialForm()
    
    return render(request, 'insertar.html', {
        'libro_form': libro_form,
        'autor_form': autor_form,
        'editorial_form': editorial_form
    })


# Vista para buscar libros:


from django.shortcuts import render
from .models import Libro

def buscar(request):
    libros = None
    mensaje = ""
    if request.method == 'GET' and 'titulo' in request.GET:
        titulo = request.GET['titulo']
        libros = Libro.objects.filter(titulo__icontains=titulo)
        
        if not libros:
            mensaje = "No se encontraron libros con ese título."
    
    return render(request, 'buscar.html', {'libros': libros, 'mensaje': mensaje})


# Vista para listar libros 

def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'listar_libros.html', {'libros': libros})


# Vista para listar autores:

def listar_autores(request):
    autores = Autor.objects.all()
    return render(request, 'listar_autores.html', {'autores': autores})


# Vista para listar editoriales:

def listar_editoriales(request):
    editoriales = Editorial.objects.all()
    return render(request, 'listar_editoriales.html', {'editoriales': editoriales})





