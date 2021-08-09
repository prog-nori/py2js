#! /usr/bin/env python3
#! -*- coding:utf-8 -*-

import ast
from pprint import pprint
from get_abstract_tree.parser import parse_nodes
from translate import Translator

class OutOfRangeValueError(Exception):
    """the value is out of range."""
    pass

class UnexpectedValueError(Exception):
    """the value is unexpected."""
    pass

class Example():
    def __init__(self):
        return

    def get_pycode(self, n=1):
        """
        pythonのサンプルコードを取得するメソッド
        """
        if type(n) != 'int':
            UnexpectedValueError('よきせぬ値が指定されました。int型を指定してください.')
        if not (n <= 4 and n >= 1):
            OutOfRangeValueError('範囲外の値が指定されました.')
        try:
            with open('./src/static/sample_programs/pycode{}.py'.format(n)) as fp:
                return ''.join(fp.readlines())
        except Exception as e:
            print(e)
            import sys
            sys.exit()

    def main(self):
        # サンプルコード(python)の取得
        pycode = self.get_pycode(5)
        # サンプルコードのast(dict)の取得
        parsed_pycode = ast.parse(pycode)
        parsed_ast = parse_nodes(parsed_pycode)
        translator = Translator(parsed_ast)
        # translator.print()
        translator.run()
        return

if __name__ == '__main__':
    example = Example()
    example.main()