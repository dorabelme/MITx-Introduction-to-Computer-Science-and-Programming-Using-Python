def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    result = None
    biggestValue = 0
    for key in aDict.keys():
        # Since all the values of aDict are lists, aDict.values() will 
        #  be a list of lists
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])
    return result
      