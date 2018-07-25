from django.contrib import admin

# Register your models here.
from .models import NewsletterUser, Newsletter

class NewsletterAdmin(admin.ModelAdmin):
	list_display = ('email', 'name', 'date_added',)


admin.site.register(NewsletterUser, NewsletterAdmin)

admin.site.register(Newsletter)
