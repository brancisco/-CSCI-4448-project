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
        poll = Poll.objects.get(pk = result.poll.id)
        pollName = poll.name
        quest = Question.objects.get(poll = result.poll.id, order = result.active_question)
        question = quest.text
        ans = Answer.objects.filter(question = quest.id)
        # answer = [a.text for a in ans]
        # ids = [a.id for a in ans]
    except:
        err = 'No question to answer ¯\_(ツ)_/¯'
        return render(request, 'take/takePoll.html', {'pollName':pollName, 'err': err})

    if request.method == "POST":
        try:
            oid = request.POST.get('answer')
            r = Response(result_id=result.id, question_id=quest.id, answer_id=oid)
            r.save()
            return render(request, 'take/waitPage.html', {'pollName':pollName, 'poll_code':poll_code, 'response':oid})
        except:
            print("fail")
            return JsonResponse({'success': False})
    return render(request, 'take/takePoll.html', {'pollName':pollName, 'question':question, 'answer':ans})

def wait(request):
    print("We are now waiting")
