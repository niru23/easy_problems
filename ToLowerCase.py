#!/usr/bin/python
import unittest

'''
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"
'''

# greedy way
def ToLowerCase(string):
    char = list(string)
    lower =[]
    for c in char:
        if ord(c) >= 65 and ord(c)<= 90:
             lower_char = chr(ord(c)+32)
        else:
              lower_char = c
        lower.append(lower_char)
    return ''.join(lower) 



def convertOpposite(string):
  ln = len(string)
  converted =[]
  for i in range(ln):
      char = string[i]
      if char >= 'A' and char <= 'Z':
         converted.append(chr(ord(char)+32))
      elif  char >= 'a' and char <= 'z':
         converted.append(chr(ord(char)-32))
  return ''.join(converted)

print(ToLowerCase('Hello'))
print(ToLowerCase('12345'))
print('ThisIsATest',convertOpposite('ThisIsATest'))
class Test(unittest.TestCase):
      data = [('Hello','hello'),('HELLO','hello')]
      def  test_ToLowerCase(self):
           print(self.data)
           for input,expected in self.data:
               actual = ToLowerCase(input)
               self.assertEqual(actual,expected)


if __name__ =="__main__":
   unittest.main()

