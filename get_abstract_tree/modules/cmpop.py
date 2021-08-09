#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import ast

def isEq(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Eq):
        output_dict['Eq'] = '='

def isNotEq(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.NotEq):
        output_dict['NotEq'] = '!='

def isLt(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Lt):
        # Less than
        output_dict['Lt'] = '<'

def isLtE(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.LtE):
        # Less than or Equal to
        output_dict['LtE'] = '<='

def isGt(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Gt):
        # Greater than
        output_dict['Gt'] = '>'

def isGtE(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.GtE):
        # Greater than or Equal to
        output_dict['GtE'] = '>='

def isIs(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Is):
        output_dict['Is'] = 'is'

def isIsNot(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.IsNot):
        output_dict['IsNot'] = 'is not'

def isIn(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.In):
        output_dict['In'] = 'in'

def isNotIn(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.NotIn):
        output_dict['NotIn'] = 'not in'