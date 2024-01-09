from django.shortcuts import render, redirect

from .models import *

# Create your views here.

def peliculas(request):
    peli=Pelicula.objects.all()
    return render(request, 'peliculas.html', {"peli":peli})

def Series(request):
    tv=Serie.objects.all()
    return render(request, 'series.html', {"tv":tv})

def Estrenos(request):
    estreno=Estreno.objects.all()
    return render(request, 'estrenos.html', {"estreno":estreno})


#vistas peliculas

def guardarpeli(request):
    imagen=request.POST['cover']
    titulo=request.POST['titulo']
    sinopsis=request.POST['sinopsis']

    peli=Pelicula.objects.create(titulo=titulo, sinopsis=sinopsis, imagen=imagen)
    return redirect('pelis')

def editarpeli(request, codigo):
    peli=Pelicula.objects.get(codigo=codigo)
    return render(request, 'editarpeli.html', {"peli":peli})

def updatepeli(request, codigo):
    peli = Pelicula.objects.get(codigo=codigo)
    imagen=request.POST['cover']
    titulo=request.POST['titulo']
    sinopsis=request.POST['sinopsis']

    peli.titulo=titulo
    peli.imagen=imagen
    peli.sinopsis=sinopsis
    peli.save()
    return redirect('pelis')

def borrarpeli(request, codigo):
    peli=Pelicula.objects.get(codigo=codigo)
    peli.delete()
    return redirect('pelis')

#vistas series

def guardarserie(request):
    imagen=request.POST['cover']
    titulo=request.POST['titulo']
    sinopsis=request.POST['sinopsis']

    tv=Serie.objects.create(titulo=titulo, sinopsis=sinopsis, imagen=imagen)
    return redirect('series')

def editarserie(request, codigo):
    show=Serie.objects.get(codigo=codigo)
    return render(request, 'editarserie.html', {"show":show})

def updateserie(request, codigo):
    show = Serie.objects.get(codigo=codigo)
    imagen=request.POST['cover']
    titulo=request.POST['titulo']
    sinopsis=request.POST['sinopsis']

    show.titulo=titulo
    show.imagen=imagen
    show.sinopsis=sinopsis
    show.save()
    return redirect('series')

def borrarserie(request, codigo):
    show=Serie.objects.get(codigo=codigo)
    show.delete()
    return redirect('series')

# vistas estrenos

def guardarestreno(request):
    imagen=request.POST['cover']
    titulo=request.POST['titulo']
    tipo=request.POST['tipo']
    fecha=request.POST['fecha']
    sinopsis=request.POST['sinopsis']

    estreno=Estreno.objects.create(titulo=titulo, sinopsis=sinopsis, imagen=imagen, tipo=tipo, fecha=fecha)
    return redirect('estrenos')

def editarestreno(request, codigo):
    estreno=Estreno.objects.get(codigo=codigo)
    return render(request, 'editarestreno.html', {"estreno":estreno})

def updateestreno(request, codigo):
    estreno = Estreno.objects.get(codigo=codigo)
    imagen=request.POST['cover']
    titulo=request.POST['titulo']
    tipo=request.POST['tipo']
    fecha=request.POST['fecha']
    sinopsis=request.POST['sinopsis']

    estreno.titulo=titulo
    estreno.imagen=imagen
    estreno.tipo=tipo
    estreno.sinopsis=sinopsis
    estreno.save()
    return redirect('estrenos')

def borrarestreno(request, codigo):
    estreno=Estreno.objects.get(codigo=codigo)
    estreno.delete()
    return redirect('estrenos')

#vistas categoria

def categorias(request):
    peliculas = Pelicula.objects.all()
    series = Serie.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'categoria.html', {'peliculas': peliculas, 'series':series, 'categorias': categorias})

def agregarcateg(request):
    nombre=request.POST['nombre']
    nueva_categoria = Categoria.objects.create(nombre=nombre)
    return redirect('categorias')

def agregar_pelicula_a_categoria(request):
    if request.method == 'POST':
        pelicula_id = request.POST.get('pelicula')
        categoria_id = request.POST.get('categoria')

        try:
            selected_pelicula = Pelicula.objects.get(codigo=pelicula_id)
            selected_categoria = Categoria.objects.get(codigo=categoria_id)
            selected_categoria.peliculas.add(selected_pelicula)
            return redirect('categorias')
        except (Pelicula.DoesNotExist, Categoria.DoesNotExist):
            # Maneja el caso si la película o la categoría seleccionada no existe
            pass

    peliculas = Pelicula.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'categoria.html', {'peliculas': peliculas, 'categorias': categorias})

def agregar_serie_a_categoria(request):
    if request.method == 'POST':
        series_id = request.POST.get('serie')
        categoria_id = request.POST.get('categoria')

        try:
            selected_series = Serie.objects.get(codigo=series_id)
            selected_categoria = Categoria.objects.get(codigo=categoria_id)
            selected_categoria.series.add(selected_series)
            return redirect('categorias')
        except (Serie.DoesNotExist, Categoria.DoesNotExist):
            pass

    series = Serie.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'categoria.html', {'series': series, 'categorias': categorias})


def borrarcateg(request, codigo):
    categoria=Categoria.objects.get(codigo=codigo)
    categoria.delete()
    return redirect('categorias')

from django.shortcuts import render
from django.http import HttpResponse
from xhtml2pdf import pisa
from io import BytesIO
from .models import Categoria


def categorias_pdf(request):
    categorias = Categoria.objects.all()
    context = {'categorias': categorias}

    template = render(request, 'imprimir.html', context)

    pdf = BytesIO()
    pisa.CreatePDF(template.content, dest=pdf)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="categorias.pdf"'
    response.write(pdf.getvalue())

    return response
