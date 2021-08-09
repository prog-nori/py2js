#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import ast
"""
本ファイルではmodule Pythonにおけるmod(Module, Interactive, Expression, FunctionType)を
識別し、与えられた関数を再帰的に処理することで該当する木構造を返すプログラムである。
"""

def isModule(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Module):
        # print('isModule')
        output_dict['Module'] = {
            'body': parse_nodes(nodes.body, nest),
            'type_ignores': parse_nodes(nodes.type_ignores, nest)
        }
        # func(nodes, nest)
    

def isInteractive(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Interactive):
        output_dict['Interactive'] = {
            'body': parse_nodes(nodes.body, nest)
        }
    

def isExpression(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Expression):
        output_dict['Expression'] = {
            'body': parse_nodes(nodes.body, nest)
        }
    

def isFunctionType(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.FunctionType):
        output_dict['FunctionType'] = {
            'argtypes': parse_nodes(nodes.argtypes, nest),
            'returns': parse_nodes(nodes.returns, nest)
        }
    