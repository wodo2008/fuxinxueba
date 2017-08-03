from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^getCompanyList',views.getCompanyList),
    url(r'^getExcAlumniList',views.getExcAlumniList),
    url(r'^getPushPositionList',views.getPushPositionList),
    url(r'^getExcAlumniDetail',views.getExcAlumniDetail),
    url(r'^getPushPositionDetail',views.getPushPositionDetail),
]