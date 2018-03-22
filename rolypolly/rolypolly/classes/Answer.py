#!/usr/bin/python
#-*- coding: utf-8 -*-

from TextInterface import TextInterface

class Answer(TextInterface):
<<<<<<< Updated upstream
    def __init__(self, text=None, correct=None):
=======
    def __init__(self, text=None, correct=False):
>>>>>>> Stashed changes
        self.text = text
        self.setCorrect(correct)

    def getCorrect(self, ):
        return self.correct

    def setCorrect(self, correct):
        self.correct = True
