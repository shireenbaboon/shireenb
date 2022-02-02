# encoding: utf-8
# module _bisect
# from /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload/_bisect.cpython-39-darwin.so
# by generator 1.147
"""
Bisection algorithms.

This module provides support for maintaining a list in sorted order without
having to sort the list after each insertion. For long lists of items with
expensive comparison operations, this can be an improvement over the more
common approach.
"""
# no imports

# functions

def bisect_left(*args, **kwargs): # real signature unknown
    """
    Return the index where to insert item x in list a, assuming a is sorted.
    
    The return value i is such that all e in a[:i] have e < x, and all e in
    a[i:] have e >= x.  So if x already appears in the list, i points just
    before the leftmost x already there.
    
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    pass

def bisect_right(*args, **kwargs): # real signature unknown
    """
    Return the index where to insert item x in list a, assuming a is sorted.
    
    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, i points just
    beyond the rightmost x already there
    
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    pass

def insort_left(*args, **kwargs): # real signature unknown
    """
    Insert item x in list a, and keep it sorted assuming a is sorted.
    
    If x is already in a, insert it to the left of the leftmost x.
    
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    pass

def insort_right(*args, **kwargs): # real signature unknown
    """
    Insert item x in list a, and keep it sorted assuming a is sorted.
    
    If x is already in a, insert it to the right of the rightmost x.
    
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f91a59796d0>'

__spec__ = None # (!) real value is "ModuleSpec(name='_bisect', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f91a59796d0>, origin='/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload/_bisect.cpython-39-darwin.so')"

