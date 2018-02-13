# -*- coding: utf-8 -*-
#
# 色々使える便利関数を集めたもの
#
#
import logging


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
