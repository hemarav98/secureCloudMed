from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("doctor", views.indexdoctor, name="indexdoctor"),
    path("loginview", views.loginview, name="loginview"),
    path("login", views.login, name="loginuser"),
    path("registerview", views.registerview, name="registerview"),
    path("register", views.register, name="registeruser"),
    path("bookappointment", views.bookappointment, name="bookappointment"),
    #path("appointment/add/", views.appointment_add, name='add-appointment')
]
