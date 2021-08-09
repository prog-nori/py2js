#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from ast2js.src.util.jscode import JsCode
from ast2js.src.modules.nodeParser import NodeParser


class Cmpop(NodeParser):

    tuples = ...

    def __init__(self, recursion_function):
        self.func = recursion_function
        self.tuples = [
            ('Eq', self.isEq),
            ('NotEq', self.isNotEq),
            ('Lt', self.isLt),
            ('LtE', self.isLtE),
            ('Gt', self.isGt),
            ('GtE', self.isGtE),
            ('Is', self.isIs),
            ('IsNot', self.isIsNot),
            ('In', self.isIn),
            ('NotIn', self.isNotIn),
        ]
        return

    def isEq(self, v, opt={}):
        return JsCode('==')

    def isNotEq(self, v, opt={}):
        return JsCode('!=')

    def isLt(self, v, opt={}):
        return JsCode('<')

    def isLtE(self, v, opt={}):
        return JsCode('<=')

    def isGt(self, v, opt={}):
        return JsCode('>')

    def isGtE(self, v, opt={}):
        return JsCode('>=')

    def isIs(self, v, opt={}):
        return JsCode('===')

    def isIsNot(self, v, opt={}):
        return JsCode('!==')

    def isIn(self, v, opt={}):
        return JsCode('in')

    def isNotIn(self, v, opt={}):
        return JsCode('not in')