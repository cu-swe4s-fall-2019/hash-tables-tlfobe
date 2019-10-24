import unittest
import hash_functions
import random
import sys


class TestHashFunctions(unittest.TestCase):
    def test_h_ascii_incorrect_inputs(self):
        self.assertRaises(TypeError, hash_functions.h_ascii,
                          ["list", "of", "strings"], 10)
        self.assertRaises(TypeError, hash_functions.h_ascii, "key", "string!")

    def test_h_ascii_simple_ascii(self):
        assert(hash_functions.h_ascii("A", 130) == 65)

    def test_h_ascii_wrap_number(self):
        assert(hash_functions.h_ascii("AAAA", 10) == 65*4 % 10)

    def test_h_ascii_random(self):
        key = ''
        count = 0
        for _ in range(random.randint(1, 10)):
            val = random.randint(97, 122)
            key += chr(val)
            count += val
        rand_N = random.randint(1, 1000)
        assert hash_functions.h_ascii(key, rand_N) == count % rand_N

    def test_h_rolling_incorect_inputs(self):
        self.assertRaises(TypeError, hash_functions.h_rolling,
                          ["list", "of", "strings"], 10)
        self.assertRaises(
            TypeError, hash_functions.h_rolling, "key", "string!")

    def test_h_rolling_simple_ascii(self):
        assert(hash_functions.h_rolling("A", 130) == 65)

    def test_h_rolling_wrap_number(self):
        assert(hash_functions.h_rolling("AAAA", 10) ==
               sum([65*56**i for i in range(4)]) % 10)

    def test_h_rolling_random(self):
        key = ''
        count = 0
        for i in range(random.randint(1, 10)):
            val = random.randint(97, 122)
            key += chr(val)
            count += val * 56 ** i
        rand_N = random.randint(1, 1000)
        assert hash_functions.h_rolling(key, rand_N) == count % 2**64 % rand_N

    def test_h_FNV_incorect_inputs(self):
        self.assertRaises(TypeError, hash_functions.h_ascii,
                          ["list", "of", "strings"], 10)
        self.assertRaises(TypeError, hash_functions.h_FNV, "key", "string!")

    def test_h_FNV_simple_ascii(self):
        assert(hash_functions.h_FNV("A", 130) == 62)

    def test_h_FNV_wrap_number(self):
        assert(hash_functions.h_FNV("AAAA", 10) == 3)

    def test_h_FNV_no_wrap(self):
        assert(hash_functions.h_FNV("") == 14695981039346656037 & sys.maxsize)

    def test_h_FNV_random(self):
        key = ''
        hash_value = 14695981039346656037
        for _ in range(random.randint(1, 10)):
            val = random.randint(97, 122)
            key += chr(val)
            hash_value = hash_value * 1099511628211 & sys.maxsize
            hash_value = hash_value ^ val & sys.maxsize
        assert hash_functions.h_FNV(key) == hash_value
