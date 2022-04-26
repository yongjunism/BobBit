from django.urls import path
from . import views

app_name = 'pricePredict'

urlpatterns = [
    path('<int:product_id>/', views.priceViewbyParam, name='price_page'),
    path('<int:product_id>/wish/', views.product_wish, name='product_wish'),
]
