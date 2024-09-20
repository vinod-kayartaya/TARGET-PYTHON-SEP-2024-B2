"""
A simple module with simple utility functions
"""

import json


def create_dict(keys:list, vals:list) -> dict:
    return dict(zip(keys, vals))

def print_json(obj, indent=None):
    print(json.dumps(obj, indent=indent))

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def line(char='-', size=80):
    print(char * size)


def dir2(arg):
    """
    returns a list of non-dunder attributes of the given object as argument
    """
    attrs = []
    for each_attr in dir(arg):
        if not each_attr.startswith('_'):
            attrs.append(each_attr)
    return attrs


def sum_of_nums(s: str) -> float:
    if type(s) in (int, float):
        return s
    
    if not isinstance(s, str):
        raise ValueError('Parameter must be int/float/str')
    
    ar = s.split(',')
    ar = [float(a) for a in ar if is_float(a)]
    return sum(ar)
