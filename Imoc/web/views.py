from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
import json


# Create your views here.
def login(request):
	return render_to_response('login.html')


def jump(request):
	result = {}
	username = request.POST.get('username')
	password = request.POST.get('password')
	result['user'] = username
	result['pwd'] = password
	result = json.dumps(result)
	if request.method == 'POST':
		return HttpResponse(result, content_type='application/json;charset=utf-8')
	else:
		return HttpResponse('无返回结果')
