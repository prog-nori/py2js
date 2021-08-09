#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import ast
import pprint

def get_dump():
    py_code = """
checker = lambda x: (type(x) == 'int' and (type(x) == 'str' and x.isdecimal()))
def add(a, b):
    c = 0
    if checker(a) and checker(b):
        c = a + b
    return c
"""
    py_code2 = """
with open('main.py') as f:
    lines = f.readlines()
    for i in lines:
        print(lines)
"""
    py_code3 = """
def add(a, b):
    c = a + b
    return c
if __name__ == '__main__':
    res = add(4, 6)
    print(res)
"""
    py_code4 = """
a = 5
if a > 10:
    print('a is larger than 10')
elif a < 10:
    print('a is smaller than 10')
else:
    print('a is 10')

#pattern B
x = None
if x is not None:
    print('yes')
if not x is None:
    print('yes2')
if x is 10:
    print('x is 10!!')
"""

    nodes = ast.parse(py_code)
    dump = ast.dump(nodes)
    return dump, nodes

from parser import parse_nodes

def main():
    dump, nodes = get_dump()
    print(ast.arg)
    # print(nodes.__dict__)
    # print(nodes.__dict__['body'][1].__dict__['args'].__dict__['args'])
    for el in nodes.__dict__['body'][1].__dict__['args'].__dict__['args']:
        print(el.__dict__)
    print('=======')
    i = 1
    res = parse_nodes(nodes, i)
    # pprint.pprint(res)
    return

if __name__ == '__main__':
    main()