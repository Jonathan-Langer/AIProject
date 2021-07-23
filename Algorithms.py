
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
    heapq.heappush(OpenList, root) #min heap
    heapq.heapify(OpenList)
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
                heapq.heapify(OpenList)
        CloseList.append(curr_node.state)
    return

#isExist() is a help func that checks if node exist in open list and if it does,
#update the g() value (cost from root value) if it is necessary
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
