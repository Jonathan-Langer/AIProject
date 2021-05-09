
import numpy as np
from queue import PriorityQueue
from Vertex import Vertex


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

        children = current_node.discoverChildren(n)

        for child in children:
            if child.state in CloseList or child in OpenList:
                children.remove(child)

        for child in children:
            if child.state not in CloseList:
                if child.isGoal(GoalState):
                    return child.solution(), len(CloseList)
                OpenList.append(child)
    return


def aStar(initialState, n):
    GoalState = generateGoalState(n)
    root = Vertex(initialState, None, None, 0, 0)
    if root.isGoal(GoalState):
        return root.solution()
    OpenList = []
    OpenList.append(root)
    CloseList = []
    while len(OpenList) > 0:
        curr_node = OpenList.pop(0)
        if curr_node.isGoal(GoalState):
            return curr_node.solution(), len(CloseList)
        min_node = minV(curr_node.discoverChildren(n), n, GoalState)  # returns the node with the min f(n) from curr_node children
        CloseList.append(curr_node.state)
        if min_node.state not in CloseList:
            if min_node.isGoal(GoalState):
                return min_node.solution(), len(CloseList)
            else:
                OpenList.append(min_node)
    return



def minV(openlist, n, GoalState):
    openlist.sort(reverse=False, key=lambda v: (v.f(n, GoalState), len(v.direction))) #  Returns the node with the less f(n) and then Up, Down, Left, Right
    return openlist[0]


def generateGoalState(n):
    GoalState=[]
    for x in range(np.power(n, 2)):
        GoalState.append(x + 1)
    GoalState[np.power(n, 2) - 1] = 0
    return GoalState







#  minNode = openlist[0];
 # for v in openlist:
    #     if minNode.f(n) > v.f(n):
    #         minNode = v
""" if minNode.f(n) == v.f(n):
    if minNode.direction == "Up" """