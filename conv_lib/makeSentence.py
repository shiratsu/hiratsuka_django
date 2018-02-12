# -*- coding: utf-8 -*-


from abc import ABCMeta, abstractmethod


class MakeSentence(metaclass=ABCMeta):

    @abstractmethod
    def makeSentence(self,dictionary):
        pass
