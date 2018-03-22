#!/usr/bin/python
#-*- coding: utf-8 -*-

class Answer():
    def __init__(self, text=None, correct=None):
        self.text = text
        self.setCorrect(correct)

    def getCorrect(self, ):
        return self.correct

    def setCorrect(self, correct):
        self.correct = True
