# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser()

# 입력하면 True가 됨
parser.add_argument('--verbose', '-v', action='store_true',
    help='verbose option' )

# 필수 입력 필드
parser.add_argument('--number', '-n', required=True, help='number value', type=int)\

# 기본값 입력 가능
parser.add_argument('--value', help='just value', default=100)

args = parser.parse_args()

if args.verbose:
    print "verbose output"

num = int(args.number)
for i in range(num):
    print i,

print args.value
