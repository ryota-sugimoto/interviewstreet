#!/usr/bin/env python

import random
num = 10000
bigfile = open("big_input","w")
print >> bigfile, num
for i in xrange(num):
  ope = [ "a", "r"] [ random.randint(0,1) ]
  print >> bigfile, ope, random.randint(-2147483648, 2147483647)
