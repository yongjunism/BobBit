import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import datetime
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
    all_data = pd.read_csv('../csv/product_Crawling_csv/' + product_csv)
    materials_dfs = []

    # materials_csv dataframe화
    for material in materials_csv:
        temp = pd.read_csv('../csv/materirals_Crawling_csv/' + material,
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

        # 과거 데이터 중 NaN제거
        drop_indexs = df.loc[df['m_price0'].isna() == True].index
        df.drop(drop_indexs, inplace=True)
        filename = spec + '_prodata.csv'
        # 경로지정
        df.to_csv('../csv/result_product_csv/'+filename, index=False)

        # 현재까지 데이터로 모델 생성
        # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        # NaN 행 제거
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

        # 모델 저장
        joblib.dump(model_LR, '../model/' + spec + '.pkl')


# 추출하고 싶은 상품 list
spec_list = ['[동서식품]맥심 모카골드 믹스']
# 커피 csv
product_csv = 'price_consumer_coffee.csv'
# 원자재 csv
materials_csv = ['런던 설탕 선물 내역.csv',
                 '런던 커피 선물 내역.csv',
                 '미국 설탕 No.11 선물 내역.csv',
                 '미국 커피 C 선물 내역.csv']


C_to_DB_consumerprice(spec_list, product_csv, materials_csv)
