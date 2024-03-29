# encoding: utf-8
# module _posixsubprocess
# from /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload/_posixsubprocess.cpython-39-darwin.so
# by generator 1.147
""" A POSIX helper for the subprocess module. """
# no imports

# functions

def fork_exec(args, executable_list, close_fds, pass_fds, cwd, env, p2cread, p2cwrite, c2pread, c2pwrite, errread, errwrite, errpipe_read, errpipe_write, restore_signals, call_setsid, gid, groups_list, uid, preexec_fn): # real signature unknown; restored from __doc__
    """
    fork_exec(args, executable_list, close_fds, pass_fds, cwd, env,
              p2cread, p2cwrite, c2pread, c2pwrite,
              errread, errwrite, errpipe_read, errpipe_write,
              restore_signals, call_setsid,
              gid, groups_list, uid,
              preexec_fn)
    
    Forks a child process, closes parent file descriptors as appropriate in the
    child and dups the few that are needed before calling exec() in the child
    process.
    
    If close_fds is true, close file descriptors 3 and higher, except those listed
    in the sorted tuple pass_fds.
    
    The preexec_fn, if supplied, will be called immediately before closing file
    descriptors and exec.
    WARNING: preexec_fn is NOT SAFE if your application uses threads.
             It may trigger infrequent, difficult to debug deadlocks.
    
    If an error occurs in the child process before the exec, it is
    serialized and written to the errpipe_write fd per subprocess.py.
    
    Returns: the child process's PID.
    
    Raises: Only on an error in the parent process.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7ffe9a3b9250>'

__spec__ = None # (!) real value is "ModuleSpec(name='_posixsubprocess', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7ffe9a3b9250>, origin='/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload/_posixsubprocess.cpython-39-darwin.so')"

