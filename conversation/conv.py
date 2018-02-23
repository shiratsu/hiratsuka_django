# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from conv_lib import ShotConversationAnalysis
from conv_lib import ShotMakeSentence
from common_lib import util
import json


# 言語解析
def shot(request):

    # 必須チェック
    aryMissing = util.checkRequired(request,['conversation_id','sentence','want_objs','what_ask'])
    
    if aryMissing.count > 0:
        strMissing = ','.join(aryMissing)
        return HttpResponse("{'error':'"+strMissing+' are required'"}", content_type='application/json; charset=UTF-8')

    anaObj = ShotConversationAnalysis.ShotConversationAnalysis() 
    makeObj = ShotMakeSentence.ShotMakeSentence() 
    
    # 言語解析
    dicAnalytics = anaObj.sentenceAnalysis(request)
    
    # 返却文章作成
    dicReturn = makeObj.makeSentence(dicAnalytics,request)
    
    strJson = json.dumps(dicReturn)    
    return HttpResponse(strJson, content_type='application/json; charset=UTF-8')
