from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from application.business.string_ops import *
import json


def index(request):
	return render(request, 'content.html', {'msg': 'THIS IS A MESSAGE'})


def add_new_message(request, msg):
	print(str(msg))
	response = {
		'status': 200,
		'message': 'Successfully added message - {}'.format(msg)
	}
	#json.dumps(response), 
	return HttpResponse(request.path)