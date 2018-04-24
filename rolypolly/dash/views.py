from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils.html import escapejs
from django.utils.safestring import mark_safe
from rolypolly.classes.User import *
from dash.models import *

def index(request):
	if 'member_id' in request.session.keys():
		user = User.objects.get(pk=request.session['member_id'])
		poll = Poll.objects.all().filter(host_id=user.id)
		for p in poll:
			print(p.name)
	else:
		redirect('/login')
	return render(request, 'dash/dash.html', {'username': user.username, 'poll': poll})

def create(request):
	if 'member_id' in request.session.keys():
		user = User.objects.get(pk=request.session['member_id'])
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

@csrf_exempt
def update_poll(request):
	try:
		data = request.POST['data']
		poll_name = request.POST['poll_name']
		poll_id = request.POST['poll_id']
		data = json.loads(data)
		questions = data
		poll = Poll.objects.get(pk=poll_id)
		poll.name = poll_name
		poll.save()
		qi = 0
		q_ids = []
		for q in questions:
			try:
				question = Question.objects.get(pk=q['id'])
				question.text = q['text']
				question.order = q['order']
				question.save()
				q_ids.append(q['id'])
				print('updated old')
			except:
				question = Question(poll_id=poll_id, text=q['text'], order=qi)
				question.save()
				q_ids.append(question.id)
				print('saved new')
			qi += 1

			ai = 0
			a_ids = []
			for a in q['answers']:
				try:
					answer = Answer.objects.get(pk=a['id'])
					answer.text = a['text']
					answer.is_correct = a['correct']
					answer.order = a['order']
					answer.save()
					a_ids.append(a['id'])
				except:
					answer = Answer(question_id=question.id, text=a['text'], is_correct=a['correct'], order=ai)
					answer.save()
					a_ids.append(answer.id)
				ai += 1
			answers = Answer.objects.all().filter(question_id=question.id)

			for a in answers:
				if a.id not in a_ids:
					a.delete()
		questions = Question.objects.all().filter(poll_id=poll_id)
		for q in questions:
			if q.id not in q_ids:
				print('deleting q {}'.format(q.id))
				q.delete()

		poll, q_object = getPollJSON(poll_id)
		return JsonResponse({'success': True, 'questions': json.dumps(q_object)})
	except:
		return JsonResponse({'success': False})

	return render(request, 'dash/review/{}'.format(poll_id), {'username': user.username, })

@csrf_exempt
def delete_poll(request, poll_id):
	if 'member_id' in request.session.keys():
		user = User.objects.get(pk=request.session['member_id'])
	else:
		redirect('/login')

	try:
		del_poll = Poll.objects.get(pk=poll_id)
		del_poll.delete()
		return JsonResponse({'success': True})
	except:
		return JsonResponse({'success': False})
		
def start(request):
	# if 'member_id' in request.session.keys():
	# 	user = User.objects.get(pk=request.session['member_id'])
	# else:
	# 	redirect('/login')
	poll = Poll.objects.get(pk=request.session['pol_id'])
	return render(request, {'poll_name': poll})

def review(request, poll_id):
	if 'member_id' in request.session.keys():
		user = User.objects.get(pk=request.session['member_id'])
	else:
		redirect('/login')
	poll, q_object = getPollJSON(poll_id)
	return render(request, 'dash/review.html',{'username': user.username, 'poll': poll, 'questions': mark_safe(escapejs(json.dumps(q_object))) })

def getPollJSON(poll_id):
	poll = Poll.objects.get(pk=poll_id)
	questions = Question.objects.all().filter(poll_id=poll_id)
	answers = []
	for q in questions:
		answers.append(Answer.objects.all().filter(question_id=q.id))

	q_object = {}
	for i in range(len(questions)):
		cur_q = questions[i]
		q_id = 'q{}'.format(cur_q.id)
		q_object[q_id] = {}
		q_object[q_id]['id'] = cur_q.id
		q_object[q_id]['text'] = cur_q.text
		q_object[q_id]['order'] = cur_q.order
		q_object[q_id]['answers'] = []
		for j in range(len(answers[i])):
			cur_a = answers[i][j]
			answer = {'id': cur_a.id, 'text': cur_a.text, 'correct': cur_a.is_correct, 'order': cur_a.order}
			q_object[q_id]['answers'].append(answer)

	return (poll, q_object)