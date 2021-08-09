#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

dictionaries = [
    {
        'python': r'(\t*|\s*)if\s((\w*|\W*)+)\s*:',
        'javascript': r'(\t*|\s*)if\s*\((\s*(\w*|\W*)+\s*)\)\s*\{'
    },
]
import re

def _format(aString: str):
    pattern = re.compile(r'\{(\D*|\d*)\}')
    another_string = pattern.split(aString)
    return another_string

def main():
    print(_format('hoge{}huga{1}piyo'))
    aString = 'if a == 5:'
    for elem in dictionaries:
        res = re.match(elem['python'], aString)
        if res is not None:
            aList = list(filter(lambda elem: elem if True != '' else False, list(res.groups())))
            print(res.groups())
            print(aList)
            # for anotherElem in aList:
            #     print(re.sub('(\s*(\w*|\W*)+\s*)', anotherElem, elem['javascript']))
if __name__ == '__main__':
    main()