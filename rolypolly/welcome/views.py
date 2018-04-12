from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.template import RequestContext
from rolypolly.classes.User import *
from dash.models import User

def index(request):
	message = "No User"
	if request.method == "POST":
		message = request.POST
	return render(request, 'welcome/welcome.html', {'message': message})
	# return HttpResponse("Welcome {}, this is our login / sign up page.".format(user.getName()))

def signup(request):
	user = None
	message = ''
	if request.method == "POST":
		
		user = User(first_name=request.POST['first_name'],
			last_name=request.POST['last_name'],
			username=request.POST['username'],
			email=request.POST['email'],
			password=request.POST['password']
		)
		try:
			user.save()
			return render(request, 'welcome/success.html', {})
		except:
			message = 'fail'

	return render(request, 'welcome/signup.html', {'message': message})

def login(request):
	message = ''
	if request.method == 'POST':
		if 'member_id' not in request.session.keys():
			try:
				user = User.objects.get(username=request.POST['username'])
				print(user.password)
				if user.password == request.POST['password']:
					message = 'Authenticated!'
					request.session['member_id'] = user.id
					return redirect('/dash')
				else:
					message = 'Not Authenticated.'
			except:
				message = 'No matching user'
				user = None
			return render(request, 'welcome/login.html', {'message': message})

	if 'member_id' in request.session.keys():
		return redirect('/dash')

	return render(request, 'welcome/login.html', {'message': message})
