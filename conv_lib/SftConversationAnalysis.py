# -*- coding: utf-8 -*-

from conversationAnalysis import ConversationAnalysis

class SftConversationAnalysis(ConversationAnalysis):


    # 文章解析PG
    def sentenceAnalysis(self,request):

        dicReturn = {}

        # 解析文を取得
        sentence = request.GET.get(key="sentence", default="")

        # 取得したいもの
        wantObjs = request.GET.get(key="want_objs", default="")

        aryObjs = wantObjs.split(',')

        # ループで回して処理をしていく
        for strObj in aryObjs:

            if strObj == 'LOC':
                dicReturn['LOC'] = self.getLocate(sentence)
            elif strObj == 'EMAIL':
                dicReturn['EMAIL'] = self.getEmail(sentence)
            elif strObj == 'PHONE':
                dicReturn['PHONE'] = self.getPhoneNumber(sentence)
        return dicReturn


    # 職種を取得
    def getJobKind(self,sent):
        dicReturn = {'val':'','if_true':False}
        return dicReturn

