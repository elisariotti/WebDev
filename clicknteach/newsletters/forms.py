from django import forms
from .models import Newsletter
from users.models import Profile
from django.contrib.auth.models import User

class NewsletterForm(forms.ModelForm):
		class Meta:
			model = Newsletter
			fields = ['subject', 'content', 'users', 'status']

		def clean_subject(self):
			subject = self.cleaned_data.get('subject')
			return subject
