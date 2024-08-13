from django.contrib import admin
from .models import Tipo_Cliente, Cliente, Contacto_Cliente, Ficha_Persona
from .models import Direccion_Persona, Compania_Seguro, Fono_Compania, Email_Compania
from .models import Empleado, Prevision,Tipo_Prestador, Prestador

admin.site.register(Tipo_Cliente)
admin.site.register(Cliente)
admin.site.register(Contacto_Cliente)
admin.site.register(Ficha_Persona)
admin.site.register(Direccion_Persona)
admin.site.register(Compania_Seguro)
admin.site.register(Fono_Compania)
admin.site.register(Email_Compania)
admin.site.register(Empleado)
admin.site.register(Prevision)
admin.site.register(Tipo_Prestador)
admin.site.register(Prestador)