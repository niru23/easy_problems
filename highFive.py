#!/usr/bin/python
import unittest
import string
import time
import psutil
import datetime as dt
import heapq
import collections
'''
Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.
Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.
 
Example 1:
Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.
 
Note:
1 <= items.length <= 1000
items[i].length == 2
The IDs of the students is between 1 to 1000
The score of the students is between 1 to 100
For each student, there are at least 5 scores
'''
items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
'''
student_info ={}
def highFive(items):
    for val in items:
        id = val[0]
        score = val[1]
        if id in student_info :
            student_info[id].append(score)
        else:
        
            student_info[id]= [score]
    student_average =[]
    for key in student_info.keys():
        ll = heapq.nlargest(5, student_info[key])
        avg = sum(ll)/len(ll)
        student_average.append([key,avg])
    return student_average
 '''
def  highFive(items): 
     min_heap = collections.defaultdict(list)
     for id,val in items:
         heapq.heappush(min_heap[id],val*(-1))
     return [[key,(sum(min_heap[key][:5])/5)*(-1)]for key in min_heap.keys()]   
    
class Test(unittest.TestCase):
      data = [([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]],[[1, 87.0], [2, 88.6]])]
      def  test_highFive(self):
           print(self.data)
           for input,expected in self.data:
               n1=dt.datetime.now()
               actual = highFive(input)
               n2=dt.datetime.now()
               print('Execution Time ',(n2-n1).microseconds,' ms' )
               print('memory % used:', psutil.virtual_memory()[2],'%')
               self.assertEqual(actual,expected)


if __name__ =="__main__":
   unittest.main()

