# encoding: utf-8
# module reportlab.lib._rl_accel
# from /Users/shireenb/PycharmProjects/pythonProject/medicalwebsite2/clinicmanagement/lib/python3.9/site-packages/reportlab/lib/_rl_accel.cpython-39-darwin.so
# by generator 1.147
"""
_rl_accel contains various accelerated utilities

	escapePDF makes a unicode or latin1 bytes safe for PDF

	asciiBase85Encode does what is says
	asciiBase85Decode does what is says

	fp_str converts numeric arguments to a single blank separated string
	calcChecksum calculate checksums for TTFs (legacy)
	add32 32 bit unsigned addition (legacy)
	hex32 32 bit unsigned to 0X8.8X string
	instanceStringWidthT1 version2 Font instance stringWidth
	instanceStringWidthTTF version2 TTFont instance stringWidth
	unicode2T1 version2 pdfmetrics.unicode2T1
	Box(width,character=None) creates a Knuth character Box with the specified width.
	Glue(width,stretch,shrink) creates a Knuth glue Box with the specified width, stretch and shrink.
	Penalty(width,penalty,flagged=0) creates a Knuth penalty Box with the specified width and penalty.
	BoxList() creates a knuth box list.
"""
# no imports

# Variables with simple values

version = b'0.80'

# functions

def add32(x, y): # real signature unknown; restored from __doc__
    """ add32(x,y)  32 bit unsigned x+y (returns long) """
    pass

def asciiBase85Decode(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ asciiBase85Decode(".....") return decoded bytes """
    pass

def asciiBase85Encode(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ asciiBase85Encode(".....") return encoded str """
    pass

def Box(width, character=None): # real signature unknown; restored from __doc__
    """ Box(width,character=None) create a Knuth Box instance """
    pass

def calcChecksum(string): # real signature unknown; restored from __doc__
    """ calcChecksum(string) calculate checksums for TTFs (returns long) """
    pass

def escapePDF(s): # real signature unknown; restored from __doc__
    """ escapePDF(s) return PDF safed string """
    pass

def fp_str(a0, a1, *more): # real signature unknown; restored from __doc__
    """ fp_str(a0, a1,...) convert numerics to blank separated string """
    pass

def Glue(width, stretch, shrink): # real signature unknown; restored from __doc__
    """ Glue(width,stretch,shrink) create a Knuth Glue instance """
    pass

def hex32(x): # real signature unknown; restored from __doc__
    """ hex32(x)  32 bit unsigned-->0X8.8X string """
    pass

def instanceStringWidthT1(*args, **kwargs): # real signature unknown
    """ Font.stringWidth(self,text,fontName,fontSize,encoding='utf8') --> width """
    pass

def instanceStringWidthTTF(*args, **kwargs): # real signature unknown
    """ TTFont.stringWidth(self,text,fontName,fontSize,encoding='utf8') --> width """
    pass

def Penalty(width, penalty, flagged=0): # real signature unknown; restored from __doc__
    """ Penalty(width,penalty,flagged=0) create a Knuth Penalty instance """
    pass

def sameFrag(f, g): # real signature unknown; restored from __doc__
    """ sameFrag(f,g) return 1 if fragments have same style """
    pass

def unicode2T1(*args, **kwargs): # real signature unknown
    """ return a list of (font,string) pairs representing the unicode text """
    pass

# classes

class BoxList(list):
    # no doc
    @classmethod
    def classmeth(cls, *args, **kw): # real signature unknown; restored from __doc__
        """ classmeth(*args, **kw) """
        pass

    def getstate(self): # real signature unknown; restored from __doc__
        """ getstate() -> state """
        pass

    def setstate(self, state): # real signature unknown; restored from __doc__
        """ setstate(state) """
        pass

    def staticmeth(self, *args, **kw): # real signature unknown; restored from __doc__
        """ staticmeth(*args, **kw) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """an int variable for demonstration purposes"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7faddf020850>'

__spec__ = None # (!) real value is "ModuleSpec(name='reportlab.lib._rl_accel', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7faddf020850>, origin='/Users/shireenb/PycharmProjects/pythonProject/medicalwebsite2/clinicmanagement/lib/python3.9/site-packages/reportlab/lib/_rl_accel.cpython-39-darwin.so')"

