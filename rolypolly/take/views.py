from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.template import RequestContext
from rolypolly.classes.User import *
from dash.models import *

from django.core import serializers

def index(request):
    poll_code = request.session.get('poll_code')
    pollName = ''
    err = ''
    question = ''
    answer = ''
    if request.method == "POST":

        print("SUBMITTED")
    try:
        result = Result.objects.get(code = poll_code)
        poll = Poll.objects.get(pk = result.poll.id)
        pollName = poll.name
        quest = Question.objects.get(poll = result.poll.id, order = result.active_question)
        question = quest.text
        ans = Answer.objects.filter(question = quest.id)
        answer = [a.text for a in ans]
    except:
        err = 'No question to answer ¯\_(ツ)_/¯'
        return render(request, 'take/takePoll.html', {'pollName':pollName, 'err': err})

    print("... ... ...")
    return render(request, 'take/takePoll.html', {'pollName':pollName, 'question':question, 'answer':answer})

def takePoll(request):
    print("This is what happends")
