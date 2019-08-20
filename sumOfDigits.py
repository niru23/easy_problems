#!/usr/bin/python
import unittest
import string
import time
import psutil
import datetime as dt
import heapq
import collections
'''
Given an array A of positive integers, let S be the sum of the digits of the minimal element of A.
Return 0 if S is odd, otherwise return 1.
 
Example 1:
Input: [34,23,1,24,75,33,54,8]
Output: 0
Explanation: 
The minimal element is 1, and the sum of those digits is S = 1 which is odd, so the answer is 0.
Example 2:
Input: [99,77,33,66,55]
Output: 1
Explanation: 
The minimal element is 33, and the sum of those digits is S = 3 + 3 = 6 which is even, so the answer is 1.
 
Note:
1 <= A.length <= 100
1 <= A[i].length <= 100
 '''
def sumOfDigits(ll):
    if len(ll) == 0:
        print('List is empty')
        return
    else:
        minval = min(ll)
        temp = minval
        digit_sum =0
        while temp != 0:
            digit = temp%10
            digit_sum =digit_sum +digit
            temp = temp//10
    
    if   digit_sum%2 == 0: return 1
    else: return 0     
    
class Test(unittest.TestCase):
      data = [([34,23,1,24,75,33,54,8],0),([99,77,33,66,55],1)]
      def  test_highFive(self):
           print(self.data)
           for input,expected in self.data:
               n1=dt.datetime.now()
               actual = sumOfDigits(input)
               n2=dt.datetime.now()
               print('Execution Time ',(n2-n1).microseconds,' ms' )
               print('memory % used:', psutil.virtual_memory()[2],'%')
               self.assertEqual(actual,expected)


if __name__ =="__main__":
   unittest.main()

