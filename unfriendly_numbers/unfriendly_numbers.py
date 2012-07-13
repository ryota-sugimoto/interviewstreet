#!/usr/bin/env python
import time
import sys


class Teller:
  def __init__(self,values):
    self.values = values
 
  def __repr__(self):
    return "Telling: " + " ".join(map(str,self.values))

def timestamp(begin,comment = ""):
   print >> sys.stderr, comment, str(time.clock() - begin)

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
    call_begin = time.clock()
    GCDs = []
    begin = time.clock()
    for unfnum in self.UnfriendNumbers:
      GCDs.append(Euclidean(self.friendNumber, unfnum))
    timestamp(begin, "euclidean:")
    
    begin = time.clock()
    GCDs_factorized = map(int_factorize, GCDs)
    timestamp(begin, "gcd factorize:")
    
    begin = time.clock()
    common_divisors = map(gen_divisor, GCDs_factorized)
    timestamp(begin, "gen common divisor:")
    
    begin = time.clock()
    uniq_common_divisors = reduce(lambda x,y: set(x).union(set(y)),
                                  common_divisors )
    timestamp(begin, "uniq common divisor:")
    
    begin = time.clock()
    friend_decomposed = int_factorize(self.friendNumber)
    timestamp(begin, "friend factorize:")
    
    begin = time.clock()
    fnum_divisors = gen_divisor(friend_decomposed)
    timestamp(begin, "cal friendnum divisor:")
    
    begin = time.clock()
    res = len(filter(lambda x: x not in common_divisors, fnum_divisors))
    timestamp(begin, "cal result:")
    timestamp(call_begin, "call all:")
    return res

class Reader:
  def __init__(self, file):
    self.file = file
    (self.num_of_unf, self.friendNumber) = map(int,
                                          self.file.next().split())
    self.unfriendNumber = UnfriendlyNumber(self.friendNumber, 
                                      map(int,
                                          self.file.next().split())
                                     )
  
  def __repr__(self):
    begin = time.clock()
    res = str(self.unfriendNumber())
    print >> sys.stderr, "read:", time.clock() - begin
    return res

if __name__ == "__main__":
  import sys
  print Reader(sys.stdin)
