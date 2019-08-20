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
Given an array of integers of size ‘n’.
Our aim is to calculate the maximum sum of ‘k’ 
consecutive elements in the array.

Input  : arr[] = {100, 200, 300, 400}
         k = 2
Output : 700

Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}
         k = 4 
Output : 39
We get maximum sum by adding subarray {4, 2, 10, 23}
of size 4.

Input  : arr[] = {2, 3}
         k = 3
Output : Invalid
There is no subarray of size 3 as size of whole
array is 2.

  '''
MIN_VAL = -sys.maxsize-1
def maxSum_greedy(arr, n, k):
    maxsum = MIN_VAL
    for i in range(n-k+1):
        current_sum =0
        for j in range(k):
            current_sum = current_sum+arr[i+j]
            maxsum =max(current_sum,maxsum)
    return maxsum
    
def maxSum(arr, n, k):
    maxsum = MIN_VAL
    window_sum = sum([arr[i] for i in range(k)])
    for i in range(n-k):
        window_sum = window_sum-arr[i]+arr[i+k]
        maxsum = max(maxsum , window_sum)
    return maxsum




class Test(unittest.TestCase):
      data = [([1, 4, 2, 10, 23, 3, 1, 0, 20],9,4,39)]
      def  test_maxSum(self):
           print(self.data)
           for input,length,window,expected in self.data:
               n1=dt.datetime.now()
               actual = maxSum_greedy(input,length,window)
               n2=dt.datetime.now()
               print('Execution Time ',(n2-n1).microseconds,' ms' )
               print('memory % used:', psutil.virtual_memory()[2],'%')
               self.assertEqual(actual,expected)
               n1=dt.datetime.now()
               actual = maxSum(input,length,window)
               n2=dt.datetime.now()
               print('Execution Time ',(n2-n1).microseconds,' ms' )
               print('memory % used:', psutil.virtual_memory()[2],'%')
               self.assertEqual(actual,expected)


if __name__ =="__main__":
   unittest.main()

