#!/usr/bin/python
#-*- coding: utf-8 -*-

from take.models import Response
from dash.models import *
# from TextInterface import TextInterface

class ResultClass(TextInterface):
    def __init__(self):
        pass

    def getPollCode(self,):
        poll_code = request.session.get('poll_code')
        return Result.objects.get(code = poll_code).code

    def getQuestion(self,):
        # return Result.objects.get(poll=result.poll.id, order=result.active_question)
        return Question.objects.get(poll=result.poll.id, order=result.active_question)
    
    def getAnswer(self,):
        # return Result.objects.get(question=quest.id)
        return Answer.objects.filter(question=quest.id)
        
    def getResponse(self,):
        return Result.objects.get(code=poll_code)

    def setResponse(self,):
        result.poll = 1
        result.save()
    
    # dont need db pull
    # just getters and setters for all the things in the model

