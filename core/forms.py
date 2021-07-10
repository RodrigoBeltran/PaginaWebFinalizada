from django import forms
from django.forms import fields
from .models import Gabinete, Rams, Juegos, Procesador, GPU
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RamsForm(forms.ModelForm):

    class Meta:
        model = Rams
        fields ='__all__'

class JuegosForm(forms.ModelForm):

    
    class Meta:
        model = Juegos
        fields = '__all__'    
class GabineteForm(forms.ModelForm):

    
    class Meta:
        model = Gabinete
        fields = '__all__'   

class ProcesadorForm(forms.ModelForm):
    class Meta:
        model= Procesador
        fields = '__all__'

class GpuForm(forms.ModelForm):

    class Meta:
        model= GPU
        fields= '__all__'            

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']