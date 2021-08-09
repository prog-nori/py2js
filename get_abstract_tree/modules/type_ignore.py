#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

import ast

def isTypeIgnore(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.TypeIgnore):
        output_dict['TypeIgnore'] = {
            'lineno': parse_nodes(nodes.lineno, nest),
            'tag': parse_nodes(nodes.tag, nest),
        }