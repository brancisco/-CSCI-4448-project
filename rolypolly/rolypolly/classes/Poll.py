#-*- coding: utf-8 -*-

class PollState:
    def __init__(self, hostId=None, pid=None, sessionCode=None, participants=None, currentQ=None):
        self.hostId = hostId
        self.pid = pid
        self.sessionCode = sessionCode
        self.participants = participants
        self.currentQ = currentQ

    def nextQuestion(self, ):
        pass

    def dbUpdateState(self, ):
        pass

    def dbStartPoll(self, ):
        pass

    def dbClosePoll(self, ):
        pass

    def setHostId(self, hostId):
        pass

    def setId(self, id):
        pass

    def genSessionCode(self, ):
        pass

    def setParticipantCount(self, count):
        pass

    def getHostId(self, ):
        pass

    def getId(self, ):
        pass

    def getSessionCode(self, ):
        pass

    def getParticipantCount(self, ):
        pass

    def getCurrentQ(self, ):
        pass