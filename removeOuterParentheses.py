#!/usr/bin/python
import unittest

'''
Input: "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
'''

# greedy way
def removeOuterParentheses(string):
     counter,residue =0,''
     for c in string:
         if c == ')': counter-=1
         if counter != 0: residue+=c
         if c == '(' : counter+=1
     return residue


class Test(unittest.TestCase):
      data = [( "(()())(())", "()()()"),("(()())(())(()(()))","()()()()(())")]
      def  test_removeOuterParenthese(self):
           print(self.data)
           for input,expected in self.data:
               actual = removeOuterParentheses(input)
               self.assertEqual(actual,expected)


if __name__ =="__main__":
   unittest.main()

