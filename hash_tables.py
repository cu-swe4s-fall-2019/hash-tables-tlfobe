import hash_functions
import sys


class LinearProbe:
    """
    Class used for creating a linear probing hash table

    Attributes
    ----------
    hash_function : function
        specific hash_function from hash_functions module
    N : int
        size of hash table
    table : list
        initialized hash table where keys + value pairs will populate
    capacity : int
        number of entries in the hash table

    Methods
    -------
    __init__(hash_function, N)
        constructor method for LinearProbe
    add(key, value)
        add key+value pair into hash table
    search(key)
        search for a value given a key
    """

    def __init__(self, hash_function, N=None):
        """
        constructor method for Linear Probe

        Arguments
        ---------
        hash_function : function
            specific hash_function from hash_functions module
        N : int
            size of hash table
        """
        if N is None:
            self.N = sys.maxsize
        elif not isinstance(N, int):
            raise TypeError("LinearProbe: N "+str(N)+" is not an int!")
        else:
            self.N = N

        if hash_function.__name__ not in ["h_FNV", "h_ascii", "h_rolling"]:
            raise NotImplementedError(
                "LinearProbe: hash function " + hash_function.__name__ +
                " is not implemented!")
        self.hash_function = hash_function
        self.table = [None for i in range(N)]
        self.capacity = 0

    def add(self, key, value):
        """
        adds a value+key pair to the has table

        Arguments
        ---------
        key : string
            string key used to creat hash
        value : anything!
            value to be stored hash value of key

        Returns
        -------
        True : bool
            returns True if value+key pair was added
        """
        start_hash = self.hash_function(key, self.N)

        for i in range(self.N):
            hash_position = (start_hash + i) % self.N
            if self.table[hash_position] is None:
                self.table[hash_position] = (key, value)
                self.capacity += 1
                return True
            if self.table[hash_position][0] == key:
                self.table[hash_position] = (key, value)
                return True
        raise IndexError("LinearProbe.search: hashtable is full!")

    def search(self, key):
        """
        search a key and return a value in the hashtable

        Arguments
        ---------
        key : string
            string key to access hash table

        Returns
        -------
        value : anything!
            value coresponding to hash adress
        """
        start_hash = self.hash_function(key, self.N)

        for i in range(self.N):
            hash_position = (start_hash + i) % self.N
            if self.table[hash_position] is None:
                raise KeyError("LinearProbe.search: key " + key +
                               " is not in hashtable")
            if self.table[hash_position][0] == key:
                return self.table[hash_position][1]
        raise KeyError(("LinearProbe.search: key " + key +
                        " is not in hashtable"))


class ChainedHash:
    """
    Class used for creating a chained hash table

    Attributes
    ----------
    hash_function : function
        specific hash_function from hash_functions module
    N : int
        size of hash table
    table : list
        initialized hash table where keys + value pairs will populate
    capacity : int
        number of entries in the hash table

    Methods
    -------
    __init__(hash_function, N)
        constructor method for LinearProbe
    add(key, value)
        add key+value pair into hash table
    search(key)
        search for a value given a key
    """

    def __init__(self, hash_function, N=None):
        """
        constructor method for Linear Probe

        Arguments
        ---------
        hash_function : function
            specific hash_function from hash_functions module
        N : int
            size of hash table
        """
        if N is None:
            self.N = sys.maxsize
        elif not isinstance(N, int):
            raise TypeError("LinearProbe: N "+str(N)+" is not an int!")
        else:
            self.N = N

        if hash_function.__name__ not in ["h_FNV", "h_ascii", "h_rolling"]:
            raise NotImplementedError(
                "LinearProbe: hash function " + hash_function.__name__ +
                " is not implemented!")
        self.hash_function = hash_function
        self.table = [[] for i in range(N)]
        self.capacity = 0
        self.keys = []

    def add(self, key, value):
        """
        adds a value+key pair to the has table

        Arguments
        ---------
        key : string
            string key used to creat hash
        value : anything!
            value to be stored hash value of key

        Returns
        -------
        True : bool
            returns True if value+key pair was added
        """
        start_hash = self.hash_function(key, self.N)

        def get_i0(a): return a[0]
        if len(self.table[start_hash]) == 0:
            self.table[start_hash].append((key, value))
            self.capacity += 1
            self.keys.append(key)
            return True
        keys = [get_i0(k_v_pair) for k_v_pair in self.table[start_hash]]
        if key not in keys:
            self.table[start_hash].append((key, value))
            self.capacity += 1
            self.keys.append(key)
            return True
        else:
            self.table[start_hash][keys.index(key)] = (key, value)
            return True
        return False

    def search(self, key):
        """
        search a key and return a value in the hashtable

        Arguments
        ---------
        key : string
            string key to access hash table

        Returns
        -------
        value : anything!
            value coresponding to hash adress
        """
        start_hash = self.hash_function(key, self.N)

        for k, v in self.table[start_hash]:
            if key == k:
                return v
        raise KeyError("ChainedHash.search: key " +
                       key+" is not in the hash table")


class QuadraticProbe:
    """
    Class used for creating a quadratic probing hash table

    Attributes
    ----------
    hash_function : function
        specific hash_function from hash_functions module
    N : int
        size of hash table
    table : list
        initialized hash table where keys + value pairs will populate
    capacity : int
        number of entries in the hash table

    Methods
    -------
    __init__(hash_function, N)
        constructor method for QuadraticProbe
    add(key, value)
        add key+value pair into hash table
    search(key)
        search for a value given a key
    """

    def __init__(self, hash_function, N=None):
        """
        constructor method for QuadraticProbe

        Arguments
        ---------
        hash_function : function
            specific hash_function from hash_functions module
        N : int
            size of hash table
        """
        if N is None:
            self.N = sys.maxsize
        elif not isinstance(N, int):
            raise TypeError("QuadraticProbe: N "+str(N)+" is not an int!")
        else:
            self.N = N

        if hash_function.__name__ not in ["h_FNV", "h_ascii", "h_rolling"]:
            raise NotImplementedError(
                "QuadraticProbe: hash function " + hash_function.__name__ +
                " is not implemented!")
        self.hash_function = hash_function
        self.table = [None for i in range(N)]
        self.capacity = 0

    def add(self, key, value):
        """
        adds a value+key pair to the has table

        Arguments
        ---------
        key : string
            string key used to creat hash
        value : anything!
            value to be stored hash value of key

        Returns
        -------
        True : bool
            returns True if value+key pair was added
        """
        start_hash = self.hash_function(key, self.N)

        for i in range(self.N):
            hash_position = (start_hash + i**2) % self.N
            if self.table[hash_position] is None:
                self.table[hash_position] = (key, value)
                self.capacity += 1
                return True
            if self.table[hash_position][0] == key:
                self.table[hash_position] = (key, value)
                return True
        raise IndexError("QuadraticProbe.search: hashtable is full!")

    def search(self, key):
        """
        search a key and return a value in the hashtable

        Arguments
        ---------
        key : string
            string key to access hash table

        Returns
        -------
        value : anything!
            value coresponding to hash adress
        """
        start_hash = self.hash_function(key, self.N)

        for i in range(self.N):
            hash_position = (start_hash + i**2) % self.N
            if self.table[hash_position] is None:
                raise KeyError("QuadraticProbe.search: key " + key +
                               " is not in hashtable")
            if self.table[hash_position][0] == key:
                return self.table[hash_position][1]
        raise KeyError(("QuadraticProbe.search: key " + key +
                        " is not in hashtable"))
