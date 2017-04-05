# -*- coding: utf-8 -*-

# help text 예제
# 실행 인자를 주지 않을 경우, 자동으로 help text 안내

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("num", help="number you want to print from 1")
args = parser.parse_args()

num = int(args.num)

for i in range(1, num+1):
    print i,


# python argparse_ex1.py 10
