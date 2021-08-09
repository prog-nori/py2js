#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

import ast

def isExceptHandler(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.ExceptHandler):
        output_dict['ExceptHandler'] = {
            'type': parse_nodes(nodes.type, nest),
            'name': parse_nodes(nodes.name, nest),
            'body': parse_nodes(nodes.body, nest),
        }