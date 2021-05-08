
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
