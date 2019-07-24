#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    print("function started")
    w = int(n / c)
    print("real",w)
    b = 0
    total = 0
    while (b == 0):
        print(w,n)
        h = int(w / m)
        l = int(w % m)
        total += h
        print("wrapper chocolate",total)
        w = h + l
        if w < m:
            print(int(n / c) + total)
            b = 1
        else:
            b = 0


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        chocolateFeast(n, c, m)




