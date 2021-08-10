#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

def deep_get(d, keys, default=None):
    """
    Example:
        d = {'meta': {'status': 'OK', 'status_code': 200}}
        deep_get(d, ['meta', 'status_code'])          # => 200
        deep_get(d, ['garbage', 'status_code'])       # => None
        deep_get(d, ['meta', 'garbage'], default='-') # => '-'
    """
    assert type(keys) is list
    if d is None:
        return default
    if not keys:
        return d
    next = {}
    if isinstance(d, dict):
        next = d.get(keys[0])
    elif isinstance(d, list):
        if len(d) > keys[0]:
            next = d[keys[0]]
    return deep_get(next, keys[1:], default)


"""
bool値をオブジェクト指向的に操作する簡易関数
"""
class Boolean:
    def __init__(self, value=None):
        if value is not None:
            self._value = value
        return
    
    def set_value(self, value: bool):
        self._value = value
        return
    
    def toggle(self):
        self._value = not self._value

    def get(self):
        return self._value
    
    def update(self, mode: str, aCondition):
        if mode == 'and':
            self._value &= aCondition
        elif mode == 'or':
            self._value |= aCondition
        if mode == 'xor':
            self._value ^= aCondition