from django.urls import path
from . import views

urlpatterns = [
    path('comm/psettings/email/confirm', views.say_hello)
]