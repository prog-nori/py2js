#! /usr/bin/env python3
#! -*- coding:utf-8 -*-

from ast2js.src.util.boolutil import hasKeyOr
from ast2js.src.util.jscode import JsCode
from ast2js.src.modules.operator import Operator
import pprint
from src.modules.stmt import Stmt
from src.modules.expr import Expr
from src.modules.cmpop import Cmpop
from src.modules.prioritize import Prioritize
from src.modules.arguments import Arguments
from src.modules.arg import Arg
from src.modules.comprehension import Comprehension
from src.modules.mod import Mod

class Translator:
    def __init__(self, pyast):
        """
        コンストラクタ。astをセットする
        """
        self.pyast = pyast
        self.stmt = Stmt(self.parse_dict)
        self.expr = Expr(self.parse_dict)
        self.cmpop = Cmpop(self.parse_dict)
        self.operator = Operator(self.parse_dict)
        self.prioritize = Prioritize(self.parse_dict)
        self.arguments = Arguments(self.parse_dict)
        self.arg = Arg(self.parse_dict)
        self.comprehension = Comprehension(self.parse_dict)
        self.mod = Mod(self.parse_dict)
        return

    def print(self):
        pprint.pprint(self.pyast)

    def run(self):
        """
        ここからpythonをjsに変換する。jsのstrを返す
        """
        self.print()
        jscode = self.parse_dict(self.pyast)
        print('===   result   ===')
        print(jscode)
        print('===    end     ===')
        return
    
    def parse_dict(self, tree, opt: dict={}):
        """
        再帰的に解析する
        """
        aList = []
        if isinstance(tree, dict):
            resp: JsCode = JsCode()
            for k, v in tree.items():
                prioritize_res: JsCode = self.prioritize.isTheFirstProcess(k, v, opt)
                stmt_res: JsCode = self.stmt.parse(k, v, opt)
                expr_res: JsCode = self.expr.parse(k, v, opt)
                cmpop_res: JsCode = self.cmpop.parse(k, v, opt)
                operator_res: JsCode = self.operator.parse(k, v, opt)
                arguments_res: JsCode = self.arguments.parse(k, v, opt)
                arg_res: JsCode = self.arg.parse(k, v, opt)
                comprehension_res: JsCode = self.comprehension.parse(k, v, opt)
                mod_res: JsCode = self.mod.parse(k, v, opt)

                if prioritize_res.hasNoResp(): # 絶対一番最初に比較!!
                    resp.add(prioritize_res)
                    return str(resp)
                if stmt_res.hasNoResp():
                    resp.add(stmt_res)
                elif expr_res.hasNoResp():
                    resp.add(expr_res)
                elif cmpop_res.hasNoResp():
                    resp.add(cmpop_res)
                elif operator_res.hasNoResp():
                    resp.add(operator_res)
                elif arguments_res.hasNoResp():
                    resp.add(arguments_res)
                elif arg_res.hasNoResp():
                    resp.add(arg_res)
                elif comprehension_res.hasNoResp():
                    resp.add(comprehension_res)
                elif mod_res.hasNoResp():
                    resp.add(mod_res)
                elif v == {}:
                    resp = JsCode('null')
                else:
                    resp.add(self.parse_dict(v, opt))
            #     print('my tern:', str(resp))
            # print('Resp:', resp)
            if hasKeyOr(opt, 'list', False):
                return resp
            return str(resp)

        elif isinstance(tree, list):
            # print('Tree:', tree)
            for item in tree:
                # print('[Type]', type(item))
                aList.append(self.parse_dict(item, opt))
            # print('aList:', aList)

        anotherList = [
            str(item) if isinstance(item, int) else None
            if isinstance(item, dict) else item
            for item in list(filter(lambda x: x is not None, aList))]
        anotherList = list(filter(lambda x: x not in [''], anotherList))

        if hasKeyOr(opt, 'list', False):
            return anotherList
        return ''.join(anotherList)