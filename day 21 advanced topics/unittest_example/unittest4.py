# -*- coding: utf-8 -*-

import unittest

def prime():
    return [2, 3, 5, 7]

class TestSample(unittest.TestCase):
    def setUp(self):
        pass

    def test_in(self):
        self.assertIn(2, prime())

    def test_True(self):
        self.assertTrue(2 + 2 == 4)

if __name__ == '__main__':
    unittest.main()
