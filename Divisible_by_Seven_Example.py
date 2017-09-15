# Author name : Kote Seema M ('https://github.com/seema-kote/')
# Created Date : 12th Sep 2017
# Credits: zhiwehu ('https://github.com/zhiwehu') 

"""
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

# Solution

def divisibleSeven(number):
    if number % 7 == 0:
        return True
    else:
        return False
def isMultipleFive(number):
    if number % 5 == 0:
        return True
    else:
        return False
list = []
for number in range(2000, 3200):
    if divisibleSeven(number):
        if not(isMultipleFive(number)):
            list.append(number)
print list


