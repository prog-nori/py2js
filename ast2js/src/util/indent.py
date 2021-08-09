#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

class Indent:
    def __init__(self, indent=0):
        self._indent = indent
        return

    def increment(self):
        self._indent += 1

    def decrement(self):
        self._indent -= 1
    
    def get(self):
        return self._indent