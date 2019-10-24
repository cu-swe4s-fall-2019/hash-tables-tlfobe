import sys


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
    
    s = 0
    for i in range(len(key)):
        s += ord(key[i]) * 56 ** i
    s = s % 2**64

    return s % N


def h_FNV(key, N = None):
    """
    generates a hash for a given key using the FNV hash fxn

    Arguments
    ---------
    key : string
        key used to get hash value
    N (optional) : int
        size of hashtable, if unspecified returns for hashtable size of 2^64
    """
    if not isinstance(key, str):
        raise TypeError("h_rolling: key "+str(key)+" is not a string!")
    if N == None:
        pass
    elif not isinstance(N, int):
        raise TypeError("h_rolling: N "+str(N)+" is not an int!")

    hash_v = 14695981039346656037 # FNV offset basis
    for char in key:
        hash_v = hash_v * 1099511628211 & sys.maxsize # FNV prime
        hash_v = hash_v ^ ord(char) & sys.maxsize
    if N == None:
        return hash_v & sys.maxsize
    else:
        return hash_v % N # FNV hash functions ideal don't need wrap, because
                        # modulo is slow!
        