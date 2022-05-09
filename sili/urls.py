from django.urls import path
from . import views
# from sili.views import home, get_response
app_name = 'sili'


urlpatterns = [
    path('', views.home,name='home'),
    path('get-response/', views.get_response,name='get_response'),
]
