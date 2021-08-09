#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

def hasKeyOr(anObject, aKey, defaultValue=None):
    """
    キーが存在すればそれを、存在しなければdefaultValueを返却する
    """
    if aKey in anObject:
        return anObject[aKey]
    else:
        return defaultValue

def hasAnyChildOr(anObject, keys, defaultValue=None):
    """
    キーが存在すればそれを、存在しなければdefaultValueを返却する
    """
    aKey = keys[0]
    aConditionA = isinstance(aKey, str) and aKey in anObject
    aConditionB = isinstance(aKey, int) and len(anObject) > aKey
    if aConditionA or aConditionB:
        if len(keys) > 1:
            return hasAnyChildOr(anObject[aKey], keys[1:], defaultValue)
        else:
            return anObject[aKey]
    else:
        return defaultValue

"""
bool値をオブジェクト指向的に操作する簡易関数
"""
class Boolean:
    def __init__(self, value=None):
        if value is not None:
            self._value = value
        return
    
    def set_value(self, value: bool):
        self._value = value
        return
    
    def toggle(self):
        self._value = not self._value

    def get(self):
        return self._value
    
    def update(self, mode: str, aCondition):
        if mode == 'and':
            self._value &= aCondition
        elif mode == 'or':
            self._value |= aCondition
        if mode == 'xor':
            self._value ^= aCondition