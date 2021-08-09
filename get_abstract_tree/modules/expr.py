#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import ast
"""
本ファイルではmodule Pythonにおけるmod(Module, Interactive, Expression, FunctionType)を
識別し、与えられた関数を再帰的に処理することで該当する木構造を返すプログラムである。
"""

def isBoolOp(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.BoolOp):
        output_dict['BoolOp'] = {
				'op': parse_nodes(nodes.op, nest),
				'values': parse_nodes(nodes.values, nest),
        }
    

def isNamedExpr(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.NamedExpr):
        output_dict['NamedExpr'] = {
				'target': parse_nodes(nodes.target, nest),
				'value': parse_nodes(nodes.value, nest),
        }
    

def isBinOp(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.BinOp):
        output_dict['BinOp'] = {
				'left': parse_nodes(nodes.left, nest),
				'op': parse_nodes(nodes.op, nest),
				'right': parse_nodes(nodes.right, nest),
        }
    

def isUnaryOp(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.UnaryOp):
        output_dict['UnaryOp'] = {
				'op': parse_nodes(nodes.op, nest),
				'operand': parse_nodes(nodes.operand, nest),
        }
    

def isLambda(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Lambda):
        output_dict['Lambda'] = {
				'args': parse_nodes(nodes.args, nest),
				'body': parse_nodes(nodes.body, nest),
        }
    

def isIfExp(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.IfExp):
        output_dict['IfExp'] = {
				'test': parse_nodes(nodes.test, nest),
				'body': parse_nodes(nodes.body, nest),
				'orelse': parse_nodes(nodes.orelse, nest),
        }
    

def isDict(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Dict):
        output_dict['Dict'] = {
				'keys': parse_nodes(nodes.keys, nest),
				'values': parse_nodes(nodes.values, nest),
        }
    

def isSet(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Set):
        output_dict['Set'] = {
				'elts': parse_nodes(nodes.elts, nest),
        }
    

def isListComp(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.ListComp):
        output_dict['ListComp'] = {
				'elt': parse_nodes(nodes.elt, nest),
				'generators': parse_nodes(nodes.generators, nest),
        }
    

def isSetComp(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.SetComp):
        output_dict['SetComp'] = {
				'elt': parse_nodes(nodes.elt, nest),
				'generators': parse_nodes(nodes.generators, nest),
        }
    

def isDictComp(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.DictComp):
        output_dict['DictComp'] = {
				'key': parse_nodes(nodes.key, nest),
				'value': parse_nodes(nodes.value, nest),
				'generators': parse_nodes(nodes.generators, nest),
        }
    

def isGeneratorExp(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.GeneratorExp):
        output_dict['GeneratorExp'] = {
				'elt': parse_nodes(nodes.elt, nest),
				'generators': parse_nodes(nodes.generators, nest),
        }
    

def isAwait(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Await):
        output_dict['Await'] = {
				'value': parse_nodes(nodes.value, nest),
        }
    

def isYield(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Yield):
        output_dict['Yield'] = {
				'value': parse_nodes(nodes.value, nest),
        }
    

def isYieldFrom(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.YieldFrom):
        output_dict['YieldFrom'] = {
				'value': parse_nodes(nodes.value, nest),
        }
    

def isCompare(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Compare):
        output_dict['Compare'] = {
				'left': parse_nodes(nodes.left, nest),
				'ops': parse_nodes(nodes.ops, nest),
				'comparators': parse_nodes(nodes.comparators, nest),
        }
    

def isCall(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Call):
        output_dict['Call'] = {
				'func': parse_nodes(nodes.func, nest),
				'args': parse_nodes(nodes.args, nest),
				'keywords': parse_nodes(nodes.keywords, nest),
        }
    

def isFormattedValue(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.FormattedValue):
        output_dict['FormattedValue'] = {
				'value': parse_nodes(nodes.value, nest),
				'conversion': parse_nodes(nodes.conversion, nest),
				'format_spec': parse_nodes(nodes.format_spec, nest),
        }
    

def isJoinedStr(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.JoinedStr):
        output_dict['JoinedStr'] = {
				'values': parse_nodes(nodes.values, nest),
        }
    

def isConstant(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Constant):
        output_dict['Constant'] = {
				'value': parse_nodes(nodes.value, nest),
				'kind': parse_nodes(nodes.kind, nest),
        }
    

def isAttribute(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Attribute):
        output_dict['Attribute'] = {
				'value': parse_nodes(nodes.value, nest),
				'attr': parse_nodes(nodes.attr, nest),
				'ctx': parse_nodes(nodes.ctx, nest),
        }
    

def isSubscript(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Subscript):
        output_dict['Subscript'] = {
				'value': parse_nodes(nodes.value, nest),
				'slice': parse_nodes(nodes.slice, nest),
				'ctx': parse_nodes(nodes.ctx, nest),
        }
    

def isStarred(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Starred):
        output_dict['Starred'] = {
				'value': parse_nodes(nodes.value, nest),
				'ctx': parse_nodes(nodes.ctx, nest),
        }
    

def isName(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Name):
        output_dict['Name'] = {
				'id': parse_nodes(nodes.id, nest),
				'ctx': parse_nodes(nodes.ctx, nest),
        }
    

def isList(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.List):
        output_dict['List'] = {
				'elts': parse_nodes(nodes.elts, nest),
				'ctx': parse_nodes(nodes.ctx, nest),
        }
    

def isTuple(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Tuple):
        output_dict['Tuple'] = {
				'elts': parse_nodes(nodes.elts, nest),
				'ctx': parse_nodes(nodes.ctx, nest),
        }
    

def isSlice(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Slice):
        output_dict['Slice'] = {
				'lower': parse_nodes(nodes.lower, nest),
				'upper': parse_nodes(nodes.upper, nest),
				'step': parse_nodes(nodes.step, nest),
        }
    

# def isAttributes(nodes, output_dict, nest, parse_nodes):
#     if isinstance(nodes, ast.attributes):
#         output_dict['attributes'] = {
# 				'lineno': parse_nodes(nodes.lineno, nest),
# 				'col_offset': parse_nodes(nodes.col_offset, nest),
# 				'end_lineno': parse_nodes(nodes.end_lineno, nest),
# 				'end_col_offset': parse_nodes(nodes.end_col_offset, nest),
#         }
#     