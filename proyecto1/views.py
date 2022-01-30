from cgitb import html
from html.entities import html5
from re import template
from xml.dom.minidom import Document
from django.http import HttpResponse
import datetime
from django.shortcuts import render
from django.template import Template, Context
from django.http import Http404

def saludo(request): # primera vista

    doc_external=open("C:/Users/Dell Laptop/Desktop/ProyectosDjango/proyecto1/proyecto1/Plantillas/mi_plantilla1.html")
    plt=Template(doc_external.read())
    doc_external.close()

    ctx=Context()

    documento =plt.render(ctx)

    return HttpResponse(documento)


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
