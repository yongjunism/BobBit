from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
<<<<<<< HEAD
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
=======
import json

# Create your views here.
def keyboard(request):
    return JsonResponse({
        'type': 'text'
    })
    
@csrf_exempt
def message(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']

    if return_str == '테스트':
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': "테스트 성공입니다."
                    }
                }],
                'quickReplies': [{
                    'label': '처음으로',
                    'action': 'message',
                    'messageText': '처음으로'
                }]
            }
        })
>>>>>>> f9c6558f9c0e69a94b83f0e4d0fedfaff74a111c
