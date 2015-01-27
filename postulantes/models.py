#coding:utf-8
from django.db import models
from django import forms
from audit_log.models.fields import CreatingUserField  
from location_field.models.plain import PlainLocationField
    

class NombrableAbstractModel(models.Model):
    nombre =   models.CharField( max_length=140, null=True, blank=True)

    def __unicode__(self):
        return self.nombre 

    class Meta:
        ordering = ('nombre',)


class Region(NombrableAbstractModel):
    class Meta:
        verbose_name = 'región'
        verbose_name_plural = 'regiones' 


class Comuna(NombrableAbstractModel):
    region = models.ForeignKey(Region, verbose_name='región') 


class Supervisor(NombrableAbstractModel):
    class Meta:
        verbose_name_plural = 'supervisores' 


class Cliente(NombrableAbstractModel):
    pass


class Medio(NombrableAbstractModel):
    total_postulantes = models.IntegerField(default=0)
    total_contratado = models.IntegerField(default=0)
     

class Instalacion(models.Model):
    nombre = models.CharField(max_length=140)
    direccion = models.CharField('dirección', max_length=140, null=True, blank=True)
    comuna = models.ForeignKey(Comuna, null=True, blank=True) 
    ubicacion = PlainLocationField(verbose_name='ubicación', based_fields=[direccion, comuna], zoom=15, null=True, blank=True)

    cliente = models.ForeignKey(Cliente, null=True, blank=True)
    supervisor = models.ForeignKey(Supervisor, null=True, blank=True)

    def __unicode__(self):
        return self.nombre 

    
    class Meta:
        verbose_name = 'Instalación'
        verbose_name_plural = 'Instalaciones'
        ordering = ('nombre',)


class Postulante(models.Model):
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        )
    ESCOLARIDAD_CHOICES = (
        ('B', 'Básica'),
        ('M', 'Media'),
        )
    ESTADO_CIVIL_CHOICES = (
        ('S', 'Soltero'),
        ('C', 'Casado'),
        ('SE', 'Separado'),
        ('V', 'Viudo'),
        )
    AFP_CHOICES = (
        ('PR', 'Provida'),
        ('HA', 'Habitat'),
        ('CA', 'Capital'),
        ('MO', 'Modelo'),
        ('CU', 'Cuprum'),
        ('PV', 'Planvital'),
        ('IP', 'IPS'),
        )
    SISTEMA_DE_SALUD_CHOICES = (
        ('F', 'FONASA'),
        ('I', 'ISAPRE'),
        )
    fecha = models.DateTimeField('ingreso', null=True, blank=True)#fecha y hora entrevista
    medio = models.CharField(max_length=140, null=True, blank=True)
    medio1 = models.ForeignKey(Medio, verbose_name='medio', null=True, blank=True, related_name='postulantes_ingresados')
    #información personal
    rut = models.CharField('RUT', max_length=20, null=True, blank=True, help_text='ej: 15774223-2')
    nombres = models.CharField(max_length=140 )
    apellidos = models.CharField(max_length=140)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)
    nacionalidad = models.CharField(max_length=140, default="Chilena", null=True, blank=True)
    sexo = models.CharField(max_length=1, null=True, blank=True, choices=SEXO_CHOICES)
    escolaridad = models.CharField(max_length=1,null=True, blank=True, choices=ESCOLARIDAD_CHOICES)
    estado_civil = models.CharField(max_length=2,null=True, blank=True, choices=ESTADO_CIVIL_CHOICES)  
    hijos = models.PositiveIntegerField(null=True, blank=True)
    jubilado = models.BooleanField(default=False)
    afp = models.CharField('AFP', max_length=2, null=True, blank=True, choices=AFP_CHOICES)
    sistema_de_salud = models.CharField(max_length=1, choices=SISTEMA_DE_SALUD_CHOICES, null=True, blank=True)
    #informacion de contacto
    domicilio = models.CharField(max_length=140, null=True, blank=True)
    comuna = models.CharField(max_length=140,null=True, blank=True)
    ubicacion = PlainLocationField(verbose_name='ubicación', based_fields=[domicilio, comuna], zoom=15, null=True, blank=True)

    telefono = models.CharField('teléfono', max_length=140, null=True, blank=True)
    telefono_emergencia = models.CharField('teléfono emergencia', max_length=140, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    #otros
    os10 = models.BooleanField('OS-10', default=False)
    vencimiento = models.DateField(null=True, blank=True)
    cargo = models.CharField(max_length=140,null=True, blank=True)
    industrial = models.BooleanField('sólo industrial', default=False)
    retail = models.BooleanField(default=False)
    ha_sido_condenado_o_detenido = models.BooleanField('anotaciones', default=False)
    motivo = models.CharField(max_length=140,null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True, help_text="indicar la razón por la cual no fue contratado")
    contratado = models.BooleanField(default=False)
    visto_bueno = models.BooleanField(default=False)
    instalacion = models.ForeignKey(Instalacion, verbose_name='instalación', null=True, blank=True)
    fecha_contratacion = models.DateField('fecha contratación', null=True, blank=True)

    reclutador = models.CharField(max_length=140, null=True, blank=True)
    creado_por = CreatingUserField(verbose_name='ingresado por')

 
    def __unicode__(self):
        return "%s %s"%(self.nombres, self.apellidos)

    class Meta:
        ordering = ('-fecha', )


class ContratadoManager(models.Manager):
    def get_queryset(self):
        return super(ContratadoManager, self).get_queryset().filter(contratado=True)

class Contratado(Postulante):
    
    objects = ContratadoManager()

    class Meta:
        proxy = True
        verbose_name = 'guardia'
        verbose_name_plural = 'guardias'
