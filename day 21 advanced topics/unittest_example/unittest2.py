# -*- coding: utf-8 -*-

import unittest

def mul(a, b):
    return a * b

class TestSample(unittest.TestCase):

    # test method 호출 직전 실행 됨
    def setUp(self):
        pass

    def test_mul(self):
        self.assertEqual(mul(5, 7), 35)

    def test_string_mul(self):
        self.assertEqual(mul('a', 5), 'aaaaa')

# python abc.py
# python abc.py -v (verbose)
# python -m unittest abc bac cab
if __name__ == '__main__':
    unittest.main()
