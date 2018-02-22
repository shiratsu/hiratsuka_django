# -*- coding: utf-8 -*-

from .conversationAnalysis import ConversationAnalysis
from common_lib import convert_kansuuji
from common_lib import convert_for_crf
from common_lib import util
import pycrfsuite


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
        
        # 暫定のため、あまり作り込んでない
        elif what_ask == 'JOB':
            dicCache['JOB'] = self.getJobKind(sentence)
        
        # 給与
        elif what_ask == 'MONEY':
            dicCache['MONEY'] = self.getMoneyInfo(sentence)
        
        return dicCache


    # 職種を取得
    def getJobKind(self,sent):
        dicReturn = {'val':'','if_true':'0'}
        
        strName = ''
        node = self.mecab.parse(sent)
        for chunk in node.splitlines()[:-1]:
            (surface, feature) = chunk.split('\t')
            #品詞を取得
            features = feature.split(",")
            pos1 = features[0]
            if pos1 == '名詞':
                #単語を取得
                strName = surface
                break

        if strName != '':
            dicReturn['val'] = strName
            dicReturn['if_true'] = '1'

        return dicReturn

    # 給与の情報を取得
    def getMoneyInfo(self,sent):

        dicReturn = {'val':'','if_true':'0'}

        # オブジェクトを初期化
        tagger = pycrfsuite.Tagger()
        tagger.open('money_model.crfsuite')
       
        # 漢数字をアラビア数字に
        sent = convert_kansuuji.kansuji2arabic(sent)

        # 形態素解析しやすいように変換する
        sent = convert_for_crf.convertText(sent)

        # CRFモデルで解析するために変換する
        crfsent = convert_for_crf.text2sent(sent)

        #分かち書きリストと予測固有表現を取得
        tokenlist = convert_for_crf.sent2tokens(crfsent)
        predictlist = tagger.tag(convert_for_crf.sent2features(crfsent))

        # 給与の情報を取り出す
        strResult = self.getExtractInfo(tokenlist,predictlist,['B-MNYUNIT','B-MONEY','I-MONEY'])

        if strResult is not None:
            dicReturn['val'] = strResult
            dicReturn['if_true'] = '1'

        return dicReturn

    # CRFの結果から、自分の必要なものを抜き出す処理    
    def getExtractInfo(self,tokenlist,predictlist,aryWantExtract):
        strResult = ''
        i = 0
        aryInfo = []
        aryPredict = []

        util.log("----------------------")
        util.log(tokenlist)
        util.log(predictlist)
        util.log("----------------------")


        for i,p in enumerate(predictlist):
            
            # 抜き出した情報が、ほしいものの中にあるか
            if p in aryWantExtract:
                if tokenlist[i] != 'は':
                    aryInfo.append(tokenlist[i])

                aryPredict.append(p)
        
        # aryInfoに中身が入っていれば、結果を作成
        if len(aryInfo) > 0  \
            and 'B-MNYUNIT' in aryPredict \
            and 'B-MONEY' in aryPredict: 
            strResult = ''.join(aryInfo)

        return strResult
