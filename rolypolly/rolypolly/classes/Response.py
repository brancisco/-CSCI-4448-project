#!/usr/bin/python
#-*- coding: utf-8 -*-
from take.models import Response
from dash.models import *

class ResponseClass():
    def __init__(self,):
        self.poll_code = ''
    
    def setPollCode(self, req):
        self.poll_code = req.session.get('poll_code')

    def setQuestion(self, qid):
        answer = this.getAnswer()
        result = this.getResult()
        request.session.modified = True
        r = Response(result_id=result.id, question_id=qid, answer_id=answer.id)
        r.save()
    
    def setAnswer(self, aid):
        result = this.getResult()
        question = this.getQuestion()
        request.session.modified = True
        r = Response(result_id=result.id, question_id=quest.id, answer_id=aid)
        r.save()
    
    def getPollCode(self,):
        return self.poll_code
    
    def getResult(self,):
        return Result.objects.get(code = this.poll_code)
    
    def getQuestion(self, ):
        result = this.getResult()
        return Question.objects.get(poll = result.poll.id, order = result.active_question)
    
    def getAnswer(self, ):
        quest = this.getQuestion()
        return Answer.objects.filter(question = quest.id)
