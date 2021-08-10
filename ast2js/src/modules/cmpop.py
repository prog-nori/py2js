#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from ast2js.src.util.jscode import JsCode
from ast2js.src.modules.nodeParser import NodeParser


class Cmpop(NodeParser):

    tuples = ...

    def __init__(self, recursion_function):
        self.func = recursion_function
        self.synbols = {
            'Eq': self.convert_Eq,
            'NotEq': self.convert_NotEq,
            'Lt': self.convert_Lt,
            'LtE': self.convert_LtE,
            'Gt': self.convert_Gt,
            'GtE': self.convert_GtE,
            'convert_': self.convert_Is,
            'convert_Not': self.convert_IsNot,
            'In': self.convert_In,
            'NotIn': self.convert_NotIn,
        }
        return

    def convert_Eq(self, v, opt={}):
        return JsCode('==')

    def convert_NotEq(self, v, opt={}):
        return JsCode('!=')

    def convert_Lt(self, v, opt={}):
        return JsCode('<')

    def convert_LtE(self, v, opt={}):
        return JsCode('<=')

    def convert_Gt(self, v, opt={}):
        return JsCode('>')

    def convert_GtE(self, v, opt={}):
        return JsCode('>=')

    def convert_Is(self, v, opt={}):
        return JsCode('===')

    def convert_IsNot(self, v, opt={}):
        return JsCode('!==')

    def convert_In(self, v, opt={}):
        return JsCode('in')

    def convert_NotIn(self, v, opt={}):
        return JsCode('not in')