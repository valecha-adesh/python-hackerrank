"""Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.

For example, if Gary's path is , he first enters a valley  units deep. Then he climbs out an up onto a mountain  units high. Finally, he returns to sea level and ends his hike.

Function Description

Complete the countingValleys function in the editor below. It must return an integer that denotes the number of valleys Gary traversed.

countingValleys has the following parameter(s):

n: the number of steps Gary takes
s: a string describing his path
Input Format

The first line contains an integer , the number of steps in Gary's hike. 
The second line contains a single string , of  characters that describe his path.

Constraints

Output Format

Print a single integer that denotes the number of valleys Gary walked through during his hike."""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    count = 0
    l = s[:]
    temp = []
    for i in range(n):
        if(l[i] == 'U'):
            temp.append(-1)
        else:
            temp.append(1)

        if (i % 2 != 0):
            if(sum(temp) == 0):
                if (temp[0]==1):
                    count = count + 1
                temp = []

    return count


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
