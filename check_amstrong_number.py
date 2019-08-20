#!/usr/bin/python
import unittest

'''
Given a string, remove the vowels from the string and print the string without vowels.
Input : 663
Output : no
Input : 153
Output : yes
'''

# greedy way
def isArmstrongNum(num,size):
    temp = num
    sum =0
    while temp >0:
        digit = temp%10
        sum+= digit**size
        temp = temp//10
    return sum == num 

print(isArmstrongNum(153,3))

class Test(unittest.TestCase):
      data = [(153,3,True),(163,3,False)]
      def  test_isArmstrongNum(self):
           print(self.data)
           for input,size,expected in self.data:
               actual = isArmstrongNum(input,size)
               self.assertEqual(actual,expected)


if __name__ =="__main__":
   unittest.main()

