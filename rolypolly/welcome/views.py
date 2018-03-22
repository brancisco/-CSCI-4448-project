from django.shortcuts import render

from django.http import HttpResponse
from rolypolly.classes.User import *

def index(request):
	user = Participant()
	user.setName("Brandon")
	return HttpResponse("Welcome {}, this is our login / sign up page.".format(user.getName()))