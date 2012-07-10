#!/usr/bin/env python
import bisect

import sys
import time

timestamp = []

class EmptyList: pass

class Median:
  def __init__(self):
    self.data = []
    
  def operation(self, command, value):
    begin = time.clock()
    if command == "add":
      bisect.insort_left(self.data, value)
    elif command == "remove":
      self.data.remove(value)
    timestamp.append(time.clock() - begin)
  
  def __call__(self):
    if len(self.data) == 0: raise EmptyList()
    center = int(len(self.data)/2)
    if len(self.data) % 2:
      return self.data[center]
    else:
      res = (self.data[center-1] + self.data[center])/2.0
      return res

class Reader:
  def __init__(self, file):
    self.file = file
    self.num_of_operation = int(self.file.next())
    self.median = Median()
  
  def next(self):
    def parser(line):
      operation = { "a": "add", "r": "remove" }
      res = [operation[line.split()[0]], int(line.split()[1])]
      return res
    
    def formatter(value):
      if value%1:
        return str(value)
      else:
        return '%i' % value
    
    try:
      line = self.file.next()
      self.median.operation(*parser(line))
      return formatter(self.median())
    except (ValueError, EmptyList):
      return "Wrong!"

  def __iter__(self):
    return self


if __name__ == '__main__':
  import sys
  processbegin = time.clock()
  for i in Reader(sys.stdin):
    print i

  print >> sys.stderr, "total time:", time.clock() - processbegin
  print >> sys.stderr, sum(timestamp)/len(timestamp)
