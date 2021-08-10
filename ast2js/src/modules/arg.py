#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from ast2js.src.util.jscode import JsCode
from ast2js.src.modules.nodeParser import NodeParser

class Arg(NodeParser):

    tuples = ...

    def __init__(self, recursion_function):
        self.func = recursion_function
        self.synbols = {
            'arg': self.convert_Arg
        }
        return

    def convert_Arg(self, v, opt={}):
        jscode: JsCode = JsCode()
        jscode.add(v.get('arg', ''))
        return jscode