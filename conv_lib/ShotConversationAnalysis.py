# -*- coding: utf-8 -*-

from .conversationAnalysis import ConversationAnalysis

class ShotConversationAnalysis(ConversationAnalysis):

    def __init__(self):
        super().__init__()
        self.dicConvAnalytics = {'LOC':'','JOB':'','MONEY':''}

    # 文章解析PG
    def sentenceAnalysis(self,request):

        dicReturn = {}

        # 解析文を取得
        sentence = request.GET.get(key="sentence", default="")

        # 取得したいもの
        what_ask = request.GET.get(key="what_ask", default="")

        # ループで回して処理をしていく
        if what_ask == 'LOC':
            dicReturn['LOC'] = self.getLocate(sentence)
            self.dicConvAnalytics['LOC'] = dicReturn['LOC'] 
        
        return dicReturn


    # 職種を取得
    def getJobKind(self,sent):
        dicReturn = {'val':'','if_true':'0'}
        return dicReturn

