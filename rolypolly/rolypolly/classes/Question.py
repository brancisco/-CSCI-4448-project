#!/usr/bin/python
#-*- coding: utf-8 -*-

import Answer from Answer

class Question(Answer):
    def __init__(self, text=None, answers=None):
        self.text = text
        self.answers = answers

    def getCorrect(self, ):
        return self.answers.getCorrect()

    def setCorrect(self, aid, correct):
        self.answers[aid].setCorrect(correct)

    def addAnswer(self, text, correct):
        answer = Answer(text, correct)
        self.answers.append(answer)
    
    def delAnswer(self, aid):
        del answers[aid]
    
    def updateAnswer(self, aid, text, correct):
        self.delAnswer(aid)
        self.addAnswer(text, correct)