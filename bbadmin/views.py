from bbuser.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict
from pricePredict.models import Product
import glob


import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib


def df_formatting(df):
    # 4개월 전으로 shift
    df['종가'] = df['종가'].shift(-4)
    drop_indexs = df.loc[df['종가'].isna() == True].index
    df.drop(drop_indexs, inplace=True)

    # formatting
    df['날짜'] = pd.to_datetime(df['날짜'], format='%Y년 %m월')
    if(df['종가'].dtypes != 'float64'):
        df['종가'] = df['종가'].str.replace(",", '')
    df['변동 %'] = df['변동 %'].str.replace("%", '')

    df = df.astype({'종가': 'float', '변동 %': 'float'})
    return df


def C_to_DB_consumerprice(spec_list, product_csv, materials_csv):
    all_data = pd.read_csv('./static/csv/product_Crawling_csv/' + product_csv)
    materials_dfs = []

    # materials_csv dataframe화
    for material in materials_csv:
        temp = pd.read_csv('./static/csv/materirals_Crawling_csv/' + material,
                           usecols=['날짜', '종가', '변동 %'])
        materials_dfs.append(df_formatting(temp))

    for spec in spec_list:
        df = all_data.loc[all_data['제품명'] == spec]
        # price 안나와있는 값 제거
        drop_index = df.loc[df['price'] == '-'].index
        df.drop(drop_index, inplace=True)
        # 날짜 colume 정규화
        df['날짜'] = pd.to_datetime(df['날짜'], format='%Y년 %m월')
        # 날짜 순 정렬
        df.sort_values(by='날짜', inplace=True, ignore_index=True)
        # price 전처리
        df['price'] = df['price'].str.replace(",", '')
        df = df.astype({'price': 'int'})
        # next_price(Target) 생성
        df['next_price'] = df['price'].shift(-1)

        # material이랑 product랑 합치는부분
        count = 0
        for material in materials_dfs:
            df = df.join(material.set_index('날짜'), on='날짜')
            df.rename(columns={'종가': 'm_price' + str(count),
                               '변동 %': 'm_per' + str(count)}, inplace=True)
            count += 1
        print(df)

        # 과거 데이터 중 NaN제거
        drop_indexs = df.loc[df['m_price0'].isna() == True].index
        df.drop(drop_indexs, inplace=True)
        filename = spec + '_prodata.csv'
        # 경로지정
        df.to_csv('./static/csv/result_product_csv/'+filename, index=False)

        # 현재 가격
        now_price = df['price'].array[-1]
        # 데이터 옮기기
        now_data = df.drop(columns=['제품명', '날짜', 'next_price'], axis=1)

        # 현재까지 데이터로 모델 생성
        # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        # 현재 날짜 제거
        drop_indexs = df.loc[df['next_price'].isna() == True].index
        df.drop(drop_indexs, inplace=True)

        # 날짜,이름 제거
        df.drop(columns=['날짜', '제품명'], axis=1, inplace=True)

        x = df.drop('next_price', axis=1)
        y = df['next_price']

        x_train, x_test = x[:int(len(x)*(70/100))], x[int(len(x)*(70/100)):]
        y_train, y_test = y[:int(len(y)*(70/100))], y[int(len(y)*(70/100)):]

        model_LR = LinearRegression()
        model_LR.fit(x, y)

        pred = model_LR.predict(now_data)
        # 마지막 예측가
        next_price = pred[-1]

        # 성능 평가용도
        test_model_LR = LinearRegression()
        test_model_LR.fit(x_train, y_train)
        y_pred = test_model_LR.predict(x_test)

        # RMSE
        RMSE = mean_squared_error(y_test, y_pred)**0.5

        # Product DB 저장
        product = get_object_or_404(Product, pName=spec)
        product.price = now_price
        product.nextprice = next_price
        product.RMSE = RMSE
        product.save()

        # 모델 저장
        joblib.dump(model_LR, './static/model/' + spec + '.pkl')


def load_adpage(request):
    # 어드민 검증
    User = get_user_model()
    user = get_object_or_404(User, username=request.user)
    user = model_to_dict(user)
    if(user['username'] != 'admin'):
        return redirect('home')
    else:
        # 어드민일때

        # 원자재 list
        material_list = []
        # 가공품 File list
        product_list = []
        # product 이름들
        pName_list = []

        m_path = "./static/csv/materirals_Crawling_csv/*"
        p_path = "./static/csv/product_Crawling_csv/*"

        products = Product.objects.all().values('pName')
        for p in products:
            # temp = model_to_dict(p)
            pName_list.append(p['pName'])

        for f in glob.glob(m_path):
            f = f.split("\\")[1]
            material_list.append(f)

        for f in glob.glob(p_path):
            f = f.split("\\")[1]
            product_list.append(f)

        return render(request, 'bbadmin/adminpage.html',
                      {'material_list': material_list,
                       'product_list': product_list,
                       'pName_list': pName_list})


def Crawlingdata_to_DB(request):
    # form 처리
    try:
        if request.method == 'POST':
            postdict = dict(request.POST)
            # 추출하고 싶은 상품 list
            spec_list = postdict['product_name']
            # 커피 csv
            product_csv = postdict['product_csv'][0]
            # 원자재 csv
            materials_csv = postdict['material']

            C_to_DB_consumerprice(spec_list, product_csv, materials_csv)

            return redirect('bbadmin:adpage')

    except Exception as e:
        return JsonResponse({'content': str(e)}, safe=False)
