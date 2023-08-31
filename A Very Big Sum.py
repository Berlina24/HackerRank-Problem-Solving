
import math
import os
import random
import re
import sys

def aVeryBigSum(ar):
    total = 0

    for i in ar:
        total += i
    return total


ar_count = int(input().strip())

ar = list(map(int, input().rstrip().split()))

result = aVeryBigSum(ar)

print(str(result) + '\n')


