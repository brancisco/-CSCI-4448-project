#!/usr/bin/python
#-*- coding: utf-8 -*-

from TextInterface import TextInterface

class Response(TextInterface):
    def __init__(self):
        self.pid = None
        self.pol_id = None
        self.qid = None
        self.aid = None
    
    def setPid(self, pid):
        self.pid = pid
    
    def setPolId(self, pol_id):
        self.pol_id = pol_id

    def setQid(self, qid):
        self.qid = qid
    
    def setAid(self, aid):
        self.aid = aid
    
    def getPid(self, ):
        return self.pid
    
    def getPolId(self, ):
        return self.pol_id
    
    def getQid(self, ):
        return self.qid
    
    def getAid(self, ):
        return self.aid
