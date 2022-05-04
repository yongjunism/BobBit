from django.urls import path
from . import views

app_name = 'productInfo'

urlpatterns = [
    path('<int:product_id>/', views.productViewbyParam, name='product_page'),
]
