"""
A simple module with simple utility functions
"""

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
