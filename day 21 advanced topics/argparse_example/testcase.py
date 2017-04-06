import unittest
import requests

from ex1 import print_url_n_times


class URLTest(unittest.TestCase):
    def setUp(self):
        url = 'http://www.naver.com'
        self.content = requests.get(url).content

    def test_url(self):
        self.assertEqual(print_url_n_times(3, self.content), True)

if __name__ == '__main__':
    unittest.main()
