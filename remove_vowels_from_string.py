#!/usr/bin/python
import unittest

'''
Given a string, remove the vowels from the string and print the string without vowels.
Input : welcome to geeksforgeeks
Output : wlcm t gksfrgks

Input : what is your name ?
Output : wht s yr nm ?
'''

# greedy way
def replace_vowels(string):
    vowels ='aeiou'
    v_list = list(vowels)
    for v in v_list:
        string = string.replace(v,'')
    return string

print(replace_vowels('welcome to geeksforgeeks'))

class Test(unittest.TestCase):
      data = [('what is your name ?','wht s yr nm ?')]
      def  test_replace_vowels(self):
           print(self.data)
           for input,expected in self.data:
               actual = replace_vowels(input)
               self.assertEqual(actual,expected)


if __name__ =="__main__":
   unittest.main()

