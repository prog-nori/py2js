#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import ast

def isAnd(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.And):
        output_dict['And'] = 'and'
    

def isOr(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Or):
        output_dict['Or'] = 'or'
    
