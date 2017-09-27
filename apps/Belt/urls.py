from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$',views.register),
    url(r'^success$', views.success),
    url(r'^add', views.add),
    url(r'^logout', views.logout),
    url(r'submit', views.submit),
    url(r'show/(?P<id>\d+)$', views.show),
    url(r'join/(?P<id>\d+)$', views.join)

]