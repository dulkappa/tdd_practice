# -*- coding:utf-8 -*-
import unittest
from FizzBuzz import fizzbuzz

class FizzBuzzTest(unittest.TestCase):
  def test_fizzbuzz_get_1(self):
    self.assertEqual(fizzbuzz(1), 1)

  def test_fizzbuzz_get_3(self):
    self.assertEqual(fizzbuzz(3), "Fizz")

  def test_fizzbuzz_get_5(self):
    self.assertEqual(fizzbuzz(5), "Buzz")

if __name__ == "__main__":
  unittest.main()
