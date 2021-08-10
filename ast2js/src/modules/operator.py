#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from ast2js.src.util.jscode import JsCode
from ast2js.src.modules.nodeParser import NodeParser


class Operator(NodeParser):
    def __init__(self, recursion_function):
        self.func = recursion_function
        self.synbols = {
            'Add': self.isAdd,
            'Sub': self.isSub,
            'Mult': self.isMult,
            'MatMult': self.isMatMult,
            'Div': self.isDiv,
            'Mod': self.isMod,
            'Pow': self.isPow,
            'LShift': self.isLShift,
            'RShift': self.isRShift,
            'BitOr': self.isBitOr,
            'BitXor': self.isBitXor,
            'BitAnd': self.isBitAnd,
            'FloorDiv': self.isFloorDiv,
        }
        return

    def isAdd(self, v, opt):
        return JsCode('+')

    def isSub(self, v, opt):
        return JsCode('-')

    def isMult(self, v, opt):
        return JsCode('*')

    def isMatMult(self, v, opt):
        return JsCode('@') # 行列乗算

    def isDiv(self, v, opt):
        return JsCode('/')

    def isMod(self, v, opt):
        return JsCode('%')

    def isPow(self, v, opt):
        return JsCode('**') # power

    def isLShift(self, v, opt):
        return JsCode('<<')

    def isRShift(self, v, opt):
        return JsCode('>>')

    def isBitOr(self, v, opt):
        return JsCode('|')

    def isBitXor(self, v, opt):
        return JsCode('^')

    def isBitAnd(self, v, opt):
        return JsCode('&')

    def isFloorDiv(self, v, opt):
        return JsCode('//')