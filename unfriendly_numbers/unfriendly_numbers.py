#!/usr/bin/env python
import time
import sys
def int_factorize(n):
  def prime():
    yield 2
    yield 3
    i = 5
    while True:
      yield i
      if i % 6 == 1:
        i += 2
      i += 2
  
  def dividable(n, denominator, count = 0):
    if n % denominator == 0:
      count = count + 1
      return dividable(n/denominator, denominator, count)
    else:
      return (count, n)
  
  decomposed = {}
  divided = n
  for p in prime():
    if divided == 1:
      return decomposed
    else:
      (count, divided) = dividable(divided, p)
      if count != 0:
        decomposed[p] = count

def gen_divisor(decomposed):
  if decomposed:
    prime = decomposed.keys()[0]
    factor = [ prime ** i for i in xrange(decomposed[prime] + 1) ]
    del decomposed[prime]
    res = []
    for i in gen_divisor(decomposed):
      res = res + [ j * i for j in factor ]
    return res
  else:
    return [1]

def Euclidean(m, n):
  if n == 0:
    return m
  else:
    return Euclidean(n, m%n)

class UnfriendlyNumber:
  def __init__(self, friendNumber, UnfriendNumbers):
    self.friendNumber = friendNumber
    self.UnfriendNumbers = UnfriendNumbers
  
  def __call__(self):
    begin = time.clock()
    GCDs = []
    for UnfriendNumber in self.UnfriendNumbers:
      GCD = Euclidean(*sorted([self.friendNumber, UnfriendNumber]))
      if not filter(lambda x: not(x % GCD), GCDs):
        GCDs.append(GCD)
    GCDs_factorized = map(int_factorize, GCDs)
    common_divisors = reduce(lambda x,y: set(x).union(set(y)),
                             map(gen_divisor, GCDs_factorized))
    fnum_divisors = gen_divisor(int_factorize(self.friendNumber))
    res = len(filter(lambda x: x not in common_divisors, fnum_divisors))
    print >> sys.stderr, "time:", time.closk() - begin
    return res

class Reader:
  def __init__(self, file):
    self.file = file
    (self.num_of_unf, self.friendNumber) = map(int,
                                          self.file.next().strip().split())
    self.unfriendNumber = UnfriendlyNumber(self.friendNumber, 
                                      map(int,
                                          self.file.next().strip().split())
                                     )
  
  def __repr__(self):
    return str(self.unfriendNumber())

if __name__ == "__main__":
  import sys
  print Reader(sys.stdin)
