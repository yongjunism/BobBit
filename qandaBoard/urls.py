from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'qandaBoard'
urlpatterns = [
        path('qna', views.index, name='index'),
        path('post', views.post, name='post'),
        path('detail/<int:post_id>/', views.detail, name='detail'),
] 