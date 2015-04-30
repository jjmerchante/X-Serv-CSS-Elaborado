from django.shortcuts import render
from models import Page
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden


def addPage(resource, body):
    try:
        Page.objects.get(name=resource)
        salida = "That page was in the server"
    except Page.DoesNotExist:
        newpage = Page(name=resource, page=body)
        newpage.save()
        salida = "New page added"
    return salida


@csrf_exempt
def mostrar(request, resource):
    if request.method == "GET":
        salida = "<html><head><link rel='stylesheet'" + \
            "href='/css/main.css'></head><body>"
        try:
            fila = Page.objects.get(name=resource)
            salida += fila.page + "</body></html>"
            return HttpResponse(salida)
        except Page.DoesNotExist:
            salida += 'Page not found: ' + resource + "</body></html>"
            return HttpResponseNotFound(salida)

    elif request.method == "PUT":
        salida = addPage(resource, request.body)
        return HttpResponse(salida)
    else:
        return HttpResponseForbidden("Method not allowed")


@csrf_exempt
def cssView(request, resource):
    if request.method == "GET":
        try:
            fila = Page.objects.get(name=resource)
            return HttpResponse(fila.page, content_type="text/css")
        except Page.DoesNotExist:
            return HttpResponseNotFound('Page not found: ' + resource)

    elif request.method == "PUT":
        salida = addPage(resource, request.body)
        return HttpResponse(salida)

    else:
        return HttpResponseForbidden("Method not allowed")
