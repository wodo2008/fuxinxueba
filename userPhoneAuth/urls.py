from userPhoneAuth import views
from django.conf.urls import url
from django.conf.urls import url

from userPhoneAuth import views

urlpatterns = [
    url(r'^userpa/getIdentiCode', views.getIdentiCode),
    url(r'^userpa/submitCode', views.submitCode),
    url(r'^userpa/index', views.index),
]