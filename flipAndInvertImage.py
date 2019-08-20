#!/usr/bin/python
import unittest
import string
import time
import psutil
import datetime as dt
import heapq
import collections
'''
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

Example 1:

Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
Example 2:

Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Notes:

1 <= A.length = A[0].length <= 20
0 <= A[i][j] <= 1
def flipAndInvertImage(ll):
    return [list(1- val for val in row[::-1]) for row in ll]

def flipAndInvertImage(ll):
      return[list(map(lambda x: 0 if x== 1 else 1,row[::-1])) for row in ll]

  '''
def flipAndInvertImage(ll):
    transformed_list=[]
    for val in ll:
        #reverse
        val = val[::-1]  
        # flip
        for i in range(len(val)):
            val[i]=1-val[i]
        transformed_list.append(val)
    return  transformed_list




class Test(unittest.TestCase):
      data = [([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]],[[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]])]
      def  test_flipAndInvertImage(self):
           print(self.data)
           for input,expected in self.data:
               n1=dt.datetime.now()
               actual = flipAndInvertImage(input)
               n2=dt.datetime.now()
               print('Execution Time ',(n2-n1).microseconds,' ms' )
               print('memory % used:', psutil.virtual_memory()[2],'%')
               self.assertEqual(actual,expected)


if __name__ =="__main__":
   unittest.main()

