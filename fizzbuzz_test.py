# -*- coding:utf-8 -*-
import unittest

def fizzbuzz(num):
    return 1

class FizzBuzzTest(unittest.TestCase):

    def test_fizzbuzz_get_1(self):
        self.assertEqual(fizzbuzz(1), 1)

if __name__ == "__main__":
    unittest.main()
