#!/usr/bin/python
#-*- coding: utf-8 -*-
from take.models import Response
from dash.models import *

class Response():
    def __init__(self):
        pass
    
    # def setPolId(self, pol_id):
    #     self.pol_id = pol_id

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
        r = Response(result_id=result.id, question_id=quest.id, answer_id=ais
        r.save()
    
    def getPolId(self, ):
        return request.session.get('poll_id')
    
    def getPollCode(self,):
        return request.session.get('poll_code')
    
    def getResult(self,):
        poll_code = this.getPolId()
        return Result.objects.get(code = poll_code)
    
    def getQuestion(self, ):
        result = this.getResult()
        return Question.objects.get(poll = result.poll.id, order = result.active_question)
    
    def getAnswer(self, ):
        quest = this.getQuestion()
        # request.POST.get('answer')
        return Answer.objects.filter(question = quest.id)
