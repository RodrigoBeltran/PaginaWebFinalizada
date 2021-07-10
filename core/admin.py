from django.contrib import admin
from .models import Distribuidor, GPU, Juegos, Rams, Gabinete, Procesador

# Register your models here.
 
admin.site.register(Distribuidor)
admin.site.register(Rams)
admin.site.register(Juegos)
admin.site.register(Gabinete)
admin.site.register(Procesador)
admin.site.register(GPU)

