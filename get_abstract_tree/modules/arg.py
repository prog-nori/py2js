#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

import ast

def isArg(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.arg):
        output_dict['arg'] = {
            'arg': parse_nodes(nodes.arg, nest),
            'annotation': parse_nodes(nodes.annotation, nest),
            'type_comment': parse_nodes(nodes.type_comment, nest)
        }