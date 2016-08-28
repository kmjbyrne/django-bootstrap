from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/message/(?P<msg>(\w+))$', views.add_new_message, name='add_new_message'),
 ]