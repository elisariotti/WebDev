from django.contrib import admin
from .models import Newsletter

class NewsletterAdmin(admin.ModelAdmin):
	list_display = ('subject', 'status', 'created',)

admin.site.register(Newsletter, NewsletterAdmin)
