# -*- coding: utf-8 -*-

from .makeSentence import MakeSentence


class ShotMakeSentence(metaclass=ABCMeta):

    # 返却文章を作る 
    def makeSentence(self,dictionary,request):
        
        dicReturn = {'sentence':'','want_objs':dictionary,'what_ask':''}

        # 質問内容
        what_ask = request.GET.get(key="what_ask", default="")

        if what_ask == 'LOC':
            dicReturn['sentence'] = '続いて希望の職種はなんですか'
            dicReturn['what_ask'] = 'JOB'

        return dicReturn

