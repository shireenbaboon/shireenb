# encoding: utf-8
# module resource
# from /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload/resource.cpython-39-darwin.so
# by generator 1.147
# no doc
# no imports

# Variables with simple values

RLIMIT_AS = 5
RLIMIT_CORE = 4
RLIMIT_CPU = 0
RLIMIT_DATA = 2
RLIMIT_FSIZE = 1
RLIMIT_MEMLOCK = 6
RLIMIT_NOFILE = 8
RLIMIT_NPROC = 7
RLIMIT_RSS = 5
RLIMIT_STACK = 3

RLIM_INFINITY = 9223372036854775807

RUSAGE_CHILDREN = -1
RUSAGE_SELF = 0

# functions

def getpagesize(*args, **kwargs): # real signature unknown
    pass

def getrlimit(*args, **kwargs): # real signature unknown
    pass

def getrusage(*args, **kwargs): # real signature unknown
    pass

def setrlimit(*args, **kwargs): # real signature unknown
    pass

# classes

class error(Exception):
    """ Base class for I/O related errors. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    characters_written = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    errno = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """POSIX exception code"""

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exception filename"""

    filename2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """second exception filename"""

    strerror = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exception strerror"""



class struct_rusage(tuple):
    """
    struct_rusage: Result from getrusage.
    
    This object may be accessed either as a tuple of
        (utime,stime,maxrss,ixrss,idrss,isrss,minflt,majflt,
        nswap,inblock,oublock,msgsnd,msgrcv,nsignals,nvcsw,nivcsw)
    or via the attributes ru_utime, ru_stime, ru_maxrss, and so on.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    ru_idrss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """unshared data size"""

    ru_inblock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """block input operations"""

    ru_isrss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """unshared stack size"""

    ru_ixrss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """shared memory size"""

    ru_majflt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """page faults requiring I/O"""

    ru_maxrss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """max. resident set size"""

    ru_minflt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """page faults not requiring I/O"""

    ru_msgrcv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """IPC messages received"""

    ru_msgsnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """IPC messages sent"""

    ru_nivcsw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """involuntary context switches"""

    ru_nsignals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """signals received"""

    ru_nswap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """number of swap outs"""

    ru_nvcsw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """voluntary context switches"""

    ru_oublock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """block output operations"""

    ru_stime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """system time used"""

    ru_utime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """user time used"""


    n_fields = 16
    n_sequence_fields = 16
    n_unnamed_fields = 0


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7fe69f04f880>'

__spec__ = None # (!) real value is "ModuleSpec(name='resource', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7fe69f04f880>, origin='/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload/resource.cpython-39-darwin.so')"

