from django.conf.urls import url
from newsletters.views import control_newsletters, control_newsletter_list, control_newsletter_detail, control_newsletter_edit, control_newsletter_delete

urlpatterns = [
	url(r'^admin/', control_newsletter_list, name='control_newsletter_list'),
	url(r'^add/$', control_newsletters, name='control_newsletters'),
	url(r'^detail/(?P<pk>\d+)/$', control_newsletter_detail, name='control_newsletter_detail'),
	url(r'^edit/(?P<pk>\d+)/$', control_newsletter_edit, name='control_newsletter_edit'),
	url(r'^delete/(?P<pk>\d+)/$', control_newsletter_delete, name='control_newsletter_delete'),
]
