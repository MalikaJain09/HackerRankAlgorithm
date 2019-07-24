#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    b = s

    while (m != 0):
            i = b % n
            if (i == 0):
                i += n
            b += 1
            m -= 1

    print(i)


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        saveThePrisoner(n, m, s)




