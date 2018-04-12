from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from rolypolly.classes.User import *
from dash.models import *

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
	return render(request, 'dash/create.html', {'username': user.username, })

def start(request):
	# if 'member_id' in request.session.keys():
	# 	user = User.objects.get(pk=request.session['member_id'])
	# else:
	# 	redirect('/login')
	poll = Poll.objects.get(pk=request.session['pol_id'])
	return render(request, {'poll_name': poll})
	