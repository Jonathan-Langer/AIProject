import sys

import numpy as np
from Vertex import Vertex


#The first search algorithm is: BFS - Breath First Search
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
        CloseList.append(current_node.state) #the CloseList is list of states (matrix) the represents the board state of the current node

        children = current_node.discoverChildren(n) #discoverChildren returnes a list of all the children of the current node

        for child in children:
            if child.state in CloseList or child in OpenList:
                children.remove(child)

        for child in children:
            if child.state not in CloseList:
                if child.isGoal(GoalState):
                    return child.solution(), len(CloseList)
                OpenList.append(child)
    return



#The second search algorithm is: IDS - Iterative Depth Search
def IDS(initialState, n):
    GoalState=generateGoalState(n)
    root = Vertex(initialState, None, None, 0, 0)

    depth=0
    result=None
    while result == None: #While we didn't find the solution, we will increase the depth in 1
        result = deepthLimitedDFS(root, GoalState, depth, n)
        depth += 1
    return result

#HELP FUNCTION - This function is implementing the DFS search algorithm but runs until specific depth
def deepthLimitedDFS(start,GoalState,depth,n):
    openList = []
    openList.append(start)
    while True:
        if len(openList) == 0:
            return None
        curr_node = openList.pop(0)
        if curr_node.isGoal(GoalState):
            return curr_node.solution(), len(openList)
        elif curr_node.depth is not depth: #If we didn't reach to the maximum depth we can explore more and discover the children of the current node
                children = curr_node.discoverChildren(n)
                openList.extend(children)



#The third search algorithm is: A* - using the Manhattan distance as the heuristic function.
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

#isExist() is a help function that checks if node exist in the openlist and if it does,
#updates the cost (the cost of the route from the root) if it is necessary, i.e if the new cost of the route (from the root)
#is lower that the cost thar is written in the OpenList
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


#minHeuristic() is a help function that returnes a list wich includes the node and his index which has the lowest heuristic from the nodes in the OpenList
def minHeuristic(openlist):
    minH = sys.maxsize
    indexOfMinNode = 0
    for i, node in enumerate(openlist):
        if node.heuristic < minH:
            minH = node.heuristic
            indexOfMinNode = i
    result = [openlist[indexOfMinNode],indexOfMinNode]
    return result

#Function that generates the goalState according to n(one dimansion fron the size of the board)
def generateGoalState(n):
    GoalState=[]
    for x in range(np.power(n, 2)):
        GoalState.append(x + 1)
    GoalState[np.power(n, 2) - 1] = 0
    return GoalState

#Function that calculates the total heuristic value of a given node
#node.g() returnes the cost of the route from the root to the current node
#node.h(n) returnes the Manhattan Distance from the state of the current node (that is invoking the function) and the goal state.
def heuristicFunc(node, n):
    return node.g() + node.h(n)