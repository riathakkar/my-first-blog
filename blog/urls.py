from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.full-width, name='post_list'),
]
