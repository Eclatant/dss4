# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser()

# 입력하면 True가 됨
parser.add_argument('--verbose', '-v', action='store_true',
    help='verbose option' )

args = parser.parse_args()

if args.verbose:
    print "verbose output"
    print 'completed'
else:
    print 'completed'
