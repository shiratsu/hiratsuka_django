# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from django.http import HttpResponse
from conv_lib import ShotConversationAnalysis
from conv_lib import ShotMakeSentence
from common_lib import util
import json
from django.core.cache import cache

# import the logging library


# 言語解析
@csrf_exempt
def index(request):

    # Get an instance of a logger

    #会話IDをキーにcacheにセット
    conversation_id = request.POST['conversation_id']

    #キャッシュから会話を取得
    cacheval = cache.get(conversation_id)
    util.log(cacheval)
    
    dicCache = {}
    if cacheval != None:
        dicCache = json.loads(cacheval)


    # 必須チェック
    aryMissing = util.checkRequired(request,['conversation_id','sentence','what_ask'])
    
    if len(aryMissing) > 0:
        strMissing = ','.join(aryMissing)
        return HttpResponse("{'error':'"+strMissing+' are required'"}", content_type='application/json; charset=UTF-8')

    anaObj = ShotConversationAnalysis.ShotConversationAnalysis() 
    makeObj = ShotMakeSentence.ShotMakeSentence() 
    
    # 

    # 言語解析
    dicCache = anaObj.sentenceAnalysis(request,dicCache)
    
    # 返却文章作成
    util.log(dicCache)
    dicReturn = makeObj.makeSentence(dicCache,request)
    dicCache['what_ask'] = dicReturn['what_ask']
    
    #util.log(dicReturn)

    # mysql cacheに格納
    strJsonCache = json.dumps(dicCache, ensure_ascii=False)    
    util.log(strJsonCache)
    cache.set(conversation_id, strJsonCache,120)

    strJson = json.dumps(dicReturn, ensure_ascii=False)    
    return HttpResponse(strJson, content_type='application/json; charset=UTF-8')
