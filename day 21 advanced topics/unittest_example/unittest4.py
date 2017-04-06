# -*- coding: utf-8 -*-

import unittest

def prime():
    return [2, 3, 5, 7]

def check_email_validity(email):
    if email:
        return True
    else:
        return False

class TestSample(unittest.TestCase):
    def setUp(self):
        pass

    def test_in(self):
        self.assertIn(2, prime())
        self.assertIn(3, prime())
        self.assertIn(4, prime())


    def test_True(self):
        self.assertTrue(2 + 2 == 4)

    def test_sorting(self):
        a = [7, 9, 2, 1, 3, 5]
        self.assertEqual(sort2(a), [1, 2, 3, 5, 7, 9])

        a = [1, 2, 3, 5, 7, 9]
        self.assertEqual(sort2(a), [1, 2, 3, 5, 7, 9])

    def test_email_validity(self):
        e1 = 'ttt@ttt'
        self.assertEqual(check_email_validity(e1), False)

        e1 = 'ttt'
        self.assertFalse(check_email_validity(e1))

        e1 = 'ttt@ttt.com'
        self.assertTrue(check_email_validity(e1))

        e1 = 'ttt-123@gmail.com'
        self.assertTrue(check_email_validity(e1))

    def test_np_intersect1d(self):
        import numpy as np

        a = np.array([1, 2, 3])
        b = np.array([1, 3, 4])

        self.assertEqual(np.insersect1d(a, b), np.array([1, 3]))

        a = np.array([0, 2, 5])
        b = np.array([1, 3, 4])

        self.assertEqual(np.insersect1d(a, b), np.array([]))













if __name__ == '__main__':
    unittest.main()
