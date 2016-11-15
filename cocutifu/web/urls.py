from django.conf.urls import include, url
from django.views.generic import TemplateView
from web.views import * 

urlpatterns = [
	url(r'^$', HomeView.as_view(), name='home'),
	url(r'^post/(?P<slug>[-\w]+)/$', PostView.as_view(), name='post'),
	url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
]
