from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.TestView.as_view()),
    path("create_profile/", views.RegisterProfileView),
    path("pointup/", views.pointUp),
]
