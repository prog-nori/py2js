#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

import ast

def isComprehension(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.comprehension):
        output_dict['comprehension'] = {
            'target': parse_nodes(nodes.target, nest),
            'iter': parse_nodes(nodes.iter, nest),
            'ifs': parse_nodes(nodes.ifs, nest),
            'is_async': parse_nodes(nodes.is_async, nest),
        }
