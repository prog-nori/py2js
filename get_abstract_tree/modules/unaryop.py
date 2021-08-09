#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import ast

def isInvert(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Invert):
        output_dict['Invert'] = '~'

def isNot(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Not):
        output_dict['Not'] = 'not'

def isUAdd(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.UAdd):
        output_dict['UAdd'] = '+='

def isUSub(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.USub):
        output_dict['USub'] = '-='
