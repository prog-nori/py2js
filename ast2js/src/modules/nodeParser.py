#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from ast2js.src.util.jscode import JsCode
from ast2js.src.util.indent import Indent

class NodeParser:

    isMatchThenParse = lambda key, method: ...

    indent: Indent = Indent(0)
    
    def parse(self, k, v, opt={}):
        res: JsCode = JsCode()

        isMatchThenParse = lambda key, method: method(v, opt=opt) if k == key else None

        for aTuple in self.tuples:
            res = isMatchThenParse(aTuple[0], aTuple[1])
            if res is not None:
                return res
        return JsCode()