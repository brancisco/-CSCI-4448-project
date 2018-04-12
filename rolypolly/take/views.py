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
    try:
        result = Result.objects.get(code = poll_code)
        try:
            poll = Poll.objects.get(pk = result.poll.id)
            pollName = poll.Name
            try:
                quest = Question.objects.get(poll = result.poll.id, order = result.active_question)
                question = quest.text
                try:
                    ans = Answer.objects.filter(question = quest.id)
                    answer = [a.text for a in ans]
                    return render(request, 'take/takePoll.html', {'pollName':pollName, 'question':question, 'answer':answer})
                except:
                    err = 'No answers avaliable'
                    return render(request, 'take/takePoll.html', {'err':err,'pollName':pollName, 'question':question})
            except:
                err = 'No question to answer ¯\_(ツ)_/¯'
            return render(request, 'take/takePoll.html', {'pollName':pollName, 'err': err})
        except:
            err = 'No poll name'
    except:
        err = 'Poll no longer exists'
    return render(request, 'take/takePoll.html', {'err': err})
