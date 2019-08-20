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
Example:

Input:  ar1[] = {1, 4, 5, 7};
        ar2[] = {10, 20, 30, 40};
        x = 32      
Output:  1 and 30

Input:  ar1[] = {1, 4, 5, 7};
        ar2[] = {10, 20, 30, 40};
        x = 50      
Output:  7 and 40
  '''
def printClosest(ar1,ar2,s):
       diff = sys.maxsize
       i =0
       j =len(ar1)-1
       while (i < len(ar1) ) and (j >=0):
              if abs(ar1[i]+ar2[j]-s)< diff:
                 left_index =i
                 right_index =j
                 diff = abs(ar1[i]+ar2[j]-s)
              if ar1[i]+ar2[j] < s :
                   i+=1
              else:
                   j-=1
       return([ar1[left_index],ar2[right_index]])
    




class Test(unittest.TestCase):
      data = [([1, 4, 5, 7],[10, 20, 30, 40],32,[1, 30])]
      def  test_twosum(self):
           print(self.data)
           for input1,input2,target,expected in self.data:
               n1=dt.datetime.now()
               actual =  printClosest(input1,input2,target)
               n2=dt.datetime.now()
               print('Execution Time ',(n2-n1).microseconds,' ms' )
               print('memory % used:', psutil.virtual_memory()[2],'%')
               
               

if __name__ =="__main__":
   unittest.main()

