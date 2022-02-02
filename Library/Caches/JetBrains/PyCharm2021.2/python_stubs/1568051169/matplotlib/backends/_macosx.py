# encoding: utf-8
# module matplotlib.backends._macosx
# from /Users/shireenb/PycharmProjects/pythonProject/medicalwebsite2/clinicmanagement/lib/python3.9/site-packages/matplotlib/backends/_macosx.cpython-39-darwin.so
# by generator 1.147
""" Mac OS X native backend """
# no imports

# functions

def choose_save_file(*args, **kwargs): # real signature unknown
    """ Closes the window. """
    pass

def event_loop_is_running(*args, **kwargs): # real signature unknown
    """ Return whether the OSX backend has set up the NSApp main event loop. """
    pass

def set_cursor(*args, **kwargs): # real signature unknown
    """ Sets the active cursor. """
    pass

def show(*args, **kwargs): # real signature unknown
    """
    Show all the figures and enter the main loop.
    
    This function does not return until all Matplotlib windows are closed,
    and is normally not needed in interactive sessions.
    """
    pass

# classes

class FigureCanvas(object):
    """ A FigureCanvas object wraps a Cocoa NSView object. """
    def draw(self, *args, **kwargs): # real signature unknown
        pass

    def draw_idle(self, *args, **kwargs): # real signature unknown
        pass

    def flush_events(self, *args, **kwargs): # real signature unknown
        """ Flush the GUI events for the figure. """
        pass

    def remove_rubberband(self, *args, **kwargs): # real signature unknown
        """ Removes the current rubberband rectangle. """
        pass

    def set_rubberband(self, *args, **kwargs): # real signature unknown
        """ Specifies a new rubberband rectangle and invalidates it. """
        pass

    def start_event_loop(self, *args, **kwargs): # real signature unknown
        """ Runs the event loop until the timeout or until stop_event_loop is called. """
        pass

    def stop_event_loop(self, *args, **kwargs): # real signature unknown
        """ Stops the event loop that was started by start_event_loop. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


class FigureManager(object):
    """ A FigureManager object wraps a Cocoa NSWindow object. """
    def destroy(self, *args, **kwargs): # real signature unknown
        """ Closes the window associated with the figure manager. """
        pass

    def get_window_title(self, *args, **kwargs): # real signature unknown
        """ Returns the title of the window associated with the figure manager. """
        pass

    def resize(self, *args, **kwargs): # real signature unknown
        """ Resize the window (in pixels). """
        pass

    def set_window_title(self, *args, **kwargs): # real signature unknown
        """ Sets the title of the window associated with the figure manager. """
        pass

    def show(self, *args, **kwargs): # real signature unknown
        """ Shows the window associated with the figure manager. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


class NavigationToolbar2(object):
    """ NavigationToolbar2 """
    def set_message(self, *args, **kwargs): # real signature unknown
        """ Set the message to be displayed on the toolbar. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


class Timer(object):
    """ A Timer object wraps a CFRunLoopTimerRef and can add it to the event loop. """
    def _timer_start(self, *args, **kwargs): # real signature unknown
        """ Initialize and start the timer. """
        pass

    def _timer_stop(self, *args, **kwargs): # real signature unknown
        """ Stop the timer. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7fd183a21a60>'

__spec__ = None # (!) real value is "ModuleSpec(name='matplotlib.backends._macosx', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7fd183a21a60>, origin='/Users/shireenb/PycharmProjects/pythonProject/medicalwebsite2/clinicmanagement/lib/python3.9/site-packages/matplotlib/backends/_macosx.cpython-39-darwin.so')"

