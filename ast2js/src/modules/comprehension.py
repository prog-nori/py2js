#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from ast2js.src.util.jscode import JsCode
from ast2js.src.modules.nodeParser import NodeParser
from ..util.boolutil import hasKeyOr

class Comprehension(NodeParser):
    
    tuples = ...

    # [x for x in numbers ]などの記法を変換するクラス
    def __init__(self, recursion_function):
        self.func = recursion_function
        self.tuples = [
            ('comprehension', self.isComprehension),
        ]
        return

    def isComprehension(self, v, opt={}):
        jscode: JsCode = JsCode()
        target = hasKeyOr(v, 'target')
        iter = hasKeyOr(v, 'iter')
        _ifs = hasKeyOr(v, 'ifs', [])
        # _is_async = hasKeyOr(v, 'is_async', 0)
        _elt = hasKeyOr(opt, 'elt')
        body = _elt if _elt is not None else {}
        # target = self.func(_target)
        # iter = self.func(_iter)
        ifs = [self.func(item) for item in _ifs]
        # for item in _ifs:
        #     ifs.append(self.func(item))
        # is_async = self.func(_is_async)
        # print('body:', body)

        # aList = []

        if isinstance(ifs, list):
            ifs.reverse()

        for aCondition in ifs:
            jscode.addln(f'if({aCondition}){{')
        _for = {
            'For': {
                'target': target,
                'iter': iter,
                'body': [{
                    'Return': {
                        'value': body
                    }
                }],
                'orelse': []
            }
        }
        # print('RETURN:')
        # print(self.func(
        #     {
        #     'Return': { 'value': body }
        #     }))
        # print('_for:', self.func(_for))
        jscode.addln(f'{self.func(iter)}.map({self.func(target)} => {self.func(body)})')
        for _ in ifs:
            jscode.add_closer()
        return jscode