"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", views.HomeView, name="home"),
    path("user/", include("bbuser.urls")),
    path("price/", include("pricePredict.urls"), name="price"),
    path("mypage/", include("mypage.urls")),
    path("", include("qandaBoard.urls")),
    path("rank/", include("rank.urls")),
    path("adminpg/", include("bbadmin.urls")),
    path("chatbot/", include("chatbot.urls")),
    path("info/", include("productInfo.urls"), name="info"),
    path("predictrel/", include("predictRel.urls")),
    path("modal_check/", views.modal_check)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
