"""
 Most use working with files functions
 
"""

import os
import shutil

def mikdir(path):
    """
    mkdir like linux command

    Arguments:
    path -- path of dir
    Return:
    None
    """
    if(os.path.exists(path)):
        pass
    else:
        os.makedirs(path)
    
def mkdirs(paths = []):
    """
    mkdir for array of path 

    Arguments:
    paths -- path list
    Return:
    None
    """
    for path in paths:
        mikdir(path)

def copy(src , target):
    """
    copy from src to traget

    Arguments:
    src -- file source path 
    traget -- file target path
    Return:
    None
    """
    shutil.copy2(src, target)

def copies(srcs , tagets):
    """
    copy list of file from srcs to tragets

    Arguments:
    srcs -- paths list 
    tragets -- paths list
    Return:
    None
    """
    # most be same len
    assert len(srcs) == len(tagets)
    # pick one by one
    for idx in range(len(srcs)):
        copy(srcs[idx], tagets[idx])


def files_exist(paths = []):
    """
    check all files is exist 

    Arguments:
    paths -- path list 
   
    Return:
    Boolean -- True or False
    """
    for path in paths:
        if not os.path.exists(path):
            return False
    return True