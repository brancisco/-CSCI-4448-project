#!/usr/bin/python
#-*- coding: utf-8 -*-

from take.models import Response
from dash.models import *

class ResultClass():
    def __init__(self,):
        self.poll_code = ''

    def setPollCode(self, req):
        self.poll_code = req.session.get('poll_code')
    
    def getResult(self,):
        user = User.objects.get(pk=request.session['member_id'])
        return Result.objects.all().filter(host=user).order_by('-date_created')

    def getPollCode(self,):
        return this.poll_code

    def getQuestion(self,):
        result = this.getResult()
        return Question.objects.get(poll=result.poll.id, order=result.active_question)
    
    def getAnswer(self,):
        quest = this.getQuestion()
        return Answer.objects.filter(question=quest.id)
        
    def getResponse(self,):
        poll_code = this.getPollCode()
        return Result.objects.get(code=poll_code)

    def setResponse(self,):
        result = this.getResult()
        result.poll = 1
        result.save()
