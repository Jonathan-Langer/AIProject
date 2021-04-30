import copy

import numpy as np
from collections import defaultdict
from Vertex import Vertex


class Graph:
    E = []
    V = []
    GoalState = []

    # Ctor
    def __init__(self, v, mat):
        self.initial_gs(mat)
        self.vGoalState = Vertex(copy.copy(self.GoalState))

    def build_graph(self, v):  # Recursive function to build the Graph
        if self.is_goal_state(v):  # Stop condition
            self.add_v(v)
            return
        if self.is_exist(v):
            return
        else:
            self.add_v(v)
            v.find_zero()  # Initial the current index of zero in this.v matrix
            if v.is_up():  # Checks if there is a way up in the matrix
                u = Vertex(copy.copy(v.mat))
                u = u.up()
                self.add_edge(v, u)  # Add edge, and initial u.pai = v, v.adj.append(u)
                self.build_graph(u)  # Recursive call

            if v.is_down():
                u = Vertex(copy.copy(v.mat))
                u = u.down()
                self.add_v(v)
                self.add_edge(v, u)
                self.build_graph(u)

            if v.is_right():
                u = Vertex(copy.copy(v.mat))
                u = u.right()
                self.add_edge(v, u)
                self.build_graph(u)

            if v.is_left():
                u = Vertex(copy.copy(v.mat))
                u = u.left()
                self.add_edge(v, u)
                self.build_graph(u)
        return self

    def add_edge(self, v, u):  # Add edge
        self.E.append([v, u])
        v.adj.append(u)
        u.pai = v

    def add_v(self, v):  # Add vertex
        self.V.append(v)

    def is_exist(self, v):  # Function which check if v is in the graph list
        for v1 in range(len(self.V)):
            if self.V[v1] == v:  # Operator '==' in V's class
                return True
        return False

    def is_goal_state(self, v):  # Checks is current vertex is GoalState
        if v == self.vGoalState:
            return True
        else:
            return False

    def initial_gs(self, mat):  # Initial this variable to be GoalState matrix
        for x in range(np.power(len(mat), 2)):
            self.GoalState.append(x + 1)
        self.GoalState[np.power(len(mat), 2) - 1] = 0
        self.GoalState = np.array(self.GoalState)
        self.GoalState = np.hsplit(self.GoalState, len(mat))
        self.GoalState = np.asmatrix(self.GoalState)

    # def move_zero(self, size):
    #     self.GoalState[0, 0], self.GoalState[size-1, size-1] = self.GoalState[size-1, size-1], self.GoalState[0, 0]
    #     return self.GoalState
