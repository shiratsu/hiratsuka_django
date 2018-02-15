# -*- coding: utf-8 -*-

from .conversationAnalysis import ConversationAnalysis

class ShotConversationAnalysis(ConversationAnalysis):

    def __init__(self):
        super().__init__()
        self.dicConvAnalytics = {'LOC':'','JOB':'','MONEY':''}

    # 文章解析PG
    def sentenceAnalysis(self,request,dicCache):

        # 解析文を取得
        sentence = request.POST["sentence"]

        # 取得したいもの
        what_ask = request.POST["what_ask"]

        # ループで回して処理をしていく
        if what_ask == 'LOC':
            dicCache['LOC'] = self.getLocate(sentence)
            #self.dicConvAnalytics['LOC'] = dicReturn['LOC'] 
        elif what_ask == 'LOC_CONFIRM':
            dicCache['LOC']['if_true'] = self.getConfirm(sentence)
        
        return dicCache


    # 職種を取得
    def getJobKind(self,sent):
        dicReturn = {'val':'','if_true':'0'}
        return dicReturn

