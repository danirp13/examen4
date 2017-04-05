from django.db import models
from django.core.urlresolvers import reverse


class Materia(models.Model):
	nombre=models.CharField(max_length=100,blank=True)
	descripcion=models.CharField(max_length=100,blank=True)
	profesor=models.CharField(max_length=100,blank=True)
	
	def __str__(self):
		return self.nombre+" "+self.profesor


class Estudiante(models.Model):
	"""estudiantes"""
	email=models.EmailField(max_length=50)
	nombres=models.CharField(max_length=100,blank=True)
	apellidos=models.CharField(max_length=100,blank=True)
	direccion=models.CharField(max_length=200,blank=True)
	fecha_nac=models.DateField(auto_now_add=False)
	observaciones=models.TextField()
	materia= models.ForeignKey(Materia)
	
	def __str__(self):
		return self.nombres+" "+self.apellidos

		
# Create your models here.
