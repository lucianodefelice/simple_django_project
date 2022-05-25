from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

def hello_world(rquest):
    return HttpResponse("Hello world")

def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :) ")

def diaDeHoy(request):

        dia = datetime.now()

        documentoDeTexto = f"Hoy es día: <br> {dia}"


        return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre, edad):

      documentoDeTexto = f"Mi nombre es: <br><br>  {nombre} <br><br> Mi edad es: {edad} "


      return HttpResponse(documentoDeTexto)

def probandoTemplate(self):

    miHtml = open("D:/Coder/Python/ProyectoEntregable/ProyectoEntregable/templates/template.html")

    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context

    miHtml.close() #Cerramos el archivo

    miContexto = Context() #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

    render = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento

    return HttpResponse(render)