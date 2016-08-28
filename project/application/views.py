from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	return render(request, 'content.html', {'msg': 'THIS IS A MESSAGE'})