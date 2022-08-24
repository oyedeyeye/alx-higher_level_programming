#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    positiveNum = number * -1
else:
    positiveNum = number
ld = positiveNum % 10
if number < 0:
    ld *= -1
if ld > 5:
    print(f"ld digit of {number:d} is {ld:d} and is greater than 5")
elif ld == 0:
    print(f"ld digit of {number:d} is {ld:d} and is 0")
elif ld < 6 and ld != 0:
    print(f"ld digit of {number:d} is {ld:d} and is less than 6 and not 0")
