#!/usr/bin/env python
#coding=utf-8
#13-4-14 上午10:05

import timeit



t = timeit.Timer('print("hello")')
print(t.timeit(3))


t1 = timeit.Timer('''
import urllib2
h = urllib2.urlopen('http://www.hefei4.com/').read()
print(h)
''')
print(t1.timeit(2))