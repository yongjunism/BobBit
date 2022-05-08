from django.shortcuts import render
# from .models import Product, Categori
# import date
# Create your views here.

def productViewbyParam(request, product_id):
    message = '조영래, 최승훈 에이블러님의 임원면접 합격을 기원합니다'

    # today = date.today()

    if request.method == 'GET':
        return render(
            request, 'productInfo/product_page.html',
            {'msg':message,
            })