#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from ast2js.src.modules.nodeParser import NodeParser
from ast2js.src.util.jscode import JsCode
# from get_abstract_tree.modules.expr import isConstant
from ..util.boolutil import (
    hasKeyOr,
    hasAnyChildOr
)
from ..util.stringutil import (
    insert,
    getIndent
)

setIndent = lambda aString, indent: insert(aString, 0, getIndent(indent))

class Arguments(NodeParser):

    tuples = ...

    def __init__(self, recursion_function):
        self.func = recursion_function
        self.tuples = [
            ('arguments', self.isArguments),
        ]
        return

    def isArguments(self, v, opt={}):
        jscode: JsCode = JsCode()
        _args = hasKeyOr(v, 'args', [])
        _vararg = hasKeyOr(v, 'vararg', [])
        _kwonlyargs = hasKeyOr(v, 'kwonlyarg', [])
        _kw_defaults = hasKeyOr(v, 'kw_defaults', [])
        _kwarg = hasKeyOr(v, 'kwarg', [])
        _defaults = hasKeyOr(v, 'defaults', [])

        get_arguments_list = lambda aList: list(filter(lambda x: x is not None, [self.func(item) if item != {} else [] for item in aList]))

        vararg = self.func(_vararg) if _vararg != {} else []
        kw_defaults = get_arguments_list(_kw_defaults)
        kwarg = ['...{}'.format(item) for item in self.func(_kwarg)] # 可変長引数
        defaults = get_arguments_list(_defaults) # argsの初期値(必要な場合のみ)

        # 引数の初期値を設定
        defaults.reverse()
        tmp_args = get_arguments_list(_args)
        for i, item in enumerate(defaults):
            own = tmp_args[len(tmp_args) - (i + 1)]
            tmp_args[len(tmp_args) - (i + 1)] = '{} = {}'.format(own, item)
        args = list(filter(lambda x: x != 'self', tmp_args))

        # 同じく。
        kw_defaults.reverse()
        tmp_kwonlyargs = get_arguments_list(_kwonlyargs)
        for i, item in enumerate(kw_defaults):
            own = tmp_kwonlyargs[len(tmp_kwonlyargs) - (i + 1)]
            if (
                own is not None
                or own not in ['None', '', 'null', {}, []]):
                tmp_kwonlyargs[len(tmp_kwonlyargs) - (i + 1)] = '{} = {}'.format(own, item)
        kwonlyargs = tmp_kwonlyargs


        # 変数を合体！
        arguments = list()
        for item in [args, vararg, kwonlyargs, kwarg]:
            if isinstance(item, list):
                arguments.extend(item)
            else:
                arguments.append(item)
        if arguments:
            jscode.add((', '.join(arguments)))
        return jscode