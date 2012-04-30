import datetime
from django.utils import timezone
from django.db import models

# Create your models here.

class Poll(models.Model):
	question = models.CharField(max_length=200)
	#                 CharField requires a max_length argument
	pub_date = models.DateTimeField('date published')
	#                                human-readable positional argument
	def __unicode__(self):
		return self.question
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=2)

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	# ForeignKey means that each Choice is related to a single Poll. 
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()
	def __unicode__(self):
		return self.choice