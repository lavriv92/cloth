from django.conf.urls import patterns, url

from .views import HomeView, ClothersView, ContactsView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^clothers/$', ClothersView.as_view(), name='clothers'),
    url(r'^contacts/$', ContactsView.as_view(), name='contacts'),
)
