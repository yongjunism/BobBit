from django.urls import path
from . import views


urlpatterns = [
    path("create_profile/", views.RegisterProfileView),
    path("pointup/", views.pointUp),
]
