from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<H1>Hello, world. You're at the polls index.</H1>")

def header():
    stringHTML = "<html>"
    stringHTML += "<h1>This is the header</h1>"
    return stringHTML

def footer():
    stringHTML = "<h1>This is the footer</h1>"
    stringHTML += "</html>"
    return stringHTML

def printLoginForm(request):
    stringHTML = header()
    stringHTML += footer()
    return HttpResponse(stringHTML)