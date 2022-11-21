#!/usr/bin/python3
# Passing Test case for checking factorial of numbers

import unittest
from power_of_two import power_of_two


class TestCase(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(power_of_two(7), False)

    def testCase2(self):
        self.assertEqual(power_of_two(8), True)

    def testCase3(self):
        self.assertEqual(power_of_two(512), True)


if __name__ == '__main__':
    unittest.main()