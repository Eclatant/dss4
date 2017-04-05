# -*- coding: utf-8 -*-

import argparse
parser = argparse.ArgumentParser()

# 정수형임을 암시
parser.add_argument("square", help="calculate square value of the number",
                    type=int)

args = parser.parse_args()

print args.square ** 2
