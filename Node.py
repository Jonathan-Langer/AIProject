import numpy as np
import copy

global N #the size of the board

class Node:
    children=[]
    puzzle = []
    #parent = Node()
    x = 0

    def __init__(self, p, parent):
        self.setPuzzle(p)
        self.parent = parent()


    def setPuzzle (self, p):
        self.puzzle=copy(copy(p))

    def goalState(self):
        isGoal = True
        m = self.puzzle[0]
        for i in range(len(self.p)):
            if m > self.puzzle[i]:
                isGoal = False
            m = self.puzzle[i]
        return isGoal

    def MoveToRight(self, p, position):
        if(position % N < N -1):
            pc = []
            self.copyPuzzle(pc,p)
            temp = pc[position - 1]
            pc[position  - 1] = pc[position]
            pc[position] = temp

            child = Node(pc)
            self.children.append(child)
            child.parent = self

    def MoveToLeft(self, p, position):
        if( position % N > 0):
            pc = []
            self.copyPuzzle(pc ,p)
            temp = pc[position - 1]
            pc[position - 1] = pc[position]
            pc[position] = temp

            child = Node(pc)
            self.children.append(child)
            child.parent = self

    def MoveToUp(self, p, position):
        if position - N >= 0:
            pc=[]
            self.copyPuzzle(pc, p)
            temp=pc[position - 3]
            pc[position - 3] = pc[position]
            pc[position] = temp

            child = Node(pc)
            self.children.append(child)
            child.parent = self

    def MoveToDown(self, p, position):
        if position  + N < len(self.puzzle):
            pc = []
            self.copyPuzzle(pc,p)
            temp=pc[position + 3]
            pc[position + 3] = pc[position]
            pc[position] = temp

            child = Node(pc)
            self.children.append(child)
            child.parent = self

    def printPuzzle(self):
        print("\n")
        m = 0
        for i in range(N):
            for j in range(N):
                print(str(self.puzzle[m]) + " " + "\n")
                m = m + 1
            print("\n")

    def isSamePuzzle(self, p):
        samePuzzle = True
        for i in range(len(p)):
            if self.puzzle[i] != p[i]:
                samePuzzle = False
        return samePuzzle

    def discoverChildren(self):
        for i in range(len(self.puzzle)):
            if self.puzzle[i] == 0:
                x = i
        self.MoveToUp(self.puzzle, self.x)
        self.MoveToDown(self.puzzle, self.x)
        self.MoveToLeft(self.puzzle, self.x)
        self.MoveToRight(self.puzzle, self.x)


    def copyPuzzle(self, a ,b):
        for i in range(len(b)):
            a[i] = b[i]
