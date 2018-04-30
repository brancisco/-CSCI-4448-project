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
	def __init__(self, responseDict={}, name=None, uid=None, poll_code=None):
		self.name = self.setName(name)
		self.id = self.setId(uid)
		self.response = responseDict
		self.poll_code = self.setPollCode(poll_code)

	def getId(self):
		return self.id

	def setId(self, uid):
		self.id = uid

	def setPollCode(self, code):
		self.code = code

	def getPollCode(self):
		return self.code

	def setResponse(self, qoid):
		self.response[qoid] = True

	def getResponse(self, qoid):
		return self.response[qoid]


class Host(User):
	def __init__(self, name=None, id=None):
		self.name = name
		self.id = id
		self.livePoll = None

	def startPoll(self, host_id, pol_id):
		self.livePoll = PollState(hostId=host_id, pid=pol_id)
