# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser()

# 파라미터의 개수를 2개로 설정
parser.add_argument('--number', help='numbers to be added', nargs=2)
args = parser.parse_args()


print sum([int(i) for i in args.number])

#python argparse_ex5.py --number  3 4
