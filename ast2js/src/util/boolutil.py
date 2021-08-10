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