from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.template import RequestContext
from rolypolly.classes.User import *
from dash.models import *

def index(request):
    poll_code = request.session.get('poll_code')
    pollName = ''
    err = ''
    try:
        result = Result.objects.get(code = poll_code)
        try:
            poll = Poll.objects.get(pk = result.poll.id)
            pollName = poll.Name
            return render(request, 'take/takePoll.html', {'pollName': pollName})
        except:
            err = 'No poll name'
    except:
        err = 'Poll no longer exists'
    return render(request, 'take/takePoll.html', {'err': err, 'pollName':pollName})
