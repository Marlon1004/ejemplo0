from cgitb import html
from html.entities import html5
from re import template
import re
from xml.dom.minidom import Document
from django.http import HttpResponse
import datetime
from django.shortcuts import render
from django.template import Template, Context
from django.http import Http404
from django.template.loader import get_template
from django.shortcuts import render


def saludo(request): # primera vista

    nombre = "Marlon"

    #doc_external=open("C:/Users/Dell Laptop/Desktop/ProyectosDjango/proyecto1/proyecto1/Plantillas/mi_plantilla1.html")
    #plt=Template(doc_external.read())
    #doc_external.close()

    #doc_externo=get_template("mi_plantilla1.html")

    #ctx=Context({"nombre_persona": nombre, "temas": ["Plantillas", "Modelos", "Formularios","vistas", "Despliegue"]})
    #documento =doc_externo.render({"nombre_persona": nombre, "temas": ["Plantillas", "Modelos", "Formularios","vistas", "Despliegue"]})

    return render(request, "mi_plantilla1.html", {"nombre_persona": nombre, "temas": ["Plantillas", "Modelos", "Formularios","vistas", "Despliegue"]})


def cursoC(request):
    return render(request, "CursoC.html")

def cursoCss(request):
    return render(request, "cursoCss.html")

def despedida(request): # primera vista
    return HttpResponse("Hasta luego")


def damefecha(request): # primera vista
    fecha=datetime.datetime.now()

    escrito= """<html> 
    <body>
    fecha y hora actuales %s
    </body>
    </html> """ % fecha
    return HttpResponse(escrito)
