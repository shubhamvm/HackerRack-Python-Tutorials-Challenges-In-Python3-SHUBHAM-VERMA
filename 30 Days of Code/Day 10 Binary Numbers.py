#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    r = 0
    m = 0

    while n > 0:
        if n % 2 == 1:
            r += 1
            if r > m:
                m = r

        else:
            r = 0

        n //= 2
    print(m)
