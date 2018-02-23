# -*- coding: utf-8 -*-

from .makeSentence import MakeSentence
from common_lib import util

class ShotMakeSentence(MakeSentence):

    # 返却文章を作る 
    def makeSentence(self,dictionary,request):
        
        dicReturn = {'sentence':'','what_ask':''}
        
        # 質問内容
        what_ask = request.POST["what_ask"]
        
        util.log("----dictionary-----")
        util.log(dictionary)
        util.log("----dictionary-----")

        aryNot = []

        for key in ['LOC','JOB','MONEY']:
            util.log("----key-----")
            util.log(key)
            util.log("----key-----")
            if key not in dictionary:
                aryNot.append(key)
            else:
                if dictionary[key]['val'] == '':
                    aryNot.append(key)
                elif dictionary[key]['if_true'] == '0':
                    aryNot.append(key)

        util.log("----aryNot-----")
        util.log(aryNot)
        util.log("----aryNot-----")

        if len(aryNot) > 0:
            for k in aryNot:
                if k == 'LOC':
                    dicReturn = self.makeSentenceLocation(dictionary)        
                elif k == 'JOB':
                    dicReturn = self.makeSentenceJob(dictionary)        
                elif k == 'MONEY':
                    dicReturn = self.makeSentenceMoney(dictionary)        
                break
        else:
            dicReturn = self.makeSentenceConfirm(dictionary)    
        
        util.log(dicReturn)
        
        return dicReturn
    
    # 位置系
    def makeSentenceLocationConfirm(self,dictionary):
        
        dicReturn = {}
        dicReturn['sentence'] = 'それは地名ですか？'
        dicReturn['what_ask'] = 'LOC_CONFIRM'

        return dicReturn

    # 位置系
    def makeSentenceLocation(self,dictionary):
        
        dicReturn = {}
        dicReturn['sentence'] = 'もう一度勤務地からお願いします。'
        dicReturn['what_ask'] = 'LOC'

        return dicReturn
    
    # 職種の文作成
    def makeSentenceJob(self,dictionary):
        
        dicReturn = {}
        dicReturn['sentence'] = '続いて希望の職種はなんですか'
        dicReturn['what_ask'] = 'JOB'

        return dicReturn
    
        
    
    # 給与の文作成
    def makeSentenceMoney(self,dictionary):
        
        dicReturn = {}
        dicReturn['sentence'] = '給与はいくらぐらいを希望されていますか'
        dicReturn['what_ask'] = 'MONEY'
        
        return dicReturn
    
    # 確認の文作成
    def makeSentenceConfirm(self,dictionary):
        
        dicReturn = {}
        dicReturn['sentence'] = """確認させていただきます 
        希望勤務地："""+dictionary['LOC']['val']+""" 
        希望職種："""+dictionary['JOB']['val']+"""
        希望給与："""+dictionary['MONEY']['val']+"""
        こちらでお間違いないでしょうか。"""
        dicReturn['what_ask'] = 'CONFIRM'

        return dicReturn
