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
from take.models import Response


def index(request):

    poll_code = request.session.get('poll_code')
    pollName = ''
    err = ''
    question = ''
    answer = ''
    response = ''
    try:
        result = Result.objects.get(code = poll_code)
        if result.date_closed:
            request.session.clear()
            return redirect('/welcome')
        poll = Poll.objects.get(pk = result.poll.id)
        pollName = poll.name
        quest = Question.objects.get(poll = result.poll.id, order = result.active_question)
        question = quest.text
        ans = Answer.objects.filter(question = quest.id)

    except:
        err = 'No question to answer ¯\_(ツ)_/¯'
        return render(request, 'take/takePoll.html', {'pollName':pollName, 'err': err})

    if request.method == "POST":
        # try:
        aid = request.POST.get('answer')
        print(request.session['answered'])
        request.session['answered'][str(quest.id)] = True
        request.session.modified = True
        r = Response(result_id=result.id, question_id=quest.id, answer_id=aid)
        r.save()
        return render(request, 'take/waitPage.html', {'poll':poll, 'poll_code':poll_code, 'response':aid})
        # except:
        #     return JsonResponse({'success': False})
    else:
        if str(quest.id) in request.session['answered']:
            return render(request, 'take/waitPage.html', {'poll':poll, 'poll_code':poll_code})

    return render(request, 'take/takePoll.html', {'poll':poll, 'question':question, 'answer':ans})

@csrf_exempt
def wait(request):
    if request.method == "POST" and request.session.get('started'):
        poll_code = request.session.get('poll_code')
        poll_id = request.session.get('poll_id')
        qoid = request.session.get('qoid')
        check = request.POST.get('check')
        print(poll_code)
        active_question = Result.objects.get(code=poll_code).active_question
        is_closed = Result.objects.get(code=poll_code).date_closed
        if is_closed:
            request.session.clear()
            request.session['thanks'] = True
            return JsonResponse({'success': True, 'FINISH': True})

        if int(active_question) != int(qoid):
            request.session['qoid'] = active_question
            return JsonResponse({'success': True, 'NEXTQ': True})

        if int(check) > 300:
            request.session.clear()
            return JsonResponse({'success': False, 'CHECK_NUMBER': 'TIMED_OUT'})

        return JsonResponse({'success': True, 'CHECK_NUMBER': int(check), 'qoid': int(qoid)})
    else:
        request.session.clear()
        return JsonResponse({'success': False, 'CHECK_NUMBER': 'TIMED_OUT'})