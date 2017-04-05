# -*- coding: utf-8 -*-

import unittest

# python unittest1.py
# python unittest1.py -v
# python -m unittest unittest1

class TestSample(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('good'.upper(), 'GOOD')

    # method 명이 test로 시작하지 않으면 수행하지 않음
    def atest_upper(self):
        self.assertEqual('good'.upper(), 'GOOD')

    def test_lower(self):
        self.assertEqual('GOOD'.lower(), 'good')
        #self.assertEqual('GOOD'.lower(), 'goood')

if __name__ == '__main__':
    unittest.main()
