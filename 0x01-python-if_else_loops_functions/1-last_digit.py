#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldigit = -1 * ((- number) % 10) if number < 0 else number % 10
if ldigit > 5:
    print(f"Last digit of {number:d} is {ldigit:d} and is greater than 5")
elif ldigit == 0:
    print(f"Last digit of {number:d} is {ldigit:d} and is 0")
else:
    print(f"Last digit of {number:d} is {ldigit:d} and is less\
 than 6 and not 0")