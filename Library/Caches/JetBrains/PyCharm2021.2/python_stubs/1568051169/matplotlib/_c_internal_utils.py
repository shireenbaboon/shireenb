# encoding: utf-8
# module matplotlib._c_internal_utils
# from /Users/shireenb/PycharmProjects/pythonProject/medicalwebsite2/clinicmanagement/lib/python3.9/site-packages/matplotlib/_c_internal_utils.cpython-39-darwin.so
# by generator 1.147
# no doc
# no imports

# functions

def display_is_valid(*args, **kwargs): # real signature unknown
    """
    Check whether the current X11 or Wayland display is valid.
    
    On Linux, returns True if either $DISPLAY is set and XOpenDisplay(NULL)
    succeeds, or $WAYLAND_DISPLAY is set and wl_display_connect(NULL)
    succeeds.  On other platforms, always returns True.
    """
    pass

def Win32_GetCurrentProcessExplicitAppUserModelID(*args, **kwargs): # real signature unknown
    """
    Wrapper for Windows's GetCurrentProcessExplicitAppUserModelID.  On 
    non-Windows platforms, always returns None.
    """
    pass

def Win32_GetForegroundWindow(*args, **kwargs): # real signature unknown
    """
    Wrapper for Windows' GetForegroundWindow.  On non-Windows platforms, 
    always returns None.
    """
    pass

def Win32_SetCurrentProcessExplicitAppUserModelID(*args, **kwargs): # real signature unknown
    """
    Wrapper for Windows's SetCurrentProcessExplicitAppUserModelID.  On 
    non-Windows platforms, a no-op.
    """
    pass

def Win32_SetForegroundWindow(*args, **kwargs): # real signature unknown
    """
    Wrapper for Windows' SetForegroundWindow.  On non-Windows platforms, 
    a no-op.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7ff1f4addd00>'

__spec__ = None # (!) real value is "ModuleSpec(name='matplotlib._c_internal_utils', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7ff1f4addd00>, origin='/Users/shireenb/PycharmProjects/pythonProject/medicalwebsite2/clinicmanagement/lib/python3.9/site-packages/matplotlib/_c_internal_utils.cpython-39-darwin.so')"

