from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models.query import EmptyQuerySet
import json
import random
from django.utils.html import escapejs
from django.utils.safestring import mark_safe
from rolypolly.classes.User import *
from dash.models import *
from take.models import *
from datetime import datetime
from hashids import Hashids


def index(request):
	if 'member_id' in request.session.keys():
		user = User.objects.get(pk=request.session['member_id'])
		print(user.id)
		poll = Poll.objects.all().filter(host_id=user.id).order_by('-date_created')

		result = Result.objects.all().filter(host=user).order_by('-date_created')
	else:
		return redirect('/login')
	request.session.set_expiry(300)
	return render(request, 'dash/dash.html', {'username': user.username, 'poll': poll, 'result': result})

def create(request):

	if 'member_id' in request.session.keys():
		user = User.objects.get(pk=request.session['member_id'])
		return render(request, 'dash/create.html', {'username': user.username})
	else:
		return redirect('/login')
	request.session.set_expiry(300)
	return render(request, 'dash/create.html', {'username': user.username})

@csrf_exempt
def check_submissions(request):
	if request.method == "POST" and 'member_id' in request.session.keys():
		res_id = request.POST.get('result_id')
		q_id = request.POST.get('waiting_on')
		result = Result.objects.get(pk=res_id)
		responses = Response.objects.all().filter(result=result, question=q_id)
		if len(responses) > 0:
			n_a = len(Answer.objects.all().filter(question=responses[0].question))
		else:
			n_a = 0
		ordered_response_array = [0]*n_a
		for r in responses:
			ordered_response_array[r.answer.order] += 1

		return JsonResponse({'success': True, 'responses': ordered_response_array})
	else:
		#TODO: should clear session? request.session.clear()
		return JsonResponse({'success': False, 'CHECK_NUMBER': 'TIMED_OUT'})

@csrf_exempt
def launch_poll(request):
	
	user = User.objects.get(pk=request.session['member_id'])
	request.session.set_expiry(300)
	other_results = Result.objects.filter(date_closed__isnull=True, host=user.id)

	if not len(other_results):
		#TODO:  must do a while not in database, try to generate hash to avoid collision
		hashids = Hashids(salt='Roses are red violets are blue', min_length=5)
		code = hashids.encode(random.randint(1, 1000000))
		poll_id = request.POST['poll_id']
		result = Result(code=str(code), active_question=0, poll_id=poll_id, host=user)
		result.save()
		return JsonResponse({'success': True, 'poll_code': code})
	else:
		return JsonResponse({'success': False})

def launch_page(request):
	if 'member_id' in request.session.keys():
		user = User.objects.get(pk=request.session['member_id'])
		request.session.set_expiry(300)
	else:
		return redirect('/login')
	try:
		result = Result.objects.get(date_closed__isnull=True, host=user.id)
		poll = Poll.objects.get(pk = result.poll.id)
		quest = Question.objects.get(poll = result.poll.id, order = result.active_question)
		questions = Question.objects.filter(poll=result.poll.id)
		ans = Answer.objects.filter(question = quest.id)

		return render(request, 'dash/launch.html', {'poll': poll, 'username': user.username, 'question': quest,
		 'answer': ans, 'result': result, 'n_questions': len(questions)})
	except:
		return redirect('/dash')

@csrf_exempt
def change_question(request):
	if 'member_id' in request.session.keys():
		user = User.objects.get(pk=request.session['member_id'])
		request.session.set_expiry(300)
	else:
		return redirect('/login')

	result = Result.objects.get(date_closed__isnull=True, host=user.id)
	questions = Question.objects.filter(poll=result.poll.id)
	direction = int(request.POST['direction'])
	if direction > 0 and result.active_question < len(questions):
		result.active_question += 1
	elif result.active_question > 0: # should make this elif to check for out of range
		result.active_question -= 1
	result.save()
	return JsonResponse({'success': True})

@csrf_exempt
def close_poll(request):
	if 'member_id' in request.session.keys():
		user = User.objects.get(pk=request.session['member_id'])
		request.session.set_expiry(300)
	else:
		return redirect('/login')

	result = Result.objects.get(date_closed__isnull=True, host=user.id)
	# TODO: This needs to be server date time instead of local date time?
	result.date_closed = datetime.now()
	result.save()
	return JsonResponse({'success': True})
	

@csrf_exempt
def save_poll(request):
	try:
		user = User.objects.get(pk=request.session['member_id'])
		data = request.POST['data']
		poll_name = request.POST['poll_name']
		data = json.loads(data)
		questions = data
		user = User.objects.get(pk=request.session['member_id'])

		poll = Poll(name=poll_name, host_id=user.id)
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
		request.session.set_expiry(300)
		return JsonResponse({'success': True})
	except:
		return JsonResponse({'success': False})

	return render(request, 'dash/create.html', {'username': user.username, })

@csrf_exempt
def update_poll(request):
	if 'member_id' in request.session.keys():
		user = User.objects.get(pk=request.session['member_id'])
	else:
		redirect('/login')
	try:
		data = request.POST['data']
		poll_name = request.POST['poll_name']
		poll_id = request.POST['poll_id']
		data = json.loads(data)
		questions = data
		poll = Poll.objects.get(pk=poll_id, host_id=user.id)
		poll.name = poll_name
		poll.save()
		qi = 0
		q_ids = []
		for q in questions:
			try:
				question = Question.objects.get(pk=q['id'])
				question.text = q['text']
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
		request.session.set_expiry(300)
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
	if 'member_id' in request.session.keys():
		user = User.objects.get(pk=request.session['member_id'])
	else:
		return redirect('/login')
	poll = Poll.objects.get(pk=request.session['pol_id'])
	request.session.set_expiry(300)
	return render(request, {'poll_name': poll})

def review(request, poll_id):
	if 'member_id' in request.session.keys():
		user = User.objects.get(pk=request.session['member_id'])
	else:
		return redirect('/login')
	poll, q_object = getPollJSON(poll_id)
	request.session.set_expiry(300)
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
