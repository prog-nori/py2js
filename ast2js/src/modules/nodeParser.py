#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from ast2js.src.util.jscode import JsCode
from ast2js.src.util.indent import Indent

class NodeParser:

    indent: Indent = Indent(0)
    
    def parse(self, k, v, opt={}):
        if k in self.synbols:
            return self.synbols[k](v, opt=opt)
        else:
            return JsCode()