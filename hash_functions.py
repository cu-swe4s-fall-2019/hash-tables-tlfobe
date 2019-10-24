
def h_ascii(key, N):
    """
    generates a hash value for a given key using a linear hash fxn

    Arguments
    ---------
    key : string
        key used to get hash value
    N : int
        size of hash table

    Returns
    -------
    hash index : int
        location in hashtable to place value
    """
    if not isinstance(key, str):
        raise TypeError("h_ascii: key "+str(key)+" is not a string!")
    if not isinstance(N, int):
        raise TypeError("h_ascii: N "+str(N)+" is not an int!")

    s = 0

    for i in range(len(key)):
        s += ord(key[i])
    return s % N


def h_rolling(key, N):
    """
    generates a hash value for a given key using a polynomial hash fxn

    Arguments
    ---------
    key : string
        key used to get hash value
    N : int
        size of hash table

    Returns
    -------
    hash index : int
        location in hashtable to place value
    """
    if not isinstance(key, str):
        raise TypeError("h_rolling: key "+str(key)+" is not a string!")
    if not isinstance(N, int):
        raise TypeError("h_rolling: N "+str(N)+" is not an int!")
    return None
