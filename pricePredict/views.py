from operator import mod
from django.shortcuts import render
from .models import Product, Categori
from django.forms.models import model_to_dict
from datetime import date

# Create your views here.


def priceViewbyParam(request, product_id):
    # 오늘 날짜
    today = date.today()

    product = Product.objects.get(pNo=product_id)
    product_dict = model_to_dict(product)
    cNo = product_dict['cKey']
    categori_list = Product.objects.filter(cKey=cNo)

    pd_list = []
    product_info = product_dict

    for item in categori_list:
        pd_list.append({
            'pName': model_to_dict(item)['pName'],
            'pNo': model_to_dict(item)['pNo']
        })

    print(product_dict['cKey'])
    if request.method == 'GET':
        return render(
            request, 'pricePredict/price_page.html',
            {'today': today,
             'pd_list': pd_list,
             'product_info': product_info}
        )
