#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import ast
"""
本ファイルではmodule Pythonにおけるstmt(FunctionDef, AsyncFunctionDef...Pass, Break, Continue)を
識別し、与えられた関数を再帰的に処理することで該当する木構造を返すプログラムである。
"""

def isFunctionDef(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.FunctionDef):
        output_dict['FunctionDef'] = {
				'name': parse_nodes(nodes.name, nest),
				'args': parse_nodes(nodes.args, nest),
				'body': parse_nodes(nodes.body, nest),
				'decorator_list': parse_nodes(nodes.decorator_list, nest),
				'returns': parse_nodes(nodes.returns, nest),
				'type_comment': parse_nodes(nodes.type_comment, nest),
        }
    

def isAsyncFunctionDef(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.AsyncFunctionDef):
        output_dict['AsyncFunctionDef'] = {
				'name': parse_nodes(nodes.name, nest),
				'args': parse_nodes(nodes.args, nest),
				'body': parse_nodes(nodes.body, nest),
				'decorator_list': parse_nodes(nodes.decorator_list, nest),
				'returns': parse_nodes(nodes.returns, nest),
				'type_comment': parse_nodes(nodes.type_comment, nest),
        }
    

def isClassDef(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.ClassDef):
        output_dict['ClassDef'] = {
				'name': parse_nodes(nodes.name, nest),
				'bases': parse_nodes(nodes.bases, nest),
				'keywords': parse_nodes(nodes.keywords, nest),
				'body': parse_nodes(nodes.body, nest),
				'decorator_list': parse_nodes(nodes.decorator_list, nest),
        }
    

def isReturn(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Return):
        output_dict['Return'] = {
				'value': parse_nodes(nodes.value, nest),
        }
    

def isDelete(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Delete):
        output_dict['Delete'] = {
				'targets': parse_nodes(nodes.targets, nest),
        }
    

def isAssign(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Assign):
        output_dict['Assign'] = {
				'targets': parse_nodes(nodes.targets, nest),
				'value': parse_nodes(nodes.value, nest),
				'type_comment': parse_nodes(nodes.type_comment, nest),
        }
    

def isAugAssign(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.AugAssign):
        output_dict['AugAssign'] = {
				'target': parse_nodes(nodes.target, nest),
				'op': parse_nodes(nodes.op, nest),
				'value': parse_nodes(nodes.value, nest),
        }
    

def isAnnAssign(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.AnnAssign):
        output_dict['AnnAssign'] = {
				'target': parse_nodes(nodes.target, nest),
				'annotation': parse_nodes(nodes.annotation, nest),
				'value': parse_nodes(nodes.value, nest),
				'simple': parse_nodes(nodes.simple, nest),
        }
    

def isFor(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.For):
        output_dict['For'] = {
				'target': parse_nodes(nodes.target, nest),
				'iter': parse_nodes(nodes.iter, nest),
				'body': parse_nodes(nodes.body, nest),
				'orelse': parse_nodes(nodes.orelse, nest),
				'type_comment': parse_nodes(nodes.type_comment, nest),
        }
    

def isAsyncFor(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.AsyncFor):
        output_dict['AsyncFor'] = {
				'target': parse_nodes(nodes.target, nest),
				'iter': parse_nodes(nodes.iter, nest),
				'body': parse_nodes(nodes.body, nest),
				'orelse': parse_nodes(nodes.orelse, nest),
				'type_comment': parse_nodes(nodes.type_comment, nest),
        }
    

def isWhile(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.While):
        output_dict['While'] = {
				'test': parse_nodes(nodes.test, nest),
				'body': parse_nodes(nodes.body, nest),
				'orelse': parse_nodes(nodes.orelse, nest),
        }
    

def isIf(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.If):
        output_dict['If'] = {
				'test': parse_nodes(nodes.test, nest),
				'body': parse_nodes(nodes.body, nest),
				'orelse': parse_nodes(nodes.orelse, nest),
        }
    

def isWith(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.With):
        output_dict['With'] = {
				'items': parse_nodes(nodes.items, nest),
				'body': parse_nodes(nodes.body, nest),
				'type_comment': parse_nodes(nodes.type_comment, nest),
        }
    

def isAsyncWith(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.AsyncWith):
        output_dict['AsyncWith'] = {
				'items': parse_nodes(nodes.items, nest),
				'body': parse_nodes(nodes.body, nest),
				'type_comment': parse_nodes(nodes.type_comment, nest),
        }
    

def isRaise(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Raise):
        output_dict['Raise'] = {
				'exc': parse_nodes(nodes.exc, nest),
				'cause': parse_nodes(nodes.cause, nest),
        }
    

def isTry(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Try):
        output_dict['Try'] = {
				'body': parse_nodes(nodes.body, nest),
				'handlers': parse_nodes(nodes.handlers, nest),
				'orelse': parse_nodes(nodes.orelse, nest),
				'finalbody': parse_nodes(nodes.finalbody, nest),
        }
    

def isAssert(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Assert):
        output_dict['Assert'] = {
				'test': parse_nodes(nodes.test, nest),
				'msg': parse_nodes(nodes.msg, nest),
        }
    

def isImport(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Import):
        output_dict['Import'] = {
				'names': parse_nodes(nodes.names, nest),
        }
    

def isImportFrom(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.ImportFrom):
        output_dict['ImportFrom'] = {
				'module': parse_nodes(nodes.module, nest),
				'names': parse_nodes(nodes.names, nest),
				'level': parse_nodes(nodes.level, nest),
        }
    

def isGlobal(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Global):
        output_dict['Global'] = {
				'names': parse_nodes(nodes.names, nest),
        }
    

def isNonlocal(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Nonlocal):
        output_dict['Nonlocal'] = {
				'names': parse_nodes(nodes.names, nest),
        }
    

def isExpr(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Expr):
        output_dict['Expr'] = {
				'value': parse_nodes(nodes.value, nest),
        }
    

def isPass(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Pass):
        output_dict['Pass'] = {

        }
    

def isBreak(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Break):
        output_dict['Break'] = {

        }
    

def isContinue(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Continue):
        output_dict['Continue'] = {

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