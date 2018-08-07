from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.loader import get_template
from django.contrib.auth.models import User
from .models import Newsletter, Profile
from .forms import NewsletterCreationForm

def control_newsletters(request):
	form = NewsletterCreationForm(request.POST or None)

	if form.is_valid():
		instance = form.save()
		newsletter = Newsletter.objects.get(id=instance.id)
		if newsletter.status == "Published":
			subject = newsletter.subject
			body = newsletter.body
			from_email = settings.EMAIL_HOST_USER

			email_list = newsletter.users.all().values_list('email', flat=True)
			#email_list = newsletter.users.filter(profile__newsletter_reader=True).values_list('email', flat=True)
			for email in email_list:
				send_mail(subject=subject, from_email=from_email,
				recipient_list=[email], message=body, fail_silently=True)

		return redirect('control_panel:control_newsletter_detail', pk=newsletter.pk)
	context = {
		"form":form,
	}

	template = "./control_panel/control_newsletters.html"
	return render(request, template, context)

def control_newsletter_edit(request, pk):
	newsletter = get_object_or_404(Newsletter, pk=pk)

	if request.method == 'POST':
		form = NewsletterCreationForm(request.POST, instance=newsletter)

		if form.is_valid():
			newsletter = form.save()
			if newsletter.status == "Published":
				subject = newsletter.subject
				body = newsletter.body
				from_email = settings.EMAIL_HOST_USER

				email_list = newsletter.users.all().values_list('email', flat=True)
				#email_list = newsletter.users.filter(profile__newsletter_reader=True).values_list('email', flat=True)
				for email in email_list:
					send_mail(subject=subject, from_email=from_email, recipient_list=[email], message=body, fail_silently=True)

			return redirect('control_panel:control_newsletter_detail', pk=newsletter.pk)
	else:
		form = NewsletterCreationForm(instance=newsletter)

	context = {
		"form":form,
	}
	template = "./control_panel/control_newsletters.html"
	return render(request, template, context)

def control_newsletter_detail(request, pk ):
	newsletter = get_object_or_404(Newsletter, pk=pk)
	user_list = newsletter.users.all().values_list('username', flat=True)
	context = {
		"newsletter": newsletter,
		"user_list": user_list,		
	}
	template = "./control_panel/control_newsletter_detail.html"
	return render(request, template, context)


def control_newsletter_delete(request, pk):
	newsletter = get_object_or_404(Newsletter, pk=pk)

	if request.method == 'POST':
		form = NewsletterCreationForm(request.POST, instance=newsletter)

		if form.is_valid():
			newsletter.delete()
			return redirect('control_panel:control_newsletter_list')

	else:
		form = NewsletterCreationForm(instance=newsletter)

	context = {
		"form":form,
	}
	template = "./control_panel/control_newsletter_delete.html"
	return render(request, template, context)

def control_newsletter_list(request):
	#newsletters = Newsletter.objects.all()
	newsletters = Newsletter.objects.all().order_by('updated')[::-1]
	paginator = Paginator(newsletters, 10)
	page = request.GET.get('page')

	try:
		items = paginator.page(page)
	except PageNotAnInteger:
		items = paginator.page(1)
	except EmptyPage:
		 items = paginator.page(paginator.num_pages)

	index = items.number - 1
	max_index = len(paginator.page_range)
	start_index = index - 5 if index >= 5 else 0
	end_index = index + 5 if index <= max_index - 5 else max_index
	page_range = paginator.page_range[start_index:end_index]

	context = {
	"items": items,
	"page_range": page_range,
	}

	template = "./control_panel/control_newsletter_list.html"
	return render(request, template, context)
