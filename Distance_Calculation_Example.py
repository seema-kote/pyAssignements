
# Author name : Kote Seema M ('https://github.com/seema-kote/')
# Created Date : 12th Sep 2017
# Credits: zhiwehu ('https://github.com/zhiwehu') 

"""A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps.
Please write a program to compute the distance from current position after a sequence of movement and original point. 
If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
"""

# Solution

import math
stepCount = 0
initialPt = [0,0]
finalPt = [0,0]
while True:
    steps = raw_input()
    movement = steps.split(" ")
    if movement[0] == 'UP':
        finalPt[0] += int(movement[1])
    elif movement[0] == 'DOWN':
        finalPt[0] -= int(movement[1])
    elif movement[0] == 'LEFT':
        finalPt[1] -= int(movement[1])
    elif movement[0] == 'RIGHT':
        finalPt[1] += int(movement[1])
    else:
        break
distance = math.sqrt((finalPt[1]-initialPt[1]**2)+(finalPt[0]-initialPt[0])**2)                 
print int(round(distance))