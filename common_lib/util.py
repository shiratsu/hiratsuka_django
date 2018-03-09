# -*- coding: utf-8 -*-
#
# 色々使える便利関数を集めたもの
#
#
import logging
import Mecab

def makeWakatiData(mecab,sentence):

    node = mecab.parse(sentence)

    sentences = []
    for chunk in node.splitlines()[:-1]:
        nodeParts = []
        (surface, feature) = chunk.split('\t')
        sentences.append(surface)
    return sentences

# 必須パラメータ確認
def checkRequired(request,aryRequired):

    aryMissing = []

    for strRequired in aryRequired:

        if request.POST[strRequired] == '':
            aryMissing.append(strRequired)         
    
    return aryMissing


# debug log
def log(messageObj):
    logger = logging.getLogger('command')
    logger.info(messageObj)
