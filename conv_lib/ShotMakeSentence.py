# -*- coding: utf-8 -*-

from .makeSentence import MakeSentence
from common_lib import util

class ShotMakeSentence(MakeSentence):

    # 返却文章を作る 
    def makeSentence(self,dictionary,request):
        
        dicReturn = {'sentence':'','what_ask':''}
        
        # 質問内容
        what_ask = request.POST["what_ask"]
        util.log("what_ask------------------------")
        util.log(what_ask)

        if what_ask == 'LOC':
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
        elif what_ask == 'LOC_CONFIRM' and dictionary['LOC']['if_true'] == '1':
            dicReturn['sentence'] = '続いて希望の職種はなんですか'
            dicReturn['what_ask'] = 'JOB'
        
        elif what_ask == 'JOB' and dictionary['JOB']['val'] != '':  
            dicReturn['sentence'] = '給与はいくらぐらいを希望されていますか'
            dicReturn['what_ask'] = 'MONEY'

        elif what_ask == 'MONEY' and dictionary['MONEY']['val'] != '':  
            dicReturn['sentence'] = """確認させていただきます 
            希望勤務地："""+dictionary['LOC']['val']+""" 
            希望職種："""+dictionary['JOB']['val']+"""
            希望給与："""+dictionary['MONEY']['val']+"""
            こちらでお間違いないでしょうか。"""
            dicReturn['what_ask'] = 'CONFIRM'


        util.log(dicReturn)
        
        return dicReturn

