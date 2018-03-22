from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.template import RequestContext
from rolypolly.classes.User import *

def index(request):
	user = Participant()
	user.setName("Brandon")
	return render(request, 'welcome/welcome.html', {})
	# return HttpResponse("Welcome {}, this is our login / sign up page.".format(user.getName()))

def init_participant(request):
	print("hello")
	if request.method == "POST":
		
		render_to_response('welcome/welcome.html', RequestContext(request, {'params':HttpRequest.POST}))
	return render(request, 'welcome/welcome.html', {})