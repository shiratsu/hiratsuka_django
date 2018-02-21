# -*- coding: utf-8 -*-
#
# CRFモデルで解析しやすいようにテキストをコンバートする
#
#
import MeCab
import re

# 形態素解析して、CRFモデルで読み込めるように変換
def text2sent(text):
    sent =[]
    m = MeCab.Tagger ("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
    tokens = [re.split("[\t,]",line) for line in m.parse(text).split('\n')]
    print(tokens)
    #print(text)
    for i in range(len(tokens)-2):
        token = tokens[i][0]
        p1 = "*"
        p2 = "*"
        p3 = "*"
        p4 = "*"
        f1='*'
        f2='*'
        #print("--------------")
        #print(len(tokens[i]))
        #print(token)
        #print(tokens[i])
        #print("--------------")
        if len(tokens[i])<=3:
            p1 = "*"
            p2 = "*"
            p3 = "*"
            p4 = "*"
        else:
            part = tokens[i][3].split('-')
            p1 = part[0]
            if len(part) == 2:
                p2 = part[1]
                p3 = "*"
                p4 = "*"
            if len(part) == 3:
                p2 = part[1]
                p3 = part[2]
                p4 = "*"
            elif len(part) == 4:
                p2 = part[1]
                p3 = part[2]
                p4 = part[3]
            else:
                p2 = "*"
                p3 = "*"
                p4 = "*"
            form = [tokens[i][4],tokens[i][5]]
            if form[0]=='':
                f1='*'
                f2='*'
            else:
                f1 = form[0]
                f2 = form[1]
        if len(tokens[i]) > 1:
            sent.append([token,p1,p2,p3,p4,f1,f2,tokens[i][2],tokens[i][1],tokens[i][1]])
    return sent

# テキストを形態素解析で分割しやすいように変換する
def convertText(text):

    #適当にtextを綺麗にする。
    text = text.replace("\u3000","。")
    text = re.sub('[^(a-zA-Z0-9ぁ-んァ-ン一-龥 。ー)]',"",text)
    text = text.replace('br','。')
    return text

def is_hiragana(ch):
    return 0x3040 <= ord(ch) <= 0x309F

def is_katakana(ch):
    return 0x30A0 <= ord(ch) <= 0x30FF

def get_character_type(ch):
    if ch.isspace():
        return 'ZSPACE'
    elif ch.isdigit():
        return 'ZDIGIT'
    elif ch.islower():
        return 'ZLLET'
    elif ch.isupper():
        return 'ZULET'
    elif is_hiragana(ch):
        return 'HIRAG'
    elif is_katakana(ch):
        return 'KATAK'
    else:
        return 'OTHER'

def get_character_types(string):
    character_types = map(get_character_type, string)
    character_types_str = '-'.join(sorted(set(character_types)))

    return character_types_str

def extract_pos_with_subtype(morph):
    idx = morph.index('*')

    return '-'.join(morph[1:idx])

def word2features(sent, i):
    word = sent[i][0]
    chtype = get_character_types(sent[i][0])
    postag = extract_pos_with_subtype(sent[i])
    features = [
        'bias',
        'word=' + word,
        'type=' + chtype,
        'postag=' + postag,
    ]
    if i >= 2:
        word2 = sent[i-2][0]
        chtype2 = get_character_types(sent[i-2][0])
        postag2 = extract_pos_with_subtype(sent[i-2])
        iobtag2 = sent[i-2][-1]
        features.extend([
            '-2:word=' + word2,
            '-2:type=' + chtype2,
            '-2:postag=' + postag2,
            '-2:iobtag=' + iobtag2,
        ])
    else:
        features.append('BOS')

    if i >= 1:
        word1 = sent[i-1][0]
        chtype1 = get_character_types(sent[i-1][0])
        postag1 = extract_pos_with_subtype(sent[i-1])
        iobtag1 = sent[i-1][-1]
        features.extend([
            '-1:word=' + word1,
            '-1:type=' + chtype1,
            '-1:postag=' + postag1,
            '-1:iobtag=' + iobtag1,
        ])
    else:
        features.append('BOS')

    if i < len(sent)-1:
        word1 = sent[i+1][0]
        chtype1 = get_character_types(sent[i+1][0])
        postag1 = extract_pos_with_subtype(sent[i+1])
        features.extend([
            '+1:word=' + word1,
            '+1:type=' + chtype1,
            '+1:postag=' + postag1,
        ])
    else:
        features.append('EOS')

    if i < len(sent)-2:
        word2 = sent[i+2][0]
        chtype2 = get_character_types(sent[i+2][0])
        postag2 = extract_pos_with_subtype(sent[i+2])
        features.extend([
            '+2:word=' + word2,
            '+2:type=' + chtype2,
            '+2:postag=' + postag2,
        ])
    else:
        features.append('EOS')

    return features

# 形態素解析した解析結果だけ取り出す。
def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]


def sent2labels(sent):
    return [morph[-1] for morph in sent]


def sent2tokens(sent):
    return [morph[0] for morph in sent]

