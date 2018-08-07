from django import forms
from .models import Newsletter
from users.models import Profile
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper


class NewsletterCreationForm(forms.ModelForm):
		helper = FormHelper()
		helper.form_show_labels = False

		class Meta:
			model = Newsletter
			fields = ['subject', 'body', 'users', 'status']

		def clean_subject(self):
			subject = self.cleaned_data.get('subject')
			return subject

#		def __init__(self, profile__newsletter_reader, *args, **kwargs):
#			super(NewsletterCreationForm, self).__init__(*args, **kwargs)
#			self.initial['users'] = [s.pk for s in list(User.objects.filter(profile__newsletter_reader=True))]
