from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^smallprogram/get_stu_question_list',views.get_stu_question_list),
    url(r'^smallprogram/get_grad_question_list',views.get_grad_question_list),
    url(r'^smallprogram/get_answer',views.get_answer),
    url(r'^smallprogram/submit_answer',views.submit_answer),
    url(r'^smallprogram/submit_question',views.submit_question),
    url(r'^smallprogram/getGradDetail',views.getGradDetail),

]
