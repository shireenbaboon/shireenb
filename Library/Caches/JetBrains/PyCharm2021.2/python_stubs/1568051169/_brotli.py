# encoding: utf-8
# module _brotli
# from /Users/shireenb/PycharmProjects/pythonProject/medicalwebsite2/clinicmanagement/lib/python3.9/site-packages/_brotli.cpython-39-darwin.so
# by generator 1.147
""" Implementation module for the Brotli library. """
# no imports

# Variables with simple values

MODE_FONT = 2
MODE_GENERIC = 0
MODE_TEXT = 1

__version__ = '1.0.9'

# functions

def decompress(string): # real signature unknown; restored from __doc__
    """
    Decompress a compressed byte string.
    
    Signature:
      decompress(string)
    
    Args:
      string (bytes): The compressed input data.
    
    Returns:
      The decompressed byte string.
    
    Raises:
      brotli.error: If decompressor fails.
    """
    pass

# classes

class Compressor(object):
    """
    An object to compress a byte string.
    
    Signature:
      Compressor(mode=MODE_GENERIC, quality=11, lgwin=22, lgblock=0)
    
    Args:
      mode (int, optional): The compression mode can be MODE_GENERIC (default),
        MODE_TEXT (for UTF-8 format text input) or MODE_FONT (for WOFF 2.0). 
      quality (int, optional): Controls the compression-speed vs compression-
        density tradeoff. The higher the quality, the slower the compression.
        Range is 0 to 11. Defaults to 11.
      lgwin (int, optional): Base 2 logarithm of the sliding window size. Range
        is 10 to 24. Defaults to 22.
      lgblock (int, optional): Base 2 logarithm of the maximum input block size.
        Range is 16 to 24. If set to 0, the value will be set based on the
        quality. Defaults to 0.
    
    Raises:
      brotli.error: If arguments are invalid.
    """
    def finish(self): # real signature unknown; restored from __doc__
        """
        Process all pending input and complete all compression, returning a string
        containing the remaining compressed data. This data should be concatenated
        to the output produced by any preceding calls to the "process()" or
        "flush()" methods.
        After calling "finish()", the "process()" and "flush()" methods
        cannot be called again, and a new "Compressor" object should be created.
        
        Signature:
          finish(string)
        
        Returns:
          The compressed output data (bytes)
        
        Raises:
          brotli.error: If compression fails
        """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """
        Process all pending input, returning a string containing the remaining
        compressed data. This data should be concatenated to the output produced by
        any preceding calls to the "process()" or "flush()" methods.
        
        Signature:
          flush()
        
        Returns:
          The compressed output data (bytes)
        
        Raises:
          brotli.error: If compression fails
        """
        pass

    def process(self): # real signature unknown; restored from __doc__
        """
        Process "string" for compression, returning a string that contains 
        compressed output data.  This data should be concatenated to the output 
        produced by any preceding calls to the "process()" or flush()" methods. 
        Some or all of the input may be kept in internal buffers for later 
        processing, and the compressed output data may be empty until enough input 
        has been accumulated.
        
        Signature:
          compress(string)
        
        Args:
          string (bytes): The input data
        
        Returns:
          The compressed output data (bytes)
        
        Raises:
          brotli.error: If compression fails
        """
        pass

    def __init__(self, mode=None, quality=11, lgwin=22, lgblock=0): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class Decompressor(object):
    """
    An object to decompress a byte string.
    
    Signature:
      Decompressor()
    
    Raises:
      brotli.error: If arguments are invalid.
    """
    def is_finished(self): # real signature unknown; restored from __doc__
        """
        Checks if decoder instance reached the final state.
        
        Signature:
          is_finished()
        
        Returns:
          True  if the decoder is in a state where it reached the end of the input
                and produced all of the output
          False otherwise
        
        Raises:
          brotli.error: If decompression fails
        """
        pass

    def process(self): # real signature unknown; restored from __doc__
        """
        Process "string" for decompression, returning a string that contains 
        decompressed output data.  This data should be concatenated to the output 
        produced by any preceding calls to the "process()" method. 
        Some or all of the input may be kept in internal buffers for later 
        processing, and the decompressed output data may be empty until enough input 
        has been accumulated.
        
        Signature:
          decompress(string)
        
        Args:
          string (bytes): The input data
        
        Returns:
          The decompressed output data (bytes)
        
        Raises:
          brotli.error: If decompression fails
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f88ada218e0>'

__spec__ = None # (!) real value is "ModuleSpec(name='_brotli', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f88ada218e0>, origin='/Users/shireenb/PycharmProjects/pythonProject/medicalwebsite2/clinicmanagement/lib/python3.9/site-packages/_brotli.cpython-39-darwin.so')"

