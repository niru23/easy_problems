#!/usr/bin/python
import unittest

'''
Given a string, remove the vowels from the string and print the string without vowels.
Input : 1.1.1.1
Output : 1[.]1[.]1[.]1

Input : what is your name ?
Output : wht s yr nm ?
'''

# greedy way
def defangIPaddr(ip):
    return ip.replace('.','[.]')

print(defangIPaddr('1.1.1.1'))

class Test(unittest.TestCase):
      data = [('1.1.1.1','1[.]1[.]1[.]1')]
      def  test_defangIPaddr(self):
           print(self.data)
           for input,expected in self.data:
               actual = defangIPaddr(input)
               self.assertEqual(actual,expected)


if __name__ =="__main__":
   unittest.main()

