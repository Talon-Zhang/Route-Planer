
# transform.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
# 
# Created by Jongdeog Lee (jlee700@illinois.edu) on 09/12/2018

"""
This file contains the transform function that converts the robot arm map
to the maze.
"""
import copy
from arm import Arm
from maze import Maze
from search import *
from geometry import *
from const import *
from util import *
import numpy as np

def transformToMaze(arm, goals, obstacles, window, granularity):
    """This function transforms the given 2D m
    ap to the maze in MP1.
    
        Args:
            arm (Arm): arm instance
            goals (list): [(x, y, r)] of goals
            obstacles (list): [(x, y, r)] of obstacles
            window (tuple): (width, height) of the window
            granularity (int): unit of increasing/decreasing degree for angles

        Return:
            Maze: the maze instance generated based on input arguments.

    """
    '''
    Constants to Use:
    WALL_CHAR = '%'

    START_CHAR = 'P'

    OBJECTIVE_CHAR = '.'

    SPACE_CHAR = ' '
    '''
    maxArm = arm.getArmLimit()
    offsets = (maxArm[0][0], maxArm[1][0])


    #compute number of rows of maze- alphas
    #numRows = ((maxArm[0][1] - offsets[0])/granularity) + 1
    
    numRows = int(((maxArm[0][1] - offsets[0])/granularity) + 1)


    #compute number of columns of maze- betas
    #numCols = ((maxBeta - offsets[1])/granularity) + 1
    numCols = int(((maxArm[1][1] - offsets[1])/granularity) + 1)


    #2d array which will be the maze
    #input_map = np.zeros((numRows, numCols))
    input_map =[]
    #input_map = [[SPACE_CHAR for a in range(numCols)] for b in range(numRows)]

    #will need flags for checking whether we have already marked something as a startCharacter or objectiveChar

    startPosition = arm.getArmAngle()
    startAlpha = round((startPosition[0] - offsets[0])/granularity)
    startBeta = round((startPosition[1] - offsets[1])/granularity)
 
    for alpha in range(numRows):
        input_map.append([])
        alphaAngle = offsets[0] + (granularity * alpha)
        for beta in range(numCols):
            input_map[alpha].append(' ')
            betaAngle = offsets[1] + (granularity * beta)
            #set the arm angle now that we have alphaAngle and betaAngle
            arm.setArmAngle((alphaAngle,betaAngle))

            #if we arrive at an obstacle or are past the boundary of the game window, 
            if(doesArmTouchObstacles(arm.getArmPos(),obstacles) or isArmWithinWindow(arm.getArmPos(),window)==False):
                input_map[alpha][beta] = "%"
            elif( doesArmTouchGoals(arm.getEnd(),goals)):
                input_map[alpha][beta]= "."
                # objectiveChar = True

    input_map[startAlpha][startBeta] = "P"
    #return the Maze instance with the created input map
    return Maze(input_map,offsets,granularity)
    #saveToFile(self, "mazeOutput.txt")

    pass
