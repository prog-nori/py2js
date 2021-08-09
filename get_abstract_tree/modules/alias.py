#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

import ast

def isAlias(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.alias):
        output_dict['alias'] = {
            'name': parse_nodes(nodes.name, nest),
            'asname': parse_nodes(nodes.asname, nest),
        }