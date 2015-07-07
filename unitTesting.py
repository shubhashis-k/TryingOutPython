__author__ = 'shubhashis'


import unittest

def is_True(number):
    return True

class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_bal(self):
        self.assertTrue(is_True(5), "Something went Wrong")
        self.assertEqual("Hello", "Hello", "These are equal")


if __name__ == '__main__':
    unittest.main()
