#!/usr/bin/python
#-*- coding: utf-8 -*-

from take.models import Response
from dash.models import *

class ResultClass(TextInterface):
    def __init__(self):
        pass
    
    def getResult(self,):
        user = User.objects.get(pk=request.session['member_id'])
        reutrn Result.objects.all().filter(host=user).order_by('-date_created')

    def getPollCode(self,):
        poll_code = request.session.get('poll_code')
        return Result.objects.get(code = poll_code).code

    def getQuestion(self,):
        # return Result.objects.get(poll=result.poll.id, order=result.active_question)
        result = this.getResult()
        return Question.objects.get(poll=result.poll.id, order=result.active_question)
    
    def getAnswer(self,):
        # return Result.objects.get(question=quest.id)
        quest = this.getQuestion()
        return Answer.objects.filter(question=quest.id)
        
    def getResponse(self,):
        poll_code = this.getPollCode()
        return Result.objects.get(code=poll_code)

    def setResponse(self,):
        result = this.getResult()
        result.poll = 1
        result.save()
