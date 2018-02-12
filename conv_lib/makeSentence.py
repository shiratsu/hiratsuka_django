# -*- coding: utf-8 -*-


from abc import ABCMeta, abstractmethod


class MakeSentence(metaclass=ABCMeta):

    # 初期化
    def __init__(self):

    
    @abstractmethod
    def makeSentence(self,dictionary):
        pass
