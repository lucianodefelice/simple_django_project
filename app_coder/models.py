from django.db import models

# Create your models here.
class Course(models.Model):

    name=models.CharField(max_length=40)
    code = models.IntegerField()


class Persona(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()


class Entregable(models.Model):
    nombre= models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()  
    entregado = models.BooleanField()