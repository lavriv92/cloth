from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^clojures/$', views.clojures, name='clojures'),
    url(r'^contacts/$', views.contacts, name='contacts'),
)
