#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from ast2js.src.util.jscode import JsCode
from ast2js.src.modules.nodeParser import NodeParser


class Operator(NodeParser):
    def __init__(self, recursion_function):
        self.func = recursion_function
        self.synbols = {
            'Add': self.convert_Add,
            'Sub': self.convert_Sub,
            'Mult': self.convert_Mult,
            'MatMult': self.convert_MatMult,
            'Div': self.convert_Div,
            'Mod': self.convert_Mod,
            'Pow': self.convert_Pow,
            'LShift': self.convert_LShift,
            'RShift': self.convert_RShift,
            'BitOr': self.convert_BitOr,
            'BitXor': self.convert_BitXor,
            'BitAnd': self.convert_BitAnd,
            'FloorDiv': self.convert_FloorDiv,
        }
        return

    def convert_Add(self, v, opt):
        return JsCode('+')

    def convert_Sub(self, v, opt):
        return JsCode('-')

    def convert_Mult(self, v, opt):
        return JsCode('*')

    def convert_MatMult(self, v, opt):
        return JsCode('@') # 行列乗算

    def convert_Div(self, v, opt):
        return JsCode('/')

    def convert_Mod(self, v, opt):
        return JsCode('%')

    def convert_Pow(self, v, opt):
        return JsCode('**') # power

    def convert_LShift(self, v, opt):
        return JsCode('<<')

    def convert_RShift(self, v, opt):
        return JsCode('>>')

    def convert_BitOr(self, v, opt):
        return JsCode('|')

    def convert_BitXor(self, v, opt):
        return JsCode('^')

    def convert_BitAnd(self, v, opt):
        return JsCode('&')

    def convert_FloorDiv(self, v, opt):
        return JsCode('//')