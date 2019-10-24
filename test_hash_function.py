import unittest
import hash_functions
import random


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

    def test_h_rolling(self):
        self.assertRaises(TypeError, hash_functions.h_ascii,
                          ["list", "of", "strings"], 10)
        self.assertRaises(TypeError, hash_functions.h_ascii, "key", "string!")

    def test_h_rolling_simple_ascii(self):
        assert(hash_functions.h_ascii("A", 130) == 65)

    def test_h_rolling_wrap_number(self):
        assert(hash_functions.h_ascii("AAAA", 10) == 65*4 % 10)

    def test_h_rolling_random(self):
        key = ''
        count = 0
        for _ in range(random.randint(1, 10)):
            val = random.randint(97, 122)
            key += chr(val)
            count += val
        rand_N = random.randint(1, 1000)
        assert hash_functions.h_ascii(key, rand_N) == count % 2**64 % rand_N
