__author__ = 'shubhashis'


import unittest

def is_True(number):
    return True

class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""
    def generate_something(self):
        print("hello")

    def test_bal(self):
        self.generate_something();
        self.assertTrue(is_True(5), "Something went Wrong")
        self.assertEqual("Hello", "Helalo", "These are equal")


if __name__ == '__main__':
    unittest.main()
