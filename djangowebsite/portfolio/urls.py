from django.urls import path
from . import views

urlpatterns = [
    path("portfolio/<str:id>",views.index,name="index"),
    path("form",views.form,name="form"),
]