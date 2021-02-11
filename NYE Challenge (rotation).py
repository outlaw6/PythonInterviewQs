import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    numOfSwaps=0
    flag = False
    for x in range(len(q) - 1, -1, -1):
        print("Current index: " + str(x) + "")
        if q[x] - (x+1) > 2:
            flag = True
            return
            #return "Too chaotic"
        
        for y in range(max(0, q[x] - 2), x):
            if q[y] > q[x]:
                numOfSwaps+=1
    return numOfSwaps



if __name__ == '__main__':

    num=1
    testList = [5,1,2,3,7,8,6,4]
    num = minimumBribes(testList)
    print(type(num))
    if (num) > 2:
        print("Too chaotic")
        print(num)


