# -*- coding: utf-8 -*-

from .makeSentence import MakeSentence
from common_lib import util

class ShotMakeSentence(MakeSentence):

    # 返却文章を作る 
    def makeSentence(self,dictionary,request):
        
        dicReturn = {'sentence':'','what_ask':''}
        
        # 質問内容
        what_ask = request.POST["what_ask"]

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


        util.log(dicReturn)
        
        return dicReturn

