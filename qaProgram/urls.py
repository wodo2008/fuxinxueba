from django.conf.urls import url
from qaProgram.migrations import views

urlpatterns = [
    url(r'^qaProgram/getCompanyList',views.get_stu_question_list),
    

]
