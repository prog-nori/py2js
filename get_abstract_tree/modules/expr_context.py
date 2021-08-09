#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import ast

def isLoad(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Load):
        output_dict['Load'] = {}
    

def isStore(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Store):
        # print(type(nodes))
        output_dict['Store'] = {}
    

def isDel(nodes, output_dict, nest, parse_nodes):
    if isinstance(nodes, ast.Del):
        output_dict['Del'] = {}
    