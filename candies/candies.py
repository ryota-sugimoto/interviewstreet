#!/usr/bin/env python
import sys

class Teller: 
  def __init__(self, value):
    self.value = value
  
  def __repr__(self):
    return str(self.value)

class Child:
  def __init__(self, score, candy):
    self.score = score
    self.candy = candy

  def jealous(self, child):
    try:
      cond1 = (self.score > child.score) and (self.candy <= child.candy)
      return cond1
    except AttributeError:
      return False
  
class AliceClass:
  def __init__(self, scores, default_candy = 1):
    self.children = map(lambda score: Child(score, default_candy), scores)
  
  def tortalCandies(self):
    return sum([child.candy for child in self])
  
  def whoIsJealous(self):
    res = []
    for index, child in enumerate(self):
      try:
        prev = self.children[ index - 1 ]
      except IndexError:
        prev = None
      try:
        next = self.children[ index + 1 ]
      except IndexError:
        next = None
      
      if child.jealous(prev) or child.jealous(next):
        res.append(index)
    return res
  
  def feedCandies(self):
    jealousChildren = self.whoIsJealous()
    if jealousChildren:
      for index in jealousChildren:
        self.children[index].candy = self.children[index].candy + 1
      self.feedCandies()

  def __iter__(self):
    return iter(self.children)
  
def reader(file):
  num_of_child = int(file.next())
  return AliceClass([ float(file.next()) for i in xrange(num_of_child) ])
  
if __name__ == '__main__':
  aliceClass = reader(sys.stdin)
  aliceClass.feedCandies()
  #for child in aliceClass:
  #  print child.score, child.candy
    
  print int(aliceClass.tortalCandies())
