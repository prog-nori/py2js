#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from ast2js.src.util.jscode import JsCode
from ast2js.src.modules.nodeParser import NodeParser
from ..util.boolutil import (
    deep_get
)
import re

class Expr(NodeParser):

    tuples = ...

    def __init__(self, recursion_function):
        self.synbols = {
            'BoolOp': self.isBoolOp,
            'NamedExpr': self.isNamedExpr,
            'BinOp': self.isBinOp,
            'UnaryOp': self.isUnaryOp,
            'Lambda': self.isLambda,
            'IfExp': self.isIfExp,
            'Dict': self.isDict,
            'Set': self.isSet,
            'ListComp': self.isListComp,
            'SetComp': self.isSetComp,
            'DictComp': self.isDictComp,
            'GeneratorExp': self.isGeneratorExp,
            'Await': self.isAwait,
            'Yield': self.isYield,
            'YieldFrom': self.isYieldFrom,
            'Compare': self.isCompare,
            'Call': self.isCall,
            'FormattedValue': self.isFormattedValue,
            'JoinedStr': self.isJoinedStr,
            'Constant': self.isConstant,
            'Attribute': self.isAttribute,
            'Subscript': self.isSubscript,
            'Starred': self.isStarred,
            'Name': self.isName,
            'List': self.isList,
            'Tuple': self.isTuple,
            'Slice': self.isSlice,
            'attributes': self.isattributes,
        }
        self.func = recursion_function
        return

    def isBoolOp(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def isNamedExpr(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def isBinOp(self, v, opt={}):
        jscode: JsCode = JsCode()
        left = self.func(v.get('left'))
        k = v.get('op')
        _op = k if k not in [{}, None] else {'Add': '+'}
        op = self.func(_op)
        right = self.func(v.get('right'))
        jscode.add(f'{left} {op} {right}')
        return jscode

    def isUnaryOp(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def isLambda(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def isIfExp(self, v, opt={}):
        # 三項演算子
        jscode: JsCode = JsCode()
        _test = v.get('test')
        _body = v.get('body')
        _orelse = v.get('orelse', [])
        orelse = None
        if not (_test is None or _body is None):
            test = self.func(_test)
            body = self.func(_body)
            orelse = self.func(_orelse)
            jscode.add(f'{test}? {body}: {orelse}')
        return jscode

    def isDict(self, v, opt={}):
        jscode: JsCode = JsCode()
        keys = [aGrandChild['Constant']['value'] for aGrandChild in v['keys']]
        values = [aGrandChild['Constant']['value'] for aGrandChild in v['values']]
        res = {}
        if len(keys) == len(values):
            for i, item in enumerate(keys):
                res[item] = values[i]
        jscode.add(','.join([
            re.sub(
                r'\'([\W|\w]+)\':',
                r'\1:',
                str(item)
            ) for item in str(res).split(',')
        ]))
        return jscode

    def isSet(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def isListComp(self, v, opt={}):
        jscode: JsCode = JsCode()
        generators = self.func(v.get('generators'), opt={
            'elt': v.get('elt')
        })
        jscode.add(generators)
        return jscode

    def isSetComp(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def isDictComp(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def isGeneratorExp(self, v, opt={}):
        jscode: JsCode = JsCode()
        elt = self.func(v.get('elt'))
        op = {
            'elt': {
                'Return': v.get('elt')
            }
        }
        generators = self.func(v.get('generators'), opt=op)
        return jscode

    def isAwait(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def isYield(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def isYieldFrom(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def isCompare(self, v, opt={}):
        jscode: JsCode = JsCode()
        left = self.func(v.get('left'))
        ops = self.func(v.get('ops'))
        comparators = self.func(v.get('comparators'))
        jscode.add(f'{left} {ops} {comparators}')
        return jscode

    def isCall(self, v, opt={}):
        # 関数呼び出し
        jscode: JsCode = JsCode()
        _args = v.get('args')
        _func = v.get('func')
        args = ''
        func = ''
        if _args is not None:
            aList = []
            for item in _args:
                res = self.func(item)
                aList.append(res)
            args = aList
        if _func is not None:
            name = self.func(_func)
            func = 'console.log' if name == 'print' else name
        if not(args == '' or func == ''):
            arguments = ', '.join([arg.replace('\n', '') for arg in args]) if len(args) > 0 else ''
            jscode.add(f'{func}({arguments})')
        return jscode

    def isFormattedValue(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def isJoinedStr(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def isConstant(self, v, opt={}):
        jscode: JsCode = JsCode()
        if 'value' in v:
            value = v.get('value')
            if isinstance(value, list):
                aString = ' '.join(value)
                anotherString = f'\'{aString}\''
                jscode.add(anotherString)
            elif isinstance(value, dict) and value == {}:
                jscode.add('null')
            elif isinstance(value, str):
                if value == 'None':
                    value = 'null'
                jscode.add(f'\'{value}\'')
            else:
                jscode.add(value)
        return jscode

    def isAttribute(self, v, opt={}):
        jscode: JsCode = JsCode()
        _parent = str(self.isName(deep_get(v, ['value', 'Name'], {})))
        parent = 'this' if _parent == 'self' else _parent
        parent = '\'\'' if parent == '' else parent
        method = deep_get(v, ['attr'], {})
        jscode.add('.'.join([parent, method]))
        return jscode

    def isSubscript(self, v, opt={}):
        jscode: JsCode = JsCode()
        _slice = v.get('slice')
        _value = v.get('value')
        if _slice is not None and _value is not None:
            aSlice = self.func(_slice)
            aValue = self.func(_value)
            jscode.add(f'{aValue}[{aSlice}]')
        return jscode

    def isStarred(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def isName(self, v: dict, opt={}):
        name = v.get('id', '')
        jscode: JsCode = JsCode()
        jscode.add(name)
        return jscode

    def isList(self, v, opt={}):
        jscode: JsCode = JsCode()
        aList = []
        if 'elts' in v:
            aList = [str(self.func(item, 'Constant')) for item in v['elts']]
        jscode.add('[')
        jscode.add(', '.join(aList))
        jscode.add(']')
        return jscode

    def isTuple(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def isSlice(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def isattributes(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode