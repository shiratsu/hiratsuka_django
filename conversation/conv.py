# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from conv_lib import ShotConversationAnalysis
from conv_lib import ShotMakeSentence
import json

# 必須パラメータ確認
def checkRequired(request):

    return True

# 言語解析
def shot(request):
    anaObj = ShotConversationAnalysis.ShotConversationAnalysis() 
    makeObj = ShotMakeSentence.ShotMakeSentence() 
    
    # 言語解析
    dicAnalytics = anaObj.sentenceAnalysis(request)
    
    # 返却文章作成
    dicReturn = makeObj.makeSentence
    (dicAnalytics,request)
    
    strJson = json.dumps(dicReturn)    
    return HttpResponse(strJson, content_type='application/json; charset=UTF-8')
