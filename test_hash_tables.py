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
        assert(table.insert('woah!', 1) is True)

    def test_linear_probe_search_1(self):
        table = hash_tables.LinearProbe(hash_functions.h_ascii, 100)
        table.insert('woah!', 1)
        assert(table.search('woah!') == 1)

    def test_linear_probe_add_search_random(self):
        table = hash_tables.LinearProbe(hash_functions.h_ascii, 100)
        key = ''
        for _ in range(random.randint(1, 10)):
            val = random.randint(97, 122)
            key += chr(val)
        value = random.randint(0, 10000)
        assert(table.insert(key, value) is True)
        assert(table.search(key) == value)

    def test_linear_probe_full_random(self):
        size = random.randint(1, 10000)
        table = hash_tables.LinearProbe(hash_functions.h_ascii, size)
        for i in range(size):
            table.insert(str(i), i)

        self.assertRaises(IndexError, table.insert, 'full', 10)
        assert table.search('full') == -1

    def test_linear_probe_key_not_in_table(self):
        table = hash_tables.LinearProbe(hash_functions.h_ascii, 30)
        assert table.search('not in table') == -1

    def test_linear_probe_replace_key(self):
        table = hash_tables.LinearProbe(hash_functions.h_ascii, 30)
        table.insert('ayo', 10)
        table.insert('ayo', 100)
        assert table.capacity == 1
        assert table.search('ayo') == 100


class TestChainedHash(unittest.TestCase):
    def test_chained_hash_incorrect_types(self):
        self.assertRaises(TypeError, hash_tables.ChainedHash,
                          hash_functions.h_ascii, "not an int!")
        self.assertRaises(NotImplementedError,
                          hash_tables.ChainedHash, lambda a, b: None, 50)

    def test_chained_hash_add_empty(self):
        table = hash_tables.ChainedHash(hash_functions.h_ascii, 100)
        assert(table.insert('woah!', 1) is True)
        assert('woah!' in table.keys)

    def test_chained_hash_search_1(self):
        table = hash_tables.ChainedHash(hash_functions.h_ascii, 100)
        table.insert('woah!', 1)
        assert(table.search('woah!') == 1)

    def test_chained_hash_add_search_random(self):
        table = hash_tables.ChainedHash(hash_functions.h_ascii, 100)
        key = ''
        for _ in range(random.randint(1, 10)):
            val = random.randint(97, 122)
            key += chr(val)
        value = random.randint(0, 10000)
        assert(table.insert(key, value) is True)
        assert(table.search(key) == value)

    def test_chained_hash_key_not_in_table(self):
        table = hash_tables.ChainedHash(hash_functions.h_ascii, 30)
        assert table.search('not in table') == -1

    def test_chained_hash_replace_key(self):
        table = hash_tables.ChainedHash(hash_functions.h_ascii, 30)
        table.insert('ayo', 10)
        table.insert('ayo', 100)
        assert table.capacity == 1
        assert table.search('ayo') == 100

    def test_chained_hash_stored_keys(self):
        table = hash_tables.ChainedHash(hash_functions.h_ascii, 50)
        table.insert('new_key', 10)
        table.insert('another_key', 30)
        table.insert('additional_key', 40)
        table.insert('new_key', 30)
        assert len(table.keys) == 3


class TestQuadraticProbe(unittest.TestCase):
    def test_quadratic_probe_incorrect_types(self):
        self.assertRaises(TypeError, hash_tables.QuadraticProbe,
                          hash_functions.h_ascii, "not an int!")
        self.assertRaises(NotImplementedError,
                          hash_tables.QuadraticProbe, lambda a, b: None, 50)

    def test_quadratic_probe_add_empty(self):
        table = hash_tables.QuadraticProbe(hash_functions.h_ascii, 100)
        assert(table.insert('woah!', 1) is True)

    def test_quadratic_probe_search_1(self):
        table = hash_tables.QuadraticProbe(hash_functions.h_ascii, 100)
        table.insert('woah!', 1)
        assert(table.search('woah!') == 1)

    def test_quadratic_probe_add_search_random(self):
        table = hash_tables.QuadraticProbe(hash_functions.h_ascii, 100)
        key = ''
        for _ in range(random.randint(1, 10)):
            val = random.randint(97, 122)
            key += chr(val)
        value = random.randint(0, 10000)
        assert(table.insert(key, value) is True)
        assert(table.search(key) == value)

    def test_quadratic_probe_key_not_in_table(self):
        table = hash_tables.QuadraticProbe(hash_functions.h_ascii, 30)
        assert table.search('not in table') == -1

    def test_quadratic_probe_replace_key(self):
        table = hash_tables.QuadraticProbe(hash_functions.h_ascii, 30)
        table.insert('ayo', 10)
        table.insert('ayo', 100)
        assert table.capacity == 1
        assert table.search('ayo') == 100
