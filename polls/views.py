from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from hiratsuka_lib import hiratsuka_test

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request):
    hiratsuka_test.test()
    return HttpResponse("Hello, world. it's detail.")

def json(request):
    return HttpResponse("{'name':'hiratsuka','hobby':'badminton'}", content_type='application/json; charset=UTF-8')

