from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from .models import NewsletterUser
from .forms import NewsletterUserSignUpForm, NewsletterUserUnsubsForm

def newsletter_signup(request):
	form = NewsletterUserSignUpForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		if NewsletterUser.objects.filter(email=instance.email).exists():
			messages.warning(request,
							'You email already exists in our database',
							"alert alert-warning alert-dismissible")
		else:
			instance.save()
			messages.success(request,
							'You email has been submited to the database',
							"alert alert-success alert-dismissible")


	context = {
		'form': form,
	}

	template = "./newsletters/sign_up.html"

	return render(request, template, context)


def newsletter_unsubscribe(request):
	form = NewsletterUserUnsubsForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		if NewsletterUser.objects.filter(email=instance.email).exists():
			NewsletterUser.objects.filter(email=instance.email).delete()
			messages.success(request,
							'You email has been removed',
							"alert alert-success alert-dismissible")

		else:
			messages.warning(request,
							'You email is not in the database',
							"alert alert-warning alert-dismissible")


	context = {
		'form': form,
	}

	template = "./newsletters/unsubscribe.html"

	return render(request, template, context)

