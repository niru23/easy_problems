#!/usr/bin/python
import unittest
import string
import time
import psutil
import datetime as dt
import heapq
import collections
import sys
'''
Given a sorted array A (sorted in ascending order), having N integers, find if there exists any pair of elements (A[i], A[j]) such that their sum is equal to X.
  '''
def twosum_greedy(arr,s):
    result =[]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i]+arr[j] == s:
                result.append([arr[i],arr[j]])
    return result
    
def twosum_pointers(arr,s):
      i =0
      j = len(arr)-1
      result =[]
      while i< j:
          if arr[i]+arr[j] ==s:
              result.append(sorted([arr[i],arr[j]]))
          if arr[i]+arr[j] < s:
               i+=1
          else:
                j-=1
      return result
    
class Test(unittest.TestCase):
      data = [( [-4,2,3,5,8,11] ,7,[[-4, 11], [2, 5]])]
      def  test_twosum(self):
           print(self.data)
           for input,target,expected in self.data:
               n1=dt.datetime.now()
               actual = twosum_greedy(input,target)
               n2=dt.datetime.now()
               print('Execution Time ',(n2-n1).microseconds,' ms' )
               print('memory % used:', psutil.virtual_memory()[2],'%')
               n1=dt.datetime.now()
               actual = twosum_pointers(input,target)
               n2=dt.datetime.now()
               print('Execution Time ',(n2-n1).microseconds,' ms' )
               print('memory % used:', psutil.virtual_memory()[2],'%')
               

if __name__ =="__main__":
   unittest.main()

