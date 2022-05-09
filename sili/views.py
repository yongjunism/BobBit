from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt


#############################
import socket
host = "127.0.0.1"  # 챗봇 엔진 서버 IP 주소
port = 5050  # 챗봇 엔진 서버 통신 포트
#############################


@csrf_exempt
def get_response(request):
	response = {'status': None}

	if request.method == 'POST':
		mySocket = socket.socket()
		mySocket.connect((host, port))
		data = json.loads(request.body)
		query = data['message']
		json_data = {
        'Query': query,
        'BotType': "MyService"
    	}
		message = json.dumps(json_data)
		mySocket.send(message.encode())

		# 챗봇 엔진 답변 출력
		data = mySocket.recv(2048).decode()
		ret_data = json.loads(data)	
		response['message'] = {'text': ret_data["Answer"], 'user': False, 'chat_bot': True}
		response['status'] = 'ok'

	else:
		response['error'] = 'no post data found'

	return HttpResponse(
		json.dumps(response),
			content_type="application/json"
		)


def home(request):
	context = {'title': 'Bobbot'}
	return render(request,'sili.html', context)
