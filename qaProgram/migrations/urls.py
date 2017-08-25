from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^qaProgram/getCompanyList',views.getCompanyList),
    url(r'^qaProgram/getExcAlumniList',views.getExcAlumniList),
    url(r'^qaProgram/getPushPositionList',views.getPushPositionList),
    url(r'^qaProgram/getExcAlumniDetail',views.getExcAlumniDetail),
    url(r'^qaProgram/getPushPositionDetail',views.getPushPositionDetail),
]
