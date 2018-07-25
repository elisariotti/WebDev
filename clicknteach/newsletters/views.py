from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
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
			# Email parameters
			subject = "Thank you for joing our Newsletter!"
			from_email = settings.EMAIL_HOST_USER
			to_email = [instance.email]

			# to open a file
			with open(settings.BASE_DIR + "/templates/newsletters/sign_up_email.txt") as f:
				signup_message = f.read()
			message = EmailMultiAlternatives(subject = subject, body = signup_message, from_email=from_email, to=to_email)
			html_template = get_template("newsletters/sign_up_email.html").render()
			message.attach_alternative(html_template, "text/html")
			message.send()

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

			# Email parameters
			subject = "You've been unsubscribed."
			from_email = settings.EMAIL_HOST_USER
			to_email = [instance.email]

			# Envio direto
			#signup_message = """Sorry to see you go, let us know if there is an issue with our service."""
			#send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=signup_message, fail_silently=False,)

			# to open a file
			with open(settings.BASE_DIR + "/templates/newsletters/unsubscribe_email.txt") as f:
				signup_message = f.read()
			message = EmailMultiAlternatives(subject = subject, body = signup_message, from_email=from_email, to=to_email)
			html_template = get_template("newsletters/unsubscribe_email.html").render()
			message.attach_alternative(html_template, "text/html")
			message.send()


		else:
			messages.warning(request,
							'You email is not in the database',
							"alert alert-warning alert-dismissible")


	context = {
		'form': form,
	}

	template = "./newsletters/unsubscribe.html"

	return render(request, template, context)
