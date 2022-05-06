from django.urls import path
from . import views

app_name = 'chatbot'

urlpatterns = [
    path('post/', views.chatbot_api, name='chatbot_api'),
]
