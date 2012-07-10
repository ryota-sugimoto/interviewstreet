#!/usr/bin/env python

class EmptyList: pass

class Median:
  def __init__(self):
    self.data = []
    
  def operation(self, command, value):
    if command == "add":
      self.data.append(value)
      self.data.sort()
    elif command == "remove":
      if value in set(self.data):
        self.data.remove(value)
      else: raise ValueError
  
  def __call__(self):
    if len(self.data) == 0: raise EmptyList()
    center = int(len(self.data)/2)
    if len(self.data) % 2:
      return self.data[center]
    else:
      return (self.data[center-1] + self.data[center])/2.0

class Reader:
  def __init__(self, file):
    self.file = file
    self.num_of_operation = int(self.file.next())
    self.median = Median()
  
  def next(self):
    def parser(line):
      operation = { "a": "add", "r": "remove" }
      return [operation[line.split()[0]], int(line.split()[1])]
    
    def formatter(value):
      if value%1:
        return str(value)
      else:
        return '%i' % value
    
    try:
      self.median.operation(*parser(self.file.next()))
      return formatter(self.median())
    except (ValueError, EmptyList):
      return "Wrong!"
  
  def __iter__(self):
    return self

if __name__ == '__main__':
  import sys
  for i in Reader(sys.stdin):
    print i
  
