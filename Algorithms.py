import sys

import numpy as np
import heapq
from queue import LifoQueue
from Vertex import Vertex


def checkInput(arr, n):
    counter = 0
    num = 0
    i = 0
    while i < n:
        if arr[i] == 0:
            if i < 4:
                counter += 1
            elif i < 8:
                counter += 2
            elif i < 12:
                counter += 3
            elif i < 16:
                counter += 4
            if i == n -1:
                return counter
            i = i + 1
        num = arr[i]
        j = i
        while j < n:
            if arr[j] < num and arr[j] != 0:
                counter = counter + 1
            j += 1
        i += 1
    return  counter



#THE FIRST ALGORITHM IS: BFS
def BFS(initialState, n):
    GoalState = generateGoalState(n)
    root = Vertex(initialState, None, None, 0, 0)
    if root.isGoal(GoalState):
        return root.solution()

    OpenList = []
    OpenList.append(root)
    CloseList = []

    while not (len(OpenList) == 0):
        current_node = OpenList.pop(0)
        CloseList.append(current_node.state)

        children = current_node.discoverChildren(n) #discover children set the children pay to curr node

        for child in children:
            if child.state in CloseList or child in OpenList:
                children.remove(child)

        for child in children:
            if child.state not in CloseList:
                if child.isGoal(GoalState):
                    return child.solution(), len(CloseList)
                OpenList.append(child)
    return


#THE SECOND ALGORITHM: IDS - ITERATIVE DEPTH SEARCH
def IDS(initialState, n):
    GoalState=generateGoalState(n)
    root = Vertex(initialState, None, None, 0, 0)

    depth=0
    result=None
    while result == None: #While you didn't find the solution increase the depth in 1
        result = deepthLimitedDFS(root, GoalState, depth, n)
        depth += 1
    return result

#HELP FUNCTION
def deepthLimitedDFS(start,GoalState,depth,n):
    openList = []
    openList.append(start)
    while True:
        if len(openList) == 0:
            return None
        actual = openList.pop(0)
        if actual.isGoal(GoalState):
            return actual.solution(), len(openList)
        elif actual.depth is not depth:
                succ = actual.discoverChildren(n)
                openList.extend(succ)



#THE THIRD ALGORITHM IS: A*
def aStar(initialState, n):
    GoalState = generateGoalState(n)
    root = Vertex(initialState, None, None, 0, 0)
    if root.isGoal(GoalState):
        return root.solution()

    OpenList = []
    OpenList.append(root)
    CloseList = []

    while len(OpenList) > 0:
        result = minHeuristic(OpenList)
        curr_node = result[0]
        if curr_node.isGoal(GoalState):
            return curr_node.solution(), len(CloseList)
        OpenList.pop(result[1])
        CloseList.append(curr_node)

        children = curr_node.discoverChildren(n)

        for node in children:
            if node not in CloseList:
                newPotentialCost = curr_node.cost + 1
            if not isExist(OpenList, node, newPotentialCost, n):
                node.cost = newPotentialCost
                node.heuristic = heuristicFunc(node, n)
                node.pai = curr_node
                OpenList.append(node)
    return None

#isExist() is a help func that checks if node exist in open list and if it does,
#update the g() value (cost from root value) if it is necessary
def isExist(openlist, v, newPotentialCost, n):
    if len(openlist) == 0:
        return False
    flag = False
    for i, node in enumerate(openlist):
        if v == node:
            if newPotentialCost < openlist[i].cost:
                openlist[i].cost = newPotentialCost
                openlist[i].heuristic = heuristicFunc(openlist[i], n)
                openlist[i].pai = v
                flag = True
    return flag



def minHeuristic(openlist):
    minH = sys.maxsize
    indexOfMinNode = 0
    for i, node in enumerate(openlist):
        if node.heuristic < minH:
            minH = node.heuristic
            indexOfMinNode = i
    result = [openlist[indexOfMinNode],indexOfMinNode]
    return result


def generateGoalState(n):
    GoalState=[]
    for x in range(np.power(n, 2)):
        GoalState.append(x + 1)
    GoalState[np.power(n, 2) - 1] = 0
    return GoalState

def heuristicFunc(node, n):
    return node.g() + node.h(n)