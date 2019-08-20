#!/usr/bin/python
import unittest
import string
import time
import psutil
import datetime as dt
'''
Unique Morse Code Words
Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
'''

alfa = list(string.ascii_lowercase)
morse_code =[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
'''
more_dict ={}
for i in range(len(alfa)):
    mores_dict[alfa[i]] = mores_code[i]

def uniqueMorseRepresentations(words):
     unique_morse_code = set()
     for word in words:
         word_trans  = ''
         for c in word:
             word_trans +=mores_dict[c]
         unique_morse_code.add(word_trans)
     print(unique_mores_code)
     return(len(unique_morse_code))
             
#print(uniqueMorseRepresentations(["gin"]))
'''
def uniqueMorseRepresentations(words):
    unique_code ={"".join( morse_code[ord(c)-ord('a')] for c in word) for word in words}
    return len( unique_code)
        
    
class Test(unittest.TestCase):
      data = [(["gin", "zen", "gig", "msg"],2)]
      def  test_uniqueMorseRepresentations(self):
           print(self.data)
           for input,expected in self.data:
               n1=dt.datetime.now()
               actual = uniqueMorseRepresentations(input)
               n2=dt.datetime.now()
               print('Execution Time ',(n2-n1).microseconds,' ms' )
               print('memory % used:', psutil.virtual_memory()[2],'%')
               self.assertEqual(actual,expected)


if __name__ =="__main__":
   unittest.main()

