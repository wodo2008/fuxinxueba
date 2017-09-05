from django.conf.urls import url
from . import views
from fuxinxueba import settings


urlpatterns = [
    url(r'^smallprogram/getCompanyList',views.getCompanyList),
    url(r'^smallprogram/getExcAlumniList',views.getExcAlumniList),
    url(r'^smallprogram/getPushPositionList',views.getPushPositionList),
    url(r'^smallprogram/getExcAlumniDetail',views.getExcAlumniDetail),
    url(r'^smallprogram/getPushPositionDetail',views.getPushPositionDetail),
    url(r'^smallprogram/getShakePage',views.getShakePage),
    url( r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.STATIC_ROOT})
]
