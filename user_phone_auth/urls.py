from . import views
urlpatterns = [
    url(r'^userpa/getIdentiCode',views.getIdentiCode),
    url(r'^userpa/submitCode',views.submitCode),
]