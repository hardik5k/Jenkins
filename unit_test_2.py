#!/usr/bin/python3
# Passing Test case for checking factorial of numbers

import unittest
from power_of_two import power_of_two


class TestCase(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(power_of_two(0), False)

    def testCase2(self):
        self.assertEqual(power_of_two(8.5), False)



if __name__ == '__main__':
    unittest.main()