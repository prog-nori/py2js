#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from ast2js.src.util.jscode import JsCode
from ast2js.src.modules.nodeParser import NodeParser
from ..util.boolutil import hasKeyOr
from ..util.stringutil import (
    insert,
    getIndent
)

class Arg(NodeParser):

    tuples = ...

    def __init__(self, recursion_function):
        self.func = recursion_function
        self.tuples = [
            ('arg', self.isArg),
        ]
        return

    def isArg(self, v, opt={}):
        jscode: JsCode = JsCode()
        jscode.add(hasKeyOr(v, 'arg', ''))
        return jscode