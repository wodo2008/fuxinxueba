from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^smallprogram/get_stu_question_list',views.get_stu_question_list),


]