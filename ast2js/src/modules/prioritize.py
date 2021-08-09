#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

"""
すべてに優先する変換処理はここに記載
"""

from ast2js.src.util.jscode import JsCode
from ast2js.src.util.boolutil import hasAnyChildOr, hasKeyOr


class Prioritize:
    def __init__(self, recursion_function):
        self.func = recursion_function
        return
    
    def isTheFirstProcess(self, k, v, opt):
        jscode: JsCode = JsCode()
        if isinstance(v, dict):
            _if = hasAnyChildOr(v, ['test', 'Compare'])
            left = ...
            right = ...
            if _if:
                left = self.func(hasKeyOr(_if, 'left'))
                right = self.func(hasAnyChildOr(_if, ['comparators']))
                if left == '__name__' and right == '\'__main__\'':
                    jscode.addln(self.func(hasKeyOr(v, 'body'), opt={'list': True}))
        return jscode