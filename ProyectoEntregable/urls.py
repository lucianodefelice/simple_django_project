"""ProyectoEntregable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ProyectoEntregable.views import  diaDeHoy, miNombreEs, template_using_context, template_using_loader, new_course, mostrar_familiares

from ProyectoEntregable.views import (
    template_using_context,
    template_using_loader,
    new_course,
    mostrar_familiares,
)
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('diadehoy', diaDeHoy),
    path('miNombreEs/<nombre>/<edad>', miNombreEs),
    path('template_using_context/<str:name>/<str:last_name>', template_using_context),
    path('template_using_loader/<str:name>/<str:last_name>', template_using_loader),
    path('new_course/<str:name>/<str:code>', new_course),
    path('mostrar_familiares/<str:nombre>/<str:apellido>/<str:email>', mostrar_familiares),
]
