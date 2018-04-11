from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.template import RequestContext
from rolypolly.classes.User import *
from dash.models import User

def index(request):
	if 'member_id' in request.session.keys():
		user = User.objects.get(pk=request.session['member_id'])
	else:
		redirect('/login')
	return render(request, 'dash/dash.html', {'username': user.username})

def create(request):
	if 'member_id' in request.session.keys():
		user = User.objects.get(pk=request.session['member_id'])
	else:
		redirect('/login')
	return render(request, 'dash/create.html', {'username': user.username})