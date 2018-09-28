#!/usr/bin/env python
# -*- coding: utf-8 -*-

from function import *

from optparse import OptionParser
import sys

if(len(sys.argv) <= 1): # 인자 첫번째는 실행 파일이 들어가므로 무조건 길이는 1 이상이다.
	print("test.py -h 또는 --help 를 입력해 메뉴얼을 참조하세요.")
	exit()

use = "Usage: %prog [options] number"
parser = OptionParser(usage = use)
parser.add_option("-g", "--colG", dest="colG", default=False, action="store_true", help="19n+1")
parser.add_option("-p", "--colAappend", dest="colAappend", default=False, action="store_true", help="collatz all text append")
parser.add_option("-b", "--colBappend", dest="colBappend", default=False, action="store_true", help="collatzb all text append")
options, args = parser.parse_args()

if options.colG:
    collatg(int(args[0]))
    input()
elif options.colAappend:
	collatzTextAppend(int(args[0]))
elif options.colBappend:
	collatzbTextAppend(int(args[0]))




