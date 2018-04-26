from django.db import models

class Response(models.Model):
	result 			= models.ForeignKey('dash.Result', on_delete=models.CASCADE)
	question 		= models.ForeignKey('dash.Question', on_delete=models.CASCADE)
	answer 			= models.ForeignKey('dash.Answer', on_delete=models.CASCADE)
	date_created 	= models.DateTimeField(auto_now_add=True)
