# -*- coding:utf-8 -*-
import unittest
import FizzBuzz

class FizzBuzzTest(unittest.TestCase):
  def test_fizzbuzz_get_1(self):
    self.assertEqual(FizzBuzz(1), 1)

if __name__ == "__main__":
  unittest.main()
