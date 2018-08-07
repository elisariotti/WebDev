from django.contrib import admin

# Register your models here.
from .models import Newsletter

class NewsletterAdmin(admin.ModelAdmin):
	list_display = ('subject', 'status', 'created',)

admin.site.register(Newsletter, NewsletterAdmin)
