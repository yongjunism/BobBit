from django.urls import path
from . import views

app_name = 'bbadmin'

urlpatterns = [
    path('', views.load_adpage, name='adpage'),
    path('post', views.Crawlingdata_to_DB, name='crawl_DB'),
]
