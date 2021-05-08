import queue
from inspect import v

from Vertex import Vertex
from queue import Queue


def BFS(initialState, n):
    root = Vertex(initialState, None, None, 0, 0)
    if root.isGoal():
        return root.solution()
    OpenList = []
    OpenList.append(root)
    CloseList = []

    while not (len(OpenList) == 0):
        current_node = OpenList.pop(0)

        children = current_node.discoverChildren(n)
        CloseList.append(current_node.state)

        for child in children:
            if child.state not in CloseList:
                if child.isGoal():
                    return child.solution(), len(CloseList)
                OpenList.append(child)
    return


def aStar(initialState, n):
    root = Vertex(initialState, None, None, 0, 0)
    if root.isGoal():
        return root.solution()
    OpenList = []
    OpenList.append(root)
    CloseList = []
    while len(OpenList) > 0:
        curr_node = OpenList.pop(0)
        if curr_node.isGoal():
            return curr_node.solution(), len(CloseList)
        min_node = minV(curr_node.discoverChildren(n), n)  # returns the node with the min f(n) from curr_node children
        CloseList.append(curr_node.state)
        if min_node.state not in CloseList:
            if min_node.isGoal():
                return min_node.solution(), len(CloseList)
            else:
                OpenList.append(min_node)
    return


def minV(openlist, n):
    openlist.sort(reverse=False, key=lambda v: (v.f(n), len(v.direction))) #  Returns the node with the less f(n) and then Up, Down, Left, Right
    return openlist[0]









#  minNode = openlist[0];
 # for v in openlist:
    #     if minNode.f(n) > v.f(n):
    #         minNode = v
""" if minNode.f(n) == v.f(n):
    if minNode.direction == "Up" """