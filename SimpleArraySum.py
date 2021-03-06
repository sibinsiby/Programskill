# Given an array of integers, find the sum of its elements.

#For example, if the array , , so return .

#Function Description

#Complete the simpleArraySum function in the editor below. It must return the sum of the array elements as an integer.

#simpleArraySum has the following parameter(s):

#ar: an array of integers
#Input Format

#The first line contains an integer, , denoting the size of the array.
#The second line contains  space-separated integers representing the array's elements.

#Constraints


#Output Format

#print the sum of the array's elements as a single integer.

#Solution

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    
        return sum(ar) # returns sum of the splitted list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input()) # returns count of list

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
