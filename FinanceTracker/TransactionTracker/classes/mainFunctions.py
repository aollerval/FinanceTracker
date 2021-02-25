from django.shortcuts import render
from django.http import HttpResponse

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

##def printTablesHTML(table): ##Have to add pages to calculate the 20 transactions that will be printed