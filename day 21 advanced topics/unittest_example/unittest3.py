# -*- coding: utf-8 -*-

import unittest

class TestSample(unittest.TestCase):
    # 최초에 한번 실행
    @classmethod
    def setUpClass(cls):
        print 'setupClass'

    # 마지막에 실행
    @classmethod
    def tearDownClass(cls):
        print 'tearDownClass'

    # 매번 테스트 메쏘드 수행 전 실행
    def setUp(self):
        print '\nsetup method is called'

    def test_upper(self):
        self.assertEqual('good'.upper(), 'GOOD')

    # method 명이 test로 시작하지 않으면 수행하지 않음
    def testupper(self):
        self.assertEqual('good'.upper(), 'GOOD')

    def test_lower(self):
        self.assertEqual('GOOD'.lower(), 'good')
        #self.assertEqual('GOOD'.lower(), 'goood')

    # 매 테스트 메쏘드 수행 후 실행
    def tearDown(self):
        print 'tearDown is called'

if __name__ == '__main__':
    unittest.main()
