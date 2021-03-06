# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import MeCab
import re

class ConversationAnalysis(metaclass=ABCMeta):

    def __init__(self):
        self.mecab = MeCab.Tagger ('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
        self.mecab.parse('')


    @abstractmethod
    def sentenceAnalysis(self,sent,dicCache):
        pass

    # 文章から人名を取得(mecabで解析して取得する。)
    # katakanaで入れられた場合は、今のところ判定不可
    def getPerson(self,sent):
        dicReturn = {'val':'','if_true':'0'}
        node = self.mecab.parse(sent)
        aryName = []
        strName = ''
        for chunk in node.splitlines()[:-1]:
            (surface, feature) = chunk.split('\t')
            #品詞を取得
            features = feature.split(",")
            pos1 = features[0]
            pos2 = features[1]
            pos3 = features[2]
            if pos1 == '名詞' and pos2 == '固有名詞' and pos3 == '人名':
                #単語を取得
                strName = surface
                break
        
        dicReturn['val'] = strName
        dicReturn['if_true'] = '1'
            
        return dicReturn


#    @abstractmethod
#    def getDate(self,sent):
#        pass
#
#    @abstractmethod
#    def getTime(self,sent):
#        pass

    # 正規表現を使ってメアドのパターンを取得
    def getEmail(self,sent):
        dicReturn = {'val':'','if_true':'0'}
        strPattern = '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]+'
        objRe = re.compile(strPattern)
        m = objRe.match(sent)
        
        if m:
            self.checkRegex(m)
        
        return dicReturn
    
    # 電話番号を取得
    # 電話番号は複数パターンある
    def getPhoneNumber(self,sent):
        dicReturn = {'val':'','if_true':'0'}
        
        strPattern1 = '^\d{10}$|^\d{11}$'
        objRe1 = re.compile(strPattern1)
        m1 = objRe1.match(sent)
        
        if m1:
            self.checkRegex(m1)

        else:
            strPattern2 = '^\d{2,4}-\d{2,4}-\d{4}$'
            objRe2 = re.compile(strPattern2)
            m2 = objRe2.match(sent)

            if m2:
                self.checkRegex(m2)
            
        return dicReturn

    

    # 地名
    # ベースは形態素解析で良い気がする
    def getLocate(self,sent):
        strLoc = ''
        dicReturn = {'val':'','if_true':'0'}
        aryIfTrue = []
        aryName = []
        node = self.mecab.parse(sent)
        for chunk in node.splitlines()[:-1]:
            (surface, feature) = chunk.split('\t')
            #品詞を取得
            features = feature.split(",")
            pos1 = features[0]
            pos2 = features[1]
            pos3 = features[2]
            if pos1 == '名詞' and pos2 == '固有名詞' and pos3 in [ '地域','一般','組織']:
                #単語を取得
                word = surface
                aryName.append(word)

                if pos3 == '地域':
                    aryIfTrue.append('True')
                elif pos3 == '一般':    
                    aryIfTrue.append('True')
                elif pos3 == '組織':    
                    aryIfTrue.append('False')
            else:
                continue
            
        strLoc = ''.join(aryName)
        dicReturn['val'] = strLoc
        dicReturn['if_true'] = 'False' not in aryIfTrue
        dicReturn['if_true'] = '1' if 'False' not in aryIfTrue  else '0'

        return dicReturn

#    @abstractmethod
#    def getDeny(self,sent):
#        pass

    # 名詞と動詞を取り出す
    def getNounVerb(self,sent):

        aryFeatures = []

        node = self.mecab.parse(sent)
        for chunk in node.splitlines()[:-1]:
            (surface, feature) = chunk.split('\t')
            #品詞を取得
            features = feature.split(",")
            features.insert(surface)
            pos = features[1]
            if pos in [ '名詞','動詞' ]:
                aryFeatures.append(features)
        return aryFeatures

    # 形態素解析の情報から固有表現を取り出す
    def getNERByKeitaiSokaiseki(self,aryFeatures):

        aryLoc = []
        aryName = []
        dicReturn = {'val':'','if_true':'0'}
        aryIfTrueLoc = []

        for features in aryFeatures:
            #品詞を取得
            word = features[0]
            pos2 = features[2]
            pos3 = features[3]
            if pos2 == '固有名詞' and pos3 in [ '地域','一般','組織']:
                #単語を取得
                word = surface
                aryLoc.append(word)

                if pos3 == '地域':
                    aryIfTrueLoc.append('True')
                elif pos3 == '一般':    
                    aryIfTrueLoc.append('False')
                elif pos3 == '組織':    
                    aryIfTrueLoc.append('False')
            elif pos1 == '名詞' and pos2 == '固有名詞' and pos3 == '人名':
                #単語を取得
                aryName.append(word)
                continue
        
        strLoc = ''.join(aryLoc)
        strName = ''.join(aryName)
        dicReturn['PSN']['val'] = strName
        dicReturn['LOC']['val'] = strLoc
        dicReturn['LOC']['if_true'] = '1' if 'False' not in aryIfTrueLoc  else '0'



        return dicReturn

    # 確認を行う
    def getConfirm(self,sent):
        aryYes = ['はい','そうです','OK','YES','合ってます','あってます','間違いない']

        strReturn = '0'

        node = self.mecab.parse(sent)
        for chunk in node.splitlines()[:-1]:
            (surface, feature) = chunk.split('\t')
            
            if surface in aryYes:
                strReturn = '1'

        return strReturn



    # マッチオブジェクトから、必要なもの取り出す
    def checkRegex(self,match):
        
        strVal = match.group()
        dicReturn['val'] = strVal
        dicReturn['if_true'] = '1'

        return dicReturn

