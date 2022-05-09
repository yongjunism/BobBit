from django.urls import path
from . import views

app_name = 'mypage'

urlpatterns = [
    path("profile/", views.profile, name='profile'),
    path("changeprofile/", views.ChangeProfileView),
    path('profile/delete/', views.profile_delete_view, name='profile_delete'),
    path('profile/wishlist/', views.product_wishlistView),
]