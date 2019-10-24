import unittest
import random
import sys
import hash_tables
import hash_functions


class TestLinearProbe(unittest.TestCase):
    def test_linear_probe_incorrect_types(self):
        self.assertRaises(TypeError, hash_tables.LinearProbe,
                          hash_functions.h_ascii, "not an int!")
        self.assertRaises(NotImplementedError,
                          hash_tables.LinearProbe, lambda a, b: None, 50)

    def test_linear_probe_add_empty(self):
        table = hash_tables.LinearProbe(hash_functions.h_ascii, 100)
        assert(table.add('woah!', 1) is True)

    def test_linear_probe_search_1(self):
        table = hash_tables.LinearProbe(hash_functions.h_ascii, 100)
        table.add('woah!', 1)
        assert(table.search('woah!') == 1)

    def test_linear_probe_add_search_random(self):
        table = hash_tables.LinearProbe(hash_functions.h_ascii, 100)
        key = ''
        for _ in range(random.randint(1, 10)):
            val = random.randint(97, 122)
            key += chr(val)
        value = random.randint(0, 10000)
        assert(table.add(key, value) is True)
        assert(table.search(key) == value)

    def test_linear_probe_full_random(self):
        size = random.randint(1, 10000)
        table = hash_tables.LinearProbe(hash_functions.h_ascii, size)
        for i in range(size):
            table.add(str(i), i)

        self.assertRaises(IndexError, table.add, 'full', 10)
        self.assertRaises(IndexError, table.search, 'full')

    def test_linear_probe_key_not_in_table(self):
        table = hash_tables.LinearProbe(hash_functions.h_ascii, 30)
        self.assertRaises(IndexError, table.search, 'not in table')


class TestChainedHash:
    pass
