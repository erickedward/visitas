from django.db import models
from datetime import datetime
from django.utils import timezone

class Departamento(models.Model):
	nombre_dpto = models.CharField(max_length=70,verbose_name='Nombre del departamento')
	piso = models.CharField(max_length=5)
	descripcion = models.CharField(max_length = 40)

	def __str__(self):
		return '%s'%(self.nombre_dpto)

class Visitante(models.Model):
	p_nombre = models.CharField(max_length = 40,verbose_name='Primer Nombre')
	s_nombre = models.CharField(max_length = 40,blank=True, null=True,verbose_name='Segundo Nombre')
	p_apellido = models.CharField(max_length = 40,verbose_name='Primer Apellido')
	s_apellido = models.CharField(max_length = 40,blank=True, null=True,verbose_name='Segundo Apellido')
	cedula = models.CharField(max_length = 15,verbose_name='Cedula de Identidad')
	direccion = models.CharField(max_length = 200,verbose_name='Dirección de Habitación')
	telefono  = models.CharField(max_length = 11)
	fecha_hora_entrada = models.DateTimeField("Hora de visita", blank=False, null=False, default=datetime.now)
	fecha_hora_salida = models.DateTimeField("Hora de salida", blank=True, null=True)
	dpto_visita = models.ForeignKey(Departamento, null=False, blank=False, on_delete=models.PROTECT)

	def salida(self):
		self.fecha_hora_salida = timezone.now()
		self.save()

	def __str__(self):
		return '%s %s %s'%(self.p_nombre, self.p_apellido, self.cedula)