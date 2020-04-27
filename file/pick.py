"""
 Pickle most use functions.
 
"""

import pickle

def put(filename , data, customPath = False , verbose = 1):
    """
    Put data into pikle file

    Arguments:
    filename -- filename string or number like 
    data -- variable to save
    customPath -- if need to save in custom path at default save in context directory
    verbose -- print process (1) or no

    Return:
    None
    """
    filePath = '{}.pickle'.format(filename)
    if customPath:
        filePath = filename
    
    # open file
    with open(filePath, 'wb') as handle:
        # save in file path
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
        if verbose == 1:
            print("""
            {} save in {}
            """.format(filename, filePath))
        
        
        
def get(filename, customPath = False , verbose = 1):
    """
    Get data from pikle file

    Arguments:
    filename -- filename string or number like 
    customPath -- if need to save in custom path at default save in context directory
    verbose -- print process (1) or no

    Return:
    data
    """
    filePath = '{}.pickle'.format(filename)
    if customPath:
        filePath = filename
    # open file
    with open(filePath, 'rb') as handle:
         # read pickle file
        data = pickle.load(handle)
        if verbose == 1:
            print("""
            read {} from {} ended.
            """.format(filename, filePath))
        return data  
