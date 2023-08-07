
import math
import os
import random
import re
import sys


def birthdayCakeCandles(candles):
    # Write your code herE
    n = candles_count
    counterH = 0
    high = 0

    for i in range(n):
        if candles[i] > high:
            high = candles[i]
            counterH = 1
        elif candles[i] == high:
            counterH += 1

    return counterH

candles_count = int(input().strip())
candles = list(map(int, input().rstrip().split()))
result = birthdayCakeCandles(candles)

print(str(result) + '\n')

