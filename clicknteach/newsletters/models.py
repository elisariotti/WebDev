from __future__ import absolute_import

from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from mezzanine.pages.models import RichText

class Newsletter(RichText):
	EMAIL_STATUS_CHOICES = (
		('Draft' , 'Draft'),
		('Published' , 'Published')
	)
	subject = models.CharField(max_length=250)
	users = models.ManyToManyField(User, limit_choices_to={'profile__newsletter_reader': True, 'is_active': True})
	status = models.CharField(max_length=10, choices=EMAIL_STATUS_CHOICES)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.subject

	class Meta:
		ordering=('updated',)
