# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from conv_lib import ShotConversationAnalysis
import json

# 言語解析
def shot(request):
    convObj = ShotConversationAnalysis() 
    dicReturn = convObj.sentenceAnalysis(request)
    
    strJson = json.dumps(dict)    

    return HttpResponse(strJson, content_type='application/json; charset=UTF-8')
