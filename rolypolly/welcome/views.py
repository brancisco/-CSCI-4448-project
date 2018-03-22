from django.shortcuts import render
from django.template import Template, Context

from django.http import HttpResponse
from rolypolly.classes.User import *

def index(request):
    user = Participant()
    user.setName("Brandon")
    return HttpResponse("Welcome {}, this is our login / sign up page.".format(user.getName()))
    # fp = open('./templates/index.html')
    # t = Template(fp.read())
    # fp.close()
    # html = t.render(Context({}))
    # return HttpResponse(html)