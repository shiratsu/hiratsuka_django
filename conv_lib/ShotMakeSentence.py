# -*- coding: utf-8 -*-

from .makeSentence import MakeSentence
from common_lib import util

class ShotMakeSentence(MakeSentence):

    # 返却文章を作る 
    def makeSentence(self,dictionary,request):
        
        dicReturn = {'sentence':'','what_ask':''}
        
        # 質問内容
        what_ask = request.POST["what_ask"]

        for check in ['LOC','JOB','MONEY']:
            if dictionary[check]['val'] != '':
                if check == 'LOC':
                    dicReturn = self.makeSentenceLocation(dictionary)        
                elif check == 'JOB'
                    dicReturn = self.makeSentenceJOB(dictionary)        
                elif check == 'Money'
                    dicReturn = self.makeSentenceMoney(dictionary)        
                break

        util.log(dicReturn)
        
        return dicReturn

    # 位置系
    def makeSentenceLocation(self,dicReturn,dictionary):
        
        dicReturn = {}
        if dictionary['LOC']['val'] != '':
            if dictionary['LOC']['if_true'] == '1':
                dicReturn['sentence'] = '続いて希望の職種はなんですか'
                dicReturn['what_ask'] = 'JOB'
            else:
                dicReturn['sentence'] = 'それは地名ですか？'
                dicReturn['what_ask'] = 'LOC_CONFIRM'
                
        else:
            dicReturn['sentence'] = 'すみません、もう一度希望勤務地をお聞かせください。'
            dicReturn['what_ask'] = 'LOC'

        return dicReturn
    
    # 職種の文作成
    def makeSentenceJob(self,dictionary):
        
        dicReturn = {}
        
        if dictionary['JOB']['val'] != '':
            dicReturn['sentence'] = '給与はいくらぐらいを希望されていますか'
            dicReturn['what_ask'] = 'MONEY'
        else:
            dicReturn['sentence'] = 'すみません、職種に関してよくわからなかったので、もう一度お願いします。'
            dicReturn['what_ask'] = 'JOB'

        return dicReturn
    
    # 給与の文作成
    def makeSentenceMoney(self,dictionary):
        
        dicReturn = {}
        
        if dictionary['MONEY']['val'] != '':
            dicReturn['sentence'] = """確認させていただきます 
            希望勤務地："""+dictionary['LOC']['val']+""" 
            希望職種："""+dictionary['JOB']['val']+"""
            希望給与："""+dictionary['MONEY']['val']+"""
            こちらでお間違いないでしょうか。"""
            dicReturn['what_ask'] = 'CONFIRM'
        else:
            dicReturn['sentence'] = 'すみません、給与に関してよくわからなかったので、もう一度お願いします。'
            dicReturn['what_ask'] = 'MONEY'

        return dicReturn
