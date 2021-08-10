#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from ast2js.src.util.jscode import JsCode
from ast2js.src.modules.nodeParser import NodeParser

class Comprehension(NodeParser):
    
    tuples = ...

    # [x for x in numbers ]などの記法を変換するクラス
    def __init__(self, recursion_function):
        self.func = recursion_function
        self.synbols = {
            'comprehension': self.isComprehension
        }
        return

    def isComprehension(self, v, opt={}):
        jscode: JsCode = JsCode()
        target = v.get('target')
        iter = v.get('iter')
        _ifs = v.get('ifs')
        _elt = opt.get('elt')
        body = _elt if _elt is not None else {}
        ifs = [self.func(item) for item in _ifs]

        if isinstance(ifs, list):
            ifs.reverse()

        for aCondition in ifs:
            jscode.addln(f'if({aCondition}){{')

        jscode.addln(f'{self.func(iter)}.map({self.func(target)} => {self.func(body)})')
        for _ in ifs:
            jscode.add_closer()
        return jscode