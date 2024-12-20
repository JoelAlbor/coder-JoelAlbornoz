from django.db import models

# Modelos

from django.db import models

# Modelo de Autor:
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    biografia = models.TextField(null=True, blank=True)  # Agregar biografía del autor (opcional)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

# Modelo de Editorial:
class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

# Modelo de Libro:
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)  # Agregar campo ISBN (identificador del librto)
    descripcion = models.TextField(null=True, blank=True)  # Agregar un campo para la descripción del libro

    def __str__(self):
        return self.titulo

