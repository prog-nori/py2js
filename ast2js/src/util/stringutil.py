#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

def insert(aString, index, anotherString):
    """
    aStringのある位置indexにanotherStringを挿入する
    """
    res = ''
    if index <= 0:
        res = anotherString + aString
    else:
        res = aString[:index] + anotherString + aString[index:]
    return res

def getIndent(i):
    """
    インデントを設ける
    """
    return ''.join(['\t' for _ in range(i)])

def list2str(aList, filter_list=[], joiner=''):
    res = get_flat_list(aList, filter_list)
    return joiner.join(res)

def get_flat_list(aList, filter_list=[]):
    res = []
    filter = lambda x: x not in filter_list
    for item in aList:
        if filter(item):
            if isinstance(item ,list):
                res.extend(get_flat_list(item, filter_list))
            elif isinstance(item, str):
                res.append(item)
    return res
