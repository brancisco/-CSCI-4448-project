#-*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from rolypolly.classes.Poll import *

class User(ABC):
	@abstractmethod
	def __init__(self):
		self.name = None

	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

class Participant(User):
	def __init__(self):
		self.name = None
		self.id = None
		self.response = None
		self.pol_id = None

	def Participant(self, ):
		pass

	def dbStoreResponse(self, ):
		pass

	def getId(self, ):
		pass

	def setId(self, id):
		pass

	def setPollId(self, id):
		pass

	def getPollId(self, ):
		pass

class Host(User):
	def __init__(self, name=None, id=None):
		self.name = name
		self.id = id
		self.livePoll = None

	def startPoll(self, host_id, pol_id):
		self.livePoll = PollState(hostId=host_id, pid=pol_id)
