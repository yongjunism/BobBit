from django.urls import path
from . import views
<<<<<<< HEAD

app_name = 'chatbot'

urlpatterns = [
    path('post/', views.chatbot_api, name='chatbot_api'),
]
=======
from django.conf import settings
from django.conf.urls.static import static


app_name = 'chatbot'
urlpatterns = [
        path('', views.keyboard),
        path('message', views.message),
] 
>>>>>>> f9c6558f9c0e69a94b83f0e4d0fedfaff74a111c
