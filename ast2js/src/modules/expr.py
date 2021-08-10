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
            'BoolOp': self.convert_BoolOp,
            'NamedExpr': self.convert_NamedExpr,
            'BinOp': self.convert_BinOp,
            'UnaryOp': self.convert_UnaryOp,
            'Lambda': self.convert_Lambda,
            'IfExp': self.convert_IfExp,
            'Dict': self.convert_Dict,
            'Set': self.convert_Set,
            'ListComp': self.convert_ListComp,
            'SetComp': self.convert_SetComp,
            'DictComp': self.convert_DictComp,
            'GeneratorExp': self.convert_GeneratorExp,
            'Await': self.convert_Await,
            'Yield': self.convert_Yield,
            'YieldFrom': self.convert_YieldFrom,
            'Compare': self.convert_Compare,
            'Call': self.convert_Call,
            'FormattedValue': self.convert_FormattedValue,
            'JoinedStr': self.convert_JoinedStr,
            'Constant': self.convert_Constant,
            'Attribute': self.convert_Attribute,
            'Subscript': self.convert_Subscript,
            'Starred': self.convert_Starred,
            'Name': self.convert_Name,
            'List': self.convert_List,
            'Tuple': self.convert_Tuple,
            'Slice': self.convert_Slice,
            'attributes': self.convert_attributes,
        }
        self.func = recursion_function
        return

    def convert_BoolOp(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_NamedExpr(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_BinOp(self, v, opt={}):
        jscode: JsCode = JsCode()
        left = self.func(v.get('left'))
        k = v.get('op')
        _op = k if k not in [{}, None] else {'Add': '+'}
        op = self.func(_op)
        right = self.func(v.get('right'))
        jscode.add(f'{left} {op} {right}')
        return jscode

    def convert_UnaryOp(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_Lambda(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_IfExp(self, v, opt={}):
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

    def convert_Dict(self, v, opt={}):
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

    def convert_Set(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_ListComp(self, v, opt={}):
        jscode: JsCode = JsCode()
        generators = self.func(v.get('generators'), opt={
            'elt': v.get('elt')
        })
        jscode.add(generators)
        return jscode

    def convert_SetComp(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_DictComp(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_GeneratorExp(self, v, opt={}):
        jscode: JsCode = JsCode()
        elt = self.func(v.get('elt'))
        op = {
            'elt': {
                'Return': v.get('elt')
            }
        }
        generators = self.func(v.get('generators'), opt=op)
        return jscode

    def convert_Await(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_Yield(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_YieldFrom(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_Compare(self, v, opt={}):
        jscode: JsCode = JsCode()
        left = self.func(v.get('left'))
        ops = self.func(v.get('ops'))
        comparators = self.func(v.get('comparators'))
        jscode.add(f'{left} {ops} {comparators}')
        return jscode

    def convert_Call(self, v, opt={}):
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

    def convert_FormattedValue(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_JoinedStr(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_Constant(self, v, opt={}):
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

    def convert_Attribute(self, v, opt={}):
        jscode: JsCode = JsCode()
        _parent = str(self.convert_Name(deep_get(v, ['value', 'Name'], {})))
        parent = 'this' if _parent == 'self' else _parent
        parent = '\'\'' if parent == '' else parent
        method = deep_get(v, ['attr'], {})
        jscode.add('.'.join([parent, method]))
        return jscode

    def convert_Subscript(self, v, opt={}):
        jscode: JsCode = JsCode()
        _slice = v.get('slice')
        _value = v.get('value')
        if _slice is not None and _value is not None:
            aSlice = self.func(_slice)
            aValue = self.func(_value)
            jscode.add(f'{aValue}[{aSlice}]')
        return jscode

    def convert_Starred(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_Name(self, v: dict, opt={}):
        name = v.get('id', '')
        jscode: JsCode = JsCode()
        jscode.add(name)
        return jscode

    def convert_List(self, v, opt={}):
        jscode: JsCode = JsCode()
        aList = []
        if 'elts' in v:
            aList = [str(self.func(item, 'Constant')) for item in v['elts']]
        jscode.add('[')
        jscode.add(', '.join(aList))
        jscode.add(']')
        return jscode

    def convert_Tuple(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_Slice(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def convert_attributes(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode