import numpy as np
import Node

class UninformedSearch:


    def BFS(self, root):
        pathToSolution = []
        OpenList = []
        ClosedList = []

        OpenList.append(root)
        goalFound = False
        while len(OpenList) > 0 and not (goalFound):
            currentNode = Node()
            currentNode = OpenList[0]
            #OpenList.append(currentNode)
            ClosedList.append(currentNode)
            OpenList.pop(0)
            currentNode.discoverChildren()

            for i in range(len(currentNode.children)):
                currentChild =currentNode.children[i]
                if currentChild.goalState() == True:
                    print("Goal Found ")
                    goalFound = True
                    #print Trace
                    self.PathTrace(pathToSolution, currentChild)

                if not(self.Contains(OpenList, currentChild)) and (not(self.Contains(ClosedList, currentChild))):
                    OpenList.append(currentChild)
        return pathToSolution

    def PathTrace(self, path, n):
        print("Printing Path \n")
        current = n
        path.append(current)
        while current.parent != None:
            current = current.parent
            path.append(current)



    def Contains(self, list, node):
        contains = False
        for i in range(len(list)):
            if list[i].isSamePuzzle():
                contains = True
        return contains