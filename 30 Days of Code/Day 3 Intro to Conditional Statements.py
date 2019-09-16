#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
if (n%2 == 0):
    if(n>21) or (n==2) or (n==4):
        print("Not Weird")
    else:
        print("Weird")
else:
    print("Weird")
