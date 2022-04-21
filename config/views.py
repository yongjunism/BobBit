from multiprocessing import context
from django.shortcuts import render
from django.views.generic.base import TemplateView
from pricePredict.models import Product
from django.forms.models import model_to_dict
# Create your views here.


# class HomeView(TemplateView):
#     template_name = "home.html"

def HomeView(request):
    s_list = Product.objects.all().values_list('pName')
    search_list = []
    for search_item in range (len(s_list)):
        search_list.append(Product.objects.all().values_list('pName')[search_item])
    return render(request,'home.html',{'search_list': search_list})