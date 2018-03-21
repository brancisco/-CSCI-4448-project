from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome, this is our login / sign up page.")