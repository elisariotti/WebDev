from django.contrib import admin

# Register your models here.
from .models import NewsletterUser

class NewsletterAdmin(admin.ModelAdmin):
	list_display = ('email', 'name', 'date_added',)

admin.site.register(NewsletterUser, NewsletterAdmin)
