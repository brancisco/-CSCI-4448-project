from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.template import RequestContext
from rolypolly.classes.User import *
from dash.models import *
from django.template import loader


def index(request):
	if request.session.get('thanks'):
		del request.session['thanks']
		t = loader.get_template('welcome/thanks.html')
		return HttpResponse(t.render())

	message = ''
	participant = Participant()
	if request.session.get('started'):
		return redirect('/take')
	if request.method == "POST":
		try:
			request.session.set_expiry(900)
			request.session['started'] = True
			request.session['answered'] = {}
			result = Result.objects.get(code=request.POST['code'])

			participant.setPollCode(request.POST['code'])
			participant.setName(request.POST['name'])
			participant.setId(request.session['started'])

			request.session['poll_code'] = participant.getPollCode()
			request.session['qoid'] = result.active_question

			return redirect('/take')
		except:
			message = 'No poll with that code'
	return render(request, 'welcome/welcome.html', {'message': message})

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
