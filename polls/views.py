from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request):
    return HttpResponse("Hello, world. it's detail.")

def json(request):
    return HttpResponse("{'name':'hiratsuka','hobby':'badminton'}", content_type='application/json; charset=UTF-8')

