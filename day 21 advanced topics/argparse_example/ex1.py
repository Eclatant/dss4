# -*- coding: utf-8 -*-

import argparse
import requests

from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()

# 파라미터의 개수를 가변적으로 설정
parser.add_argument('--number', '-n', help='number of requests', type=int)
parser.add_argument('--url', '-u', help='url to make http request')
args = parser.parse_args()

number = args.number
url = args.url

def print_url_n_times(number, web_content):
    for i in range(number):
        try:
            soup = BeautifulSoup(web_content, "html5lib")
            print soup.title.get_text()
        except:
            return False

    return True

print_url_n_times(number, url)
