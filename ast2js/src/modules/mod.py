#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from ast2js.src.util.jscode import JsCode
from ast2js.src.modules.nodeParser import NodeParser
from ..util.boolutil import hasKeyOr

class Mod(NodeParser):

    tuples = ...

    def __init__(self, recursion_function):
        self.func = recursion_function
        self.tuples = [
            ('Module', self.isModule),
            ('Interactive', self.isInteractive),
            ('Expression', self.isExpression),
            ('FunctionType', self.isFunctionType),
        ]
        return

    def isModule(self, v, opt={}):
        jscode: JsCode = JsCode()
        body = self.func(hasKeyOr(v, 'body'))
        if body:
            jscode.add(body)
        return jscode
    
    def isInteractive(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode
    
    def isExpression(self, v, opt={}):
        jscode: JsCode = JsCode()
        body = self.func(hasKeyOr(v, 'body'))
        if body:
            jscode.addln(body)
        return jscode

    def isFunctionType(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode