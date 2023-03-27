from django.urls import path
from . import views

urlpatterns = [
    path("portfolio/<str:id>",views.index,name="index"),
    path("form/",views.confirmation,name="form_confirm"),
    path("form/<int:port>/<int:review>/<int:event>",views.form,name="form"),
    path("user/register/", views.register, name="register"),
    path("user/login/",views.login, name="login"),
    path("user/profile/", views.profile, name="profile"),
    path("", views.home, name="home"),
]