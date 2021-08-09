#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import ast
import pprint
import re

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

    nodes = ast.parse(py_code2)
    # print(nodes.__dict__)
    # child = nodes.__dict__['body'][0]
    # print(isinstance(child, ast.Assign))
    # print(type(nodes))
    # pprint.pprint(nodes)
    dump = ast.dump(nodes)
    # pprint.pprint(dump)
    # pprint.pprint(ast.literal_eval(dump))
    return dump, nodes

def _match(dump):
    # formwork = r'(\w+|\W+)(\t*|\s*)\((\w+|\W+)\)'
    formwork = r'([\w|\W]*)\=*[\(|\[]([\w|\W]*)[\)|\]]'
    res = re.match(formwork, dump)
    # print(dump, '\n***\n', res)
    if res is not None:
        aList = list(res.groups())
        i = 1
        for x in res.groups():
            print('\t{}: {}'.format(i, x))
            i += 1
        # print(len(res.groups()), res.groups())
        # pprint.pprint(aList)
        # print(aList)
        # print(45, res.groupdict())
        print('======')
        _match(res.groups()[0])
        # print(res.group())
    # print(res)
    return

def _sub(dump):
    # hoge=(やhoge(の形を: (の形に置換
    tmp = re.sub(
        r'([a-zA-Z_]+)=*([\(|\[])',
        r'\1: \2',
        dump)
    # =hogeを: {hoge}の形に置換
    # かっこ閉じるがうまく動作していない
    res = re.sub(
        r'=([\W|\w]+)[\W|\w]*',
        r': {\1}',
        tmp)
    # print(res)
    # pprint.pprint(str(res), indent=4)
    return res

# from parse_example import parse_nodes

def main():
    dump, nodes = get_dump()
    i = 1
    # res = parse_nodes(nodes, i)
    # print('=== FINISH ===')
    # print(res)
    # text = _sub(dump)
    # pprint.pprint(ast.literal_eval(text))
    # _match(dump)
    return

if __name__ == '__main__':
    main()