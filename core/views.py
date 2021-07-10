from django.core import paginator
from django.http import request
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import html
from .models import GPU, Juegos, Rams, Gabinete, Procesador
from .forms import RamsForm, JuegosForm, GabineteForm, ProcesadorForm, GpuForm, CustomUserCreationForm
from rest_framework import viewsets
from .serializers import RamsSerializer
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required



# Create your views here.


# API REST
class RamsViewset(viewsets.ModelViewSet):
    queryset = Rams.objects.all()
    serializer_class = RamsSerializer



def inicio(request):
    return render(request,"core/inicio.html")

def inicio(request):
    return render(request,"core/inicio.html")

def acerca(request):
    return render(request,"core/acerca.html")

def contacto(request): 
    return render(request,"core/contacto.html")

def juego(request):
    juego = Juegos.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(juego, 4)
        juego = paginator.page(page)
    except:
        raise Http404   

    data = {
        'entity': juego,
        'paginator': paginator
    }
    return render(request,"core/juego.html", data)

def EnfriamientoCPU(request): 
    return render(request,"core/EnfriamientoCPU.html")

def fuentesDePoder(request): 
    return render(request,"core/fuentesDePoder.html")

def Gabinetes(request):
    gabinete = Gabinete.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(gabinete, 4)
        gabinete = paginator.page(page)
    except:
        raise Http404   

    data = {
        'entity': gabinete,
        'paginator': paginator
    }
    return render(request,"core/Gabinetes.html", data)

def PlacaMadre(request): 
    return render(request,"core/PlacaMadre.html")

def Procesadores(request): 
    proces = Procesador.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(proces, 4)
        proces = paginator.page(page)
    except:
        raise Http404   

    data = {
        'entity': proces,
        'paginator': paginator
    }
    return render(request,"core/Procesadores.html", data)

def SistemasAlmacenamiento (request):
    return render(request,"core/SistemasAlmacenamiento.html")

def TargetasGraficas (request):
    gpu = GPU.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(gpu, 4)
        gpu = paginator.page(page)
    except:
        raise Http404   

    data = {
        'entity': gpu,
        'paginator': paginator
    }
    return render(request,"core/TargetasGraficas.html", data)

def TarjetasRam (request):
    rams = Rams.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(rams, 4)
        rams = paginator.page(page)
    except:
        raise Http404   

    data = {
        'entity': rams,
        'paginator': paginator
    }
    return render(request,"core/TarjetasRam.html", data)


#CRUD Tarjetas Rams
@permission_required('core.agregarRams')
def agregarRams(request):
    data = {
        'form': RamsForm()
    }
    if request.method == 'POST':
        formulario = RamsForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Tarjetas Rams agregado Correctamente")
        else:
            data["form"] = formulario    
    return render(request, "core/crud/rams/add-ram.html", data)
@permission_required('core.view_rams')
def listRam(request):
    rams = Rams.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(rams, 2)
        rams = paginator.page(page)
    except:
        raise Http404   

    data = {
        'entity': rams,
        'paginator': paginator
    }
    return render(request, "core/crud/rams/listRam.html", data)
@permission_required('core.change_rams')
def modiRams(request, id):
    rams = get_object_or_404(Rams, id=id)

    data={
        'form': RamsForm(instance=rams)
    }
    if request.method == 'POST':
        formulario = RamsForm(data=request.POST, instance=rams, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listRam")
        data["form"] = formulario    
    return render(request, "core/crud/rams/modi-ram.html", data)
@permission_required('core.delete_rams')
def eliminar_rams (request, id):
    rams = get_object_or_404(Rams, id=id)
    rams.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listRam")  

@permission_required('core.agregarJuego')
def agregarJuego(request):
    data = {
        'form': JuegosForm()
    }
    if request.method == 'POST':
        formulario = JuegosForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Juego agregado Correctamente")
        else:
            data["form"] = formulario 
    return render(request,"core/crud/juegos/add-juego.html", data)

@permission_required('core.change_juego')    
def modiJuego (request, id):
    juego = get_object_or_404(Juegos, id=id)

    data ={
        'form': JuegosForm(instance=juego)
    }
    if request.method == 'POST':
        formulario = JuegosForm(data=request.POST,  instance=juego, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listJuego")
        data["form"] = formulario 
    return render(request,"core/crud/juegos/modi-juego.html", data)
@permission_required('core.view_juego')    
def listJuego(request):
    juego = Juegos.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(juego, 2)
        juego = paginator.page(page)
    except:
        raise Http404   

    data = {
        'entity': juego,
        'paginator': paginator
    }
    return render(request,"core/crud/juegos/listJuego.html",data)
@permission_required('core.delete_juego')    
def eliminar_Juego(request, id):
    juego = get_object_or_404(Juegos, id=id)
    juego.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listJuego")   

# CRUD Gabinetes
@permission_required('core.agregarGabinete')
def agregarGabinete(request):
    data ={
        'form': GabineteForm()
    }
    if request.method=='POST':
        formulario = GabineteForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Gabinete agregado Correctamente")
        else:
            data["form"]= formulario    
    return render(request, "core/crud/gabinete/add-gabinete.html", data)
@permission_required('core.view_gabinete ')
def listGabinete(request):
    gabinete = Gabinete.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(gabinete, 2)
        gabinete = paginator.page(page)
    except:
        raise Http404   

    data = {
        'entity': gabinete,
        'paginator': paginator
    }
    return render(request,"core/crud/gabinete/listGabinete.html",data)
@permission_required('core.change_gabinete ')
def modiGabinete(request, id):

    gabinetes = get_object_or_404(Gabinete, id=id)

    data = {
        'form': GabineteForm(instance=gabinetes)
    }
    if request.method == 'POST':
        formulario = GabineteForm(data=request.POST, instance=gabinetes, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listGabinete")
        data["form"] = formulario    
    return render(request,"core/crud/gabinete/modi-gabi.html", data)
@permission_required('core.delete_gabinete ')
def eliminar_gabinete(request, id):
    gabinete = get_object_or_404(Gabinete, id=id)
    gabinete.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listGabinete")

#CRUD Procesadores
@permission_required('core.agregarProce') 
def agregarProce(request):
    data={
        'form': ProcesadorForm()
    }

    if request.method == 'POST':
        formulario = ProcesadorForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Procesador agregado Correctamente")
        else:
            data["form"]= formulario    
    return render(request, 'core/crud/proces/add-proce.html', data)
@permission_required('core.view_proces ')
def listarProce (request):
    proces = Procesador.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(proces, 2)
        proces = paginator.page(page)
    except:
        raise Http404   

    data = {
        'entity': proces,
        'paginator': paginator
    }
    return render(request,"core/crud/proces/listProce.html", data)
@permission_required('core.change_proces ')
def modificarProce(request, id):
    proces = get_object_or_404(Procesador, id=id)

    data={
        'form': ProcesadorForm(instance=proces)
    }
    if request.method == 'POST':
        formulario = ProcesadorForm(data=request.POST, instance=proces, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listarProce")
        data["form"] = formulario    

    return render(request, 'core/crud/proces/modi-proce.html',data)
@permission_required('core.delete_proces ')
def eliminar_Proce(request, id):
    proces = get_object_or_404(Procesador, id=id)
    proces.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listarProce")

# CRUD  Tarjetas Graficas
@permission_required('core.agregarGPU')
def agregarGPU(request):
    data={
        'form': GpuForm()
    }
    if request.method =='POST':
        formulario = GpuForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Tarjetas Grafica agregado Correctamente")
        else:
            data["form"] = formulario   
    return render(request, 'core/crud/Graficos/add-graficos.html', data)
@permission_required('core.view_gpu ')
def listarGPU(request):
    gpu = GPU.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(gpu, 2)
        gpu = paginator.page(page)
    except:
        raise Http404   

    data = {
        'entity': gpu,
        'paginator': paginator
    }
    return render(request, "core/crud/Graficos/listGraficos.html", data)
@permission_required('core.change_gpu ')
def modificarGpu(request, id):
    gpu= get_object_or_404(GPU, id= id)

    data={
        'form': GpuForm(instance=gpu)
    }
    if request.method == 'POST':
        formulario = GpuForm(data=request.POST, instance=gpu, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listarGPU")
        data["form"] = formulario 

    return render(request, 'core/crud/Graficos/modi-graficos.html', data)
@permission_required('core.delete_gpu ')
def eliminar_Gpu(request, id):
    gpu = get_object_or_404(GPU, id=id)
    gpu.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listarGPU")                


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente.")
            # ir al inicio
            return redirect(to='inicio')
        data["form"] = formulario    
    return render(request, 'registration/registro.html', data)
