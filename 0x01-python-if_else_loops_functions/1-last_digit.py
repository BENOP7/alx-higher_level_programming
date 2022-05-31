#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > -1:
    lastdigit = number % 10
else:
    lastdigit = (-number) % 10 * -1
print('Last digit of {0:d} is {1:d} and'.format(number, lastdigit), end=' ')
if lastdigit == 0:
    print('is 0')
elif lastdigit > 5:
    print('is greater than 5')
else:
    print('is less than 6 and not 0')
