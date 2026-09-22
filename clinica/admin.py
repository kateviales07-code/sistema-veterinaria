from django.contrib import admin
from .models import Propietario, Mascota, ConsultaVeterinaria

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'propietario', 'peso', 'activo')
    
admin.site.register(Propietario)

admin.site.register(ConsultaVeterinaria)
