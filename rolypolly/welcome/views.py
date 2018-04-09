from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.template import RequestContext
from rolypolly.classes.User import *

def index(request):
	
	message = "No User"
	if request.method == "POST":
		message = request.POST
	return render(request, 'welcome/welcome.html', {'message': message})
	# return HttpResponse("Welcome {}, this is our login / sign up page.".format(user.getName()))
