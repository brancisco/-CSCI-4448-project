#!/usr/bin/python
#-*- coding: utf-8 -*-

from take.models import Response

# from TextInterface import TextInterface

class Result(TextInterface):
    def __init__(self):
        pass

    def getPollCode(self,):
        poll_code = request.session.get('poll_code')
        return Result.objects.get(code = poll_code).code

    def getQuestion(self,):
        return Result.objects.get(poll=result.poll.id, order=result.active_question)
    
    def getAnswer(self,):
        return Answer.objects.filter(question=quest.id)
        
    def getResponse(self,):

    def setRespons(self,):
        
    
    # dont need db pull
    # just getters and setters for all the things in the model

