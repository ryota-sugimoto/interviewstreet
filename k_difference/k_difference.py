#!/usr/bin/env python
import sys
import bisect

class K_Difference:
  def __init__(self, K, Numbers):
    self.K = K
    self.Numbers = Numbers

  def __repr__(self):
    commenout = '''def inner_search(nums, count = 0):
      if nums:
        target = self.K + nums[0]
        index = bisect.bisect_left(nums[1:], target) + 1
        try:
          if nums[index] == target:
            count = count + 1
        except IndexError: pass
        return inner_search(nums[1:],count)
      else:
        return count
    '''
    
    def inner_search(nums):
      offset = 0
      count = 0
      for n in nums:
        target = self.K + n
        index = bisect.bisect_left(nums, target, lo=offset+1)
        try:
          if nums[index] == target:
            count = count + 1
        except IndexError: pass
        offset = offset + 1
      return count
    
    try: 
      return self.result
    except AttributeError:
      self.result = str(inner_search(sorted(self.Numbers)))
      return self.result

if __name__ == '__main__':
  (N, K) = map(int, sys.stdin.next().split())
  nums = map(int,sys.stdin.next().split())
  
  print K_Difference(K, nums)
