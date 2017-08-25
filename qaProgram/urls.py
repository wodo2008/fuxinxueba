from django.conf.urls import url
from qaProgram.migrations import views

urlpatterns = [
    url(r'^smallprogram/getCompanyList',views.get_stu_question_list),


]
