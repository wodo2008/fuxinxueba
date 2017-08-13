from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^smallprogram/getCompanyList',views.getCompanyList),
    url(r'^smallprogram/getExcAlumniList',views.getExcAlumniList),
    url(r'^smallprogram/getPushPositionList',views.getPushPositionList),
    url(r'^smallprogram/getExcAlumniDetail',views.getExcAlumniDetail),
    url(r'^smallprogram/getPushPositionDetail',views.getPushPositionDetail),
]
