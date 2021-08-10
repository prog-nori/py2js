#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from ast2js.src.modules.nodeParser import NodeParser
from ast2js.src.util.jscode import JsCode
from ..util.boolutil import (
    deep_get,
)
import re

class Stmt(NodeParser):
    tuples = ...

    def __init__(self, recursion_function):
        self.func = recursion_function
        self.isThisInClass = False
        self.synbols = {
            'FunctionDef': self.isFunctionDef,
            'AsyncFunctionDef': self.isAsyncFunctionDef,
            'ClassDef': self.isClassDef,
            'Return': self.isReturn,
            'Delete': self.isDelete,
            'Assign': self.isAssign,
            'AugAssign': self.isAugAssign,
            'AnnAssign': self.isAnnAssign,
            'For': self.isFor,
            'AsyncFor': self.isAsyncFor,
            'While': self.isWhile,
            'If': self.isIf,
            'With': self.isWith,
            'AsyncWith': self.isAsyncWith,
            'Raise': self.isRaise,
            'Try': self.isTry,
            'Assert': self.isAssert,
            'Import': self.isImport,
            'ImportFrom': self.isImportFrom,
            'Global': self.isGlobal,
            'Nonlocal': self.isNonlocal,
            'Expr': self.isExpr,
            'Pass': self.isPass,
            'Break': self.isBreak,
            'Continue': self.isContinue,
            'attributes': self.isattributes,
        }
        return

    def isFunctionDef(self, v, opt={}):
        jscode: JsCode = JsCode()
        isThisInClass = self.isThisInClass
        args = self.func(v.get('args'), {'list': True})
        aList = list(filter(lambda x: x not in ['null'], args.get()))
        aCondition = isinstance(aList, list) and len(aList) == 0
        args = '' if aCondition else ','.join(aList if len(aList) > 0 else '')
        func_name = v.get('name')

        if isThisInClass is True:
            func_name = 'constructor' if func_name == '__init__' else func_name
            jscode.addln(f'{func_name}({args}) {{')
        else:
            jscode.addln(f'const {func_name} = ({args}) => {{')
        body = v.get('body', {})
        _inner_process = self.func(body, opt={'list': True})
        inner_process = []
        for item in _inner_process:
            inner_process.extend([item for item in str(item).split('\n')])
        jscode.addln(inner_process)
        jscode.add_closer()
        jscode.add_br()
        return jscode

    def isAsyncFunctionDef(self, v, opt={}):
        # async def main(): ...のような形
        return self.isFunctionDef(v, opt)

    def isClassDef(self, v, opt={}):
        jscode: JsCode = JsCode()
        name = v.get('name')
        class_definition = f'class {name} '
        if len(v['bases']) != 0:
            # 継承処理
            extends_classname = self.func(v.get('bases', 0))
            jscode.addln(f'{class_definition}extends {extends_classname}{{')
        else:
            jscode.addln('{}{{'.format(class_definition))
        self.isThisInClass = True
        body = self.func(v.get('body'), {'list': True})
        inner_process = []
        for item in body:
            inner_process.extend([item for item in str(item).split('\n')])
        jscode.add([f'{item}\n' for item in inner_process])
        jscode.add_closer()
        self.isThisInClass = False
        return jscode

    def isReturn(self, v, opt={}):
        value = self.func(v.get('value'))
        jscode: JsCode = JsCode()
        if value is not None:
            jscode.add(f'return {value}')
        else:
            jscode.add(f'return')
        return jscode

    def isDelete(self, v, opt={}):
        jscode: JsCode = JsCode()
        jscode.add(self.func(v, opt={}))
        return jscode

    def isAssign(self, v, opt={}):
        jscode: JsCode = JsCode()
        variable_name = self.func(deep_get(v, ['targets', 0], ''))
        value = self.get_assign_variable_type(v.get('value'))
        keyword = ''
        if isinstance(value, str) and len(value) > 0:
            if value[0].isupper():
                value = 'new {}'.format(value)
        keyword = 'let'
        jscode.add(f'{keyword} {variable_name} = {value}')
        return jscode

    def isAugAssign(self, v, opt={}):
        # += -= *= /=等
        jscode: JsCode = JsCode()
        target = v.get('target')
        _key = v.get('op', {})
        key = self.func(_key)
        op = ''
        if not key == '':
            op = f'{key}='
        else:
            op = '+='
        value = self.func(v.get('value'))
        left = self.func(target)
        jscode.add(f'{left} {op} {value}')
        return jscode

    def isAnnAssign(self, v, opt={}):
        jscode: JsCode = JsCode()
        jscode.add(self.func(v, opt={}))
        return jscode

    def isFor(self, v, opt={}):
        jscode: JsCode = JsCode()
        _target = deep_get(v, ['target'], None)
        _iter = deep_get(v, ['iter'], None)
        target = ''
        iter = ''
        childNode = None
        if _target is not None:
            target = self.func(_target)
        if _iter is not None:
            childNode = list(_iter.keys())[0]
            iter = self.func(_iter)
            iter = re.sub(r'range\(([\W|\w]+)\)', r'\1', iter)
            try:
                iter = int(iter)
            except ValueError:
                pass
        if not (target == '' or iter == ''):
            if childNode == 'List':
                jscode.addln(f'for(const {target} of {iter}){{')
            elif childNode == 'Dict':
                jscode.addln(f'for(const {target} in {iter}){{')
            elif isinstance(iter, int):
                jscode.addln('for(let {0}=0; {0} < {1}; {0}++){{'.format(target, iter))
            else:
                jscode.addln(f'for(const {target} in {iter}){{')
            body =  self.func(v.get('body'), {'list': True})
            jscode.add([f'{item}\n' for item in body])
            jscode.add_closer()
        return jscode

    def isAsyncFor(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def isWhile(self, v, opt={}):
        jscode: JsCode = JsCode()
        _test = v.get('test')
        _body = v.get('body')
        _orelse = v.get('orelse')
        test = self.func(_test)
        body = [self.func(item) for item in _body]
        orelse = [self.func(item) for item in _orelse]
        
        jscode.addln(f'while({test}){{')
        jscode.addln(body)
        jscode.add_closer()
        jscode.add(orelse)
        return jscode

    def isIf(self, v, opt={}):
        jscode: JsCode = JsCode()
        _test = v.get('test')
        _body = v.get('body')
        _orelse = v.get('orelse', [])
        orelse = None
        if not (_test is None or _body is None):
            test = self.func(_test)
            body = self.func(_body)
            orelse = self.func(_orelse)
            jscode.addln(f'if({test}) {{')
            jscode.addln(f'{body}')
            jscode.add_closer()
        if not orelse == '':
            else_body = ''
            for item in _orelse:
                else_body += self.func(item)
                if 'If' in item and else_body:
                    jscode.addln(f' else {else_body}}}') #
                else:
                    jscode.addln(' else {')
                    jscode.add(else_body)
                    jscode.add_closer()
        else:
            jscode.add_br
        return jscode

    def isWith(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def isAsyncWith(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def isRaise(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def isTry(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def isAssert(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def isImport(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def isImportFrom(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def isGlobal(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def isNonlocal(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def isExpr(self, v, opt={}):
        jscode: JsCode = JsCode()
        _value = v.get('value')
        if _value is not None:
            value = self.func(_value)
            jscode.add(value)
        return jscode

    def isPass(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def isBreak(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def isContinue(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def isattributes(self, v, opt={}):
        jscode: JsCode = JsCode()
        return jscode

    def get_assign_variable_type(self, aVariable):
        if 'func' in aVariable:
            func_name = self.func(aVariable.get('func'))
            args = ''
            if 'args' in aVariable:
                args = ', '.join([item['value'] for item in aVariable['args']])
            return '{}({})'.format(func_name, args)
        else:
            return self.func(aVariable)