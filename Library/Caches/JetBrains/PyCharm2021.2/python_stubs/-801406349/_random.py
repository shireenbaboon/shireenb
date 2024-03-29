# encoding: utf-8
# module _random
# from /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload/_random.cpython-39-darwin.so
# by generator 1.147
""" Module implements the Mersenne Twister random number generator. """
# no imports

# no functions
# classes

class Random(object):
    """ Random() -> create a random number generator with its own internal state. """
    def getrandbits(self, k): # real signature unknown; restored from __doc__
        """ getrandbits(k) -> x.  Generates an int with k random bits. """
        pass

    def getstate(self): # real signature unknown; restored from __doc__
        """ getstate() -> tuple containing the current state. """
        return ()

    def random(self): # real signature unknown; restored from __doc__
        """ random() -> x in the interval [0, 1). """
        pass

    def seed(self, n=None): # real signature unknown; restored from __doc__
        """
        seed([n]) -> None.
        
        Defaults to use urandom and falls back to a combination
        of the current time and the process identifier.
        """
        pass

    def setstate(self, state): # real signature unknown; restored from __doc__
        """ setstate(state) -> None.  Restores generator state. """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7faeb2753580>'

__spec__ = None # (!) real value is "ModuleSpec(name='_random', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7faeb2753580>, origin='/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload/_random.cpython-39-darwin.so')"

