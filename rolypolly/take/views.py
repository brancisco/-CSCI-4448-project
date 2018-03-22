from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Here is where you will be taking the poll.")