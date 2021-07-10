"""eva03 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.db import router
from django.urls import path, include
from core import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers



router = routers.DefaultRouter()
router.register('Rams', views.RamsViewset)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name="inicio"),
    path('acerca/', views.acerca, name="acerca"),
    path('contacto/', views.contacto, name="contacto"),
    path('juego/', views.juego, name="juego"),
    path('enfriamientoCPU/', views.EnfriamientoCPU, name="EnfriamientoCPU"),
    path('fuentesDePoder/', views.fuentesDePoder, name="fuentesDePoder"),
    path('Gabinetes/', views.Gabinetes, name="Gabinetes"),
    path('PlacaMadre/', views.PlacaMadre, name="PlacaMadre"),
    path('Procesadores/', views.Procesadores, name="Procesadores"),
    path('SistemasAlmacenamiento/', views.SistemasAlmacenamiento, name="SistemasAlmacenamiento"),
    path('TargetasGraficas/', views.TargetasGraficas, name="TargetasGraficas"),
    path('TarjetasRam/', views.TarjetasRam, name="TarjetasRam"),
    

    path('agregarRams/', views.agregarRams, name="agregarRams"),
    path('listRam/',views.listRam, name="listRam" ),
    path('modiRams/<id>/', views.modiRams, name="modiRams"),
    path('eliminar_rams/<id>/', views.eliminar_rams, name="eliminar_rams"),

    path('agregarJuego/', views.agregarJuego, name="agregarJuego"),
    path('listJuego/', views.listJuego, name="listJuego"),
    path('modiJuego/<id>/', views.modiJuego, name="modiJuego"),
    path('eliminar_Juego/<id>/', views.eliminar_Juego, name='eliminar_Juego'),

    path('agregarGabinete/', views.agregarGabinete, name="agregarGabinete"),
    path('listGabinete/', views.listGabinete, name="listGabinete"),
    path('modiGabinete/<id>/', views.modiGabinete, name="modiGabinete"),
    path('eliminar_gabinete/<id>/', views.eliminar_gabinete, name="eliminar_gabinete"),

    path('agregarProce/', views.agregarProce, name="agregarProce"),
    path('listarProce/', views.listarProce, name="listarProce"),
    path('modificarProce/<id>/', views.modificarProce, name="modificarProce"),
    path('eliminar_Proce/<id>', views.eliminar_Proce, name= "eliminar_Proce"),

    path('agregarGPU/', views.agregarGPU, name= "agregarGPU"),
    path('listarGPU/', views.listarGPU, name="listarGPU" ),
    path('modificarGpu/<id>/', views.modificarGpu, name="modificarGpu"),
    path('eliminar_Gpu/<id>/,', views.eliminar_Gpu, name="eliminar_Gpu"),

    path('api/', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    path ('registro/', views.registro, name="registro")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
