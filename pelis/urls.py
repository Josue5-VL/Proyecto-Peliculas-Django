from django.urls import path
from . import views

urlpatterns = [
    path('', views.peliculas, name='pelis'),
    path('guardarpeli/', views.guardarpeli),
    path('editarpeli/<codigo>', views.editarpeli),
    path('editarpeli/updatepeli/<codigo>', views.updatepeli),
    path('borrarpeli/<codigo>', views.borrarpeli),
    
    path('series/', views.Series, name='series'),
    path('series/guardarserie/', views.guardarserie),
    path('series/editarserie/<codigo>', views.editarserie),
    path('series/editarserie/updateserie/<codigo>', views.updateserie),
    path('series/borrarserie/<codigo>', views.borrarserie),

    path('estrenos/', views.Estrenos, name='estrenos'),
    path('estrenos/guardarestreno/', views.guardarestreno),
    path('estrenos/editarestreno/<codigo>', views.editarestreno, name='estrenos'),
    path('estrenos/editarestreno/updateestreno/<codigo>', views.updateestreno),
    path('estrenos/borrarestreno/<codigo>', views.borrarestreno),

    path('categorias/', views.categorias, name='categorias'),
    path('categorias/guardarcateg/', views.agregarcateg),
    path('categorias/agregarpelicat/', views.agregar_pelicula_a_categoria),
    path('categorias/agregarseriecat/', views.agregar_serie_a_categoria),
    path('categorias/borrarcateg/<codigo>', views.borrarcateg),
    path('categorias/imprimircateg/', views.categorias_pdf),

]
