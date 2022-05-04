from django.shortcuts import render

# Create your views here.

def productViewbyParam(request, product_id):
    message = '임원 면접 합격을 기원합니다'
    if request.method == 'GET':
        return render(
            request, 'productInfo/product_page.html',
            {'msg':message,
            })