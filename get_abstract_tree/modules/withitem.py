#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

import ast

def isWithitem(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.withitem):
        output_dict['Withitem'] = {
            'context_expr': parse_nodes(nodes.context_expr, nest),
            'optional_vars': parse_nodes(nodes.optional_vars, nest),
        }