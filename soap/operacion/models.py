
from django.db import models
from django.db.models.signals import post_save, post_delete # para fecha actualización
from django.dispatch import receiver    # para fecha actualización
from django.utils import timezone

class Tipo_Cliente(models.Model):
    nombre_tipo_cliente = models.CharField(max_length=50, verbose_name="Tipo Cliente")
    def __str__(self):    #un método str(self) le dice a Python cómo mostrar la representación “string” de un objeto
        return self.nombre_tipo_cliente
    
class Cliente(models.Model):
    tipo_cliente = models.ForeignKey(Tipo_Cliente, on_delete=models.PROTECT, verbose_name="Tipo Cliente")  # on_delete=models.PROTECT
    rut_cliente = models.CharField(max_length=10, unique=True, null=True, blank=True, help_text='Ingrese Rut con guión, Ej: 123456789-0')
    nombre_cliente = models.CharField(max_length=50, unique=True, null=False, blank=False,verbose_name="Nombre Cliente") # blank=True => puede estar vacio en formulario
    razon_social = models.CharField(max_length=50,unique=True, null=True, blank=True, verbose_name="Razon Social")     # null=False => obligatorio en base de datos 
    direccion_cliente = models.CharField(max_length=100, null=True, blank=True, verbose_name="Direccion Cliente")
    nombre_rep_cliente = models.CharField(max_length=50, null=True, blank=True, verbose_name="Nombre Representante")
    apellido_rep_cliente = models.CharField(max_length=50, null=True, blank=True, verbose_name="Apellido Representante")
    cargo_rep_cliente = models.CharField(max_length=50, null=True, blank=True, verbose_name="Cargo")
    email_rep_cliente = models.EmailField(max_length=50, unique=True, null=True, blank=True, verbose_name="Email Cliente")
    fono_rep_cliente = models.CharField(max_length=9, null=True, blank=True, verbose_name="Fono Representante")
    def __str__(self):
        return self.nombre_cliente

class Contacto_Cliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    nombres_contacto_cliente = models.CharField(max_length=50, null=False, blank=False,verbose_name="Nombres Contacto Cliente")
    primer_apellido_contacto_cliente = models.CharField(max_length=50, null=False, blank=False,verbose_name="Primer Apellido Contacto Cliente")
    segundo_apellido_contacto_cliente = models.CharField(max_length=50, verbose_name="Segundo Apellido Contacto Cliente")
    cargo_contacto_cliente = models.CharField(max_length=50, verbose_name="Cargo Contacto Cliente")
    email_contacto_cliente = models.EmailField(max_length=50, unique=True, verbose_name="Email Contacto Cliente")
    fono_contacto_cliente = models.CharField(max_length=9, verbose_name="Fono Contacto Cliente")
    def __str__(self):
        return self.nombres_contacto_cliente + " " + self.primer_apellido_contacto_cliente
    
class Ficha_Persona(models.Model):
    rut_persona = models.CharField(max_length=10, unique=True, null=False, blank=False,help_text='Ingrese Rut con guión, Ej: 123456789-0')
    nombres_persona = models.CharField(max_length=50, null=False, blank=False, verbose_name="Nombres Persona")
    primer_apellido_persona = models.CharField(max_length=50, null=False, blank=False, verbose_name="Primer Apellido Persona")
    segundo_apellido_persona = models.CharField(max_length=50, verbose_name="Segundo Apellido Persona")
    email_persona = models.EmailField(max_length=50, unique=True, verbose_name="Email Persona")
    fono_persona = models.CharField(max_length=9, null=True, blank=True, verbose_name="Fono Persona")
    fono2_persona = models.CharField(max_length=9, null=True, blank=True, verbose_name="Fono 2 Persona")
    def __str__(self):
        return self.nombres_persona + " " + self.primer_apellido_persona
    
class Direccion_Persona(models.Model):
    ficha_persona = models.ForeignKey(Ficha_Persona, on_delete=models.PROTECT)
    direccion_persona = models.CharField(max_length=100, null=True, blank=True, verbose_name="Direccion Persona")
    def __str__(self):
        return self.direccion_persona


class Compania_Seguro(models.Model):
    nombre_compania_seguro = models.CharField(max_length=50, null=True, blank=True, verbose_name="Commpania Seguro")
    def __str__(self):
        return self.nombre_compania_seguro

class Fono_Compania(models.Model):
    compania_seguro = models.ForeignKey(Compania_Seguro, on_delete=models.PROTECT)
    fono_compania = models.CharField(max_length=9, null=True, blank=True, verbose_name="Fono Persona")
    def __str__(self):
        return self.fono_compania

class Email_Compania(models.Model):
    compania_seguro = models.ForeignKey(Compania_Seguro, on_delete=models.PROTECT)
    email_compania = models.EmailField(max_length=50, unique=True, verbose_name="Email Persona")
    def __str__(self):
        return self.email_compania


estado_contratacion = [
    [0, 'Activo'],
    [1, 'No Activo'],
    [2, 'Otro'],
]

class Empleado(models.Model):
    rut_empleado = models.CharField(max_length=10, unique=True, help_text='Ingrese Rut con guión, Ej: 123456789-0')
    nombres_empleado = models.CharField(max_length=50, verbose_name="Nombres Empleado")
    primer_apellido_empleado = models.CharField(max_length=50, verbose_name="Primer Apellido Empleado")
    segundo_apellido_empleado = models.CharField(max_length=50, verbose_name="Segundo Apellido Empleado")
    email_empresa = models.EmailField(max_length=50, unique=True, verbose_name="Email Empresa")
    cargo_empleado = models.CharField(max_length=50, verbose_name="Cargo Empleado")
    area_empleado = models.CharField(max_length=50, verbose_name="Area Empleado")
    # superior = muestre listado de esta misma tabla.
    estado_contratacion = models.IntegerField(choices = estado_contratacion)
    def __str__(self):
        return self.nombres_empleado + " " + self.primer_apellido_empleado


class Prevision(models.Model):
    nombre_prevision = models.CharField(max_length=50, verbose_name="Nombre Prevision")
    def __str__(self):
        return self.nombre_prevision
    

class Tipo_Prestador(models.Model):
    nombre_tipo_prestador = models.CharField(max_length=50, verbose_name="Tipo Prestador")
    def __str__(self):
        return self.nombre_tipo_prestador

class Prestador(models.Model):
    tipo_prestador = models.ForeignKey(Tipo_Prestador, on_delete=models.PROTECT)
    prestador = models.CharField(max_length=50, verbose_name="Prestador")
    def __str__(self):
        return self.tipo_prestador


#tipo_consulta = models.IntegerField(choices = opciones_consultas)
    #mensaje = models.TextField()
    #avisos = models.BooleanField()

 #contacto = models.ForeignKey(Contacto, on_delete=models.PROTECT, verbose_name="Contacto")  # on_delete=models.PROTECT
    #imagen = models.ImageField(upload_to="clientes", null=True)
    #pdf = models.FileField(upload_to="clientes", null=True)  #null=True para en usar la validacion en form