#!/usr/bin/python
import unittest
import string
import time
import psutil
import datetime as dt
import heapq
import collections
'''
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.

  '''
def sortedSquares(ll):
    left,right=0,len(ll)-1
    result = [None]*len(ll)
    res =right
    while res >=0:
        if ll[left]**2 >= ll[right]**2:
           result[res] = ll[left]**2
           left+=1
        else:
             result[res] = ll[right]**2
             right-=1
        res-=1
    return  result




class Test(unittest.TestCase):
      data = [([-4,-1,0,3,10],[0, 1, 9, 16, 100]),([0,-3,5,1,-10],[0,1,9,25,100])]
      def  test_sortedSquares(self):
           print(self.data)
           for input,expected in self.data:
               n1=dt.datetime.now()
               actual = sortedSquares(input)
               n2=dt.datetime.now()
               print('Execution Time ',(n2-n1).microseconds,' ms' )
               print('memory % used:', psutil.virtual_memory()[2],'%')
               self.assertEqual(actual,expected)


if __name__ =="__main__":
   unittest.main()

