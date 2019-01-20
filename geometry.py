# geometry.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
# 
# Created by Jongdeog Lee (jlee700@illinois.edu) on 09/12/2018

"""
This file contains geometry functions that relate with Part1 in MP2.
"""

import math
import numpy as np
from const import *

def computeCoordinate(start, length, angle):
    """Compute the end cooridinate based on the given start position, length and angle.

        Args:
            start (tuple): base of the arm link. (x-coordinate, y-coordinate)
            length (int): length of the arm link
            angle (int): degree of the arm link from x-axis to couter-clockwise

        Return:
            End position of the arm link, (x-coordinate, y-coordinate)
    """

    
    endx = start[0] + length * math.cos(angle * math.pi /180)
    endy = start[1] - length * math.sin(angle * math.pi /180)
    return (endx,endy)

def doesArmTouchObstacles(armPos, obstacles):
    """Determine whether the given arm links touch obstacles

        Args:
            armPos (list): start and end position of all arm links [(start, end)]
            obstacles (list): x-, y- coordinate and radius of obstacles [(x, y, r)]

        Return:
            True if touched. False it not.
    """    
# source for equation = https://math.stackexchange.com/questions/275529/check-if-line-intersects-with-circles-perimeter : anwsered by ryu zen
    for j in obstacles:
        for i in armPos:
            x1 = i[0][0] 
            x2 = i[1][0] 
            y1 = i[0][1] 
            y2 = i[1][1] 
            xo = j[0]
            yo = j[1]
            r = j[2]

            # math below from aforementioned source

            ax = x1 - xo 
            ay = y1 - yo 
            bx = x2 - xo 
            by = y2 - yo 

            c = ax**2 + ay**2 - r**2;
            b = 2 * ( ax * (bx - ax) + ay * (by - ay))
            a = (bx - ax)**2 + (by - ay)**2;
            disc = b**2 - 4 * a * c
            if disc <= 0:
                continue
            discsqrt = math.sqrt(disc)
            t1 = (-b + discsqrt)/(2*a);
            t2 = (-b - discsqrt)/(2*a);
            if((0 < t1 and t1 < 1) or (0 < t2 and t2 < 1)):
                return True;

    return False

def doesArmTouchGoals(armEnd, goals):
    """Determine whether the given arm links touch goals

        Args:
            armEnd (tuple): the arm tick position, (x-coordinate, y-coordinate)
            goals (list): x-, y- coordinate and radius of goals [(x, y, r)]

        Return:
            True if touched. False it not.
    """

    for i in goals:
        if ((armEnd[0] - i[0]) ** 2 +(armEnd[1] - i[1]) ** 2) <= (i[2]**2):
            return True
    return False


def isArmWithinWindow(armPos, window):
    """Determine whether the given arm stays in the window

        Args:
            armPos (list): start and end position of all arm links [(start, end)]
            window (tuple): (width, height) of the window

        Return:
            True if all parts are in the window. False it not.
    """
    # print(armPos)
    for i in armPos:
        # print(i)
        if i[1][0] < 0 or i[1][0] > (window[0]-1) or  i[1][1] < 0 or i[1][1] > (window[1]-1) :
            return False
    return True