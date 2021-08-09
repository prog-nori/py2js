#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

import ast

def isKeyword(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.keyword):
        output_dict['Keyword'] = {
            'arg': parse_nodes(nodes.arg, nest),
            'value': parse_nodes(nodes.value, nest),
        }