#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

from typing import Union

class JsCode(object):

    def __init__(self, value='', indent: int=0) -> None:
        self._indent: int = indent # インデント要素はここで統括する
        self.setIndent = lambda aString: '{}{}'.format(''.join(['\t' for _ in range(self._indent)]), aString)

        self._code_list: list = []
        if value != '':
            self.add(value)
        return
    
    def __str__(self) -> str:
        aList = [str(item) for item in self._code_list]
        return ''.join(aList)
    

    def get(self) -> list:
        return [str(item) for item in self._code_list]

    def add(self, aLine: Union[str, list]) -> None:
        if isinstance(aLine, list):
            for item in aLine:
                aString = self.setIndent(item)
                self._code_list.append(aString)
        else:
            aString = self.setIndent(aLine)
            self._code_list.append(f'{aString}')
        return
    
    def addln(self, aLine: Union[str, list]) -> None:
        br = lambda aString: f'{aString}\n'
        if isinstance(aLine, list):
            self.add([br(item) for item in aLine])
        else:
            self.add(br(aLine))
        if aLine[-1:] == '{':
            self._indent += 1
        return
    
    def add_br(self) -> None:
        self.add('\n')
        return
    
    def add_closer(self) -> None:
        self._indent -= 1
        self.add('}\n')
        return

    def hasNoResp(self) -> bool:
        """
        値が空文字またはNoneの場合Falseを返す
        それ以外の場合はTrueを返す
        """
        return ''.join(self.get()) not in ['', None]