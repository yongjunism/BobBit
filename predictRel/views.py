from django.shortcuts import render
from pricePredict.models import Product
import urllib.parse
import requests 

# Create your views here.
def get_news(keyword):
    client_id = 'R5V8X2w9Pkvb5_9XWb1P'
    client_secret = 'EuFmp6rjVk'

    url = 'https://openapi.naver.com/v1/search/news.json' 
    headers = {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret':client_secret} 
    params = {'query':keyword, 'display':3 } 
    r = requests.get(url, params = params, headers = headers)

    j = r.json()
    return j


def predictRelView(request, product):
    product_mat = {
        'ramyun': ['런던 설탕', '런던 소맥', '미국 대두', '미국 팜유', '미국 소맥' ],
        'bob':['쌀 가격'],
        'sauce':['미국 대두', '미국 소맥', '런던 소맥'],
        'egg':['미국 옥수수', '런던 소맥', '미국 소맥', '귀리', '미국 대두박'],
        'ice':['런던 설탕', '미국 설탕', '런던 커피', '미국 커피', ],
        'coffee':['런던 설탕', '미국 설탕', '미국 팜유']
    }

    products = Product.objects.all()
    print(products)
    news = []
    for mat in product_mat[product]:
        news.append([mat, get_news(mat)])
      
    context = {'news':news, 'products':products, 'pName':product}
    
    return render(request, 'predictRel/predictRel.html', context)