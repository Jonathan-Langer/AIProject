
import numpy as np
import heapq
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
    heapq.heappush(OpenList, root) #min heap
    OpenList.append(root)
    CloseList = []

    while len(OpenList) > 0:
        curr_node = OpenList.pop(0)
        children = curr_node.discoverChildren(n)

        if curr_node.isGoal(GoalState):
            return curr_node.solution(), len(CloseList)

        #min_node = minV(curr_node.discoverChildren(n), n, GoalState)  # returns the node with the min f(n) from curr_node children
        for node in children:
            if node.isGoal(GoalState):
                return node.solution(), len(CloseList)
            if node.state not in CloseList and not isExist(OpenList, node):
                heapq.heappush(OpenList, node)
        CloseList.append(curr_node.state)
    return

# A star  isExist() is a help func checks if node exist in open list and if it does,
# update the g() value (cost from root value) if it is necessary
def isExist(openlist, v):
    if len(openlist) == 0:
        return False
    flag = False
    for i, node in enumerate(openlist):
        if v == node:
            if v.g() < openlist[i].g():
                openlist[i].cost = v.g() + 1
                openlist[i].pai = v
                flag = True
    return flag




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