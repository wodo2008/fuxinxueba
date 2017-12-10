from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'smallprogram/saveuserinfo',views.save_user_info),
    url(r'smallprogram/saveansinfo',views.save_ans_info),
]