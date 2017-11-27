from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^userpa/getIdentiCode',views.getIdentiCode),
    url(r'^userpa/submitCode',views.submitCode),
    url(r'^userpa/index',views.index),
]