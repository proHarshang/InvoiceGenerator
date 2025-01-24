from django.conf.urls import url
from app import views

urlpatterns = [
    url("login/", views.login_view, name="login"),
    url("index/", views.index_view, name="index"),
]
