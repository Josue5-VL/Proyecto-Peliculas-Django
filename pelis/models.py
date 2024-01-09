from django.db import models

class Pelicula(models.Model):
    codigo = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to="pelis/static/media", null=True)
    titulo = models.CharField(max_length=100)
    sinopsis = models.TextField()

class Serie(models.Model):
    codigo = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to="pelis/static/media", null=True)
    titulo = models.CharField(max_length=100)
    sinopsis = models.TextField()

class Categoria(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    peliculas = models.ManyToManyField(Pelicula)
    series = models.ManyToManyField(Serie)

class Estreno(models.Model):
    codigo = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="pelis/static/media", null=True)
    tipo = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    sinopsis = models.TextField()
