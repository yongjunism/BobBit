from django.shortcuts import render
import requests 

# Create your views here.
def get_news(keyword):
    client_id = 'R5V8X2w9Pkvb5_9XWb1P'
    client_secret = 'EuFmp6rjVk'

    url = 'https://openapi.naver.com/v1/search/news.json' 
    headers = {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret':client_secret} 
    params = {'query':keyword} 
    r = requests.get(url, params = params, headers = headers)

    j = r.json()
    return j


def predictRelView(request, product):
    product_mat = {
        'ramyun': ['런던 설탕', '런던 소맥', '미국 대두', ]
    }

    news = {}

    for mat in product_mat[product]:
        news['mat'] = get_news(mat)


    return render(request, 'predictRel/predictRel.html', news)