from operator import mod
from django.shortcuts import render
from .models import Product, Categori
from django.forms.models import model_to_dict
from datetime import date
from .categori_to_emoji import EMOJI
import pandas as pd
import joblib

# Create your views here.


def priceViewbyParam(request, product_id):
    # 오늘 날짜
    today = date.today()
    lastmonth = today.month

    product = Product.objects.get(pNo=product_id)
    product_dict = model_to_dict(product)
    cNo = product_dict['cKey']

    # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    # 데이터 불러오기
    pd_data = pd.read_csv(
        'static/csv/result_product_csv/' + product_dict['pName'] + '_prodata.csv')

    # 모델 불러오기
    model = joblib.load('static/model/'+product_dict['pName']+'.pkl')
    # 마지막 행 가져와서 예측
    last_idx = pd_data.index[-1]

    now_data = pd_data.drop(
        columns=['제품명', '날짜', 'next_price'], axis=1)

    pd_data = pd_data[['날짜', 'price']]
    pd_data.rename(columns={'날짜': 'date', 'price': 'value'}, inplace=True)
    pd_data = pd_data.to_json(orient='records')

    pred = model.predict(now_data)
    # 마지막 예측가
    next_price = pred[-1]

    print(pd_data)
    # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    categori_list = Product.objects.filter(cKey=cNo)

    pd_list = []
    product_info = product_dict

    for item in categori_list:
        pd_list.append({
            'pName': model_to_dict(item)['pName'],
            'pNo': model_to_dict(item)['pNo'],
            'price': model_to_dict(item)['price']
        })

    if request.method == 'GET':
        return render(
            request, 'pricePredict/price_page.html',
            {'today': today,  # 오늘 날짜
             'pd_list': pd_list,
             'lastmonth': lastmonth,
             'icon': EMOJI[cNo],
             'product_info': product_info,  # 해당 상품의 db 데이터
             'pd_data': pd_data,        # 해당 상품의 지금까지 csv데이터
             'next_price': next_price}  # 다음달 상품 가격
        )
