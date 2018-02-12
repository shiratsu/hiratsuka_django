# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from conv_lib import ShotConversationAnalysis
from conv_lib import ShotMakeSentence
from common_lib import util
import json

# import the logging library


# 言語解析
def index(request):

    # Get an instance of a logger

    # 必須チェック
    aryMissing = util.checkRequired(request,['conversation_id','sentence','want_objs','what_ask'])
    
    if len(aryMissing) > 0:
        strMissing = ','.join(aryMissing)
        return HttpResponse("{'error':'"+strMissing+' are required'"}", content_type='application/json; charset=UTF-8')

    anaObj = ShotConversationAnalysis.ShotConversationAnalysis() 
    makeObj = ShotMakeSentence.ShotMakeSentence() 
    
    # 言語解析
    dicAnalytics = anaObj.sentenceAnalysis(request)
    
    # 返却文章作成
    util.log(dicAnalytics)
    dicReturn = makeObj.makeSentence(dicAnalytics,request)
    
    #util.log(dicReturn)

    strJson = json.dumps(dicReturn)    
    return HttpResponse(strJson, content_type='application/json; charset=UTF-8')
