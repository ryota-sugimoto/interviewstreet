#!/usr/bin/env python
import sys
import bisect
import random
import time
class RangeCache:
  def __init__(self, m, n):
    self.cache = {}
  def __call__(self, m, n):
    try:
      return self.cache[(m,n)]
    except KeyError:
      self.cache[(m,n)] = xrange(m,n)
      return self.cache[(m,n)]
      
      
class Requirements:
  def __init__(self, num, requirements):
    self.num = num
    self.reqs = requirements
    self.optimize()
    self.make_cache()
    self.rangeCache = RangeCache(0,10)
    
  def make_cache(self):
    self.cache = {}
    for req in self.reqs:
      for index in req:
        try:
          self.cache[index].append(req)
        except KeyError:
          self.cache[index] = [ req ]
   
  def optimize(self):
     def req_count(reqs):
       count = {}
       for req in reqs:
         for index in req:
           count[index] = count.get(index, 0) + 1
       return count
     count = req_count(self.reqs)
     opt_indices = sorted(count.keys(),
                          key = lambda key: count[key],
                          reverse = True)
     no_related = set(range(self.num)) - set(opt_indices)
     opt_indices = opt_indices + sorted(list(no_related))
     res = []
     for req in self.reqs:
         res.append([opt_indices[req[0]], opt_indices[req[1]]])
     self.reqs = res
       
  def __call__(self, index):
    return self.cache.get(index, [])
      
  def allowed_num(self, assigned_num, index):
    min = 0
    max = 10
    for req in self(index):
      if req[0] == index:
        tar = req[1]
        if tar < index:
          tmp = assigned_num[tar]+1
          max = tmp if tmp < max else max
      else:
        tar = req[0]
        if tar < index:
          tmp = assigned_num[tar]
          min = tmp if tmp > min else min
    return self.rangeCache(min,max)
  
rec = 0
class Variables:
  def __init__(self, num, requirements):
    self.num = num
    self.reqs = requirements
  
  def solve(self):
    def inner_solve(assigned_num = [None] * self.num, index = 0, count = 0):
      global rec
      rec = rec + 1
      if index == self.num:
        return count + 1
      else:
        range = self.reqs.allowed_num( assigned_num, index )
        for i in range:
          assigned_num[index] = i
          count = inner_solve(assigned_num, index+1, count)
      return count
    global rec
    res = inner_solve()
    print >> sys.stderr, "recursive:", rec
    return res


def reader(file):
  (var_num, req_num) = map(int, file.next().split())
  reqs = []
  for i in xrange(req_num):
    reqs.append(map(int, file.next().split()))
  
  var = Variables(var_num, Requirements(var_num, reqs))
  return var.solve()

if __name__ == '__main__':
  begin = time.clock()
  print >> sys.stderr, reader(sys.stdin) % 1007
  print >> sys.stderr, time.clock() - begin
