from django.conf.urls import url, include
from django.contrib import admin
# from django.urls import path

from mall_test.apps.users import views

urlpatterns = [
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
]
