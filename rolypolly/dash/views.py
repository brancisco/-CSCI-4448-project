from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rolypolly.classes.User import *
from dash.models import *

def index(request):
	if 'member_id' in request.session.keys():
		user = User.objects.get(pk=request.session['member_id'])
		return render(request, 'dash/dash.html', {'username': user.username})
	else:
		redirect('/login')


def create(request):
	user = None
	if 'member_id' in request.session.keys():
		user = User.objects.get(pk=request.session['member_id'])
		return render(request, 'dash/create.html', {'username': user.username})
	else:
		redirect('/login')
	return render(request, 'dash/create.html', {'username': user.username})

@csrf_exempt
def save_poll(request):
	try:
		data = request.POST['data']
		poll_name = request.POST['poll_name']
		data = json.loads(data)
		questions = data

		poll = Poll(name=poll_name, host_id=1)
		poll.save()
		qi = 0
		for q in questions:
			question = Question(poll_id=poll.id, text=q['text'], order=qi)
			question.save()
			qi += 1
			ai = 0
			for a in q['answers']:
				answer = Answer(question_id=question.id, text=a['text'], is_correct=a['correct'], order=ai)
				answer.save()
				ai += 1
		return JsonResponse({'success': True})
	except:
		return JsonResponse({'success': False})

	return render(request, 'dash/create.html', {'username': user.username, })

def start(request):
	# if 'member_id' in request.session.keys():
	# 	user = User.objects.get(pk=request.session['member_id'])
	# else:
	# 	redirect('/login')
	poll = Poll.objects.get(pk=request.session['pol_id'])
	return render(request, {'poll_name': poll})
