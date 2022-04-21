from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile),
    path('profile/delete/', views.profile_delete_view, name='profile_delete'),
]