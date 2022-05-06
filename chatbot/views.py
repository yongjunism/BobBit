from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
# Create your views here.


@method_decorator(csrf_exempt)
def chatbot_api(request):
    # form 처리
    try:
        if request.method == 'POST':
            body = json.loads(request.body.decode('utf-8'))
            print(body)
            return JsonResponse({'message': 'SUCCESS'})

    except Exception as e:
        return JsonResponse({'content': str(e)}, safe=False)
