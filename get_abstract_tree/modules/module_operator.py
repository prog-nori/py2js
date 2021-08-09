#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import ast

def isAdd(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Add):
        output_dict['Add'] = '+'

def isSub(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Sub):
        output_dict['Sub'] = '-'

def isMult(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Mult):
        output_dict['Mult'] = '*'

def isMatMult(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.MatMult):
        output_dict['MatMult'] = '@' # 行列乗算

def isDiv(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Div):
        # Greater than
        output_dict['Div'] = '/'

def isMod(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Mod):
        # Greater than or Equal to
        output_dict['Mod'] = '%'

def isPow(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Pow):
        output_dict['Pow'] = '**' # power

def isLShift(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.LShift):
        output_dict['LShift'] = '<<'

def isRShift(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.RShift):
        output_dict['RShift'] = '>>'

def isBitOr(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.BitOr):
        output_dict['BitOr'] = '|'

def isBitXor(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.BitXor):
        output_dict['BitXor'] = '^'

def isBitAnd(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.BitAnd):
        output_dict['BitAnd'] = '&'

def isFloorDiv(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.FloorDiv):
        output_dict['FloorDiv'] = '//'