#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input())

c = list(map(int, input().rstrip().split()))


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count=0
    for i in range(len(c)):
        if c[i]!=1:

            count=count+1
            if i <=(len(c)-4):

              if c[i+1]==0 and c[i+2]==0 :
                print(i+1,i+2)
                count -=1
                if c[i+2]==0 and c[i+3]==0 :
                      print(i+2,i+3)
                      count +=1
                      if c[i+3]==0 and c[i+4]==0:

                          count-=1
                          if c[i + 4] == 0 and c[i + 5] == 0:
                              count += 1
                              if c[i+5]==0 and c[i+6]==0:
                                  count-=1
                                  if c[i+6]==0 and c[i+7]==0:
                                      count+=1


    return count-1



result = jumpingOnClouds(c)
print(result)

