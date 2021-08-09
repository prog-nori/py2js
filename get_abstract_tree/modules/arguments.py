#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

import ast

def isArguments(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.arguments):
        output_dict['arguments'] = {
            'posonlyargs': parse_nodes(nodes.posonlyargs, nest),
            'args': parse_nodes(nodes.args, nest),
            'vararg': parse_nodes(nodes.vararg, nest),
            'kwonlyargs': parse_nodes(nodes.kwonlyargs, nest),
            'kw_defaults': parse_nodes(nodes.kw_defaults, nest),
            'kwarg': parse_nodes(nodes.kwarg, nest),
            'defaults': parse_nodes(nodes.defaults, nest),
        }