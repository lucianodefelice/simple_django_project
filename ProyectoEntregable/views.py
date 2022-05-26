from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.template import loader
#from app_coder import Course
from app_coder.models import Course
from app_coder.models import Persona


def diaDeHoy(request):

        dia = datetime.now()
        documentoDeTexto = f"Hoy es día: <br> {dia}"
        return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre, edad):

      documentoDeTexto = f"Mi nombre es: <br><br>  {nombre} <br><br> Mi edad es: {edad} "
      return HttpResponse(documentoDeTexto)


def template_using_context(
    self, name: str = 'Name', last_name: str = 'Last_name'):

    miHtml = open("D:/Coder/Python/ProyectoEntregable/ProyectoEntregable/templates/template.html")
    template= Template(miHtml.read())
    
    miHtml.close() #Cerramos el archivo

    context_dict={
        'name': name,
        'last_name': last_name,
        'now': datetime.now(),
        'my_grades': [4, 5, 8, 7, 3]
    }

    my_context= Context(context_dict)
    render= template.render(my_context)
    return HttpResponse(render)

def template_using_loader(
    self, name: str = 'Name', last_name: str = 'Last_name'):
    template= loader.get_template('template_loader.html')
    context_dict={
        'name': name,
        'last_name': last_name,
        'now': datetime.now(),
        'my_grades': [4, 5, 8, 7, 3]
    }
    render=template.render(context_dict)
    return HttpResponse(render)    


def new_course(
    self, name: str = 'course', code: int = 0):
    template= loader.get_template('template_course.html')
    course = Course(name=name, code=code)

    course.save()

    context_dict={
        'course': course
    }
    render=template.render(context_dict)
    return HttpResponse(render)   

def mostrar_familiares(
    self, nombre: str = 'nombre', apellido: str = 'apellido', email: str = 'email'):
    template= loader.get_template('template_familiar.html')
    familiar = Persona(nombre=nombre, apellido=apellido, email=email)

    familiar.save()

    context_dict={
        'familiar': familiar
    }
    render=template.render(context_dict)
    return HttpResponse(render)   
